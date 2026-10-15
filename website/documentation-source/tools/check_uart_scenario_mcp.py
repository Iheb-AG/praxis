"""Record UART/timer/EXTI readiness using only actual Praxis MCP responses.

No manual/header/wiki reads, web requests, firmware generation or board operations.
Test inputs name requested entities; hardware facts come exclusively from the MCP.
The configured knowledge/build pair is tested first. An optional candidate bundle
is inspected in a separate process without changing the configured client pair.
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
    raw = '\n'.join(block.text for block in response.content if block.type == 'text')
    try:
        return json.loads(raw)
    except ValueError:
        return raw


async def inspect(name, parameters, output, *, knowledge):
    trace, documents, nets = [], {}, {}
    async with stdio_client(parameters) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        tools = sorted(item.name for item in (await client.list_tools()).tools)

        async def call(tool, arguments):
            response = await client.call_tool(tool, arguments)
            result = value(response)
            trace.append(dict(tool=tool, arguments=arguments, is_error=bool(response.isError),
                              response=response.model_dump(mode='json')))
            print(f'{name}: {tool} {arguments}: {"error" if response.isError else "response"}', flush=True)
            return bool(response.isError), result

        if knowledge:
            gate_error, gate = await call('read_peripheral_doc', {'peripheral_name': 'usart2'})
            error, index = await call('read_wiki_index', {})
            if error or not isinstance(index, str):
                raise RuntimeError('Index retrieval failed')
            for target in ('PA2', 'PA3', 'USART2_TX', 'USART2_RX', 'P1:14', 'P1:13',
                           'LED_A', 'LED_B', 'BLUE_LED', 'RED_LED', 'USER_BUTTON'):
                error, text = await call('query_schematic_netlist', {'query_target': target})
                nets[target] = dict(error=error, found=not error and 'No match' not in str(text), text=text)

            # Follow prerequisites returned by the MCP itself, with cycle/depth bounds.
            async def document(entity, active=()):
                if entity in documents:
                    return
                if entity in active or len(active) > 64:
                    raise RuntimeError('Invalid prerequisite route from MCP')
                error, text = await call('read_peripheral_doc', {'peripheral_name': entity})
                if error and 'PREREQUISITE_REQUIRED' in str(text):
                    match = re.search(r'retrieve in order: ([a-z0-9_, ]+)', str(text))
                    if match:
                        for parent in match[1].strip().split(', '):
                            await document(parent, (*active, entity))
                        error, text = await call('read_peripheral_doc', {'peripheral_name': entity})
                documents[entity] = dict(error=error, text=text,
                    semantics_available=not error and '## Reviewed operating semantics' in str(text)
                    and 'Not reviewed.' not in str(text))

            for entity in ('usart2', 'tim2', 'exti', 'syscfg', 'nvic'):
                await document(entity)
            missing_nets = [key for key, row in nets.items() if not row['found']]
            missing_docs = [key for key, row in documents.items() if row['error']]
            unreviewed = [key for key, row in documents.items()
                          if not row['error'] and not row['semantics_available']]
            workflow_ready = bool(re.search(r'\| uart_timer_interrupts \| True \|', index))
            result = dict(name=name, tools=tools,
                index_gate_enforced=gate_error and 'PREREQUISITE_REQUIRED' in str(gate),
                index=index, missing_topology=missing_nets, missing_documents=missing_docs,
                unreviewed_operating_semantics=unreviewed,
                workflow_ready=workflow_ready,
                knowledge_ready=not (missing_nets or missing_docs or unreviewed) and workflow_ready,
                limitation='Readiness is a minimum retrieval check, not independent semantic or physical validation.')
        else:
            error, profile = await call('get_build_profile', {})
            if error:
                raise RuntimeError('Build profile retrieval failed')
            result = dict(name=name, tools=tools, profile=profile)
    (output / f'{name}-responses.json').write_text(json.dumps(trace, indent=2, sort_keys=True) + '\n')
    return result


async def run(args):
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    config = json.loads(args.config.read_text())['mcp']

    def parameters(entry):
        command = entry['command']
        # Do not inherit a write authorization when testing read-only readiness.
        env = {key: val for key, val in os.environ.items() if key != 'PRAXIS_HARDWARE_AUTHORIZATION'}
        return StdioServerParameters(command=command[0], args=command[1:], cwd=str(output), env=env)

    configured = await inspect('configured-knowledge', parameters(config['project-praxis']), output, knowledge=True)
    build = await inspect('configured-build', parameters(config['project-praxis-build']), output, knowledge=False)
    candidate = None
    if args.candidate_bundle:
        candidate = await inspect('candidate-knowledge', StdioServerParameters(command=sys.executable,
            args=['-m', 'praxis', 'serve', '--bundle', str(args.candidate_bundle.resolve())],
            cwd=str(output)), output, knowledge=True)
    findings = dict(configured=configured, build=build, candidate=candidate,
        firmware_generated=False, compilation_requested=False, hardware_operations=0,
        wiring_confirmation='User reported jumper fitted and board reconnected; physical placement remains a human assertion.',
        scenario_status='ready for detailed configuration review' if configured['knowledge_ready'] else 'blocked at knowledge readiness')
    (output / 'readiness.json').write_text(json.dumps(findings, sort_keys=True, indent=2) + '\n')
    report = ['# UART, timer and interrupt MCP readiness test', '',
              'Evidence: actual local MCP stdio responses. No external model or source-document lookup was used in this replay.', '',
              f"Scenario status: **{findings['scenario_status']}**.", '',
              '## Configured knowledge server', '', configured['index'].split('## Hardware')[0], '',
              f"Index-first gate enforced: {configured['index_gate_enforced']}.", '',
              f"Missing pin/net/connector queries: {', '.join(configured['missing_topology']) or 'none'}.", '',
              f"Missing documents: {', '.join(configured['missing_documents']) or 'none'}.", '',
              f"Unreviewed operating semantics: {', '.join(configured['unreviewed_operating_semantics']) or 'none'}.", '',
              f"Published UART/timer/interrupt workflow ready: {configured['workflow_ready']}.", '',
              '## Configured build server', '',
              f"Bundle revision: `{build['profile']['bundle_revision']}`.", '',
              'Only get_build_profile was called; compilation and board operations were not requested.', '']
    if candidate:
        report += ['## Separate discovery-bundle diagnostic', '',
                   'This separate process does not change OpenCode configuration or the build/hardware profile.', '',
                   f"Missing topology: {', '.join(candidate['missing_topology']) or 'none'}.", '',
                   f"Missing documents: {', '.join(candidate['missing_documents']) or 'none'}.", '',
                   f"Unreviewed operating semantics: {', '.join(candidate['unreviewed_operating_semantics']) or 'none'}.", '']
    report += ['## Interpretation', '',
               'MCP transport and routing responses are evidence of retrieval behavior. A returned header declaration is not reviewed initialization guidance.', '',
               'The user reports the jumper is fitted. MCP connectivity documents describe the reference design; physical jumper placement remains a human assertion.', '',
               'No firmware was generated, built or flashed. The previous LED/button firmware was not replaced.', '',
               ('Next: review exact returned configurations, generate application code and build through the matching MCP service.'
                if configured['knowledge_ready'] else
                'Required next work: publish source-backed missing connectivity/operating semantics, then repeat this MCP test with matching knowledge/build profiles.'), '',
               'Raw responses are recorded beside this report; readiness.json contains the complete index and selected profile.']
    (output / 'READINESS_REPORT.md').write_text('\n'.join(report) + '\n')
    print(json.dumps(dict(scenario_status=findings['scenario_status'],
                         configured_ready=configured['knowledge_ready'],
                         candidate_ready=candidate['knowledge_ready'] if candidate else None,
                         output=str(output)), indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', required=True, type=Path)
    parser.add_argument('--candidate-bundle', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    asyncio.run(asyncio.wait_for(run(args), timeout=120))


if __name__ == '__main__':
    main()
