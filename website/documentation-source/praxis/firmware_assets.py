"""Hash-registered firmware inputs, kept separate from immutable knowledge bundles."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from praxis.bundle import Bundle, digest, read_inside, revision
from praxis.errors import PraxisError


class Asset(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    path: str
    sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    kind: Literal["header", "startup", "system", "runtime", "linker", "license", "evidence"]
    origin: str = Field(min_length=1)
    version: str = Field(min_length=1)
    license: str = Field(min_length=1)


class AssetManifest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    schema_version: Literal[1]
    bundle_revision: str = Field(pattern=r"^[0-9a-f]{64}$")
    mcu: Literal["STM32F407VGT6"]
    package: Literal["Package_QFP:LQFP-100_14x14mm_P0.5mm"]
    profile: Literal["stm32f407vg-c11-flash"]
    review: str = Field(min_length=1)
    files: list[Asset] = Field(min_length=1)


class FirmwareAssets:
    def __init__(self, root: Path, bundle: Bundle | None = None):
        self.root = root.resolve()
        try:
            self.manifest = AssetManifest.model_validate_json(read_inside(self.root, "manifest.json", 1024 * 1024))
        except ValidationError as exc:
            raise PraxisError("INVALID_ASSETS", str(exc)) from exc
        if revision(self.manifest.model_dump()) != self.manifest.bundle_revision:
            raise PraxisError("INTEGRITY_ERROR", "Firmware asset manifest revision mismatch")
        if bundle and (bundle.manifest.target.knowledge_adapter is not None
                or bundle.manifest.target.family != "stm32"
                or (bundle.manifest.target.mcu, bundle.manifest.target.package) != (
                    self.manifest.mcu, self.manifest.package)):
            raise PraxisError("TARGET_MISMATCH", "Firmware assets do not match the knowledge target/package")
        self.contents = {}
        for asset in self.manifest.files:
            if asset.path in self.contents:
                raise PraxisError("INVALID_ASSETS", "Duplicate firmware asset path")
            data = read_inside(self.root, asset.path, 8 * 1024 * 1024)
            if digest(data) != asset.sha256:
                raise PraxisError("INTEGRITY_ERROR", f"Firmware asset changed: {asset.path}")
            self.contents[asset.path] = data
        required = {"startup_stm32f407xx.s": "startup", "system_stm32f4xx.c": "system",
                    "runtime.c": "runtime", "stm32f407vg_flash.ld": "linker",
                    "include/stm32f407xx.h": "header", "include/stm32f4xx.h": "header"}
        kinds = {asset.path: asset.kind for asset in self.manifest.files}
        if any(kinds.get(path) != kind for path, kind in required.items()):
            raise PraxisError("INVALID_ASSETS", "Required F407 startup/system/linker/header inputs are missing")
        # The reviewed memory contract is enforced in code as well as the linker file.
        self.flash = (0x08000000, 1024 * 1024)
        self.ram = (0x20000000, 128 * 1024)
        self.ccm = (0x10000000, 64 * 1024)
        assembly = self.contents["startup_stm32f407xx.s"].decode("utf-8")
        vector_text = assembly.split("g_pfnVectors:", 1)[-1].split(".size  g_pfnVectors", 1)[0]
        self.vectors = re.findall(r"^\s*\.word\s+(\w+)", vector_text, re.M)
        if len(self.vectors) != 98 or self.vectors[:2] != ["_estack", "Reset_Handler"]:
            raise PraxisError("INVALID_ASSETS", "Pinned F407 vector table is not the reviewed 98-entry layout")
        header = self.contents["include/stm32f407xx.h"].decode("utf-8")
        for name, number in re.findall(r"^\s*(\w+)_IRQn\s*=\s*(-?\d+)", header, re.M):
            handler = {"RNG": "HASH_RNG_IRQHandler"}.get(name, name + "_IRQHandler")
            if int(number) >= 0 and self.vectors[16 + int(number)] != handler:
                raise PraxisError("INVALID_ASSETS", f"Startup vector disagrees with vendor IRQ declaration: {name}")

    @property
    def identity(self):
        return self.manifest.bundle_revision

    def describe(self):
        return {"profile": self.manifest.profile, "mcu": self.manifest.mcu,
                "asset_revision": self.identity, "review": self.manifest.review,
                "memory": {"flash": self.flash, "main_sram": self.ram, "ccm_separate_unused": self.ccm},
                "vector_entries": len(self.vectors), "language": "C11, freestanding, soft-float",
                "clock": "Application must establish its clock basis; reference example selects HSI and updates SystemCoreClock",
                "clock_validation": "ELF checks do not verify arbitrary clock logic. Establish AHB division, call SystemCoreClockUpdate, stop initialization on timeout, and check SysTick_Config's result. Reviewed fixture tests and optional probe diagnostics provide separate evidence.",
                "input_contract": "C/header-only directory; startup, system source, runtime and linker supplied by approved assets",
                "files": [asset.model_dump() for asset in self.manifest.files],
                "limits": "Image structure checks do not establish application behavior or physical operation"}

    def stage(self, destination: Path):
        for name, data in self.contents.items():
            path = destination / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)


def make_manifest(root: Path, files: list[Asset], review: str):
    """Authoring helper; publication must follow actual source review."""
    value = AssetManifest(schema_version=1, bundle_revision="0" * 64, mcu="STM32F407VGT6",
        package="Package_QFP:LQFP-100_14x14mm_P0.5mm", profile="stm32f407vg-c11-flash",
        review=review, files=files).model_dump()
    value["bundle_revision"] = revision(value)
    (root / "manifest.json").write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
