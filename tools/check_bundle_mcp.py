"""Family-independent, real stdio MCP replay; no ingestion, build or hardware operations."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.bundle import Bundle, digest
from praxis.coverage import order
from praxis.errors import PraxisError
from praxis.routing import Session


async def check(bundle_path: Path, peripheral: str, signal: str, output: Path):
    bundle = Bundle(bundle_path)
    canonical = bundle.manifest.aliases.get(peripheral.lower(), peripheral.lower())
    if canonical not in bundle.manifest.peripherals:
        raise PraxisError("UNKNOWN_PERIPHERAL", "Choose a published entity or declared alias for the replay")
    expected = Session(bundle)
    expected.read_wiki_index()
    net = expected.query_schematic_netlist(signal)
    if net.startswith("No match"):
        raise PraxisError("UNKNOWN_NET", "Choose an existing exact net, pin, endpoint or signal alias")
    route = order(bundle.dependencies)
    unknown = "praxis_absent_entity"
    while unknown in bundle.manifest.peripherals or unknown in bundle.manifest.aliases:
        unknown += "_x"
    missing_net = "praxis_absent_net"
    while missing_net in expected.netlist.exact or missing_net.casefold() in expected.netlist.pins:
        missing_net += "_x"
    params = StdioServerParameters(command=sys.executable,
        args=["-m", "praxis", "serve", "--bundle", str(bundle.root)], cwd=str(output.resolve()))
    trace = []
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        discovered = sorted(tool.name for tool in (await client.list_tools()).tools)

        async def call(tool, arguments, *, error=None, exact=None, contains=()):
            response = await client.call_tool(tool, arguments)
            text = "\n".join(block.text for block in response.content if block.type == "text")
            passed = bool(response.isError) == bool(error)
            if error:
                passed &= error in text
            passed &= all(value in text for value in contains)
            if exact is not None:
                passed &= exact == text
            trace.append(dict(tool=tool, arguments=arguments, passed=bool(passed),
                is_error=bool(response.isError), expected_error=error,
                response_sha256=digest(text.encode()), response_bytes=len(text.encode())))

        await call("read_peripheral_doc", {"peripheral_name": peripheral},
                   error="PREREQUISITE_REQUIRED", contains=("index",))
        await call("query_schematic_netlist", {"query_target": signal}, error="PREREQUISITE_REQUIRED")
        await call("read_wiki_index", {}, exact=bundle.read("wiki/index.md"))
        if bundle.dependencies[canonical]:
            await call("read_peripheral_doc", {"peripheral_name": peripheral},
                       error="PREREQUISITE_REQUIRED", contains=tuple(bundle.dependencies[canonical]))
        await call("query_schematic_netlist", {"query_target": signal}, exact=net)
        await call("query_schematic_netlist", {"query_target": missing_net},
                   exact=expected.query_schematic_netlist(missing_net))
        await call("read_peripheral_doc", {"peripheral_name": unknown}, error="UNKNOWN_PERIPHERAL")
        await call("read_peripheral_doc", {"peripheral_name": "../outside"}, error="INVALID_INPUT")
        for name in route:
            await call("read_peripheral_doc", {"peripheral_name": name},
                       exact=bundle.read(bundle.manifest.peripherals[name]))
        # Reading the index again must not erase successful prerequisite retrievals.
        await call("read_wiki_index", {}, exact=bundle.read("wiki/index.md"))
        await call("read_peripheral_doc", {"peripheral_name": peripheral.upper()},
                   exact=bundle.read(bundle.manifest.peripherals[canonical]))
    report = dict(passed=all(row["passed"] for row in trace) and discovered == [
        "query_schematic_netlist", "read_peripheral_doc", "read_wiki_index"],
        target=bundle.manifest.target.model_dump(), revision=bundle.manifest.bundle_revision,
        calls=len(trace), discovered_tools=discovered, trace=trace,
        limits="Actual MCP retrieval and complete-byte checks only; no live LLM, operating-semantic, build or physical qualification.")
    (output / "report.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--peripheral", required=True)
    parser.add_argument("--signal", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    result = asyncio.run(asyncio.wait_for(check(args.bundle, args.peripheral, args.signal, args.output), 60))
    print(json.dumps({name: result[name] for name in ("passed", "calls", "revision")}, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
