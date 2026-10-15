import json
import shutil
import subprocess
import sys

import pytest

from praxis.adapters.kicad import audit_hierarchy, parse_schematic
from praxis.board import load, validate
from praxis.bundle import Bundle
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.models import Profile, ReviewedSchematic
from praxis.routing import Session
from conftest import ROOT, require_tool

SOURCE = ROOT / "sources/stm32f407g-disc1"
BUNDLE = ROOT / "bundles/stm32f407g-disc1-e01-m1"


def inputs():
    profile = Profile.model_validate_json((SOURCE / "profile.json").read_bytes())
    board = load(SOURCE / "reviewed/board.json")
    schematic = ReviewedSchematic.model_validate_json((SOURCE / "reviewed/netlist.json").read_bytes())
    return profile, board, schematic


def test_discovery_queries_return_reviewed_board_context_and_explicit_circuit_nets():
    session = Session(Bundle(BUNDLE))
    with pytest.raises(PraxisError, match="missing: index"):
        session.query_schematic_netlist("LED_A")
    index = session.read_wiki_index()
    assert "STM32F407G-DISC1" in index and "Actual card revision is unconfirmed" in index
    green = session.query_schematic_netlist("LED_A")
    assert green == session.query_schematic_netlist("LD4") == session.query_schematic_netlist("PD12")
    assert "U4:59" in green and "LD4:1" in green and "R40:2" in green
    assert "Separate circuit net: LD4_ANODE" in green
    assert "high" in green and "510 ohm" in green and "schematic_e01:page:4" in green
    assert "SysTick_Config(SystemCoreClock / 1000U)" in green
    assert "not HCLK/8" in green
    button = session.query_schematic_netlist("USER_BUTTON")
    assert "U4:23" in button and "PA0" in button and "external-down" in button
    assert "220000 ohm" in button and "SB20" in button
    assert session.query_schematic_netlist("PC13").startswith("No match")


def test_reference_net_memberships_do_not_union_across_components():
    profile, board, schematic = inputs()
    circuits = validate(board, schematic, profile.target, profile.pin_map,
                        {s.id: s.authority for s in profile.sources}, profile.required_workflows)
    nets = {n.name: {p.endpoint for p in n.pins} for n in schematic.nets}
    assert nets["PD12"] == {"U4:59", "R40:1"}
    assert nets["LD4_ANODE"] == {"R40:2", "LD4:1"}
    assert circuits["ld4"] == ["GND", "LD4_ANODE", "PD12"]
    assert nets["PA0"] == {"U4:23", "SB20:1"}
    assert nets["B1_SIGNAL"] == {"R35:2", "B1:1", "B1:2", "R39:1"}


@pytest.mark.parametrize("failure", ["pin", "led_polarity", "button_polarity", "pull",
    "disconnected", "bridge_open", "missing_alias", "unknown_source", "wrong_revision",
    "required_timing", "source_authority", "component_pin", "duplicate_component"])
def test_invalid_required_board_facts_block_publication(tmp_path, failure):
    for tool in ("clang", "arm-none-eabi-gcc"):
        require_tool(tool)
    root = tmp_path / "inputs"
    shutil.copytree(SOURCE, root, ignore=shutil.ignore_patterns("imports"))
    board_path, net_path = root / "reviewed/board.json", root / "reviewed/netlist.json"
    board, net = json.loads(board_path.read_text()), json.loads(net_path.read_text())
    led = next(s for s in board["signals"] if s["id"] == "ld4")
    button = next(s for s in board["signals"] if s["id"] == "b1")
    if failure == "pin":
        led["pin"] = "PA2"
    elif failure == "led_polarity":
        led["active_level"] = "low"
    elif failure == "button_polarity":
        button["active_level"] = "low"
    elif failure == "pull":
        button["pull"] = "external-up"
    elif failure == "disconnected":
        led["series_path"] = ["R36"]
    elif failure == "bridge_open":
        next(c for c in net["components"] if c["ref"] == "SB20")["fitted"] = False
    elif failure == "missing_alias":
        led["aliases"].remove("LED_A")
    elif failure == "unknown_source":
        led["sources"][0]["source"] = "not_registered"
    elif failure == "wrong_revision":
        board["board_revision"] = "MB997-G-01"
    elif failure == "required_timing":
        next(f for f in board["facts"] if f["id"] == "timing_source")["state"] = "unresolved"
    elif failure == "source_authority":
        led["sources"][0]["source"] = "header"
    elif failure == "component_pin":
        next(c for c in net["components"] if c["ref"] == "U4")["pins"]["59"] = "PA2"
    else:
        net["components"].append(net["components"][0])
    board_path.write_text(json.dumps(board))
    net_path.write_text(json.dumps(net))
    output = tmp_path / "rejected"
    with pytest.raises(PraxisError):
        compile_bundle(root / "profile.json", output)
    assert not output.exists()


def test_documented_board_is_deterministic_across_input_locations(tmp_path):
    for tool in ("clang", "arm-none-eabi-gcc"):
        require_tool(tool)
    outputs = []
    for name in ("first", "second"):
        source = tmp_path / name
        shutil.copytree(SOURCE, source, ignore=shutil.ignore_patterns("imports"))
        output = compile_bundle(source / "profile.json", tmp_path / (name + "-bundle"))
        outputs.append({p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()})
    assert outputs[0] == outputs[1]
    bundle = Bundle(tmp_path / "first-bundle")
    assert not bundle.manifest.target.example_only
    assert "schemas/board" in bundle.manifest.documents
    assert max(len(text.encode()) for text in bundle.documents.values()) <= 65536


def test_kicad_component_values_properties_and_dnp_are_preserved(tmp_path):
    profile = Profile.model_validate_json((ROOT / "sources/stm32f401re/profile.json").read_bytes())
    raw = (ROOT / "sources/stm32f401re/raw/netlist.xml").read_text()
    raw = raw.replace('<comp ref="R1">', '<comp ref="R1"><property name="dnp"/>')
    path = tmp_path / "export.xml"
    path.write_text(raw)
    result = parse_schematic(path, "netlist", profile.target, profile.pin_map)
    resistor = next(c for c in result.components if c.ref == "R1")
    assert resistor.value == "33R" and resistor.pins == {"1": "1", "2": "2"}
    assert not resistor.fitted and "dnp" in resistor.properties


def test_kicad_hierarchy_requires_registered_subsheets_and_rejects_cycles(tmp_path):
    parent, child = tmp_path / "parent.kicad_sch", tmp_path / "child.kicad_sch"
    parent.write_text('(kicad_sch (sheet (property "Sheetfile" "child.kicad_sch")))')
    child.write_text('(kicad_sch)')
    with pytest.raises(PraxisError, match="UNREGISTERED_DEPENDENCY"):
        audit_hierarchy(parent, [parent])
    audit_hierarchy(parent, [parent, child])
    child.write_text('(kicad_sch (sheet (property "Sheetfile" "parent.kicad_sch")))')
    with pytest.raises(PraxisError, match="SCHEMATIC_CYCLE"):
        audit_hierarchy(parent, [parent, child])


@pytest.mark.parametrize("target", ["stm32f401re", "atmega328p", "stm32f407vgt6", "stm32f407g-disc1-e01-m1"])
def test_published_bundles_serve_offline_without_ingestion_libraries_or_input_sources(tmp_path, target):
    destination = tmp_path / "published"
    shutil.copytree(ROOT / "bundles" / target, destination)
    code = '''
import sys
from importlib.abc import MetaPathFinder
from pathlib import Path
class NoAdapters(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname.split('.')[0] in ('clang', 'defusedxml', 'bs4', 'pdfplumber'):
            raise ModuleNotFoundError('Ingestion dependency unavailable')
sys.meta_path.insert(0, NoAdapters())
from praxis.bundle import Bundle
from praxis.routing import Session
import socket
import subprocess
def forbidden(*args, **kwargs):
    raise AssertionError('Retrieval attempted network or subprocess execution')
socket.socket = forbidden
subprocess.Popen = forbidden
session = Session(Bundle(Path(sys.argv[1])))
assert session.read_wiki_index()
first = 'rcc' if session.bundle.manifest.target.family == 'stm32' else 'clock'
assert session.read_peripheral_doc(first)
assert session.read_peripheral_doc('gpio')
query = 'LED_A' if not session.bundle.manifest.target.example_only else 'UART_RX'
assert not session.query_schematic_netlist(query).startswith('No match')
'''
    result = subprocess.run([sys.executable, "-c", code, str(destination)], cwd=tmp_path,
                            capture_output=True, text=True, timeout=10, check=False)
    assert result.returncode == 0, result.stderr
