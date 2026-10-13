"""Batch actual ingestion MCP calls and preserve raw responses for review.

No local source reads except connection settings and the requested tool-call JSON.
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    commands = ['-m', 'praxis', 'ingest-serve']
    for flag in ('profile', 'catalog', 'archive_root', 'publication_root'):
        commands += ['--' + flag.replace('_', '-'), str(getattr(args, flag).resolve())]
    for archive in args.evidence_archive:
        commands += ['--evidence-archive', str(archive.resolve())]
    params = StdioServerParameters(command=sys.executable, args=commands,
                                  cwd=str(output), env=dict(os.environ))
    calls = json.loads(args.calls.read_text())
    failed = False
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        available = sorted(tool.name for tool in (await client.list_tools()).tools)
        (output / 'tools.json').write_text(json.dumps(available, indent=2) + '\n')
        for i, request in enumerate(calls):
            response = await client.call_tool(request['tool'], request.get('arguments', {}))
            (output / f'response-{i:03}.json').write_text(json.dumps(dict(request=request,
                response=response.model_dump(mode='json')), indent=2, sort_keys=True) + '\n')
            for j, block in enumerate(response.content):
                if block.type == 'image':
                    (output / f'image-{i:03}-{j}.png').write_bytes(base64.b64decode(block.data))
            print(f'{i}: {request["tool"]}: {"error" if response.isError else "response"}', flush=True)
            if response.isError and not request.get('expect_error'):
                failed = True
                break
    if failed:
        raise RuntimeError('Tool failed; inspect recorded MCP response before continuing')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for flag in ('profile', 'catalog', 'archive-root', 'publication-root', 'calls', 'output'):
        parser.add_argument('--' + flag, required=True, type=Path)
    parser.add_argument('--evidence-archive', action='append', default=[], type=Path)
    args = parser.parse_args()
    try:
        asyncio.run(asyncio.wait_for(run(args), timeout=240))
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
