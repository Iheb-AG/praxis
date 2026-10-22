"""Bounded diagnostic sessions for validated project-owned MCP launch entries.

Only discovery, index retrieval and service descriptions are invoked. These fresh
sessions do not inspect a client's existing sessions or access a physical probe.
"""
import asyncio
import os
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.errors import PraxisError
from praxis.jsonio import load_json


REQUIRED = {
    'praxis': {'read_wiki_index', 'read_peripheral_doc', 'query_schematic_netlist'},
    'praxis_build': {'get_build_profile', 'build_firmware', 'validate_firmware', 'generate_project_report'},
    'praxis_ingest': {'get_ingestion_profile', 'publish_reviewed_bundle', 'activate_published_bundle'},
    'praxis_references': {'list_hardware_references', 'acquire_hardware_reference',
                          'search_hardware_reference', 'read_hardware_reference'},
}


def require(condition, code, message):
    if not condition:
        raise PraxisError(code, message)


def value(result):
    require(not result.isError, 'MCP_TOOL_ERROR', '\n'.join(
        c.text for c in result.content if c.type == 'text')[:1000])
    data = result.structuredContent
    if data is None:
        text = '\n'.join(c.text for c in result.content if c.type == 'text')
        try:
            data = load_json(text)
        except PraxisError as exc:
            if exc.code == 'INVALID_JSON':
                return text
            raise
    return data.get('result', data) if isinstance(data, dict) else data


async def inspect_session(session, name, bundle, selection, workspace):
    await session.initialize()
    names, cursor, seen = set(), None, set()
    for _ in range(32):
        page = await session.list_tools(cursor=cursor)
        for tool in page.tools:
            require(tool.name not in names, 'MCP_CATALOG_INVALID', 'Duplicate tool identity')
            names.add(tool.name)
        cursor = page.nextCursor
        if not cursor:
            break
        require(cursor not in seen, 'MCP_CATALOG_INVALID', 'Tool pagination repeated a cursor')
        seen.add(cursor)
    else:
        raise PraxisError('MCP_CATALOG_INVALID', 'Tool catalog exceeds diagnostic page limit')
    require(REQUIRED[name] <= names, 'MCP_TOOLS_MISSING',
            'Missing required tools: ' + ', '.join(sorted(REQUIRED[name] - names)))
    require(not {'flash_firmware', 'control_execution'} & names, 'UNEXPECTED_HARDWARE_AUTHORITY',
            'Project diagnostics expect launches without programming authorization')
    if name == 'praxis':
        result = value(await session.call_tool('read_wiki_index', {}))
        expected = (f'Praxis session bundle revision: `{selection.bundle_revision}`\n'
                    f'Handoff generation: {selection.generation}\n\n'
                    + bundle.read(bundle.manifest.documents['index']))
        require(result == expected, 'MCP_REVISION_MISMATCH', 'Knowledge index differs from selected bundle')
    elif name == 'praxis_build':
        result = value(await session.call_tool('get_build_profile', {}))
        require(isinstance(result, dict), 'MCP_RESPONSE_INVALID', 'Expected a build profile object')
        require(result.get('target') == bundle.manifest.target.model_dump()
                and result.get('bundle_revision') == selection.bundle_revision
                and result.get('bundle_handoff', {}).get('generation') == selection.generation,
                'MCP_REVISION_MISMATCH', 'Build service serves another target or selection')
        require(result.get('application_workspace') == str(workspace), 'PROJECT_PATH_MISMATCH',
                'Build service points to another workspace')
    elif name == 'praxis_ingest':
        result = value(await session.call_tool('get_ingestion_profile', {}))
        require(isinstance(result, dict), 'MCP_RESPONSE_INVALID', 'Expected an ingestion profile object')
        require(result.get('target') == bundle.manifest.target.model_dump()
                and result.get('bundle_handoff', {}).get('bundle_revision') == selection.bundle_revision
                and result.get('bundle_handoff', {}).get('generation') == selection.generation,
                'MCP_REVISION_MISMATCH', 'Ingestion service targets another project selection')
    else:
        result = value(await session.call_tool('list_hardware_references', {}))
        require(isinstance(result, dict) and isinstance(result.get('references'), list),
                'MCP_RESPONSE_INVALID', 'Expected the reference library inventory')
    return {'name': name, 'status': 'passed', 'tools': sorted(names)}


def failure(exc):
    # AnyIO wraps errors raised inside transport/task scopes. Preserve the useful
    # leaf code without leaking full stderr, stack traces or reference contents.
    if isinstance(exc, BaseExceptionGroup):
        return failure(exc.exceptions[0])
    return {'code': exc.code if isinstance(exc, PraxisError) else
            'MCP_TIMEOUT' if isinstance(exc, TimeoutError) else 'MCP_CONNECTION_FAILED',
            'detail': str(exc)[:1000] or type(exc).__name__}


async def inspect_services(entries, bundle, selection, workspace: Path, timeout: float):
    outcomes = []
    for name in REQUIRED:
        entry = entries[name]
        if not entry.get('enabled', True):
            outcomes.append({'name': name, 'status': 'disabled_by_project'})
            continue
        try:
            # One timeout covers startup, pagination and calls. Context managers
            # close sessions and reap temporary children on failure/cancellation.
            async with asyncio.timeout(timeout):
                with open(os.devnull, 'w') as stderr:
                    async with stdio_client(StdioServerParameters(command=entry['command'],
                            args=entry['args'], cwd=entry['cwd']), errlog=stderr) as (reader, writer):
                        async with ClientSession(reader, writer) as session:
                            outcome = await inspect_session(session, name, bundle, selection, workspace)
            outcomes.append(outcome)
        except Exception as exc:
            outcomes.append({'name': name, 'status': 'failed', **failure(exc)})
    return outcomes
