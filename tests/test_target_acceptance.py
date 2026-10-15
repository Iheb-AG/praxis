import copy
import json

import pytest
from pydantic import ValidationError

from praxis.acceptance import AcceptancePlan, load_plan, summarize
from praxis.errors import PraxisError


def plan_data():
    return {
        "format": "praxis-target-acceptance-plan-v1",
        "target": {"id": "test_target", "mcu": "TEST", "package": "TEST", "board_revision": "R1"},
        "scope": "Compile-only test scope",
        "cases": [{"id": "demo", "source_directory": "demo/app", "workflows": ["polling"],
                   "limitations": ["Not physically tested"]}],
    }


@pytest.mark.parametrize("path", ["/absolute", "../escape", "demo/../escape", "a\\b", "./app", "a//b"])
def test_plan_rejects_unsafe_and_noncanonical_paths(path):
    raw = plan_data()
    raw["cases"][0]["source_directory"] = path
    with pytest.raises(ValidationError):
        AcceptancePlan.model_validate(raw)


@pytest.mark.parametrize("mutation", ["identity", "source", "workflow"])
def test_plan_rejects_duplicate_scopes(mutation):
    raw = plan_data()
    if mutation == "workflow":
        raw["cases"][0]["workflows"] *= 2
    else:
        duplicate = copy.deepcopy(raw["cases"][0])
        duplicate["id" if mutation == "source" else "source_directory"] = "other"
        raw["cases"].append(duplicate)
    with pytest.raises(ValidationError):
        AcceptancePlan.model_validate(raw)


def support():
    return {"target": plan_data()["target"], "bundle_revision": "a" * 64, "metrics": {}, "limits": [],
            "workflows": {"polling": {"knowledge_ready": True, "issues": []},
                          "usb": {"knowledge_ready": False, "issues": ["mode unreviewed"]}},
            "catalog": {"exhaustive": False, "goals": {"bootloader": {"issues": ["No workflow authored"]}}}}


def test_successful_builds_never_promote_incomplete_mcu_or_historical_hardware_evidence():
    plan = AcceptancePlan.model_validate(plan_data())
    builds = {"demo": {"passed": True, "bundle_revision": "a" * 64, "artifact_id": "c" * 64}}
    report = summarize(support(), plan, builds, {"protocol": True})
    assert report["software_checks_passed"] is True
    assert report["full_mcu_accepted"] is False
    assert report["overall_mcu_completion_percent"] is None
    assert report["workflows"]["polling"]["build_qualification"] == "linked_examples_only"
    assert report["workflows"]["polling"]["hardware_qualification"] == "not_assessed_for_this_revision"
    assert "usb: mode unreviewed" in report["acceptance_blockers"]
    assert "catalog/bootloader: No workflow authored" in report["acceptance_blockers"]


@pytest.mark.parametrize("failure", ["missing", "failed", "revision", "artifact", "check", "extra", "empty"])
def test_no_missing_or_stale_case_can_pass_software_acceptance(failure):
    builds = {"demo": {"passed": True, "bundle_revision": "a" * 64, "artifact_id": "c" * 64}}
    checks = {"protocol": True}
    if failure == "missing":
        builds.clear()
    elif failure == "failed":
        builds["demo"]["passed"] = False
    elif failure == "revision":
        builds["demo"]["bundle_revision"] = "b" * 64
    elif failure == "artifact":
        builds["demo"].pop("artifact_id")
    elif failure == "extra":
        builds["unexpected"] = builds["demo"].copy()
    elif failure == "empty":
        checks.clear()
    else:
        checks["protocol"] = False
    assert summarize(support(), AcceptancePlan.model_validate(plan_data()), builds, checks)["software_checks_passed"] is False


@pytest.mark.parametrize("mutation", ["target", "symlink", "workflow"])
def test_binding_fails_before_any_build(tmp_path, monkeypatch, mutation):
    from types import SimpleNamespace
    raw = plan_data()
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    (workspace / "demo").mkdir()
    source = workspace / "demo/app"
    if mutation == "symlink":
        outside = tmp_path / "outside"
        outside.mkdir()
        source.symlink_to(outside, target_is_directory=True)
    else:
        source.mkdir()
    if mutation == "target":
        raw["target"]["mcu"] = "WRONG"
    if mutation == "workflow":
        raw["cases"][0]["workflows"] = ["absent"]
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(raw))
    target = SimpleNamespace(model_dump=lambda: plan_data()["target"])
    bundle = SimpleNamespace(manifest=SimpleNamespace(target=target))
    monkeypatch.setattr("praxis.acceptance.assess", lambda _: support())
    with pytest.raises(PraxisError):
        load_plan(path, bundle, workspace)


def test_registered_applications_obey_strict_sandbox_source_contract(tmp_path):
    from conftest import ROOT
    from praxis.verify import snapshot
    plan = AcceptancePlan.model_validate(json.loads(
        (ROOT / "examples/acceptance/stm32f407g-disc1.json").read_text()))
    for case in plan.cases:
        destination = tmp_path / case.id
        destination.mkdir()
        units, fingerprint = snapshot(ROOT / "examples" / case.source_directory, destination)
        assert units and len(fingerprint) == 64
