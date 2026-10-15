"""F407 declaration completeness, source conflicts, publication, and real ABI checks."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from praxis.bundle import Bundle
from praxis.compiler import compile_bundle, parse_cmsis_headers, parse_device_tree, parse_kicad_netlist
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.jsonio import load_json
from praxis.models import Profile
from praxis.routing import Session
from praxis.verify import command
from conftest import ROOT, require_tool

SOURCE = ROOT / "sources/stm32f407vgt6"


@pytest.fixture(scope="module")
def catalog():
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    return parse_cmsis_headers(SOURCE / "raw/vendor/stm32f407xx.h", defines=["-DSTM32F407xx"])


@pytest.fixture(scope="module")
def compiled(tmp_path_factory):
    for tool in ("arm-none-eabi-gcc", "clang", "gcc", "dtc", "fdtoverlay"):
        require_tool(tool)
    destination = tmp_path_factory.mktemp("f407") / "bundle"
    compile_bundle(SOURCE / "profile.json", destination)
    return Bundle(destination)


@pytest.fixture
def inputs(tmp_path):
    for tool in ("arm-none-eabi-gcc", "clang", "gcc", "dtc", "fdtoverlay"):
        require_tool(tool)
    destination = tmp_path / "inputs"
    shutil.copytree(SOURCE, destination, ignore=shutil.ignore_patterns("imports"))
    return destination


def change_json(path, update):
    data = json.loads(path.read_text())
    update(data)
    path.write_text(json.dumps(data, indent=2) + "\n")


def test_complete_maps_masks_arrays_and_reserved_gaps(catalog):
    assert {name: len(doc.registers) for name, doc in catalog.items()} == {
        "rcc": 23, "gpio": 10, "usart": 7, "nvic": 7}
    assert sum(len(r.fields) for p in catalog.values() for r in p.registers) == 463
    rcc = {r.name: r for r in catalog["rcc"].registers}
    assert rcc["AHB1ENR"].offset == 0x30
    assert rcc["APB1ENR"].offset == 0x40
    assert rcc["PLLI2SCFGR"].offset == 0x84
    assert all(not r.name.startswith("RESERVED") for r in rcc.values())
    ue = next(f for r in catalog["usart"].registers if r.name == "CR1" for f in r.fields if f.name == "UE")
    assert (ue.lsb, ue.width, ue.mask) == (13, 1, 0x2000)
    nvic = {r.name: r for r in catalog["nvic"].registers}
    assert (nvic["ICPR"].offset, nvic["ICPR"].count, nvic["ICPR"].width) == (0x180, 8, 32)
    assert (nvic["IP"].offset, nvic["IP"].count, nvic["IP"].width) == (0x300, 240, 8)
    assert nvic["IP"].fields[0].mask == 0xF0
    assert nvic["STIR"].offset == 0xE00
    assert catalog["usart"].instances["USART2"] == 0x40004400
    assert catalog["rcc"].instances["RCC"] == 0x40023800
    # Header qualifiers and absent reset macros must not create invented facts.
    assert all(r.access == "unknown" and r.reset is None for p in catalog.values() for r in p.registers)


def test_declared_reset_macros_only(inputs):
    path = inputs / "raw/vendor/stm32f407xx.h"
    with path.open("a") as handle:
        handle.write("\n#define USART_BRR_RESET_VALUE 0x42UL\n")
    found = parse_cmsis_headers(path)
    assert next(r for r in found["usart"].registers if r.name == "BRR").reset == 0x42
    assert next(r for r in found["usart"].registers if r.name == "CR1").reset is None
    with path.open("a") as handle:
        handle.write("#define USART_BRR_RESET 0x43UL\n")
    with pytest.raises(PraxisError, match="DECLARATION_CONFLICT"):
        parse_cmsis_headers(path)


def test_reset_command_bit_is_not_a_register_reset_value(inputs):
    path = inputs / "raw/vendor/stm32f407xx.h"
    with path.open("a") as handle:
        handle.write("\n#define USART_CR1_RESET_Pos 0U\n"
                     "#define USART_CR1_RESET_Msk (1UL << USART_CR1_RESET_Pos)\n"
                     "#define USART_CR1_RESET USART_CR1_RESET_Msk\n")
    # Select the original UE field view to avoid an intentionally overlapping
    # synthetic bit; the RESET macro remains visible to reset-value detection.
    found = parse_cmsis_headers(path, register_fields={"usart": {"CR1": ["UE"]}})
    assert next(r for r in found["usart"].registers if r.name == "CR1").reset is None


def test_generated_bundle_target_limits_sources_and_hedg(compiled):
    index = compiled.read("wiki/index.md")
    assert "STM32F407VGT6" in index and "LQFP-100" in index
    assert "PCLK1=42 MHz" in index and "SYSCLK=HCLK=168 MHz" in index
    assert compiled.read("wiki/peripherals/usart.md").endswith("\n")
    assert all(text.count("## Register map") == 1 and text.count("## Bit fields") == 1
               for path, text in compiled.documents.items() if path.startswith("wiki/peripherals/"))
    assert "cmsis_core:NVIC_Type.IP" in compiled.read("wiki/peripherals/nvic.md")
    assert "clock_review:SystemClock_Config" in compiled.read("wiki/peripherals/rcc.md")
    assert "header:RCC_AHB1ENR_GPIOAEN_Msk" in compiled.read("wiki/peripherals/rcc.md")
    assert evaluate(compiled)["passed"]
    session = Session(compiled)
    with pytest.raises(PraxisError, match="PREREQUISITE_REQUIRED"):
        session.read_peripheral_doc("usart2")
    session.read_wiki_index()
    assert "U1:25" in session.query_schematic_netlist("PA2")
    assert "U1:26" in session.query_schematic_netlist("USART2_RX")
    assert session.query_schematic_netlist("PA20").startswith("No match")
    assert "J1:1" not in session.query_schematic_netlist("USART2_TX")  # resistor keeps nets distinct
    assert session.served == {"index"}
    for peripheral in ("rcc", "gpio", "usart", "nvic"):
        assert session.read_peripheral_doc(peripheral) == compiled.read(f"wiki/peripherals/{peripheral}.md")


def test_adapter_topology_is_configuration_not_af_inference():
    profile = Profile.model_validate_json((SOURCE / "profile.json").read_bytes())
    nets = parse_kicad_netlist(SOURCE / "raw/netlist.xml", target=profile.target, pin_map=profile.pin_map)
    tx = next(n for n in nets if n.name == "UART_TX_MCU")
    assert {(p.endpoint, p.name) for p in tx.pins} == {("U1:25", "PA2"), ("R1:1", "1")}
    for tool in ("gcc", "dtc", "fdtoverlay"):
        require_tool(tool)
    nodes = parse_device_tree(SOURCE / "raw/topology.dts", overlays=[SOURCE / "raw/enable_uart.dtso"])
    uart = next(n for n in nodes if n.path == "/bus/serial@4400")
    assert uart.enabled and uart.decoded["interrupts"][0]["args"] == [38]
    assert uart.decoded["reg"][0]["address"] == 0x40004400
    assert uart.decoded["clocks"][0]["provider"] == "/clock"
    clock = next(n for n in nodes if n.path == "/clock")
    assert int(clock.properties["clock-frequency"], 16) == 42_000_000


def test_byte_identical_across_different_input_locations(inputs, compiled, tmp_path):
    second = tmp_path / "another-bundle"
    compile_bundle(inputs / "profile.json", second)
    original = {p.relative_to(compiled.root): p.read_bytes() for p in compiled.root.rglob("*") if p.is_file()}
    rebuilt = {p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()}
    assert original == rebuilt
    assert compile_bundle(inputs / "profile.json", second) == second


@pytest.mark.parametrize("kind,code", [
    ("required", "UNREVIEWED_REQUIRED_FACT"), ("offset", "DECLARATION_CONFLICT"),
    ("field", "DECLARATION_CONFLICT"), ("duplicate", "DUPLICATE_ENTITY"),
    ("package", "PACKAGE_MISMATCH"), ("pin", "PIN_MISMATCH"),
    ("link", "BROKEN_LINK"), ("oversized", None),
    ("encoding", "INVALID_ENCODING"), ("include", "UNREGISTERED_INCLUDE"),
    ("macro", "UNSUPPORTED_EXPRESSION"), ("clock", "INVALID_PROFILE"),
])
def test_invalid_inputs_never_publish(inputs, tmp_path, kind, code):
    definitions = inputs / "reviewed/peripherals.json"
    if kind == "required":
        change_json(definitions, lambda data: data[0]["registers"].__setitem__(slice(None),
                    [r for r in data[0]["registers"] if r["name"] != "PLLCFGR"]))
        # Removing the optional profile list cannot bypass the F407 minimum workflow.
        change_json(inputs / "profile.json", lambda data: data["header"].update(required_registers={}))
    elif kind == "offset":
        change_json(definitions, lambda data: data[0]["registers"][0].update(offset=0x100))
    elif kind == "field":
        change_json(definitions, lambda data: data[0]["registers"][0]["fields"][0].update(lsb=31, mask=1 << 31))
    elif kind == "duplicate":
        change_json(definitions, lambda data: data.append(data[0]))
    elif kind in ("package", "pin"):
        path = inputs / "raw/netlist.xml"
        text = path.read_text().replace("LQFP-100_14x14mm", "LQFP-64_10x10mm") if kind == "package" else path.read_text().replace('pin="25"', 'pin="16"')
        path.write_text(text)
    elif kind in ("link", "oversized"):
        with (inputs / "reviewed/usart.md").open("a") as handle:
            handle.write("\n[[peripherals/absent]]\n" if kind == "link" else "x" * 200_000)
    elif kind == "encoding":
        (inputs / "reviewed/usart.md").write_bytes(b"\xff\xfe")
    elif kind == "include":
        (inputs / "raw/vendor/unregistered.h").write_text("#define NEW_FACT 1\n")
        with (inputs / "raw/vendor/stm32f407xx.h").open("a") as handle:
            handle.write('\n#include "unregistered.h"\n')
    elif kind == "macro":
        with (inputs / "raw/vendor/stm32f407xx.h").open("a") as handle:
            handle.write("\n#undef RCC_PLLCFGR_PLLM_Msk\n#define RCC_PLLCFGR_PLLM_Msk forbidden_call(3)\n")
    elif kind == "clock":
        change_json(inputs / "profile.json", lambda data: data["clock_plan"].update(apb1_div=2))
    out = tmp_path / "bad-bundle"
    if kind == "oversized":
        published = Bundle(compile_bundle(inputs / "profile.json", out))
        assert "x" * 200_000 in published.read("wiki/peripherals/usart.md")
        return
    with pytest.raises(PraxisError, match=code):
        compile_bundle(inputs / "profile.json", out)
    assert not out.exists()
    assert not list(tmp_path.glob(".praxis-staging-*"))


def test_duplicate_json_keys_fail_instead_of_overwriting():
    with pytest.raises(PraxisError, match="DUPLICATE_IDENTITY"):
        load_json('{"aliases":{"usart2":"usart","usart2":"rcc"}}')


def test_header_identity_cannot_cross_targets(inputs, tmp_path):
    path = inputs / "raw/vendor/stm32f407xx.h"
    path.write_text(path.read_text().replace("__STM32F407xx_H", "__STM32F401xE_H"))
    with pytest.raises(PraxisError, match="TARGET_MISMATCH"):
        compile_bundle(inputs / "profile.json", tmp_path / "wrong-target")


@pytest.mark.parametrize("kind", ["cpp", "dtc", "incbin"])
def test_transitive_dts_dependencies_need_provenance(tmp_path, kind):
    require_tool("gcc")
    require_tool("dtc")
    source = tmp_path / "board.dts"
    dependency = tmp_path / ("payload.bin" if kind == "incbin" else "common.dtsi")
    if kind == "cpp":
        dependency.write_text("#define CLOCK_HZ 42000000\n")
        source.write_text('/dts-v1/;\n#include "common.dtsi"\n/ { clock-frequency = <CLOCK_HZ>; };\n')
    elif kind == "dtc":
        dependency.write_text("clock-frequency = <42000000>;\n")
        source.write_text('/dts-v1/; / { /include/ "common.dtsi" };\n')
    else:
        dependency.write_bytes(b"fixture")
        source.write_text('/dts-v1/; / { example = /incbin/("payload.bin"); };\n')
    with pytest.raises(PraxisError, match="UNREGISTERED_INCLUDE"):
        parse_device_tree(source, registered_sources=[source])
    nodes = parse_device_tree(source, registered_sources=[source, dependency])
    assert nodes[0].path == "/"
    if kind == "incbin":
        assert "example" in nodes[0].unresolved
    else:
        assert int(nodes[0].properties["clock-frequency"], 16) == 42_000_000


def test_xml_dtd_and_external_entity_disabled(tmp_path):
    profile = Profile.model_validate_json((SOURCE / "profile.json").read_bytes())
    path = tmp_path / "entity.xml"
    path.write_text('<!DOCTYPE export [<!ENTITY secret SYSTEM "file:///etc/passwd">]><export>&secret;</export>')
    with pytest.raises(PraxisError, match="INVALID_NETLIST"):
        parse_kicad_netlist(path, target=profile.target, pin_map=profile.pin_map)


def test_root_compiler_cli_from_unrelated_directory(tmp_path):
    result = subprocess.run([sys.executable, str(ROOT / "compiler.py"), "--profile", str(tmp_path / "absent.json"),
                             "--output", str(tmp_path / "output")], cwd=tmp_path,
                            capture_output=True, text=True, timeout=5, check=False)
    assert result.returncode == 2 and result.stderr.startswith("INPUT_ERROR:")
    assert not result.stdout and "Traceback" not in result.stderr


def test_real_arm_header_static_assertions(catalog, tmp_path):
    assertions = ['#include <stddef.h>', '#include "stm32f407xx.h"']
    for declaration in catalog.values():
        for register in declaration.registers:
            member = declaration.members[register.name]
            assertions.append(f'_Static_assert(offsetof({declaration.structure}, {member}) == {register.offset}, "offset");')
            if "[" not in member:
                assertions.append(f'_Static_assert(sizeof((({declaration.structure} *)0)->{member}) == {register.count * register.width // 8}, "array size");')
    assertions.extend(['_Static_assert(USART2_IRQn == 38, "irq");',
                       '_Static_assert(USART_CR1_UE == 0x2000U, "UE mask");',
                       '_Static_assert(RCC_BASE == 0x40023800U, "RCC base");',
                       '_Static_assert(USART2_BASE == 0x40004400U, "USART2 base");'])
    unit = tmp_path / "assertions.c"
    unit.write_text("\n".join(assertions) + "\n")
    args = ["arm-none-eabi-gcc", "-mcpu=cortex-m4", "-mthumb", "-mfloat-abi=soft", "-DSTM32F407xx",
            "-std=c11", "-ffreestanding", "-Wall", "-Wextra", "-Werror", "-fsyntax-only",
            f"-I{SOURCE / 'raw/vendor'}", str(unit)]
    result = subprocess.run(args, capture_output=True, text=True, timeout=30, check=False)
    assert result.returncode == 0, result.stderr
    # A plausible but wrong offset must fail the same real compiler.
    unit.write_text('#include <stddef.h>\n#include "stm32f407xx.h"\n_Static_assert(offsetof(RCC_TypeDef, AHB1ENR) == 0x34, "wrong offset");\n')
    result = subprocess.run(args, capture_output=True, text=True, timeout=30, check=False)
    assert result.returncode != 0 and "wrong offset" in result.stderr


def test_f407_verification_cannot_select_f401_define():
    args = command("sha256:" + "a" * 64, "stm32", Path("/tmp/src"), Path("/tmp/headers"),
                   Path("/tmp/out"), "driver.c", "syntax", 168_000_000, "test", mcu="STM32F407VGT6")
    assert "-DSTM32F407xx" in args and "-DSTM32F401xE" not in args
