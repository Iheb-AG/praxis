"""Large knowledge documents must compile, hash, decode and cross MCP intact."""
import asyncio
import json
import shutil
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_tool
from praxis.bundle import Bundle, digest, read_inside, revision
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError


@pytest.fixture(scope="module")
def large_bundle(tmp_path_factory):
    require_tool("avr-gcc")
    root = tmp_path_factory.mktemp("large-knowledge")
    source = root / "inputs"
    shutil.copytree(ROOT / "sources/atmega328p", source, ignore=shutil.ignore_patterns("imports"))
    path = source / "reviewed/usart.md"
    # Exceed both the former 64 KiB publication cap and the generic 8 MiB raw
    # input budget, which must not accidentally become a Markdown ceiling.
    narrative = "\n## Large UTF-8 fixture\n" + "Complete evidence row — µ\n" * 350_000 + "END_LARGE_EVIDENCE\n"
    path.write_text(path.read_text() + narrative, encoding="utf-8")
    assert path.stat().st_size > 8 * 1024 * 1024
    return Bundle(compile_bundle(source / "profile.json", root / "bundle"))


def test_large_source_and_published_document_are_complete(large_bundle):
    path = "wiki/peripherals/usart.md"
    text = large_bundle.read(path)
    raw = (large_bundle.root / path).read_bytes()
    assert text.encode() == raw
    assert len(raw) > 8 * 1024 * 1024
    assert text.count("Complete evidence row — µ") == 350_000
    assert "END_LARGE_EVIDENCE" in text
    assert text.count("## Register map") == 1 and text.count("## Bit fields") == 1
    assert digest(raw) == large_bundle.manifest.file_hashes[path]


async def test_large_document_survives_real_stdio_mcp(large_bundle, tmp_path):
    async def exercise():
        params = StdioServerParameters(command=sys.executable,
            args=[str(ROOT / "server.py"), "--bundle", str(large_bundle.root)], cwd=str(tmp_path))
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            blocked = await client.call_tool("read_peripheral_doc", {"peripheral_name": "usart"})
            assert blocked.isError and "PREREQUISITE_REQUIRED" in blocked.content[0].text
            await client.call_tool("read_wiki_index", {})
            for name in ("clock", "gpio", "usart"):
                result = await client.call_tool("read_peripheral_doc", {"peripheral_name": name})
                assert not result.isError
            text = "\n".join(block.text for block in result.content if block.type == "text")
            assert text == large_bundle.read("wiki/peripherals/usart.md")
            assert text.count("Complete evidence row — µ") == 350_000
    await asyncio.wait_for(exercise(), timeout=60)


@pytest.mark.parametrize("failure", ["hash", "encoding", "link"])
def test_large_document_tail_is_validated(large_bundle, tmp_path, failure):
    root = tmp_path / "bundle"
    shutil.copytree(large_bundle.root, root)
    path = root / "wiki/peripherals/usart.md"
    data = path.read_bytes() + {"hash": b"changed tail", "encoding": b"\xff", "link": b"\n[[absent]]\n"}[failure]
    path.write_bytes(data)
    if failure != "hash":
        manifest_path = root / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["file_hashes"]["wiki/peripherals/usart.md"] = digest(data)
        manifest["bundle_revision"] = revision(manifest)
        manifest_path.write_text(json.dumps(manifest))
    code = {"hash": "INTEGRITY_ERROR", "encoding": "INVALID_ENCODING", "link": "BROKEN_LINK"}[failure]
    with pytest.raises(PraxisError, match=code):
        Bundle(root)


def test_explicit_nonknowledge_input_limits_remain_enforced(tmp_path):
    path = tmp_path / "input.json"
    path.write_bytes(b"x" * 65537)
    assert read_inside(tmp_path, path.name) == path.read_bytes()
    with pytest.raises(PraxisError, match="DOCUMENT_TOO_LARGE"):
        read_inside(tmp_path, path.name, 65536)
