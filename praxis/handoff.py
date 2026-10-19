"""Opt-in, project-scoped revision handoff; never changes an immutable bundle.

The operator pins policy.json once. Publication replaces only active.json after
validating the complete candidate. Readers fail closed on bad selections and take
immutable snapshots at tool boundaries. No process control, target I/O or network.
"""
from __future__ import annotations

import json
import os
import re
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from praxis.bundle import Bundle, digest, read_inside
from praxis.errors import PraxisError
from praxis.jsonio import load_json


class Policy(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    format: Literal['praxis-bundle-handoff-v1'] = 'praxis-bundle-handoff-v1'
    initial_bundle: str
    publication_root: str
    target: dict
    assets: str
    workspace: str
    artifacts: str
    lock: str
    lock_sha256: str = Field(pattern='^[0-9a-f]{64}$')
    asset_revision: str = Field(pattern='^[0-9a-f]{64}$')
    hardware_profile: dict | None = None


class Selection(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    policy_sha256: str = Field(pattern='^[0-9a-f]{64}$')
    generation: int = Field(ge=0, strict=True)
    bundle_path: str
    bundle_revision: str = Field(pattern='^[0-9a-f]{64}$')
    hardware_profile: str | None = None


def encoded(value: dict) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode()


def real_path(path: Path) -> Path:
    path = path.absolute()
    if path != path.resolve() or path.is_symlink():
        raise PraxisError('INVALID_PATH', 'Handoff paths must be absolute real paths without symlinks')
    return path


def immutable(path: Path, data: bytes):
    real_path(path)
    if path.exists() or path.is_symlink():
        if read_inside(path.parent, path.name, 1024 * 1024) != data or path.is_symlink():
            raise PraxisError('INTEGRITY_ERROR', f'Handoff record changed: {path.name}')
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open('xb') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        if read_inside(path.parent, path.name, 1024 * 1024) != data:
            raise PraxisError('INTEGRITY_ERROR', 'Concurrent handoff record conflict') from None


class BundleHandoff:
    def __init__(self, root: Path):
        self.root = real_path(root)
        raw = read_inside(self.root, 'policy.json', 1024 * 1024)
        try:
            self.policy = Policy.model_validate_json(raw)
        except ValidationError as exc:
            raise PraxisError('INVALID_HANDOFF', 'Invalid handoff policy; provision it again in a new directory') from exc
        self.policy_hash = digest(raw)
        for key in ('initial_bundle', 'publication_root', 'assets', 'workspace', 'artifacts', 'lock'):
            path = Path(getattr(self.policy, key))
            if not path.is_absolute():
                raise PraxisError('INVALID_HANDOFF', 'Policy paths must be absolute')
            real_path(path)

    def check_launch(self, bundle: Path):
        if real_path(bundle) != Path(self.policy.initial_bundle):
            raise PraxisError('HANDOFF_POLICY_MISMATCH', 'Launch --bundle must match the handoff initial bundle')

    def check_build_launch(self, assets: Path, workspace: Path, artifacts: Path, lock: Path,
                           hardware_profile: Path | None):
        for key, path in dict(assets=assets, workspace=workspace, artifacts=artifacts, lock=lock).items():
            if real_path(path) != Path(getattr(self.policy, key)):
                raise PraxisError('HANDOFF_POLICY_MISMATCH', f'Build {key} differs from handoff policy')
        self.check_build_inputs()
        if bool(hardware_profile) != bool(self.policy.hardware_profile):
            raise PraxisError('HANDOFF_POLICY_MISMATCH', 'Hardware inspection scope differs from handoff policy')
        if hardware_profile:
            raw = load_json(read_inside(hardware_profile.parent.resolve(), hardware_profile.name, 65536))
            if raw != self.policy.hardware_profile:
                raise PraxisError('HANDOFF_POLICY_MISMATCH', 'Launch hardware profile differs from handoff policy')

    def selection(self) -> Selection:
        real_path(self.root / 'policy.json')
        real_path(self.root / 'active.json')
        if digest(read_inside(self.root, 'policy.json', 1024 * 1024)) != self.policy_hash:
            raise PraxisError('HANDOFF_POLICY_CHANGED', 'Pinned handoff policy changed; restore it or restart explicitly')
        try:
            selected = Selection.model_validate_json(read_inside(self.root, 'active.json', 1024 * 1024))
        except ValidationError as exc:
            raise PraxisError('INVALID_HANDOFF', 'Invalid active selection; reactivate a validated publication') from exc
        if selected.policy_sha256 != self.policy_hash:
            raise PraxisError('HANDOFF_POLICY_MISMATCH', 'Active selection belongs to another handoff policy')
        if not Path(selected.bundle_path).is_absolute():
            raise PraxisError('INVALID_PATH', 'Selected bundle path must be absolute')
        path = real_path(Path(selected.bundle_path))
        allowed = path == Path(self.policy.initial_bundle) or path.parent == Path(self.policy.publication_root)
        if not allowed:
            raise PraxisError('INVALID_PATH', 'Selected bundle is outside this project publication root')
        expected_profile = str(self.root / 'profiles' / f'{selected.bundle_revision}.json') if self.policy.hardware_profile else None
        if selected.hardware_profile != expected_profile:
            raise PraxisError('INVALID_HANDOFF', 'Selected hardware profile does not belong to this revision')
        return selected

    def load_bundle(self, selected: Selection) -> Bundle:
        bundle = Bundle(Path(selected.bundle_path))
        if bundle.manifest.target.model_dump() != self.policy.target:
            raise PraxisError('TARGET_MISMATCH', 'Handoff cannot change MCU, package, board identity or target assumptions')
        if bundle.manifest.bundle_revision != selected.bundle_revision:
            raise PraxisError('INTEGRITY_ERROR', 'Selected bundle revision differs from its validated manifest')
        return bundle

    def check_runtime_profile(self, selected: Selection):
        if selected.hardware_profile:
            from praxis.hardware import profile_revision
            value = {**self.policy.hardware_profile, 'bundle_revision': selected.bundle_revision}
            value['profile_revision'] = profile_revision(value)
            path = real_path(Path(selected.hardware_profile))
            if load_json(read_inside(path.parent, path.name, 65536)) != value:
                raise PraxisError('INTEGRITY_ERROR', 'Rebound hardware profile differs from pinned inspection scope')

    def check_build_inputs(self):
        if digest(read_inside(Path(self.policy.lock).parent, Path(self.policy.lock).name, 1024 * 1024)) != self.policy.lock_sha256:
            raise PraxisError('INTEGRITY_ERROR', 'Pinned toolchain lock changed')

    def _candidate(self, path: Path, generation: int):
        from praxis.firmware_build import BuildService
        from praxis.hardware import HardwareService, profile_revision
        self.check_build_inputs()
        service = BuildService(path, Path(self.policy.assets), Path(self.policy.workspace),
                               Path(self.policy.artifacts), Path(self.policy.lock))
        if service.assets.identity != self.policy.asset_revision:
            raise PraxisError('INTEGRITY_ERROR', 'Pinned firmware assets changed')
        selected = Selection(policy_sha256=self.policy_hash, generation=generation,
            bundle_path=str(path), bundle_revision=service.bundle.manifest.bundle_revision)
        self.load_bundle(selected)
        if self.policy.hardware_profile:
            value = {**self.policy.hardware_profile, 'bundle_revision': selected.bundle_revision}
            value['profile_revision'] = profile_revision(value)
            profile = self.root / 'profiles' / f'{selected.bundle_revision}.json'
            immutable(profile, encoded(value))
            HardwareService(service.bundle, service.assets, profile, self.root / 'probe-locks')
            selected = selected.model_copy(update={'hardware_profile': str(profile)})
        return selected

    @contextmanager
    def writer(self):
        # Lock acquisition is bounded and never waits behind a compiler/flash job.
        # A stale lock after a crash requires explicit operator recovery.
        path = self.root / '.activation.lock'
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError as exc:
            raise PraxisError('HANDOFF_BUSY', 'Another activation is in progress; retry after it completes') from exc
        try:
            os.close(descriptor)
            yield
        finally:
            path.unlink()

    def _commit(self, selected: Selection):
        data = encoded(selected.model_dump())
        immutable(self.root / 'selections' / f'{digest(data)}.json', data)
        descriptor, name = tempfile.mkstemp(prefix='.active-', dir=self.root)
        try:
            with os.fdopen(descriptor, 'wb') as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            if (self.root / 'active.json').is_symlink():
                raise PraxisError('INVALID_PATH', 'Active handoff record cannot be a symlink')
            os.replace(name, self.root / 'active.json')
        finally:
            Path(name).unlink(missing_ok=True)

    def activate(self, output_name: str, expected_revision: str) -> dict:
        if re.fullmatch('[a-z][a-z0-9_-]{0,79}', output_name) is None:
            raise PraxisError('INVALID_INPUT', 'Select one canonical publication name, never a path')
        with self.writer():
            previous = self.selection()
            path = real_path(Path(self.policy.publication_root) / output_name)
            selected = self._candidate(path, previous.generation + 1)
            if selected.bundle_revision != expected_revision:
                raise PraxisError('INTEGRITY_ERROR', 'Expected revision does not match published bundle')
            if (selected.bundle_path, selected.bundle_revision) == (previous.bundle_path, previous.bundle_revision):
                selected = previous
            else:
                self._commit(selected)
        return {**selected.model_dump(), 'status': 'activated', 'reconnect_required': False,
                'next_steps': ['read_wiki_index', 'get_build_profile'],
                'limits': 'Services adopt at tool boundaries. Re-read prerequisites; old probe connections and approvals do not transfer.'}


def initialize(output: Path, bundle: Path, publication_root: Path, assets: Path,
               workspace: Path, artifacts: Path, lock: Path, hardware_profile: Path | None = None) -> dict:
    from praxis.firmware_build import BuildService
    from praxis.hardware import HardwareService
    output = real_path(output)
    if output.exists():
        raise PraxisError('OUTPUT_EXISTS', 'Choose a new handoff directory')
    paths = dict(bundle=bundle, publication_root=publication_root, assets=assets,
                 workspace=workspace, artifacts=artifacts, lock=lock)
    paths = {key: real_path(path) for key, path in paths.items()}
    if output.is_relative_to(paths['bundle']) or output.is_relative_to(paths['workspace']):
        raise PraxisError('INVALID_PATH', 'Keep handoff control records outside bundles and application workspace')
    build = BuildService(paths['bundle'], paths['assets'], paths['workspace'], paths['artifacts'], paths['lock'])
    profile = None
    if hardware_profile:
        hardware = HardwareService(build.bundle, build.assets, real_path(hardware_profile), output / 'probe-locks')
        profile = hardware.profile.model_dump()
    policy = Policy(initial_bundle=str(paths['bundle']), publication_root=str(paths['publication_root']),
        target=build.bundle.manifest.target.model_dump(), assets=str(paths['assets']),
        workspace=str(paths['workspace']), artifacts=str(paths['artifacts']), lock=str(paths['lock']),
        lock_sha256=digest(paths['lock'].read_bytes()), asset_revision=build.assets.identity, hardware_profile=profile)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.handoff-', dir=output.parent) as directory:
        stage = Path(directory) / 'control'
        stage.mkdir()
        (stage / 'policy.json').write_bytes(encoded(policy.model_dump()))
        state = BundleHandoff(stage)
        selected = state._candidate(paths['bundle'], 0)
        # Rebind only the location, never backend identity, grants or board facts.
        if selected.hardware_profile:
            selected = selected.model_copy(update={'hardware_profile': str(output / 'profiles' / Path(selected.hardware_profile).name)})
        state._commit(selected)
        if output.exists() or output.is_symlink():
            raise PraxisError('OUTPUT_EXISTS', 'Handoff destination appeared during initialization')
        os.rename(stage, output)
    return {'handoff': str(output), 'bundle_revision': selected.bundle_revision,
            'instructions': 'Launch knowledge, build and ingestion with the same --handoff directory. No flash authorization is granted.'}
