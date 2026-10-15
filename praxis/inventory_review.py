"""Source-bound editorial repairs and scope facts, separate from operating approval.

Repairs cannot delete section identities or turn source scope into mode support.
All target-specific decisions and replacement values are supplied as pinned data.
"""
from pathlib import Path
from typing import Literal
import json

from pydantic import Field, StrictBool, StrictInt, StrictStr, model_validator

from praxis.adapters.outline import canonical
from praxis.bundle import digest, read_inside
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Digest, Identifier, Record


class EvidenceFile(Record):
    id: Identifier
    path: str = Field(min_length=1)
    sha256: Digest


class EvidenceRef(Record):
    evidence: Identifier
    locator: str = Field(min_length=1)


class OutlineRepair(Record):
    document: Identifier
    gap_locator: str = Field(min_length=1)
    action: Literal["classify_metadata", "repair_entry"]
    rationale: str = Field(min_length=1)
    reviewer: str = Field(min_length=1)
    evidence: list[EvidenceRef] = Field(min_length=1)
    section: str | None = None
    title: str | None = None
    destination_page: int | None = Field(default=None, gt=0)

    @model_validator(mode="after")
    def action_shape(self):
        if self.action == "repair_entry" and (not self.section or not self.title or self.destination_page is None):
            raise ValueError("Entry repair requires the same section identity, complete title and positive page")
        if self.action == "classify_metadata" and any(x is not None for x in (self.section, self.title, self.destination_page)):
            raise ValueError("Metadata classification cannot edit a section")
        return self


class InventoryFact(Record):
    id: Identifier
    description: str = Field(min_length=1)
    value: StrictBool | StrictInt | StrictStr
    unit: str = ""
    reviewer: str = Field(min_length=1)
    evidence: list[EvidenceRef] = Field(min_length=1)


def load_evidence(root: Path, files: list[EvidenceFile], source_hashes: set[str]) -> dict:
    found = {}
    for spec in files:
        data = read_inside(root, spec.path)
        if digest(data) != spec.sha256:
            raise PraxisError("INVENTORY_INTEGRITY", f"Supporting evidence changed: {spec.id}")
        row = load_json(data)
        if not isinstance(row, dict) or row.get("source_sha256") not in source_hashes:
            raise PraxisError("SOURCE_MISMATCH", f"{spec.id}: evidence PDF is not one of the pinned inventory sources")
        try:
            if row.get("format") == "praxis-page-layout-v1":
                if row.get("packet_sha256") != digest(canonical({k: v for k, v in row.items() if k != "packet_sha256"})):
                    raise PraxisError("INVENTORY_INTEGRITY", f"{spec.id}: layout packet hash differs")
                locators = {row["locator"], *(word["locator"] for word in row["words"])}
            elif isinstance(row.get("evidence"), dict) and row["evidence"].get("locator") == row.get("locator"):
                # The archived v1 extracted part has this fixed serialization.
                # Repinning an edited envelope must not preserve stale artifact provenance.
                artifact = (json.dumps(row["evidence"], indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()
                if digest(artifact) != row.get("artifact_sha256"):
                    raise PraxisError("INVENTORY_INTEGRITY", f"{spec.id}: extracted source-part hash differs")
                locators = {row["locator"]}
                for table in row["evidence"].get("tables", []):
                    locators.add(table["locator"])
                    locators.update(f"{table['locator']}/row:{n}" for n in range(1, len(table["rows"]) + 1))
            else:
                raise PraxisError("INVALID_INVENTORY_EVIDENCE", f"{spec.id}: select an MCP source-part or layout response")
            if not isinstance(row["origin"], str) or not isinstance(row["locator"], str):
                raise TypeError("Evidence origin and locator must be strings")
        except (KeyError, TypeError) as exc:
            raise PraxisError("INVALID_INVENTORY_EVIDENCE", f"{spec.id}: incomplete evidence identity or locators") from exc
        found[spec.id] = dict(data=row, locators=locators, sha256=spec.sha256)
    return found


def references(refs: list[EvidenceRef], evidence: dict) -> list[dict]:
    result = []
    for ref in refs:
        if ref.evidence not in evidence or ref.locator not in evidence[ref.evidence]["locators"]:
            raise PraxisError("UNKNOWN_LOCATOR", f"Evidence reference not registered: {ref.evidence}/{ref.locator}")
        row = evidence[ref.evidence]
        result.append({**ref.model_dump(), "evidence_sha256": row["sha256"],
                       "source_sha256": row["data"]["source_sha256"], "origin": row["data"]["origin"]})
    return result


def apply_repairs(document: str, outline: dict, repairs: list[OutlineRepair], evidence: dict):
    entries = {row["section"]: dict(row) for row in outline["entries"]}
    unresolved = {row["locators"][0]: row for row in outline["unresolved"]}
    applied = []
    for repair in repairs:
        if repair.document != document:
            continue
        if repair.gap_locator not in unresolved:
            raise PraxisError("UNKNOWN_REPAIR", f"{document}: no unresolved item at {repair.gap_locator}")
        proof = references(repair.evidence, evidence)
        page = repair.gap_locator.split("/")[0]
        if (any(row["source_sha256"] != outline["source"]["sha256"] for row in proof)
                or not any(row["locator"].split("/")[0] == page for row in proof)):
            raise PraxisError("SOURCE_MISMATCH", "Outline repair must cite the same pinned PDF and affected page")
        raw_gap = unresolved[repair.gap_locator]
        if repair.action == "classify_metadata":
            if raw_gap["reason"] != "unlabelled_numeric_line":
                raise PraxisError("INVALID_REPAIR", "Only isolated numeric extraction artifacts can be classified as metadata")
            if not any(word["locator"] == ref.locator and word["text"] == raw_gap["text"]
                       for ref in repair.evidence
                       for word in evidence[ref.evidence]["data"].get("words", [])):
                raise PraxisError("INVALID_REPAIR", "Metadata classification needs the matching source word as evidence")
        else:
            if repair.section not in entries or raw_gap.get("section", repair.section) != repair.section:
                raise PraxisError("INVALID_REPAIR", "Repair must preserve an existing source section identity")
            if raw_gap["reason"] not in ("heading_without_supported_page_leader", "unrecognized_contents_line"):
                raise PraxisError("INVALID_REPAIR", "Repair is not a supported incomplete heading or detached fragment")
            old = entries[repair.section]
            if page not in {locator.split("/")[0] for locator in old["locators"]}:
                raise PraxisError("SOURCE_MISMATCH", "Detached fragment and heading must share the affected page")
            if not any(word["locator"] == ref.locator and word["text"] == str(repair.destination_page)
                       for ref in repair.evidence
                       for word in evidence[ref.evidence]["data"].get("words", [])):
                raise PraxisError("INVALID_REPAIR", "Heading repair needs the matching destination-page word as evidence")
            entries[repair.section] = {**old, "raw_title": old["title"], "raw_destination_page": old["destination_page"],
                "title": repair.title, "destination_page": repair.destination_page,
                "extraction_flags": [], "editorial_repair": repair.model_dump()}
        applied.append({**repair.model_dump(), "original_gap": raw_gap, "provenance": proof,
                        "status": "implementing_author_editorial_review_not_independent_signoff"})
        del unresolved[repair.gap_locator]
    return list(entries.values()), list(unresolved.values()), applied
