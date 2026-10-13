"""Portable CRC calculation checked against independent polynomial division.

Host GCC establishes arithmetic behavior only, not the peripheral's operation.
"""

import random
import subprocess

from conftest import ROOT, require_tool


def divide(seed, word):
    remainder = (seed ^ word) << 32
    for bit in range(63, 31, -1):
        if remainder & (1 << bit):
            remainder ^= 0x104C11DB7 << (bit - 32)
    return remainder


def test_word_feed_arithmetic_against_polynomial_division(tmp_path):
    require_tool('gcc')
    source = tmp_path / 'crc.c'
    source.write_text('#include <stdio.h>\n#include <inttypes.h>\n#include "word_crc.h"\n'
        'int main(void) { uint32_t s, w; while (scanf("%" SCNx32 " %" SCNx32, &s, &w) == 2) {\n'
        ' printf("%08" PRIx32 "\\n", praxis_crc_word(s, w)); } return 0; }\n')
    executable = tmp_path / 'crc'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-O2', '-I',
        str(ROOT / 'examples/stm32f407g-disc1-crc-dma/application'), str(source), '-o', str(executable)],
        check=True, capture_output=True, timeout=10)
    randomizer = random.Random(407)
    cases = [(0xffffffff, 0), (0xffffffff, 0xffffffff), (0, 0)]
    cases.extend((randomizer.getrandbits(32), randomizer.getrandbits(32)) for _ in range(1000))
    result = subprocess.run([str(executable)], input=''.join(f'{s:x} {w:x}\n' for s, w in cases),
        text=True, capture_output=True, check=True, timeout=5)
    assert [int(line, 16) for line in result.stdout.splitlines()] == [divide(*c) for c in cases]
    assert divide(0xffffffff, 0) == 0xC704DD7B
    assert divide(0xffffffff, 0xffffffff) == 0
