"""Source-scoped STM32/ARM core knowledge and actual controller effect tests."""
import copy
import json
import shutil
import subprocess

import pytest
from pydantic import ValidationError

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.coverage import workflow_coverage
from praxis.definitions import load_definitions
from praxis.errors import PraxisError
from praxis.models import Profile, Register
from praxis.routing import Session

APPLICATION = ROOT / 'examples/stm32f407g-disc1-arm-core/application'
BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-arm-core-v2'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    binary = tmp_path_factory.mktemp('arm-core-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
        str(ROOT / 'tests/fixtures/f407_arm_core_model.c'), '-o', str(binary)],
        check=True, capture_output=True, timeout=30)
    return binary


def run(model, *arguments):
    result = subprocess.run([str(model), *(str(v) for v in arguments)], check=True,
                            capture_output=True, timeout=5, text=True)
    data = json.loads(result.stdout)
    if 'violation' in data:
        assert not data['violation']
        assert data['reads'] < 65 and data['writes'] < 15
        assert data['icsr'] & 0x90000000 == 0x90000000  # NMI/PendSV pending preserved.
    return data


def test_irq_enable_follows_vector_priority_reload_clear_and_barriers(model):
    data = run(model, 0)
    assert data['status'] == 0 and data['stopped']
    assert data['load'] == 15999 and data['val'] == 0
    assert data['enabled_control'] == 7 and data['control'] == 0
    assert data['vector'] == 0x08000000 and data['priority'] == 0xF0
    assert data['enables'] == 1 and data['barriers'] >= 4
    assert data['quiet'] and not data['failed'] and not data['icsr'] & (1 << 26)


@pytest.mark.parametrize('fault,status', [
    (1,1),(2,2),(3,2),(4,3),(5,3),(6,3),(7,4),(8,5),(9,5),(10,5),(11,5),
    (19,1),(20,1),(21,1),(29,1),(30,1),(31,1),(32,9),(33,4),(34,8),(35,4),
    (37,4),(38,3),(39,4),
])
def test_rejected_context_clock_period_owner_or_vector_never_writes(model, fault, status):
    data = run(model, fault)
    assert data['status'] == status and data['writes'] == 0 and not data['enables']
    if fault in (1,19,20,21,29,30,31,32,33,34,35):
        assert data['reads'] == 0


@pytest.mark.parametrize('fault,status,quiet', [
    (12,5,False),(13,6,False),(14,6,True),(15,6,True),
    (16,6,False),(17,6,True),(18,6,False),
])
def test_write_failures_latch_failure_and_report_cleanup_without_retry(model, fault, status, quiet):
    data = run(model, fault)
    assert data['status'] == status and data['failed'] and data['retry_blocked']
    assert bool(data['quiet']) is quiet
    if fault != 17:
        assert not data['enables']


def test_polling_consumes_stale_flag_and_requires_a_later_event(model):
    good = run(model, 22)
    assert good['status'] == good['wait'] == 0 and good['poll_reads'] == 3
    assert good['enabled_control'] == 5 and good['stopped']
    assert good['priority_writes'] == good['vector_writes'] == 0
    stale = run(model, 23)
    assert stale['wait'] == 7 and stale['poll_reads'] == 6  # Drain + four attempts + shutdown readback.
    assert stale['failed'] and stale['retry_blocked'] and stale['quiet']
    assert stale['control'] == 0


@pytest.mark.parametrize('fault,expected', [(24,6),(25,1),(26,8),(36,2)])
def test_polling_requires_its_own_configuration_context_and_finite_budget(model, fault, expected):
    data = run(model, fault)
    assert data['status'] == 0 and data['wait'] == expected
    if fault in (25,26,36):
        assert data['poll_reads'] == 0
    else:
        assert data['failed'] and data['retry_blocked']


@pytest.mark.parametrize('fault', [27,28])
def test_shutdown_readback_failure_is_not_reported_as_success(model, fault):
    data = run(model, fault)
    assert data['status'] == 0 and not data['stopped']
    assert data['failed'] and data['retry_blocked'] and not data['quiet']


@pytest.mark.parametrize('clock,tick,reload', [
    (16000000,1000,15999),(168000000,1000,167999),(2,1,1),(16777216,1,0xFFFFFF),
    (0,1000,None),(16000000,0,None),(1,1,None),(16000000,3,None),
    (16777217,1,None),(0xFFFFFFFF,1,None),
])
def test_integer_period_bounds_and_no_rounding(model, clock, tick, reload):
    data = run(model, 'period', clock, tick)
    assert bool(data['ok']) == (reload is not None)
    assert data['reload'] == (reload if reload is not None else 0xDEADBEEF)


def test_new_bundle_exposes_exact_core_contracts_without_uart_gate():
    bundle = Bundle(BUNDLE)
    session = Session(bundle)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='retrieve in order: rcc, scb'):
        session.read_peripheral_doc('systick')
    for name in ('rcc','scb','systick'):
        session.read_peripheral_doc(name)
    assert not {'usart','nvic'} & session.served
    scb = bundle.read('wiki/peripherals/scb.md')
    tick = bundle.read('wiki/peripherals/systick.md')
    assert 'Reviewed write-value mask' in scb and '0x3FFFFE00' in scb
    assert 'PENDSTSET=0' in tick and 'All four reset values remain unasserted' in tick
    assert 'core_clock_interrupt' in tick and 'flash_vector_table' in scb
    assert all("## Register map" in bundle.read(path) and "## Bit fields" in bundle.read(path)
               for path in bundle.manifest.peripherals.values())


def test_dependency_modes_and_conflicting_reset_values_remain_explicit():
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-arm-core-v2.json').read_bytes())
    records = load_definitions(profile, {s.id:source/s.path for s in profile.sources})
    by_id = {r.id:r for r in records}
    assert all(reg.reset is None for reg in by_id['systick'].registers)
    assert by_id['scb'].registers[1].write_mask == 0x3FFFFE00
    report = workflow_coverage(profile, records, {}, Session(Bundle(BUNDLE)).netlist)
    assert report['systick_1khz_interrupt']['ready'] and report['systick_core_polling']['ready']
    assert 'systick/quiescent_owned' in report['systick_1khz_interrupt']['mode_order']
    broken = [r.model_copy(update={'operating_modes': {}}) if r.id=='scb' else r for r in records]
    with pytest.raises(PraxisError, match='required mode scb/systick_exception_setup is not published'):
        workflow_coverage(profile, broken, {}, Session(Bundle(BUNDLE)).netlist)


@pytest.mark.parametrize('change', ['too_wide','outside_fields','unknown','readonly'])
def test_reviewed_write_mask_rejects_unsupported_values(change):
    source = ROOT / 'sources/stm32f407g-disc1/reviewed/arm-core-v2/extension.json'
    r = copy.deepcopy(json.loads(source.read_text())['additions'][1]['registers'][0])
    if change == 'too_wide':
        r['write_mask'] = 1 << 32
    if change == 'outside_fields':
        r['write_mask'] = 1 << 20
    if change == 'unknown':
        r['access'] = 'unknown'
    if change == 'readonly':
        r['access'] = 'RO'
    with pytest.raises(ValidationError):
        Register.model_validate(r)


def test_first_local_core_revision_is_blocked_for_its_missing_pending_guard():
    session = Session(Bundle(ROOT/'bundles/stm32f407g-disc1-e01-arm-core-v1'))
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='PRAXIS-2026-002'):
        session.read_peripheral_doc('systick')


def test_header_only_provenance_cannot_publish_a_reviewed_write_mask(tmp_path):
    from praxis.compiler import _definitions
    source = tmp_path / 'source'
    shutil.copytree(ROOT / 'sources/synthetic-cortex-m3', source)
    data = json.loads((source / 'profile.json').read_text())
    (source / 'reviewed/clock.md').write_text('Synthetic editorial fixture; no manufactured hardware.\n')
    data['sources'].append(dict(id='narrative', path='reviewed/clock.md', authority='semantics',
        version='test', license='MIT', origin='Synthetic review fixture'))
    ref = dict(source='header', locator='CLK_CTRL_ENABLE_MASK')
    records = [dict(id='clock', title='Synthetic clock', prerequisites=[],
        instances=[dict(name='CLOCK0', base_address=0x40000000, bus='synthetic', clock='synthetic',
                        sources=[dict(source='header', locator='CLOCK0_BASE')])],
        registers=[dict(name='CTRL', offset=0, width=32, access='RW', access_widths=[32],
            write_mask=1, side_effects='Synthetic reviewed subset', sources=[ref],
            fields=[dict(name='ENABLE', lsb=0, width=1, mask=1, meaning='Synthetic flag', sources=[ref])])],
        reviewed_markdown='reviewed/clock.md',
        review=dict(status='reviewed', reviewer='Synthetic fixture author', basis='Schema test only'))]
    (source / 'reviewed/peripherals.json').write_text(json.dumps(records))
    profile = Profile.model_validate(data)
    paths = {s.id:source/s.path for s in profile.sources}
    with pytest.raises(PraxisError, match='reviewed write masks require semantic evidence'):
        _definitions(profile, paths, source)
    records[0]['registers'][0]['sources'].append(dict(source='narrative', locator='synthetic_policy'))
    (source / 'reviewed/peripherals.json').write_text(json.dumps(records))
    assert _definitions(profile, paths, source)[0].registers[0].write_mask == 1
