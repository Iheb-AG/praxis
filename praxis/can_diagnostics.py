"""Fixed read-only CAN1 acknowledgement diagnosis for the F407 loopback artifact.

Source evidence retrieved through MCP: CAN1 base and MCR/MSR/BTR declarations;
RM0090 Rev22 pp1073–1075,1090–1093,1099. No FIFO or W1C action is performed.
"""
from __future__ import annotations

import re

from praxis.errors import PraxisError

# Deliberately bounded allowlist, checked against the selected immutable Markdown.
GATE = 0x40023840
CAN1 = 0x40006400


def validate_bundle(bundle):
    if bundle.manifest.target.mcu != 'STM32F407VGT6':
        raise PraxisError('DIAGNOSTIC_UNSUPPORTED', 'CAN1 diagnostics require the exact F407 target')
    for name in ('can', 'rcc'):
        if name not in bundle.manifest.peripherals:
            raise PraxisError('DIAGNOSTIC_UNSUPPORTED', 'Select the reviewed CAN bundle')
    can = bundle.read(bundle.manifest.peripherals['can'])
    rcc = bundle.read(bundle.manifest.peripherals['rcc'])
    expected = [(can, r'^\| CAN1 \| 0x40006400 \|'),
                (rcc, r'^\| RCC \| 0x40023800 \|'),
                (rcc, r'^\| APB1ENR \| 0x040 \| 32 \|')]
    expected += [(can, rf'^\| {name} \| 0x{offset:03X} \| 32 \|')
                 for name,offset in [('MCR',0),('MSR',4),('BTR',28)]]
    if any(len(re.findall(pattern, text, re.M)) != 1 for text,pattern in expected):
        raise PraxisError('DIAGNOSTIC_UNSUPPORTED', 'Published register layout differs from the reviewed read allowlist')


def script() -> list[str]:
    return [
        f'set can_gate_before [lindex [read_memory 0x{GATE:08x} 32 1] 0]',
        'echo [format "PRAXIS_CAN_STATE|gate_before|%08x" $can_gate_before]',
        'if {$can_gate_before & 0x02000000} {',
        f'  set can_mcr [lindex [read_memory 0x{CAN1:08x} 32 1] 0]',
        f'  set can_msr [lindex [read_memory 0x{CAN1+4:08x} 32 1] 0]',
        '  echo [format "PRAXIS_CAN_STATE|mcr|%08x" $can_mcr]',
        '  echo [format "PRAXIS_CAN_STATE|msr|%08x" $can_msr]',
        '  if {$can_msr & 1} {',  # BTR is accessible only in acknowledged initialization.
        f'    set can_btr [lindex [read_memory 0x{CAN1+28:08x} 32 1] 0]',
        '    echo [format "PRAXIS_CAN_STATE|btr|%08x" $can_btr]',
        '  }',
        '}',
        f'set can_gate_after [lindex [read_memory 0x{GATE:08x} 32 1] 0]',
        'echo [format "PRAXIS_CAN_STATE|gate_after|%08x" $can_gate_after]',
    ]


def parse(output: str) -> dict:
    lines = output.splitlines()
    if (lines.count('PRAXIS_IMAGE_VERIFIED') != 1 or lines.count('PRAXIS_IMAGE_REVERIFIED') != 1
            or lines.index('PRAXIS_IMAGE_VERIFIED') >= lines.index('PRAXIS_IMAGE_REVERIFIED')):
        raise PraxisError('DIAGNOSTIC_PROTOCOL', 'CAN state requires ordered exact-image checks')
    rows, names = {}, []
    for position,line in enumerate(lines):
        if not line.startswith('PRAXIS_CAN_STATE|'):
            continue
        parts = line.split('|')
        if (len(parts) != 3 or parts[1] not in ('gate_before','gate_after','mcr','msr','btr')
                or parts[1] in rows or not re.fullmatch('[0-9a-f]{8}',parts[2])
                or not lines.index('PRAXIS_IMAGE_VERIFIED') < position < lines.index('PRAXIS_IMAGE_REVERIFIED')):
            raise PraxisError('DIAGNOSTIC_PROTOCOL', 'Malformed, duplicate or unbracketed CAN state')
        rows[parts[1]] = int(parts[2],16)
        names.append(parts[1])
    if ('gate_before' not in rows or 'gate_after' not in rows or
            rows['gate_before'] != rows['gate_after']):
        raise PraxisError('DIAGNOSTIC_PROTOCOL', 'CAN gate snapshot is absent or changed')
    enabled = bool(rows['gate_before'] & (1 << 25))
    expected = {'gate_before','gate_after'}
    if enabled:
        expected |= {'mcr','msr'}
        if rows.get('msr',0) & 1:
            expected.add('btr')
    canonical = [k for k in ('gate_before','mcr','msr','btr','gate_after') if k in expected]
    if set(rows) != expected or names != canonical:
        raise PraxisError('DIAGNOSTIC_PROTOCOL', 'CAN state differs from gated read policy')
    status = {'clock_enabled': enabled, 'raw': {k:hex(v) for k,v in rows.items()},
              'provenance': 'Selected immutable CAN/RCC Markdown; RM0090 Rev22 pp1073–1075,1090–1093,1099',
              'limits': 'Sequential live samples; not an atomic trace or proof of the earlier timeout phase.'}
    if enabled:
        status.update(init_requested=bool(rows['mcr'] & 1), sleep_requested=bool(rows['mcr'] & 2),
                      init_acknowledged=bool(rows['msr'] & 1), sleep_acknowledged=bool(rows['msr'] & 2),
                      rx_signal_high=bool(rows['msr'] & (1 << 11)))
    return status
