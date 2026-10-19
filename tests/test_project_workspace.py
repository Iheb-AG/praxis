"""Project isolation and exact bundle reuse, with real stdio and target compilation."""
import asyncio
import json
import shutil
import tomllib
from contextlib import AsyncExitStack
from pathlib import Path

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_image, require_tool
from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.handoff import BundleHandoff
from praxis.project_workspace import create_project, snapshot_inputs
from test_bundle_handoff import candidate

PROFILE = ROOT / 'sources/stm32f407g-disc1/profile.json'
ASSETS = ROOT / 'assets/stm32f407vg'
LOCK = ROOT / 'toolchain-f407.lock.json'
CATALOG = ROOT / 'sources/stm32f407g-disc1/web-sources.json'


@pytest.fixture(scope='module')
def seed(tmp_path_factory):
    from praxis.compiler import compile_bundle
    require_tool('clang')
    root = tmp_path_factory.mktemp('workspace-seed')
    return compile_bundle(PROFILE, root / 'bundle')


def make(root, **kwargs):
    return create_project(root, 'example_project', kwargs.pop('profile', PROFILE), ASSETS,
        LOCK, **kwargs)


def test_fresh_compiles_sources_and_installs_only_local_config(tmp_path, monkeypatch):
    from praxis import project_workspace
    require_tool('clang')
    monkeypatch.setattr(project_workspace, 'check_reuse', lambda *_: pytest.fail('Fresh must not reuse a bundle'))
    result = make(tmp_path / 'project with spaces', mode='fresh', install_codex=True, catalog=CATALOG)
    root = Path(result['project'])
    state = root / '.praxis'
    assert result['decision'] == 'compiled_from_source'
    assert result['codex_config_installed']
    profile = state / 'authoring/profile.json'
    assert profile.read_bytes() == PROFILE.read_bytes()
    assert not (state / 'authoring/profile-discovery.json').exists()
    record = json.loads((state / 'project.json').read_text())
    assert record['firmware_artifact_id'] is None and not record['project_accepted']
    assert record['physical_validation'] == 'not_assessed'
    assert record['requested_mode'] == 'fresh' and record['reuse_checks'] == []
    config = tomllib.loads((root / '.codex/config.toml').read_text())
    assert set(config) == {'mcp_servers'}
    assert set(config['mcp_servers']) == {'praxis', 'praxis_build', 'praxis_ingest', 'praxis_references'}
    for entry in config['mcp_servers'].values():
        assert entry['cwd'] == str(root)
        assert '--hardware-authorization' not in entry['args']
        # Only installed Python, immutable assets and toolchain lock are external.
        for index, arg in enumerate(entry['args'][:-1]):
            if arg.startswith('--') and arg not in {'--assets', '--lock'}:
                assert Path(entry['args'][index + 1]).is_relative_to(root), entry
    manifest = json.loads((state / 'source-snapshot.json').read_text())
    for path, expected in manifest['files'].items():
        assert digest((state / 'authoring' / path).read_bytes()) == expected


def test_exact_reuse_does_not_run_compiler_or_share_state(seed, tmp_path, monkeypatch):
    import praxis.compiler
    monkeypatch.setattr(praxis.compiler, 'compile_bundle', lambda *_: pytest.fail('Exact reuse should not compile'))
    original = Bundle(seed)
    a = make(tmp_path / 'a', mode='reuse', candidates=[seed])
    b = make(tmp_path / 'b', mode='reuse', candidates=[seed])
    assert a['decision'] == b['decision'] == 'reused_exact_bundle'
    ca = BundleHandoff(tmp_path / 'a/.praxis/handoff')
    cb = BundleHandoff(tmp_path / 'b/.praxis/handoff')
    assert ca.selection().bundle_revision == cb.selection().bundle_revision == original.manifest.bundle_revision
    assert ca.selection().bundle_path != cb.selection().bundle_path != str(seed)
    changed = candidate(ca, source=Path(ca.selection().bundle_path))
    ca.activate('next', changed.manifest.bundle_revision)
    assert ca.selection().generation == 1 and cb.selection().generation == 0
    assert Bundle(seed).manifest == original.manifest
    # No inherited ingestion service when the project did not select a catalog.
    entries = json.loads((tmp_path / 'a/.praxis/mcp-servers.json').read_text())['mcpServers']
    assert entries['praxis_ingest'] == {'enabled': False}


@pytest.mark.parametrize('fault', ['target', 'source', 'profile', 'workflow'])
def test_forced_reuse_rejects_incompatible_inputs(seed, tmp_path, fault):
    profile = PROFILE
    bundle = seed
    workflows = []
    if fault == 'target':
        bundle = ROOT / 'bundles/stm32f401re'
    elif fault in {'source', 'profile'}:
        source_root = tmp_path / 'sources'
        snapshot_inputs(PROFILE, source_root)
        profile = source_root / 'profile.json'
        data = json.loads(profile.read_text())
        if fault == 'source':
            path = source_root / next(s['path'] for s in data['sources'] if s['path'].endswith('.md'))
            path.write_text(path.read_text() + '\nTest-only editorial whitespace.\n')
        else:
            data['review']['reviewer'] += ' Test-only edited profile.'
            profile.write_text(json.dumps(data))
    else:
        workflows = ['unreviewed_usb_application']
    destination = tmp_path / 'project'
    with pytest.raises(PraxisError, match='NO_COMPATIBLE_BUNDLE'):
        make(destination, mode='reuse', candidates=[bundle], profile=profile, workflows=workflows)
    assert not (destination / '.praxis').exists()
    assert not (destination / '.codex/config.toml').exists()


def test_auto_rebuilds_after_rejected_explicit_candidate(tmp_path):
    require_tool('clang')
    result = make(tmp_path / 'project', candidates=[ROOT / 'bundles/stm32f401re'])
    assert result['decision'] == 'compiled_from_source'
    manifest = json.loads(Path(result['manifest']).read_text())
    assert not manifest['reuse_checks'][0]['compatible']
    assert 'TARGET_MISMATCH' in manifest['reuse_checks'][0]['error']


@pytest.mark.parametrize('mode,candidates', [('fresh', [ROOT / 'bundles/stm32f401re']), ('reuse', [])])
def test_mode_cannot_silently_ignore_or_invent_a_bundle(tmp_path, mode, candidates):
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        make(tmp_path / 'project', mode=mode, candidates=candidates)


def test_existing_state_and_client_config_are_never_overwritten(seed, tmp_path):
    root = tmp_path / 'project'
    root.mkdir()
    config = root / '.codex/config.toml'
    config.parent.mkdir()
    config.write_text('model = "preserve-user-choice"\n')
    before = config.read_bytes()
    with pytest.raises(PraxisError, match='CONFIG_EXISTS'):
        make(root, mode='reuse', candidates=[seed], install_codex=True)
    assert config.read_bytes() == before and not (root / '.praxis').exists()
    make(root, mode='reuse', candidates=[seed])
    with pytest.raises(PraxisError, match='PROJECT_EXISTS'):
        make(root, mode='reuse', candidates=[seed])
    assert config.read_bytes() == before


def test_source_symlinks_fail_before_copying_outside_bytes(tmp_path):
    source = tmp_path / 'input'
    source.mkdir()
    data = json.loads(PROFILE.read_text())
    selected = data['sources'][0]['path']
    (source / selected).parent.mkdir(parents=True, exist_ok=True)
    outside = tmp_path / 'external'
    outside.write_text('must not enter snapshot')
    (source / selected).symlink_to(outside)
    for name in data['header']['include_directories']:
        (source / name).mkdir(parents=True, exist_ok=True)
    (source / 'profile.json').write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        snapshot_inputs(source / 'profile.json', tmp_path / 'snapshot')


def test_source_snapshot_cannot_strip_unreviewed_archive_markers(tmp_path):
    from praxis.web_import import FORMAT
    source = tmp_path / 'input'
    snapshot_inputs(PROFILE, source)
    data = json.loads((source / 'profile.json').read_text())
    spec = next(s for s in data['sources'] if s['path'].endswith('.md'))
    spec['path'] = 'unreviewed/extracted/part.md'
    spec.pop('expected_sha256', None)
    part = source / spec['path']
    part.parent.mkdir(parents=True)
    part.write_text('Unreviewed source text, not approved operating knowledge.')
    (source / 'unreviewed/import.json').write_text(json.dumps({'format': FORMAT}))
    (source / 'profile.json').write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='UNDECLARED_WEB_IMPORT'):
        snapshot_inputs(source / 'profile.json', tmp_path / 'snapshot')


def test_inspection_seed_is_copied_to_stable_project_state(seed, tmp_path):
    from praxis.hardware import provision_profile
    require_tool('openocd')
    original = tmp_path / 'disposable/hardware.json'
    original.parent.mkdir()
    provision_profile(seed, ASSETS, Path(shutil.which('openocd')), original)
    root = tmp_path / 'project'
    make(root, mode='reuse', candidates=[seed], hardware_profile=original, install_codex=True)
    profile = root / '.praxis/hardware-initial.json'
    assert profile.read_bytes() == original.read_bytes()
    original.unlink()
    config = tomllib.loads((root / '.codex/config.toml').read_text())['mcp_servers']['praxis_build']
    assert config['args'][config['args'].index('--hardware-profile') + 1] == str(profile)
    assert not any('authorization' in path.name for path in (root / '.praxis').rglob('*'))
    control = BundleHandoff(root / '.praxis/handoff')
    control.check_runtime_profile(control.selection())
    control.check_build_launch(ASSETS, root / '.praxis/workspace', root / '.praxis/artifacts', LOCK, profile)


async def test_project_launches_keep_reference_handoff_and_build_states_separate(seed, tmp_path):
    require_image(LOCK)
    roots = [tmp_path / name for name in ('one', 'two')]
    for root in roots:
        make(root, mode='reuse', candidates=[seed], catalog=CATALOG, install_codex=True)

    async def exercise():
        async with AsyncExitStack() as stack:
            clients = {}
            for index, root in enumerate(roots):
                config = tomllib.loads((root / '.codex/config.toml').read_text())['mcp_servers']
                for name in ('praxis', 'praxis_build', 'praxis_ingest', 'praxis_references'):
                    entry = config[name]
                    reader, writer = await stack.enter_async_context(stdio_client(StdioServerParameters(
                        command=entry['command'], args=entry['args'], cwd=str(tmp_path))))
                    client = await stack.enter_async_context(ClientSession(reader, writer))
                    await client.initialize()
                    clients[index, name] = client

            async def call(index, service, tool, arguments=None):
                result = await clients[index, service].call_tool(tool, arguments or {})
                assert not result.isError, result
                data = result.structuredContent
                if data is None:
                    text = '\n'.join(c.text for c in result.content if c.type == 'text')
                    try:
                        data = json.loads(text)
                    except ValueError:
                        return text
                return data.get('result', data)

            initial = Bundle(seed).manifest.bundle_revision
            for index, root in enumerate(roots):
                assert initial in await call(index, 'praxis', 'read_wiki_index')
                build = await call(index, 'praxis_build', 'get_build_profile')
                assert Path(build['application_workspace']).is_relative_to(root)
                ingestion = await call(index, 'praxis_ingest', 'get_ingestion_profile')
                assert ingestion['target']['id'] == build['target']['id']
                assert (await call(index, 'praxis_references', 'list_hardware_references'))['references'] == []
            control = BundleHandoff(roots[0] / '.praxis/handoff')
            changed = candidate(control, source=Path(control.selection().bundle_path))
            await call(0, 'praxis_ingest', 'activate_published_bundle',
                {'output_name': 'next', 'expected_revision': changed.manifest.bundle_revision})
            assert changed.manifest.bundle_revision in await call(0, 'praxis', 'read_wiki_index')
            assert initial in await call(1, 'praxis', 'read_wiki_index')
            build = await call(0, 'praxis_build', 'get_build_profile')
            assert build['bundle_revision'] == changed.manifest.bundle_revision
            workspace = Path(build['application_workspace'])
            (workspace / 'src').mkdir()
            (workspace / 'src/main.c').write_text('#include <stm32f407xx.h>\nint main(void){for(;;){__NOP();}}\n')
            built = await call(0, 'praxis_build', 'build_firmware', {'source_directory': 'src'})
            assert built['compile_passed'] and built['image_validated'], built
            assert not list((roots[1] / '.praxis/artifacts').iterdir())
            assert (await call(1, 'praxis_build', 'get_build_profile'))['bundle_revision'] == initial
    await asyncio.wait_for(exercise(), timeout=100)
