import json

import pytest

from praxis.errors import PraxisError
from conftest import require_tool
from praxis.bundle import Bundle
from praxis.target_matrix import compile_matrix, load
from test_mcu_inventory import mcu_profile


def catalog(directory):
    profile, data = mcu_profile(directory / "part")
    path = directory / "catalog.json"
    path.write_text(json.dumps({"schema_version": 1, "targets": [
        {"id": data["target"]["id"], "profile": "part/profile.json"}]}))
    return path, profile, data


@pytest.mark.parametrize("mutation", ["duplicate", "traversal", "wrong_target", "symlink"])
def test_matrix_rejects_ambiguous_escaped_and_mismatched_inputs(tmp_path, mutation):
    path, profile, data = catalog(tmp_path)
    matrix = json.loads(path.read_text())
    if mutation == "duplicate":
        matrix["targets"] *= 2
    elif mutation == "traversal":
        matrix["targets"][0]["profile"] = "../outside.json"
    elif mutation == "wrong_target":
        matrix["targets"][0]["id"] = "wrong_target"
    else:
        (tmp_path / "linked.json").symlink_to(profile)
        matrix["targets"][0]["profile"] = "linked.json"
    path.write_text(json.dumps(matrix))
    with pytest.raises(PraxisError):
        load(path)


def test_unknown_target_fails_before_compilation(tmp_path, monkeypatch):
    path, _, _ = catalog(tmp_path)
    monkeypatch.setattr("praxis.target_matrix.compile_bundle", lambda *args: pytest.fail("Do not compile"))
    with pytest.raises(PraxisError, match="UNKNOWN_TARGET"):
        compile_matrix(path, tmp_path / "output", ["absent"])
    assert not (tmp_path / "output").exists()


def test_matrix_failure_report_is_explicit_and_idempotent(tmp_path, monkeypatch):
    path, _, data = catalog(tmp_path)
    def fail(*args):
        raise PraxisError("MISSING_TOOL", "Test extractor is unavailable")
    monkeypatch.setattr("praxis.target_matrix.compile_bundle", fail)
    output = tmp_path / "output"
    report = compile_matrix(path, output)
    assert not report["passed"]
    assert report["targets"][data["target"]["id"]]["error_code"] == "MISSING_TOOL"
    assert compile_matrix(path, output) == report
    assert json.loads((output / "report.json").read_text()) == report
    assert not (output / data["target"]["id"]).exists()


def test_batch_cli_returns_failure_exit_code_and_report(tmp_path, monkeypatch, capsys):
    from praxis.cli import main
    path, _, _ = catalog(tmp_path)
    def fail(*args):
        raise PraxisError("SOURCE_HASH_MISMATCH", "Changed source")
    monkeypatch.setattr("praxis.target_matrix.compile_bundle", fail)
    assert main(["compile-matrix", "--catalog", str(path), "--output", str(tmp_path / "out")]) == 1
    assert json.loads(capsys.readouterr().out)["passed"] is False


def test_successful_batch_is_reproducible_and_isolates_failed_targets(tmp_path):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    path, _, data = catalog(tmp_path)
    output = tmp_path / "first"
    first = compile_matrix(path, output)
    assert first["passed"]
    assert compile_matrix(path, output) == first
    identity = data["target"]["id"]
    assert Bundle(output / identity).manifest.target.clock_hz is None
    second, candidate = mcu_profile(tmp_path / "bad-part")
    candidate["target"]["id"] = "bad_part"
    candidate["sources"][0]["expected_sha256"] = "0" * 64
    second.write_text(json.dumps(candidate))
    matrix = json.loads(path.read_text())
    matrix["targets"].append({"id": "bad_part", "profile": "bad-part/profile.json"})
    path.write_text(json.dumps(matrix))
    result = compile_matrix(path, tmp_path / "mixed")
    assert not result["passed"]
    assert result["targets"][identity]["status"] == "published"
    assert result["targets"]["bad_part"]["error_code"] == "SOURCE_HASH_MISMATCH"
    assert not (tmp_path / "mixed/bad_part").exists()
