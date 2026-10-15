"""Publication policy must generalize through data without losing evidence gates."""
import json
import shutil

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle, digest
from praxis.compiler import compile_bundle
from praxis.contracts import load_contract
from praxis.errors import PraxisError
from praxis.models import Profile
from praxis.routing import Session


def save(path, data):
    path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")


@pytest.fixture
def inputs(tmp_path):
    root = tmp_path / "inputs"
    shutil.copytree(ROOT / "sources/synthetic-cortex-m3", root)
    path = root / "profile.json"
    profile = json.loads(path.read_text())
    source = next(s for s in profile["sources"] if s["id"] == profile["compilation_contract"])
    contract = json.loads((root / source["path"]).read_text())
    return path, profile, source, contract


def repin(path, profile, source, contract):
    contract_path = path.parent / source["path"]
    save(contract_path, contract)
    source["expected_sha256"] = digest(contract_path.read_bytes())
    save(path, profile)


@pytest.mark.parametrize("mutation,code", [
    ("missing", "INVALID_PROFILE"), ("unregistered", "UNKNOWN_SOURCE"),
    ("unpinned", "INVALID_CONTRACT"), ("authority", "INVALID_CONTRACT"),
    ("tamper", "SOURCE_HASH_MISMATCH"), ("target", "TARGET_MISMATCH"),
    ("cpu", "TARGET_MISMATCH"), ("references", "UNKNOWN_SOURCE"),
    ("duplicate", "INVALID_CONTRACT"), ("range", "INVALID_CONTRACT"),
    ("executable", "INVALID_CONTRACT"),
])
def test_invalid_policy_fails_before_extractors(inputs, tmp_path, monkeypatch, mutation, code):
    path, profile, source, contract = inputs
    if mutation == "missing":
        del profile["compilation_contract"]
    elif mutation == "unregistered":
        profile["compilation_contract"] = "absent"
    elif mutation == "unpinned":
        source.pop("expected_sha256")
    elif mutation == "authority":
        source["authority"] = "semantics"
    elif mutation == "target":
        contract["mcu"] = "ANOTHER-PART"
    elif mutation == "cpu":
        contract["cpu"] = "cortex-m7"
    elif mutation == "references":
        contract["sources"][0]["source"] = "unknown"
    elif mutation == "duplicate":
        contract["required_registers"] = {"uart": ["CTRL", "CTRL"]}
    elif mutation == "range":
        contract["clock_plan"] = {"frequency": {"minimum": 10, "maximum": 1}}
    elif mutation == "executable":
        contract["command"] = "python untrusted.py"
    if mutation == "tamper":
        (path.parent / source["path"]).write_bytes(b"{}")
        save(path, profile)
    else:
        # Leave intentionally absent/malformed registration untouched.
        if mutation not in ("unpinned", "authority", "missing", "unregistered"):
            repin(path, profile, source, contract)
        else:
            save(path, profile)
    monkeypatch.setattr("praxis.compiler._definitions", lambda *a: pytest.fail("Policy must validate first"))
    output = tmp_path / "bundle"
    with pytest.raises(PraxisError, match=code):
        compile_bundle(path, output)
    assert not output.exists()


def test_declared_minimum_is_not_bypassed_by_empty_profile_requirements(inputs, tmp_path):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    path, profile, source, contract = inputs
    contract["required_registers"] = {"uart": ["CTRL"]}
    profile["header"]["required_registers"] = {}
    repin(path, profile, source, contract)
    with pytest.raises(PraxisError, match="UNREVIEWED_REQUIRED_FACT.*CTRL"):
        compile_bundle(path, tmp_path / "bundle")
    assert not (tmp_path / "bundle").exists()


def test_new_names_views_and_routes_need_data_changes_only(inputs, tmp_path):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    path, profile, source, contract = inputs
    names = {"clock": "energy", "pins": "pads", "uart": "serial_port", "interrupts": "events"}
    policy = profile["discovery"]["peripherals"]
    profile["discovery"]["peripherals"] = {
        names[name]: {**spec, "prerequisites": [names[p] for p in spec["prerequisites"]]}
        for name, spec in policy.items()}
    profile["discovery"]["peripherals"]["pads"]["member_views"] = {"ROUTE": ["INPUT_PATH", "OUTPUT_PATH"]}
    profile["workflows"] = {}
    contract.update(pin_document="pads", board_prerequisites=["energy", "pads"])
    repin(path, profile, source, contract)
    first = Bundle(compile_bundle(path, tmp_path / "first"))
    second = Bundle(compile_bundle(path, tmp_path / "second"))
    assert first.manifest.bundle_revision == second.manifest.bundle_revision
    assert first.documents == second.documents
    assert first.dependencies == {"energy": [], "pads": ["energy"], "serial_port": ["pads"], "events": ["serial_port"]}
    text = first.read("wiki/peripherals/pads.md")
    assert "INPUT_PATH | 0x000 | 32" in text and "OUTPUT_PATH | 0x004 | 32" in text
    assert "vendor_blocks:PINMUX_Type.ROUTE[1]" in text
    assert "profile:discovery.peripherals.pads.member_views.ROUTE" in text
    session = Session(first)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match="retrieve in order: energy, pads"):
        session.read_peripheral_doc("serial_port")
    for name in ("energy", "pads", "serial_port", "events"):
        session.read_peripheral_doc(name)
    assert "[[peripherals/pads]]" in session.query_schematic_netlist("UART0_TX")
    assert "compilation_policy" in first.read("wiki/policy.md")
    assert not any("peripherals/" + forbidden in first.read("wiki/index.md")
                   for forbidden in ("rcc", "gpio", "usart", "nvic"))


def test_all_shipped_source_profiles_have_explicit_pinned_policy():
    paths = [p for p in (ROOT / "sources").rglob("profile*.json") if p.parent.name != "contracts"]
    assert paths
    for path in paths:
        profile = Profile.model_validate_json(path.read_bytes())
        assert load_contract(profile, path.parent).mcu == profile.target.mcu


def test_pinned_array_view_cannot_be_silently_overridden(inputs, tmp_path):
    require_tool("arm-none-eabi-gcc")
    require_tool("clang")
    path, profile, source, contract = inputs
    contract["member_views"] = {"pins": {"ROUTE": ["INPUT_PATH", "OUTPUT_PATH"]}}
    profile["discovery"]["peripherals"]["pins"]["member_views"] = {"ROUTE": ["OTHER_A", "OTHER_B"]}
    repin(path, profile, source, contract)
    with pytest.raises(PraxisError, match="DISCOVERY_BLOCKED.*pinned publication policy"):
        compile_bundle(path, tmp_path / "bundle")
    assert not (tmp_path / "bundle").exists()
