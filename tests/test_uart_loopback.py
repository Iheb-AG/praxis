"""Trusted host tests for pure UART framing/control; no physical behavior claim."""
import binascii
import ctypes
import shutil
import subprocess

import pytest

from conftest import ROOT

APP = ROOT / 'examples/stm32f407g-disc1-uart-loopback/application'


@pytest.fixture(scope='module', params=['application', 'telemetry_application'])
def app(request):
    return APP.parent / request.param


@pytest.fixture(scope='module')
def protocol(tmp_path_factory, app):
    cc = shutil.which('gcc')
    if cc is None:
        pytest.skip('host GCC unavailable')
    out = tmp_path_factory.mktemp('uart-protocol') / 'protocol.so'
    subprocess.run([cc, '-std=c11', '-Wall', '-Wextra', '-Werror', '-shared', '-fPIC',
                    str(app / 'protocol.c'), '-o', str(out)], check=True, capture_output=True, timeout=20)
    library = ctypes.CDLL(str(out))
    library.frame_make.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32]
    library.frame_valid.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint32]
    library.frame_valid.restype = ctypes.c_bool
    return library


def reference(sequence):
    payload = bytes(((sequence >> (8 * (i % 4))) ^ (0x31 + 17 * i)) & 255 for i in range(8))
    body = bytes([1, 1]) + sequence.to_bytes(4, 'little') + bytes([8]) + payload
    return b'\xa5\x5a' + body + binascii.crc_hqx(body, 0xffff).to_bytes(2, 'big')


@pytest.mark.parametrize('sequence', [0, 1, 255, 256, 0x12345678, 0xffffffff])
def test_independent_crc_payload_sequence_and_corruption(protocol, sequence):
    frame = (ctypes.c_uint8 * 19)()
    protocol.frame_make(frame, sequence)
    assert bytes(frame) == reference(sequence)
    assert protocol.frame_valid(frame, sequence)
    assert not protocol.frame_valid(frame, (sequence + 1) & 0xffffffff)
    for index in range(19):
        for bit in range(8):
            changed = (ctypes.c_uint8 * 19).from_buffer_copy(frame)
            changed[index] ^= 1 << bit
            assert not protocol.frame_valid(changed, sequence)
    # Corrupt payload and recompute a correct CRC: still reject wrong payload.
    modified = bytearray(frame)
    modified[9] ^= 1
    modified[17:] = binascii.crc_hqx(modified[2:17], 0xffff).to_bytes(2, 'big')
    assert not protocol.frame_valid((ctypes.c_uint8 * 19).from_buffer_copy(modified), sequence)


def test_controller_and_debounce_boundaries(tmp_path, app):
    cc = shutil.which('gcc')
    if cc is None:
        pytest.skip('host GCC unavailable')
    executable = tmp_path / 'controller-test'
    subprocess.run([cc, '-std=c11', '-Wall', '-Wextra', '-Werror',
                    '-fsanitize=undefined', '-fno-sanitize-recover=all', '-I' + str(app),
                    str(ROOT / 'tests/fixtures/uart/controller_test.c'),
                    str(app / 'protocol.c'), str(app / 'controller.c'), '-o', str(executable)],
                   check=True, capture_output=True, timeout=20)
    result = subprocess.run([str(executable)], check=True, capture_output=True, text=True, timeout=3)
    assert 'checks passed' in result.stdout
