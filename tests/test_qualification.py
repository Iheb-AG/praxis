"""Offline modeled observations, never hardware tests or measured truth."""

import copy
import json

import pytest

from conftest import ROOT
from praxis.bundle import Bundle
from praxis.cli import main
from praxis.errors import PraxisError
from praxis.qualification import qualify_window, qualify_windows
from praxis.telemetry import ABI, FIELDS, MAGIC, SIZE, SYMBOL, assess, decode_sample

ARTIFACT, BUNDLE = "a" * 64, "b" * 64


def observation(state=1):
    samples = []
    for i in range(3):
        row = dict.fromkeys(FIELDS, 0)
        row.update(
            generation=2 + 2 * i,
            magic=MAGIC,
            abi=ABI,
            size_bytes=SIZE,
            uptime_ms=1000 + i * 250,
            timer_irqs=1000 + i * 250,
            state=state,
            run_number=1,
            frames_started=100 + (i if state == 1 else 0),
            frames_validated=100 + (i if state == 1 else 0),
            run_validated=100 + (i if state == 1 else 0),
            rx_bytes=1900 + (19 * i if state == 1 else 0),
            tx_bytes=1900 + (19 * i if state == 1 else 0),
            flags=0 if state == 3 else 1,
            failure_reason=4 if state == 3 else 0,
        )
        samples.append(decode_sample([row[k] for k in FIELDS]))
    return dict(
        artifact_id=ARTIFACT,
        bundle_revision=BUNDLE,
        samples=samples,
        abi=ABI,
        symbol=SYMBOL,
        record_bytes=SIZE,
        image_sha256="c" * 64,
        elf_sha256="d" * 64,
        readback_verified_before_and_after=True,
        execution_state="running",
        assessment={"everything_passed": True},
    )


@pytest.mark.parametrize("phase,state", [("running", 1), ("paused", 0), ("failure", 3)])
def test_phase_acceptance(phase, state):
    result = qualify_window(
        observation(state), artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase=phase
    )
    assert result["passed"] and not result["failures"]
    assert "everything_passed" not in result["assessment"]


@pytest.mark.parametrize(
    "key,value,failure",
    [
        ("artifact_id", "e" * 64, "artifact_matches"),
        ("bundle_revision", "e" * 64, "bundle_matches"),
        ("abi", True, "abi_matches"),
        ("symbol", "arbitrary", "abi_matches"),
        ("readback_verified_before_and_after", 1, "image_checks_reported"),
        ("image_sha256", "unverified", "image_identity_present"),
        ("execution_state", "halted", "cpu_running_reported"),
    ],
)
def test_metadata_never_promotes_a_pass(key, value, failure):
    r = observation()
    r[key] = value
    result = qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")
    assert not result["passed"] and failure in result["failures"]


def test_mixed_run_failed_intermediate_and_stale_windows():
    for change in ("run_number", "failure_reason", "generation", "timer_irqs"):
        r = observation()
        r["samples"][1][change] = 4 if change in ("run_number", "failure_reason") else 0
        result = qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")
        assert not result["passed"]
    r = observation()
    r["samples"] = [r["samples"][0]] * 3
    assert not qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")[
        "passed"
    ]


def test_recomputes_sample_labels_and_indicators():
    r = observation(3)
    for s in r["samples"]:
        s["state_name"] = "running"
        s["failure_name"] = "none"
        s["indicators"] = {"blue": True}
    assert not qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")[
        "passed"
    ]


def test_inconsistent_relations_and_pause_with_traffic():
    r = observation()
    r["samples"][-1]["frames_started"] = 1
    assert not qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")[
        "passed"
    ]
    r = observation(0)
    r["samples"][-1]["rx_bytes"] += 1
    assert not qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="paused")[
        "passed"
    ]


def test_intermediate_reset_cannot_hide_in_first_last_delta():
    r = observation()
    r["samples"][1]["uptime_ms"] = 0
    result = assess(r["samples"])
    assert not result["counter_continuity_plausible"]
    assert not result["fresh_progress"] and not result["blue_success_reported"]


def test_all_windows_required_and_image_run_match():
    first, second = observation(), observation()
    assert qualify_windows(
        [first, second], artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running"
    )["passed"]
    second["image_sha256"] = "e" * 64
    assert not qualify_windows(
        [first, second], artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running"
    )["passed"]
    second = copy.deepcopy(first)
    for s in second["samples"]:
        s["run_number"] = 2
    result = qualify_windows(
        [first, second], artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running"
    )
    assert not result["passed"] and not result["repeatability_qualified"]


@pytest.mark.parametrize("samples", [[], [{}], [{}] * 6, [dict.fromkeys(FIELDS, True)] * 2])
def test_malformed_records_rejected(samples):
    r = observation()
    r["samples"] = samples
    with pytest.raises(PraxisError):
        qualify_window(r, artifact_id=ARTIFACT, bundle_revision=BUNDLE, phase="running")


def test_cli_uses_verified_bundle_and_preserves_input_hash(tmp_path, capsys):
    bundle = ROOT / "bundles/stm32f407g-disc1-e01-uart-v1"
    r = observation(0)
    r["bundle_revision"] = Bundle(bundle).manifest.bundle_revision
    path = tmp_path / "private.json"
    path.write_text(json.dumps(r))
    assert (
        main(
            [
                "qualify-telemetry",
                "--bundle",
                str(bundle),
                "--artifact",
                ARTIFACT,
                "--phase",
                "paused",
                "--observation",
                str(path),
            ]
        )
        == 0
    )
    result = json.loads(capsys.readouterr().out)
    assert result["passed"] and len(result["input_sha256"]) == 1
    assert str(path) not in json.dumps(result)
