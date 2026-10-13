"""Optional full-link service. Generated inputs are compiled only in rootless Podman."""

from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
import time
import uuid
from pathlib import Path

from praxis.bundle import Bundle, digest, read_inside, relative_path
from praxis.elf_validation import validate_bytes
from praxis.errors import PraxisError
from praxis.firmware_assets import FirmwareAssets
from praxis.verify import MAX_DIAGNOSTICS, _image, _rootless, bounded, command, snapshot

FLAGS = ['-mcpu=cortex-m4', '-mthumb', '-mfloat-abi=soft', '-DSTM32F407xx',
         '-DHSE_VALUE=8000000U', '-DHSI_VALUE=16000000U', '-DUSER_VECT_TAB_ADDRESS',
         '-std=c11', '-ffreestanding', '-fno-common', '-Wall', '-Wextra', '-Werror',
         '-fmax-errors=20', '-O2', '-g', '-ffunction-sections', '-fdata-sections',
         '-I/approved/include', '-I/src', '-fdebug-prefix-map=/src=source',
         '-fdebug-prefix-map=/approved=approved']
ARTIFACT_FILES = ('firmware.elf', 'firmware.bin', 'firmware.hex', 'firmware.map', 'report.json')


def build_commands(units: list[str]) -> list[tuple[str, list[str]]]:
    commands, objects = [], []
    inputs = [f'/src/{name}' for name in units] + [
        '/approved/system_stm32f4xx.c', '/approved/runtime.c', '/approved/startup_stm32f407xx.s']
    for index, name in enumerate(inputs):
        obj = f'/out/unit-{index:03d}.o'
        commands.append(('arm-none-eabi-gcc', [*FLAGS, '-c', name, '-o', obj]))
        objects.append(obj)
    commands.append(('arm-none-eabi-gcc', [*FLAGS, '-nostdlib',
        '-Wl,--gc-sections,--build-id=none', '-Wl,-Map=/out/firmware.map',
        '-T/approved/stm32f407vg_flash.ld', *objects, '-lgcc', '-o', '/out/firmware.elf']))
    for fmt, suffix in [('binary', 'bin'), ('ihex', 'hex')]:
        commands.append(('arm-none-eabi-objcopy', ['-O', fmt, '/out/firmware.elf', f'/out/firmware.{suffix}']))
    return commands


class BuildService:
    def __init__(self, bundle: Path, assets: Path, workspace: Path, artifacts: Path, lock: Path):
        self.bundle = Bundle(bundle)
        self.assets = FirmwareAssets(assets, self.bundle)
        if workspace.is_symlink() or not workspace.is_dir():
            raise PraxisError('INVALID_WORKSPACE', 'Select an existing real source workspace')
        self.workspace = workspace.resolve()
        if artifacts.is_symlink():
            raise PraxisError('INVALID_PATH', 'Artifact root must not be a symlink')
        self.artifacts = artifacts.resolve()
        if self.workspace == self.artifacts or self.artifacts.is_relative_to(self.workspace):
            raise PraxisError('INVALID_PATH', 'Keep the artifact store outside the source workspace')
        self.lock_path = lock.resolve()
        try:
            self.lock = json.loads(lock.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            raise PraxisError('INVALID_LOCK', 'Cannot read toolchain lock') from exc
        if (self.lock.get('schema_version') != 1 or self.lock.get('asset_revision') != self.assets.identity
                or self.lock.get('profile') != self.assets.manifest.profile):
            raise PraxisError('INVALID_LOCK', 'Toolchain lock must pin this exact firmware asset revision/profile')
        if self.lock.get('image') is not None:
            _image(self.lock['image'])

    def profile(self) -> dict:
        return {**self.assets.describe(), 'target': self.bundle.manifest.target.model_dump(),
                'bundle_revision': self.bundle.manifest.bundle_revision,
                'image': self.lock.get('image'), 'provisioned': bool(self.lock.get('image')),
                'application_workspace': str(self.workspace),
                'compiler': self.lock.get('compiler_versions'),
                'instructions': 'Read the knowledge MCP first. Supply application C/H files only; include <stm32f407xx.h>. Call build_firmware and inspect both compile_passed and image_validated. Physical behavior is untested.'}

    def source_path(self, name: str) -> Path:
        path = self.workspace / relative_path(name)
        try:
            resolved = path.resolve(strict=True)
        except OSError as exc:
            raise PraxisError('INVALID_SOURCE', 'Source directory does not exist inside the configured workspace') from exc
        if not resolved.is_relative_to(self.workspace) or any(
                p.is_symlink() for p in [path, *path.parents] if p.is_relative_to(self.workspace)):
            raise PraxisError('INVALID_PATH', 'Source path escapes the configured workspace or uses a symlink')
        return path

    def build(self, source_directory: str) -> dict:
        source_path = self.source_path(source_directory)
        image = _image(self.lock.get('image'))
        _rootless()
        report = {'compile_passed': False, 'image_validated': False, 'artifact_id': None,
                  'bundle_revision': self.bundle.manifest.bundle_revision,
                  'asset_revision': self.assets.identity, 'image': image,
                  'compiler_versions': self.lock.get('compiler_versions'),
                  'physical_behavior': 'not tested', 'commands': [], 'diagnostics': ''}
        with tempfile.TemporaryDirectory(prefix='praxis-build-') as directory:
            root = Path(directory)
            source, approved, out = root / 'source', root / 'approved', root / 'out'
            for path in (source, approved, out):
                path.mkdir()
            units, fingerprint = snapshot(source_path, source)
            approved_names = {Path(name).name for name in self.assets.contents if name.endswith('.h')}
            if any(path.name in approved_names for path in source.rglob('*.h')):
                raise PraxisError('HEADER_SHADOW', 'Application headers must not shadow pinned CMSIS headers')
            self.assets.stage(approved)
            report['source_sha256'] = fingerprint
            deadline = time.monotonic() + 30
            for compiler, flags in build_commands(units):
                name = 'praxis-build-' + uuid.uuid4().hex
                # Reuse the exact resource, filesystem, capability and network policy of verify.
                container = command(image, 'stm32', source, approved, out, units[0], 'object', 16000000, name,
                                    mcu='STM32F407VGT6')
                position = container.index('--entrypoint')
                container = container[:position] + ['--env', 'SOURCE_DATE_EPOCH=0', '--entrypoint',
                            '/usr/bin/' + compiler, image, *flags]
                container[container.index('fsize=65536:65536')] = 'fsize=8388608:8388608'
                try:
                    result = bounded(container, max(0.1, deadline - time.monotonic()))
                finally:
                    bounded(['podman', 'rm', '--force', '--ignore', name], 5)
                report['commands'].append({'executable': compiler, 'arguments': flags,
                                            'returncode': result['returncode'], 'failure': result['failure']})
                remaining = MAX_DIAGNOSTICS - len(report['diagnostics'].encode())
                report['diagnostics'] += result['diagnostics'].encode()[:remaining].decode(errors='replace')
                if result['returncode'] or result['failure'] or time.monotonic() >= deadline:
                    report['failure'] = result['failure'] or ('TIMEOUT' if time.monotonic() >= deadline else 'COMPILER_ERROR')
                    return report
                if sum(p.stat().st_size for p in out.iterdir()) > 16 * 1024 * 1024:
                    report['failure'] = 'ARTIFACT_LIMIT'
                    return report
            report['compile_passed'] = True
            elf = read_inside(out, 'firmware.elf', 8 * 1024 * 1024)
            report['validation'] = validate_bytes(elf, self.assets)
            report['image_validated'] = report['validation']['valid']
            if not report['image_validated']:
                return report
            # Record identities, never a mutable caller-selected output filename.
            payload_hashes = {name: digest(read_inside(out, name, 8 * 1024 * 1024))
                              for name in ARTIFACT_FILES if name != 'report.json'}
            artifact_id = digest(json.dumps({'source': fingerprint, 'bundle': report['bundle_revision'],
                'assets': self.assets.identity, 'image': image, 'files': payload_hashes, 'flags': FLAGS,
                'build_report': {k: v for k, v in report.items() if k != 'artifact_id'}},
                sort_keys=True, separators=(',', ':')).encode())
            report['artifact_id'] = artifact_id
            (out / 'report.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
            hashes = {name: digest(read_inside(out, name, 8 * 1024 * 1024)) for name in ARTIFACT_FILES}
            manifest = {'schema_version': 1, 'artifact_id': artifact_id, 'files': hashes,
                        'bundle_revision': report['bundle_revision'], 'asset_revision': self.assets.identity}
            self.artifacts.mkdir(parents=True, exist_ok=True)
            dest = self.artifacts / artifact_id
            if dest.exists():
                self.validate(artifact_id)
            else:
                staging = Path(tempfile.mkdtemp(prefix='.staging-', dir=self.artifacts))
                try:
                    for name in ARTIFACT_FILES:
                        shutil.copyfile(out / name, staging / name)
                    (staging / 'manifest.json').write_text(json.dumps(manifest, indent=2, sort_keys=True) + '\n')
                    os.rename(staging, dest)
                finally:
                    if staging.exists():
                        shutil.rmtree(staging)
            return report

    def validate(self, artifact_id: str) -> dict:
        if not re.fullmatch('[0-9a-f]{64}', artifact_id):
            raise PraxisError('INVALID_ARTIFACT', 'Use the 64-character artifact ID returned by build_firmware')
        root = self.artifacts / artifact_id
        if root.is_symlink():
            raise PraxisError('INVALID_ARTIFACT', 'Artifact directory cannot be a symlink')
        try:
            manifest = json.loads(read_inside(root, 'manifest.json', 65536))
            if (manifest['schema_version'] != 1 or manifest['artifact_id'] != artifact_id
                    or manifest['asset_revision'] != self.assets.identity
                    or manifest['bundle_revision'] != self.bundle.manifest.bundle_revision
                    or set(manifest['files']) != set(ARTIFACT_FILES)):
                raise ValueError('Artifact identity/profile mismatch')
            for name, expected in manifest['files'].items():
                if digest(read_inside(root, name, 8 * 1024 * 1024)) != expected:
                    raise PraxisError('INTEGRITY_ERROR', f'Artifact changed: {name}')
            report = json.loads(read_inside(root, 'report.json', 1024 * 1024))
            elf = read_inside(root, 'firmware.elf', 8 * 1024 * 1024)
            identity = digest(json.dumps({'source': report['source_sha256'], 'bundle': manifest['bundle_revision'],
                'assets': self.assets.identity, 'image': report['image'],
                'files': {name: manifest['files'][name] for name in ARTIFACT_FILES if name != 'report.json'},
                'flags': FLAGS, 'build_report': {k: v for k, v in report.items() if k != 'artifact_id'}},
                sort_keys=True, separators=(',', ':')).encode())
            if identity != artifact_id:
                raise PraxisError('INTEGRITY_ERROR', 'Artifact content no longer matches its immutable ID')
            return {'artifact_id': artifact_id, 'validation': validate_bytes(elf, self.assets),
                    'physical_behavior': 'not tested'}
        except (ValueError, KeyError, TypeError) as exc:
            raise PraxisError('INVALID_ARTIFACT', str(exc)) from exc
