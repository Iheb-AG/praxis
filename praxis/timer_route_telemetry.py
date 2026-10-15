"""Fixed example software ABI and recomputed qualification, without hardware access.

The versioned data is an application recipe, not manufacturer register metadata.
Raw capture words take precedence over supplied labels or pass/fail assessments.
"""

from __future__ import annotations

import json
import re
from importlib.resources import files

from praxis.errors import PraxisError

SPEC = json.loads(files("praxis").joinpath("data/timer-route-telemetry-v1.json").read_text())
KIND, SYMBOL, MAGIC, ABI = (SPEC[k] for k in ("kind", "symbol", "magic", "abi"))
FIELDS = tuple(SPEC["fields"])
SIZE = len(FIELDS) * 4
EXPECTED = SPEC["expected"]
CAPTURES = tuple(f"capture{i}" for i in range(9))
END_FIELDS = (
    "end_pwm_cr1",
    "end_pwm_ccer",
    "end_pwm_dier",
    "end_capture_cr1",
    "end_capture_ccer",
    "end_capture_dier",
    "end_pin_modes",
)
PHASES = ("boot", "passed", "failed")
STATUSES = (
    "ok",
    "invalid",
    "context",
    "clock",
    "busy",
    "state",
    "timeout",
    "overcapture",
    "reset_required",
)
DIGEST = re.compile(r"^[0-9a-f]{64}$")
LIMITS = [
    "Qualifies firmware self-reports and captured counter differences, not independent electrical measurements.",
    "Both timers share HSI; relative ticks do not calibrate frequency, duty cycle or oscillator accuracy.",
    "No-edge timeout does not identify a removed jumper or exclude other physical faults.",
    "Publication progress is a software heartbeat, not repeated loopback execution.",
    "Recorded exact-image checks are reported evidence, not re-executed offline.",
    "No boot-unique identity; reset and rollover cannot always be distinguished.",
    "No timer IRQ/DMA, repeatability or full MCU acceptance is established.",
]


def decode_sample(words: list[int]) -> dict:
    if (
        not isinstance(words, list)
        or len(words) != len(FIELDS)
        or any(type(v) is not int or not 0 <= v <= 0xFFFFFFFF for v in words)
    ):
        raise PraxisError("TELEMETRY_PROTOCOL", "Expected the complete timer ABI as uint32 words")
    row = dict(zip(FIELDS, words, strict=True))
    if (
        row["generation"] & 1
        or row["magic"] != MAGIC
        or row["abi"] != ABI
        or row["size_bytes"] != SIZE
        or row["phase"] >= len(PHASES)
        or row["status"] >= len(STATUSES)
        or row["flags"] & ~15
        or row["end_valid_mask"] & ~7
        or row["captures"] > 9
        or row["frames"] > 8
    ):
        raise PraxisError("TELEMETRY_ABI", "Uninitialized, torn or incompatible timer record")
    return {**row, "phase_name": PHASES[row["phase"]], "status_name": STATUSES[row["status"]]}


def checks(row: dict) -> dict[str, bool]:
    count = row["captures"]
    values = [row[k] for k in CAPTURES[:count]]
    deltas = [(b - a) & 0xFFFFFFFF for a, b in zip(values, values[1:], strict=False)]
    lo, hi = (
        EXPECTED["period_ticks"] - EXPECTED["tolerance_ticks"],
        EXPECTED["period_ticks"] + EXPECTED["tolerance_ticks"],
    )
    valid = [lo <= value <= hi for value in deltas]
    frames = row["frames"]
    return {
        "fixed_recipe": all(row[k] == v for k, v in EXPECTED.items()),
        "unused_capture_words_zero": all(row[k] == 0 for k in CAPTURES[count:]),
        "validated_prefix_matches": (
            frames <= len(deltas)
            and all(valid[:frames])
            and (
                (count == 0 and frames == 0)
                or (count > 0 and len(deltas) == frames)
                or (len(deltas) == frames + 1 and not valid[-1] and row["status"] == 5)
            )
        ),
        "all_periods_recomputed": len(deltas) == 8 and all(valid),
        "complete_capture_count": row["frames"] == 8 and count == 9,
        "shutdown_snapshots_present": row["end_valid_mask"] == 7,
        "shutdown_snapshots_quiet": all(row[k] == 0 for k in END_FIELDS),
        "success_status": row["phase"] == 1 and row["status"] == 0 and row["flags"] == 11,
        "safe_failure_status": row["phase"] == 2 and row["status"] != 0 and row["flags"] == 15,
        "no_edge_timeout": row["status"] == 6 and count == 0 and frames == 0,
    }


def assess(samples: list[dict]) -> dict:
    if (
        not isinstance(samples, list)
        or not 1 <= len(samples) <= 100
        or any(not isinstance(s, dict) or not set(FIELDS) <= s.keys() for s in samples)
    ):
        raise PraxisError("INVALID_OBSERVATION", "Select complete timer ABI samples")
    rows = [decode_sample([s[k] for k in FIELDS]) for s in samples]
    pairs = list(zip(rows, rows[1:], strict=False))
    fresh = bool(pairs) and all(
        0 < ((b["publications"] - a["publications"]) & 0xFFFFFFFF) < 0x40000000
        and ((b["generation"] - a["generation"]) & 0xFFFFFFFF)
        == 2 * ((b["publications"] - a["publications"]) & 0xFFFFFFFF)
        for a, b in pairs
    )
    stable = all(
        all(s[k] == rows[0][k] for k in FIELDS if k not in ("generation", "publications"))
        for s in rows
    )
    common = {k: all(checks(s)[k] for s in rows) for k in checks(rows[0])}
    base = all(
        common[k]
        for k in (
            "fixed_recipe",
            "unused_capture_words_zero",
            "validated_prefix_matches",
            "shutdown_snapshots_present",
            "shutdown_snapshots_quiet",
        )
    )
    return dict(
        fresh_publication_progress=fresh,
        terminal_result_stable=stable,
        sample_checks=common,
        firmware_failure_reported=any(s["phase"] == 2 or s["status"] != 0 for s in rows),
        loopback_success_reported=fresh
        and stable
        and base
        and common["success_status"]
        and common["all_periods_recomputed"]
        and common["complete_capture_count"],
        safe_failure_reported=fresh and stable and base and common["safe_failure_status"],
        limits=LIMITS,
    )


def qualify_windows(
    observations: list[dict], *, artifact_id: str, bundle_revision: str, expected: str = "passed"
) -> dict:
    if (
        not isinstance(artifact_id, str)
        or not DIGEST.fullmatch(artifact_id)
        or not isinstance(bundle_revision, str)
        or not DIGEST.fullmatch(bundle_revision)
        or expected not in ("passed", "timeout", "failed")
        or not isinstance(observations, list)
        or not 1 <= len(observations) <= 20
    ):
        raise PraxisError("INVALID_QUALIFICATION", "Select exact hashes and 1–20 timer windows")
    windows, all_rows, identities = [], [], set()
    for observation in observations:
        if not isinstance(observation, dict):
            raise PraxisError("INVALID_OBSERVATION", "Expected a timer observation object")
        raw = observation.get("samples")
        if not isinstance(raw, list) or not 2 <= len(raw) <= 5:
            raise PraxisError("INVALID_OBSERVATION", "Select 2–5 complete samples per timer window")
        summary = assess(raw)
        rows = [decode_sample([s[k] for k in FIELDS]) for s in raw]
        identity_ok = all(
            isinstance(observation.get(k), str) and DIGEST.fullmatch(observation[k])
            for k in ("image_sha256", "elf_sha256")
        )
        required = [
            "fixed_recipe",
            "unused_capture_words_zero",
            "validated_prefix_matches",
            "shutdown_snapshots_present",
            "shutdown_snapshots_quiet",
        ]
        required += (
            ["success_status", "complete_capture_count", "all_periods_recomputed"]
            if expected == "passed"
            else ["safe_failure_status"]
        )
        if expected == "timeout":
            required.append("no_edge_timeout")
        test = {
            "artifact_matches": observation.get("artifact_id") == artifact_id,
            "bundle_matches": observation.get("bundle_revision") == bundle_revision,
            "abi_matches": observation.get("kind") == KIND
            and observation.get("symbol") == SYMBOL
            and type(observation.get("abi")) is int
            and observation["abi"] == ABI
            and type(observation.get("record_bytes")) is int
            and observation["record_bytes"] == SIZE,
            "image_identity_present": bool(identity_ok),
            "image_checks_reported": observation.get("readback_verified_before_and_after") is True,
            "cpu_running_reported": observation.get("execution_state") == "running",
            "fresh_publication_progress": summary["fresh_publication_progress"],
            "terminal_result_stable": summary["terminal_result_stable"],
            **{k: summary["sample_checks"][k] for k in required},
        }
        windows.append(
            dict(
                passed=all(test.values()),
                checks=test,
                failures=sorted(k for k, v in test.items() if not v),
                sample_count=len(rows),
                assessment=summary,
            )
        )
        all_rows.extend(rows)
        identities.add(
            (observation["image_sha256"], observation["elf_sha256"])
            if identity_ok
            else (None, None)
        )
    combined = assess(all_rows)
    return dict(
        format="praxis-timer-route-qualification-v1",
        expected=expected,
        artifact_id=artifact_id,
        bundle_revision=bundle_revision,
        passed=all(w["passed"] for w in windows)
        and len(identities) == 1
        and combined["fresh_publication_progress"]
        and combined["terminal_result_stable"],
        same_image=len(identities) == 1,
        windows=windows,
        ordered_publication_progress=combined["fresh_publication_progress"],
        terminal_result_stable=combined["terminal_result_stable"],
        repeatability_qualified=False,
        mutating_operations=0,
        limits=LIMITS,
    )
