"""Project provisioning checks with opt-in canonical MCP diagnostic launches.

A static pass describes on-disk configuration. Live mode tests fresh sessions,
never existing client sessions, electrical correctness or permission to program.
"""
import asyncio
from pathlib import Path
import tomllib

from pydantic import ValidationError

from praxis.bundle import read_inside
from praxis.errors import PraxisError
from praxis.handoff import BundleHandoff, real_path
from praxis.jsonio import load_json
from praxis.models import Profile
from praxis.project_workspace import _client_entries


def check_project(root: Path, *, live: bool = False, timeout: float = 30) -> dict:
    if not 0 < timeout <= 120:
        raise PraxisError('INVALID_INPUT', 'Diagnostic timeout must be greater than 0 and at most 120 seconds per service')
    report = {'format': 'praxis-project-check-v1', 'configuration_valid': False,
              'checks': [], 'live_services': 'not_checked', 'sandbox_execution': 'not_checked',
              'physical_validation': 'not_assessed', 'programming_authorization': 'not_assessed'}

    def check(name, operation):
        try:
            value = operation()
        except (PraxisError, OSError, ValueError, ValidationError, ImportError) as exc:
            report['checks'].append({'name': name, 'status': 'failed',
                'code': (exc.code if isinstance(exc, PraxisError) else
                         'MISSING_DEPENDENCY' if isinstance(exc, ImportError) else 'INPUT_ERROR'),
                'detail': str(exc)})
            return None
        report['checks'].append({'name': name, 'status': 'passed'})
        return value

    def require(condition, code, message):
        if not condition:
            raise PraxisError(code, message)

    root = check('project_path', lambda: real_path(root))
    if root is None:
        return report
    state = root / '.praxis'

    def load_manifest():
        real_path(state)
        value = load_json(read_inside(state, 'project.json', 1024 * 1024))
        require(isinstance(value, dict) and value.get('format') == 'praxis-project-workspace-v1',
                'INVALID_PROJECT', 'Select a root created with praxis project-init')
        return value

    manifest = check('project_manifest', load_manifest)
    control = check('handoff_policy', lambda: BundleHandoff(state / 'handoff'))
    if manifest is None or control is None:
        return report

    def isolation():
        for key, expected in {'publication_root': state / 'bundles', 'workspace': state / 'workspace',
                              'artifacts': state / 'artifacts'}.items():
            require(Path(getattr(control.policy, key)) == expected, 'PROJECT_PATH_MISMATCH',
                    f'{key} must belong to this project: {expected}')
            require(expected.is_dir(), 'MISSING_FILE', f'Missing project directory: {expected}')
        require(control.policy.target == manifest.get('target'), 'TARGET_MISMATCH',
                'Project and handoff targets differ')
        for name in ('references', 'reports'):
            directory = real_path(state / name)
            require(directory.is_dir(), 'MISSING_FILE', f'Missing project directory: {directory}')
        require(manifest.get('initial_bundle') == 'bundles/initial-r001'
                and Path(control.policy.initial_bundle) == state / 'bundles/initial-r001',
                'PROJECT_PATH_MISMATCH', 'Initial bundle must belong to this project')
        return True

    check('project_isolation', isolation)
    selection = check('active_selection', control.selection)
    if selection is None:
        return report
    bundle = check('bundle_integrity', lambda: control.load_bundle(selection))
    check('inspection_binding', lambda: control.check_runtime_profile(selection))
    check('pinned_toolchain', control.check_build_inputs)
    check('build_launch_binding', lambda: control.check_build_launch(
        Path(control.policy.assets), Path(control.policy.workspace), Path(control.policy.artifacts),
        Path(control.policy.lock), state / 'hardware-initial.json' if control.policy.hardware_profile else None))
    if bundle is not None:
        report.update(target=bundle.manifest.target.id, bundle_revision=selection.bundle_revision,
                      generation=selection.generation, bundle_path=selection.bundle_path)

        def assets():
            from praxis.firmware_build import BuildService
            service = BuildService(Path(selection.bundle_path), Path(control.policy.assets),
                Path(control.policy.workspace), Path(control.policy.artifacts), Path(control.policy.lock))
            require(service.assets.identity == control.policy.asset_revision, 'INTEGRITY_ERROR',
                    'Firmware assets differ from pinned handoff policy')
            return True
        check('build_inputs', assets)

    def expected_entries():
        profile = Profile.model_validate_json(read_inside(state, 'authoring/profile.json', 8 * 1024 * 1024))
        require(profile.target.model_dump() == control.policy.target, 'TARGET_MISMATCH',
                'Authoring profile and handoff target differ')
        if manifest.get('catalog') is not None:
            from praxis.web_import import Catalog
            require(manifest['catalog'] == 'authoring/catalog.json', 'INVALID_PROJECT',
                    'Project catalog must be authoring/catalog.json')
            catalog = Catalog.model_validate_json(read_inside(state, 'authoring/catalog.json', 1024 * 1024))
            require(all(s.target == profile.target.mcu for s in catalog.sources), 'TARGET_MISMATCH',
                    'Source catalog targets another MCU')
        return _client_entries(root, Path(control.policy.initial_bundle), Path(control.policy.assets),
            Path(control.policy.lock), manifest.get('catalog') is not None,
            sorted(set(profile.web_imports.values())), control.policy.hardware_profile is not None)

    expected = check('authoring_identity', expected_entries)
    if expected is not None:
        def compare(entries):
            require(isinstance(entries, dict), 'INVALID_CONFIG', 'Expected MCP server entries')
            for name, wanted in expected.items():
                actual = entries.get(name)
                require(isinstance(actual, dict), 'MISSING_SERVICE', f'Missing project service: {name}')
                # Timeout customization is harmless. Command/environment changes need an
                # explicit review; do not run arbitrary launchers as part of diagnostics.
                wanted = {k: v for k, v in wanted.items() if not k.endswith('_timeout_sec')}
                actual = {k: v for k, v in actual.items() if not k.endswith('_timeout_sec')}
                require(actual == wanted, 'SERVICE_CONFIG_MISMATCH',
                        f'{name}: configuration differs from this project; compare .praxis/codex-mcp.toml')
            return True

        def generated():
            value = load_json(read_inside(state, 'mcp-servers.json', 1024 * 1024))
            require(isinstance(value, dict), 'INVALID_CONFIG', 'Expected a launch-settings object')
            return compare(value.get('mcpServers'))
        check('generated_launch_settings', generated)
        config = root / '.codex/config.toml'
        if config.exists() or config.is_symlink():
            check('local_codex_settings', lambda: compare(tomllib.loads(
                read_inside(root, '.codex/config.toml', 1024 * 1024).decode('utf-8')).get('mcp_servers')))
        else:
            report['checks'].append({'name': 'local_codex_settings', 'status': 'not_configured',
                'detail': 'Install the generated fragment in your client; effective client configuration is not checked.'})
    # Do not report a coherent check if another author activated a revision during it.
    check('selection_stability', lambda: require(control.selection() == selection,
        'SELECTION_CHANGED', 'Bundle changed during checks; rerun project-check'))
    report['configuration_valid'] = all(item['status'] != 'failed' for item in report['checks'])
    report['limits'] = ('On-disk checks only. Client trust/global overrides, MCP connectivity, dependency '
                        'availability, sandbox execution and hardware behavior require separate checks.')
    if live:
        report['live_services'] = 'blocked_by_configuration'
        if report['configuration_valid']:
            from praxis.project_live import inspect_services
            # Launch captured canonical entries, never reread/execute a config that
            # may have changed after validation. No operator write grant is copied.
            report['services'] = asyncio.run(inspect_services(expected, bundle, selection,
                Path(control.policy.workspace), timeout))
            live_ok = all(row['status'] != 'failed' for row in report['services'])
            stable = check('post_live_selection_stability', lambda: require(
                control.selection() == selection, 'SELECTION_CHANGED',
                'Active selection changed during service checks; rerun project-check') or True)
            report['live_services'] = 'passed' if live_ok and stable else 'failed'
            report['limits'] = ('Fresh diagnostic MCP sessions only; existing client connections and '
                'client trust/global overrides are not inspected. No builds, downloads, publication '
                'or hardware operations were requested. Hardware and sandbox execution remain untested.')
    return report
