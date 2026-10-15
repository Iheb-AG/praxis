"""CAN1-only contracts, nested declarations, shared effect model and IRQ-vector link."""
import json
import struct
import subprocess

import pytest

from conftest import ROOT, require_image, require_tool
from praxis.bundle import Bundle
from praxis.coverage import workflow_coverage
from praxis.definitions import load_definitions
from praxis.errors import PraxisError
from praxis.models import Profile
from praxis.routing import Session

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-can-v1'
APPLICATION = ROOT / 'examples/stm32f407g-disc1-can/application'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    binary = tmp_path_factory.mktemp('can-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
        str(ROOT / 'tests/fixtures/f407_can_model.c'), '-o', str(binary)],
        check=True, capture_output=True, timeout=30)
    return binary


def run(model, fault=0):
    result = subprocess.run([str(model), str(fault)], check=True,
                            capture_output=True, timeout=5, text=True)
    record = json.loads(result.stdout)
    assert not record['violation']  # Protection, literal actions and ordering checked by model.
    assert record['calls'] < 160 and record['retry_blocked']
    return record


@pytest.mark.parametrize('fault', [0, 40, 43])
def test_success_requires_isr_receipt_full_payload_release_and_tx_completion(model, fault):
    result = run(model, fault)
    assert result['configured_status'] == result['status'] == 0 and result['received']
    assert result['requests'] == result['releases'] == result['acks'] == 1
    assert result['rx_reads'] == 15 and result['dispatched'] == 1
    assert result['irq_count'] == (2 if fault == 43 else 1)
    assert not result['ier'] and not result['irq_enabled'] and not result['rf0']
    assert result['reset_required']  # Explicit one-shot, no automatic reuse.
    assert result['fmr'] == (0xE00 if fault == 40 else 0x2A1C0E00)


@pytest.mark.parametrize('fault,status', [(1, 3), (2, 3), (30, 2), (31, 5), (35, 5), (36, 5)])
def test_failed_init_filter_and_configuration_never_enable_irq_or_request(model, fault, status):
    result = run(model, fault)
    assert result['configured_status'] == result['status'] == status
    assert not result['requests'] and not result['ier'] and not result['irq_enabled']
    assert result['reset_required'] and not result['acks']


@pytest.mark.parametrize('fault', [33, 34, 37, 38, 39])
def test_existing_owner_wrong_clock_or_missing_reset_rejects_without_writes(model, fault):
    result = run(model, fault)
    assert result['status'] == 2 and not result['config_writes'] and not result['requests']
    if fault == 33:
        assert result['irq_enabled'] == 1 << 20  # Preserve existing line owner.


@pytest.mark.parametrize('fault,status', [
    (3, 8), (4, 8), (5, 8), (6, 4), (7, 4), (8, 4), (9, 6), (10, 8), (11, 6),
    (12, 4), (13, 4), (14, 7), (15, 7), (16, 7), (17, 7), (18, 7), (19, 7),
    (20, 7), (21, 2), (22, 4), (23, 9), (24, 10), (25, 10), (26, 10),
    (27, 2), (28, 2), (29, 2), (32, 2), (45, 4),
])
def test_errors_missing_delivery_corrupt_data_and_lost_actions_cannot_pass(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and result['reset_required']
    if fault != 27:  # Fault27 loses the already validated success acknowledgement.
        assert not result['acks']
    if fault not in [24, 25]:
        assert not result['ier'] and not result['irq_enabled']
    if fault == 3:
        assert result['requests'] == 1 and not result['irq_count']
        assert result['rf0'] == 1 and not result['received']  # Polling cannot fake IRQ delivery.
    if fault in [8, 22, 45]:
        assert result['esr'] and not result['acks']
    if fault in [12, 13]:
        assert result['rf0'] & 0x18 and not result['releases']  # Retain FULL/FOVR.
    if fault in [6, 7]:
        assert result['tsr'] & 0xC and not result['acks']  # Retain TERR/ALST.
    if fault in [14, 15, 16, 17, 18, 19, 20]:
        assert result['rx_reads'] == 15 and not result['releases']


@pytest.mark.parametrize('fault,status', [(41, 2), (42, 1), (44, 1)])
def test_unready_handler_null_payload_and_zero_budget_do_not_leave_owned_irq_enabled(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and not result['ier'] and not result['irq_enabled']
    assert not result['acks'] and not result['received']


def test_complete_nested_tables_unknown_resets_and_prior_workflows_preserved():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    assert coverage['peripherals']['can']['registers'] == 89
    assert coverage['peripherals']['can']['fields'] == 108
    assert coverage['peripherals']['can']['reviewed_registers'] == 23
    for workflow in ['can1_silent_loopback_irq', 'can1_silent_loopback',
                     'dac_channel1_software_trigger', 'i2c1_controller_transmit', 'adc1_internal_reference']:
        assert coverage['workflows'][workflow]['ready']
    assert not coverage['workflows']['feature_can']['ready']
    assert not coverage['workflows']['can1_external_bus']['ready']
    text = bundle.read('wiki/peripherals/can.md')
    assert '| sTxMailBox_0__TIR | 0x180 | 32 | — | RW | not asserted |' in text
    assert '| FMR | 0x200 | 32 | — | RW | not asserted |' in text
    assert '| sFIFOMailBox_0__RIR | 0x1B0 | 32 | — | RO |' in text
    assert '| sTxMailBox_0__TIR | STID | 31:21 | 0xFFE00000 |' in text
    assert 'only in CAN1' in text and 'CAN2' in text
    assert all("## Register map" in bundle.read(path) and "## Bit fields" in bundle.read(path)
               for path in bundle.manifest.peripherals.values())


def test_can_routing_cannot_bypass_interrupt_and_clock_documents():
    session = Session(Bundle(BUNDLE))
    with pytest.raises(PraxisError, match='index'):
        session.read_peripheral_doc('can')
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='rcc, flash, pwr, gpio, usart, tim, syscfg, exti, nvic'):
        session.read_peripheral_doc('can')
    for entity in ['rcc', 'flash', 'pwr', 'gpio', 'usart', 'tim', 'syscfg', 'exti', 'nvic']:
        session.read_peripheral_doc(entity)
    assert session.read_peripheral_doc('can1') == session.read_peripheral_doc('can')


@pytest.mark.parametrize('change', [
    {'instances': {'can': ['CAN2']}}, {'modes': {'can': ['normal_bus']}},
])
def test_can2_and_normal_bus_do_not_inherit_internal_test_support(change):
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-can-v1.json').read_bytes())
    records = load_definitions(profile, {s.id: source / s.path for s in profile.sources})
    workflow = profile.workflows['can1_silent_loopback_irq'].model_copy(update=change)
    profile = profile.model_copy(update={'workflows': {'wrong_can': workflow}, 'publication_requires': []})
    result = workflow_coverage(profile, records, {})['wrong_can']
    assert not result['ready'] and result['issues']


def test_isolated_target_link_binds_irq20_to_real_handler(tmp_path):
    from elftools.elf.elffile import ELFFile
    from praxis.firmware_build import BuildService

    require_image(ROOT / 'toolchain-f407.lock.json')
    service = BuildService(BUNDLE, ROOT / 'assets/stm32f407vg', ROOT / 'examples',
                           tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json')
    result = service.build('stm32f407g-disc1-can/application')
    assert result['compile_passed'] and result['image_validated']
    elf = tmp_path / 'artifacts' / result['artifact_id'] / 'firmware.elf'
    with elf.open('rb') as stream:
        image = ELFFile(stream)
        words = struct.unpack('<98I', image.get_section_by_name('.isr_vector').data())
        symbols = image.get_section_by_name('.symtab')
        handler = symbols.get_symbol_by_name('CAN1_RX0_IRQHandler')[0]
        assert handler['st_size'] > 0 and words[36] == handler['st_value']
        assert words[36] != symbols.get_symbol_by_name('Default_Handler')[0]['st_value']
