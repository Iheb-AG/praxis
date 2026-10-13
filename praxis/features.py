"""Target-wide inventory from verified Markdown; no semantic inference or probes."""

from __future__ import annotations

import json

from praxis.errors import PraxisError
from praxis.render import table


def feature_report(coverage: dict) -> dict:
    entities = {}
    for name, row in sorted(coverage["peripherals"].items()):
        if row["status"] == "unmapped_type":
            continue  # A helper C type is not another silicon peripheral.
        modes = row.get("reviewed_modes", {})
        entities[name] = {
            "declaration_status": row["status"],
            "published": row["published"],
            "declared_instances": row["instances"],
            "reviewed_modes": modes,
            "mode_scoped_workflows": sorted(
                key
                for key, value in coverage["workflows"].items()
                if (name in value.get("mode_scope", {})
                    or any(mode.startswith(name + '/') for mode in value.get('mode_order', []))) and value["ready"]
            ),
            "source": row["provenance"],
            "issues": row["issues"],
            "missing": ([] if modes else ["No explicit reviewed operating-mode contract"]),
            "physical_package_availability": "not established by register declarations",
            "build_qualification": "separate artifact evidence required",
            "hardware_qualification": "separate workflow evidence required",
        }
    return {
        "format": "praxis-features-v1",
        "target": coverage["target"],
        "all_features_supported": False,
        "scope": "Recognized register blocks, declared instances and explicitly reviewed modes; "
        "not an exhaustive inventory of every instruction, boot mode or operating combination.",
        "counts": {
            "register_blocks": len(entities),
            "declared_instances": sum(len(r["declared_instances"]) for r in entities.values()),
            "reviewed_mode_contracts": sum(len(r["reviewed_modes"]) for r in entities.values()),
            "blocks_without_mode_contracts": sum(
                not r["reviewed_modes"] for r in entities.values()
            ),
        },
        "features": entities,
        "limits": [
            "Register instances do not establish package pins or board connectivity.",
            "A reviewed mode is not a compiler check or a hardware qualification.",
            "Capability absence in this inventory does not establish silicon absence.",
        ],
    }


def markdown(report: dict) -> str:
    return (
        "# Target feature support\n\n" + report["scope"] + "\n\n"
        "**Complete MCU feature support is not established.**\n\n"
        + table(
            [
                "Entity",
                "Declared instances",
                "Reviewed modes and scope",
                "Ready mode workflows",
                "Declaration status",
                "Provenance",
            ],
            [
                [
                    name,
                    ", ".join(r["declared_instances"]),
                    "; ".join(
                        f"{m}: {', '.join(instances)}"
                        for m, instances in r["reviewed_modes"].items()
                    )
                    or "none",
                    ", ".join(r["mode_scoped_workflows"]) or "none",
                    r["declaration_status"],
                    r["source"],
                ]
                for name, r in report["features"].items()
            ],
        )
        + "\nSee [[index]], [[coverage]] and [[sources]].\n\n## Machine-readable report\n\n```json\n"
        + json.dumps(report, sort_keys=True, separators=(",", ":"))
        + "\n```\n"
    )


def from_bundle(bundle):
    if "features" not in bundle.manifest.documents:
        raise PraxisError(
            "FEATURE_REPORT_UNAVAILABLE",
            "Compile a current configurable profile to publish feature support",
        )
    text = bundle.read(bundle.manifest.documents["features"])
    from praxis.jsonio import load_json

    try:
        return load_json(text.split("```json\n", 1)[1].split("\n```", 1)[0])
    except IndexError as exc:
        raise PraxisError(
            "INVALID_FEATURE_REPORT", "Missing complete feature JSON in verified Markdown"
        ) from exc
