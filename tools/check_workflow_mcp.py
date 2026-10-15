"""Replay explicit workflow/mode contracts through real knowledge and build MCP.

The client obtains documents and prerequisite routes only through MCP. It does
not parse vendor sources, invoke a compiler itself or expose hardware tools.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from check_adc_workflow_mcp import value


async def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False, mode=0o700)
    trace, documents, checks = [], {}, {}
    env = {k: v for k, v in os.environ.items() if k != 'PRAXIS_HARDWARE_AUTHORIZATION'}

    async def call(client, server, name, arguments):
        response = await client.call_tool(name, arguments)
        trace.append(dict(server=server, tool=name, arguments=arguments,
                          response=response.model_dump(mode='json')))
        print(f'{server}: {name}: {"error" if response.isError else "response"}', flush=True)
        return bool(response.isError), value(response)

    connection = StdioServerParameters(command=sys.executable,
        args=['-m', 'praxis', 'serve', '--bundle', str(args.bundle.resolve())], cwd=str(output), env=env)
    async with stdio_client(connection) as (reader, writer), ClientSession(reader, writer) as client:
        initialized = await client.initialize()
        match = re.search(r'Session bundle revision: ([0-9a-f]{64})', initialized.instructions or '')
        if match is None:
            raise RuntimeError('Knowledge MCP did not advertise its immutable revision')
        revision = match[1]
        checks['three_readonly_tools'] = sorted(t.name for t in (await client.list_tools()).tools) == [
            'query_schematic_netlist', 'read_peripheral_doc', 'read_wiki_index']
        entities = list(dict.fromkeys([*args.peripheral, *(m.split('/')[0] for m in args.mode)]))
        error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': entities[0]})
        checks['index_gate'] = error and 'PREREQUISITE_REQUIRED' in str(text)
        error, index = await call(client, 'knowledge', 'read_wiki_index', {})
        if error or not isinstance(index, str):
            raise RuntimeError('Index unavailable')
        for signal in args.signal:
            error, topology = await call(client, 'knowledge', 'query_schematic_netlist',
                                         {'query_target': signal})
            checks[f'signal:{signal}'] = (not error and isinstance(topology, str)
                and '| ' in topology and 'no match' not in topology.lower())
        for name, expected in [(args.workflow, True), *((n, False) for n in args.blocked_workflow)]:
            checks[f'workflow:{name}:{expected}'] = bool(re.search(
                rf'^\| {re.escape(name)} \| {expected} \|', index, re.M))

        async def retrieve(entity, active=()):
            if entity in documents:
                return
            if entity in active or len(active) > 64:
                raise RuntimeError('Invalid MCP dependency route')
            error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': entity})
            if error and 'PREREQUISITE_REQUIRED' in str(text):
                route = re.search(r'retrieve in order: ([a-z0-9_, ]+)', str(text))
                if route:
                    for parent in route[1].strip().split(', '):
                        await retrieve(parent, (*active, entity))
                    error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': entity})
            if error or not isinstance(text, str):
                raise RuntimeError(f'Cannot retrieve {entity}: {text}')
            documents[entity] = text

        for entity in entities:
            await retrieve(entity)
        checks['complete_documents'] = all(
            '## Register map' in text and '## Bit fields' in text
            for text in documents.values())
        for requested in args.mode:
            entity, mode = requested.split('/')
            checks[f'mode:{requested}'] = bool(re.search(rf'^\| {re.escape(mode)} \|', documents[entity], re.M))
        for requested in args.forbid_register:
            entity, register = requested.split('/')
            checks[f'absent-register:{requested}'] = not re.search(
                rf'^\| {re.escape(register)} \| 0x[0-9A-F]+ \|', documents[entity], re.M)

    build_result = None
    if args.source_directory:
        connection = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
            '--bundle', str(args.bundle.resolve()), '--assets', str(args.assets.resolve()),
            '--workspace', str(args.workspace.resolve()), '--artifacts', str(args.artifacts.resolve()),
            '--lock', str(args.lock.resolve())], cwd=str(output), env=env)
        async with stdio_client(connection) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            checks['no_hardware_tools'] = sorted(t.name for t in (await client.list_tools()).tools) == [
                'build_firmware', 'get_build_profile', 'validate_firmware']
            error, profile = await call(client, 'build', 'get_build_profile', {})
            if error or profile.get('bundle_revision') != revision:
                raise RuntimeError('Knowledge/build bundle mismatch or unavailable profile')
            checks['matching_bundle_pair'] = True
            error, build_result = await call(client, 'build', 'build_firmware',
                                            {'source_directory': args.source_directory})
            checks['target_compilation'] = (not error and build_result.get('compile_passed') is True
                                            and build_result.get('image_validated') is True)
            if checks['target_compilation']:
                error, validated = await call(client, 'build', 'validate_firmware',
                                               {'artifact_id': build_result['artifact_id']})
                checks['artifact_revalidated'] = not error and validated.get('validation', {}).get('valid') is True
    report = dict(format='praxis-workflow-mcp-replay-v1', passed=all(checks.values()), checks=checks,
        workflow=args.workflow, bundle_revision=revision, tool_calls=len(trace),
        hardware_operations=0, firmware_build=build_result,
        limits=['Source/retrieval/compile checks do not establish physical behavior.',
                'Workflow readiness is limited to the exact published operating contracts.'])
    (output / 'responses.json').write_text(json.dumps(trace, indent=2, sort_keys=True) + '\n')
    (output / 'report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'firmware_build'}, indent=2))
    return 0 if report['passed'] else 1


def entity_mode(value):
    if not re.fullmatch(r'[a-z][a-z0-9_]*/[a-zA-Z][a-zA-Z0-9_]*', value):
        raise argparse.ArgumentTypeError('Use exact peripheral/mode or peripheral/REGISTER')
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--workflow', required=True)
    parser.add_argument('--blocked-workflow', action='append', default=[])
    parser.add_argument('--mode', type=entity_mode, action='append', default=[])
    parser.add_argument('--forbid-register', type=entity_mode, action='append', default=[])
    parser.add_argument('--peripheral', action='append', default=[])
    parser.add_argument('--signal', action='append', default=[],
                        help='Resolve an exact topology signal through knowledge MCP before the build')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-directory')
    parser.add_argument('--assets', type=Path, default=Path('assets/stm32f407vg'))
    parser.add_argument('--workspace', type=Path, default=Path('examples'))
    parser.add_argument('--artifacts', type=Path, default=Path('.praxis-output/firmware-artifacts'))
    parser.add_argument('--lock', type=Path, default=Path('toolchain-f407.lock.json'))
    args = parser.parse_args()
    if not args.mode and not args.peripheral:
        parser.error('Provide at least one --mode or --peripheral')
    if any(item.split('/')[0] not in {*args.peripheral, *(m.split('/')[0] for m in args.mode)}
           for item in args.forbid_register):
        parser.error('--forbid-register must refer to a requested document')
    try:
        return asyncio.run(asyncio.wait_for(run(args), timeout=240))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
