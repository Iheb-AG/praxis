import os
import shutil
import json
import subprocess
import importlib
from pathlib import Path

import pytest

from praxis.bundle import Bundle

ROOT = Path(__file__).resolve().parents[1]


def require_tool(name):
    if not shutil.which(name):
        if os.environ.get("PRAXIS_REQUIRE_EXTERNAL_TOOLS") == "1":
            pytest.fail(f"Required release tool missing: {name}")
        pytest.skip(f"Optional external tool missing: {name}")


def require_module(name):
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        if os.environ.get("PRAXIS_REQUIRE_EXTERNAL_TOOLS") == "1":
            pytest.fail(f"Required test dependency missing: {name}; install the corresponding project extra")
        pytest.skip(f"Optional Python dependency missing: {name}")


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    # Strict acceptance may never succeed with unexecuted checks, including
    # collection-level skips or a new test that bypasses require_tool/module.
    if os.environ.get("PRAXIS_REQUIRE_EXTERNAL_TOOLS") == "1":
        reporter = session.config.pluginmanager.get_plugin("terminalreporter")
        if exitstatus == pytest.ExitCode.OK and reporter is not None and reporter.stats.get("skipped"):
            session.exitstatus = pytest.ExitCode.TESTS_FAILED


def require_image(lock):
    require_tool("podman")
    image = json.loads(lock.read_text()).get("image")
    available = False
    if image:
        result = subprocess.run(["podman", "image", "exists", image], timeout=10, capture_output=True)
        available = result.returncode == 0
    if not available:
        if os.environ.get("PRAXIS_REQUIRE_EXTERNAL_TOOLS") == "1":
            pytest.fail(f"Provision the locally installed sandbox image for {lock.name}")
        pytest.skip(f"Local sandbox image unavailable for {lock.name}")
    return lock


@pytest.fixture(params=["stm32f401re", "atmega328p"])
def bundle(request):
    return Bundle(ROOT / "bundles" / request.param)

