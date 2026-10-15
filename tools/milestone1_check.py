"""Run Milestone 1 implementation acceptance; report independent release review separately."""

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from praxis.bundle import Bundle
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.routing import Session

ROOT = Path(__file__).resolve().parents[1]
TARGETS = ["stm32f401re", "atmega328p", "stm32f407vgt6", "stm32f407g-disc1-e01-m1",
           "stm32f407g-disc1-e01-discovery-v2"]
TESTS = ["tests/test_compiler_adapters.py", "tests/test_f407_ingestion.py",
         "tests/test_board_ingestion.py", "tests/test_bundle_routing.py", "tests/test_web_import.py",
         "tests/test_configurable_discovery.py", "tests/test_large_documents.py",
         "tests/test_kicad_pin_names.py", "tests/test_dependency_policy.py"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".praxis-output/milestone1/report.json")
    args = parser.parse_args(argv)
    tools = ["clang", "gcc", "arm-none-eabi-gcc", "avr-gcc", "dtc", "fdtoverlay", "kicad-cli"]
    blockers = [f"Missing acceptance tool: {name}" for name in tools if not shutil.which(name)]
    for module in ("clang", "defusedxml", "bs4", "pdfplumber", "pytest"):
        if importlib.util.find_spec(module) is None:
            blockers.append(f"Missing acceptance dependency: {module}")
    revisions = {}
    try:
        for name in TARGETS:
            bundle = Bundle(ROOT / "bundles" / name)
            Session(bundle)
            revisions[name] = bundle.manifest.bundle_revision
    except Exception as exc:
        blockers.append(f"Bundle validation failed: {exc}")
    implementation_ready = False
    test_result = None
    if not blockers:
        env = {**os.environ, "PRAXIS_REQUIRE_EXTERNAL_TOOLS": "1"}
        result = subprocess.run([sys.executable, "-m", "pytest", "-q", *TESTS],
                                cwd=ROOT, env=env, capture_output=True, text=True, timeout=180)
        test_result = {"exit_code": result.returncode, "stdout": result.stdout,
                       "stderr": result.stderr}
        implementation_ready = result.returncode == 0
        if not implementation_ready:
            blockers.append("Milestone 1 acceptance tests failed")
    try:
        review = load_json((ROOT / "release-review.json").read_bytes())
    except (OSError, ValueError, PraxisError):
        review = {}
    if not isinstance(review, dict):
        review = {}
    independent_review = (review.get("status") == "independently-reviewed" and
        isinstance(review.get("reviewer"), str) and bool(review["reviewer"].strip()) and
        review.get("bundle_revisions") == revisions and len(revisions) == len(TARGETS))
    report = {"milestone": 1, "implementation_checks_passed": implementation_ready,
              "independent_review_passed": independent_review,
              "milestone_complete": implementation_ready,
              "bundle_revisions": revisions, "tools": {name: shutil.which(name) for name in tools},
              "tests": test_result, "blockers": blockers,
              "release_notes": ["Milestone 1 implementation acceptance does not establish v1 release readiness.",
                  "Independent engineering review and the remaining sandbox/release checks are separate."] +
                  ([] if independent_review else ["Independent review of all included reference revisions remains pending."]),
              "physical_board": "STM32F407G-DISC1 identified; PCB revision and modifications unconfirmed",
              "pdf_schematics": "Reviewed transcription supported; automatic geometry interpretation is deferred"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: report[key] for key in ("milestone_complete", "implementation_checks_passed", "blockers")}, indent=2))
    return 0 if report["milestone_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
