"""Detect broken provisioning without launching configured commands or hardware."""
import json
from pathlib import Path
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.project_check import check_project
from praxis.project_workspace import create_project


@pytest.fixture
def project(tmp_path):
    require_tool('clang')
    root = tmp_path / 'project'
    create_project(root, 'check_example', ROOT / 'sources/stm32f407g-disc1/profile.json',
                   ROOT / 'assets/stm32f407vg', ROOT / 'toolchain-f407.lock.json',
                   mode='fresh', install_codex=True)
    return root


def test_valid_check_does_not_execute_commands_or_change_files(project, monkeypatch):
    before = {str(p): p.read_bytes() for p in project.rglob('*') if p.is_file()}
    monkeypatch.setattr(subprocess, 'Popen', lambda *a, **k: pytest.fail('Must not execute any command'))
    report = check_project(project)
    assert report['configuration_valid']
    assert report['live_services'] == report['sandbox_execution'] == 'not_checked'
    assert report['physical_validation'] == 'not_assessed'
    assert before == {str(p): p.read_bytes() for p in project.rglob('*') if p.is_file()}


@pytest.mark.parametrize('fault', ['missing_bundle', 'corrupt_bundle', 'wrong_project',
    'disabled_service', 'malformed_launch', 'malformed_selection', 'missing_assets', 'environment'])
def test_broken_setup_fails_with_actionable_diagnostic(project, fault):
    state = project / '.praxis'
    config = project / '.codex/config.toml'
    if fault == 'missing_bundle':
        (state / 'bundles/initial-r001/wiki/index.md').unlink()
    elif fault == 'corrupt_bundle':
        (state / 'bundles/initial-r001/wiki/index.md').write_text('incorrect content')
    elif fault == 'wrong_project':
        config.write_text(config.read_text().replace(str(state / 'workspace'), '/tmp/another-project/workspace'))
    elif fault == 'disabled_service':
        config.write_text(config.read_text().replace('enabled = true', 'enabled = false', 1))
    elif fault == 'malformed_launch':
        (state / 'mcp-servers.json').write_text('[]')
    elif fault == 'malformed_selection':
        (state / 'handoff/active.json').write_text('{}')
    elif fault == 'missing_assets':
        policy = state / 'handoff/policy.json'
        value = json.loads(policy.read_text())
        value['assets'] = str(project / 'missing-assets')
        policy.write_text(json.dumps(value))
    else:
        config.write_text(config.read_text().replace('[mcp_servers.praxis]',
            '[mcp_servers.praxis]\nenv = { PYTHONPATH = "/tmp/untrusted" }'))
    report = check_project(project)
    assert not report['configuration_valid']
    failures = [x for x in report['checks'] if x['status'] == 'failed']
    assert failures and all(x['code'] and x['detail'] for x in failures)


def test_cli_missing_project_has_json_failure_and_nonzero_exit(tmp_path, capsys):
    from praxis.cli import main
    assert main(['project-check', '--root', str(tmp_path)]) == 1
    assert not json.loads(capsys.readouterr().out)['configuration_valid']


def test_missing_client_config_is_not_claimed_connected(project):
    (project / '.codex/config.toml').unlink()
    report = check_project(project)
    assert report['configuration_valid']
    assert any(c['status'] == 'not_configured' for c in report['checks'])


def test_missing_inspection_launch_profile_is_detected(tmp_path):
    import shutil
    from praxis.hardware import provision_profile
    from praxis.compiler import compile_bundle
    require_tool('clang')
    require_tool('openocd')
    bundle = compile_bundle(ROOT / 'sources/stm32f407g-disc1/profile.json', tmp_path / 'seed')
    inspection = tmp_path / 'inspection.json'
    provision_profile(bundle, ROOT / 'assets/stm32f407vg',
                      Path(shutil.which('openocd')), inspection)
    root = tmp_path / 'project'
    create_project(root, 'inspection_check', ROOT / 'sources/stm32f407g-disc1/profile.json',
                   ROOT / 'assets/stm32f407vg', ROOT / 'toolchain-f407.lock.json',
                   mode='reuse', candidates=[bundle], hardware_profile=inspection)
    assert check_project(root)['configuration_valid']
    (root / '.praxis/hardware-initial.json').unlink()
    report = check_project(root)
    assert not report['configuration_valid']
    assert any(c['name'] == 'build_launch_binding' and c['status'] == 'failed' for c in report['checks'])


def test_symlink_project_is_rejected(project, tmp_path):
    link = tmp_path / 'linked'
    link.symlink_to(project, target_is_directory=True)
    assert not check_project(link)['configuration_valid']


def test_missing_build_dependency_is_an_explicit_failure(project, monkeypatch):
    import praxis.firmware_build

    def missing(*args, **kwargs):
        raise ModuleNotFoundError('Missing test dependency: pyelftools')

    monkeypatch.setattr(praxis.firmware_build, 'BuildService', missing)
    report = check_project(project)
    assert not report['configuration_valid']
    assert any(c.get('code') == 'MISSING_DEPENDENCY' for c in report['checks'])


def test_changed_selection_during_check_is_rejected(project, monkeypatch):
    from praxis.handoff import BundleHandoff
    original = BundleHandoff.selection
    calls = 0

    def changed(self):
        nonlocal calls
        calls += 1
        value = original(self)
        return value if calls == 1 else value.model_copy(update={'generation': value.generation + 1})

    monkeypatch.setattr(BundleHandoff, 'selection', changed)
    report = check_project(project)
    assert not report['configuration_valid']
    assert report['checks'][-1]['code'] == 'SELECTION_CHANGED'


def test_podman_runtime_failure_is_not_reported_as_missing_image(tmp_path, monkeypatch):
    from conftest import require_image
    import conftest
    lock = tmp_path / 'lock.json'
    lock.write_text('{"image":"sha256:example"}')
    monkeypatch.setattr(conftest, 'require_tool', lambda _: None)
    monkeypatch.setattr(subprocess, 'run', lambda *a, **k:
        subprocess.CompletedProcess(a, 125, b'', b'permission denied: runtime directory'))
    with pytest.raises(pytest.fail.Exception, match='Podman runtime unavailable.*permission denied'):
        require_image(lock)
