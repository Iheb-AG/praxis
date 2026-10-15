"""Fixed interrupt-example ABI layered on the existing raw-period qualifier.

Own identity/receipt checks are mandatory before adapting common capture words.
Hardware facts remain in reviewed source contracts, not this software protocol.
"""

from __future__ import annotations

import copy
import json
from importlib.resources import files

from praxis import timer_route_telemetry as base
from praxis.errors import PraxisError

SPEC = json.loads(files("praxis").joinpath("data/timer-irq-telemetry-v1.json").read_text())
KIND, SYMBOL, MAGIC, ABI = (SPEC[k] for k in ("kind", "symbol", "magic", "abi"))
FIELDS = tuple(SPEC["fields"])
SIZE = len(FIELDS) * 4
EXTRA = FIELDS[len(base.FIELDS) :]
LIMITS = [
    "IRQ receipt counts, vector checks and shutdown snapshots are firmware self-reports.",
    "Exact-image checks bind the selected artifact; they do not authenticate truthful execution.",
    "Both timers share HSI; no independent frequency/duty calibration or arbitrary IRQ-order proof.",
    "Timeout qualification excludes a reported pending capture with no ISR delivery.",
    "No DMA, formal repeatability, full MCU acceptance or independent release review is established.",
    *[s for s in base.LIMITS if not s.startswith("No timer IRQ/DMA")],
]


def common(row: dict) -> dict:
    """Adapt already validated own ABI fields; preserve all raw captures/counters."""
    return {
        **{k: row[k] for k in base.FIELDS},
        "magic": base.MAGIC,
        "abi": base.ABI,
        "size_bytes": base.SIZE,
    }


def decode_sample(words: list[int]) -> dict:
    if (
        not isinstance(words, list)
        or len(words) != len(FIELDS)
        or any(type(v) is not int or not 0 <= v <= 0xFFFFFFFF for v in words)
    ):
        raise PraxisError("TELEMETRY_PROTOCOL", "Expected complete timer IRQ uint32 words")
    row = dict(zip(FIELDS, words, strict=True))
    if (
        row["magic"] != MAGIC
        or row["abi"] != ABI
        or row["size_bytes"] != SIZE
        or row["irq_error"] > 11
        or row["discarded_edges"] > 1
        or row["data_reads"] > 10
        or row["irq_count"] > 32
        or row["irq_priority"] > 255
        or any(
            row[k] > 1
            for k in [
                "vector_verified",
                "end_irq_enabled",
                "end_irq_pending",
                "end_irq_active",
                "timeout_pending_capture",
                "irq_snapshot_valid",
            ]
        )
    ):
        raise PraxisError("TELEMETRY_ABI", "Uninitialized or incompatible timer IRQ record")
    checked = base.decode_sample([common(row)[k] for k in base.FIELDS])
    return {**row, "phase_name": checked["phase_name"], "status_name": checked["status_name"]}


def rows(samples):
    if (
        not isinstance(samples, list)
        or not 1 <= len(samples) <= 100
        or any(not isinstance(s, dict) or not set(FIELDS) <= s.keys() for s in samples)
    ):
        raise PraxisError("INVALID_OBSERVATION", "Select complete timer IRQ samples")
    return [decode_sample([s[k] for k in FIELDS]) for s in samples]


def receipt_checks(row):
    return dict(
        irq_success=all(row[k] == v for k, v in SPEC["irq_expected"].items()),
        irq_shutdown_known=row["irq_snapshot_valid"] == 1
        and row["vector_verified"] == 1
        and row["irq_priority"] == SPEC["irq_expected"]["irq_priority"]
        and all(row[k] == 0 for k in ["end_irq_enabled", "end_irq_pending", "end_irq_active"]),
        irq_receipts_plausible=row["irq_count"] >= row["data_reads"]
        and 0 <= row["data_reads"] - row["discarded_edges"] - row["captures"] <= 1,
        no_pending_capture_timeout=row["timeout_pending_capture"] == 0
        and row["irq_count"] == 0
        and row["data_reads"] == 0
        and row["discarded_edges"] == 0
        and row["irq_error"] == 7,
    )


def assess(samples):
    raw = rows(samples)
    report = base.assess([common(s) for s in raw])
    stable = all(all(s[k] == raw[0][k] for k in EXTRA) for s in raw)
    checks = {k: all(receipt_checks(s)[k] for s in raw) for k in receipt_checks(raw[0])}
    report.update(irq_terminal_stable=stable, irq_checks=checks, limits=LIMITS)
    report["terminal_result_stable"] &= stable
    report["loopback_success_reported"] &= (
        stable and checks["irq_success"] and checks["irq_receipts_plausible"]
    )
    report["safe_failure_reported"] &= (
        stable and checks["irq_shutdown_known"] and checks["irq_receipts_plausible"]
    )
    return report


def qualify_windows(observations, *, artifact_id, bundle_revision, expected="passed"):
    if (
        not isinstance(observations, list)
        or not 1 <= len(observations) <= 20
        or expected not in ("passed", "timeout", "failed")
    ):
        raise PraxisError(
            "INVALID_QUALIFICATION", "Select1–20 timer IRQ windows and a supported outcome"
        )
    adapted = []
    own = []
    all_rows = []
    for observation in observations:
        if not isinstance(observation, dict):
            raise PraxisError("INVALID_OBSERVATION", "Expected a timer IRQ observation")
        raw = rows(observation.get("samples"))
        summary = assess(raw)
        required = ["irq_terminal_stable", "irq_shutdown_known", "irq_receipts_plausible"]
        checks = {"irq_terminal_stable": summary["irq_terminal_stable"], **summary["irq_checks"]}
        if expected == "passed":
            required.append("irq_success")
        elif expected == "timeout":
            required.append("no_pending_capture_timeout")
        metadata = (
            observation.get("kind") == KIND
            and observation.get("symbol") == SYMBOL
            and type(observation.get("abi")) is int
            and observation["abi"] == ABI
            and type(observation.get("record_bytes")) is int
            and observation["record_bytes"] == SIZE
        )
        own.append(
            dict(
                metadata_matches=metadata,
                checks={k: checks[k] for k in required},
                passed=metadata and all(checks[k] for k in required),
            )
        )
        # Identity above is checked independently; common qualification never infers an ABI.
        candidate = copy.deepcopy(observation)
        candidate.update(
            kind=base.KIND,
            symbol=base.SYMBOL,
            abi=base.ABI,
            record_bytes=base.SIZE,
            samples=[common(s) for s in raw],
        )
        adapted.append(candidate)
        all_rows.extend(raw)
    report = base.qualify_windows(
        adapted, artifact_id=artifact_id, bundle_revision=bundle_revision, expected=expected
    )
    combined = assess(all_rows)
    report.update(
        format="praxis-timer-irq-qualification-v1",
        irq_windows=own,
        irq_terminal_stable=combined["irq_terminal_stable"],
        limits=LIMITS,
    )
    report["passed"] &= all(w["passed"] for w in own) and combined["irq_terminal_stable"]
    return report
