"""Programming tests use trusted ELF fixtures, fake probes and real Tcl WITHOUT adapter init.

These tests never connect to or program an attached board.
"""
import asyncio
import json
import os
import struct
import subprocess
import sys
from pathlib import Path

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_tool
from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.firmware_build import FLAGS
from praxis.hardware import IDENTITY, HardwareService, parse_observation, provision_profile
from praxis.programming import (CONTROLS, ProgrammingService, authorize_plan, canonical_hash,
    checked_plan, image_from_elf, mutation_configuration, mutation_script, save_plan)
from test_firmware_build import good_elf as good_elf, service
from test_hardware_inspection import PROBE, values


@pytest.fixture
def programming(tmp_path, monkeypatch, good_elf):
    build = service(tmp_path)
    image = image_from_elf(good_elf, build.assets)
    payloads = {'firmware.elf': good_elf, 'firmware.bin': image.data,
                'firmware.hex': b'TEST FIXTURE', 'firmware.map': b'TEST FIXTURE'}
    report = {'source_sha256': 'a' * 64, 'image': 'sha256:' + 'b' * 64,
              'compile_passed': True, 'image_validated': True, 'artifact_id': None}
    hashes = {name: digest(data) for name, data in payloads.items()}
    artifact = digest(json.dumps({'source': report['source_sha256'],
        'bundle': build.bundle.manifest.bundle_revision, 'assets': build.assets.identity,
        'image': report['image'], 'files': hashes, 'flags': FLAGS,
        'build_report': {k: v for k, v in report.items() if k != 'artifact_id'}},
        sort_keys=True, separators=(',', ':')).encode())
    report['artifact_id'] = artifact
    payloads['report.json'] = json.dumps(report).encode()
    root = build.artifacts / artifact
    root.mkdir(parents=True)
    for name, data in payloads.items():
        (root / name).write_bytes(data)
    (root / 'manifest.json').write_text(json.dumps({'schema_version': 1,
        'artifact_id': artifact, 'bundle_revision': build.bundle.manifest.bundle_revision,
        'asset_revision': build.assets.identity,
        'files': {name: digest(data) for name, data in payloads.items()}}))
    observation = tmp_path / 'observation.json'
    observation.write_text(json.dumps(values(True)))
    backend = tmp_path / 'fixture-openocd'
    backend.write_text('#!' + sys.executable + '\n'
        'import sys,json,pathlib,re\n'
        'if "--version" in sys.argv:\n'
        ' print("Open On-Chip Debugger 0.12.0 (TEST FIXTURE ONLY)");sys.exit(0)\n'
        f'p=pathlib.Path({str(observation)!r});data=json.loads(p.read_text())\n'
        'script=pathlib.Path(sys.argv[-1]).read_text()\n'
        'uid="".join("%08x"%data["uid%d"%i] for i in range(3))\n'
        'expected=re.search(r\'if {\\$praxis_uid ne "([0-9a-f]+)"}\',script)\n'
        'if expected and expected[1]!=uid:\n'
        ' print("PRAXIS_TARGET_CHANGED");sys.exit(1)\n'
        'mutating="PRAXIS_OPERATION_COMPLETE" in script\n'
        'if mutating:\n'
        ' if "flash write_image" in script:\n'
        '  data["state"]="halted"\n'
        '  raw=pathlib.Path("image.bin").read_bytes()\n'
        '  if data.get("corrupt_readback"):raw=bytes([raw[0]^1])+raw[1:]\n'
        '  pathlib.Path("readback.bin").write_bytes(raw)\n'
        ' else:\n'
        '  print("PRAXIS_IMAGE_VERIFIED")\n'
        '  data["state"]="halted" if "wait_halt" in script else "running"\n'
        ' data.update(pc=0x08000401,sp=0x2001ff00,lr=0xfffffffd,xpsr=0x1000000)\n'
        ' p.write_text(json.dumps(data));print("PRAXIS_OPERATION_COMPLETE")\n'
        'for k,v in data.items():\n'
        ' if ("|"+k+"|") in script or ("get_reg" in script and k in ("pc","sp","lr","xpsr") and data["state"]=="halted"):\n'
        '  print("PRAXIS|"+k+"|"+(v if k=="state" else "0x%08x"%v))\n')
    backend.chmod(0o700)
    profile = tmp_path / 'hardware.json'
    provision_profile(build.bundle.root, build.assets.root, backend, profile)
    monkeypatch.setattr('praxis.hardware.discover_probes', lambda: [dict(PROBE)])
    hardware = HardwareService(build.bundle, build.assets, profile, tmp_path / 'locks')
    connection = hardware.inspect_target('TEST123')['connection_id']
    runner = ProgrammingService(build, hardware)
    plan = runner.plan_firmware(artifact, connection)
    plan_path = tmp_path / 'plan.json'
    save_plan(plan, plan_path)
    grant_path = tmp_path / 'authorization.json'
    authorize_plan(plan_path, grant_path, tmp_path / 'audit', 'Test operator',
                   'TEST FIXTURE board; no physical device', ['flash', *sorted(CONTROLS)])
    return ProgrammingService(build, hardware, grant_path), artifact, connection, observation


def test_image_bytes_and_whole_sector_plan(programming):
    s, artifact, connection, _ = programming
    plan = s.plan_firmware(artifact, connection)
    assert plan['image_start'] == 0x08000000
    assert plan['erase_length'] == 16384 and plan['last_sector'] == 0
    assert plan['image_length'] < plan['erase_length']
    assert s.build.validate(artifact)['validation']['valid']
    assert checked_plan(plan).plan_revision == s.authorization.plan.plan_revision
    assert s.describe()['enabled'] and 'flash' in s.describe()['actions']


def test_bundle_handoff_invalidates_connections_and_programming_scope(programming, tmp_path):
    from mcp.server.fastmcp.exceptions import ToolError
    from praxis.build_server import create_build_server
    from praxis.handoff import BundleHandoff, initialize
    from test_bundle_handoff import candidate
    original, artifact, _connection, _ = programming
    build = original.build
    control_root = tmp_path / 'handoff'
    profile = tmp_path / 'hardware.json'
    initialize(control_root, build.bundle.root, tmp_path / 'publications', build.assets.root,
        build.workspace, build.artifacts, build.lock_path, profile)
    control = BundleHandoff(control_root)
    server = create_build_server(build.bundle.root, build.assets.root, build.workspace,
        build.artifacts, build.lock_path, profile, original.authorization_path,
        handoff=control_root)
    def tool(name):
        return server._tool_manager.get_tool(name).fn
    assert tool('get_build_profile')()['hardware_programming']['enabled']
    connection = tool('inspect_target')('TEST123')['connection_id']
    bundle = candidate(control, source=build.bundle.root)
    control.activate('next', bundle.manifest.bundle_revision)
    updated = tool('get_build_profile')()
    assert updated['bundle_revision'] == bundle.manifest.bundle_revision
    assert not updated['hardware_programming']['enabled']
    assert updated['hardware_inspection']['enabled']
    with pytest.raises(ToolError, match='UNKNOWN_CONNECTION'):
        tool('inspect_execution')(connection)
    with pytest.raises(ToolError, match='AUTHORIZATION_REQUIRED'):
        tool('flash_firmware')(artifact, connection)
    with pytest.raises(ToolError, match='AUTHORIZATION_REQUIRED'):
        tool('control_execution')(artifact, connection, 'reset_run')


def test_authorization_absent_never_launches_mutating_backend(programming, monkeypatch):
    s, artifact, connection, _ = programming
    s = ProgrammingService(s.build, s.hardware)
    monkeypatch.setattr(s, 'run_backend', lambda *_: pytest.fail('Unauthorized backend launch'))
    with pytest.raises(PraxisError, match='AUTHORIZATION_REQUIRED'):
        s.flash_firmware(artifact, connection)


def test_successful_flash_readback_and_persistent_single_attempt(programming):
    s, artifact, connection, _ = programming
    r = s.flash_firmware(artifact, connection)
    assert r['success'] and r['readback_verified'] and r['execution_state'] == 'halted'
    assert r['erased_range']['length'] == 16384
    assert r['physical_behavior'] == 'not tested'
    restarted = ProgrammingService(s.build, s.hardware, s.authorization_path)
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        restarted.flash_firmware(artifact, connection)


def test_readback_corruption_fails_and_consumes_attempt(programming):
    s, artifact, connection, observation = programming
    observation.write_text(json.dumps(values(True, corrupt_readback=True)))
    r = s.flash_firmware(artifact, connection)
    assert not r['success'] and not r['readback_verified'] and r['failure'] == 'READBACK_MISMATCH'
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        s.flash_firmware(artifact, connection)


def test_work_area_fallback_warning_with_exact_readback_is_not_failure(programming, monkeypatch):
    s, artifact, connection, _ = programming
    from praxis.verify import bounded as real_bounded

    def warnings(*args, **kwargs):
        result = real_bounded(*args, **kwargs)
        return {**result, 'diagnostics': 'Error: No working memory available.\n'
                'Warn: falling back to single memory accesses\n' + result['diagnostics']}

    monkeypatch.setattr('praxis.programming.bounded', warnings)
    result = s.flash_firmware(artifact, connection)
    assert result['success'] and result['readback_verified']
    assert '-work-area-size 0' in mutation_configuration('TEST123', 0x374B, True)


def test_error_after_program_and_dump_remains_unverified_and_consumed(programming, monkeypatch):
    """Reproduce the first physical attempt's late error without writing a physical board."""
    s, artifact, connection, _ = programming
    image = s.snapshot_image(artifact)

    def late_error(*args, **kwargs):
        (kwargs['cwd'] / 'readback.bin').write_bytes(image.data)
        return {'failure': None, 'returncode': 1, 'diagnostics':
                "PRAXIS_OPERATION_COMPLETE\nPRAXIS|state|halted\nError: unknown register 'xpsr'\n"}

    monkeypatch.setattr('praxis.programming.bounded', late_error)
    result = s.flash_firmware(artifact, connection)
    assert not result['success'] and not result['readback_verified']
    assert result['failure'] == 'BACKEND_OPERATION_FAILED'
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        s.flash_firmware(artifact, connection)


@pytest.mark.parametrize('failure,returncode', [('TIMEOUT', -9), ('OUTPUT_LIMIT', -9), (None, 1)])
def test_backend_failure_no_automatic_retry(programming, monkeypatch, failure, returncode):
    s, artifact, connection, _ = programming
    calls = []
    def fail(*args, **kwargs):
        calls.append(args)
        return {'failure': failure, 'returncode': returncode, 'diagnostics': 'TEST disconnect/timeout'}
    monkeypatch.setattr('praxis.programming.bounded', fail)
    r = s.flash_firmware(artifact, connection)
    assert not r['success'] and r['execution_state'] == 'unknown'
    assert len(calls) == 1
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        s.flash_firmware(artifact, connection)
    assert len(calls) == 1


def test_target_changed_before_programming_invalidates_connection(programming):
    s, artifact, connection, observation = programming
    observation.write_text(json.dumps(values(True, uid0=99)))
    r = s.flash_firmware(artifact, connection)
    assert not r['success'] and r['failure'] == 'TARGET_CHANGED'
    assert connection not in s.hardware.connections


@pytest.mark.parametrize('case,code', [('expired', 'AUTHORIZATION_EXPIRED'),
    ('changed', 'INVALID_AUTHORIZATION'), ('artifact', 'AUTHORIZATION_MISMATCH'),
    ('probe', 'AUTHORIZATION_MISMATCH'), ('corrupt', 'INTEGRITY_ERROR')])
def test_invalid_scope_or_artifact_never_launches(programming, monkeypatch, case, code):
    s, artifact, connection, _ = programming
    monkeypatch.setattr(s, 'run_backend', lambda *_: pytest.fail('Invalid-scope backend launch'))
    if case == 'expired':
        monkeypatch.setattr('praxis.programming.time.time', lambda: s.authorization.expires_at + 1)
    elif case == 'changed':
        s.authorization_path.write_text('{}')
    elif case == 'artifact':
        monkeypatch.setattr(s, 'make_plan', lambda *args:
                            s.authorization.plan.model_copy(update={'artifact_id': 'f' * 64}))
    elif case == 'probe':
        s.hardware.connections[connection] = ('DIFFERENT', '000000010000000200000003')
    else:
        (s.build.artifacts / artifact / 'firmware.elf').write_bytes(b'corrupt')
    with pytest.raises(PraxisError, match=code):
        s.flash_firmware(artifact, connection)


def test_disconnected_probe_does_not_consume_or_launch(programming, monkeypatch):
    s, artifact, connection, _ = programming
    monkeypatch.setattr('praxis.hardware.discover_probes', lambda: [])
    with pytest.raises(PraxisError, match='PROBE_NOT_FOUND'):
        s.flash_firmware(artifact, connection)
    assert not Path(s.authorization.audit_root).exists()


def test_control_budget_survives_service_restart(programming):
    s, artifact, connection, _ = programming
    for _ in range(s.authorization.max_control_attempts):
        assert s.control_execution(artifact, connection, 'halt', 0)['success']
    s = ProgrammingService(s.build, s.hardware, s.authorization_path)
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        s.control_execution(artifact, connection, 'halt', 0)


def test_operation_not_in_scope_never_launches(programming, tmp_path, monkeypatch):
    s, artifact, connection, _ = programming
    grant = tmp_path / 'flash-only.json'
    authorize_plan(tmp_path / 'plan.json', grant, tmp_path / 'audit-two', 'Test operator',
                   'TEST FIXTURE', ['flash'], max_controls=0)
    s = ProgrammingService(s.build, s.hardware, grant)
    monkeypatch.setattr(s, 'run_backend', lambda *_: pytest.fail('Disallowed operation launched'))
    with pytest.raises(PraxisError, match='OPERATION_NOT_AUTHORIZED'):
        s.control_execution(artifact, connection, 'reset_run', 0)


def test_control_only_scope_never_authorizes_flash(programming, tmp_path, monkeypatch):
    s, artifact, connection, _ = programming
    grant = tmp_path / 'control-only.json'
    authorize_plan(tmp_path / 'plan.json', grant, tmp_path / 'control-audit', 'Test operator',
                   'TEST FIXTURE verified image; execution only', ['reset_run', 'halt', 'resume'])
    runner = ProgrammingService(s.build, s.hardware, grant)
    assert runner.describe()['max_flash_attempts'] == 0
    assert runner.control_execution(artifact, connection, 'reset_run', 0)['success']
    monkeypatch.setattr(runner, 'run_backend', lambda *_: pytest.fail('Unauthorized flash launch'))
    with pytest.raises(PraxisError, match='OPERATION_NOT_AUTHORIZED'):
        runner.flash_firmware(artifact, connection)


@pytest.mark.parametrize('actions,max_controls', [([], 6), (['halt', 'halt'], 6), (['halt'], 0)])
def test_unusable_control_scope_rejected(programming, tmp_path, actions, max_controls):
    with pytest.raises(PraxisError, match='INVALID_AUTHORIZATION'):
        authorize_plan(tmp_path / 'plan.json', tmp_path / 'bad-grant.json', tmp_path / 'audit-new',
                       'Test operator', 'TEST FIXTURE', actions, max_controls=max_controls)


@pytest.mark.parametrize('action,needs_ack', [('flash', True), ('reset_run', False)])
def test_cli_erase_acknowledgement_only_required_for_flash(programming, tmp_path, action, needs_ack):
    from praxis.cli import main
    output = tmp_path / 'cli-grant.json'
    argv = ['hardware-authorize', '--plan', str(tmp_path / 'plan.json'), '--output', str(output),
            '--audit-root', str(tmp_path / 'cli-audit'), '--operator', 'Test operator',
            '--board-confirmation', 'TEST FIXTURE only', '--actions', action]
    if needs_ack:
        with pytest.raises(SystemExit) as error:
            main(argv)
        assert error.value.code == 2 and not output.exists()
        argv.append('--acknowledge-sector-erase')
    assert main(argv) == 0
    assert json.loads(output.read_text())['max_flash_attempts'] == int(action == 'flash')


def test_audit_reservation_failure_prevents_backend(programming, monkeypatch):
    s, artifact, connection, _ = programming
    def denied(*args):
        raise OSError('TEST audit disk unavailable')
    monkeypatch.setattr(s, 'reserve_attempt', denied)
    monkeypatch.setattr(s, 'run_backend', lambda *_: pytest.fail('Unrecorded operation launched'))
    with pytest.raises(OSError):
        s.flash_firmware(artifact, connection)


def test_audit_result_failure_does_not_release_consumed_attempt(programming, monkeypatch):
    s, artifact, connection, _ = programming
    def denied(*args):
        raise OSError('TEST result disk unavailable')
    monkeypatch.setattr('praxis.programming.exclusive_json', denied)
    with pytest.raises(PraxisError, match='AUDIT_FAILED'):
        s.flash_firmware(artifact, connection)
    with pytest.raises(PraxisError, match='OPERATION_BUDGET'):
        s.flash_firmware(artifact, connection)


def test_probe_lock_prevents_concurrent_mutation(programming):
    s, artifact, connection, _ = programming
    with s.hardware.probe_lock('TEST123'), pytest.raises(PraxisError, match='PROBE_BUSY'):
        s.flash_firmware(artifact, connection)


def test_authorization_lock_does_not_block_indefinitely(programming):
    import fcntl

    s, artifact, connection, _ = programming
    path = Path(s.authorization.audit_root) / s.authorization.authorization_revision / 'budget.lock'
    path.parent.mkdir(parents=True)
    with path.open('w') as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        with pytest.raises(PraxisError, match='AUTHORIZATION_BUSY'):
            s.flash_firmware(artifact, connection)


def test_expiry_after_staging_prevents_backend_launch(programming, monkeypatch):
    s, artifact, _, _ = programming
    image = s.snapshot_image(artifact)
    monkeypatch.setattr('praxis.programming.bounded', lambda *_a, **_k:
                        pytest.fail('Expired backend launched'))
    with pytest.raises(PraxisError, match='AUTHORIZATION_EXPIRED'):
        s.run_backend(PROBE, '000000010000000200000003', 'flash', image, 0, 1)


@pytest.mark.parametrize('operation', sorted(CONTROLS))
def test_control_operations_verify_image_and_report_state(programming, operation):
    s, artifact, connection, _ = programming
    r = s.control_execution(artifact, connection, operation, 0)
    assert r['success'] and r['readback_verified']
    running = operation in {'reset_run', 'resume'}
    assert r['execution_state'] == ('running' if running else 'halted')
    assert r['run_continues_after_return'] is running


@pytest.mark.parametrize('operation,ms', [('mass_erase', 0), ('step', 0),
    ('reset_run', -1), ('reset_run', 5001), ('reset_run', True)])
def test_unregistered_operations_and_unbounded_windows_rejected(programming, operation, ms):
    s, artifact, connection, _ = programming
    with pytest.raises(PraxisError, match='INVALID_OPERATION'):
        s.control_execution(artifact, connection, operation, ms)


def test_authorization_cannot_be_placed_in_source_workspace(programming):
    s, _, _, _ = programming
    path = s.build.workspace / 'grant.json'
    path.write_bytes(s.authorization_path.read_bytes())
    with pytest.raises(PraxisError, match='INVALID_AUTHORIZATION'):
        ProgrammingService(s.build, s.hardware, path)


def test_plan_modified_hash_and_sector_geometry_rejected(programming):
    s, _, _, _ = programming
    plan = s.authorization.plan.model_dump()
    plan['erase_length'] = 20000
    plan['plan_revision'] = canonical_hash(plan, 'plan_revision')
    with pytest.raises(PraxisError, match='INVALID_FLASH_PLAN'):
        checked_plan(plan)


def test_real_openocd_parses_flash_config_without_adapter_init(tmp_path):
    require_tool('openocd')
    cfg = tmp_path / 'cfg.tcl'
    cfg.write_text(mutation_configuration('TEST123', 0x374B, True))
    r = subprocess.run(['openocd', '-f', str(cfg), '-c', 'echo TEST_CONFIG_OK; shutdown'],
                       cwd=tmp_path, capture_output=True, text=True, timeout=5)
    assert r.returncode == 0 and 'TEST_CONFIG_OK' in r.stdout + r.stderr


@pytest.mark.parametrize('operation', ['flash', *sorted(CONTROLS)])
@pytest.mark.parametrize('case', ['ok', 'wrong_uid', 'wrong_family', 'wrong_image'])
def test_real_tcl_guards_and_exact_comparison_before_mutation(programming, tmp_path, operation, case):
    """Run the generated Tcl interpreter with modeled memory and modeled writes, never an adapter."""
    require_tool('openocd')
    s, artifact, _, _ = programming
    image = s.snapshot_image(artifact)
    data = values()
    if case == 'wrong_uid':
        data['uid0'] = 99
    if case == 'wrong_family':
        data['idcode'] = 0x433
    table = {f'0x{address:08x}': data[name] for name, (address, _) in IDENTITY.items()}
    for offset in range(0, len(image.data) // 4 * 4, 4):
        table[f'0x{0x08000000 + offset:08x}'] = struct.unpack_from('<I', image.data, offset)[0]
    for offset in range(len(image.data) // 4 * 4, len(image.data)):
        table[f'0x{0x08000000 + offset:08x}'] = image.data[offset]
    if case == 'wrong_image':
        table['0x08000000'] ^= 1
    pairs = ' '.join(f'{key} {hex(value)}' for key, value in table.items())
    prelude = ('gdb_port disabled\ntcl_port disabled\ntelnet_port disabled\n'
        f'set test_values [dict create {pairs}]\nset test_state halted\n'
        'proc test_read {address width count} {\n global test_values\n set result {}\n'
        ' for {set i 0} {$i < $count} {incr i} {\n'
        '  lappend result [dict get $test_values [format "0x%08x" [expr {$address+$i*($width/8)}]]]\n'
        ' }\n return $result\n}\n'
        'proc test_control {operation args} {\n global test_state\n echo "TEST_MUTATION|$operation"\n'
        ' if {$operation eq "reset"} {\n'
        '  if {[lindex $args 0] eq "run"} {set test_state running} else {set test_state halted}\n'
        ' } elseif {$operation eq "resume"} {set test_state running} '
        'elseif {$operation eq "halt"} {set test_state halted}\n}\n'
        'proc test_regs {args} {\n'
        ' if {[llength $args] != 2 || [lindex $args 0] ne "-force" || '
        '[lindex $args 1] ne "pc sp lr xPSR"} {error "TEST_UNKNOWN_REGISTER"}\n'
        ' return [dict create pc 0x08000401 sp 0x2001ff00 lr 0xfffffffd xPSR 0x1000000]\n}\n'
        'proc test_noop {args} {}\n')
    script = mutation_script('000000010000000200000003', operation, image, 0)
    script = script.replace('init\n', 'echo TEST_NO_ADAPTER\n', 1)
    script = script.replace('read_memory ', 'test_read ').replace('praxis.cpu curstate', 'set test_state')
    script = script.replace('get_reg ', 'test_regs ')
    for name in ('reset', 'flash', 'resume', 'halt', 'dump_image'):
        script = '\n'.join('test_control ' + line if line.startswith(name + ' ') or line == name else line
                           for line in script.splitlines()) + '\n'
    for name in ('poll', 'wait_halt'):
        script = '\n'.join('test_noop' + line[len(name):] if line.startswith(name + ' ') or line == name else line
                           for line in script.splitlines()) + '\n'
    path = tmp_path / 'guard.tcl'
    path.write_text(prelude + script)
    r = subprocess.run(['openocd', '-f', str(path)], cwd=tmp_path,
                       capture_output=True, text=True, timeout=5)
    output = r.stdout + r.stderr
    should_fail = case in {'wrong_uid', 'wrong_family'} or (case == 'wrong_image' and operation != 'flash')
    if should_fail:
        assert r.returncode, output
        assert not any(line.startswith('TEST_MUTATION|') for line in output.splitlines()), output
    else:
        assert r.returncode == 0 and 'PRAXIS_OPERATION_COMPLETE' in output, output
        result = parse_observation(output, False, core_registers=True)
        assert result['state'] == ('running' if operation in {'reset_run', 'resume'} else 'halted')
    assert not any(word in mutation_configuration('TEST123', 0x374B, True) + mutation_script(
        '000000010000000200000003', operation, image, 0)
        for word in ('mass_erase', 'options_write', 'optcr', 'unlock', 'protect ', 'source ['))


@pytest.mark.parametrize('scope', ['full', 'control_only', 'flash_only'])
async def test_authorized_tools_over_stdio_fake_probe(programming, tmp_path, scope):
    s, artifact, _, _ = programming
    grant = s.authorization_path
    if scope != 'full':
        grant = tmp_path / (scope + '.json')
        authorize_plan(tmp_path / 'plan.json', grant, tmp_path / 'scoped-audit', 'Test operator',
                       'TEST FIXTURE only', ['reset_run', 'halt'] if scope == 'control_only' else ['flash'])
    runner = tmp_path / 'stdio-fixture.py'
    runner.write_text('import praxis.hardware\nfrom pathlib import Path\n'
        'from praxis.build_server import create_build_server\n'
        f'praxis.hardware.discover_probes=lambda:[{PROBE!r}]\n'
        f'create_build_server(Path({str(s.build.bundle.root)!r}),Path({str(s.build.assets.root)!r}),'
        f'Path({str(s.build.workspace)!r}),Path({str(s.build.artifacts)!r}),'
        f'Path({str(s.build.lock_path)!r}),Path({str(s.hardware.backend.parent / "hardware.json")!r}),'
        f'Path({str(grant)!r})).run(transport="stdio")\n')
    params = StdioServerParameters(command=sys.executable, args=[str(runner)], cwd=str(ROOT), env=dict(os.environ))
    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            tools = {tool.name: tool for tool in (await client.list_tools()).tools}
            assert len(tools) == (9 if scope == 'full' else 8)
            assert ('flash_firmware' in tools) == (scope != 'control_only')
            assert ('control_execution' in tools) == (scope != 'flash_only')
            for name in ('flash_firmware', 'control_execution'):
                if name in tools:
                    assert tools[name].annotations.destructiveHint
                    assert not tools[name].annotations.readOnlyHint
            async def call(name, arguments):
                result = await client.call_tool(name, arguments)
                assert not result.isError, result.content
                return result.structuredContent or json.loads(result.content[0].text)
            profile = await call('get_build_profile', {})
            assert profile['hardware_programming']['enabled']
            target = await call('inspect_target', {'probe_serial': 'TEST123'})
            args = {'artifact_id': artifact, 'connection_id': target['connection_id']}
            plan = await call('plan_firmware', args)
            assert plan['plan_revision'] == s.authorization.plan.plan_revision
            if scope != 'control_only':
                result = await call('flash_firmware', args)
                assert result['success'] and result['execution_state'] == 'halted'
                second = await client.call_tool('flash_firmware', args)
                assert second.isError and 'OPERATION_BUDGET' in second.content[0].text
            else:
                assert profile['hardware_programming']['max_flash_attempts'] == 0
            if scope != 'flash_only':
                for action in ['reset_run', 'halt']:
                    result = await call('control_execution', {**args, 'operation': action, 'observation_ms': 0})
                    assert result['success']
    await asyncio.wait_for(exercise(), timeout=30)
