"""Exercise knowledge routing, isolated build and project reporting over real MCP.

No hardware tools are enabled. A project specification supplies the requested
scope; hardware knowledge is retrieved from the selected server, never inferred.
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
    result = response.structuredContent
    if result is not None:
        return result['result'] if set(result) == {'result'} else result
    text = '\n'.join(c.text for c in response.content if c.type == 'text')
    try:
        return json.loads(text)
    except ValueError:
        return text


async def run(args):
    from praxis.project_report import parse_spec
    spec = parse_spec(args.spec.read_bytes())
    args.evidence.mkdir(parents=True, exist_ok=False)
    trace = []

    async def call(client, tool, arguments):
        response = await client.call_tool(tool, arguments)
        trace.append({'tool': tool, 'arguments': arguments, 'response': response.model_dump(mode='json')})
        (args.evidence / 'mcp-trace.json').write_text(json.dumps(trace, sort_keys=True, indent=2) + '\n')
        print(f'{tool}: {"error" if response.isError else "success"}', flush=True)
        return response, value(response)

    env = dict(os.environ)
    base = ['-m', 'praxis']
    knowledge = StdioServerParameters(command=sys.executable,
        args=[*base, 'serve', '--bundle', str(args.bundle.resolve())], env=env)
    async with stdio_client(knowledge) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        response, text = await call(client, 'read_peripheral_doc', {'peripheral_name': 'usart'})
        if not response.isError or 'PREREQUISITE_REQUIRED' not in str(text):
            raise RuntimeError('Fresh-session knowledge gate did not block retrieval')
        response, index = await call(client, 'read_wiki_index', {})
        if response.isError or spec.target_id not in str(index):
            raise RuntimeError('Knowledge server returned the wrong target')
        queries = list(dict.fromkeys([*spec.signals,
            *(endpoint for w in spec.proposed_wires for endpoint in (w.from_endpoint, w.to_endpoint))]))
        for query in queries:
            response, text = await call(client, 'query_schematic_netlist', {'query_target': query})
            if response.isError or 'No match' in str(text):
                raise RuntimeError(f'Unresolved scenario topology: {query}')
        served = set()

        async def document(entity, active=()):
            if entity in served:
                return
            if entity in active or len(active) > 64:
                raise RuntimeError('Cyclic or excessive dependency route')
            response, text = await call(client, 'read_peripheral_doc', {'peripheral_name': entity})
            if response.isError:
                missing = re.search(r'retrieve in order: ([a-z0-9_, ]+)', str(text))
                if missing is None:
                    raise RuntimeError(str(text))
                for parent in missing[1].strip().split(', '):
                    await document(parent, (*active, entity))
                response, text = await call(client, 'read_peripheral_doc', {'peripheral_name': entity})
            if response.isError:
                raise RuntimeError(str(text))
            served.add(entity)
        for key in dict.fromkeys(key for item in [*spec.explanations, *spec.diagrams] for key in item.documents):
            if key.startswith('peripherals/'):
                await document(key.removeprefix('peripherals/'))

    build = StdioServerParameters(command=sys.executable, args=[*base, 'build-serve',
        '--bundle', str(args.bundle.resolve()), '--assets', str(args.assets.resolve()),
        '--workspace', str(args.workspace.resolve()), '--artifacts', str(args.artifacts.resolve()),
        '--lock', str(args.lock.resolve()), '--project-reports', str(args.reports.resolve())], env=env)
    async with stdio_client(build) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        tools = {t.name for t in (await client.list_tools()).tools}
        if tools != {'get_build_profile', 'build_firmware', 'validate_firmware', 'generate_project_report'}:
            raise RuntimeError('Unexpected build tools; hardware access must remain disabled')
        response, profile = await call(client, 'get_build_profile', {})
        if (response.isError or profile['target']['id'] != spec.target_id
                or profile['bundle_revision'] != spec.bundle_revision):
            raise RuntimeError('Build server target/bundle mismatch')
        response, artifact = await call(client, 'build_firmware', {'source_directory': args.source})
        if response.isError or not artifact['compile_passed'] or not artifact['image_validated']:
            raise RuntimeError(f'Build was not accepted: {artifact}')
        response, checked = await call(client, 'validate_firmware', {'artifact_id': artifact['artifact_id']})
        if response.isError or not checked['validation']['valid']:
            raise RuntimeError(f'Artifact validation failed: {checked}')
        response, report = await call(client, 'generate_project_report',
            {'specification': spec.model_dump(), 'artifact_id': artifact['artifact_id']})
        if response.isError:
            raise RuntimeError(str(report))
        summary = {'knowledge_tools_exercised': True, 'build_checked': True,
            'artifact_id': artifact['artifact_id'], 'report': report, 'hardware_operations': 0,
            'physical_verification': 'not_assessed'}
        (args.evidence / 'summary.json').write_text(json.dumps(summary, sort_keys=True, indent=2) + '\n')
        print(json.dumps(summary, sort_keys=True, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ('bundle', 'assets', 'workspace', 'artifacts', 'lock', 'reports', 'spec', 'evidence'):
        parser.add_argument('--' + flag, type=Path, required=True)
    parser.add_argument('--source', required=True, help='Existing application C/H directory relative to workspace')
    asyncio.run(asyncio.wait_for(run(parser.parse_args()), timeout=120))


if __name__ == '__main__':
    main()
