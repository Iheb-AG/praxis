"""Opt-in, artifact-bound SRAM observation. No arbitrary address/symbol selection.

The launch-selected, fixed example ABI is a software observation contract, not peripheral
register knowledge. Exact flash bytes and MCU UID are checked in the same backend
invocation before any application SRAM is read. No halt/reset/write is requested.
"""
from __future__ import annotations

import io
import re
import tempfile
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

from praxis.bundle import digest, read_inside
from praxis.errors import PraxisError
from praxis.hardware import check_target, configuration, parse_observation, read_script
from praxis.programming import image_from_elf, verify_script
from praxis.verify import bounded

SYMBOL = 'praxis_telemetry'
MAGIC = 0x50525831
ABI = 1
FIELDS = ('generation', 'magic', 'abi', 'size_bytes', 'uptime_ms', 'timer_irqs',
          'uart_irqs', 'exti_irqs', 'run_number', 'state', 'frames_started',
          'frames_validated', 'run_validated', 'rx_bytes', 'tx_bytes', 'uart_errors',
          'queue_overflows', 'failure_reason', 'flags', 'last_good_ms',
          'next_sequence', 'button_presses', 'main_iterations')
SIZE = len(FIELDS) * 4
MAX_IMAGE_BYTES = 64 * 1024
STATES = ('paused', 'running', 'pausing', 'failed')
FAILURES = ('none', 'timeout', 'invalid_frame', 'unexpected_rx', 'uart_error', 'queue_overflow')
KINDS = ('uart-loopback-v1', 'can-loopback-v1', 'timer-routes-v1', 'timer-irq-v1')
LIMITS = [
    'SRAM values are firmware self-reports, not independent electrical or optical measurements.',
    'Timer/counter progress does not measure oscillator accuracy or prove arbitrary interrupt ordering.',
    'No reset, halt, resume, programming, peripheral-register read or target-memory write is requested.',
    'Debug attachment and sequential flash/SRAM reads can perturb timing; they are not electrically passive.',
    'Matching image bytes do not authenticate truthful counters or prove that this image is executing.',
    'Seqlock consistency is checked per sample; counter rollover, reset and freshness have separate limits.',
]


@dataclass(frozen=True)
class TelemetryContract:
    kind: str
    symbol: str
    abi: int
    fields: tuple[str, ...]
    decode: Callable
    assess: Callable

    @property
    def size(self) -> int:
        return len(self.fields) * 4


def get_contract(kind: str = 'uart-loopback-v1') -> TelemetryContract:
    """Explicit built-in allowlist; never infer ABI from SRAM or accept caller schemas."""
    if kind == 'uart-loopback-v1':
        return TelemetryContract(kind, SYMBOL, ABI, FIELDS, decode_sample, assess)
    if kind == 'can-loopback-v1':
        from praxis import can_telemetry as can
        return TelemetryContract(kind, can.SYMBOL, can.ABI, can.FIELDS, can.decode_sample, can.assess)
    if kind == 'timer-routes-v1':
        from praxis import timer_route_telemetry as timer
        return TelemetryContract(kind, timer.SYMBOL, timer.ABI, timer.FIELDS,
                                 timer.decode_sample, timer.assess)
    if kind == 'timer-irq-v1':
        from praxis import timer_irq_telemetry as timer
        return TelemetryContract(kind, timer.SYMBOL, timer.ABI, timer.FIELDS,
                                 timer.decode_sample, timer.assess)
    raise PraxisError('TELEMETRY_UNSUPPORTED', 'Select a built-in telemetry kind at server launch')


def telemetry_address(data: bytes, ram: tuple[int, int], *, contract=None) -> int:
    """Only the fixed, sized global object in allocated .bss below the stack."""
    from elftools.elf.elffile import ELFFile
    from elftools.common.exceptions import ELFError
    contract = contract or get_contract()
    try:
        elf = ELFFile(io.BytesIO(data))
        table = elf.get_section_by_name('.symtab')
        matches = table.get_symbol_by_name(contract.symbol) if table else []
        if not matches or len(matches) != 1:
            raise ValueError(f'Exactly one {contract.symbol} object is required')
        symbol = matches[0]
        if (symbol['st_info']['type'] != 'STT_OBJECT' or symbol['st_info']['bind'] != 'STB_GLOBAL'
                or symbol['st_size'] != contract.size or not isinstance(symbol['st_shndx'], int)):
            raise ValueError('Telemetry must be a global object of the fixed ABI size')
        section = elf.get_section(symbol['st_shndx'])
        address = symbol['st_value']
        if (section.name != '.bss' or section['sh_type'] != 'SHT_NOBITS'
                or section['sh_flags'] & 7 != 3 or address % 4
                or not ram[0] <= address < address + contract.size <= ram[0] + ram[1] - 4096
                or not section['sh_addr'] <= address < address + contract.size <= section['sh_addr'] + section['sh_size']):
            raise ValueError('Telemetry must lie in allocated writable main-SRAM .bss, below the stack')
        return address
    except (ELFError, ValueError, KeyError, IndexError, TypeError) as exc:
        raise PraxisError('TELEMETRY_UNSUPPORTED', str(exc)) from exc


def decode_sample(words: list[int]) -> dict:
    if len(words) != len(FIELDS) or any(type(value) is not int or not 0 <= value <= 0xffffffff for value in words):
        raise PraxisError('TELEMETRY_PROTOCOL', 'Malformed telemetry word count or uint32 value')
    row = dict(zip(FIELDS, words, strict=True))
    if (row['generation'] & 1 or row['magic'] != MAGIC or row['abi'] != ABI or row['size_bytes'] != SIZE):
        raise PraxisError('TELEMETRY_ABI', 'Record is uninitialized, incompatible or not coherently published')
    if row['state'] >= len(STATES) or row['failure_reason'] >= len(FAILURES) or row['flags'] & ~15:
        raise PraxisError('TELEMETRY_ABI', 'Unknown state, failure reason or flag encoding')
    return {**row, 'state_name': STATES[row['state']], 'failure_name': FAILURES[row['failure_reason']],
            'indicators': {'blue': bool(row['flags'] & 1), 'orange': bool(row['flags'] & 2),
                           'in_flight': bool(row['flags'] & 4), 'green': bool(row['flags'] & 8)}}


def assess(samples: list[dict]) -> dict:
    """Report progress/firmware outcomes; do not manufacture a physical-test pass."""
    first, last = samples[0], samples[-1]
    deltas = {name: (last[name] - first[name]) & 0xffffffff for name in
              ('uptime_ms', 'timer_irqs', 'uart_irqs', 'exti_irqs', 'frames_started',
               'frames_validated', 'rx_bytes', 'tx_bytes', 'uart_errors', 'queue_overflows')}
    # Negative discontinuities become huge unsigned deltas. Do not call them progress.
    # Check every adjacent pair: a reset in the middle can otherwise disappear
    # when the final counters have caught up with the first sample.
    plausible = all(value < 0x80000000 for value in deltas.values()) and all(
        ((b[name] - a[name]) & 0xffffffff) < 0x80000000
        for a, b in zip(samples, samples[1:], strict=False) for name in deltas)
    same_run = all(sample['run_number'] == first['run_number'] for sample in samples)
    advanced = all(0 < ((b['generation'] - a['generation']) & 0xffffffff) < 0x80000000
                   for a, b in zip(samples, samples[1:], strict=False))
    live = len(samples) > 1 and plausible and advanced and deltas['uptime_ms'] > 0 and deltas['timer_irqs'] > 0
    failure_seen = any(sample['state_name'] == 'failed' or sample['failure_reason'] != 0 for sample in samples)
    outcomes = {'fresh_progress': live, 'counter_continuity_plausible': plausible,
                'same_run': same_run, 'deltas_modulo_uint32': deltas,
                'firmware_failure_reported': failure_seen,
                'uart_progress_observed': live and same_run and not failure_seen and deltas['frames_validated'] > 0,
                'blue_success_reported': plausible and same_run and not failure_seen
                    and last['indicators']['blue'] and last['run_validated'] >= 100
                    and last['failure_reason'] == 0 and last['state_name'] != 'failed',
                'limits': 'No stimulus was generated; absent UART progress while paused is expected. '
                          'A reset can mimic rollover; no boot-unique identity is implemented. '
                          'These are firmware-reported outcomes, not independent packet capture.'}
    return outcomes


def read_telemetry_script(uid: str, image: bytes, address: int, samples: int, interval_ms: int,
                          *, contract=None, can_state: bool = False) -> str:
    contract = contract or get_contract()
    if can_state and contract.kind != 'can-loopback-v1':
        raise PraxisError('DIAGNOSTIC_UNSUPPORTED', 'Named CAN reads require the CAN telemetry contract')
    if (not isinstance(image, bytes) or not 392 <= len(image) <= MAX_IMAGE_BYTES):
        raise PraxisError('TELEMETRY_UNSUPPORTED', 'The bounded telemetry reader supports images of 392 bytes to 64 KiB')
    if (not re.fullmatch('[0-9a-f]{24}', uid) or type(address) is not int or address % 4
            or not 0x20000000 <= address <= 0x20020000 - 4096 - contract.size
            or type(samples) is not int or not 1 <= samples <= 5
            or type(interval_ms) is not int or not 10 <= interval_ms <= 1000):
        raise PraxisError('INVALID_TELEMETRY_REQUEST', 'Use 1–5 samples, 10–1000 ms spacing and a validated ABI object')
    # This fixed F407 address bound is also checked against the pinned assets.
    prefix = read_script(False, uid).split('echo "PRAXIS|state|', 1)[0].rstrip()
    commands = [prefix, 'echo PRAXIS_TELEMETRY_BEFORE', *verify_script(image, confirm_mismatch=True)]
    for index in range(samples):
        if index:
            commands.append(f'sleep {interval_ms}')
        commands += ['set coherent 0', 'set reason "publisher_busy"', 'for {set retry 0} {$retry < 4} {incr retry} {',
            f'  set before [lindex [read_memory 0x{address:08x} 32 1] 0]',
            '  if {$before & 1} { sleep 1; continue }',
            f'  set row [read_memory 0x{address:08x} 32 {len(contract.fields)}]',
            f'  set confirmation [read_memory 0x{address:08x} 32 {len(contract.fields)}]',
            f'  set after [lindex [read_memory 0x{address:08x} 32 1] 0]',
            '  set reason [format "before=%08x after=%08x row=%08x duplicate=%d" $before $after [lindex $row 0] [expr {$row eq $confirmation}]]',
            f'  if {{[llength $row] == {len(contract.fields)} && $row eq $confirmation && $before == $after && [lindex $row 0] == $before}} {{',
            '    set coherent 1', '    break', '  }', '  sleep 1', '}',
            'if {!$coherent} { error "PRAXIS_TELEMETRY_BUSY: $reason" }',
            'set encoded {}', 'foreach word $row { lappend encoded [format "%08x" $word] }',
            f'echo "PRAXIS_TELEMETRY|{index}|[join $encoded ,]"']
    if can_state:
        from praxis.can_diagnostics import script
        commands += script()
    # A second exact check brackets the samples, without halting a running core.
    commands += ['echo PRAXIS_TELEMETRY_AFTER']
    commands += [line.replace('PRAXIS_IMAGE_VERIFIED', 'PRAXIS_IMAGE_REVERIFIED') for line in verify_script(image, confirm_mismatch=True)]
    commands += ['echo "PRAXIS|state|[praxis.cpu curstate]"', 'echo PRAXIS_TELEMETRY_COMPLETE', 'shutdown']
    return '\n'.join(commands) + '\n'


def parse_samples(output: str, count: int, *, contract=None) -> list[dict]:
    contract = contract or get_contract()
    if type(count) is not int or not 1 <= count <= 5:
        raise PraxisError('INVALID_TELEMETRY_REQUEST', 'Select 1–5 samples')
    lines = output.splitlines()
    for marker in ('PRAXIS_IMAGE_VERIFIED', 'PRAXIS_IMAGE_REVERIFIED', 'PRAXIS_TELEMETRY_COMPLETE'):
        if lines.count(marker) != 1:
            raise PraxisError('TELEMETRY_PROTOCOL', 'Backend did not complete exact-image and observation checks')
    start = lines.index('PRAXIS_IMAGE_VERIFIED')
    end = lines.index('PRAXIS_IMAGE_REVERIFIED')
    complete = lines.index('PRAXIS_TELEMETRY_COMPLETE')
    positions = [i for i, line in enumerate(lines) if line.startswith('PRAXIS_TELEMETRY|')]
    if not start < end < complete or any(not start < position < end for position in positions):
        raise PraxisError('TELEMETRY_PROTOCOL', 'Samples must be bracketed by ordered exact-image checks')
    samples = []
    for line in lines:
        if not line.startswith('PRAXIS_TELEMETRY|'):
            continue
        parts = line.split('|')
        if len(parts) != 3 or parts[1] != str(len(samples)):
            raise PraxisError('TELEMETRY_PROTOCOL', 'Duplicate, malformed or out-of-order sample')
        tokens = parts[2].split(',')
        if len(tokens) != len(contract.fields) or any(not re.fullmatch('[0-9a-f]{8}', token) for token in tokens):
            raise PraxisError('TELEMETRY_PROTOCOL', 'Invalid telemetry word encoding')
        samples.append(contract.decode([int(token, 16) for token in tokens]))
    if len(samples) != count:
        raise PraxisError('TELEMETRY_PROTOCOL', 'Missing telemetry samples')
    return samples


class TelemetryService:
    def __init__(self, build, hardware, artifact_id: str, kind: str = 'uart-loopback-v1'):
        self.build, self.hardware, self.artifact_id = build, hardware, artifact_id
        self.contract = get_contract(kind)
        self.elf, self.image, self.address = self.snapshot()

    def snapshot(self):
        result = self.build.validate(self.artifact_id)
        if not result['validation']['valid']:
            raise PraxisError('IMAGE_REJECTED', 'Telemetry requires an accepted firmware image')
        data = read_inside(self.build.artifacts / self.artifact_id, 'firmware.elf', 8 * 1024 * 1024)
        if digest(data) != result['validation']['elf_sha256']:
            raise PraxisError('INTEGRITY_ERROR', 'ELF changed during validated snapshot')
        return data, image_from_elf(data, self.build.assets), telemetry_address(
            data, self.build.assets.ram, contract=self.contract)

    def describe(self):
        c = self.contract
        return {'enabled': True, 'artifact_id': self.artifact_id, 'symbol': c.symbol,
                'kind': c.kind, 'abi': c.abi, 'record_bytes': c.size,
                'fields': list(c.fields), 'limits': LIMITS}

    def read_can_diagnostics(self, connection_id: str) -> dict:
        from praxis.can_diagnostics import validate_bundle
        if self.contract.kind != 'can-loopback-v1':
            raise PraxisError('DIAGNOSTIC_UNSUPPORTED', 'Select the CAN telemetry contract')
        validate_bundle(self.build.bundle)
        return self.read(connection_id, 1, 100, can_state=True)

    def read(self, connection_id: str, samples: int = 2, interval_ms: int = 100,
             *, can_state: bool = False) -> dict:
        if connection_id not in self.hardware.connections:
            raise PraxisError('UNKNOWN_CONNECTION', 'Call inspect_target first in this process')
        serial, uid = self.hardware.connections[connection_id]
        # Revalidate persistent bytes, even though launch selected a fixed artifact.
        data, image, address = self.snapshot()
        if data != self.elf or address != self.address:
            raise PraxisError('INTEGRITY_ERROR', 'Telemetry artifact changed since launch')
        script = read_telemetry_script(uid, image.data, address, samples, interval_ms,
                                       contract=self.contract, can_state=can_state)
        probe = self.hardware.select(serial)
        with self.hardware.probe_lock(serial):
            self.hardware.verify_backend()
            with tempfile.TemporaryDirectory(prefix='praxis-telemetry-') as directory:
                root = Path(directory)
                (root / 'attach.cfg').write_text(configuration(serial, probe['product_id']))
                (root / 'read.tcl').write_text(script)
                result = bounded([str(self.hardware.backend), '-f', str(root / 'attach.cfg'),
                                  '-f', str(root / 'read.tcl')], 15, cwd=root)
        if result['failure']:
            raise PraxisError(result['failure'], 'Telemetry stopped; no halt/reset/write fallback attempted')
        if result['returncode']:
            code = next((code for marker, code in [('PRAXIS_TARGET_CHANGED', 'TARGET_CHANGED'),
                ('PRAXIS_TARGET_MISMATCH', 'TARGET_MISMATCH'), ('PRAXIS_READBACK_MISMATCH', 'READBACK_MISMATCH'),
                ('PRAXIS_TELEMETRY_BUSY', 'TELEMETRY_BUSY')] if marker in result['diagnostics']), 'TELEMETRY_BACKEND_FAILED')
            if code in {'TARGET_CHANGED', 'TARGET_MISMATCH'}:
                self.hardware.connections.pop(connection_id, None)
            detail = re.search(r'PRAXIS_READBACK_MISMATCH: address=0x[0-9a-f]{8} actual=0x[0-9a-f]{8} expected=0x[0-9a-f]{8} scalar=0x[0-9a-f]{8}', result['diagnostics'])
            if code == 'TELEMETRY_BUSY':
                detail = re.search(r'PRAXIS_TELEMETRY_BUSY: (?:publisher_busy|before=[0-9a-f]{8} after=[0-9a-f]{8} row=[0-9a-f]{8} duplicate=[01])', result['diagnostics'])
            context = ('; ' + detail[0].split(': ', 1)[1]) if detail else ''
            phase = 'after' if 'PRAXIS_TELEMETRY_AFTER' in result['diagnostics'] else 'before'
            location = f'{phase} sampling image check' if code == 'READBACK_MISMATCH' else 'bounded observation'
            raise PraxisError(code, f'Telemetry unavailable during {location}{context}; verify target/image; no write requested')
        values = parse_observation(result['diagnostics'], False)
        if check_target(values)['uid'] != uid:
            self.hardware.connections.pop(connection_id, None)
            raise PraxisError('TARGET_CHANGED', 'Returned MCU identity differs from preflight')
        rows = parse_samples(result['diagnostics'], samples, contract=self.contract)
        extra = {}
        if can_state:
            from praxis.can_diagnostics import parse
            extra['can_state'] = parse(result['diagnostics'])
        return {**extra, 'run_id': uuid.uuid4().hex, 'observed_at': datetime.now(UTC).isoformat(),
                'artifact_id': self.artifact_id, 'elf_sha256': digest(data),
                'image_sha256': digest(image.data), 'readback_verified_before_and_after': True,
                'flash_word_rechecks': len(re.findall(r'^PRAXIS_FLASH_WORD_RECHECK\|0x[0-9a-f]{8}$', result['diagnostics'], re.MULTILINE)),
                'read_strategy': 'Block comparison; mismatches require two matching individual reads. Duplicate coherent SRAM records.',
                'bundle_revision': self.build.bundle.manifest.bundle_revision,
                'hardware_profile_revision': self.hardware.profile.profile_revision,
                'symbol': self.contract.symbol, 'kind': self.contract.kind,
                'abi': self.contract.abi, 'record_bytes': self.contract.size,
                'execution_state': values['state'], 'samples': rows,
                'assessment': self.contract.assess(rows),
                'requested_sample_spacing_ms': interval_ms, 'limits': LIMITS}
