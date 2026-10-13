"""Exercise an already-built Docker knowledge image through real stdio MCP sessions.

No image pull, firmware build, probe access, or hardware actions. Requires runtime
Python dependencies on the test host; end users only need Docker and a bundle.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.bundle import Bundle, digest
from praxis.coverage import order
from praxis.routing import Session


def launch(engine: str, image: str, bundle: Path) -> list[str]:
    # Reject commas rather than incorrectly parsing them as --mount options.
    if "," in str(bundle.resolve()):
        raise ValueError("Choose a bundle path without commas for Docker --mount")
    return [engine, "run", "--rm", "--init", "-i", "--pull=never", "--network=none",
            "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
            "--pids-limit=64", "--memory=256m", "--cpus=1", "--mount",
            f"type=bind,source={bundle.resolve()},target=/bundle,readonly", image]


async def replay(engine: str, image: str, path: Path, cwd: Path) -> dict:
    bundle = Bundle(path)
    expected = Session(bundle)
    argv = launch(engine, image, path)
    params = StdioServerParameters(command=argv[0], args=argv[1:], cwd=str(cwd))
    trace = []
    async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
        initialization = await client.initialize()
        assert bundle.manifest.bundle_revision in initialization.instructions
        tools = (await client.list_tools()).tools
        assert sorted(t.name for t in tools) == [
            "query_schematic_netlist", "read_peripheral_doc", "read_wiki_index"]
        assert all(t.annotations.readOnlyHint and not t.annotations.destructiveHint for t in tools)

        async def call(name, arguments, *, error=None, exact=None):
            result = await client.call_tool(name, arguments)
            text = "\n".join(b.text for b in result.content if b.type == "text")
            assert bool(result.isError) == bool(error), text
            if error:
                assert error in text, text
            if exact is not None:
                assert text == exact, f"Full response differs for {name}: {arguments}"
            trace.append(dict(tool=name, arguments=arguments, expected_error=error,
                              response_sha256=digest(text.encode()), bytes=len(text.encode())))

        await call("read_peripheral_doc", {"peripheral_name": "usart"}, error="PREREQUISITE_REQUIRED")
        await call("query_schematic_netlist", {"query_target": "PA2"}, error="PREREQUISITE_REQUIRED")
        await call("read_wiki_index", {}, exact=expected.read_wiki_index())
        # All registered documents are compared in dependency order, without truncation.
        for entity in order(bundle.dependencies):
            await call("read_peripheral_doc", {"peripheral_name": entity},
                       exact=expected.read_peripheral_doc(entity))
        signal = "LED_A" if not bundle.manifest.target.example_only else "UART_RX"
        await call("query_schematic_netlist", {"query_target": signal},
                   exact=expected.query_schematic_netlist(signal))
        await call("query_schematic_netlist", {"query_target": "praxis_absent_net"},
                   exact=expected.query_schematic_netlist("praxis_absent_net"))
        await call("read_peripheral_doc", {"peripheral_name": "../gpio"}, error="INVALID_INPUT")
        await call("read_wiki_index", {}, exact=expected.read_wiki_index())
        await call("read_peripheral_doc", {"peripheral_name": "USART"},
                   exact=expected.read_peripheral_doc("USART"))
    return dict(target=bundle.manifest.target.id, revision=bundle.manifest.bundle_revision,
                calls=len(trace), complete_documents=len(bundle.manifest.peripherals), trace=trace)


def check_failures(engine: str, image: str, bundle: Path, root: Path) -> list[str]:
    missing = root / "missing"
    missing.mkdir()
    corrupt = root / "corrupt"
    shutil.copytree(bundle, corrupt)
    index = corrupt / "wiki/index.md"
    index.write_bytes(index.read_bytes() + b"\nTampered document.\n")
    passed = []
    for path, code in ((missing, "MISSING_FILE"), (corrupt, "INTEGRITY_ERROR")):
        result = subprocess.run(launch(engine, image, path), input="", text=True,
                                capture_output=True, timeout=30, check=False)
        assert result.returncode != 0, result
        assert code in result.stderr, result.stderr
        assert result.stdout == "", "Startup diagnostics polluted MCP stdout"
        passed.append(code)
    probe = """import importlib.util, json, os
from pathlib import Path
assert os.getuid() == 10001
assert all(importlib.util.find_spec(m) is None for m in ('clang', 'pdfplumber', 'pytest', 'elftools'))
for path in ('/app/probe', '/bundle/probe'):
    try:
        Path(path).write_text('unexpected')
    except OSError:
        pass
    else:
        raise AssertionError('Writable path: ' + path)
print(json.dumps({'uid': os.getuid(), 'read_only': True, 'optional_extras_absent': True}))
"""
    args = launch(engine, image, bundle)
    # Docker options precede the image. Override the CLI only for this runtime probe.
    args[-1:-1] = ["--entrypoint", "/app/.venv/bin/python"]
    result = subprocess.run([*args, "-c", probe], text=True, capture_output=True,
                            timeout=30, check=True)
    assert json.loads(result.stdout)["read_only"]
    passed.extend(["non_root", "read_only_filesystem_and_bundle", "no_optional_extras"])
    return passed


async def check(args, root):
    # Fresh sequential sessions for the same target must both start gated. Different
    # targets share one image but never a Session, state store, or loaded bundle.
    sessions = []
    for bundle in (*args.bundle, args.bundle[0]):
        sessions.append(await asyncio.wait_for(replay(args.engine, args.image, bundle, root), 90))
    negative = await asyncio.to_thread(check_failures, args.engine, args.image, args.bundle[0], root)
    inspected = subprocess.run([args.engine, "image", "inspect", args.image], text=True,
                               capture_output=True, timeout=15, check=True)
    metadata = json.loads(inspected.stdout)[0]
    return dict(passed=True, image=args.image, image_id=metadata["Id"],
                architecture=metadata["Architecture"], os=metadata["Os"],
                sessions=sessions, negative_and_runtime_checks=negative,
                limits="Local architecture only; no compiler, physical board, or remote registry publication tested.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", default="docker")
    parser.add_argument("--image", required=True)
    parser.add_argument("--bundle", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, help="New JSON evidence file; default stdout")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="praxis-container-") as directory:
        root = Path(directory)
        root.chmod(0o755)
        report = asyncio.run(check(args, root))
    text = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.output:
        with args.output.open("x", encoding="utf-8") as handle:
            handle.write(text)
        print(json.dumps({"passed": True, "sessions": len(report["sessions"]),
                          "calls": sum(s["calls"] for s in report["sessions"]),
                          "image_id": report["image_id"]}, sort_keys=True))
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
