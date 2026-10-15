import json
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from praxis.adapters.outline import prepare
from praxis.bundle import digest
from praxis.capability_inventory import InventorySpec, from_spec, markdown
from praxis.errors import PraxisError
from test_source_outline import SOURCE, pages


@pytest.fixture
def scope(tmp_path, monkeypatch):
    outline = prepare(pages(), source=SOURCE)
    raw = json.dumps(outline).encode()
    (tmp_path / "outline.json").write_bytes(raw)
    target = dict(id="test_target", mcu="TEST-MCU", package="LQFP", board_revision="R1")
    spec = dict(format="praxis-capability-inventory-v1", target=target, scope="Proposed test inventory",
        documents=[dict(id="vendor_manual", path="outline.json", sha256=digest(raw), revision_label="Rev 1")],
        bindings=[dict(document="vendor_manual", section="1", applicability="applicable",
            rationale="Synthetic memory scope", peripherals=["memory"], workflows=["polling"]),
            dict(document="vendor_manual", section="1.2", applicability="excluded",
                 rationale="Synthetic target excludes this scope")],
        missing_sources=[dict(id="errata", reason="Revision review required")])
    path = tmp_path / "inventory.json"
    path.write_text(json.dumps(spec))
    reference = target.copy()
    target_object = SimpleNamespace(model_dump=lambda: reference.copy())
    bundle = SimpleNamespace(manifest=SimpleNamespace(target=target_object,
        peripherals={"memory": "wiki/peripherals/memory.md"}, bundle_revision="d" * 64))
    monkeypatch.setattr("praxis.capability_inventory.assess", lambda _: {
        "workflows": {"polling": {"knowledge_ready": True, "issues": []}}})
    monkeypatch.setattr("praxis.capability_inventory.read_report", lambda *_: {
        "peripherals": {"memory": {"published": True}}})
    return path, spec, bundle


def test_source_scope_and_narrow_ready_workflows_never_become_full_support(scope):
    path, _, bundle = scope
    report = from_spec(bundle, path)
    assert from_spec(bundle, path) == report
    assert report["counts"]["indexed_sections"] == 5
    rows = {row["section"]: row for row in report["sections"]}
    assert rows["1.1"]["binding_section"] == "1"
    assert rows["1.2"]["binding_section"] == "1.2" and rows["1.2"]["applicability"] == "excluded"
    assert rows["1.1"]["related_workflows"]["polling"]["knowledge_ready"]
    assert rows["2"]["applicability"] == "pending"
    assert all(row["all_section_modes_supported"] is False for row in rows.values())
    assert report["inventory_complete"] is False and report["all_features_supported"] is False
    assert report["overall_mcu_completion_percent"] is None
    assert "errata: Revision review required" in report["gaps"]
    assert "not an MCU completion percentage" in markdown(report)


@pytest.mark.parametrize("mutation,code", [
    ("target", "TARGET_MISMATCH"), ("source_target", "TARGET_MISMATCH"),
    ("hash", "INVENTORY_INTEGRITY"), ("traversal", "INVALID_PATH"),
    ("symlink", "INVALID_PATH"), ("section", "UNKNOWN_SECTION"),
    ("peripheral", "UNKNOWN_PERIPHERAL"), ("workflow", "UNKNOWN_WORKFLOW")])
def test_bad_inventory_bindings_fail_before_coverage_claims(scope, mutation, code, tmp_path):
    path, spec, bundle = scope
    if mutation == "target":
        spec["target"]["package"] = "WRONG"
    elif mutation == "source_target":
        data = json.loads((tmp_path / "outline.json").read_text())
        data["source"]["target"] = "WRONG"
        from praxis.adapters.outline import canonical
        data["packet_sha256"] = digest(canonical({k: v for k, v in data.items() if k != "packet_sha256"}))
        raw = json.dumps(data).encode()
        (tmp_path / "outline.json").write_bytes(raw)
        spec["documents"][0]["sha256"] = digest(raw)
    elif mutation == "hash":
        (tmp_path / "outline.json").write_text("tampered")
    elif mutation == "traversal":
        spec["documents"][0]["path"] = "../outside.json"
    elif mutation == "symlink":
        outside = tmp_path.parent / (tmp_path.name + "-outside.json")
        outside.write_bytes((tmp_path / "outline.json").read_bytes())
        (tmp_path / "link.json").symlink_to(outside)
        spec["documents"][0]["path"] = "link.json"
    else:
        key = {"section": "section", "peripheral": "peripherals", "workflow": "workflows"}[mutation]
        spec["bindings"][0][key] = "99" if mutation == "section" else ["absent"]
    path.write_text(json.dumps(spec))
    with pytest.raises(PraxisError, match=code):
        from_spec(bundle, path)


@pytest.mark.parametrize("mutation", ["document", "binding", "unregistered", "missing", "excluded"])
def test_schema_rejects_ambiguous_or_conflicting_scope_data(scope, mutation):
    _, spec, _ = scope
    if mutation == "document":
        spec["documents"] *= 2
    elif mutation == "binding":
        spec["bindings"] *= 2
    elif mutation == "unregistered":
        spec["bindings"][0]["document"] = "unknown"
    elif mutation == "missing":
        spec["missing_sources"][0]["id"] = "vendor_manual"
    else:
        spec["bindings"][0]["applicability"] = "excluded"
    with pytest.raises(ValidationError):
        InventorySpec.model_validate(spec)


def test_require_complete_cli_fails_for_unfinished_inventory(scope, monkeypatch, capsys):
    from praxis.cli import main
    path, _, bundle = scope
    monkeypatch.setattr("praxis.bundle.Bundle", lambda _: bundle)
    assert main(["inventory", "--bundle", "unused", "--inventory", str(path), "--require-complete"]) == 1
    report = json.loads(capsys.readouterr().out)
    assert report["inventory_complete"] is False


def test_known_but_unpublished_entities_remain_visible_gaps(scope):
    path, _, bundle = scope
    bundle.manifest.peripherals.clear()
    report = from_spec(bundle, path)
    assert "memory: mapped declaration is not published in this bundle revision" in report["gaps"]
    assert report["sections"][0]["unpublished_peripherals"] == ["memory"]


def test_shipped_f407_source_scope_covers_all_four_pinned_documents_and_keeps_old_gaps():
    from conftest import ROOT
    from praxis.bundle import Bundle
    report = from_spec(Bundle(ROOT / "bundles/stm32f407g-disc1-e01-arm-core-v2"),
                       ROOT / "examples/inventory/stm32f407g-disc1/inventory.json")
    assert report["counts"] == {"source_documents": 4, "indexed_sections": 1683,
        "applicability_pending_or_mixed": 741, "unresolved_extraction_items": 29, "missing_sources": 3}
    sections = {(row["document"], row["section"]): row for row in report["sections"]}
    assert sections[("rm0090", "6")]["applicability"] == "excluded"
    assert sections[("rm0090", "7")]["related_peripherals"] == ["rcc"]
    assert sections[("rm0090", "23")]["applicability"] == "pending"
    assert sections[("rm0090", "5.4")]["destination_page"] is None
    assert sections[("es0182", "2.1.1")]["table_values"]["Rev. A"] == "A"
    assert "itm: mapped declaration is not published in this bundle revision" in report["gaps"]
