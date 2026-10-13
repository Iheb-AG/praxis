"""Synthetic authoring evidence: no vendor operating facts are certified here."""
import copy
import json

import pytest
from pydantic import ValidationError

from praxis.adapters.discovery import Declaration
from praxis.adapters.manual import canonical, number, prepare
from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.models import ManualSpec, PeripheralDiscovery, Register


@pytest.fixture
def declaration():
    return Declaration(structure='TEST_Type', instances={'TEST0': 0x40000000},
        registers=[Register(name='CR', offset=4, width=32, reset=0, access='unknown',
            side_effects='Synthetic declaration; no operating review.', sources=[dict(source='header', locator='CR')],
            fields=[dict(name='ENABLE', lsb=0, width=1, mask=1, meaning='Synthetic declaration',
                sources=[dict(source='header', locator='TEST_CR_ENABLE_Msk')])])],
        members={'CR': 'CR'}, field_expressions={'CR.ENABLE': 'TEST_CR_ENABLE_Msk'})


def part(page, text='', rows=None):
    return dict(locator=f'page:{page}', page=page, text=text,
        artifact=f'extracted/part-{page:04}.json', artifact_sha256=digest(text.encode()),
        tables=[] if rows is None else [dict(locator=f'page:{page}/table:1', rows=rows)])


def packet(declaration, parts, **kwargs):
    return prepare(declaration, parts, entity='test', target={'mcu': 'SYNTHETIC'},
        source={'id': 'manual', 'source_sha256': 'a' * 64}, **kwargs)


def test_candidates_have_provenance_but_never_publish(declaration):
    result = packet(declaration, [part(1, '''Control (TEST_CR)
Address offset: 0x04
Reset value: 0x0000 0000
Access: read/write
Bit 0 ENABLE: This bit must be set before use.
''')])
    assert result['counts']['candidates'] == 4
    assert result['gaps']['CR'] == {'missing_categories': [], 'missing_field_positions': []}
    assert all(f['locators'] and f['review_required'] for f in result['candidates'])
    assert result['review_required'] and not result['publication_ready']
    assert result['status'] == 'pending-review' and not result['conflicts']
    assert result['review_hints'][0]['locator'] == 'page:1/line:5'
    assert result['evidence_parts'][0]['artifact_sha256']
    check = dict(result)
    checksum = check.pop('packet_sha256')
    assert digest(canonical(check)) == checksum


def test_page_order_continuation_gaps_and_other_registers(declaration):
    parts = [part(10, 'Reset value: 0'), part(9, 'Control (TEST_CR)\nAddress offset: 4'),
             part(12, 'Access: RW'), part(11, 'Other control (OTHER_CR)\nAccess: RO')]
    result = packet(declaration, parts)
    assert {f['kind'] for f in result['candidates']} == {'offset', 'reset'}
    assert canonical(result) == canonical(packet(declaration, list(reversed(parts))))
    gap = packet(declaration, [parts[1], parts[0], part(12, 'Bit 0 ENABLE: must enable')])
    assert 'ENABLE' in gap['gaps']['CR']['missing_field_positions']


def test_numeric_and_header_conflicts_remain_visible(declaration):
    result = packet(declaration, [part(1, '''Control (TEST_CR)
Address offset: 4
Bit 1 ENABLE: Enable.
Reset value: 0 (system reset only)
'''), part(2, 'Address offset: 8\nReset value: 0x1 + 0x2\nBits 31:32 ENABLE: invalid')])
    assert {(f['kind'], f['field']) for f in result['conflicts']} == {('offset', None), ('field', 'ENABLE')}
    offsets = [f for f in result['candidates'] if f['kind'] == 'offset']
    assert len(offsets) == 2 and all(f['status'] == 'conflict' for f in offsets)
    reset = next(f for f in result['candidates'] if f['kind'] == 'reset')
    assert reset['qualifier'] == '(system reset only)' and reset['status'] == 'unreviewed'
    assert {i['code'] for i in result['extraction_issues']} == {'UNSUPPORTED_VALUE', 'FIELD_RANGE'}


def test_exact_table_identity_and_explicit_scope(declaration):
    rows = [['Register', 'Offset', 'Reset', 'Access', 'Field', 'Bits'],
            ['CR', '4', '0', 'RW', 'ENABLE', '0'],
            ['TEST_CR', '4', '0', 'RW', 'ENABLE', '0'],
            ['TEST_CR_EXTRA', '8', '1', 'RO', 'ENABLE', '1']]
    evidence = part(3, rows=rows)
    original = copy.deepcopy(evidence)
    unscoped = packet(declaration, [evidence])
    assert unscoped['counts']['candidates'] == 4
    assert unscoped['extraction_issues'][0]['code'] == 'UNSCOPED_TABLE'
    scoped = packet(declaration, [evidence], spec=ManualSpec(table_scopes={'page:3/table:1': 'test'}))
    assert not scoped['extraction_issues']
    assert all(len(f['locators']) == 2 for f in scoped['candidates'])
    assert scoped['evidence_parts'][0]['table_locators'] == ['page:3/table:1']
    assert evidence == original  # Whole source table is never rewritten or sliced.


def test_synthetic_vendor_vocabulary_and_symbols(declaration):
    spec = ManualSpec(register_symbols={'test': {'CR': ['TST_CTRL']}}, labels={
        'register': ['Symbol'], 'offset': ['Displacement'], 'reset': ['Initial value'],
        'access': ['Permission'], 'field': ['Name'], 'bits': ['Position']})
    rows = [['Symbol', 'Displacement', 'Initial value', 'Permission', 'Name', 'Position'],
            ['TST_CTRL', '0x04', '0', 'RO', 'ENABLE', '0']]
    result = packet(declaration, [part(1, 'Configuration (TST_CTRL)\nDisplacement: 4', rows)], spec=spec)
    assert result['counts']['candidates'] == 4
    assert result['register_symbols'] == {'TST_CTRL': 'CR'}
    assert result['parser_config_sha256'] != packet(declaration, [])['parser_config_sha256']
    assert not packet(declaration, [part(1, 'Control (TEST_CR)\nOffset: 4')], spec=spec)['candidates']


@pytest.mark.parametrize('value,expected', [('0x0000 0010', (16, '')), ('16', (16, '')),
    ('0X10 (power reset)', (16, '(power reset)')), ('0x0/0x1', None), ('-1', None),
    ('0x100000000', None), ('0x0 (unfinished', None), ('9' * 5000, None)])
def test_restricted_numbers(value, expected):
    assert number(value) == expected


@pytest.mark.parametrize('registers', [[], ['UNKNOWN'], ['CR', 'CR']])
def test_invalid_register_selections(declaration, registers):
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        packet(declaration, [], registers=registers)


def test_symbol_config_and_vocabulary_rejected(declaration):
    with pytest.raises(ValidationError):
        ManualSpec(labels={'offset': ['Offset'], 'reset': [' offset ']})
    with pytest.raises(ValidationError):
        ManualSpec(register_symbols={'test': {'CR': ['evil()']}})
    with pytest.raises(PraxisError, match='INVALID_MANUAL_CONFIG'):
        packet(declaration, [], spec=ManualSpec(register_symbols={'test': {'MISSING': ['TEST_BAD']}}))
    declaration.registers.append(declaration.registers[0].model_copy(update={'name': 'OTHER', 'offset': 8}))
    with pytest.raises(PraxisError, match='AMBIGUOUS_MANUAL_SYMBOL'):
        packet(declaration, [], spec=ManualSpec(register_symbols={'test': {'CR': ['SAME'], 'OTHER': ['SAME']}}))


def test_no_silent_truncation_or_duplicate_parts(declaration, monkeypatch):
    evidence = part(1, 'Control (TEST_CR)\nOffset: 4')
    with pytest.raises(PraxisError, match='IMPORT_INTEGRITY'):
        packet(declaration, [evidence, evidence])
    with pytest.raises(PraxisError, match='REVIEW_LIMIT'):
        packet(declaration, [part(1, 'x' * 4097)])
    import praxis.adapters.manual as adapter
    monkeypatch.setattr(adapter, 'MAX_PACKET', 100)
    with pytest.raises(PraxisError, match='REVIEW_LIMIT'):
        packet(declaration, [evidence])


def test_cli_review_packets_not_reviewed_peripherals(declaration):
    from praxis.models import Peripheral
    result = packet(declaration, [part(1, 'Control (TEST_CR)\nOffset: 4')])
    with pytest.raises(ValidationError):
        Peripheral.model_validate(result)
    assert json.loads(canonical(result))['publication_ready'] is False


def test_configured_register_prefix(declaration):
    spec = PeripheralDiscovery(structure='TEST_Type', prefix='ALT', register_prefixes={'CR': 'ALT_CTRL'})
    result = packet(declaration, [part(1, 'Control (ALT_CTRL)\nOffset: 4')], discovery=spec)
    assert result['candidates'][0]['value'] == 4


def test_mode_qualified_and_wrapped_headings_end_prior_context(declaration):
    declaration.registers.append(declaration.registers[0].model_copy(update={'name': 'OTHER', 'offset': 8}))
    result = packet(declaration, [part(1, '''1.2.1 Control (TEST_CR) (only in test mode)
Address offset: 4
Bit 0 ENABLE bit
1.2.2 Other register (TEST_OTHER) (not used in special
mode)
Address offset: 8
1.2.3 Unrecognized register
(UNKNOWN)
Reset value: 123
''')])
    offsets = {f['register']: f['value'] for f in result['candidates'] if f['kind'] == 'offset'}
    assert offsets == {'CR': 4, 'OTHER': 8} and not result['conflicts']
    assert not any(f['kind'] == 'reset' for f in result['candidates'])
    field = next(f for f in result['candidates'] if f['kind'] == 'field')
    assert 'only in test mode' in field['section_contexts'][0]


def test_explicit_complete_part_selection_never_guesses_applicability(declaration):
    parts = [part(1, '1.1 Control (TEST_CR)\nOffset: 4'),
             part(2, '2.1 Control (TEST_CR)\nOffset: 8')]
    assert packet(declaration, parts)['conflicts']
    selected = packet(declaration, parts, locators=['page:1'])
    assert not selected['conflicts'] and selected['selected_evidence_locators'] == ['page:1']
    assert selected['counts']['parts_examined'] == 1
    for invalid in ([], ['page:0'], ['page:1', 'page:1'], ['../manual']):
        with pytest.raises(PraxisError, match='UNKNOWN_LOCATOR'):
            packet(declaration, parts, locators=invalid)
