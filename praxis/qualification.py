"""Deterministic acceptance of recorded telemetry, separate from physical truth.

Never attaches to hardware. Recomputes outcomes from ABI words instead of trusting
an earlier assessment or a report's pass flag. Input logs remain private.
"""

from __future__ import annotations

import re

from praxis.errors import PraxisError
from praxis.telemetry import ABI, FIELDS, SIZE, SYMBOL, assess, decode_sample

PHASES = ("failure", "running", "paused")
DIGEST = re.compile(r"^[0-9a-f]{64}$")


def qualify_window(
    observation: dict,
    *,
    artifact_id: str,
    bundle_revision: str,
    phase: str,
    minimum_frames: int = 100,
) -> dict:
    if (
        phase not in PHASES
        or not DIGEST.fullmatch(artifact_id)
        or not DIGEST.fullmatch(bundle_revision)
        or type(minimum_frames) is not int
        or not 1 <= minimum_frames <= 0xFFFFFFFF
    ):
        raise PraxisError(
            "INVALID_QUALIFICATION",
            "Choose a phase, exact artifact/bundle hashes and positive frame threshold",
        )
    if not isinstance(observation, dict):
        raise PraxisError("INVALID_OBSERVATION", "Expected a recorded telemetry object")
    raw = observation.get("samples")
    if not isinstance(raw, list) or not 2 <= len(raw) <= 5:
        raise PraxisError(
            "INVALID_OBSERVATION", "Qualification requires 2–5 coherent samples per window"
        )
    samples = []
    for row in raw:
        if not isinstance(row, dict) or not set(FIELDS) <= row.keys():
            raise PraxisError("INVALID_OBSERVATION", "Missing ABI words in a telemetry sample")
        samples.append(decode_sample([row[name] for name in FIELDS]))
    summary = assess(samples)
    checks = {
        "artifact_matches": observation.get("artifact_id") == artifact_id,
        "bundle_matches": observation.get("bundle_revision") == bundle_revision,
        "abi_matches": type(observation.get("abi")) is int
        and observation["abi"] == ABI
        and observation.get("record_bytes") == SIZE
        and observation.get("symbol") == SYMBOL,
        "image_checks_reported": observation.get("readback_verified_before_and_after") is True,
        "image_identity_present": all(
            isinstance(observation.get(k), str) and DIGEST.fullmatch(observation[k]) is not None
            for k in ("image_sha256", "elf_sha256")
        ),
        "cpu_running_reported": observation.get("execution_state") == "running",
        "fresh_counter_progress": summary["fresh_progress"],
        "same_run": summary["same_run"],
        "counter_relations": all(
            s["run_validated"] <= s["frames_validated"] <= s["frames_started"] for s in samples
        ),
    }
    delta = summary["deltas_modulo_uint32"]
    if phase == "failure":
        checks.update(
            failed_state=all(
                s["state_name"] == "failed" and s["failure_reason"] != 0 for s in samples
            ),
            frames_stopped=delta["frames_started"] == delta["frames_validated"] == 0,
            success_off=all(not s["indicators"]["blue"] for s in samples),
        )
    else:
        checks.update(
            expected_state=all(s["state_name"] == phase for s in samples),
            no_active_failure=all(s["failure_reason"] == 0 for s in samples),
            no_uart_queue_errors=all(
                s["uart_errors"] == s["queue_overflows"] == 0 for s in samples
            ),
        )
        if phase == "running":
            checks.update(
                validated_progress=delta["frames_validated"] > 0,
                byte_progress=delta["rx_bytes"] > 0 and delta["tx_bytes"] > 0,
                success_threshold=all(
                    s["run_validated"] >= minimum_frames and s["indicators"]["blue"]
                    for s in samples
                ),
            )
        else:
            checks["uart_stopped"] = all(
                delta[k] == 0
                for k in ("frames_started", "frames_validated", "rx_bytes", "tx_bytes", "uart_irqs")
            )
    return {
        "phase": phase,
        "passed": all(checks.values()),
        "checks": checks,
        "failures": sorted(k for k, v in checks.items() if not v),
        "artifact_id": artifact_id,
        "bundle_revision": bundle_revision,
        "image_sha256": observation.get("image_sha256"),
        "elf_sha256": observation.get("elf_sha256"),
        "run_number": samples[0]["run_number"],
        "sample_count": len(samples),
        "assessment": summary,
        "failure_names": sorted({s["failure_name"] for s in samples}),
        "limits": [
            "Validates recorded firmware self-reports, not independent hardware measurements.",
            "Reported image checks are not independently re-executed by this offline validator.",
            "One passing window does not establish repeatability or explain earlier failures.",
        ],
    }


def qualify_windows(
    observations: list[dict],
    *,
    artifact_id: str,
    bundle_revision: str,
    phase: str,
    minimum_frames: int = 100,
) -> dict:
    if not 1 <= len(observations) <= 20:
        raise PraxisError("INVALID_QUALIFICATION", "Select 1–20 recorded windows of one phase")
    windows = [
        qualify_window(
            row,
            artifact_id=artifact_id,
            bundle_revision=bundle_revision,
            phase=phase,
            minimum_frames=minimum_frames,
        )
        for row in observations
    ]
    identities = {(w["image_sha256"], w["elf_sha256"]) for w in windows}
    # A separate invocation is required for an intentional power cycle/new run.
    same_run = len({w["run_number"] for w in windows}) == 1
    return {
        "format": "praxis-telemetry-qualification-v1",
        "phase": phase,
        "passed": all(w["passed"] for w in windows) and len(identities) == 1 and same_run,
        "same_image": len(identities) == 1,
        "same_run_across_windows": same_run,
        "windows": windows,
        "repeatability_qualified": False,
        "mutating_operations": 0,
    }
