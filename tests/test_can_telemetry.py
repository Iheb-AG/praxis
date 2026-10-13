"""CAN telemetry qualification, actual MCP with a fake probe, and target ABI layout."""
import asyncio
import copy
import io
import json
import os
import struct
import subprocess
import sys

import pytest
from elftools.elf.elffile import ELFFile
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_image, require_tool
from praxis import can_telemetry as can
from praxis.bundle import Bundle
from praxis.cli import main
from praxis.errors import PraxisError
from praxis.firmware_build import BuildService, build_commands
from praxis.hardware import provision_profile
from praxis.telemetry import get_contract, parse_samples, telemetry_address
from test_hardware_inspection import PROBE, values
from test_telemetry import register_fixture

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-can-v1'
APPLICATION = ROOT / 'examples/stm32f407g-disc1-can/telemetry_application'
ASSETS = ROOT / 'assets/stm32f407vg'
ARTIFACT = 'a' * 64
REVISION = Bundle(BUNDLE).manifest.bundle_revision


def words(**changes):
    row = dict.fromkeys(can.FIELDS, 0)
    row.update(generation=2, magic=can.MAGIC, abi=can.ABI, size_bytes=can.SIZE,
               publications=1, phase=1, status=0, flags=255, clock_step=24,
               irq_count=1, rx_words_read_mask=15, rx_identifier=can.IDENTIFIER,
               rx_length=8, rx_low=can.PAYLOAD_LOW, rx_high=can.PAYLOAD_HIGH,
               last_tsr=0x1c000003, expected_identifier=can.IDENTIFIER,
               expected_low=can.PAYLOAD_LOW, expected_high=can.PAYLOAD_HIGH)
    row.update(changes)
    return [row[k] for k in can.FIELDS]


def observation(**changes):
    return {'artifact_id': ARTIFACT, 'bundle_revision': REVISION,
            'kind': can.KIND, 'symbol': can.SYMBOL, 'abi': can.ABI, 'record_bytes': can.SIZE,
            'readback_verified_before_and_after': True, 'execution_state': 'running',
            'image_sha256': 'b' * 64, 'elf_sha256': 'c' * 64,
            'samples': [dict(zip(can.FIELDS, words(generation=2+i*2, publications=i+1, **changes),
                                strict=True)) for i in range(3)],
            'assessment': {'loopback_success_reported': True}}


def qualify(rows, **kwargs):
    return can.qualify_windows(rows, artifact_id=ARTIFACT, bundle_revision=REVISION, **kwargs)


@pytest.mark.parametrize('change', [
    {'generation': 3}, {'magic': 0}, {'abi': 2}, {'size_bytes': 0}, {'phase': 3},
    {'status': 11}, {'flags': 256}, {'rx_words_read_mask': 16}, {'clock_step': 25},
    {'publications': True}, {'last_tsr': -1},
])
def test_malformed_or_wrong_abi_words_fail(change):
    with pytest.raises(PraxisError, match='TELEMETRY_(ABI|PROTOCOL)'):
        can.decode_sample(words(**change))


@pytest.mark.parametrize('change', [
    {'phase': 0}, {'phase': 2, 'status': 8}, {'status': 4}, {'flags': 127},
    {'clock_step': 23}, {'irq_count': 0}, {'rx_words_read_mask': 7},
    {'rx_identifier': can.IDENTIFIER | 4}, {'rx_length': 9}, {'rx_length': 0x208},
    {'rx_low': 0}, {'rx_high': 0}, {'expected_identifier': 0}, {'expected_low': 0},
    {'last_tsr': 0x1c000001}, {'last_tsr': 0x1c000003 | 8}, {'last_esr': 0x10},
    {'last_rf0': 1}, {'end_ier': 2}, {'end_irq_enabled': 1 << 20},
])
def test_failed_receipt_errors_wrong_payload_and_unclean_state_cannot_pass(change):
    report = qualify([observation(**change)])
    assert not report['passed'] and report['windows'][0]['failures']


@pytest.mark.parametrize('key,value', [
    ('artifact_id', 'f'*64), ('bundle_revision', 'f'*64), ('kind', 'uart-loopback-v1'),
    ('symbol', 'praxis_telemetry'), ('abi', True), ('record_bytes', True),
    ('execution_state', 'halted'), ('image_sha256', []),
    ('readback_verified_before_and_after', 1),
])
def test_wrong_metadata_cannot_promote_success(key, value):
    row = observation()
    row[key] = value
    assert not qualify([row])['passed']


def test_qualification_recomputes_labels_requires_freshness_and_all_windows():
    assert qualify([observation()])['passed']
    row = observation(phase=2, status=8)
    for sample in row['samples']:
        sample['phase_name'] = 'passed'
    assert not qualify([row])['passed']
    assert qualify([row], expected='failed')['passed']
    assert not qualify([observation()], expected='failed')['passed']
    row = observation()
    row['samples'][1] = copy.deepcopy(row['samples'][0])
    assert not qualify([row])['passed']
    row = observation()
    row['samples'][1]['publications'] = 0
    assert not qualify([row])['passed']
    row = observation()
    row['samples'][1]['last_esr'] = 1
    assert not qualify([row])['passed']
    # Reusing the identical window is stale across the boundary.
    assert not qualify([observation(), observation()])['passed']
    later = observation()
    for sample in later['samples']:
        sample['publications'] += 3
        sample['generation'] += 6
    assert qualify([observation(), later])['passed']
    later['image_sha256'] = 'e' * 64
    assert not qualify([observation(), later])['passed']


def test_wrapping_generation_and_publications_are_bounded_not_boot_identity():
    rows = [can.decode_sample(words(generation=0xfffffffe, publications=0xffffffff)),
            can.decode_sample(words(generation=0, publications=0))]
    assert can.assess(rows)['loopback_success_reported']
    rows[1]['generation'] = 2  # Inconsistent publication delta.
    assert not can.assess(rows)['loopback_success_reported']


@pytest.mark.parametrize('samples', [None, [], [{}], [dict.fromkeys(can.FIELDS, 0)]*6])
def test_invalid_window_shape(samples):
    row = observation()
    row['samples'] = samples
    with pytest.raises(PraxisError, match='INVALID_OBSERVATION'):
        qualify([row])


def test_publisher_layout_and_barriers_match_python(tmp_path):
    require_tool('gcc')
    binary = tmp_path / 'publisher'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-I', str(APPLICATION),
                    str(ROOT/'tests/fixtures/f407_can_publisher.c'), '-o', str(binary)],
                   check=True, capture_output=True, timeout=20)
    result = json.loads(subprocess.check_output([str(binary)], timeout=5))
    assert result['failures'] == 0 and result['fences'] == 4
    decoded = can.decode_sample(result['words'])
    assert decoded['publications'] == 2 and decoded['phase_name'] == 'boot'
    for name in ('can_controller.h', 'clock_setup.h', 'clock_sequence.h'):
        assert (APPLICATION/name).read_bytes() == (APPLICATION.parent/'application'/name).read_bytes()


@pytest.fixture(scope='module')
def can_elf(tmp_path_factory):
    require_tool('arm-none-eabi-gcc')
    out = tmp_path_factory.mktemp('can-abi-link')
    for compiler, flags in build_commands(['main.c']):
        args = [a.replace('/approved/', str(ASSETS)+'/').replace('/src/', str(APPLICATION)+'/')
                .replace('/out/', str(out)+'/').replace('-I/src', '-I'+str(APPLICATION)) for a in flags]
        subprocess.run([compiler, *args], cwd=out, check=True, capture_output=True, timeout=20)
    return (out/'firmware.elf').read_bytes()


def test_wrong_contract_or_elf_object_rejected(can_elf):
    contract = get_contract(can.KIND)
    address = telemetry_address(can_elf, (0x20000000, 128*1024), contract=contract)
    assert address % 4 == 0
    with pytest.raises(PraxisError, match='TELEMETRY_UNSUPPORTED'):
        telemetry_address(can_elf, (0x20000000, 128*1024))
    elf = ELFFile(io.BytesIO(can_elf))
    table = elf.get_section_by_name('.symtab')
    index = next(i for i,s in enumerate(table.iter_symbols()) if s.name == can.SYMBOL)
    for offset, value in [(4, 0x40000000), (8, 4)]:
        bad = bytearray(can_elf)
        struct.pack_into('<I', bad, table['sh_offset'] + index*table['sh_entsize'] + offset, value)
        with pytest.raises(PraxisError, match='TELEMETRY_UNSUPPORTED'):
            telemetry_address(bytes(bad), (0x20000000, 128*1024), contract=contract)
    with pytest.raises(PraxisError, match='TELEMETRY_UNSUPPORTED'):
        get_contract('arbitrary')
    encoded = 'PRAXIS_TELEMETRY|0|' + ','.join(f'{v:08x}' for v in words())
    text = f'PRAXIS_IMAGE_VERIFIED\n{encoded}\nPRAXIS_IMAGE_REVERIFIED\nPRAXIS_TELEMETRY_COMPLETE\n'
    assert parse_samples(text, 1, contract=contract)[0]['phase_name'] == 'passed'
    with pytest.raises(PraxisError, match='TELEMETRY_ABI'):
        parse_samples(text, 1)


def test_can_offline_cli_writes_new_report_and_rejects_forged_success(tmp_path):
    source, out = tmp_path/'observation.json', tmp_path/'qualification.json'
    source.write_text(json.dumps(observation()))
    args = ['qualify-can', '--bundle', str(BUNDLE), '--artifact', ARTIFACT,
            '--observation', str(source), '--output', str(out)]
    assert main(args) == 0
    report = json.loads(out.read_text())
    assert report['passed'] and not report['repeatability_qualified']
    source.write_text(json.dumps(observation(irq_count=0)))
    assert main(args[:-2]) == 1


def test_sandbox_telemetry_link_binds_object_and_real_handler(tmp_path):
    require_image(ROOT/'toolchain-f407.lock.json')
    service = BuildService(BUNDLE, ASSETS, ROOT/'examples', tmp_path/'artifacts',
                           ROOT/'toolchain-f407.lock.json')
    result = service.build('stm32f407g-disc1-can/telemetry_application')
    assert result['image_validated'] and result['compile_passed']
    data = (service.artifacts/result['artifact_id']/'firmware.elf').read_bytes()
    assert telemetry_address(data, service.assets.ram, contract=get_contract(can.KIND))
    image = ELFFile(io.BytesIO(data))
    symbols = image.get_section_by_name('.symtab')
    vector = struct.unpack('<98I', image.get_section_by_name('.isr_vector').data())
    assert vector[36] == symbols.get_symbol_by_name('CAN1_RX0_IRQHandler')[0]['st_value']
    assert vector[36] != symbols.get_symbol_by_name('Default_Handler')[0]['st_value']


async def test_actual_mcp_can_contract_with_fixture_probe(tmp_path, can_elf):
    # Explicit fake probe/backend. No discovery or attachment to physical hardware.
    workspace = tmp_path/'workspace'
    workspace.mkdir()
    build = BuildService(BUNDLE, ASSETS, workspace, tmp_path/'artifacts', ROOT/'toolchain-f407.lock.json')
    artifact = register_fixture(build, can_elf)
    rows = [words(), words(generation=4, publications=2)]
    data = values()
    backend = tmp_path/'fixture-openocd'
    backend.write_text('#!'+sys.executable+'\nimport sys,pathlib\n'
        "if '--version' in sys.argv: print('Open On-Chip Debugger 0.12.0 (TEST ONLY)');sys.exit(0)\n"
        'script=pathlib.Path(sys.argv[-1]).read_text()\n'
        f'for k,v in {data!r}.items():\n'
        " if ('|'+k+'|') in script: print('PRAXIS|'+k+'|'+(v if k=='state' else '0x%08x'%v))\n"
        "if 'PRAXIS_TELEMETRY_COMPLETE' in script:\n"
        " print('PRAXIS_IMAGE_VERIFIED')\n"
        " if 'PRAXIS_CAN_STATE' in script:\n"
        "  print('PRAXIS_CAN_STATE|gate_before|02000000')\n"
        "  print('PRAXIS_CAN_STATE|mcr|00010018')\n"
        "  print('PRAXIS_CAN_STATE|msr|00000c00')\n"
        "  print('PRAXIS_CAN_STATE|gate_after|02000000')\n"
        f' for i,row in enumerate({rows!r}[:script.count(\'echo "PRAXIS_TELEMETRY|\')]):\n'
        "  print('PRAXIS_TELEMETRY|%d|'%i+','.join('%08x'%v for v in row))\n"
        " print('PRAXIS_IMAGE_REVERIFIED');print('PRAXIS_TELEMETRY_COMPLETE')\n")
    backend.chmod(0o700)
    profile = tmp_path/'hardware.json'
    provision_profile(BUNDLE, ASSETS, backend, profile)
    script = ('from pathlib import Path\nimport praxis.hardware\n'
        f'praxis.hardware.discover_probes=lambda:[{PROBE!r}]\n'
        'from praxis.build_server import create_build_server\n'
        f'create_build_server(Path({str(BUNDLE)!r}),Path({str(ASSETS)!r}),'
        f'Path({str(workspace)!r}),Path({str(build.artifacts)!r}),'
        f'Path({str(build.lock_path)!r}),Path({str(profile)!r}),'
        f'telemetry_artifact={artifact!r},telemetry_kind={can.KIND!r}).run(transport="stdio")\n')
    params = StdioServerParameters(command=sys.executable, args=['-c',script],
                                   cwd=str(tmp_path), env=dict(os.environ))

    async def exercise():
        async with stdio_client(params) as (r,w), ClientSession(r,w) as client:
            await client.initialize()
            tools = {t.name:t for t in (await client.list_tools()).tools}
            assert tools['read_firmware_telemetry'].annotations.readOnlyHint
            assert 'flash_firmware' not in tools and 'control_execution' not in tools
            assert set(tools['read_firmware_telemetry'].inputSchema['properties']) == {
                'connection_id', 'samples', 'interval_ms'}

            async def call(name, arguments):
                result = await client.call_tool(name, arguments)
                assert not result.isError
                return result.structuredContent or json.loads(result.content[0].text)

            profile = await call('get_build_profile', {})
            assert profile['firmware_telemetry']['kind'] == can.KIND
            assert profile['bundle_revision'] == REVISION
            target = await call('inspect_target', {'probe_serial':'TEST123'})
            observation = await call('read_firmware_telemetry', {'connection_id':target['connection_id']})
            assert observation['assessment']['loopback_success_reported']
            report = can.qualify_windows([observation], artifact_id=artifact, bundle_revision=REVISION)
            assert report['passed'] and not report['repeatability_qualified']
            diagnostics = await call('read_can_diagnostics', {'connection_id':target['connection_id']})
            assert diagnostics['can_state']['clock_enabled']
            assert not diagnostics['can_state']['init_acknowledged']
            result = await client.call_tool('read_firmware_telemetry',
                {'connection_id':target['connection_id'],'samples':6})
            assert result.isError and 'INVALID_TELEMETRY_REQUEST' in result.content[0].text

    await asyncio.wait_for(exercise(), 30)
