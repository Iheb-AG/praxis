"""Source-scoped DAC knowledge, shared MMIO controller and retained ARM integration."""
import json
import subprocess

import pytest

from conftest import ROOT, require_image, require_tool
from praxis.bundle import Bundle
from praxis.coverage import workflow_coverage
from praxis.definitions import load_definitions
from praxis.errors import PraxisError
from praxis.models import Profile
from praxis.routing import Session

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-dac-v1'
APPLICATION = ROOT / 'examples/stm32f407g-disc1-dac/application'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    binary = tmp_path_factory.mktemp('dac-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
        str(ROOT / 'tests/fixtures/f407_dac_model.c'), '-o', str(binary)],
        check=True, capture_output=True, timeout=30)
    return binary


def run(model, fault=0):
    result = subprocess.run([str(model), str(fault)], check=True,
                            capture_output=True, timeout=5, text=True)
    record = json.loads(result.stdout)
    assert not record['violation']  # No WO reads, RO writes, flag erasure or trigger reordering.
    assert record['calls'] < 100 and record['timer_attempts'] < 10
    assert not record['analog']  # A model/DOR match never proves voltage or settling.
    return record


def test_transfer_requires_two_fresh_intervals_and_reports_only_digital_completion(model):
    result = run(model)
    assert result['configured'] and result['status'] == 0 and result['loaded']
    assert result['code'] == 2048 and result['waits'] == 2
    assert result['triggers'] == result['transfers'] == result['dor_reads'] == 1
    assert result['timer_attempts'] == 4
    assert result['owned'] and not result['reset_required'] and not result['cleaned']


@pytest.mark.parametrize('fault,status', [(1, 1), (2, 1), (3, 3), (27, 1)])
def test_invalid_input_and_unreviewed_output_never_enable_or_trigger(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and not result['triggers'] and not result['waits']
    assert not result['owned'] and result['writes'] == result['config_writes']


@pytest.mark.parametrize('fault', [4, 5, 6, 8])
def test_wrong_clock_reset_existing_channel_or_error_reject_configuration(model, fault):
    result = run(model, fault)
    assert not result['configured'] and not result['config_writes']
    assert result['status'] == 2 and result['reset_required'] and result['retry_blocked']
    assert not result['triggers'] and not result['waits']
    if fault == 6:
        assert result['cr'] == 0x10000  # Preserve channel2 owner.
    if fault == 8:
        assert result['sr'] == 0x2000  # Preserve diagnostic, no W1C write.


@pytest.mark.parametrize('fault,status', [
    (9, 4), (10, 4), (11, 7), (12, 5), (13, 5), (14, 5), (15, 5),
    (16, 6), (17, 6), (18, 7), (20, 4), (24, 6), (26, 4), (28, 6), (29, 5),
])
def test_failures_latch_reset_and_do_not_swallow_error_or_overwrite_an_owner(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and not result['loaded']
    assert result['reset_required'] and result['retry_blocked']
    if fault in [13, 14, 15]:
        assert result['sr'] == 0x2000 and result['cleaned']
    if fault == 29:
        assert result['sr'] == 0x20000000 and result['cleaned']
    if fault in [16, 24, 28]:
        assert not result['cleaned']
        assert result['cr'] == {16: 0x1003D, 24: 0x3E, 28: 0x3F}[fault]
    if fault in [9, 13, 16, 17, 24, 26, 28]:
        assert not result['triggers']


def test_old_matching_output_cannot_replace_a_fresh_trigger_and_delay(model):
    result = run(model, 19)
    assert result['status'] == 0 and result['loaded']
    assert result['triggers'] == 1 and result['waits'] == 2
    failed = run(model, 20)
    assert failed['status'] == 4 and not failed['loaded'] and not failed['dor_reads']


def test_repeated_call_cannot_retake_a_held_output(model):
    result = run(model, 21)
    assert result['status'] == 0 and result['owned'] and result['retry_blocked']
    assert result['triggers'] == 1 and result['waits'] == 2


@pytest.mark.parametrize('fault,stopped,cr', [(22, True, 0x3C), (23, False, 0x3D)])
def test_shutdown_requires_acknowledgement_and_reset_before_reuse(model, fault, stopped, cr):
    result = run(model, fault)
    assert result['status'] == 0 and result['reset_required']
    assert result['stopped'] == stopped and result['cr'] == cr
    assert result['owned'] != stopped


@pytest.mark.parametrize('fault', [7, 25])
def test_lost_configuration_or_failed_reconfiguration_cannot_reuse_old_contract(model, fault):
    result = run(model, fault)
    assert not result['configured'] and result['config_writes'] == 1
    assert result['status'] == 2 and result['reset_required'] and result['retry_blocked']
    assert not result['triggers'] and not result['waits']


def test_bundle_preserves_complete_tables_source_qualifiers_and_prior_modes():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    assert coverage['peripherals']['dac']['registers'] == 14
    assert coverage['peripherals']['dac']['fields'] == 34
    for workflow in ['dac_channel1_software_trigger', 'i2c1_controller_transmit',
                     'adc1_internal_reference', 'uart_timer_interrupts']:
        assert coverage['workflows'][workflow]['ready']
    for workflow in ['feature_dac', 'dac_channel1_wired_output']:
        assert not coverage['workflows'][workflow]['ready']
    text = bundle.read('wiki/peripherals/dac.md')
    assert '| SWTRIGR | 0x004 | 32 | — | WO |' in text
    assert '| DOR1 | 0x02C | 32 | — | RO |' in text
    assert '10-bit' in text and 'not' in text and 'settling' in text
    assert 'ds_dac_143' in text and 'rm_dac_450' in text
    assert all(len(text.encode()) <= 65536 for text in bundle.documents.values())


def test_retrieval_requires_index_and_every_dac_prerequisite():
    session = Session(Bundle(BUNDLE))
    with pytest.raises(PraxisError, match='index'):
        session.read_peripheral_doc('dac')
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='rcc, flash, pwr, gpio, tim'):
        session.read_peripheral_doc('dac')
    for name in ['rcc', 'flash', 'pwr', 'gpio']:
        session.read_peripheral_doc(name)
    with pytest.raises(PraxisError, match='tim'):
        session.read_peripheral_doc('dac')
    session.read_peripheral_doc('tim')
    assert session.read_peripheral_doc('DAC1') == session.read_peripheral_doc('dac')


@pytest.mark.parametrize('change', [
    {'instances': {'dac': ['DAC2']}},
    {'modes': {'dac': ['channel2_software_trigger']}},
])
def test_unreviewed_instance_and_mode_do_not_inherit_contract(change):
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-dac-v1.json').read_bytes())
    records = load_definitions(profile, {s.id: source / s.path for s in profile.sources})
    workflow = profile.workflows['dac_channel1_software_trigger'].model_copy(update=change)
    profile = profile.model_copy(update={'workflows': {'wrong_dac': workflow}, 'publication_requires': []})
    result = workflow_coverage(profile, records, {})['wrong_dac']
    assert not result['ready'] and result['issues']


def test_isolated_target_link_retains_the_complete_unused_integration_entry(tmp_path):
    from elftools.elf.elffile import ELFFile
    from praxis.firmware_build import BuildService

    require_image(ROOT / 'toolchain-f407.lock.json')
    service = BuildService(BUNDLE, ROOT / 'assets/stm32f407vg', ROOT / 'examples',
                           tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json')
    result = service.build('stm32f407g-disc1-dac/application')
    assert result['compile_passed'] and result['image_validated']
    elf = tmp_path / 'artifacts' / result['artifact_id'] / 'firmware.elf'
    with elf.open('rb') as stream:
        symbols = ELFFile(stream).get_section_by_name('.symtab')
        entry = symbols.get_symbol_by_name('application_output')
        assert entry and entry[0]['st_size'] > 0
