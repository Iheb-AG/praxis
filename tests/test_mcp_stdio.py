import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT


async def exercise(target, cwd):
    params = StdioServerParameters(command=sys.executable,
                                  args=[str(ROOT / "server.py"), "--bundle", str(ROOT / "bundles" / target)],
                                  cwd=str(cwd))
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        tools = (await client.list_tools()).tools
        assert {t.name for t in tools} == {"read_wiki_index", "read_peripheral_doc", "query_schematic_netlist"}
        assert all(t.annotations.readOnlyHint for t in tools)
        blocked = await client.call_tool("read_peripheral_doc", {"peripheral_name": "usart"})
        assert blocked.isError and "PREREQUISITE_REQUIRED" in blocked.content[0].text
        result = await client.call_tool("read_wiki_index", {})
        assert not result.isError and target in result.content[0].text
        route = ["rcc", "gpio", "usart", "nvic"] if target.startswith("stm") else ["clock", "gpio", "usart", "interrupts"]
        for name in route:
            result = await client.call_tool("read_peripheral_doc", {"peripheral_name": name})
            assert not result.isError
            assert result.content[0].text == (ROOT / "bundles" / target / "wiki/peripherals" / f"{name}.md").read_text()
        result = await client.call_tool("query_schematic_netlist", {"query_target": "UART_RX"})
        assert not result.isError and "J1:2" in result.content[0].text
        bad = await client.call_tool("read_peripheral_doc", {"peripheral_name": "../usart"})
        assert bad.isError and "INVALID_INPUT" in bad.content[0].text


async def test_real_stdio_clients_from_unrelated_cwd(tmp_path):
    await asyncio.wait_for(asyncio.gather(
        exercise("stm32f401re", tmp_path), exercise("atmega328p", tmp_path),
        exercise("stm32f407vgt6", tmp_path)), timeout=30)


async def test_discovery_board_led_button_queries_over_real_stdio(tmp_path):
    params = StdioServerParameters(command=sys.executable,
        args=[str(ROOT / "server.py"), "--bundle", str(ROOT / "bundles/stm32f407g-disc1-e01-m1")],
        cwd=str(tmp_path))
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        result = await client.call_tool("query_schematic_netlist", {"query_target": "LED_A"})
        assert result.isError and "missing: index" in result.content[0].text
        index = await client.call_tool("read_wiki_index", {})
        assert "STM32F407G-DISC1" in index.content[0].text
        for name, pin in [("LED_A", "PD12"), ("LED_B", "PD13"), ("USER_BUTTON", "PA0")]:
            result = await client.call_tool("query_schematic_netlist", {"query_target": name})
            assert not result.isError and pin in result.content[0].text
            assert "schematic_e01" in result.content[0].text and "MB997-E-01" in result.content[0].text
        blocked = await client.call_tool("read_peripheral_doc", {"peripheral_name": "gpio"})
        assert blocked.isError and "rcc" in blocked.content[0].text
        for name in ("rcc", "gpio"):
            result = await client.call_tool("read_peripheral_doc", {"peripheral_name": name})
            assert not result.isError
