"""Replay and record the configurable-discovery scenario against a real MCP process.

No external model, network, compiler, build service or hardware operation is used.
Run with the repository Python environment from any directory.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.bundle import Bundle, digest


async def check(bundle_path: Path, output: Path):
    bundle = Bundle(bundle_path)
    params = StdioServerParameters(command=sys.executable,
        args=['-m', 'praxis', 'serve', '--bundle', str(bundle.root)], cwd=str(output))
    trace = []
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        discovered = sorted(tool.name for tool in (await client.list_tools()).tools)

        async def call(tool, arguments, *, error=None, contains=(), exact=None):
            response = await client.call_tool(tool, arguments)
            text = '\n'.join(block.text for block in response.content if block.type == 'text')
            passed = bool(response.isError) == bool(error)
            if error:
                passed &= error in text
            passed &= all(fragment in text for fragment in contains)
            if exact is not None:
                passed &= text == exact
            trace.append(dict(tool=tool, arguments=arguments, is_error=bool(response.isError),
                              expected_error=error, passed=bool(passed), result=text,
                              sha256=digest(text.encode()), bytes=len(text.encode())))
            return text

        async def document(name, canonical=None, **expectations):
            canonical = canonical or name
            exact = (bundle.read(bundle.manifest.peripherals[canonical])
                     if not expectations.get('error') else None)
            return await call('read_peripheral_doc', {'peripheral_name': name}, exact=exact, **expectations)

        await document('tim2', error='PREREQUISITE_REQUIRED', contains=('index',))
        await call('read_wiki_index', {}, exact=bundle.read('wiki/index.md'),
                   contains=('STM32F407VGT6', 'MB997-E-01', 'Peripheral coverage',
                             'uart_timer_interrupts', 'operating semantics not reviewed'))
        await document('tim2', error='PREREQUISITE_REQUIRED', contains=('rcc',))
        await document('exti', error='PREREQUISITE_REQUIRED', contains=('rcc, gpio, syscfg',))
        await document('rcc')
        await document('tim2', 'tim', contains=('TIM2', 'Not reviewed.', 'TIM_CR1_CEN_Msk'))
        await document('spi1', 'spi', contains=('SPI_CR1_SPE_Msk', 'Not reviewed.'))
        await document('i2c1', 'i2c', contains=('I2C_CR1_PE_Msk', 'Not reviewed.'))
        await document('gpio')
        await document('syscfg')
        await document('exti', contains=('EXTI_PR_PR0_Msk', 'Not reviewed.'))
        await document('dma1_stream0', error='PREREQUISITE_REQUIRED', contains=('dma',))
        await document('dma')
        await document('dma1_stream0', 'dma_stream', contains=('DMA_SxCR_EN_Msk',))
        await document('flash', contains=('bit fields withheld', 'FLASH_ACR_BYTE0_ADDRESS_Msk'))
        await document('itm', error='UNKNOWN_PERIPHERAL')
        await document('clock', error='UNKNOWN_PERIPHERAL')
        for name, fragments in [('LED_A', ('PD12', 'schematic_e01')),
                                ('USER_BUTTON', ('PA0', 'SB20', 'schematic_e01')),
                                ('USART2_TX', ('No match',)), ('PA20', ('No match',))]:
            await call('query_schematic_netlist', {'query_target': name}, contains=fragments)
    details = output / 'responses.jsonl'
    details.write_text(''.join(json.dumps(row, sort_keys=True) + '\n' for row in trace), encoding='utf-8')
    report = dict(kind='actual MCP stdio replay; no external model',
                  target=bundle.manifest.target.id, revision=bundle.manifest.bundle_revision,
                  tools=discovered, calls=len(trace),
                  passed=all(row['passed'] for row in trace) and discovered ==
                    ['query_schematic_netlist', 'read_peripheral_doc', 'read_wiki_index'],
                  trace=[{key: value for key, value in row.items() if key != 'result'} for row in trace],
                  evidence_sha256=digest(details.read_bytes()),
                  findings=[
                      'Aliases resolve to full canonical documents without truncation.',
                      'Missing index and missing transitive prerequisites return MCP errors.',
                      'TIM/SPI/I2C retrieval succeeds without reading USART/NVIC.',
                      'EXTI requires RCC/GPIO/SYSCFG; DMA streams require the DMA controller document.',
                      'New declaration documents explicitly state their operating semantics are unreviewed.',
                      'FLASH mask gaps are disclosed and ITM is not served.',
                      'LED_A/USER_BUTTON remain backed by the documented reference-board subset.',
                      'USART2_TX wiring is not in this partial schematic bundle; declarations do not add board nets.'],
                  limits=['No live-model evaluation, firmware generation or target compilation in this replay.',
                          'No flash, reset, debug-probe or physical-board operations.',
                          'Retrieval success does not validate hardware behavior or unreviewed operating semantics.'])
    (output / 'report.json').write_text(json.dumps(report, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bundle', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = asyncio.run(asyncio.wait_for(check(args.bundle, args.output), timeout=60))
    print(json.dumps({key: result[key] for key in ('passed', 'calls', 'revision')}, sort_keys=True))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
