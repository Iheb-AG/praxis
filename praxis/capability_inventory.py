"""Source-pinned scope reconciliation, distinct from mode support and qualification.

Explicit document-section bindings are target data. No fuzzy peripheral routing,
manufacturer branches or inference of whole-section support from example reads.
"""
from pathlib import Path
from typing import Literal

from pydantic import Field, model_validator

from praxis.adapters.outline import validate_packet
from praxis.bundle import Bundle, digest, read_inside
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Digest, Identifier, Record
from praxis.inventory_review import EvidenceFile, EvidenceRef, InventoryFact, OutlineRepair, apply_repairs, load_evidence, references
from praxis.render import table
from praxis.reports import read_report
from praxis.support import CatalogTarget, assess


class OutlineDocument(Record):
    id: Identifier
    path: str = Field(min_length=1)
    sha256: Digest
    revision_label: str = Field(min_length=1)


class SectionBinding(Record):
    document: Identifier
    section: str = Field(pattern=r"^(?:[0-9]+|[A-Z])(?:\.[0-9]+)*$")
    applicability: Literal["pending", "mixed", "applicable", "excluded", "document_metadata"]
    rationale: str = Field(min_length=1)
    peripherals: list[Identifier] = []
    workflows: list[Identifier] = []
    evidence: list[EvidenceRef] = []

    @model_validator(mode="after")
    def unique_scope(self):
        if (len(set(self.peripherals)) != len(self.peripherals)
                or len(set(self.workflows)) != len(self.workflows)):
            raise ValueError("Use unique exact peripheral/workflow identities")
        if self.applicability in ("excluded", "document_metadata") and (self.peripherals or self.workflows):
            raise ValueError("Excluded/metadata sections cannot claim operating coverage")
        return self


class MissingInventorySource(Record):
    id: Identifier
    reason: str = Field(min_length=1)


class InventorySpec(Record):
    format: Literal["praxis-capability-inventory-v1"]
    target: CatalogTarget
    scope: str = Field(min_length=1)
    documents: list[OutlineDocument] = Field(min_length=1)
    bindings: list[SectionBinding]
    missing_sources: list[MissingInventorySource] = []
    exhaustiveness_review: Literal["pending"] = "pending"
    supporting_evidence: list[EvidenceFile] = []
    outline_repairs: list[OutlineRepair] = []
    facts: list[InventoryFact] = []

    @model_validator(mode="after")
    def unique_identities(self):
        ids = [row.id for row in self.documents]
        selections = [(row.document, row.section) for row in self.bindings]
        if len(set(ids)) != len(ids) or len(set(selections)) != len(selections):
            raise ValueError("Duplicate document or section-binding identities")
        if any(row.document not in ids for row in self.bindings):
            raise ValueError("Every binding must select a registered document")
        missing = [row.id for row in self.missing_sources]
        if len(set(missing)) != len(missing) or set(missing) & set(ids):
            raise ValueError("Missing sources must be distinct and cannot also be supplied")
        evidence_ids = [row.id for row in self.supporting_evidence]
        repairs = [(row.document, row.gap_locator) for row in self.outline_repairs]
        if (len(set(evidence_ids)) != len(evidence_ids) or len(set(repairs)) != len(repairs)
                or any(row.document not in ids for row in self.outline_repairs)
                or len({row.id for row in self.facts}) != len(self.facts)):
            raise ValueError("Use unique evidence, fact and repair identities, with registered documents")
        return self


def from_spec(bundle: Bundle, path: Path) -> dict:
    raw = path.read_bytes()
    spec = InventorySpec.model_validate(load_json(raw))
    target = bundle.manifest.target.model_dump()
    if any(target[key] != value for key, value in spec.target.model_dump().items()):
        raise PraxisError("TARGET_MISMATCH", "Inventory must match the exact MCU/package/board reference")
    support = assess(bundle)
    known_entities = read_report(bundle, "coverage")["peripherals"]
    results, documents, gaps = [], {}, []
    outlines = {}
    for doc in spec.documents:
        data = read_inside(path.resolve().parent, doc.path)
        if digest(data) != doc.sha256:
            raise PraxisError("INVENTORY_INTEGRITY", f"Pinned outline changed: {doc.id}")
        outline = validate_packet(load_json(data))
        if outline["source"]["target"] != target["mcu"]:
            raise PraxisError("TARGET_MISMATCH", f"Outline archive targets another MCU: {doc.id}")
        outlines[doc.id] = outline
    evidence = load_evidence(path.resolve().parent, spec.supporting_evidence,
                             {row["source"]["sha256"] for row in outlines.values()})
    for doc in spec.documents:
        outline = outlines[doc.id]
        reviewed_entries, remaining_gaps, repairs = apply_repairs(doc.id, outline, spec.outline_repairs, evidence)
        sections = {row["section"] for row in outline["entries"]}
        bindings = [row for row in spec.bindings if row.document == doc.id]
        for binding in bindings:
            references(binding.evidence, evidence)
            if not any(section == binding.section or section.startswith(binding.section + ".") for section in sections):
                raise PraxisError("UNKNOWN_SECTION", f"{doc.id}/{binding.section}: binding is not in pinned outline")
            if not set(binding.peripherals) <= known_entities.keys():
                raise PraxisError("UNKNOWN_PERIPHERAL", f"{doc.id}/{binding.section}: mapping selects unknown canonical entity")
            if not set(binding.workflows) <= support["workflows"].keys():
                raise PraxisError("UNKNOWN_WORKFLOW", f"{doc.id}/{binding.section}: mapping selects undeclared workflow")
        documents[doc.id] = {"revision_label": doc.revision_label, "outline_sha256": doc.sha256,
            "packet_sha256": outline["packet_sha256"], "source": outline["source"],
            "counts": outline["counts"], "contents_boundaries_observed": outline["contents_boundaries_observed"],
            "extraction_gaps": outline["unresolved"]}
        if spec.outline_repairs:
            documents[doc.id].update(remaining_extraction_gaps=remaining_gaps, editorial_repairs=repairs)
        if not outline["contents_boundaries_observed"]:
            gaps.append(f"{doc.id}: complete contiguous index boundaries not observed")
        if remaining_gaps:
            gaps.append(f"{doc.id}: {len(remaining_gaps)} unresolved index extraction lines/rows")
        for entry in reviewed_entries:
            matches = [row for row in bindings if entry["section"] == row.section
                       or entry["section"].startswith(row.section + ".")]
            selected = max(matches, key=lambda row: len(row.section.split(".")), default=None)
            applicability = selected.applicability if selected else "pending"
            related = selected.workflows if selected else []
            results.append({"document": doc.id, **entry, "applicability": applicability,
                "binding_section": selected.section if selected else None,
                "rationale": selected.rationale if selected else "No reviewed applicability binding authored",
                "related_peripherals": selected.peripherals if selected else [],
                "unpublished_peripherals": [name for name in (selected.peripherals if selected else [])
                                            if name not in bundle.manifest.peripherals],
                "related_workflows": {name: support["workflows"][name] for name in related},
                "all_section_modes_supported": False,
                "qualification": "not_established_by_scope_mapping"})
            if selected and selected.evidence:
                results[-1]["applicability_provenance"] = references(selected.evidence, evidence)
    pending = sum(row["applicability"] in ("pending", "mixed") for row in results)
    if pending:
        gaps.append(f"{pending} indexed sections still require applicability reconciliation")
    unpublished = sorted({name for row in results for name in row["unpublished_peripherals"]})
    gaps.extend(f"{name}: mapped declaration is not published in this bundle revision" for name in unpublished)
    gaps.extend(f"{row.id}: {row.reason}" for row in spec.missing_sources)
    gaps.extend(["Full section bodies, tables, instance/mode requirements and errata workarounds need review",
                 "Manufacturer-wide exhaustiveness review is pending; indexed headings are not the capability denominator",
                 "Build and physical qualification remain separate exact-artifact evidence"])
    report = {"format": "praxis-capability-inventory-report-v1", "target": target,
        "bundle_revision": bundle.manifest.bundle_revision, "inventory_sha256": digest(raw), "scope": spec.scope,
        "documents": documents, "sections": results, "gaps": gaps,
        "inventory_complete": False, "all_features_supported": False, "overall_mcu_completion_percent": None,
        "counts": {"source_documents": len(documents), "indexed_sections": len(results),
                   "applicability_pending_or_mixed": pending,
                   "unresolved_extraction_items": sum(d["counts"]["unresolved"] for d in documents.values()),
                   "missing_sources": len(spec.missing_sources)},
        "boundary": "Source scope map only. Related ready workflows do not establish all modes of a document section."}
    if spec.outline_repairs:
        report["counts"]["unresolved_extraction_items_after_review"] = sum(
            len(row["remaining_extraction_gaps"]) for row in documents.values())
        report["counts"]["editorial_repairs"] = sum(len(row["editorial_repairs"]) for row in documents.values())
    if spec.facts:
        report["scope_facts"] = [{**fact.model_dump(), "provenance": references(fact.evidence, evidence),
            "status": "editorial_inventory_fact_not_operating_or_physical_qualification"} for fact in spec.facts]
    return report


def markdown(report: dict) -> str:
    text = (f"# Manufacturer scope inventory\n\nTarget: {report['target']['id']}.\n\n"
            f"Bundle revision: {report['bundle_revision']}.\n\n{report['scope']}\n\n"
            "**Inventory remains incomplete; section counts are not an MCU completion percentage.**\n\n")
    text += table(["Document", "Revision", "Index entries", "Raw extraction items", "Remaining after editorial review", "Source SHA-256"], [
        [name, row["revision_label"], row["counts"]["entries"], row["counts"]["unresolved"],
         len(row.get("remaining_extraction_gaps", row["extraction_gaps"])), row["source"]["sha256"]]
        for name, row in report["documents"].items()])
    if report.get("scope_facts"):
        text += "\n## Editorial target scope facts\n\nThese facts do not approve operating modes or physical behavior.\n\n" + table(
            ["Fact", "Value", "Unit", "Scope", "Source locators"], [[row["id"], str(row["value"]), row["unit"],
                row["description"], "; ".join(ref["evidence"] + "/" + ref["locator"] for ref in row["provenance"])]
                for row in report["scope_facts"]])
    text += "\n## Section scope\n\n" + table(
        ["Document / section", "Title", "Applicability", "Related entities", "Related workflows", "Source locators"],
        [[f"{row['document']} / {row['section']}", row["title"], row["applicability"],
          ", ".join(row["related_peripherals"]), ", ".join(row["related_workflows"]), "; ".join(row["locators"])]
         for row in report["sections"]])
    return text + "\n## Remaining gaps\n\n" + "\n".join(f"- {line}" for line in report["gaps"]) + "\n"
