"""Demonstrate the LED/button build/plan/flash pipeline through actual MCP calls.

prepare: retrieve knowledge, build in the isolated service and inspect/plan only.
execute: consume an independently approved grant; one flash, verify, one reset/run.
No grant is created here. Failures stop the pipeline; no automatic programming retry.
Raw logs contain device identifiers and remain in the private output directory.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from datetime import UTC, datetime
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.programming import Authorization, checked_plan

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-m1'


def save(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        json.dump(data, handle, sort_keys=True, indent=2)
        handle.write('\n')


async def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False, mode=0o700)
    fd = os.open(output / 'events.jsonl', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as log:
        async def call(client, tool, arguments):
            def record(data):
                log.write(json.dumps({'at': datetime.now(UTC).isoformat(), **data}, sort_keys=True) + '\n')
                log.flush()
            record(dict(phase='request', tool=tool, arguments=arguments))
            print(f'MCP → {tool}', flush=True)
            response = await client.call_tool(tool, arguments)
            record(dict(phase='response', tool=tool, response=response.model_dump(mode='json')))
            if response.isError:
                raise RuntimeError(f'{tool} failed; inspect the recorded response; do not retry a write')
            if response.structuredContent:
                data = response.structuredContent
                return data['result'] if set(data) == {'result'} else data
            text = '\n'.join(block.text for block in response.content if block.type == 'text')
            try:
                return json.loads(text)
            except ValueError:
                return text

        # Knowledge retrieval always uses the same bundle as the build/hardware profile.
        params = StdioServerParameters(command=sys.executable,
            args=['-m', 'praxis', 'serve', '--bundle', str(args.bundle.resolve())], cwd=str(output))
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            index = await call(client, 'read_wiki_index', {})
            if 'stm32f407g_disc1_mb997_e01' not in index:
                raise RuntimeError('Wrong knowledge bundle')
            for signal in args.signals:
                result = await call(client, 'query_schematic_netlist', {'query_target': signal})
                if 'No match' in str(result):
                    raise RuntimeError('Required topology is not published')
            # The caller names its requirements; routing comes from actual MCP errors.
            served = set()
            async def document(entity, active=()):
                if entity in served:
                    return
                if entity in active or len(active) > 64:
                    raise RuntimeError('Invalid prerequisite route')
                response = await client.call_tool('read_peripheral_doc', {'peripheral_name': entity})
                log.write(json.dumps(dict(phase='response', tool='read_peripheral_doc',
                    arguments={'peripheral_name': entity}, response=response.model_dump(mode='json')),
                    sort_keys=True) + '\n')
                log.flush()
                raw = '\n'.join(block.text for block in response.content if block.type == 'text')
                if response.isError:
                    match = re.search(r'retrieve in order: ([a-z0-9_, ]+)', raw)
                    if 'PREREQUISITE_REQUIRED' not in raw or not match:
                        raise RuntimeError('Document unavailable; inspect MCP evidence')
                    for prerequisite in match[1].strip().split(', '):
                        await document(prerequisite, (*active, entity))
                    raw = await call(client, 'read_peripheral_doc', {'peripheral_name': entity})
                if '## Reviewed operating semantics' not in raw or 'Not reviewed.' in raw:
                    raise RuntimeError('Required document has no reviewed operating semantics')
                served.add(entity)
            for entity in args.peripherals:
                await document(entity)

        server_args = ['-m', 'praxis', 'build-serve', '--bundle', str(args.bundle.resolve()),
            '--assets', str(ROOT / 'assets/stm32f407vg'), '--workspace', str(ROOT / 'examples'),
            '--artifacts', str(ROOT / '.praxis-output/firmware-artifacts'),
            '--lock', str(ROOT / 'toolchain-f407.lock.json'),
            '--hardware-profile', str(args.hardware_profile.resolve())]
        grant = None
        if args.mode == 'execute':
            if not args.authorization:
                raise RuntimeError('execute requires an operator-approved --authorization file')
            grant = Authorization.model_validate_json(args.authorization.read_bytes())
            if set(grant.actions) != {'flash', 'reset_run'} or grant.max_flash_attempts != 1:
                raise RuntimeError('This demonstration requires exactly one flash plus reset_run scope')
            server_args += ['--hardware-authorization', str(args.authorization.resolve())]
        params = StdioServerParameters(command=sys.executable, args=server_args, cwd=str(output),
                                      env=dict(os.environ))
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            profile = await call(client, 'get_build_profile', {})
            save(output / 'build-profile.json', profile)
            if args.mode == 'prepare':
                build = await call(client, 'build_firmware', {
                    'source_directory': args.source_directory})
                save(output / 'build.json', build)
                if not build.get('compile_passed') or not build.get('image_validated'):
                    raise RuntimeError('Build/image validation failed; no hardware write requested')
                artifact = build['artifact_id']
            else:
                artifact = grant.plan.artifact_id
            validation = await call(client, 'validate_firmware', {'artifact_id': artifact})
            if not validation['validation']['valid']:
                raise RuntimeError('Artifact validation failed')
            save(output / 'validation.json', validation)
            probes = await call(client, 'list_debug_probes', {})
            if not any(p['serial'] == args.probe_serial and p['selectable'] for p in probes['probes']):
                raise RuntimeError('Selected probe is not connected; no fallback selection')
            target = await call(client, 'inspect_target', {'probe_serial': args.probe_serial})
            save(output / 'target.json', target)
            connection = target['connection_id']
            before = await call(client, 'inspect_execution', {'connection_id': connection})
            save(output / 'before.json', before)
            binding = {'artifact_id': artifact, 'connection_id': connection}
            plan = checked_plan(await call(client, 'plan_firmware', binding))
            save(output / 'plan.json', plan.model_dump())
            if args.mode == 'prepare':
                summary = {'prepared': True, 'artifact_id': artifact,
                           'image_bytes': plan.image_length, 'erase_bytes': plan.erase_length,
                           'erase_start': hex(plan.erase_start), 'last_sector': plan.last_sector,
                           'physical_revision': plan.physical_board_revision,
                           'mutating_operations': 0}
            else:
                if plan != grant.plan:
                    raise RuntimeError('Fresh target/artifact plan differs from the approved scope')
                flash = await call(client, 'flash_firmware', binding)
                save(output / 'flash.json', flash)
                if not flash.get('success') or not flash.get('readback_verified') or flash.get('execution_state') != 'halted':
                    save(output / 'summary.json', {'passed': False, 'phase': 'flash', 'run_id': flash.get('run_id')})
                    raise RuntimeError('Flash failed or uncertain; stopped without retry or reset/run')
                control = await call(client, 'control_execution', {
                    **binding, 'operation': 'reset_run', 'observation_ms': 1000})
                save(output / 'reset-run.json', control)
                if not control.get('success') or not control.get('readback_verified') or control.get('execution_state') != 'running':
                    raise RuntimeError('Execution control failed; stopped without retry')
                after = await call(client, 'inspect_execution', {'connection_id': connection})
                save(output / 'after.json', after)
                summary = {'passed': True, 'artifact_id': artifact, 'flash_run_id': flash['run_id'],
                           'control_run_id': control['run_id'], 'readback_verified': True,
                           'flash_state': flash['execution_state'], 'reset_run_state': control['execution_state'],
                           'programmed_bytes': plan.image_length, 'erased_bytes': plan.erase_length,
                           'physical_behavior': 'Awaiting actual human observations; no optical/timing measurement'}
            save(output / 'summary.json', summary)
            print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('prepare', 'execute'))
    parser.add_argument('--probe-serial', required=True)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--authorization', type=Path)
    parser.add_argument('--bundle', type=Path, default=BUNDLE)
    parser.add_argument('--hardware-profile', type=Path,
                        default=ROOT / '.praxis-output/hardware-profile.json')
    parser.add_argument('--source-directory',
                        default='stm32f407g-disc1-led-button/validated_opencode_application')
    parser.add_argument('--signals', nargs='+', default=['LED_A', 'LED_B', 'USER_BUTTON'])
    parser.add_argument('--peripherals', nargs='+', default=['rcc', 'gpio'])
    args = parser.parse_args()
    try:
        asyncio.run(asyncio.wait_for(run(args), timeout=120))
    except Exception as exc:
        def report(error):
            if isinstance(error, BaseExceptionGroup):
                for child in error.exceptions:
                    report(child)
            else:
                print(f'{type(error).__name__}: {error}', file=sys.stderr)
        report(exc)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
