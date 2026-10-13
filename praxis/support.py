"""Read-only, scoped support assessment from a verified Markdown bundle.

A capability catalog is a contributor's proposed scope, not hardware evidence.
Only the bundle can establish knowledge readiness; compilation and hardware
qualification require separate, artifact-bound evidence.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Identifier, Record
from praxis.render import table


class CapabilityGoal(Record):
    id: Identifier
    category: Identifier
    description: str = Field(min_length=1, max_length=1024)
    workflows: list[Identifier] = Field(default_factory=list, max_length=64)

    @model_validator(mode="after")
    def unique_workflows(self):
        if not self.description.strip() or len(self.workflows) != len(set(self.workflows)):
            raise ValueError("Describe the goal and list each prerequisite workflow once")
        return self


class CatalogTarget(Record):
    id: Identifier
    mcu: str = Field(min_length=1)
    package: str = Field(min_length=1)
    board_revision: str = Field(min_length=1)


class CapabilityCatalog(Record):
    format: Literal["praxis-capability-catalog-v1"]
    target: CatalogTarget
    scope: str = Field(min_length=1, max_length=2048)
    exhaustive: Literal[False] = False
    goals: list[CapabilityGoal] = Field(min_length=1, max_length=512)

    @model_validator(mode="after")
    def unique_goals(self):
        identities = [goal.id for goal in self.goals]
        if not self.scope.strip() or len(identities) != len(set(identities)):
            raise ValueError("Describe the finite scope and use unique goal identities")
        return self


class _ReportRecord(BaseModel):
    # Ignore editorial/forward-compatible fields, but never coerce readiness or counts.
    model_config = ConfigDict(strict=True, extra="ignore")


class _Block(_ReportRecord):
    status: Literal["unmapped_type", "not_selected", "blocked", "declarations_only",
                    "partial_declarations", "reviewed_subset"]
    published: bool
    instances: list[str]
    registers: int = Field(ge=0)
    fields: int = Field(ge=0)
    reviewed_modes: dict[str, list[str]] = Field(default_factory=dict)
    provenance: str


class _Workflow(_ReportRecord):
    ready: bool
    issues: list[str]
    closure: list[str]
    instance_scope: dict[str, list[str]] = Field(default_factory=dict)
    mode_scope: dict[str, list[str]] = Field(default_factory=dict)
    mode_order: list[str] = Field(default_factory=list)
    required_signals: list[str] = Field(default_factory=list)


class _Coverage(_ReportRecord):
    format: Literal["praxis-coverage-v1"]
    target: str
    counts: dict[str, int]
    peripherals: dict[str, _Block]
    workflows: dict[str, _Workflow]


def _coverage(bundle: Bundle) -> _Coverage:
    path = bundle.manifest.documents.get("coverage")
    if path is None:
        raise PraxisError("SUPPORT_REPORT_UNAVAILABLE",
                          "Select a configurable bundle containing a coverage document")
    try:
        data = bundle.read(path).split("```json\n", 1)[1].split("\n```", 1)
        if len(data) != 2:
            raise ValueError("Unclosed coverage JSON")
        coverage = _Coverage.model_validate(load_json(data[0]))
    except (IndexError, ValueError) as exc:
        raise PraxisError("INVALID_SUPPORT_REPORT", "Coverage JSON is missing or invalid") from exc
    blocks = [row for row in coverage.peripherals.values() if row.status != "unmapped_type"]
    expected = {
        "register_blocks": len(blocks),
        "published": sum(row.published for row in blocks),
        "reviewed_subsets": sum(row.status == "reviewed_subset" for row in blocks),
        "blocked": sum(row.status == "blocked" for row in blocks),
        "unmapped_types": sum(row.status == "unmapped_type"
                              for row in coverage.peripherals.values()),
        "registers": sum(row.registers for row in blocks if row.published),
        "fields": sum(row.fields for row in blocks if row.published),
    }
    published = {name for name, row in coverage.peripherals.items() if row.published}
    if (coverage.target != bundle.manifest.target.id
            or any(coverage.counts.get(key) != value for key, value in expected.items())
            or published != set(bundle.manifest.peripherals)
            or any(row.ready and (row.issues or not row.closure
                                  or not set(row.closure) <= published)
                   for row in coverage.workflows.values())):
        raise PraxisError("INVALID_SUPPORT_REPORT",
                          "Coverage identity, counts or ready workflow prerequisites disagree; rebuild")
    return coverage


def _metric(numerator: int, denominator: int, scope: str) -> dict:
    return {"numerator": numerator, "denominator": denominator,
            "percent": round(100 * numerator / denominator, 1) if denominator else None,
            "scope": scope}


def _workflow(row: _Workflow) -> dict:
    return {"knowledge_ready": row.ready, "issues": row.issues,
            "retrieval_closure": row.closure, "instance_scope": row.instance_scope,
            "mode_scope": row.mode_scope, "mode_order": row.mode_order,
            "required_signals": row.required_signals,
            "build_qualification": "not_assessed",
            "hardware_qualification": "not_assessed"}


def assess(bundle: Bundle, catalog_path: Path | None = None,
           workflow: str | None = None) -> dict:
    """Deterministic assessment; no source imports, network, subprocesses or board access."""
    coverage = _coverage(bundle)
    blocks = [row for row in coverage.peripherals.values() if row.status != "unmapped_type"]
    workflows = {name: _workflow(row) for name, row in sorted(coverage.workflows.items())}
    report = {
        "format": "praxis-support-v1",
        "target": bundle.manifest.target.model_dump(),
        "bundle_revision": bundle.manifest.bundle_revision,
        "overall_mcu_completion_percent": None,
        "all_features_supported": False,
        "metrics": {
            "published_register_blocks": _metric(sum(r.published for r in blocks), len(blocks),
                "Recognized register blocks only; declarations do not establish operating support"),
            "blocks_with_reviewed_subset": _metric(
                sum(r.status == "reviewed_subset" for r in blocks), len(blocks),
                "At least some reviewed operating knowledge; not every mode of these blocks"),
            "blocks_with_mode_contract": _metric(sum(bool(r.reviewed_modes) for r in blocks),
                len(blocks), "At least one explicit mode contract; legacy subsets may lack contracts"),
            "declared_workflows_knowledge_ready": _metric(
                sum(row.ready for row in coverage.workflows.values()), len(workflows),
                "Only workflows declared in this profile; neither exhaustive nor hardware qualification"),
        },
        "reviewed_mode_contracts": sum(len(r.reviewed_modes) for r in blocks),
        "workflows": workflows,
        "limits": [
            "The MCU-wide feature denominator has not been established; never average these metrics.",
            "Catalog goals are proposed scope, not authoritative evidence of silicon capabilities.",
            "Knowledge readiness does not prove generated code, physical wiring or initialization order.",
            "Build and hardware qualification require separate exact-artifact evidence.",
            "Published hashes establish integrity, not independent engineering approval.",
        ],
    }
    if catalog_path is not None:
        with catalog_path.open("rb") as handle:
            raw = handle.read(256 * 1024 + 1)
        if len(raw) > 256 * 1024:
            raise PraxisError("CATALOG_LIMIT", "Select a capability catalog under 256 KiB")
        try:
            catalog = CapabilityCatalog.model_validate(load_json(raw))
        except ValidationError as exc:
            raise PraxisError("INVALID_CAPABILITY_CATALOG", str(exc)) from exc
        target = bundle.manifest.target.model_dump()
        if any(target[key] != value for key, value in catalog.target.model_dump().items()):
            raise PraxisError("TARGET_MISMATCH", "Catalog target/package/board revision must match the bundle")
        goals = {}
        for goal in sorted(catalog.goals, key=lambda row: row.id):
            issues = []
            for name in sorted(goal.workflows):
                if name not in workflows:
                    issues.append(f"{name}: workflow not declared in this bundle")
                elif not workflows[name]["knowledge_ready"]:
                    issues.extend(f"{name}: {issue}" for issue in workflows[name]["issues"])
                    if not workflows[name]["issues"]:
                        issues.append(f"{name}: workflow is not knowledge-ready")
            if not goal.workflows:
                issues.append("No workflow requirements authored; scope remains planned")
            goals[goal.id] = {"category": goal.category, "description": goal.description,
                "workflows": sorted(goal.workflows), "knowledge_ready": not issues,
                "status": "planned" if not goal.workflows else "blocked" if issues else "knowledge_ready",
                "issues": issues, "build_qualification": "not_assessed",
                "hardware_qualification": "not_assessed"}
        report["catalog"] = {"sha256": digest(raw), "scope": catalog.scope, "exhaustive": False,
            "metric": _metric(sum(row["knowledge_ready"] for row in goals.values()), len(goals),
                "Unweighted, authored catalog goals only; changing the catalog changes the denominator"),
            "goals": goals}
    if workflow is not None:
        if workflow not in workflows:
            raise PraxisError("UNKNOWN_WORKFLOW",
                f"Unknown exact workflow {workflow!r}; choose from {', '.join(workflows)}")
        report["selected_workflow"] = {"id": workflow, **workflows[workflow]}
    return report


def markdown(report: dict) -> str:
    target = report["target"]
    text = (f"# Praxis support assessment\n\nTarget: {target['id']}; MCU: {target['mcu']}; "
            f"board revision: {target['board_revision']}.\n\n"
            f"Bundle revision: {report['bundle_revision']}.\n\n"
            "**Overall MCU completion is unmeasured. These denominators are limited scopes.**\n\n")
    text += table(["Metric", "Count", "Percent", "Scope"], [
        [name, f"{m['numerator']}/{m['denominator']}",
         "unmeasured" if m['percent'] is None else f"{m['percent']}%", m["scope"]]
        for name, m in report["metrics"].items()])
    text += "\n## Workflow knowledge readiness\n\n" + table(
        ["Workflow", "Knowledge ready", "Missing facts"],
        [[name, str(row["knowledge_ready"]), "; ".join(row["issues"]) or "none reported"]
         for name, row in report["workflows"].items()])
    if "catalog" in report:
        catalog = report["catalog"]
        metric = catalog["metric"]
        text += (f"\n## Authored capability scope\n\n{catalog['scope']}\n\n"
                 f"Catalog SHA-256: {catalog['sha256']}.\n\n"
                 f"Knowledge-ready goals: {metric['numerator']}/{metric['denominator']} "
                 f"({metric['percent']}%). This is not MCU-wide completion.\n\n")
        text += table(["Goal", "Category", "Status", "Missing facts"], [
            [name, row["category"], row["status"], "; ".join(row["issues"]) or "none reported"]
            for name, row in catalog["goals"].items()])
    if "selected_workflow" in report:
        selected = report["selected_workflow"]
        text += (f"\nSelected workflow: {selected['id']}; "
                 f"knowledge ready: {selected['knowledge_ready']}.\n")
    return text + "\n## Limits\n\n" + "\n".join(f"- {line}" for line in report["limits"]) + "\n"
