"""Replay a data-defined target acceptance plan through real knowledge/build MCP.

Exit 0 means the specified software checks passed, NOT full MCU acceptance.
No flash, reset, probe or network tools are exposed. Every case is attempted and
recorded; an error makes software acceptance fail instead of skipping the case.
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

from praxis.acceptance import hash_plan, load_plan, summarize
from praxis.bundle import Bundle, digest
from praxis.coverage import order
from praxis.support import assess, markdown


def payload(response):
    if response.structuredContent is not None:
        value = response.structuredContent
        return value["result"] if set(value) == {"result"} else value
    text = "\n".join(block.text for block in response.content if block.type == "text")
    try:
        return json.loads(text)
    except ValueError:
        return text


async def run(args):
    bundle = Bundle(args.bundle)
    plan = load_plan(args.plan, bundle, args.workspace)
    support = assess(bundle, args.catalog)
    inventory = None
    if args.inventory is not None:
        from praxis.capability_inventory import from_spec
        inventory = from_spec(bundle, args.inventory)
    revision = bundle.manifest.bundle_revision
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False, mode=0o700)
    trace, checks, builds, topology = [], {}, {}, {}
    env = {key: value for key, value in os.environ.items() if key != "PRAXIS_HARDWARE_AUTHORIZATION"}

    def connection(command):
        return StdioServerParameters(command=sys.executable, args=["-m", "praxis", *command],
                                     cwd=str(output), env=env)

    async def call(client, server, name, arguments):
        response = await client.call_tool(name, arguments)
        value = payload(response)
        encoded = json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
        trace.append(dict(server=server, tool=name, arguments=arguments, is_error=bool(response.isError),
                          response_sha256=digest(encoded), response_bytes=len(encoded)))
        print(f"{server}: {name}: {'error' if response.isError else 'response'}", flush=True)
        return bool(response.isError), value

    async with stdio_client(connection(["serve", "--bundle", str(bundle.root)])) as (reader, writer), \
            ClientSession(reader, writer) as client:
        initialized = await client.initialize()
        checks["knowledge_revision"] = f"Session bundle revision: {revision}" in (initialized.instructions or "")
        checks["knowledge_tools"] = sorted(t.name for t in (await client.list_tools()).tools) == [
            "query_schematic_netlist", "read_peripheral_doc", "read_wiki_index"]
        route = order(bundle.dependencies)
        error, value = await call(client, "knowledge", "read_peripheral_doc", {"peripheral_name": route[-1]})
        checks["index_gate"] = error and "PREREQUISITE_REQUIRED" in str(value)
        error, value = await call(client, "knowledge", "query_schematic_netlist", {"query_target": "absent"})
        checks["topology_index_gate"] = error and "PREREQUISITE_REQUIRED" in str(value)
        error, index = await call(client, "knowledge", "read_wiki_index", {})
        checks["complete_index"] = not error and index == bundle.read("wiki/index.md")
        for name, row in support["workflows"].items():
            checks[f"workflow:{name}"] = isinstance(index, str) and bool(re.search(
                rf"^\| {re.escape(name)} \| {row['knowledge_ready']} \|", index, re.M))
        for name in route:
            error, value = await call(client, "knowledge", "read_peripheral_doc", {"peripheral_name": name})
            checks[f"complete_document:{name}"] = not error and value == bundle.read(bundle.manifest.peripherals[name])
        signals = sorted({signal for row in support["workflows"].values() for signal in row["required_signals"]})
        for signal in signals:
            error, value = await call(client, "knowledge", "query_schematic_netlist", {"query_target": signal})
            checks[f"topology_response:{signal}"] = not error and isinstance(value, str)
            topology[signal] = {"matched": not error and isinstance(value, str) and not value.lower().startswith("no match"),
                                "response": value}

    command = ["build-serve", "--bundle", str(bundle.root), "--assets", str(args.assets.resolve()),
        "--workspace", str(args.workspace.resolve()), "--artifacts", str(output / "artifacts"),
        "--lock", str(args.lock.resolve())]
    async with stdio_client(connection(command)) as (reader, writer), ClientSession(reader, writer) as client:
        await client.initialize()
        checks["build_tools_without_hardware"] = sorted(t.name for t in (await client.list_tools()).tools) == [
            "build_firmware", "get_build_profile", "validate_firmware"]
        error, profile = await call(client, "build", "get_build_profile", {})
        checks["matching_build_revision"] = not error and profile.get("bundle_revision") == revision
        if not checks["matching_build_revision"] or not checks["build_tools_without_hardware"]:
            raise RuntimeError("Refusing builds: mismatched revision or unexpected hardware tools")
        for case in plan.cases:
            error, build = await call(client, "build", "build_firmware", {"source_directory": case.source_directory})
            record = {"passed": False, "bundle_revision": revision, "limitations": case.limitations,
                      "workflows": case.workflows, "response": build}
            if not error and isinstance(build, dict):
                record.update({key: build.get(key) for key in ("artifact_id", "asset_revision", "image",
                               "source_sha256", "compiler_versions", "bundle_revision")})
                if build.get("compile_passed") is True and build.get("image_validated") is True:
                    error, validation = await call(client, "build", "validate_firmware", {"artifact_id": build["artifact_id"]})
                    record["passed"] = not error and validation.get("validation", {}).get("valid") is True
                    record["revalidation"] = validation
            builds[case.id] = record

    report = summarize(support, plan, builds, checks)
    report['manufacturer_inventory_assessed'] = inventory is not None
    if inventory is not None:
        report['source_inventory'] = {key: inventory[key] for key in (
            'inventory_sha256', 'counts', 'inventory_complete', 'all_features_supported', 'gaps')}
        report['acceptance_blockers'].extend('source inventory: ' + gap for gap in inventory['gaps'])
        (output / 'inventory.json').write_text(json.dumps(inventory, sort_keys=True, indent=2) + '\n')
    report.update(plan_sha256=hash_plan(plan), tool_calls=len(trace), topology=topology)
    for filename, value in (("report.json", report), ("trace.json", trace)):
        (output / filename).write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")
    (output / "support.md").write_text(markdown(support))
    print(json.dumps({key: report[key] for key in ("software_checks_passed", "full_mcu_accepted",
          "bundle_revision", "tool_calls", "hardware_operations")}, indent=2))
    return 0 if report["software_checks_passed"] else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("bundle", "plan", "catalog", "workspace", "assets", "lock", "output"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument('--inventory', type=Path, help='Optional pinned manufacturer scope; gaps remain acceptance blockers')
    args = parser.parse_args()
    return asyncio.run(asyncio.wait_for(run(args), timeout=900))


if __name__ == "__main__":
    raise SystemExit(main())
