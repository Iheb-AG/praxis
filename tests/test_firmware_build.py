"""Real ARM fixture checks; native compilation is restricted to these trusted test inputs.

The production BuildService never invokes the host compiler.
"""
import io
import json
import os
import shutil
import struct
import subprocess
import sys

import pytest
from elftools.elf.elffile import ELFFile
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_image, require_tool
from praxis.elf_validation import validate_bytes
from praxis.errors import PraxisError
from praxis.firmware_assets import FirmwareAssets
from praxis.firmware_build import BuildService, build_commands
from praxis.verify import snapshot

ASSETS = ROOT / 'assets/stm32f407vg'
BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-m1'


@pytest.fixture(scope='module')
def assets():
    return FirmwareAssets(ASSETS)


@pytest.fixture(scope='module')
def good_elf(tmp_path_factory):
    require_tool('arm-none-eabi-gcc')
    out = tmp_path_factory.mktemp('trusted-f407')
    src = ROOT / 'examples/stm32f407g-disc1-led-button/application'
    for compiler, args in build_commands(['main.c']):
        translated = [a.replace('/approved/', str(ASSETS) + '/').replace('/src/', str(src) + '/')
                      .replace('/out/', str(out) + '/').replace('-I/src', '-I' + str(src)) for a in args]
        subprocess.run([compiler, *translated], cwd=out, check=True, capture_output=True)
    return (out / 'firmware.elf').read_bytes()


def service(tmp_path, image=None):
    workspace = tmp_path / 'workspace'
    workspace.mkdir(exist_ok=True)
    lock = tmp_path / 'lock.json'
    lock.write_text(json.dumps({'schema_version': 1, 'profile': 'stm32f407vg-c11-flash',
                               'asset_revision': FirmwareAssets(ASSETS).identity, 'image': image}))
    return BuildService(BUNDLE, ASSETS, workspace, tmp_path / 'artifacts', lock)


def test_reference_memory_vectors_and_startup(good_elf, assets):
    result = validate_bytes(good_elf, assets)
    assert result['valid'], result['errors']
    assert result['initial_sp'] == '0x20020000'
    assert result['physical_behavior'] == 'not tested'
    elf = ELFFile(io.BytesIO(good_elf))
    vector = elf.get_section_by_name('.isr_vector')
    assert vector['sh_size'] == 98 * 4
    symbols = {s.name: s['st_value'] for s in elf.get_section_by_name('.symtab').iter_symbols()}
    words = struct.unpack('<98I', vector.data())
    assert words[15] == symbols['SysTick_Handler'] != symbols['Default_Handler']


@pytest.mark.parametrize('slot,value,code', [(0, 0x20030000, 'INITIAL_SP'),
    (1, 0x20000001, 'RESET_ADDRESS'), (34, 0, 'VECTOR_HANDLER'), (95, 0x08000001, 'VECTOR_HANDLER')])
def test_invalid_stack_reset_or_irq_rejected(good_elf, assets, slot, value, code):
    elf = ELFFile(io.BytesIO(good_elf))
    offset = elf.get_section_by_name('.isr_vector')['sh_offset'] + slot * 4
    modified = bytearray(good_elf)
    struct.pack_into('<I', modified, offset, value)
    result = validate_bytes(bytes(modified), assets)
    assert not result['valid'] and code in {e['code'] for e in result['errors']}


@pytest.mark.parametrize('data', [b'', b'not elf', b'\x7fELF' + bytes(40)])
def test_malformed_images_report_errors(assets, data):
    assert not validate_bytes(data, assets)['valid']


def test_asset_hash_change_rejected(tmp_path):
    shutil.copytree(ASSETS, tmp_path / 'assets')
    (tmp_path / 'assets/stm32f407vg_flash.ld').write_text('MEMORY { RAM : LENGTH=192K }')
    with pytest.raises(PraxisError, match='INTEGRITY_ERROR'):
        FirmwareAssets(tmp_path / 'assets')


def test_wrong_mcu_assets_rejected():
    from praxis.bundle import Bundle
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        FirmwareAssets(ASSETS, Bundle(ROOT / 'bundles/stm32f401re'))


def test_fifo_source_cannot_block_snapshot(tmp_path):
    src, dst = tmp_path / 'src', tmp_path / 'dst'
    src.mkdir()
    dst.mkdir()
    os.mkfifo(src / 'trap.c')
    with pytest.raises(PraxisError, match='INVALID_SOURCE'):
        snapshot(src, dst)


@pytest.mark.parametrize('name', ['../escape', '/tmp/escape', 'a/../../escape', 'link'])
def test_build_workspace_path_rejection(tmp_path, name):
    s = service(tmp_path)
    (s.workspace / 'link').symlink_to(tmp_path, target_is_directory=True)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        s.source_path(name)


def test_unprovisioned_build_fails_closed(tmp_path):
    s = service(tmp_path)
    (s.workspace / 'app').mkdir()
    (s.workspace / 'app/main.c').write_text('int main(void) { return 0; }')
    with pytest.raises(PraxisError, match='UNPROVISIONED_IMAGE'):
        s.build('app')
    assert not s.artifacts.exists()


async def test_build_tools_over_real_stdio(tmp_path):
    import asyncio
    s = service(tmp_path)
    params = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
        '--bundle', str(BUNDLE), '--assets', str(ASSETS), '--workspace', str(s.workspace),
        '--artifacts', str(s.artifacts), '--lock', str(s.lock_path)], cwd=str(tmp_path))

    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            tools = {t.name: t for t in (await client.list_tools()).tools}
            assert set(tools) == {'get_build_profile', 'build_firmware', 'validate_firmware'}
            assert tools['get_build_profile'].annotations.readOnlyHint
            assert not tools['build_firmware'].annotations.readOnlyHint
            result = await client.call_tool('get_build_profile', {})
            assert not result.isError and 'STM32F407VGT6' in result.content[0].text
            result = await client.call_tool('build_firmware', {'source_directory': '../escape'})
            assert result.isError and 'INVALID_PATH' in result.content[0].text
            result = await client.call_tool('validate_firmware', {'artifact_id': '../../etc/passwd'})
            assert result.isError and 'INVALID_ARTIFACT' in result.content[0].text
    await asyncio.wait_for(exercise(), timeout=20)


def live_service(tmp_path):
    lock = require_image(ROOT / 'toolchain-f407.lock.json')
    workspace = tmp_path / 'workspace'
    workspace.mkdir()
    shutil.copytree(ROOT / 'examples/stm32f407g-disc1-led-button/application', workspace / 'app')
    return BuildService(BUNDLE, ASSETS, workspace, tmp_path / 'artifacts', lock)


def test_live_full_build_and_artifact_integrity(tmp_path):
    s = live_service(tmp_path)
    report = s.build('app')
    assert report['compile_passed'] and report['image_validated'], report
    artifact = report['artifact_id']
    assert s.validate(artifact)['validation']['valid']
    assert s.build('app')['artifact_id'] == artifact
    root = s.artifacts / artifact
    (root / 'firmware.bin').write_bytes(b'tampered')
    with pytest.raises(PraxisError, match='INTEGRITY_ERROR'):
        s.validate(artifact)


def test_live_compile_failure_and_header_shadow(tmp_path):
    s = live_service(tmp_path)
    (s.workspace / 'app/main.c').write_text('int main(void) { undefined_symbol = 1; }')
    result = s.build('app')
    assert not result['compile_passed'] and result['artifact_id'] is None
    assert 'undefined_symbol' in result['diagnostics']
    (s.workspace / 'app/stm32f407xx.h').write_text('/* shadow */')
    with pytest.raises(PraxisError, match='HEADER_SHADOW'):
        s.build('app')


async def test_live_build_over_real_stdio(tmp_path):
    import asyncio
    s = live_service(tmp_path)
    params = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
        '--bundle', str(BUNDLE), '--assets', str(ASSETS), '--workspace', str(s.workspace),
        '--artifacts', str(s.artifacts), '--lock', str(s.lock_path)], cwd=str(tmp_path), env=dict(os.environ))

    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            response = await client.call_tool('build_firmware', {'source_directory': 'app'})
            assert not response.isError, response
            result = response.structuredContent or json.loads(response.content[0].text)
            assert result['compile_passed'] and result['image_validated'], result
            checked = await client.call_tool('validate_firmware', {'artifact_id': result['artifact_id']})
            checked_result = checked.structuredContent or json.loads(checked.content[0].text)
            assert not checked.isError and checked_result['validation']['valid']
    await asyncio.wait_for(exercise(), timeout=45)
