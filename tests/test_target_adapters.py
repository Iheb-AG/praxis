"""Cross-vendor knowledge extraction never inherits target firmware qualification."""

import json
import shutil

import pytest
from pydantic import ValidationError

from conftest import ROOT, require_tool
from praxis.adapters.discovery import parse_cmsis_headers
from praxis.adapters.headers import cmsis
from praxis.bundle import Bundle, revision
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.firmware_assets import FirmwareAssets
from praxis.models import MAX_DOCUMENT_BYTES, Profile, Target
from praxis.routing import Session
from praxis.verify import verify

SOURCE = ROOT / "sources/synthetic-cortex-m3"


@pytest.fixture(scope="module")
def compiled(tmp_path_factory):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    return Bundle(compile_bundle(SOURCE / "profile.json", tmp_path_factory.mktemp("adapter") / "bundle"))


def test_generic_layout_macro_conventions_and_provenance(compiled):
    text = compiled.read("wiki/peripherals/uart.md")
    assert "UART0 | 0x40002000" in text
    assert "DATA | 0x010 | 8" in text
    assert "CTRL | ENABLE | 2:2 | 0x4" in text
    assert "vendor_blocks:UART_Type.DATA" in text
    assert "header:UART_CTRL_ENABLE_MASK" in text
    assert "header:UART0_BASE" in text
    assert "header:UART_CTRL_RESET_VALUE" in text
    assert "Not reviewed." in text
    assert "CMSIS" not in compiled.manifest.target.mcu
    assert all(len(text.encode()) <= MAX_DOCUMENT_BYTES for text in compiled.documents.values())
    index = compiled.read("wiki/index.md")
    assert "cortex-m3" in index and "knowledge-only target" in index
    assert "peripherals/rcc" not in index and "peripherals/gpio" not in index


def test_unreviewed_workflow_and_target_specific_route(compiled):
    report = json.loads(compiled.read("wiki/coverage.md").split("```json\n")[1].split("\n```", 1)[0])
    assert report["counts"]["published"] == 4
    assert report["counts"]["reviewed_subsets"] == 0
    assert not report["workflows"]["uart_polling"]["ready"]
    assert compiled.dependencies == {"clock": [], "pins": ["clock"], "uart": ["pins"], "interrupts": ["uart"]}
    session = Session(compiled)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match="retrieve in order: clock, pins"):
        session.read_peripheral_doc("uart0")
    mapping = session.query_schematic_netlist("UART0_TX")
    assert "U1:1" in mapping and "J1:1" in mapping and "schematic:net:TX" in mapping
    assert session.query_schematic_netlist("P0_20").startswith("No match")
    for name in ("clock", "pins", "uart0", "interrupts"):
        assert session.read_peripheral_doc(name)
    assert evaluate(compiled)["passed"]


def test_generic_generation_is_location_independent(compiled, tmp_path):
    source = tmp_path / "other-inputs"
    shutil.copytree(SOURCE, source)
    other = compile_bundle(source / "profile.json", tmp_path / "other-bundle")
    assert Bundle(other).manifest.bundle_revision == compiled.manifest.bundle_revision
    assert {p.relative_to(other): p.read_bytes() for p in other.rglob("*") if p.is_file()} == {
        p.relative_to(compiled.root): p.read_bytes() for p in compiled.root.rglob("*") if p.is_file()}


@pytest.mark.parametrize("mutation,code", [
    ("identity", "TARGET_MISMATCH"), ("wrong_cpu", "EXTRACTOR_FAILED"),
    ("unregistered_include", "UNREGISTERED_INCLUDE"), ("wrong_package", "PACKAGE_MISMATCH"),
    ("required_workflow", "PUBLICATION_BLOCKED"), ("cycle", "DEPENDENCY_CYCLE"),
    ("mask", "DISCOVERY_BLOCKED"),
])
def test_bad_custom_inputs_never_publish(tmp_path, mutation, code):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    source = tmp_path / "inputs"
    shutil.copytree(SOURCE, source)
    path = source / "profile.json"
    data = json.loads(path.read_text())
    if mutation == "identity":
        data["target"]["knowledge_adapter"]["header_identity"] = ["ANOTHER_PART"]
    elif mutation == "wrong_cpu":
        data["target"]["knowledge_adapter"]["cpu"] = "cortex-m4"
    elif mutation == "unregistered_include":
        data["sources"] = [s for s in data["sources"] if s["id"] != "vendor_blocks"]
    elif mutation == "wrong_package":
        data["target"]["package"] = "Fixture:WrongPackage"
    elif mutation == "required_workflow":
        data["publication_requires"] = ["uart_polling"]
    elif mutation == "cycle":
        data["discovery"]["peripherals"]["clock"]["prerequisites"] = ["interrupts"]
    else:
        data["discovery"]["peripherals"]["uart"]["register_fields"] = {"CTRL": ["ENABLE"]}
        header = source / "raw/demo_m3.h"
        header.write_text(header.read_text().replace("UART_CTRL_ENABLE_SHIFT 2U", "UART_CTRL_ENABLE_SHIFT 33U"))
    path.write_text(json.dumps(data))
    output = tmp_path / "bundle"
    with pytest.raises(PraxisError, match=code):
        compile_bundle(path, output)
    assert not output.exists()


def test_optional_unsupported_masks_are_withheld_and_reported(tmp_path):
    require_tool("arm-none-eabi-gcc")
    source = tmp_path / "inputs"
    shutil.copytree(SOURCE, source)
    header = source / "raw/demo_m3.h"
    header.write_text(header.read_text().replace("UART_CTRL_ENABLE_SHIFT 2U", "UART_CTRL_ENABLE_SHIFT 33U"))
    bundle = Bundle(compile_bundle(source / "profile.json", tmp_path / "bundle"))
    text = bundle.read("wiki/peripherals/uart.md")
    assert "bit fields withheld" in text and "0x200000000" not in text
    assert '"status":"partial_declarations"' in bundle.read("wiki/coverage.md")


@pytest.mark.parametrize("mutation", ["no_adapter", "builtin_family", "builtin_mcu", "cpu_flags", "empty_guard", "no_discovery", "avr_header"])
def test_profile_configuration_is_explicit_and_cannot_spoof_builtins(mutation):
    data = json.loads((SOURCE / "profile.json").read_text())
    if mutation == "no_adapter":
        del data["target"]["knowledge_adapter"]
    elif mutation == "builtin_family":
        data["target"]["family"] = "stm32"
    elif mutation == "builtin_mcu":
        data["target"]["mcu"] = "STM32F407VGT6"
    elif mutation == "cpu_flags":
        data["target"]["knowledge_adapter"]["cpu"] = "cortex-m3 -fplugin=attack"
    elif mutation == "empty_guard":
        data["target"]["knowledge_adapter"]["header_identity"] = []
    elif mutation == "no_discovery":
        del data["discovery"]
    else:
        data["header"]["kind"] = "avr"
    with pytest.raises(ValidationError):
        Profile.model_validate(data)


def test_legacy_manifest_hashes_and_target_dump_are_unchanged():
    for directory in sorted((ROOT / "bundles").iterdir()):
        if not (directory / "manifest.json").is_file():
            continue
        bundle = Bundle(directory)
        if bundle.manifest.target.knowledge_adapter is None:
            assert "knowledge_adapter" not in bundle.manifest.model_dump()["target"]
            assert revision(bundle.manifest.model_dump()) == bundle.manifest.bundle_revision
            assert "knowledge_adapter" not in json.loads(bundle.manifest.target.model_dump_json())
    target = Target.model_validate(json.loads((ROOT / "sources/atmega328p/profile.json").read_text())["target"])
    assert "knowledge_adapter" not in target.model_dump()


def test_custom_target_cannot_use_existing_assets_or_verifier(compiled, tmp_path, monkeypatch):
    assets = next((ROOT / "assets").glob("*/manifest.json")).parent
    with pytest.raises(PraxisError, match="TARGET_MISMATCH"):
        FirmwareAssets(assets, compiled)
    def forbidden(*args, **kwargs):
        pytest.fail("Knowledge-only target must fail before invoking a container or compiler")
    monkeypatch.setattr("praxis.verify._rootless", forbidden)
    with pytest.raises(PraxisError, match="UNSUPPORTED_FIRMWARE_TARGET"):
        verify(compiled.root, tmp_path / "absent", "syntax", tmp_path / "absent-lock", tmp_path / "output")
    assert not (tmp_path / "output").exists()


def test_custom_gpio_arrays_are_not_reinterpreted_as_stm32(tmp_path):
    require_tool("arm-none-eabi-gcc")
    header = tmp_path / "gpio.h"
    header.write_text("typedef struct { unsigned int AFR[3]; } GPIO_Type;\n"
                      "#define GPIO0_BASE 0x40000000UL\n#define GPIO0 ((GPIO_Type *) GPIO0_BASE)\n")
    item = parse_cmsis_headers(header, structures={"gpio": "GPIO_Type"}, stm32_views=False)["gpio"]
    assert [(r.name, r.count) for r in item.registers] == [("AFR", 3)]
    assert item.registers[0].sources[0].source == "header"


@pytest.mark.parametrize("cpu", ["cortex-m0", "cortex-m0plus", "cortex-m3", "cortex-m4", "cortex-m7"])
def test_declared_cpu_is_used_by_clang(tmp_path, cpu):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    expected = "__ARM_ARCH_6M__" if cpu in ("cortex-m0", "cortex-m0plus") else "__ARM_ARCH_7M__" if cpu == "cortex-m3" else "__ARM_ARCH_7EM__"
    header = tmp_path / "cpu.h"
    header.write_text(f"#ifndef {expected}\n#error Wrong CPU\n#endif\n"
                      "typedef struct { unsigned int CTRL; } CPU_Type;\n")
    assert cmsis(header, ["CPU_Type"], [], cpu=cpu)["CPU_Type"]["CTRL"]["width"] == 32


async def test_real_stdio_generic_bundle(compiled, tmp_path):
    from tools.check_bundle_mcp import check
    report = await check(compiled.root, "uart0", "UART0_TX", tmp_path)
    assert report["passed"] and report["calls"] == 14
    assert report["target"]["family"] == "praxis_demo"
    assert (tmp_path / "report.json").is_file()


def test_ingestion_identity_cannot_switch_adapter(tmp_path, monkeypatch):
    from praxis.ingestion_server import IngestionService
    source = tmp_path / "inputs"
    shutil.copytree(SOURCE, source)
    catalog = tmp_path / "catalog.json"
    catalog.write_text(json.dumps({"schema_version": 1, "allowed_hosts": ["example.invalid"],
        "sources": [{"id": "placeholder", "target": "PRAXIS-DEMO-M3",
                     "url": "https://example.invalid/unavailable", "kind": "text"}]}))
    service = IngestionService(source / "profile.json", catalog, tmp_path / "archives",
                               tmp_path / "published", [])
    assert "knowledge adapter" in service.describe()["extraction_scope"]
    data = json.loads((source / "profile.json").read_text())
    data["target"]["knowledge_adapter"]["header_identity"].append("PRAXIS_DEMO_BLOCKS_H")
    (source / "changed.json").write_text(json.dumps(data))
    def forbidden(*args, **kwargs):
        pytest.fail("Changed extraction identity must fail before compilation")
    monkeypatch.setattr("praxis.compiler.compile_bundle", forbidden)
    with pytest.raises(PraxisError, match="TARGET_MISMATCH"):
        service.publish("changed.json", "changed-bundle")
    assert not (tmp_path / "published").exists()


@pytest.mark.parametrize("missing", [False, True])
def test_explicit_structure_names_and_missing_structure_errors(tmp_path, missing):
    require_tool("arm-none-eabi-gcc")
    source = tmp_path / "inputs"
    shutil.copytree(SOURCE, source)
    for name in ("demo_m3.h", "vendor_blocks.h"):
        path = source / "raw" / name
        path.write_text(path.read_text().replace("UART_Type", "uart_registers_t"))
    path = source / "profile.json"
    data = json.loads(path.read_text())
    uart = data["discovery"]["peripherals"]["uart"]
    uart["structure"] = "MissingType" if missing else "uart_registers_t"
    if missing:
        uart["instances"] = {"UART0": "UART0_BASE"}
    path.write_text(json.dumps(data))
    if missing:
        with pytest.raises(PraxisError, match="Structure not declared: MissingType"):
            compile_bundle(path, tmp_path / "bundle")
        assert not (tmp_path / "bundle").exists()
    else:
        bundle = Bundle(compile_bundle(path, tmp_path / "bundle"))
        assert "vendor_blocks:uart_registers_t.DATA" in bundle.read("wiki/peripherals/uart.md")


def test_topology_only_custom_bundle_has_a_valid_evaluation(tmp_path):
    require_tool("arm-none-eabi-gcc")
    source = tmp_path / "inputs"
    shutil.copytree(SOURCE, source)
    path = source / "profile.json"
    data = json.loads(path.read_text())
    data["discovery"]["peripherals"] = {}
    path.write_text(json.dumps(data))
    bundle = Bundle(compile_bundle(path, tmp_path / "bundle"))
    assert not bundle.manifest.peripherals
    assert evaluate(bundle)["passed"]


def test_new_stm32_knowledge_profile_remains_separate_from_firmware_support():
    from praxis.targets import require_firmware_target
    data = json.loads((SOURCE / "profile.json").read_text())
    data["target"]["family"] = "stm32"
    data["target"]["mcu"] = "STM32DEMO1234"  # Fictional identity for schema behavior only.
    profile = Profile.model_validate(data)
    assert profile.target.knowledge_adapter.cpu == "cortex-m3"
    with pytest.raises(PraxisError, match="UNSUPPORTED_FIRMWARE_TARGET"):
        require_firmware_target(profile.target)
    for model in ("STM32F401RE", "STM32F407VGT6"):
        data["target"]["mcu"] = model
        with pytest.raises(ValidationError, match="cannot override"):
            Profile.model_validate(data)
