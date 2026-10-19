"""Explicit revision activation over persistent MCP sessions; never touches a target."""
import asyncio
import json
import shutil
import sys
from contextlib import AsyncExitStack
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from threading import Event

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_image, require_tool
from praxis.bundle import Bundle, digest, revision
from praxis.errors import PraxisError
from praxis.handoff import BundleHandoff, encoded, initialize

INITIAL = ROOT / 'bundles/stm32f407g-disc1-e01-m1'
ASSETS = ROOT / 'assets/stm32f407vg'


@pytest.fixture
def project(tmp_path):
    workspace = tmp_path / 'applications'
    workspace.mkdir()
    root = tmp_path / 'control'
    initialize(root, INITIAL, tmp_path / 'publications', ASSETS, workspace,
               tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json')
    return BundleHandoff(root)


def candidate(project, name='next', source=INITIAL):
    destination = Path(project.policy.publication_root) / name
    shutil.copytree(source, destination)
    # Synthetic test revision only: do not fabricate hardware facts or review receipts.
    manifest = json.loads((destination / 'manifest.json').read_bytes())
    index = destination / manifest['documents']['index']
    index.write_text(index.read_text() + '\nTest-only revision marker.\n')
    manifest['file_hashes'][manifest['documents']['index']] = digest(index.read_bytes())
    manifest['bundle_revision'] = revision(manifest)
    (destination / 'manifest.json').write_bytes(encoded(manifest))
    return Bundle(destination)


def test_activation_is_atomic_idempotent_and_keeps_originals(project):
    original = project.selection()
    before = {p.name: digest(p.read_bytes()) for p in INITIAL.glob('*.json')}
    bundle = candidate(project)
    result = project.activate('next', bundle.manifest.bundle_revision)
    assert result['status'] == 'activated' and not result['reconnect_required']
    assert project.selection().generation == 1
    assert project.load_bundle(project.selection()).manifest == bundle.manifest
    assert project.activate('next', bundle.manifest.bundle_revision)['generation'] == 1
    assert before == {p.name: digest(p.read_bytes()) for p in INITIAL.glob('*.json')}
    assert original.bundle_revision != bundle.manifest.bundle_revision
    assert len(list((project.root / 'selections').glob('*.json'))) == 2


@pytest.mark.parametrize('fault', ['target', 'revision', 'hash', 'link', 'symlink', 'lock'])
def test_bad_candidate_keeps_previous_selection(project, fault, tmp_path):
    original = (project.root / 'active.json').read_bytes()
    bundle = candidate(project, source=ROOT / 'bundles/stm32f401re' if fault == 'target' else INITIAL)
    expected = bundle.manifest.bundle_revision
    if fault == 'revision':
        expected = '0' * 64
    elif fault == 'hash':
        (bundle.root / 'wiki/index.md').write_text('corrupt')
    elif fault == 'link':
        manifest = json.loads((bundle.root / 'manifest.json').read_bytes())
        path = bundle.root / 'wiki/index.md'
        path.write_text(path.read_text() + '\n[[missing/path]]\n')
        manifest['file_hashes']['wiki/index.md'] = digest(path.read_bytes())
        manifest['bundle_revision'] = revision(manifest)
        (bundle.root / 'manifest.json').write_bytes(encoded(manifest))
    elif fault == 'symlink':
        shutil.move(bundle.root, tmp_path / 'outside')
        bundle.root.symlink_to(tmp_path / 'outside', target_is_directory=True)
    elif fault == 'lock':
        # Change only the local policy's lock path, never the repository lock.
        policy = project.policy.model_dump()
        path = tmp_path / 'changed-lock.json'
        path.write_bytes(Path(policy['lock']).read_bytes() + b'\n')
        policy['lock'] = str(path)
        (project.root / 'policy.json').write_bytes(encoded(policy))
        project = BundleHandoff(project.root)
        selected = json.loads(original)
        selected['policy_sha256'] = project.policy_hash
        original = encoded(selected)
        (project.root / 'active.json').write_bytes(original)
    with pytest.raises(PraxisError):
        project.activate('next', expected)
    assert (project.root / 'active.json').read_bytes() == original


@pytest.mark.parametrize('name', ['../escape', '/tmp/escape', 'nested/name', 'NEXT'])
def test_activation_names_are_not_paths(project, name):
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        project.activate(name, '0' * 64)


def test_policy_changes_bad_active_and_busy_writer_fail_closed(project):
    bundle = candidate(project)
    with project.writer(), pytest.raises(PraxisError, match='HANDOFF_BUSY'):
        project.activate('next', bundle.manifest.bundle_revision)
    saved = (project.root / 'active.json').read_bytes()
    value = json.loads(saved)
    value['bundle_path'] = str(ROOT / 'bundles/stm32f401re')
    (project.root / 'active.json').write_bytes(encoded(value))
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        project.selection()
    (project.root / 'active.json').write_bytes(saved)
    (project.root / 'policy.json').write_bytes((project.root / 'policy.json').read_bytes() + b'\n')
    with pytest.raises(PraxisError, match='HANDOFF_POLICY_CHANGED'):
        project.selection()


def test_in_flight_build_uses_one_snapshot_then_next_call_adopts(project, monkeypatch):
    from praxis.build_server import create_build_server
    from praxis.firmware_build import BuildService
    started, release = Event(), Event()
    def hold(service, _directory):
        started.set()
        assert release.wait(10), 'Test did not release the in-flight build'
        return {'bundle_revision': service.bundle.manifest.bundle_revision}
    monkeypatch.setattr(BuildService, 'build', hold)
    server = create_build_server(INITIAL, ASSETS, Path(project.policy.workspace),
        Path(project.policy.artifacts), Path(project.policy.lock), handoff=project.root)
    def tool(name):
        return server._tool_manager.get_tool(name).fn
    first = tool('get_build_profile')()['bundle_revision']
    bundle = candidate(project)
    with ThreadPoolExecutor(max_workers=2) as pool:
        running = pool.submit(tool('build_firmware'), 'fixture')
        try:
            assert started.wait(5)
            project.activate('next', bundle.manifest.bundle_revision)
        finally:
            release.set()
        assert running.result(timeout=10)['bundle_revision'] == first
    assert tool('get_build_profile')()['bundle_revision'] == bundle.manifest.bundle_revision


def test_read_only_hardware_scope_rebinds_without_board_claim(tmp_path):
    from praxis.hardware import HardwareService, provision_profile
    from praxis.firmware_assets import FirmwareAssets
    require_tool('openocd')
    profile = tmp_path / 'hardware.json'
    provision_profile(INITIAL, ASSETS, Path(shutil.which('openocd')), profile)
    workspace = tmp_path / 'applications'
    workspace.mkdir()
    initialize(tmp_path / 'control', INITIAL, tmp_path / 'published', ASSETS, workspace,
               tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json', profile)
    control = BundleHandoff(tmp_path / 'control')
    bundle = candidate(control)
    result = control.activate('next', bundle.manifest.bundle_revision)
    control.check_runtime_profile(control.selection())
    hardware = HardwareService(bundle, FirmwareAssets(ASSETS, bundle),
        Path(result['hardware_profile']), tmp_path / 'locks')
    original = json.loads(profile.read_bytes())
    assert hardware.profile.openocd_sha256 == original['openocd_sha256']
    assert hardware.profile.asset_revision == original['asset_revision']
    assert hardware.profile.bundle_revision == bundle.manifest.bundle_revision
    assert hardware.profile.physical_board_revision is None
    assert hardware.connections == {}
    assert 'authorization' not in Path(result['hardware_profile']).read_text()
    assert json.loads(profile.read_bytes()) == original


async def test_publication_handoff_build_report_and_recovery_over_persistent_stdio(project, tmp_path):
    require_tool('clang')
    require_image(ROOT / 'toolchain-f407.lock.json')
    sources = tmp_path / 'sources'
    shutil.copytree(ROOT / 'sources/stm32f407g-disc1', sources, ignore=shutil.ignore_patterns('imports'))
    catalog = tmp_path / 'catalog.json'
    catalog.write_bytes(encoded({'schema_version': 1, 'allowed_hosts': ['example.org'], 'sources': [
        {'id': 'manual', 'target': 'STM32F407VGT6', 'url': 'https://example.org/manual', 'kind': 'text'}]}))
    app = Path(project.policy.workspace) / 'app'
    app.mkdir()
    (app / 'main.c').write_text('#include <stm32f407xx.h>\nint main(void) { for (;;) { __NOP(); } }\n')
    base = ['--bundle', str(INITIAL)]
    selected = ['--handoff', str(project.root)]
    commands = {
        'knowledge': ['serve', *base, *selected],
        'pinned': ['serve', *base],
        'build': ['build-serve', *base, *selected, '--assets', str(ASSETS),
            '--workspace', project.policy.workspace, '--artifacts', project.policy.artifacts,
            '--lock', project.policy.lock, '--project-reports', str(tmp_path / 'reports')],
        'ingest': ['ingest-serve', '--profile', str(sources / 'profile-discovery.json'),
            '--catalog', str(catalog), '--archive-root', str(tmp_path / 'acquired'),
            '--publication-root', project.policy.publication_root, *selected]}

    async def exercise():
        async with AsyncExitStack() as stack:
            clients = {}
            for name, args in commands.items():
                reader, writer = await stack.enter_async_context(stdio_client(StdioServerParameters(
                    command=sys.executable, args=['-m', 'praxis', *args], cwd=str(tmp_path))))
                client = await stack.enter_async_context(ClientSession(reader, writer))
                await client.initialize()
                clients[name] = client

            async def call(server, tool, arguments=None, error=None):
                result = await clients[server].call_tool(tool, arguments or {})
                text = '\n'.join(c.text for c in result.content if c.type == 'text')
                if error:
                    assert result.isError and error in text, text
                    return text
                assert not result.isError, text
                data = result.structuredContent
                if data is None:
                    try:
                        data = json.loads(text)
                    except ValueError:
                        return text
                return data.get('result', data)

            initial = project.selection().bundle_revision
            assert initial in await call('knowledge', 'read_wiki_index')
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'rcc'})
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'gpio'})
            await call('build', 'build_firmware', {'source_directory': 'app'}, 'BUNDLE_HANDOFF_REQUIRED')
            assert (await call('build', 'get_build_profile'))['bundle_revision'] == initial
            old_build = await call('build', 'build_firmware', {'source_directory': 'app'})
            assert old_build['compile_passed'] and old_build['image_validated'], old_build
            assert 'activate_published_bundle' in {t.name for t in (await clients['ingest'].list_tools()).tools}
            publication = await call('ingest', 'publish_reviewed_bundle',
                {'reviewed_profile': 'profile-discovery.json', 'output_name': 'fresh'})
            assert publication['handoff']['status'] == 'activated', publication
            new = publication['bundle_revision']
            assert new != initial
            saved = project.selection()
            staged = await call('ingest', 'publish_reviewed_bundle',
                {'reviewed_profile': 'profile-discovery.json', 'output_name': 'staged', 'activate': False})
            assert 'handoff' not in staged and project.selection() == saved
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'gpio'}, 'missing: index')
            await call('build', 'validate_firmware', {'artifact_id': old_build['artifact_id']}, 'BUNDLE_HANDOFF_REQUIRED')
            assert new in await call('knowledge', 'read_wiki_index')
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'gpio'}, 'rcc')
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'rcc'})
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'gpio'})
            profile = await call('build', 'get_build_profile')
            assert profile['bundle_revision'] == new
            assert not profile['hardware_programming']['enabled']
            await call('build', 'validate_firmware', {'artifact_id': old_build['artifact_id']}, 'INVALID_ARTIFACT')
            built = await call('build', 'build_firmware', {'source_directory': 'app'})
            assert built['compile_passed'] and built['image_validated']
            assert built['bundle_revision'] == new and built['artifact_id'] != old_build['artifact_id']
            await call('build', 'validate_firmware', {'artifact_id': built['artifact_id']})
            spec = {'format': 'praxis-project-v1', 'id': 'handoff_fixture', 'title': 'Handoff fixture',
                'objective': 'Verify persistent-session revision handoff; no physical behavior test.',
                'target_id': profile['target']['id'], 'bundle_revision': new,
                'requirements': [{'id': 'setup', 'description': 'Build after activation',
                    'workflows': ['gpio_led_button'], 'verification_plan': 'Revalidate built ELF.'}],
                'explanations': [{'title': 'Scope', 'explanation': 'No target programming.',
                    'documents': ['peripherals/gpio']}], 'signals': ['LED_A'],
                'limitations': ['Software service fixture only.']}
            report = await call('build', 'generate_project_report',
                {'specification': spec, 'artifact_id': built['artifact_id']})
            assert report['build_status'] == 'artifact_revalidated' and not report['project_accepted']
            # Re-activation is idempotent: successfully served prerequisites remain served.
            await call('ingest', 'activate_published_bundle', {'output_name': 'fresh', 'expected_revision': new})
            await call('knowledge', 'read_peripheral_doc', {'peripheral_name': 'gpio'})
            assert await call('pinned', 'read_wiki_index') == (INITIAL / 'wiki/index.md').read_text()
            # A damaged pointer fails closed; no stale reads/builds are silently served.
            active = (project.root / 'active.json').read_bytes()
            (project.root / 'active.json').write_text('{}')
            await call('knowledge', 'read_wiki_index', error='INVALID_HANDOFF')
            await call('build', 'get_build_profile', error='INVALID_HANDOFF')
            (project.root / 'active.json').write_bytes(active)
            assert new in await call('knowledge', 'read_wiki_index')
            assert (await call('build', 'get_build_profile'))['bundle_revision'] == new
            # Services and their tool lists stayed connected throughout the handoff.
            assert len((await clients['knowledge'].list_tools()).tools) == 3
    await asyncio.wait_for(exercise(), timeout=150)
