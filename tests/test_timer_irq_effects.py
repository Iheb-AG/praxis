"""Independent exception delivery, software publisher and source-bound IRQ scope."""

import json
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis import timer_irq_telemetry as timer
from praxis.bundle import Bundle, digest
from praxis.compiler import compile_bundle
from praxis.definitions import load_definitions
from praxis.models import Profile
from praxis.reports import read_report
from test_timer_irq import APP, ASSETS, observation, qualify

SOURCE = ROOT / "sources/stm32f407g-disc1"
WORKFLOW = "tim2_tim5_capture_irq"


@pytest.fixture(scope="module")
def model(tmp_path_factory):
    require_tool("gcc")
    output = tmp_path_factory.mktemp("timer-irq") / "model"
    subprocess.run(
        [
            "gcc",
            "-std=c11",
            "-Wall",
            "-Wextra",
            "-Werror",
            "-isystem",
            str(ASSETS / "include"),
            "-I",
            str(APP),
            str(ROOT / "tests/fixtures/f407_timer_irq_model.c"),
            "-o",
            str(output),
        ],
        check=True,
        capture_output=True,
        timeout=30,
    )
    return output


def run(model, fault=0, wrap=False, immediate=False, publication_wrap=False):
    value = json.loads(
        subprocess.check_output(
            [
                str(model),
                str(fault),
                str(int(wrap)),
                str(int(immediate)),
                str(int(publication_wrap)),
            ],
            timeout=5,
        )
    )
    assert value["violations"] == 0 and value["reads"] < 400 and value["writes"] < 65
    assert value["irq_reads"] < 1000100 and value["irq_writes"] < 30 and value["fences"] == 4
    row = timer.decode_sample(value["words"])
    record = observation()
    record["samples"] = [
        dict(
            row,
            generation=(row["generation"] + 2 * i) & 0xFFFFFFFF,
            publications=(row["publications"] + i) & 0xFFFFFFFF,
        )
        for i in range(3)
    ]
    return value, row, record


@pytest.mark.parametrize("wrap", [False, True])
@pytest.mark.parametrize("immediate", [False, True])
@pytest.mark.parametrize("publication_wrap", [False, True])
def test_irq_can_arrive_before_unmask_returns_and_counter_publisher_wraps(
    model, wrap, immediate, publication_wrap
):
    effects, row, record = run(
        model, wrap=wrap, immediate=immediate, publication_wrap=publication_wrap
    )
    assert effects["deliveries"] == row["irq_count"] == row["data_reads"] == 10
    assert row["discarded_edges"] == 1 and row["frames"] == 8 and row["captures"] == 9
    assert row["generation"] == (2 if publication_wrap else 4)
    assert row["publications"] == (1 if publication_wrap else 2)
    assert row["size_bytes"] == timer.SIZE == 180 and qualify([record])["passed"]


@pytest.mark.parametrize("fault", range(1, 55))
def test_every_injected_failure_rejects_success_without_bad_bus_or_thread_capture_access(
    model, fault
):
    _, row, record = run(model, fault)
    assert row["phase"] == 2 and not qualify([record])["passed"]
    assert qualify([record], expected="timeout")["passed"] == (fault == 1)


@pytest.mark.parametrize("fault", [2, 32, 33, 34, 35, 36, 37, 38, 39, 51, 52, 53, 54])
def test_unowned_context_vector_or_irq_fails_before_configuration_writes(model, fault):
    effects, row, record = run(model, fault)
    assert effects["writes"] == effects["irq_writes"] == effects["deliveries"] == 0
    assert row["irq_snapshot_valid"] == 0
    assert not qualify([record], expected="failed")["passed"]


@pytest.mark.parametrize("fault", [25, 26, 27, 28, 29, 45, 46, 47, 50])
def test_lost_domain_or_failed_pin_source_line_pending_active_cleanup_cannot_claim_quiet(
    model, fault
):
    _, _, record = run(model, fault)
    assert not qualify([record], expected="failed")["passed"]


def test_pending_capture_without_delivery_is_not_a_missing_wire_timeout(model):
    _, row, record = run(model, 48)
    assert row["timeout_pending_capture"] == 1 and row["irq_count"] == row["data_reads"] == 0
    assert qualify([record], expected="failed")["passed"]
    assert not qualify([record], expected="timeout")["passed"]
    _, row, record = run(model, 1)
    assert row["timeout_pending_capture"] == 0 and row["irq_error"] == 7
    assert qualify([record], expected="timeout")["passed"]


@pytest.mark.parametrize("fault", [15, 21, 22, 23, 24, 40, 41, 42, 43, 44, 49])
def test_observed_safe_failures_retain_errors_and_rejected_capture_words(model, fault):
    _, row, record = run(model, fault)
    assert qualify([record], expected="failed")["passed"] == (fault != 40)
    if fault == 24:
        assert row["captures"] == 2 and row["frames"] == 0 and row["irq_error"] == 6
        assert ((row["capture1"] - row["capture0"]) & 0xFFFFFFFF) == 1100


@pytest.fixture(scope="module")
def irq_bundle(tmp_path_factory):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    return Bundle(
        compile_bundle(
            SOURCE / "profile-timer-irq-v1.json", tmp_path_factory.mktemp("irq-bundle") / "bundle"
        )
    )


def test_mode_dependency_route_is_exact_and_does_not_inherit_systick_handler(irq_bundle):
    report = read_report(irq_bundle, "coverage")
    row = report["workflows"][WORKFLOW]
    assert row["ready"] and row["mode_instance_scope"] == {
        "tim": {"capture_ch3_pa2_irq": ["TIM5"], "pwm_ch2_irq_pair": ["TIM2"]}
    }
    order = row["mode_order"]
    assert "scb/flash_vector_table" not in order
    assert order.index("systick/quiescent_owned") < order.index("scb/tim5_fixed_irq_context")
    assert order.index("scb/tim5_fixed_irq_context") < order.index("nvic/tim5_capture_prepare")
    assert order.index("nvic/tim5_capture_prepare") < order.index("tim/capture_ch3_pa2_irq")
    assert sum(w["ready"] for w in report["workflows"].values()) == 24
    assert len(report["workflows"]) == 39
    assert report["workflows"]["tim2_tim5_pwm_capture_loopback"]["ready"]
    for name in [
        "feature_eth",
        "feature_flash",
        "feature_rtc",
        "feature_usb_otg_global",
        "tim2_capture_ch1_external",
        "tim2_pwm_ch1_pin",
    ]:
        assert not report["workflows"][name]["ready"]


def test_evidence_source_hashes_and_exact_locators_are_pinned():
    profile = Profile.model_validate_json((SOURCE / "profile-timer-irq-v1.json").read_bytes())
    paths = {s.id: SOURCE / s.path for s in profile.sources}
    evidence = json.loads(paths["timer_irq_evidence"].read_bytes())["pages"]
    assert {
        "rm0090/page:629",
        "rm0090/page:630",
        "rm0090/page:631",
        "pm0214/page:247",
        "pm0214/page:228",
        "header/lines:40-170",
    } <= evidence.keys()
    for source in profile.sources:
        if source.id.startswith("timer_irq_"):
            assert digest(paths[source.id].read_bytes()) == source.expected_sha256
    for item in load_definitions(profile, paths):
        refs = [s for m in item.operating_modes.values() for s in m.sources]
        for register in item.registers:
            refs += register.sources + [s for f in register.fields for s in f.sources]
        for ref in refs:
            if ref.source == "timer_irq_evidence":
                record = evidence[ref.locator]
                assert (
                    len(record.get("source_sha256", record.get("registered_source_sha256", "")))
                    == 64
                )


def test_plan_keeps_all_previous_cases_and_is_not_claimed_physical():
    from praxis.acceptance import AcceptancePlan

    old = AcceptancePlan.model_validate_json(
        (ROOT / "examples/acceptance/stm32f407g-disc1-timer-observations.json").read_bytes()
    )
    new = AcceptancePlan.model_validate_json(
        (ROOT / "examples/acceptance/stm32f407g-disc1-timer-irq.json").read_bytes()
    )
    assert new.cases[:-1] == old.cases and len(new.cases) == 17
    assert new.cases[-1].workflows == [WORKFLOW]
    assert "No new flash" in new.cases[-1].limitations[0]
    assert (APP / "timer_controller.h").read_bytes() == (
        APP.parent / "routes_telemetry_application/timer_controller.h"
    ).read_bytes()


def test_repeated_compilation_is_identical_and_old_bundle_is_unchanged(irq_bundle, tmp_path):
    other = Bundle(compile_bundle(SOURCE / "profile-timer-irq-v1.json", tmp_path / "bundle"))
    assert irq_bundle.manifest.file_hashes == other.manifest.file_hashes
    assert irq_bundle.manifest.bundle_revision == other.manifest.bundle_revision
    parent = Bundle(ROOT / "bundles/stm32f407g-disc1-e01-timer-routes-v1")
    assert (
        parent.manifest.bundle_revision
        == "2dbfa901ec294c0f8edc5e37e87d41a3aa69f169dcce18b4acf088d48f5c0167"
    )
