"""Strict acceptance must fail rather than pass with unexecuted checks."""
import os
import subprocess
import sys

import pytest

from conftest import ROOT, require_module, require_tool


def test_missing_native_tool_is_a_failure_in_strict_mode(monkeypatch):
    monkeypatch.setenv("PRAXIS_REQUIRE_EXTERNAL_TOOLS", "1")
    monkeypatch.setattr("conftest.shutil.which", lambda name: None)
    with pytest.raises(pytest.fail.Exception, match="Required release tool missing"):
        require_tool("a_required_tool")


def test_missing_python_dependency_is_a_failure_in_strict_mode(monkeypatch):
    monkeypatch.setenv("PRAXIS_REQUIRE_EXTERNAL_TOOLS", "1")
    with pytest.raises(pytest.fail.Exception, match="Required test dependency missing"):
        require_module("praxis_deliberately_nonexistent_test_dependency")


def test_strict_session_refuses_an_unexpected_skip(tmp_path):
    fixture = tmp_path / "test_negative_skip_fixture.py"
    fixture.write_text("import pytest\ndef test_unexecuted():\n    pytest.skip('negative policy fixture')\n")
    env = {**os.environ, "PRAXIS_REQUIRE_EXTERNAL_TOOLS": "1", "PYTHONPATH": str(ROOT / "tests")}
    result = subprocess.run([sys.executable, "-m", "pytest", "-p", "conftest", "-q", str(fixture)],
        cwd=tmp_path, env=env, text=True, capture_output=True, timeout=20)
    assert result.returncode == 1, result.stdout + result.stderr
    assert "1 skipped" in result.stdout  # Deliberate negative fixture; acceptance must fail.
