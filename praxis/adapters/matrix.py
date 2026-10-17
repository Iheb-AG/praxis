"""Configured request-matrix extraction; candidates require semantic review.

Axes, complete table selections, placeholders and wrap rules come from versioned
configuration. No MCU names, channel maps or request names live in this adapter.
"""

from __future__ import annotations

import copy
import json
import re
from typing import Literal

from pydantic import Field, StrictInt, model_validator

from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.models import Digest, Identifier, Record

MAX_PACKET = 1024 * 1024
TABLE = re.compile(r"page:[1-9][0-9]*/table:[1-9][0-9]*")
SIGNAL = re.compile(r"[A-Za-z_][A-Za-z0-9_]{0,127}")


class MatrixSpec(Record):
    format: Literal["praxis-routing-matrix-v1"]
    id: Identifier
    target: str = Field(min_length=1, max_length=128)
    group: str = Field(min_length=1, max_length=128)
    evidence_source: Identifier
    source_sha256: Digest
    table_locators: list[str] = Field(min_length=1, max_length=32)
    context_locator: str = Field(pattern=r"^page:[1-9][0-9]*$")
    context_contains: list[str] = Field(min_length=1, max_length=8)
    row_axis: str = Field(min_length=1, max_length=48)
    column_axis: str = Field(min_length=1, max_length=48)
    row_ids: list[StrictInt] = Field(min_length=1, max_length=256)
    column_ids: list[StrictInt] = Field(min_length=1, max_length=256)
    empty_cells: list[str] = Field(default_factory=lambda: ["-"], max_length=16)
    join_suffixes: list[str] = Field(default_factory=list, max_length=8)

    @model_validator(mode="after")
    def unambiguous_rules(self):
        if len(set(self.table_locators)) != len(self.table_locators) or any(
            not TABLE.fullmatch(v) for v in self.table_locators
        ):
            raise ValueError("Select unique complete page/table locators")
        for axis in (self.row_ids, self.column_ids):
            if len(set(axis)) != len(axis) or any(
                type(v) is not int or not 0 <= v < 4096 for v in axis
            ):
                raise ValueError("Axis IDs must be unique bounded nonnegative integers")
        for values, limit in (
            (self.context_contains, 256),
            (self.empty_cells, 32),
            (self.join_suffixes, 8),
        ):
            if len(set(values)) != len(values) or any(
                not isinstance(v, str) or len(v) > limit for v in values
            ):
                raise ValueError("Use unique bounded literal rules")
        if any(not v.strip() for v in self.context_contains + self.join_suffixes):
            raise ValueError("Context and wrap rules cannot be blank")
        return self


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def axis_id(value, label):
    if not isinstance(value, str):
        return None
    found = re.fullmatch(re.escape(label) + r"\s+([0-9]{1,4})", " ".join(value.split()))
    return int(found[1]) if found else None


def signals(value, spec):
    if not isinstance(value, str):
        return None
    if value.strip() in spec.empty_cells:
        return []
    lines = []
    for line in value.splitlines():
        line = line.strip()
        if lines and any(lines[-1].endswith(suffix) for suffix in spec.join_suffixes):
            lines[-1] += line
        else:
            lines.append(line)
    tokens = " ".join(lines).split()
    if (
        not tokens
        or len(set(tokens)) != len(tokens)
        or any(not SIGNAL.fullmatch(v) or v.endswith("_") for v in tokens)
    ):
        return None
    return tokens


def prepare(parts, spec: MatrixSpec, source: dict, policy_sha256: str):
    if (
        source.get("id") != spec.evidence_source
        or source.get("sha256") != spec.source_sha256
        or source.get("target") != spec.target
    ):
        raise PraxisError(
            "SOURCE_HASH_MISMATCH", "Matrix rules must bind this exact source and target"
        )
    pages = {p["locator"]: p for p in parts}
    if len(pages) != len(parts):
        raise PraxisError("DUPLICATE_SOURCE", "Evidence page identities must be unique")
    context = pages.get(spec.context_locator)
    if context is None:
        raise PraxisError("UNKNOWN_LOCATOR", "Read the complete configured matrix context page")
    text = " ".join(context.get("text", "").split())
    if any(" ".join(v.split()) not in text for v in spec.context_contains):
        raise PraxisError(
            "MATRIX_CONTEXT",
            "Configured matrix title/context is absent; do not choose another table",
        )
    cells, gaps, originals, duplicates = {}, [], [], set()
    for locator in sorted(spec.table_locators):
        page = pages.get(locator.split("/table:")[0])
        matches = [t for t in page.get("tables", []) if t.get("locator") == locator] if page else []
        if len(matches) != 1:
            raise PraxisError("UNKNOWN_LOCATOR", f"Select one complete extracted table: {locator}")
        table = matches[0]
        originals.append(
            dict(
                locator=locator, artifact_sha256=page["artifact_sha256"], table=copy.deepcopy(table)
            )
        )
        rows = table.get("rows")
        if not isinstance(rows, list) or not rows or any(not isinstance(r, list) for r in rows):
            gaps.append(dict(locator=locator, reason="malformed_table"))
            continue
        columns = [axis_id(v, spec.column_axis) for v in rows[0][1:]]
        if (
            len(set(columns)) != len(columns)
            or None in columns
            or set(columns) != set(spec.column_ids)
        ):
            gaps.append(dict(locator=locator, reason="ambiguous_or_incomplete_columns"))
            continue
        for number, row in enumerate(rows[1:], 2):
            pointer = f"{locator}/row:{number}"
            row_id = axis_id(row[0], spec.row_axis) if row else None
            if row_id not in spec.row_ids or len(row) != len(columns) + 1:
                gaps.append(dict(locator=pointer, reason="ambiguous_row_or_column_count"))
                continue
            for index, column in enumerate(columns, 1):
                key = (row_id, column)
                at = f"{pointer}/column:{index + 1}"
                if key in cells or key in duplicates:
                    cells.pop(key, None)
                    duplicates.add(key)
                    gaps.append(
                        dict(
                            locator=at,
                            reason="duplicate_matrix_cell",
                            row_id=row_id,
                            column_id=column,
                        )
                    )
                    continue
                names = signals(row[index], spec)
                cells[key] = dict(
                    row_id=row_id,
                    column_id=column,
                    raw=row[index],
                    signals=names or [],
                    status="unresolved" if names is None else "signals" if names else "empty",
                    provenance=dict(**source, artifact_sha256=page["artifact_sha256"], locator=at),
                )
                if names is None:
                    gaps.append(
                        dict(
                            locator=at,
                            reason="unsupported_or_qualified_cell",
                            row_id=row_id,
                            column_id=column,
                            raw=row[index],
                        )
                    )
    for row in sorted(spec.row_ids):
        for column in sorted(spec.column_ids):
            if (row, column) not in cells:
                gaps.append(dict(reason="missing_or_duplicate_cell", row_id=row, column_id=column))
    ordered = [cells[k] for k in sorted(cells)]
    candidates = [
        dict(
            group=spec.group,
            row_id=c["row_id"],
            column_id=c["column_id"],
            signal=s,
            provenance=c["provenance"],
            status="unreviewed",
        )
        for c in ordered
        for s in sorted(c["signals"])
    ]
    report = dict(
        format="praxis-routing-matrix-review-v1",
        spec_id=spec.id,
        policy_sha256=policy_sha256,
        source=source,
        row_axis=spec.row_axis,
        column_axis=spec.column_axis,
        cells=ordered,
        candidates=candidates,
        gaps=gaps,
        original_tables=originals,
        context_pages=[
            dict(locator=p["locator"], artifact_sha256=p["artifact_sha256"], text=p.get("text", ""))
            for p in sorted(parts, key=lambda p: p["locator"])
        ],
        counts=dict(
            expected_cells=len(spec.row_ids) * len(spec.column_ids),
            cells=len(cells),
            candidates=len(candidates),
            unresolved_cells=sum(c["status"] == "unresolved" for c in ordered),
        ),
        complete=not gaps,
        review_required=True,
        publication_ready=False,
        limits=[
            "Literal routing candidates only; qualified/footnoted cells are unresolved.",
            "No automatic target applicability, operating semantics, board wiring or hardware qualification.",
            "Shared requests in one cell require separate configuration and ownership review.",
        ],
    )
    encoded = canonical(report)
    if len(encoded) > MAX_PACKET:
        raise PraxisError(
            "REVIEW_LIMIT", "Complete matrix exceeds 1 MiB; select a smaller complete matrix"
        )
    report["packet_sha256"] = digest(encoded)
    return report
