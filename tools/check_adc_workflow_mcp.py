"""Replay the ADC workflow and optional isolated compilation through actual MCP.

Hardware facts come from MCP responses. This client never reads manuals/headers,
calls a compiler itself, or attaches to a board. Raw responses remain local.
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


def value(response):
    if response.structuredContent is not None:
        data = response.structuredContent
        return data['result'] if set(data) == {'result'} else data
    raw = '\n'.join(b.text for b in response.content if b.type == 'text')
    try:
        return json.loads(raw)
    except ValueError:
        return raw


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

    knowledge = StdioServerParameters(command=sys.executable,
        args=['-m', 'praxis', 'serve', '--bundle', str(args.bundle.resolve())],
        cwd=str(output), env=env)
    async with stdio_client(knowledge) as (reader, writer), ClientSession(reader, writer) as client:
        initialized = await client.initialize()
        revision = re.search(r'Session bundle revision: ([0-9a-f]{64})', initialized.instructions or '')
        if revision is None:
            raise RuntimeError('Knowledge MCP did not advertise its immutable revision')
        revision = revision[1]
        names = sorted(t.name for t in (await client.list_tools()).tools)
        checks['three_readonly_tools'] = names == [
            'query_schematic_netlist', 'read_peripheral_doc', 'read_wiki_index']
        error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': 'adc'})
        checks['index_gate'] = error and 'PREREQUISITE_REQUIRED' in str(text)
        error, index = await call(client, 'knowledge', 'read_wiki_index', {})
        if error or not isinstance(index, str):
            raise RuntimeError('MCP index unavailable')
        checks['adc_publication_gate'] = bool(re.search(r'\| adc1_internal_reference \| True \|', index))
        checks['feature_adc_gate'] = bool(re.search(r'\| feature_adc \| True \|', index))
        checks['flash_programming_blocked'] = bool(re.search(r'\| feature_flash \| False \|', index))
        checks['explicit_mode_route'] = all(key in index for key in (
            'adc/single_conversion', 'adc_common/internal_reference_prescale4',
            'tim/polling_update_delay', 'rcc/adc_timer_gates', 'rcc/pll_hse8_168mhz'))

        async def document(entity, active=()):
            if entity in documents:
                return
            if entity in active or len(active) > 64:
                raise RuntimeError('Invalid dependency route from MCP')
            error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': entity})
            if error and 'PREREQUISITE_REQUIRED' in str(text):
                match = re.search(r'retrieve in order: ([a-z0-9_, ]+)', str(text))
                if match:
                    for parent in match[1].strip().split(', '):
                        await document(parent, (*active, entity))
                    error, text = await call(client, 'knowledge', 'read_peripheral_doc', {'peripheral_name': entity})
            if error or not isinstance(text, str):
                raise RuntimeError(f'Cannot retrieve {entity}')
            documents[entity] = text

        for entity in ('adc', 'tim'):
            await document(entity)
        checks['complete_reviewed_documents'] = all('## Reviewed operating modes' in documents[n]
            and '## Register map' in documents[n] and '## Bit fields' in documents[n]
            for n in ('adc', 'adc_common', 'tim', 'rcc', 'flash', 'pwr'))
        checks['adc1_internal_only_scope'] = ('single_conversion' in documents['adc'] and
            'ADC1 only' in documents['adc'] and 'ADC2/ADC3' in documents['adc'])
        checks['side_effects_retained'] = ('read DR clears' in documents['adc'] and
            'stale UG' in documents['tim'] and 'not W1C' in documents['tim'])
        checks['gate_conflict_resolved'] = ('eb6911d964b1cf8a' in documents['rcc'] and
            'st_adc_gate' in documents['rcc'])

    build_result = None
    if args.source_directory:
        build = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
            '--bundle', str(args.bundle.resolve()), '--assets', str(args.assets.resolve()),
            '--workspace', str(args.workspace.resolve()), '--artifacts', str(args.artifacts.resolve()),
            '--lock', str(args.lock.resolve())], cwd=str(output), env=env)
        async with stdio_client(build) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            names = sorted(t.name for t in (await client.list_tools()).tools)
            checks['build_without_hardware_tools'] = names == [
                'build_firmware', 'get_build_profile', 'validate_firmware']
            error, profile = await call(client, 'build', 'get_build_profile', {})
            if error:
                raise RuntimeError('Build profile unavailable')
            checks['matching_bundle_pair'] = profile['bundle_revision'] == revision
            if not checks['matching_bundle_pair']:
                raise RuntimeError('Knowledge/build bundle mismatch')
            error, build_result = await call(client, 'build', 'build_firmware',
                                            {'source_directory': args.source_directory})
            checks['target_compilation'] = (not error and build_result.get('compile_passed') is True
                                            and build_result.get('image_validated') is True)
            if checks['target_compilation']:
                error, validated = await call(client, 'build', 'validate_firmware',
                                               {'artifact_id': build_result['artifact_id']})
                checks['artifact_revalidated'] = not error and validated.get('validation', {}).get('valid') is True

    (output / 'responses.json').write_text(json.dumps(trace, indent=2, sort_keys=True) + '\n')
    report = dict(format='praxis-adc-mcp-replay-v1', passed=all(checks.values()), checks=checks,
                  tool_calls=len(trace), bundle_revision=revision, hardware_operations=0,
                  all_mcu_features_supported=False,
                  firmware_build=build_result,
                  limits=['No external model or physical test.',
                          'Compilation is separate from runtime peripheral qualification.',
                          'ADC scope is one internal-reference mode; supply, timing and physical behavior remain unqualified.'])
    (output / 'report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'firmware_build'}, indent=2))
    return 0 if report['passed'] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-directory')
    parser.add_argument('--workspace', type=Path, default=Path('examples'))
    parser.add_argument('--assets', type=Path, default=Path('assets/stm32f407vg'))
    parser.add_argument('--artifacts', type=Path, default=Path('.praxis-output/firmware-artifacts'))
    parser.add_argument('--lock', type=Path, default=Path('toolchain-f407.lock.json'))
    args = parser.parse_args()
    return asyncio.run(asyncio.wait_for(run(args), timeout=180))


if __name__ == '__main__':
    raise SystemExit(main())
