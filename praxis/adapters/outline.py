"""Lossless accounting of dotted-leader document contents, never operating semantics.

The recognizer has no vendor, peripheral or target-name rules. Every selected
nonempty line is accounted for; unsupported headings remain explicit gaps.
"""
from __future__ import annotations

import json
import re

from praxis.bundle import digest
from praxis.errors import PraxisError

START = re.compile(r"^([0-9]+(?:\.[0-9]+)*|[A-Z](?:\.[0-9]+)*)\s+(.+)$")
LEADER = re.compile(r"^(.*?)\s+(?:\.\s*)+([0-9]+)\s*$")
ALIGNED_PAGE = re.compile(r"^(.*\S)\s{2,}([0-9]+)\s*$")
FOOTER = re.compile(r"(?:\bRev(?:ision)?\.?\s+[0-9]+\b|^[0-9]+/[0-9]+$)", re.I)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def prepare(parts: list[dict], *, source: dict, table_columns: dict[str, str] | None = None) -> dict:
    if not parts or len({part["locator"] for part in parts}) != len(parts):
        raise PraxisError("UNKNOWN_LOCATOR", "Choose unique complete PDF evidence pages")
    if any(not isinstance(p.get("page"), int) or not isinstance(p.get("text"), str) for p in parts):
        raise PraxisError("UNSUPPORTED_OUTLINE", "The outline adapter requires extracted PDF page text")
    if len({p["page"] for p in parts}) != len(parts):
        raise PraxisError("IMPORT_INTEGRITY", "Duplicate PDF page numbers")
    parts = sorted(parts, key=lambda part: part["page"])
    if table_columns is not None:
        return _tables(parts, source, table_columns)
    entries, unresolved, ledger, contents_pages = [], [], [], []
    pending, active, ended = None, False, False
    last_page = None

    def gap(reason):
        nonlocal pending
        if pending is not None:
            # Retain the section identity even if its page/title layout cannot
            # be completed. Dropping it would shrink the scope denominator.
            entries.append({"section": pending["section"], "title": " ".join(pending["fragments"]),
                "destination_page": None, "locators": pending["locators"],
                "applicability": "unreviewed", "operating_knowledge": "not_established",
                "extraction_flags": [reason]})
            unresolved.append({"reason": reason, **pending})
            for index in pending.pop("ledger_indices"):
                ledger[index]["disposition"] = "unresolved"
            unresolved[-1].pop("ledger_indices", None)
            pending = None

    def complete():
        nonlocal pending
        match = LEADER.fullmatch(" ".join(pending["fragments"]))
        if match is None and len(pending["raw_fragments"]) == 1:
            # A long contents title can leave no dots. Require an actual PDF
            # alignment gap; ordinary single-space trailing numbers are ambiguous.
            match = ALIGNED_PAGE.fullmatch(pending["raw_fragments"][0].strip())
        if match is None:
            return
        title, destination = " ".join(match[1].split()), int(match[2])
        if not title or destination <= 0:
            gap("invalid_title_or_destination")
            return
        indices = pending.pop("ledger_indices")
        for index in indices:
            ledger[index]["disposition"] = "entry"
        entries.append({"section": pending["section"], "title": title, "destination_page": destination,
                        "locators": pending["locators"], "applicability": "unreviewed",
                        "operating_knowledge": "not_established"})
        pending = None

    for part in parts:
        if last_page is not None and part["page"] != last_page + 1:
            gap("noncontiguous_evidence_pages")
            active = False
        last_page = part["page"]
        lines = [(n, " ".join(text.split()), text) for n, text in enumerate(part["text"].splitlines(), 1) if text.strip()]
        header = next((text for _, text, _ in lines[:8] if "Contents" in text.split()), None)
        if header is not None:
            if ended:
                raise PraxisError("AMBIGUOUS_OUTLINE", "A second contents block needs a separate explicit selection")
            active = True
            contents_pages.append(part["page"])
        else:
            if active:
                gap("contents_boundary_before_complete_heading")
                ended, active = True, False
        for number, text, raw_text in lines:
            locator = f"{part['locator']}/line:{number}"
            row = {"locator": locator, "sha256": digest(text.encode()), "disposition": "outside_contents"}
            ledger.append(row)
            index = len(ledger) - 1
            if not active:
                continue
            if "Contents" in text.split() or FOOTER.search(text):
                row["disposition"] = "page_metadata"
                continue
            if text.isdigit():
                if pending is not None and pending["fragments"][-1].endswith("."):
                    pending["fragments"].append(text)
                    pending["raw_fragments"].append(raw_text)
                    pending["locators"].append(locator)
                    pending["ledger_indices"].append(index)
                    complete()
                    continue
                row["disposition"] = "unresolved"
                unresolved.append({"reason": "unlabelled_numeric_line", "text": text, "locators": [locator]})
                continue
            heading_text = text.removeprefix("Appendix ")
            match = START.fullmatch(heading_text)
            if match:
                gap("heading_without_supported_page_leader")
                pending = {"section": match[1], "fragments": [match[2]],
                           "raw_fragments": [re.sub(r"^\s*(?:Appendix\s+)?" + re.escape(match[1]) + r"\s+", "", raw_text)],
                           "locators": [locator], "ledger_indices": [index]}
            elif pending is not None:
                pending["fragments"].append(text)
                pending["raw_fragments"].append(raw_text)
                pending["locators"].append(locator)
                pending["ledger_indices"].append(index)
            else:
                row["disposition"] = "unresolved"
                unresolved.append({"reason": "unrecognized_contents_line", "text": text, "locators": [locator]})
            if pending is not None:
                complete()
    gap("selection_ended_inside_heading")
    if not entries:
        raise PraxisError("UNSUPPORTED_OUTLINE", "No dotted-leader section entries found; review layout or select contents pages")
    seen = set()
    for entry in entries:
        if entry["section"] in seen:
            raise PraxisError("DUPLICATE_SECTION", f"Conflicting or repeated contents section {entry['section']}")
        seen.add(entry["section"])
    selected = {part["page"] for part in parts}
    contiguous = all(p in selected for p in range(min(contents_pages), max(contents_pages) + 1))
    start_observed = min(contents_pages) - 1 in selected
    gaps = ["Contents headings do not enumerate all operating modes or establish target applicability",
            "Body requirements, tables, errata and package constraints still require review"]
    if not (start_observed and ended and contiguous):
        gaps.append("Complete contents boundaries were not observed in contiguous selected evidence")
    if unresolved:
        gaps.append("Unresolved contents lines require editorial repair with source provenance")
    report = {"format": "praxis-source-outline-v1", "source": source, "index_layout": "dotted_contents",
        "status": "pending-review", "publication_ready": False,
        "entries": entries, "unresolved": unresolved, "line_accounting": ledger,
        "evidence_parts": [{"locator": p["locator"], "artifact_sha256": p["artifact_sha256"]} for p in parts],
        "contents_pages": contents_pages, "contents_boundaries_observed": start_observed and ended and contiguous,
        "counts": {"entries": len(entries), "unresolved": len(unresolved), "selected_pages": len(parts),
                   "incomplete_entries": sum(bool(row.get("extraction_flags")) for row in entries),
                   "accounted_nonempty_lines": len(ledger)}, "gaps": gaps}
    report["packet_sha256"] = digest(canonical(report))
    return report


def _tables(parts, source, columns):
    if (set(columns) != {"section", "title"} or any(not isinstance(v, str) or not v.strip() for v in columns.values())
            or len(set(columns.values())) != 2):
        raise PraxisError("INVALID_INPUT", "Map distinct literal section/title column headings")
    entries, unresolved, ledger, table_ledger, index_pages = [], [], [], [], []
    for part in parts:
        page_matched = False
        for n, text in enumerate(part["text"].splitlines(), 1):
            if text.strip():
                ledger.append({"locator": f"{part['locator']}/line:{n}",
                               "sha256": digest(" ".join(text.split()).encode()), "disposition": "table_extraction_view"})
        for table in part.get("tables", []):
            headings = None
            for n, raw in enumerate(table["rows"], 1):
                row = [" ".join((value or "").split()) for value in raw]
                location = f"{table['locator']}/row:{n}"
                accounting = {"locator": location, "sha256": digest(canonical(raw)), "disposition": "outside_index"}
                table_ledger.append(accounting)
                if all(value in row for value in columns.values()):
                    if len(row) != len(set(row)) or any(row.count(value) != 1 for value in columns.values()):
                        raise PraxisError("AMBIGUOUS_OUTLINE", "Index table column headings must be unique")
                    headings = row
                    accounting["disposition"] = "index_header"
                    page_matched = True
                    continue
                if headings is None:
                    continue
                if len(row) != len(headings):
                    accounting["disposition"] = "unresolved"
                    unresolved.append({"reason": "table_column_count", "row": raw, "locators": [location]})
                    continue
                section = row[headings.index(columns["section"])]
                title = row[headings.index(columns["title"])]
                if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)*|[A-Z](?:\.[0-9]+)*", section) or not title:
                    accounting["disposition"] = "unresolved"
                    unresolved.append({"reason": "unrecognized_index_row", "row": raw, "locators": [location]})
                    continue
                accounting["disposition"] = "entry"
                entries.append({"section": section, "title": title, "destination_page": None,
                    "locators": [location], "applicability": "unreviewed", "operating_knowledge": "not_established",
                    "table_values": dict(zip(headings, row, strict=True))})
        if page_matched:
            index_pages.append(part["page"])
    if not entries:
        raise PraxisError("UNSUPPORTED_OUTLINE", "No index tables match the configured literal column headings")
    if len({row["section"] for row in entries}) != len(entries):
        raise PraxisError("DUPLICATE_SECTION", "Repeated section identities in table index")
    selected = {p["page"] for p in parts}
    boundaries = all(p in selected for p in range(min(index_pages) - 1, max(index_pages) + 2))
    report = {"format": "praxis-source-outline-v1", "source": source, "index_layout": "table_index",
        "status": "pending-review", "publication_ready": False, "table_columns": columns,
        "entries": entries, "unresolved": unresolved, "line_accounting": ledger, "table_accounting": table_ledger,
        "evidence_parts": [{"locator": p["locator"], "artifact_sha256": p["artifact_sha256"]} for p in parts],
        "contents_pages": index_pages, "contents_boundaries_observed": boundaries,
        "counts": {"entries": len(entries), "unresolved": len(unresolved), "selected_pages": len(parts),
                   "accounted_nonempty_lines": len(ledger), "accounted_table_rows": len(table_ledger)},
        "gaps": ["Table indices are candidates, not reviewed limitations, applicability or operating semantics",
                 "Read full section bodies and status legends; raw table values are not interpreted"]}
    if not boundaries:
        report["gaps"].append("Complete contiguous table-index boundaries were not observed")
    if unresolved:
        report["gaps"].append("Unresolved table rows require editorial repair with provenance")
    report["packet_sha256"] = digest(canonical(report))
    return report


def validate_packet(report):
    if report.get("format") != "praxis-source-outline-v1":
        raise PraxisError("INVALID_INVENTORY", "Select a versioned source outline packet")
    body = {key: value for key, value in report.items() if key != "packet_sha256"}
    if report.get("packet_sha256") != digest(canonical(body)):
        raise PraxisError("INVENTORY_INTEGRITY", "Source outline packet bytes or identity changed")
    if (report.get("status") != "pending-review" or report.get("publication_ready") is not False
            or not report.get("entries") or report["counts"]["entries"] != len(report["entries"])
            or len({r["section"] for r in report["entries"]}) != len(report["entries"])):
        raise PraxisError("INVALID_INVENTORY", "Outline must retain unique unreviewed section candidates")
    return report
