"""MCU extraction without fabricated wiring or inherited firmware qualification."""
import asyncio
import json
import shutil

import pytest
from pydantic import ValidationError

from conftest import ROOT, require_tool
from praxis.bundle import Bundle, digest
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.models import Profile
from praxis.netlist import NetlistIndex
from praxis.reports import read_report
from praxis.routing import Session
from praxis.targets import require_firmware_target


def mcu_profile(directory):
    shutil.copytree(ROOT / "sources/synthetic-cortex-m3", directory)
    path = directory / "profile.json"
    data = json.loads(path.read_text())
    data["target"].update(scope="mcu", clock_hz=None, board_revision="not-applicable",
                          primary_mcu_ref="not-applicable")
    for key in ("netlist", "pin_map", "signal_aliases"):
        data.pop(key)
    data["sources"] = [s for s in data["sources"] if s["id"] != "schematic"]
    path.write_text(json.dumps(data))
    return path, data


@pytest.fixture(scope="module")
def mcu_bundle(tmp_path_factory):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    root = tmp_path_factory.mktemp("mcu-only")
    profile, _ = mcu_profile(root / "inputs")
    return Bundle(compile_bundle(profile, root / "bundle"))


def test_mcu_scope_has_no_fake_clock_wiring_or_qualified_firmware(mcu_bundle):
    target = mcu_bundle.manifest.target
    assert target.clock_hz is None and target.scope == "mcu"
    session = Session(mcu_bundle)
    with pytest.raises(PraxisError, match="PREREQUISITE_REQUIRED"):
        session.query_schematic_netlist("LED_A")
    assert "Experimental MCU-only" in session.read_wiki_index()
    assert "No evaluation board" in session.read_wiki_index()
    result = session.query_schematic_netlist("LED_A")
    assert result.startswith("No match") and "connectivity is unavailable" in result
    assert session.netlist.nets == {}
    with pytest.raises(PraxisError, match="PREREQUISITE_REQUIRED"):
        session.read_peripheral_doc("uart")
    session.read_peripheral_doc("clock")
    session.read_peripheral_doc("pins")
    assert "0x40002000" in session.read_peripheral_doc("uart0")
    assert not read_report(mcu_bundle, "coverage")["workflows"]["uart_polling"]["ready"]
    assert evaluate(mcu_bundle)["passed"]
    with pytest.raises(PraxisError, match="UNSUPPORTED_FIRMWARE_TARGET"):
        require_firmware_target(target)


@pytest.mark.parametrize("change", ["clockless_board", "board_netlist_missing", "netlist", "pin_map",
                                   "signal_aliases", "board", "required_workflows", "board_revision",
                                   "primary_mcu_ref", "without_adapter", "qualified_board"])
def test_invalid_mcu_scope_cannot_relax_board_requirements(tmp_path, change):
    _, data = mcu_profile(tmp_path / "inputs")
    if change in ("clockless_board", "board_netlist_missing"):
        data["target"]["scope"] = "board"
        if change == "board_netlist_missing":
            data["target"]["clock_hz"] = 12_000_000
    elif change == "netlist":
        data["netlist"] = "schematic"
    elif change == "pin_map":
        data["pin_map"] = {"1": "P0_2"}
    elif change == "signal_aliases":
        data["signal_aliases"] = {"TX": ["UART0_TX"]}
    elif change == "board":
        data["board"] = "schematic"
    elif change == "required_workflows":
        data["required_workflows"] = ["led_button_polling"]
    elif change in ("board_revision", "primary_mcu_ref"):
        data["target"][change] = "fabricated-board"
    elif change == "without_adapter":
        del data["target"]["knowledge_adapter"]
    else:
        data["target"]["example_only"] = False
    with pytest.raises(ValidationError):
        Profile.model_validate(data)


def test_empty_netlist_is_only_valid_for_explicit_unavailable_mcu_scope(mcu_bundle):
    text = mcu_bundle.read(mcu_bundle.manifest.netlist)
    with pytest.raises(PraxisError, match="INVALID_NETLIST"):
        NetlistIndex(text, "U1")
    with pytest.raises(PraxisError, match="INVALID_NETLIST"):
        NetlistIndex(text.replace("Connectivity status: unavailable (MCU-only).", ""),
                     "not-applicable", allow_empty=True)
    fixture = Bundle(ROOT / "bundles/synthetic-cortex-m3-v1")
    with pytest.raises(PraxisError, match="cannot claim electrical"):
        NetlistIndex(fixture.read(fixture.manifest.netlist), "U1", allow_empty=True)


def test_source_pin_rejects_changes_before_any_parser_runs(tmp_path, monkeypatch):
    path, data = mcu_profile(tmp_path / "inputs")
    source = data["sources"][0]
    file = path.parent / source["path"]
    source["expected_sha256"] = digest(file.read_bytes())
    path.write_text(json.dumps(data))
    file.write_bytes(file.read_bytes() + b"\n/* modified */\n")
    monkeypatch.setattr("praxis.compiler._definitions", lambda *args: pytest.fail("Pin check must run first"))
    with pytest.raises(PraxisError, match="SOURCE_HASH_MISMATCH"):
        compile_bundle(path, tmp_path / "bundle")
    assert not (tmp_path / "bundle").exists()


def test_legacy_manifest_serialization_remains_unchanged():
    for root in (ROOT / "bundles").iterdir():
        if (root / "manifest.json").is_file():
            bundle = Bundle(root)
            if bundle.manifest.target.scope == "board":
                assert "scope" not in bundle.manifest.target.model_dump()


@pytest.mark.parametrize("part,cpu,offset", [("stm32f103c8t6", "cortex-m3", "0x008"),
                                           ("stm32g071rbt6", "cortex-m0plus", "0x00C"),
                                           ("stm32h743zit6", "cortex-m7", "0x00C")])
def test_real_st_headers_compile_with_their_own_layouts(tmp_path, part, cpu, offset):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    profile = ROOT / "sources/stm32-experimental" / part / "profile.json"
    first = Bundle(compile_bundle(profile, tmp_path / "first"))
    second = Bundle(compile_bundle(profile, tmp_path / "second"))
    assert first.manifest.bundle_revision == second.manifest.bundle_revision
    assert first.documents == second.documents
    assert first.manifest.target.knowledge_adapter.cpu == cpu
    assert f"BRR | {offset} | 32" in first.read("wiki/peripherals/usart.md")
    gpio = first.read("wiki/peripherals/gpio.md")
    usart = first.read("wiki/peripherals/usart.md")
    if cpu == "cortex-m3":
        assert "CRL | 0x000" in gpio and "MODER |" not in gpio
        assert "CR1 | UE | 13:13 | 0x2000" in usart
    else:
        assert "MODER | 0x000" in gpio
        assert "CR1 | UE | 0:0 | 0x1" in usart
    assert gpio.count("## Register map") == 1 and usart.count("## Bit fields") == 1
    coverage = read_report(first, "coverage")
    assert coverage["counts"]["published"] >= 30
    assert coverage["counts"]["reviewed_subsets"] == 0
    assert not any(w["ready"] for w in coverage["workflows"].values())
    assert evaluate(first)["passed"]
    if cpu == "cortex-m7":
        assert len(first.read("wiki/peripherals/rcc.md").encode()) > 65536
        assert "## Machine-readable report" in first.read("wiki/coverage.md")
        assert "reports/coverage" not in first.manifest.documents


async def test_mcu_only_real_stdio(mcu_bundle, tmp_path):
    from tools.check_bundle_mcp import check
    report = await asyncio.wait_for(check(mcu_bundle.root, "uart0", "LED_A", tmp_path), 30)
    assert report["passed"] and report["target"]["scope"] == "mcu"
