import json
import shutil

import pytest

from praxis.adapters.devicetree import compile_dts, parse_dtb
from praxis.adapters.headers import cmsis
from praxis.adapters.kicad import export, parse
from praxis.bundle import Bundle
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.expressions import integer
from praxis.models import Profile
from conftest import ROOT, require_tool


def test_integer_parser_is_restricted_and_resolves_aliases():
    assert integer("(BASE + (1UL << SHIFT))", {"BASE": "0x40000000UL", "SHIFT": "17"}) == 0x40020000
    for expression in ["__import__('os').system('true')", "(uint32_t)3", "f(1)", "1 << 1000", "A"]:
        with pytest.raises(PraxisError, match="UNSUPPORTED_EXPRESSION"):
            integer(expression, {"A": "A"})


def test_clang_preserves_reserved_arrays_and_widths(tmp_path):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    header = tmp_path / "layout.h"
    header.write_text("typedef struct { unsigned int A; unsigned int RESERVED[3]; unsigned char B[4]; } Fixture;")
    layout = cmsis(header, ["Fixture"], [])
    assert layout["Fixture"]["A"] == {"offset": 0, "width": 32, "count": 1}
    assert layout["Fixture"]["RESERVED"] == {"offset": 4, "width": 32, "count": 3}
    assert layout["Fixture"]["B"] == {"offset": 16, "width": 8, "count": 4}


@pytest.mark.parametrize("target", ["stm32f401re", "atmega328p"])
def test_deterministic_compile_and_immutable_publication(tmp_path, target):
    require_tool("arm-none-eabi-gcc" if target.startswith("stm") else "avr-gcc")
    if target.startswith("stm"):
        require_tool("clang")
        require_tool("dtc")
        require_tool("fdtoverlay")
    source = tmp_path / "inputs"
    shutil.copytree(ROOT / "sources" / target, source, ignore=shutil.ignore_patterns("imports"))
    profile = source / "profile.json"
    first, second = tmp_path / "first", tmp_path / "second"
    compile_bundle(profile, first)
    compile_bundle(profile, second)
    assert {p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()} == {
        p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()}
    assert compile_bundle(profile, first) == first
    original = (first / "manifest.json").read_bytes()
    review_file = source / "reviewed/usart.md"
    review_file.write_text(review_file.read_text() + "\nAdditional reviewed note.\n")
    with pytest.raises(PraxisError, match="IMMUTABLE_BUNDLE"):
        compile_bundle(profile, first)
    assert (first / "manifest.json").read_bytes() == original
    Bundle(first)


@pytest.mark.parametrize("failure", ["package", "clock", "conflict", "mask", "duplicate", "unreviewed", "oversized"])
def test_compiler_rejects_bad_sources_without_publication(tmp_path, failure):
    require_tool("avr-gcc")
    source = tmp_path / "inputs"
    shutil.copytree(ROOT / "sources/atmega328p", source, ignore=shutil.ignore_patterns("imports"))
    definitions = source / "reviewed/peripherals.json"
    data = json.loads(definitions.read_text())
    if failure in ("package", "clock"):
        path = source / "profile.json"
        profile = json.loads(path.read_text())
        if failure == "package":
            profile["target"]["package"] = "wrong-package"
        else:
            profile["target"]["clock_hz"] = 8_000_000
        path.write_text(json.dumps(profile))
    elif failure == "conflict":
        data[0]["registers"][0]["offset"] += 1
    elif failure == "duplicate":
        data.append(data[0])
    elif failure == "mask":
        fields = next(r["fields"] for p in data for r in p["registers"] if r["name"] == "UCSR0A")
        fields[0]["lsb"], fields[1]["lsb"] = fields[1]["lsb"], fields[0]["lsb"]
        fields[0]["mask"], fields[1]["mask"] = fields[1]["mask"], fields[0]["mask"]
    elif failure == "unreviewed":
        data[0]["review"]["status"] = "draft"
    else:
        (source / "reviewed/usart.md").write_text("x" * 200_000)
    definitions.write_text(json.dumps(data))
    output = tmp_path / "output"
    if failure == "oversized":
        bundle = Bundle(compile_bundle(source / "profile.json", output))
        assert "x" * 200_000 in bundle.read("wiki/peripherals/usart.md")
        return
    with pytest.raises(PraxisError):
        compile_bundle(source / "profile.json", output)
    assert not output.exists()


def test_xml_entities_are_never_expanded(tmp_path):
    profile = Profile.model_validate_json((ROOT / "sources/atmega328p/profile.json").read_bytes())
    path = tmp_path / "bad.xml"
    path.write_text('<!DOCTYPE export [<!ENTITY x SYSTEM "file:///etc/passwd">]><export>&x;</export>')
    with pytest.raises((PraxisError, ValueError)):
        parse(path, "netlist", profile.target, profile.pin_map)


def test_device_tree_overlay_translation_and_unknown_properties():
    require_tool("dtc")
    require_tool("fdtoverlay")
    base = ROOT / "sources/stm32f401re/raw"
    nodes = compile_dts(base / "topology.dts", [base / "enable_uart.dtso"], [base], "dts")
    uart = next(n for n in nodes if n.path == "/bus/serial@4400")
    assert uart.enabled
    assert uart.decoded["reg"] == [{"address": 0x40004400, "size": 0x400}]
    assert uart.decoded["clocks"] == [{"provider": "/clock", "args": []}]
    assert uart.decoded["interrupts"] == [{"provider": "/interrupt-controller", "args": [38]}]
    assert uart.decoded["pins"] == ["PA2", "PA3"]
    assert "praxis,unknown" in uart.unresolved
    assert uart.properties["praxis,unknown"] == "00001234"


def test_dangling_phandle_blocks_publication(tmp_path):
    require_tool("dtc")
    source = tmp_path / "bad.dts"
    source.write_text('/dts-v1/; / { device { clocks = <0xDEADBEEF>; }; };')
    with pytest.raises(PraxisError, match="DANGLING_PHANDLE"):
        compile_dts(source, [], [tmp_path], "dts")


@pytest.mark.parametrize("data", [b"", b"\xd0\x0d\xfe\xed" + b"\xff" * 40])
def test_truncated_dtb_is_rejected_before_c_access(data):
    with pytest.raises(PraxisError, match="INVALID_DTB"):
        parse_dtb(data, "dts")


@pytest.mark.parametrize("target", ["stm32f401re", "atmega328p"])
def test_live_kicad_export_matches_fixture(tmp_path, target):
    require_tool("kicad-cli")
    root = ROOT / "sources" / target
    profile = Profile.model_validate_json((root / "profile.json").read_bytes())
    destination = tmp_path / "export.xml"
    export(root / "raw/board.kicad_sch", destination)
    actual = parse(destination, "netlist", profile.target, profile.pin_map)
    expected = parse(root / "raw/netlist.xml", "netlist", profile.target, profile.pin_map)
    def memberships(nets):
        return {n.name: {(p.endpoint, p.name) for p in n.pins} for n in nets}
    # Native local labels are sheet-qualified by KiCad. The hand-authored XML
    # fixtures intentionally use unqualified names. Preserve native identities;
    # compare their explicitly expected root-sheet namespace and all endpoints.
    assert memberships(actual) == {"/" + name: pins for name, pins in memberships(expected).items()}


@pytest.mark.parametrize("target", ["stm32f401re", "atmega328p"])
def test_native_kicad_profiles_compile_and_preserve_qualified_net_names(tmp_path, target):
    require_tool("kicad-cli")
    for tool in (["clang", "arm-none-eabi-gcc", "dtc", "fdtoverlay"]
                 if target.startswith("stm") else ["avr-gcc"]):
        require_tool(tool)
    source = tmp_path / "inputs"
    shutil.copytree(ROOT / "sources" / target, source, ignore=shutil.ignore_patterns("imports"))
    profile_path = source / "profile.json"
    profile = json.loads(profile_path.read_text())
    profile["netlist"] = "schematic"
    profile["signal_aliases"] = {"/" + name: aliases for name, aliases in profile["signal_aliases"].items()}
    profile_path.write_text(json.dumps(profile))
    output = compile_bundle(profile_path, tmp_path / "native")
    bundle = Bundle(output)
    assert "kicad-cli" in bundle.manifest.extractor_versions
    assert "| /UART_RX |" in bundle.read(bundle.manifest.netlist)

