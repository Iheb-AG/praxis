"""Source-bound I2C subset, effect-model negative cases and isolated target build."""
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

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-i2c-v1'
APPLICATION = ROOT / 'examples/stm32f407g-disc1-i2c/application'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    binary = tmp_path_factory.mktemp('i2c-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
        str(ROOT / 'tests/fixtures/f407_i2c_model.c'), '-o', str(binary)],
        check=True, capture_output=True, timeout=30)
    return binary


def run(model, fault=0):
    result = subprocess.run([str(model), str(fault)], check=True,
                            capture_output=True, timeout=5, text=True)
    return json.loads(result.stdout)


def test_controller_obeys_read_clear_and_completion_order(model):
    result = run(model)
    assert result['configured'] and result['status'] == 0 and result['queued'] == 3
    assert result['cleaned'] and result['stops'] == result['addresses'] == 1
    assert not result['dirty'] and not result['cr1'] and not result['violation']
    assert result['config_writes'] == 5


@pytest.mark.parametrize('fault,status', [
    (1, 4), (2, 4), (3, 4), (4, 5), (5, 6), (6, 5), (7, 4), (8, 4),
    (9, 4), (10, 4), (11, 6), (12, 7), (13, 8), (14, 9), (23, 9), (24, 6),
])
def test_bus_failures_never_report_success_and_require_reset(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and result['dirty'] and result['retry_blocked']
    assert not result['violation'] and result['calls'] < 100
    if fault in [1, 2, 5, 10, 11, 23]:
        assert result['stops'] == 0
    if fault in [4, 6]:
        assert result['cleaned'] and result['sr1'] & 0x400  # Retain rc_w0 AF diagnostic.
        assert result['cr1'] == 1  # PE=0 would clear AF; preserve until explicit reset.
    if fault == 9:
        assert result['stops'] == 1 and not result['cleaned']  # No STOP after ownership ended.


@pytest.mark.parametrize('fault,status', [(15, 3), (16, 1), (17, 1), (18, 1), (19, 1)])
def test_invalid_input_or_unreviewed_wiring_cannot_touch_bus(model, fault, status):
    result = run(model, fault)
    assert result['status'] == status and not result['addresses'] and not result['stops']
    assert not result['cr1'] and not result['dirty'] and not result['violation']


@pytest.mark.parametrize('fault', [20, 21, 22])
def test_wrong_clock_missing_reset_or_existing_owner_cannot_configure(model, fault):
    result = run(model, fault)
    assert not result['configured'] and not result['config_writes']
    assert result['status'] == 2 and not result['addresses'] and not result['stops']


def test_failed_reconfiguration_invalidates_previous_clock_contract(model):
    result = run(model, 25)
    assert not result['configured'] and result['config_writes'] == 5
    assert result['status'] == 2 and result['dirty'] and result['retry_blocked']
    assert not result['addresses'] and not result['stops'] and not result['violation']


def test_bundle_retains_all_nine_registers_and_no_f42_filter():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    assert coverage['workflows']['i2c1_controller_transmit']['ready']
    assert not coverage['workflows']['feature_i2c']['ready']
    assert not coverage['workflows']['i2c1_wired_transmit']['ready']
    assert coverage['workflows']['adc1_internal_reference']['ready']
    assert coverage['peripherals']['i2c']['registers'] == 9
    text = bundle.read('wiki/peripherals/i2c.md')
    assert '| TRISE | 0x020 |' in text and '| FLTR | 0x024 |' not in text
    assert 'not W1C' in text and 'forbids software STOP' in text
    assert all(len(text.encode()) <= 65536 for text in bundle.documents.values())
    session = Session(bundle)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='rcc, flash, pwr'):
        session.read_peripheral_doc('i2c')
    for name in ['rcc', 'flash', 'pwr', 'i2c']:
        assert session.read_peripheral_doc(name)


def test_i2c2_does_not_inherit_i2c1_contract():
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-i2c-v1.json').read_bytes())
    records = load_definitions(profile, {s.id: source / s.path for s in profile.sources})
    workflow = profile.workflows['i2c1_controller_transmit'].model_copy(update={
        'instances': {'i2c': ['I2C2']}})
    profile = profile.model_copy(update={'workflows': {'wrong_i2c': workflow}, 'publication_requires': []})
    result = workflow_coverage(profile, records, {})['wrong_i2c']
    assert not result['ready']
    assert any('outside reviewed mode scope' in issue for issue in result['issues'])


def test_i2c_example_isolated_target_build_when_provisioned(tmp_path):
    from praxis.firmware_build import BuildService
    require_image(ROOT / 'toolchain-f407.lock.json')
    service = BuildService(BUNDLE, ROOT / 'assets/stm32f407vg', ROOT / 'examples',
                           tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json')
    result = service.build('stm32f407g-disc1-i2c/application')
    assert result['compile_passed'] and result['image_validated']
