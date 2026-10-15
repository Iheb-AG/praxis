"""Artifact-bound software acceptance; never infer full MCU support from compilation.

Target plans are authored test scope, not manufacturer facts. Coverage and operating
requirements come from the integrity-checked bundle. Hardware and independent review
remain separate evidence gates.
"""
from pathlib import Path, PurePosixPath
from typing import Literal

from pydantic import Field, model_validator

from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Identifier, Record
from praxis.support import CatalogTarget, assess


class AcceptanceCase(Record):
    id: Identifier
    source_directory: str = Field(min_length=1)
    workflows: list[Identifier] = Field(min_length=1)
    limitations: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def safe_case(self):
        path = PurePosixPath(self.source_directory)
        if (path.is_absolute() or ".." in path.parts or "\\" in self.source_directory
                or str(path) != self.source_directory or not path.parts
                or len(set(self.workflows)) != len(self.workflows)):
            raise ValueError("Use a normalized relative source path and unique workflow names")
        return self


class AcceptancePlan(Record):
    format: Literal["praxis-target-acceptance-plan-v1"]
    target: CatalogTarget
    scope: str = Field(min_length=1)
    cases: list[AcceptanceCase] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_cases(self):
        if len({case.id for case in self.cases}) != len(self.cases):
            raise ValueError("Acceptance case identities must be unique")
        if len({case.source_directory for case in self.cases}) != len(self.cases):
            raise ValueError("Register each application directory once")
        return self


def load_plan(path: Path, bundle: Bundle, workspace: Path) -> AcceptancePlan:
    plan = AcceptancePlan.model_validate(load_json(path.read_bytes()))
    target = bundle.manifest.target.model_dump()
    if any(target[key] != value for key, value in plan.target.model_dump().items()):
        raise PraxisError("TARGET_MISMATCH", "Acceptance target/package/revision must match the bundle")
    root = workspace.resolve(strict=True)
    workflows = assess(bundle)["workflows"]
    for case in plan.cases:
        source = (root / case.source_directory).resolve(strict=True)
        if not source.is_relative_to(root) or not source.is_dir():
            raise PraxisError("INVALID_PATH", "Acceptance source must remain inside the application workspace")
        unknown = set(case.workflows) - workflows.keys()
        if unknown:
            raise PraxisError("UNKNOWN_WORKFLOW", f"{case.id}: undeclared workflows {sorted(unknown)}")
    return plan


def summarize(support: dict, plan: AcceptancePlan, builds: dict, checks: dict) -> dict:
    """Join exact-revision build evidence to scopes without promoting it to physical proof."""
    revision = support["bundle_revision"]
    workflows = {}
    for name, row in support["workflows"].items():
        declared = [case.id for case in plan.cases if name in case.workflows]
        verified = [identity for identity in declared if
                    builds.get(identity, {}).get("passed") is True
                    and builds[identity].get("bundle_revision") == revision
                    and builds[identity].get("artifact_id")]
        workflows[name] = {**row, "application_cases": declared,
            "build_qualification": "linked_examples_only" if verified else "not_assessed",
            "linked_cases": verified, "hardware_qualification": "not_assessed_for_this_revision"}
    blockers = ["Software-only replay does not assess independent release sign-off",
                "Software-only replay does not confirm physical board identity or qualify per-mode behavior",
                "Historical physical observations do not transfer to these builds"]
    blockers.extend(f"{name}: {issue}" for name, row in workflows.items() if not row["knowledge_ready"]
                    for issue in (row["issues"] or ["not knowledge-ready"]))
    blockers.extend(f"{name}: no exact-revision linked example assessed" for name, row in workflows.items()
                    if not row["linked_cases"])
    catalog = support.get("catalog", {})
    if catalog.get("exhaustive") is not True:
        blockers.append("No exhaustive manufacturer-wide mode/instance inventory supplied")
    blockers.extend(f"catalog/{name}: {issue}" for name, row in catalog.get("goals", {}).items()
                    for issue in row["issues"])
    software_passed = bool(checks) and all(value is True for value in checks.values())
    software_passed &= set(builds) == {case.id for case in plan.cases}
    software_passed &= all(row.get("passed") is True and row.get("bundle_revision") == revision
                           and bool(row.get("artifact_id")) for row in builds.values())
    return {"format": "praxis-target-acceptance-v1", "target": support["target"],
        "bundle_revision": revision, "software_checks_passed": bool(software_passed),
        "full_mcu_accepted": False, "overall_mcu_completion_percent": None,
        "scope": plan.scope, "metrics": support["metrics"], "catalog": catalog,
        "workflows": workflows, "builds": builds, "checks": checks,
        "acceptance_blockers": sorted(set(blockers)), "hardware_operations": 0,
        "limits": [*support["limits"],
                   "A linked example covers its declared code paths, not every workflow or operating mode.",
                   "Negative retrieval guards passing do not turn missing capabilities into accepted support."]}


def hash_plan(plan: AcceptancePlan) -> str:
    return digest(plan.model_dump_json().encode())
