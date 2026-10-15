"""Fail-closed release gate. Missing tools or review are blockers, not passing skips."""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from praxis.bundle import Bundle
from praxis.firmware_assets import FirmwareAssets

ROOT = Path(__file__).resolve().parents[1]


def bundle_revisions(directory: Path) -> dict[str, str]:
    """Review every shipped bundle; adding another cannot bypass a fixed list."""
    return {path.name: Bundle(path).manifest.bundle_revision
            for path in sorted(directory.iterdir()) if path.is_dir() and not path.name.startswith('.')}


def main():
    required = ["clang", "gcc", "arm-none-eabi-gcc", "avr-gcc", "dtc", "fdtoverlay", "kicad-cli", "podman"]
    blockers = [f"Missing external tool: {name}" for name in required if not shutil.which(name)]
    lock = json.loads((ROOT / "toolchain.lock.json").read_text())
    review = json.loads((ROOT / "release-review.json").read_text())
    if not lock.get("image"):
        blockers.append("Toolchain image lock is unprovisioned")
    revisions = bundle_revisions(ROOT / "bundles")
    asset_revision = FirmwareAssets(ROOT / "assets/stm32f407vg").identity
    if (review.get("status") != "independently-reviewed" or not review.get("reviewer")
            or review.get("bundle_revisions") != revisions):
        blockers.append("Independent review of the exact current bundle revisions is missing")
    if review.get("firmware_asset_revision") != asset_revision:
        blockers.append("Independent review of the exact firmware asset revision is missing")
    if blockers:
        print(json.dumps({"release_ready": False, "blockers": blockers}, indent=2))
        return 2
    env = {**os.environ, "PRAXIS_REQUIRE_EXTERNAL_TOOLS": "1"}
    result = subprocess.run([sys.executable, "-m", "pytest", "-q"], cwd=ROOT, env=env, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())

