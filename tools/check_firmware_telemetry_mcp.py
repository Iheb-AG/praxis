"""Read one explicitly selected firmware's telemetry through real stdio MCP.

Saves private target/plan/events files. Never builds, flashes, resets, halts or
generates authorization. --expect-mismatch tests the old-image guard before flash.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.programming import checked_plan

ROOT = Path(__file__).resolve().parents[1]


def save(path, data):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        json.dump(data, handle, sort_keys=True, indent=2)
        handle.write('\n')


async def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False, mode=0o700)
    serial = args.probe_serial
    if args.probe_from_plan:
        serial = checked_plan(json.loads(args.probe_from_plan.read_text())).probe_serial
    server_args = ['-m', 'praxis', 'build-serve',
                   '--bundle', str(args.bundle.resolve()),
                   '--assets', str(ROOT / 'assets/stm32f407vg'),
                   '--workspace', str(ROOT / 'examples'),
                   '--artifacts', str(ROOT / '.praxis-output/firmware-artifacts'),
                   '--lock', str(ROOT / 'toolchain-f407.lock.json'),
                   '--hardware-profile', str(args.hardware_profile.resolve()),
                   '--telemetry-artifact', args.artifact,
                   '--telemetry-kind', args.telemetry_kind]
    params = StdioServerParameters(command=sys.executable, args=server_args,
                                   cwd=str(output), env=dict(os.environ))
    fd = os.open(output / 'events.jsonl', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as log:
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()

            async def call(name, arguments, expect_error=False):
                print(f'MCP → {name}', flush=True)
                response = await client.call_tool(name, arguments)
                log.write(json.dumps({'tool': name, 'arguments': arguments,
                                      'response': response.model_dump(mode='json')}, sort_keys=True) + '\n')
                log.flush()
                text = '\n'.join(block.text for block in response.content if block.type == 'text')
                if response.isError:
                    if expect_error and 'READBACK_MISMATCH:' in text:
                        return {'expected_error': 'READBACK_MISMATCH'}
                    raise RuntimeError(f'{name} failed; see private events.jsonl')
                if expect_error:
                    raise RuntimeError('Expected the old-image guard to reject this request; it succeeded')
                data = response.structuredContent
                if data is None:
                    data = json.loads(text)
                return data['result'] if isinstance(data, dict) and set(data) == {'result'} else data

            listing = await client.list_tools()
            tools = {tool.name: tool for tool in listing.tools}
            if 'read_firmware_telemetry' not in tools or 'flash_firmware' in tools or 'control_execution' in tools:
                raise RuntimeError('Required read-only telemetry tool set was not discovered')
            if args.can_diagnostics and 'read_can_diagnostics' not in tools:
                raise RuntimeError('Fixed CAN diagnostic tool was not discovered')
            save(output / 'tools.json', listing.model_dump(mode='json'))
            profile = await call('get_build_profile', {})
            save(output / 'build-profile.json', profile)
            if profile['firmware_telemetry']['kind'] != args.telemetry_kind:
                raise RuntimeError('Telemetry contract differs from launch selection')
            probes = await call('list_debug_probes', {})
            if not any(p['serial'] == serial and p['selectable'] for p in probes['probes']):
                raise RuntimeError('Selected probe is not connected; no fallback selection')
            target = await call('inspect_target', {'probe_serial': serial})
            save(output / 'target.json', target)
            connection = target['connection_id']
            plan = checked_plan(await call('plan_firmware', {'artifact_id': args.artifact,
                                                           'connection_id': connection}))
            save(output / 'plan.json', plan.model_dump())
            observations = []
            for index in range(args.windows):
                tool = 'read_can_diagnostics' if args.can_diagnostics else 'read_firmware_telemetry'
                arguments = {'connection_id': connection}
                if not args.can_diagnostics:
                    arguments.update(samples=args.samples, interval_ms=args.interval_ms)
                result = await call(tool, arguments, expect_error=args.expect_mismatch)
                save(output / f'observation-{index:02d}.json', result)
                observations.append(result)
            summary = {'artifact_id': args.artifact, 'image_bytes': plan.image_length,
                       'erase_start': hex(plan.erase_start), 'erase_bytes': plan.erase_length,
                       'last_sector': plan.last_sector,
                       'physical_revision': plan.physical_board_revision,
                       'mutating_operations': 0, 'windows': len(observations),
                       'expected_image_mismatch_observed': args.expect_mismatch,
                       'assessments': [row['assessment'] for row in observations if 'assessment' in row],
                       'can_states': [row['can_state'] for row in observations if 'can_state' in row]}
            save(output / 'summary.json', summary)
            print(json.dumps(summary, indent=2, sort_keys=True), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', required=True)
    parser.add_argument('--output', required=True, type=Path)
    probes = parser.add_mutually_exclusive_group(required=True)
    probes.add_argument('--probe-serial')
    probes.add_argument('--probe-from-plan', type=Path)
    parser.add_argument('--bundle', type=Path, default=ROOT / 'bundles/stm32f407g-disc1-e01-uart-v1')
    parser.add_argument('--hardware-profile', type=Path,
                        default=ROOT / '.praxis-output/hardware-profile-uart.json')
    parser.add_argument('--expect-mismatch', action='store_true')
    parser.add_argument('--can-diagnostics', action='store_true',
                        help='Use named read-only CAN acknowledgement diagnostics instead of sample windows')
    parser.add_argument('--telemetry-kind', choices=('uart-loopback-v1', 'can-loopback-v1'),
                        default='uart-loopback-v1')
    parser.add_argument('--windows', type=int, choices=range(1, 11), default=1)
    parser.add_argument('--samples', type=int, choices=range(1, 6), default=2)
    parser.add_argument('--interval-ms', type=int, choices=range(10, 1001), default=100)
    args = parser.parse_args()
    if args.can_diagnostics and args.telemetry_kind != 'can-loopback-v1':
        parser.error('--can-diagnostics requires --telemetry-kind can-loopback-v1')
    try:
        asyncio.run(asyncio.wait_for(run(args), timeout=180))
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
