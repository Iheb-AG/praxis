"""Fixture-backed probe tests and real OpenOCD configuration parsing (no target access)."""
import asyncio
import json
import os
import re
import subprocess
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.errors import PraxisError
from praxis.firmware_assets import FirmwareAssets
from praxis.hardware import (DIAGNOSTICS, IDENTITY, HardwareService, check_target,
    configuration, decode_clock, discover_probes, halted_core_register_script,
    parse_observation, profile_revision,
    provision_profile, read_script)

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-m1'
ASSETS = ROOT / 'assets/stm32f407vg'
PROBE = {'serial': 'TEST123', 'vendor_id': 0x0483, 'product_id': 0x374B,
         'usb_location': '1-1', 'product': 'TEST FIXTURE ST-LINK', 'selectable': True}


def values(diagnostics=False, **overrides):
    result = {'idcode': 0x10076413, 'cpuid': 0x410FC241, 'flash_kib': 1024,
              'uid0': 1, 'uid1': 2, 'uid2': 3, 'state': 'running'}
    if diagnostics:
        result.update({name: 0 for name in DIAGNOSTICS})
        result.update(rcc_cr=2, rcc_ahb1enr=9, systick_load=15999)
    result.update(overrides)
    return result


def markers(data):
    return '\n'.join(f'PRAXIS|{name}|' + (value if name == 'state' else f'0x{value:08x}')
                     for name, value in data.items()) + '\n'


@pytest.fixture
def hardware(tmp_path, monkeypatch):
    # A trusted fixture executable substitutes for OpenOCD; no hardware is touched.
    backend = tmp_path / 'fixture-openocd'
    observation = tmp_path / 'fixture-observation.json'
    observation.write_text(json.dumps(values(True)))
    backend.write_text('#!' + sys.executable + '\nimport sys,json,pathlib\n'
        'if "--version" in sys.argv:\n print("Open On-Chip Debugger 0.12.0 (TEST FIXTURE ONLY)")\n'
        'else:\n'
        f' data=json.loads(pathlib.Path({str(observation)!r}).read_text())\n'
        ' script=pathlib.Path(sys.argv[-1]).read_text()\n'
        ' for k,v in data.items():\n'
        '  if ("|"+k+"|") in script or ("get_reg" in script and k in ("pc","sp","lr","xpsr") and data["state"]=="halted"):\n'
        '   print("PRAXIS|"+k+"|"+(v if k=="state" else "0x%08x"%v))\n')
    backend.chmod(0o700)
    profile = tmp_path / 'hardware.json'
    provision_profile(BUNDLE, ASSETS, backend, profile)
    monkeypatch.setattr('praxis.hardware.discover_probes', lambda: [dict(PROBE)])
    s = HardwareService(Bundle(BUNDLE), FirmwareAssets(ASSETS), profile, tmp_path / 'locks')
    return s, observation


def test_sysfs_usb_enumeration_no_target_attach(tmp_path):
    for name, vid, pid, serial in [('1-1', '0483', '374b', 'TEST123'),
                                 ('1-2', '1234', '5678', 'unrelated'),
                                 ('1-3', '0483', '374b', 'bad;serial')]:
        dev = tmp_path / name
        dev.mkdir()
        for key, value in {'idVendor': vid, 'idProduct': pid, 'serial': serial}.items():
            (dev / key).write_text(value)
    probes = discover_probes(tmp_path)
    assert len(probes) == 2 and probes[0]['selectable'] and not probes[1]['selectable']


def test_generated_commands_do_not_write_halt_reset_or_serve_network():
    cfg = configuration('TEST123', 0x374B)
    for line in ['gdb_port disabled', 'tcl_port disabled', 'telnet_port disabled',
                 'reset_config none', 'praxis.cpu configure -work-area-size 0']:
        assert line in cfg
    script = read_script(True, '000000010000000200000003')
    text = cfg + script
    assert script.index('PRAXIS_TARGET_MISMATCH') < script.index('0x1fff7a22')
    assert script.index('PRAXIS_TARGET_CHANGED') < script.index('0x40023800')
    assert not re.search(r'^\s*(source|halt|resume|reset |mww|mwh|mwb|write_memory|flash |program|step|bp )', text, re.M)
    assert '0xe000e010' not in text.lower()  # SysTick CTRL clears COUNTFLAG.
    assert '0xe000edf0' not in text.lower()  # DHCSR has clear-on-read flags.


@pytest.mark.parametrize('serial', ['x;reset halt', '[shutdown]', 'x\ny', '', 'a' * 65])
def test_probe_serial_cannot_inject_tcl(serial):
    with pytest.raises(PraxisError, match='INVALID_PROBE'):
        configuration(serial, 0x374B)


def test_complete_fixture_backend_and_identity_binding(hardware):
    s, observation = hardware
    target = s.inspect_target('TEST123')
    assert target['target_identity']['device_id'] == 0x413
    assert 'exact MCU package and PCB revision not detected' in target['compatibility']
    result = s.inspect_execution(target['connection_id'])
    assert result['clock']['nominal_hclk_hz'] == 16000000
    assert result['clock']['systick_period_if_processor_clock_ms'] == 1
    assert result['core_registers'] == {} and result['physical_behavior'] == 'not tested'
    observation.write_text(json.dumps(values(True, uid0=99)))
    with pytest.raises(PraxisError, match='TARGET_CHANGED'):
        s.inspect_execution(target['connection_id'])
    with pytest.raises(PraxisError, match='UNKNOWN_CONNECTION'):
        s.inspect_execution(target['connection_id'])


def test_already_halted_core_registers_are_returned(hardware):
    s, observation = hardware
    observation.write_text(json.dumps(values(True, state='halted', pc=0x08000401,
                                          sp=0x2001FF00, lr=0xFFFFFFFD, xpsr=0x1000000)))
    target = s.inspect_target('TEST123')
    result = s.inspect_execution(target['connection_id'])
    assert result['core_registers']['sp'] == '0x2001ff00'


def test_disabled_gpio_clocks_suppress_signal_claims(hardware):
    s, observation = hardware
    data = values(True, rcc_ahb1enr=0)
    data.pop('gpioa_idr')
    data.pop('gpiod_odr')
    observation.write_text(json.dumps(data))
    target = s.inspect_target('TEST123')
    result = s.inspect_execution(target['connection_id'])
    assert result['signals']['led_a_output_latch'] is None
    assert result['signals']['button_input_sample'] is None
    with pytest.raises(PraxisError, match='BACKEND_PROTOCOL'):
        parse_observation(markers({**data, 'rcc_ahb1enr': 9}), True)


@pytest.mark.parametrize('change', [{'idcode': 0x433}, {'flash_kib': 512}, {'cpuid': 0x410FC231},
                                  {'uid0': 0, 'uid1': 0, 'uid2': 0}])
def test_wrong_family_core_flash_or_uid_rejected(change):
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        check_target(values(**change))


def test_missing_or_ambiguous_probe_never_runs_backend(hardware, monkeypatch):
    s, _ = hardware
    monkeypatch.setattr(s, 'observe', lambda *_: pytest.fail('No backend access permitted'))
    monkeypatch.setattr('praxis.hardware.discover_probes', lambda: [])
    with pytest.raises(PraxisError, match='PROBE_NOT_FOUND'):
        s.inspect_target('TEST123')
    monkeypatch.setattr('praxis.hardware.discover_probes', lambda: [PROBE, PROBE])
    with pytest.raises(PraxisError, match='AMBIGUOUS_PROBE'):
        s.inspect_target('TEST123')


def test_probe_lock_excludes_other_processes(hardware):
    s, _ = hardware
    with s.probe_lock('TEST123'), pytest.raises(PraxisError, match='PROBE_BUSY'), s.probe_lock('TEST123'):
        pytest.fail('Probe lock was bypassed')


def test_backend_tampering_rejected(hardware):
    s, _ = hardware
    s.backend.write_text('#!/bin/false\n')
    with pytest.raises(PraxisError, match='INTEGRITY_ERROR'):
        s.inspect_target('TEST123')


@pytest.mark.parametrize('output', [markers(values()).replace('0x00000400', '-1'),
    markers(values()) + 'PRAXIS|state|running\n', markers(values()).replace('PRAXIS|uid0|', 'PRAXIS|unknown|'),
    markers(values()).replace('PRAXIS|state|running', 'PRAXIS|state|made-up'), 'no observations'])
def test_malformed_or_incomplete_backend_results_rejected(output):
    with pytest.raises(PraxisError, match='BACKEND_PROTOCOL'):
        parse_observation(output, False)


@pytest.mark.parametrize('failure,returncode,code', [('TIMEOUT', -9, 'TIMEOUT'),
    ('OUTPUT_LIMIT', -9, 'OUTPUT_LIMIT'), (None, 1, 'PROBE_ACCESS_FAILED')])
def test_backend_failures_never_fall_back_to_reset(hardware, monkeypatch, failure, returncode, code):
    s, _ = hardware
    monkeypatch.setattr('praxis.hardware.bounded', lambda *args, **kwargs:
                        {'failure': failure, 'returncode': returncode, 'diagnostics': 'USB denied'})
    with pytest.raises(PraxisError, match=code):
        s.inspect_target('TEST123')
    assert not s.connections


def test_profile_target_revision_mismatch(hardware):
    s, _ = hardware
    profile = s.backend.parent / 'hardware.json'
    data = json.loads(profile.read_text())
    data['bundle_revision'] = 'a' * 64
    data['profile_revision'] = profile_revision(data)
    profile.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        HardwareService(s.bundle, s.assets, profile, s.lock_root)


def test_clock_diagnostics_catch_prescaler_and_unstable_sampling():
    half = decode_clock(values(True, rcc_cfgr=0x80, rcc_cfgr_after=0x80))
    assert half['nominal_hclk_hz'] == 8000000
    assert half['systick_period_if_processor_clock_ms'] == 2
    changed = decode_clock(values(True, rcc_cfgr_after=0x80))
    assert not changed['stable_sample'] and changed['nominal_hclk_hz'] is None
    pll = (8 | (336 << 6) | (1 << 22) | (7 << 24))
    assert decode_clock(values(True, rcc_cfgr=8, rcc_cfgr_after=8, rcc_pllcfgr=pll))['nominal_hclk_hz'] == 168000000


def test_real_openocd_parses_minimal_config_without_connecting(tmp_path):
    require_tool('openocd')
    cfg = tmp_path / 'attach.cfg'
    cfg.write_text(configuration('TEST123', 0x374B))
    result = subprocess.run(['openocd', '-f', str(cfg), '-c', 'echo PRAXIS_CONFIG_VALID; shutdown'],
                            capture_output=True, text=True, timeout=5, cwd=tmp_path)
    assert result.returncode == 0 and 'PRAXIS_CONFIG_VALID' in result.stdout + result.stderr


@pytest.mark.parametrize('state', ['halted', 'running', 'unknown'])
@pytest.mark.parametrize('legacy_spelling', [False, True])
def test_real_tcl_case_sensitive_core_register_contract(tmp_path, state, legacy_spelling):
    """Model the documented OpenOCD register namespace, never attach or halt a target."""
    require_tool('openocd')
    fragment = '\n'.join(halted_core_register_script()).replace('praxis.cpu curstate', 'set test_state')
    if legacy_spelling:
        fragment = fragment.replace('xPSR', 'xpsr')
    prefix = ('gdb_port disabled\ntcl_port disabled\ntelnet_port disabled\n'
        f'set test_state {state}\n'
        'proc test_get_reg {option names} {\n'
        ' echo TEST_CORE_READ\n'
        ' if {$option ne "-force" || $names ne "pc sp lr xPSR"} {\n'
        '  error "TEST_UNKNOWN_REGISTER: expected case-sensitive xPSR"\n }\n'
        ' return [dict create pc 0x08000401 sp 0x2001ff00 lr 0xfffffffd xPSR 0x01000000]\n}\n')
    path = tmp_path / 'core-contract.tcl'
    path.write_text(prefix + fragment.replace('get_reg ', 'test_get_reg ') + '\nshutdown\n')
    result = subprocess.run(['openocd', '-f', str(path)], capture_output=True,
                            text=True, timeout=5, cwd=tmp_path)
    output = result.stdout + result.stderr
    if state != 'halted':
        assert result.returncode == 0 and 'TEST_CORE_READ' not in output, output
    elif legacy_spelling:
        assert result.returncode != 0 and 'TEST_UNKNOWN_REGISTER' in output, output
    else:
        assert result.returncode == 0, output
        assert 'PRAXIS|xpsr|0x01000000' in output
        assert 'PRAXIS|xPSR|' not in output


@pytest.mark.parametrize('change,error', [({'idcode': 0x433}, 'PRAXIS_TARGET_MISMATCH'),
    ({'uid0': 99}, 'PRAXIS_TARGET_CHANGED'), ({'rcc_ahb1enr': 0}, None)])
def test_real_tcl_guards_precede_peripheral_reads(tmp_path, change, error):
    """Execute actual generated Tcl with mock memory; never initialize a debug adapter."""
    require_tool('openocd')
    data = values(True, **change)
    pairs = ' '.join(f'0x{address:08x} 0x{data[name]:x}'
                     for name, (address, _) in {**IDENTITY, **DIAGNOSTICS}.items())
    prefix = ('gdb_port disabled\ntcl_port disabled\ntelnet_port disabled\n'
        f'set praxis_test_values [dict create {pairs}]\n'
        'proc praxis_test_memory {address width count} {\n'
        ' global praxis_test_values\n echo "TEST_READ|$address"\n'
        ' return [list [dict get $praxis_test_values $address]]\n}\n'
        'set praxis_test_state unknown\n')
    script = read_script(True, '000000010000000200000003')
    script = script.replace('init\n', 'echo TEST_NO_ADAPTER\n', 1)
    script = script.replace('read_memory ', 'praxis_test_memory ')
    script = script.replace('praxis.cpu curstate', 'set praxis_test_state')
    path = tmp_path / 'guard-test.tcl'
    path.write_text(prefix + script)
    result = subprocess.run(['openocd', '-f', str(path)], capture_output=True,
                            text=True, timeout=5, cwd=tmp_path)
    output = result.stdout + result.stderr
    reads = [line for line in output.splitlines() if line.startswith('TEST_READ|')]
    if error:
        assert result.returncode and error in output
        assert not any(line.startswith('TEST_READ|0x400') for line in reads)
        if change.get('idcode'):
            assert 'TEST_READ|0x1fff7a22' not in reads
    else:
        assert result.returncode == 0, output
        assert 'TEST_READ|0x40020010' not in reads and 'TEST_READ|0x40020c14' not in reads
        assert parse_observation(output, True)['rcc_ahb1enr'] == 0


async def test_hardware_tools_discovered_over_real_stdio(hardware, tmp_path):
    s, _ = hardware
    lock = tmp_path / 'lock.json'
    lock.write_text(json.dumps({'schema_version': 1, 'profile': s.assets.manifest.profile,
                               'asset_revision': s.assets.identity, 'image': None}))
    workspace = tmp_path / 'workspace'
    workspace.mkdir()
    params = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
        '--bundle', str(BUNDLE), '--assets', str(ASSETS), '--workspace', str(workspace),
        '--artifacts', str(tmp_path / 'artifacts'), '--lock', str(lock),
        '--hardware-profile', str(s.backend.parent / 'hardware.json')], cwd=str(tmp_path), env=dict(os.environ))

    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            names = {tool.name for tool in (await client.list_tools()).tools}
            assert names == {'get_build_profile', 'build_firmware', 'validate_firmware',
                             'list_debug_probes', 'inspect_target', 'inspect_execution', 'plan_firmware'}
            profile = await client.call_tool('get_build_profile', {})
            result = profile.structuredContent or json.loads(profile.content[0].text)
            assert result['hardware_inspection']['enabled']
            invalid = await client.call_tool('inspect_target', {'probe_serial': ';reset halt'})
            assert invalid.isError and 'INVALID_PROBE' in invalid.content[0].text
            invalid = await client.call_tool('inspect_execution', {'connection_id': 'missing'})
            assert invalid.isError and 'UNKNOWN_CONNECTION' in invalid.content[0].text
    await asyncio.wait_for(exercise(), timeout=20)


def test_diagnostic_addresses_match_pinned_target_headers(tmp_path):
    require_tool('arm-none-eabi-gcc')
    code = '#include <stddef.h>\n#include <stm32f407xx.h>\n'
    expressions = {'idcode': 'DBGMCU_BASE + offsetof(DBGMCU_TypeDef, IDCODE)',
                   'cpuid': 'SCB_BASE + offsetof(SCB_Type, CPUID)', 'flash_kib': 'FLASHSIZE_BASE',
                   'uid0': 'UID_BASE', 'uid1': 'UID_BASE+4', 'uid2': 'UID_BASE+8',
                   'cfsr': 'SCB_BASE + offsetof(SCB_Type, CFSR)',
                   'hfsr': 'SCB_BASE + offsetof(SCB_Type, HFSR)',
                   'mmfar': 'SCB_BASE + offsetof(SCB_Type, MMFAR)',
                   'bfar': 'SCB_BASE + offsetof(SCB_Type, BFAR)',
                   'rcc_cr': 'RCC_BASE + offsetof(RCC_TypeDef, CR)',
                   'rcc_cfgr': 'RCC_BASE + offsetof(RCC_TypeDef, CFGR)',
                   'rcc_cfgr_after': 'RCC_BASE + offsetof(RCC_TypeDef, CFGR)',
                   'rcc_pllcfgr': 'RCC_BASE + offsetof(RCC_TypeDef, PLLCFGR)',
                   'rcc_ahb1enr': 'RCC_BASE + offsetof(RCC_TypeDef, AHB1ENR)',
                   'gpioa_idr': 'GPIOA_BASE + offsetof(GPIO_TypeDef, IDR)',
                   'gpiod_odr': 'GPIOD_BASE + offsetof(GPIO_TypeDef, ODR)',
                   'systick_load': 'SysTick_BASE + offsetof(SysTick_Type, LOAD)'}
    for name, (address, _) in {**IDENTITY, **DIAGNOSTICS}.items():
        code += f'_Static_assert(({expressions[name]}) == 0x{address:x}UL, "{name}");\n'
    source = tmp_path / 'addresses.c'
    source.write_text(code)
    result = subprocess.run(['arm-none-eabi-gcc', '-std=c11', '-mcpu=cortex-m4', '-mthumb',
        '-mfloat-abi=soft', '-DSTM32F407xx', '-I' + str(ASSETS / 'include'), '-fsyntax-only', str(source)],
        capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr
