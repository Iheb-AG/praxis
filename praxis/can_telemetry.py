"""CAN example software ABI and offline qualification; never accesses hardware.

Register interpretations mirror the reviewed CAN1 loopback contract, not a
general CAN decoder. All result labels are recomputed from raw uint32 words.
"""
from __future__ import annotations

import re

from praxis.errors import PraxisError

KIND = 'can-loopback-v1'
SYMBOL = 'praxis_can_telemetry'
MAGIC = 0x50524331
ABI = 1
FIELDS = ('generation', 'magic', 'abi', 'size_bytes', 'publications', 'phase',
          'status', 'flags', 'clock_step', 'irq_count', 'rx_words_read_mask',
          'rx_identifier', 'rx_length', 'rx_low', 'rx_high', 'last_esr',
          'last_tsr', 'last_rf0', 'expected_identifier', 'expected_low',
          'expected_high', 'end_ier', 'end_irq_enabled')
SIZE = len(FIELDS) * 4
PHASES = ('boot', 'passed', 'failed')
STATUSES = ('ok', 'invalid', 'state', 'init_timeout', 'error', 'filter',
            'tx_error', 'rx_error', 'timeout', 'release_timeout', 'irq_error')
IDENTIFIER = 0x123 << 21
PAYLOAD_LOW, PAYLOAD_HIGH = 0x58415250, 0xFF005349
DIGEST = re.compile(r'^[0-9a-f]{64}$')
LIMITS = [
    'Qualifies firmware self-reports; no independent CAN wire capture or timing measurement.',
    'Internal silent loopback does not qualify GPIO routes, a transceiver or an external CAN bus.',
    'Publication progress is a software heartbeat, not a timer or oscillator measurement.',
    'Image checks in recorded observations are reported evidence, not re-executed offline.',
    'No boot-unique identity: reset versus rollover cannot always be distinguished.',
    'A passing window does not establish repeatability or arbitrary firmware correctness.',
]


def decode_sample(words: list[int]) -> dict:
    if (len(words) != len(FIELDS) or
            any(type(v) is not int or not 0 <= v <= 0xffffffff for v in words)):
        raise PraxisError('TELEMETRY_PROTOCOL', 'Malformed CAN telemetry word count or uint32')
    row = dict(zip(FIELDS, words, strict=True))
    if (row['generation'] & 1 or row['magic'] != MAGIC or row['abi'] != ABI or
            row['size_bytes'] != SIZE or row['phase'] >= len(PHASES) or
            row['status'] >= len(STATUSES) or row['flags'] & ~255 or
            row['rx_words_read_mask'] & ~15 or row['clock_step'] > 24):
        raise PraxisError('TELEMETRY_ABI', 'Uninitialized, torn or incompatible CAN record')
    return {**row, 'phase_name': PHASES[row['phase']], 'status_name': STATUSES[row['status']]}


def success_checks(row: dict) -> dict[str, bool]:
    """Same fixed ID/payload and pre-ack diagnostic conditions as the example."""
    return {
        'passed_status': row['phase'] == 1 and row['status'] == 0,
        'clock_and_cleanup_flags': row['flags'] == 255 and row['clock_step'] == 24,
        'interrupt_receipt': row['irq_count'] >= 1 and row['rx_words_read_mask'] == 15,
        'fixed_request': (row['expected_identifier'] == IDENTIFIER and
                          row['expected_low'] == PAYLOAD_LOW and
                          row['expected_high'] == PAYLOAD_HIGH),
        'received_frame': (row['rx_identifier'] == IDENTIFIER and
                           row['rx_length'] & 0xff == 8 and
                           (row['rx_length'] >> 8) & 0xff <= 1 and
                           row['rx_low'] == PAYLOAD_LOW and row['rx_high'] == PAYLOAD_HIGH),
        # RM0090 CAN1: RQCP0/TXOK0/TME0 are required before successful W1C ack.
        'tx_completed': row['last_tsr'] & 0x04000003 == 0x04000003,
        'no_saved_errors': (row['last_esr'] == 0 and row['last_rf0'] == 0 and
                            row['last_tsr'] & 0xC == 0),
        'source_and_line_disabled': row['end_ier'] == 0 and row['end_irq_enabled'] & (1 << 20) == 0,
    }


def assess(samples: list[dict]) -> dict:
    if not samples:
        raise PraxisError('INVALID_OBSERVATION', 'Select at least one CAN sample')
    # Decode again: caller-provided labels and earlier assessments have no authority.
    rows = [decode_sample([s[name] for name in FIELDS]) for s in samples]
    pairs = list(zip(rows, rows[1:], strict=False))
    fresh = bool(pairs) and all(
        0 < ((b['publications'] - a['publications']) & 0xffffffff) < 0x40000000
        and ((b['generation'] - a['generation']) & 0xffffffff)
        == 2 * ((b['publications'] - a['publications']) & 0xffffffff)
        for a, b in pairs)
    terminal_fields = tuple(k for k in FIELDS if k not in ('generation', 'publications'))
    stable = all(all(s[k] == rows[0][k] for k in terminal_fields) for s in rows)
    checks = {name: all(success_checks(s)[name] for s in rows)
              for name in success_checks(rows[0])}
    return {'fresh_publication_progress': fresh, 'terminal_result_stable': stable,
            'sample_checks': checks,
            'firmware_failure_reported': any(s['phase'] == 2 or s['status'] != 0 for s in rows),
            'loopback_success_reported': fresh and stable and all(checks.values()),
            'limits': LIMITS}


def qualify_windows(observations: list[dict], *, artifact_id: str,
                    bundle_revision: str, expected: str = 'passed') -> dict:
    if (not isinstance(artifact_id, str) or not DIGEST.fullmatch(artifact_id) or
            not isinstance(bundle_revision, str) or not DIGEST.fullmatch(bundle_revision) or
            expected not in ('passed', 'failed') or not isinstance(observations, list) or
            not 1 <= len(observations) <= 20):
        raise PraxisError('INVALID_QUALIFICATION', 'Select exact hashes and 1–20 CAN windows')
    windows, all_rows, identities = [], [], set()
    for observation in observations:
        if not isinstance(observation, dict):
            raise PraxisError('INVALID_OBSERVATION', 'Expected a CAN observation object')
        raw = observation.get('samples')
        if (not isinstance(raw, list) or not 2 <= len(raw) <= 5 or
                any(not isinstance(s, dict) or not set(FIELDS) <= s.keys() for s in raw)):
            raise PraxisError('INVALID_OBSERVATION', 'Select 2–5 complete CAN samples per window')
        rows = [decode_sample([s[k] for k in FIELDS]) for s in raw]
        summary = assess(rows)
        identity_ok = all(isinstance(observation.get(k), str) and
                          DIGEST.fullmatch(observation[k]) for k in ('image_sha256', 'elf_sha256'))
        checks = {
            'artifact_matches': observation.get('artifact_id') == artifact_id,
            'bundle_matches': observation.get('bundle_revision') == bundle_revision,
            'abi_matches': (observation.get('kind') == KIND and observation.get('symbol') == SYMBOL
                            and type(observation.get('abi')) is int and observation['abi'] == ABI
                            and type(observation.get('record_bytes')) is int
                            and observation['record_bytes'] == SIZE),
            'image_identity_present': bool(identity_ok),
            'image_checks_reported': observation.get('readback_verified_before_and_after') is True,
            'cpu_running_reported': observation.get('execution_state') == 'running',
            'fresh_publication_progress': summary['fresh_publication_progress'],
            'terminal_result_stable': summary['terminal_result_stable'],
        }
        if expected == 'passed':
            checks.update(summary['sample_checks'])
        else:
            checks['failed_status'] = all(s['phase'] == 2 and s['status'] != 0 for s in rows)
        windows.append({'passed': all(checks.values()), 'checks': checks,
                        'failures': sorted(k for k, v in checks.items() if not v),
                        'sample_count': len(rows), 'assessment': summary})
        all_rows.extend(rows)
        # Only validated strings enter the identity set; malformed JSON types cannot crash it.
        identities.add((observation['image_sha256'], observation['elf_sha256']) if identity_ok
                       else (None, None))
    combined = assess(all_rows)
    return {'format': 'praxis-can-qualification-v1', 'expected': expected,
            'artifact_id': artifact_id, 'bundle_revision': bundle_revision,
            'passed': (all(w['passed'] for w in windows) and len(identities) == 1
                       and combined['fresh_publication_progress'] and combined['terminal_result_stable']),
            'same_image': len(identities) == 1, 'windows': windows,
            'ordered_publication_progress': combined['fresh_publication_progress'],
            'terminal_result_stable': combined['terminal_result_stable'],
            'repeatability_qualified': False, 'mutating_operations': 0, 'limits': LIMITS}
