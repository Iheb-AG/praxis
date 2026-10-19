"""Project-owned source snapshots, explicit bundle reuse and local MCP launch settings.

Nothing here searches other conversations, changes global client settings, infers
hardware compatibility from a name, grants hardware writes or edits old bundles.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

from pydantic import ValidationError

from praxis.bundle import Bundle, digest, read_inside, relative_path
from praxis.errors import PraxisError
from praxis.handoff import encoded, initialize, real_path
from praxis.models import Profile

MAX_INPUT_BYTES = 1024 * 1024 * 1024


def snapshot_inputs(profile_path: Path, destination: Path) -> dict:
    """Copy only registered inputs, include trees and declared evidence archives.

    Reuse their bytes/provenance, not their containing project's unrelated profiles,
    bundles, grants or source code. Includes/archives retain their relative paths.
    """
    profile_path = real_path(profile_path)
    root = profile_path.parent
    raw = read_inside(root, profile_path.name, 8 * 1024 * 1024)
    try:
        profile = Profile.model_validate_json(raw)
    except ValidationError as exc:
        raise PraxisError('INVALID_PROFILE', str(exc)) from exc
    # Validate archive markers at the original location before copying. Removing
    # those markers during staging must never turn unreviewed evidence into facts.
    from praxis.compiler import _web_sources
    from praxis.models import Source
    paths, sources = {}, []
    for source in profile.sources:
        path = real_path(root / relative_path(source.path))
        if not path.is_file():
            raise PraxisError('INVALID_SOURCE', f'Expected a regular registered input: {source.path}')
        if path.stat().st_size > MAX_INPUT_BYTES:
            raise PraxisError('PROJECT_INPUT_LIMIT', 'A registered input exceeds the project snapshot budget')
        data = read_inside(root, source.path)
        paths[source.id] = root / source.path
        sources.append(Source(**source.model_dump(exclude={'expected_sha256'}), sha256=digest(data)))
    _web_sources(profile, paths, sources, root)
    selected = {source.path for source in profile.sources}
    for name in [*profile.header.include_directories, *profile.web_imports.values()]:
        if name == '.':
            # Root-level headers must be explicit registered inputs. Do not copy
            # an entire arbitrary project just because -I. was selected.
            continue
        directory = root / relative_path(name)
        real_path(directory)
        if not directory.is_dir():
            raise PraxisError('MISSING_FILE', f'Required input directory missing: {name}')
        for path in sorted(directory.rglob('*')):
            real_path(path)
            if not path.is_dir():
                selected.add(path.relative_to(root).as_posix())
    hashes, size = {}, 0
    for name in sorted(selected):
        path = root / relative_path(name)
        real_path(path)
        if not path.is_file():
            raise PraxisError('INVALID_SOURCE', f'Expected a regular registered input: {name}')
        size += path.stat().st_size
        if size > MAX_INPUT_BYTES or len(selected) > 10000:
            raise PraxisError('PROJECT_INPUT_LIMIT', 'Use an explicit input snapshot under 1 GiB and 10,000 files')
        data = read_inside(root, name)
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        hashes[name] = digest(data)
    if 'profile.json' in hashes:
        raise PraxisError('INVALID_PROFILE', 'profile.json is reserved for the project profile, not a source identity')
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'profile.json').write_bytes(raw)
    for source in profile.sources:
        if source.expected_sha256 is not None and hashes[source.path] != source.expected_sha256:
            raise PraxisError('SOURCE_HASH_MISMATCH', f'Pinned input changed: {source.id}')
    return {'profile_sha256': digest(raw), 'files': hashes, 'bytes': size,
            'limits': 'A reviewed-source snapshot is reuse of source evidence, not fresh online acquisition.'}


def check_reuse(bundle: Bundle, profile_path: Path, workflows: list[str]) -> dict:
    """Conservative exact-bundle reuse; a changed board/profile must be rebuilt."""
    from praxis.compiler import _web_sources
    from praxis.models import Source
    from praxis.support import assess
    profile = Profile.model_validate_json(profile_path.read_bytes())
    if bundle.manifest.target.model_dump() != profile.target.model_dump():
        raise PraxisError('TARGET_MISMATCH', 'Reuse requires the exact MCU, package, board identity and target assumptions')
    root = profile_path.parent
    paths, sources = {}, []
    for spec in profile.sources:
        data = read_inside(root, spec.path)
        paths[spec.id] = root / spec.path
        sources.append(Source(**spec.model_dump(exclude={'expected_sha256'}), sha256=digest(data)))
    _web_sources(profile, paths, sources, root)
    expected = {source.id: source.sha256 for source in sources}
    expected['profile'] = digest(profile_path.read_bytes())
    actual = {source.id: source.sha256 for source in bundle.manifest.sources}
    if expected != actual:
        raise PraxisError('SOURCE_MISMATCH', 'Bundle inputs differ from this project profile; rebuild from reviewed inputs')
    readiness = {}
    for name in workflows:
        selected = assess(bundle, workflow=name)['selected_workflow']
        readiness[name] = selected
        if not selected['knowledge_ready']:
            raise PraxisError('WORKFLOW_NOT_READY', f'Reuse cannot satisfy requested workflow: {name}')
    return {'compatible': True, 'checked_workflows': readiness,
            'physical_validation': 'not_assessed',
            'limits': 'Only listed workflows were requested; matching hardware is not whole-MCU or physical acceptance.'}


def _client_entries(root: Path, initial: Path, assets: Path, lock: Path, catalog: bool,
                    archives: list[str], inspection: bool) -> dict:
    state = root / '.praxis'
    python = str(Path(sys.executable).absolute())
    common = ['--bundle', str(initial), '--handoff', str(state / 'handoff')]
    commands = {
        'praxis': ['serve', *common],
        'praxis_build': ['build-serve', *common, '--assets', str(assets),
            '--workspace', str(state / 'workspace'), '--artifacts', str(state / 'artifacts'),
            '--lock', str(lock), '--project-reports', str(state / 'reports')],
        'praxis_references': ['reference-serve', '--archive-root', str(state / 'references')]}
    if inspection:
        commands['praxis_build'] += ['--hardware-profile', str(state / 'hardware-initial.json')]
    if catalog:
        commands['praxis_ingest'] = ['ingest-serve', '--profile', str(state / 'authoring/profile.json'),
            '--catalog', str(state / 'authoring/catalog.json'), '--archive-root', str(state / 'authoring/imports/acquired'),
            '--publication-root', str(state / 'bundles'), '--handoff', str(state / 'handoff')]
        for archive in archives:
            commands['praxis_ingest'] += ['--evidence-archive', str(state / 'authoring' / archive)]
    entries = {name: {'command': python, 'args': ['-m', 'praxis', *args],
        'cwd': str(root), 'enabled': True, 'startup_timeout_sec': 90,
        'tool_timeout_sec': 180} for name, args in commands.items()}
    if not catalog:
        # Disable an inherited global ingestion entry rather than silently leaking it.
        entries['praxis_ingest'] = {'enabled': False}
    return entries


def client_toml(entries: dict) -> str:
    lines = ['# Generated project-local Praxis settings; global settings are unchanged.',
             '# Load only in a trusted project. Do not commit machine-specific paths.', '']
    for name, fields in sorted(entries.items()):
        lines.append(f'[mcp_servers.{name}]')
        for key, value in fields.items():
            lines.append(f'{key} = {json.dumps(value, ensure_ascii=False)}')
        lines.append('')
    return '\n'.join(lines)


def create_project(root: Path, project_id: str, profile: Path, assets: Path, lock: Path,
                   mode: str = 'auto', candidates: list[Path] = (), catalog: Path | None = None,
                   workflows: list[str] = (), hardware_profile: Path | None = None,
                   install_codex: bool = False) -> dict:
    """Initialize one independent full-build project from explicitly selected evidence."""
    if not re.fullmatch('[a-z][a-z0-9_]{0,63}', project_id):
        raise PraxisError('INVALID_INPUT', 'Use a project ID with lowercase letters, digits and underscores')
    if mode not in {'auto', 'reuse', 'fresh'} or (mode == 'fresh' and candidates):
        raise PraxisError('INVALID_INPUT', 'Use auto/reuse/fresh; fresh does not accept precompiled bundle candidates')
    if mode == 'reuse' and not candidates:
        raise PraxisError('INVALID_INPUT', 'Reuse requires an explicitly selected bundle candidate')
    root, profile, assets, lock = map(real_path, (root, profile, assets, lock))
    state = root / '.praxis'
    config = root / '.codex/config.toml'
    if state.exists() or state.is_symlink():
        raise PraxisError('PROJECT_EXISTS', 'This project already has .praxis state; use another project directory')
    if install_codex and (config.exists() or config.is_symlink()):
        raise PraxisError('CONFIG_EXISTS', 'Project Codex configuration exists; generate a fragment and merge only its MCP entries explicitly')
    if root.is_relative_to(profile.parent):
        raise PraxisError('INVALID_PATH', 'Project root must stay outside the source authoring tree')
    root.mkdir(parents=True, exist_ok=True)
    chosen = None
    attempts = []
    with tempfile.TemporaryDirectory(prefix='.praxis-init-', dir=root) as temporary:
        stage = Path(temporary) / 'state'
        stage.mkdir()
        (stage / '.gitignore').write_text('*\n')
        snapshot = snapshot_inputs(profile, stage / 'authoring')
        local_profile = stage / 'authoring/profile.json'
        parsed = Profile.model_validate_json(local_profile.read_bytes())
        if catalog:
            from praxis.web_import import Catalog
            raw = read_inside(catalog.parent.resolve(), catalog.name, 1024 * 1024)
            selected_catalog = Catalog.model_validate_json(raw)
            if any(source.target != parsed.target.mcu for source in selected_catalog.sources):
                raise PraxisError('TARGET_MISMATCH', 'Source catalog must select this project MCU')
            if (stage / 'authoring/catalog.json').exists():
                raise PraxisError('INVALID_PROFILE', 'catalog.json is reserved for the project acquisition catalog')
            (stage / 'authoring/catalog.json').write_bytes(raw)
        for path in candidates:
            try:
                candidate = Bundle(real_path(path))
                checked = check_reuse(candidate, local_profile, list(workflows))
                chosen = candidate
                attempts.append({'path': str(candidate.root), 'revision': candidate.manifest.bundle_revision, **checked})
                break
            except PraxisError as exc:
                attempts.append({'path': str(path), 'compatible': False, 'error': str(exc)})
        if mode == 'reuse' and chosen is None:
            raise PraxisError('NO_COMPATIBLE_BUNDLE', json.dumps(attempts, sort_keys=True))
        initial_name = 'initial-r001'
        initial_stage = stage / 'bundles' / initial_name
        if chosen:
            # Copy verified bytes; never share another project's mutable selection.
            initial_stage.mkdir(parents=True)
            for name in ['manifest.json', *sorted(chosen.manifest.file_hashes)]:
                real_path(chosen.root / name)
                destination = initial_stage / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(read_inside(chosen.root, name))
            decision = 'reused_exact_bundle'
        else:
            from praxis.compiler import compile_bundle
            compile_bundle(local_profile, initial_stage)
            decision = 'compiled_from_source'
        initial_bundle = Bundle(initial_stage)
        # Record readiness without claiming that initialization implements the whole project.
        from praxis.support import assess
        has_coverage = 'coverage' in initial_bundle.manifest.documents
        support = assess(initial_bundle) if has_coverage else {'workflows': {}}
        for name in workflows:
            selected_workflow = assess(initial_bundle, workflow=name)['selected_workflow']
            if not selected_workflow['knowledge_ready']:
                raise PraxisError('WORKFLOW_NOT_READY', f'Initial project bundle lacks operating support for {name}')
        if hardware_profile:
            from praxis.firmware_assets import FirmwareAssets
            from praxis.hardware import HardwareService, profile_revision
            # The profile's backend/assets are validated against the candidate below;
            # rebind only the bundle hash, never physical observations or write grants.
            value = json.loads(read_inside(hardware_profile.parent.resolve(), hardware_profile.name, 65536))
            from praxis.hardware import HardwareProfile
            old = HardwareProfile.model_validate(value)
            if profile_revision(value) != old.profile_revision:
                raise PraxisError('INTEGRITY_ERROR', 'Inspection seed profile hash mismatch')
            value['bundle_revision'] = initial_bundle.manifest.bundle_revision
            value['profile_revision'] = profile_revision(value)
            (stage / 'hardware-initial.json').write_bytes(encoded(value))
            HardwareService(initial_bundle, FirmwareAssets(assets, initial_bundle),
                stage / 'hardware-initial.json', stage / 'probe-locks')
        for directory in ('workspace', 'artifacts', 'reports', 'references'):
            (stage / directory).mkdir()
        from praxis.firmware_build import BuildService
        BuildService(initial_stage, assets, stage / 'workspace', stage / 'artifacts', lock)
        (stage / 'source-snapshot.json').write_bytes(encoded(snapshot))
        if state.exists() or state.is_symlink():
            raise PraxisError('PROJECT_EXISTS', 'Project state appeared during initialization')
        os.rename(stage, state)
    try:
        initial = state / 'bundles' / initial_name
        initialize(state / 'handoff', initial, state / 'bundles', assets, state / 'workspace',
            state / 'artifacts', lock, state / 'hardware-initial.json' if hardware_profile else None)
        archives = sorted(set(parsed.web_imports.values()))
        entries = _client_entries(root, initial, assets, lock, catalog is not None, archives, hardware_profile is not None)
        (state / 'mcp-servers.json').write_bytes(encoded({'mcpServers': entries}))
        (state / 'codex-mcp.toml').write_text(client_toml(entries))
        manifest = {'format': 'praxis-project-workspace-v1', 'id': project_id,
            'requested_mode': mode, 'decision': decision, 'target': parsed.target.model_dump(),
            'initial_bundle': 'bundles/' + initial_name, 'initial_bundle_revision': initial_bundle.manifest.bundle_revision,
            'profile': 'authoring/profile.json', 'catalog': 'authoring/catalog.json' if catalog else None,
            'handoff': 'handoff', 'source_snapshot': 'source-snapshot.json', 'reuse_checks': attempts,
            'initial_workflow_readiness': {key: value['knowledge_ready'] for key, value in support['workflows'].items()},
            'workflow_coverage': 'available' if has_coverage else 'unavailable_legacy_bundle',
            'checked_workflows': list(workflows), 'firmware_artifact_id': None,
            'physical_validation': 'not_assessed', 'project_accepted': False,
            'limits': 'Source reuse is explicit. Similar MCUs do not establish board connectivity or full project support.'}
        (state / 'project.json').write_bytes(encoded(manifest))
        if install_codex:
            real_path(config)
            config.parent.mkdir(parents=True, exist_ok=True)
            with config.open('x', encoding='utf-8') as handle:
                handle.write(client_toml(entries))
            ignored_config = config.parent / '.gitignore'
            if not ignored_config.exists() and not ignored_config.is_symlink():
                with ignored_config.open('x', encoding='utf-8') as handle:
                    handle.write('/config.toml\n')
    except BaseException:
        # Only our newly created, never-connected state is removed on setup failure.
        shutil.rmtree(state)
        raise
    return {'project': str(root), 'manifest': str(state / 'project.json'),
            'decision': decision, 'bundle_revision': initial_bundle.manifest.bundle_revision,
            'codex_config_installed': install_codex,
            'next_steps': ['Trust/open this project in the client and reconnect once',
                'Confirm knowledge/build and ingestion paths lie within this project',
                'Implement missing workflows; project initialization is not firmware completion']}
