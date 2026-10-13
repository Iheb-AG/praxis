import os
import shutil
import json
import subprocess
from pathlib import Path

import pytest

from praxis.bundle import Bundle

ROOT = Path(__file__).resolve().parents[1]


def require_tool(name):
    if not shutil.which(name):
        if os.environ.get("PRAXIS_REQUIRE_EXTERNAL_TOOLS") == "1":
            pytest.fail(f"Required release tool missing: {name}")
        pytest.skip(f"Optional external tool missing: {name}")


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

