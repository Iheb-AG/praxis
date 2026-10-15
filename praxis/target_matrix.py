"""Offline batch compilation of explicitly registered, isolated target profiles."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Literal

from pydantic import Field, ValidationError, model_validator

from praxis.bundle import Bundle, digest, read_inside, relative_path
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.models import Identifier, Profile, Record


class MatrixEntry(Record):
    id: Identifier
    profile: str = Field(min_length=1, max_length=256)


class TargetMatrix(Record):
    schema_version: Literal[1] = 1
    targets: list[MatrixEntry] = Field(min_length=1, max_length=256)

    @model_validator(mode="after")
    def unique_entries(self):
        if len({row.id for row in self.targets}) != len(self.targets):
            raise ValueError("Target matrix identities must be unique")
        if len({row.profile for row in self.targets}) != len(self.targets):
            raise ValueError("Each profile must be registered once")
        for row in self.targets:
            relative_path(row.profile)
        return self


def load(catalog: Path):
    catalog = catalog.resolve(strict=True)
    root = catalog.parent
    try:
        matrix = TargetMatrix.model_validate_json(read_inside(root, catalog.name, 1024 * 1024))
        profiles = {}
        for row in matrix.targets:
            parts = relative_path(row.profile).parts
            if any((root.joinpath(*parts[:i])).is_symlink() for i in range(1, len(parts) + 1)):
                raise PraxisError("INVALID_PATH", "Matrix profile paths cannot contain symbolic links")
            raw = read_inside(root, row.profile, 8 * 1024 * 1024)
            profile = Profile.model_validate_json(raw)
            if profile.target.id != row.id:
                raise PraxisError("TARGET_MISMATCH", f"Matrix entry {row.id} selects profile target {profile.target.id}")
            profiles[row.id] = (root / row.profile, profile, digest(raw))
    except ValidationError as exc:
        raise PraxisError("INVALID_TARGET_MATRIX", str(exc)) from exc
    return profiles


def compile_matrix(catalog: Path, output: Path, selected: list[str] | None = None) -> dict:
    profiles = load(catalog)
    requested = sorted(profiles if selected is None else selected)
    if not requested or len(requested) != len(set(requested)) or not set(requested) <= profiles.keys():
        raise PraxisError("UNKNOWN_TARGET", f"Choose unique registered targets: {', '.join(sorted(profiles))}")
    if output.is_symlink():
        raise PraxisError("INVALID_PATH", "Target matrix output cannot be a symlink")
    output.mkdir(parents=True, exist_ok=True)
    rows = {}
    for identity in requested:
        path, profile, profile_hash = profiles[identity]
        row = dict(profile_sha256=profile_hash, mcu=profile.target.mcu,
                   cpu=profile.target.knowledge_adapter.cpu if profile.target.knowledge_adapter else "builtin",
                   scope=profile.target.scope, bundle_directory=identity,
                   operating_support="separate reviewed mode/workflow evidence required",
                   physical_qualification=False)
        try:
            bundle = Bundle(compile_bundle(path, output / identity))
            source = next((item for item in bundle.manifest.sources if item.id == "profile"), None)
            if source is None or source.sha256 != profile_hash or bundle.manifest.target != profile.target:
                raise PraxisError("SOURCE_CHANGED", "Target profile changed after matrix validation; choose a stable input snapshot")
            replay = evaluate(bundle)
            from praxis.reports import read_report
            coverage = read_report(bundle, "coverage")
            row.update(status="published" if replay["passed"] else "retrieval_failed",
                       bundle_revision=bundle.manifest.bundle_revision,
                       counts=coverage["counts"],
                       workflows={name: {"ready": value["ready"], "issues": value["issues"]}
                                  for name, value in coverage["workflows"].items()},
                       documents=len(bundle.documents),
                       largest_document_bytes=max(map(len, bundle.documents.values())),
                       retrieval_replay_passed=replay["passed"])
        except PraxisError as exc:
            row.update(status="failed", error_code=exc.code, error=exc.message)
        rows[identity] = row
    report = dict(format="praxis-target-matrix-v1", passed=all(row["status"] == "published" for row in rows.values()),
                  targets=rows, limits="Publication and deterministic retrieval only. No firmware build, "
                  "board connectivity, automatic operating semantics or physical qualification is implied.")
    encoded = (json.dumps(report, sort_keys=True, indent=2) + "\n").encode()
    destination = output / "report.json"
    if destination.exists():
        if read_inside(output, "report.json", 8 * 1024 * 1024) != encoded:
            raise PraxisError("IMMUTABLE_MATRIX_REPORT", "Output has a different matrix report; choose a new output directory")
    else:
        with destination.open("xb") as handle:
            handle.write(encoded)
    return report
