import copy
import json

import pytest
from pydantic import ValidationError

from praxis.adapters.outline import canonical, prepare
from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.inventory_review import EvidenceFile, EvidenceRef, InventoryFact, OutlineRepair, apply_repairs, load_evidence, references
from test_source_outline import SOURCE, part


@pytest.fixture
def reviewed(tmp_path):
    outline = prepare([part(1, "Title"), part(2, "Contents\n1 Memory . . . 10\n1.1 Long title\n39\n2 Other . . . 12"),
                       part(3, "List of tables")], source=SOURCE)
    layout = dict(format="praxis-page-layout-v1", source_id="manual", source_sha256=SOURCE["sha256"],
        locator="page:2", origin=SOURCE["origin"], width=595, height=842,
        words=[dict(locator="page:2/word:1", text="39", top=760),
               dict(locator="page:2/word:2", text="11", top=120)])
    layout["packet_sha256"] = digest(canonical(layout))
    path = tmp_path / "layout.json"
    path.write_text(json.dumps(layout))
    file = EvidenceFile(id="layout", path="layout.json", sha256=digest(path.read_bytes()))
    evidence = load_evidence(tmp_path, [file], {SOURCE["sha256"]})
    numeric = next(row for row in outline["unresolved"] if row["reason"] == "unlabelled_numeric_line")
    heading = next(row for row in outline["unresolved"] if row.get("section") == "1.1")
    repairs = [OutlineRepair(document="manual", gap_locator=numeric["locators"][0],
        action="classify_metadata", rationale="Synthetic footer reviewed", reviewer="Test editorial reviewer",
        evidence=[EvidenceRef(evidence="layout", locator="page:2/word:1")]),
        OutlineRepair(document="manual", gap_locator=heading["locators"][0], action="repair_entry", section="1.1",
        title="Long title", destination_page=11, rationale="Synthetic heading reviewed", reviewer="Test editorial reviewer",
        evidence=[EvidenceRef(evidence="layout", locator="page:2/word:2")])]
    return outline, evidence, repairs, file, path


def test_review_resolves_layout_without_deleting_scope_or_altering_source_packet(reviewed):
    outline, evidence, repairs, _, _ = reviewed
    original = copy.deepcopy(outline)
    entries, gaps, applied = apply_repairs("manual", outline, repairs, evidence)
    assert outline == original and not gaps and len(applied) == 2
    assert [row["section"] for row in entries] == [row["section"] for row in outline["entries"]]
    repaired = next(row for row in entries if row["section"] == "1.1")
    assert repaired["destination_page"] == 11 and repaired["raw_destination_page"] is None
    assert repaired["raw_title"] == "Long title" and repaired["operating_knowledge"] == "not_established"
    assert all(row["original_gap"] and row["provenance"] for row in applied)
    assert "not_independent" in applied[0]["status"]


@pytest.mark.parametrize("mutation,code", [
    ("unknown_gap", "UNKNOWN_REPAIR"), ("unknown_word", "UNKNOWN_LOCATOR"),
    ("wrong_pdf", "SOURCE_MISMATCH"), ("wrong_page", "SOURCE_MISMATCH"),
    ("wrong_numeric_word", "INVALID_REPAIR"), ("wrong_destination", "INVALID_REPAIR"),
    ("renamed_section", "INVALID_REPAIR"), ("wrong_kind", "INVALID_REPAIR")])
def test_invalid_repairs_never_hide_extraction_gaps(reviewed, mutation, code):
    outline, evidence, repairs, _, _ = reviewed
    if mutation == "unknown_gap":
        repairs[0] = repairs[0].model_copy(update={"gap_locator": "page:2/line:999"})
    elif mutation == "unknown_word":
        repairs[0] = repairs[0].model_copy(update={"evidence": [EvidenceRef(evidence="layout", locator="page:2/word:999")]})
    elif mutation == "wrong_pdf":
        evidence["layout"]["data"]["source_sha256"] = "b" * 64
    elif mutation == "wrong_page":
        repairs[0] = repairs[0].model_copy(update={"evidence": [EvidenceRef(evidence="layout", locator="page:3/word:1")]})
        evidence["layout"]["locators"].add("page:3/word:1")
    elif mutation == "wrong_numeric_word":
        repairs[0] = repairs[0].model_copy(update={"evidence": [EvidenceRef(evidence="layout", locator="page:2/word:2")]})
    elif mutation == "wrong_destination":
        repairs[1] = repairs[1].model_copy(update={"destination_page": 13})
    elif mutation == "renamed_section":
        repairs[1] = repairs[1].model_copy(update={"section": "99"})
    else:
        repairs[1] = OutlineRepair(document="manual", gap_locator=repairs[1].gap_locator,
            action="classify_metadata", rationale="Invalid", reviewer="Test", evidence=repairs[1].evidence)
    with pytest.raises(PraxisError, match=code):
        apply_repairs("manual", outline, repairs, evidence)


@pytest.mark.parametrize("mutation,code", [
    ("bytes", "INVENTORY_INTEGRITY"), ("pdf", "SOURCE_MISMATCH"),
    ("packet", "INVENTORY_INTEGRITY"), ("escape", "INVALID_PATH")])
def test_supporting_evidence_is_hash_pinned_and_source_bound(reviewed, tmp_path, mutation, code):
    _, _, _, file, path = reviewed
    if mutation == "escape":
        file = file.model_copy(update={"path": "../outside.json"})
    elif mutation == "bytes":
        path.write_bytes(b"changed")
    else:
        data = json.loads(path.read_text())
        data["source_sha256" if mutation == "pdf" else "width"] = "b" * 64 if mutation == "pdf" else 600
        path.write_text(json.dumps(data))
        file = file.model_copy(update={"sha256": digest(path.read_bytes())})
    with pytest.raises(PraxisError, match=code):
        load_evidence(tmp_path, [file], {SOURCE["sha256"]})


def test_scope_facts_require_literal_values_and_existing_provenance(reviewed):
    _, evidence, _, _, _ = reviewed
    ref = EvidenceRef(evidence="layout", locator="page:2/word:2")
    fact = InventoryFact(id="count", description="Synthetic count", value=2, unit="units", reviewer="Test", evidence=[ref])
    assert references(fact.evidence, evidence)[0]["source_sha256"] == SOURCE["sha256"]
    for value in [2.5, None, {}, []]:
        with pytest.raises(ValidationError):
            InventoryFact(id="count", description="Synthetic count", value=value, reviewer="Test", evidence=[ref])


def test_repinned_envelope_cannot_hide_changed_extracted_source_part(tmp_path):
    body = dict(locator="page:1", text="Original", tables=[])
    artifact = (json.dumps(body, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()
    data = dict(source_id="manual", source_sha256=SOURCE["sha256"], locator="page:1",
                origin=SOURCE["origin"], evidence=body, artifact_sha256=digest(artifact))
    path = tmp_path / "part.json"
    path.write_text(json.dumps(data))
    file = EvidenceFile(id="part", path="part.json", sha256=digest(path.read_bytes()))
    assert load_evidence(tmp_path, [file], {SOURCE["sha256"]})["part"]["locators"] == {"page:1"}
    data["evidence"]["text"] = "Changed"
    path.write_text(json.dumps(data))
    file = file.model_copy(update={"sha256": digest(path.read_bytes())})
    with pytest.raises(PraxisError, match="INVENTORY_INTEGRITY"):
        load_evidence(tmp_path, [file], {SOURCE["sha256"]})


def test_malformed_rehashed_layout_has_actionable_error(tmp_path):
    row = dict(format="praxis-page-layout-v1", source_sha256=SOURCE["sha256"], locator="page:1", words=[{}])
    row["packet_sha256"] = digest(canonical(row))
    path = tmp_path / "layout.json"
    path.write_text(json.dumps(row))
    file = EvidenceFile(id="layout", path="layout.json", sha256=digest(path.read_bytes()))
    with pytest.raises(PraxisError, match="INVALID_INVENTORY_EVIDENCE"):
        load_evidence(tmp_path, [file], {SOURCE["sha256"]})


def test_repaired_f407_inventory_preserves_legacy_sources_and_package_constraints():
    from conftest import ROOT
    from praxis.bundle import Bundle
    from praxis.capability_inventory import from_spec
    bundle = Bundle(ROOT / "bundles/stm32f407g-disc1-e01-arm-core-v2")
    root = ROOT / "examples/inventory/stm32f407g-disc1"
    old = from_spec(bundle, root / "inventory.json")
    reviewed = from_spec(bundle, root / "inventory-v2.json")
    assert old["counts"]["unresolved_extraction_items"] == reviewed["counts"]["unresolved_extraction_items"] == 29
    assert reviewed["counts"]["indexed_sections"] == old["counts"]["indexed_sections"] == 1683
    assert reviewed["counts"]["unresolved_extraction_items_after_review"] == 0
    assert reviewed["counts"]["editorial_repairs"] == 29
    assert reviewed["counts"]["applicability_pending_or_mixed"] < old["counts"]["applicability_pending_or_mixed"]
    sections = {(row["document"], row["section"]): row for row in reviewed["sections"]}
    for section in ["16", "23", "25", "29", "37"]:
        assert sections[("rm0090", section)]["applicability"] == "excluded"
        assert sections[("rm0090", section)]["applicability_provenance"]
    assert sections[("rm0090", "11")]["applicability"] == "pending"
    assert sections[("rm0090", "5.4")]["destination_page"] == 141
    assert sections[("ds8626", "3.20")]["title"] == "VBAT operation"
    assert sections[("rm0090", "36")]["applicability"] == "mixed"
    facts = {row["id"]: row for row in reviewed["scope_facts"]}
    assert facts["package_pin_count"]["value"] == 100 and facts["gpio_count"]["value"] == 82
    assert "no FSMC interrupt" in facts["fsmc_lqfp100_constraint"]["value"]
    assert "contiguous" in facts["system_sram_total"]["description"]
    assert reviewed["inventory_complete"] is False and reviewed["all_features_supported"] is False
