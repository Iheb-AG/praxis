"""Support preflight must never promote declarations or planned goals to readiness."""

import json
import subprocess
import sys

import pytest

from praxis.bundle import Bundle, digest, revision
from praxis.cli import main
from praxis.errors import PraxisError
from praxis.support import assess, markdown
from conftest import ROOT

BUNDLE = ROOT / "bundles/stm32f407g-disc1-e01-clock-v1"
CATALOG = ROOT / "examples/capabilities/stm32f407g-disc1.json"


def write_catalog(tmp_path, mutate):
    data = json.loads(CATALOG.read_text())
    mutate(data)
    path = tmp_path / "catalog.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def replace_coverage(tmp_path, mutate):
    """Simulate a publisher bug with valid hashes, rather than a corrupt file."""
    source = Bundle(BUNDLE)
    manifest = source.manifest.model_dump()
    for path, content in source.documents.items():
        destination = tmp_path / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        if path == manifest["documents"]["coverage"]:
            data = json.loads(content.split("```json\n")[1].split("\n```")[0])
            mutate(data)
            content = "# Coverage\n\n```json\n" + json.dumps(data) + "\n```\n"
            manifest["file_hashes"][path] = digest(content.encode())
        destination.write_text(content, encoding="utf-8")
    manifest["bundle_revision"] = revision(manifest)
    (tmp_path / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    return Bundle(tmp_path)


def test_actual_counts_have_explicit_denominators_and_no_overall_percentage():
    report = assess(Bundle(BUNDLE), CATALOG)
    assert report["metrics"]["published_register_blocks"]["percent"] == 97.6
    assert report["metrics"]["blocks_with_reviewed_subset"]["percent"] == 35.7
    assert report["metrics"]["blocks_with_mode_contract"]["percent"] == 21.4
    assert report["metrics"]["declared_workflows_knowledge_ready"] == {
        "numerator": 9, "denominator": 20, "percent": 45.0,
        "scope": "Only workflows declared in this profile; neither exhaustive nor hardware qualification",
    }
    assert report["reviewed_mode_contracts"] == 12
    assert report["overall_mcu_completion_percent"] is None
    assert report["all_features_supported"] is False
    assert report["catalog"]["metric"]["numerator"] == 9
    assert report["catalog"]["metric"]["denominator"] == 26
    assert report["catalog"]["exhaustive"] is False
    assert report["catalog"]["sha256"] == digest(CATALOG.read_bytes())
    assert report["catalog"]["goals"]["application_bootloader"]["status"] == "planned"
    assert not report["catalog"]["goals"]["spi1_wired_polling"]["knowledge_ready"]


def test_all_catalog_workflows_must_be_ready_and_missing_names_remain_blocked(tmp_path):
    path = write_catalog(tmp_path, lambda data: data.update(goals=[
        {"id": "mixed", "category": "test", "description": "Both must pass",
         "workflows": ["crc_word_feed", "feature_flash"]},
        {"id": "missing", "category": "test", "description": "Future workflow",
         "workflows": ["not_yet_authored"]},
    ]))
    goals = assess(Bundle(BUNDLE), path)["catalog"]["goals"]
    assert goals["mixed"]["status"] == "blocked"
    assert any("flash.program_erase" in issue for issue in goals["mixed"]["issues"])
    assert goals["missing"]["status"] == "blocked"
    assert goals["missing"]["issues"] == ["not_yet_authored: workflow not declared in this bundle"]


def test_finite_catalog_at_100_percent_never_claims_complete_mcu_support(tmp_path):
    path = write_catalog(tmp_path, lambda data: data.update(goals=[
        {"id": "crc_only", "category": "test", "description": "One finite goal",
         "workflows": ["crc_word_feed"]},
    ]))
    report = assess(Bundle(BUNDLE), path)
    assert report["catalog"]["metric"]["percent"] == 100.0
    assert report["overall_mcu_completion_percent"] is None
    assert not report["all_features_supported"]
    assert report["catalog"]["goals"]["crc_only"]["hardware_qualification"] == "not_assessed"
    assert "not MCU-wide completion" in markdown(report)


@pytest.mark.parametrize("key", ["id", "mcu", "package", "board_revision"])
def test_catalog_requires_exact_target_identity(tmp_path, key):
    path = write_catalog(tmp_path, lambda data: data["target"].update({key: "wrong_target"}))
    with pytest.raises(PraxisError, match="TARGET_MISMATCH"):
        assess(Bundle(BUNDLE), path)


@pytest.mark.parametrize("mutate", [
    lambda d: d["goals"].append(d["goals"][0]),
    lambda d: d["goals"][0].update(workflows=["gpio_led_button", "gpio_led_button"]),
    lambda d: d.update(exhaustive=True),
    lambda d: d.update(goals=[]),
    lambda d: d.update(scope=" "),
    lambda d: d["goals"][0].update(description=" "),
    lambda d: d["goals"][0].update(hardware_qualified=True),
])
def test_invalid_or_self_qualifying_catalogs_are_rejected(tmp_path, mutate):
    with pytest.raises(PraxisError, match="INVALID_CAPABILITY_CATALOG"):
        assess(Bundle(BUNDLE), write_catalog(tmp_path, mutate))


def test_duplicate_json_keys_and_oversized_catalogs_fail(tmp_path):
    path = tmp_path / "catalog.json"
    path.write_text('{"format": "a", "format": "b"}')
    with pytest.raises(PraxisError, match="DUPLICATE_IDENTITY"):
        assess(Bundle(BUNDLE), path)
    path.write_bytes(b" " * (256 * 1024 + 1))
    with pytest.raises(PraxisError, match="CATALOG_LIMIT"):
        assess(Bundle(BUNDLE), path)


@pytest.mark.parametrize("mutate", [
    lambda d: d.update(target="another_target"),
    lambda d: d["counts"].update(published=42),
    lambda d: d["workflows"]["feature_flash"].update(ready=True),
    lambda d: d["workflows"]["crc_word_feed"].update(ready="true"),
    lambda d: d["workflows"]["crc_word_feed"].update(closure=["itm"]),
    lambda d: d["workflows"]["crc_word_feed"].update(closure=[]),
    lambda d: d["peripherals"]["crc"].update(published=False),
])
def test_hashes_do_not_hide_inconsistent_coverage(tmp_path, mutate):
    bundle = replace_coverage(tmp_path, mutate)
    with pytest.raises(PraxisError, match="INVALID_SUPPORT_REPORT"):
        assess(bundle)


def test_workflow_preflight_exit_codes_and_legacy_bundle_error(capsys):
    args = ["support", "--bundle", str(BUNDLE), "--workflow"]
    assert main([*args, "uart_timer_interrupts"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert report["selected_workflow"]["knowledge_ready"]
    assert report["selected_workflow"]["hardware_qualification"] == "not_assessed"
    assert main([*args, "feature_flash"]) == 1
    assert not json.loads(capsys.readouterr().out)["selected_workflow"]["knowledge_ready"]
    assert main([*args, "UART_TIMER_INTERRUPTS"]) == 2
    assert "UNKNOWN_WORKFLOW" in capsys.readouterr().err
    assert main(["support", "--bundle", str(ROOT / "bundles/atmega328p")]) == 2
    assert "SUPPORT_REPORT_UNAVAILABLE" in capsys.readouterr().err


def test_report_is_deterministic_and_markdown_preserves_blockers(capsys):
    first = assess(Bundle(BUNDLE), CATALOG, "feature_flash")
    assert json.dumps(first, sort_keys=True) == json.dumps(assess(Bundle(BUNDLE), CATALOG,
                                                             "feature_flash"), sort_keys=True)
    assert main(["support", "--bundle", str(BUNDLE), "--format", "markdown",
                 "--catalog", str(CATALOG)]) == 0
    text = capsys.readouterr().out
    assert "97.6%" in text and "SPI1_SCK" in text and "program_erase" in text
    assert "application_bootloader" in text and "planned" in text


def test_assessment_runs_from_unrelated_directory_without_ingestion_or_probe_imports(tmp_path):
    code = """
import json, sys
from pathlib import Path
from praxis.bundle import Bundle
from praxis.support import assess
report = assess(Bundle(Path(sys.argv[1])), Path(sys.argv[2]))
assert not any(name.startswith(('praxis.adapters', 'praxis.compiler', 'praxis.hardware',
    'praxis.programming', 'clang', 'pdfplumber', 'httpx', 'defusedxml')) for name in sys.modules)
print(json.dumps(report, sort_keys=True))
"""
    result = subprocess.run([sys.executable, "-c", code, str(BUNDLE), str(CATALOG)],
                            cwd=tmp_path, capture_output=True, text=True, timeout=15, check=True)
    assert json.loads(result.stdout) == assess(Bundle(BUNDLE), CATALOG)


def test_catalog_schema_is_available_to_contributors(capsys):
    assert main(["schema", "--kind", "capability-catalog"]) == 0
    schema = json.loads(capsys.readouterr().out)
    assert schema["properties"]["exhaustive"]["const"] is False
    assert "CapabilityGoal" in schema["$defs"]


def test_earlier_immutable_bundle_has_its_own_readiness():
    earlier = Bundle(ROOT / "bundles/stm32f407g-disc1-e01-features-v1")
    report = assess(earlier, CATALOG)
    assert report["reviewed_mode_contracts"] == 7
    assert not report["workflows"]["rng_pll_polling"]["knowledge_ready"]
    assert report["catalog"]["goals"]["pll_hse8_168mhz"]["status"] == "blocked"
    assert report["bundle_revision"] != Bundle(BUNDLE).manifest.bundle_revision
