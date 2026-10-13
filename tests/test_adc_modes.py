"""Reviewed ADC scope, actual callback ordering and bounded failure paths."""
import json
import subprocess

import pytest

from conftest import ROOT, require_image, require_tool
from praxis.bundle import Bundle
from praxis.coverage import workflow_coverage
from praxis.definitions import load_definitions
from praxis.models import Profile
from praxis.routing import Session
from praxis.errors import PraxisError

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-adc-v1'
APPLICATION = ROOT / 'examples/stm32f407g-disc1-adc/application'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    binary = tmp_path_factory.mktemp('adc-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
        str(ROOT / 'tests/fixtures/f407_adc_model.c'), '-o', str(binary)],
        check=True, capture_output=True, timeout=30)
    return binary


def run(model, fault=-1, budget=3):
    result = subprocess.run([str(model), str(fault), str(budget)], check=True,
                            capture_output=True, timeout=5, text=True)
    return json.loads(result.stdout)


def test_same_target_callback_waits_for_new_update_and_reads_adc_once(model):
    result = run(model)
    assert result['completed'] == result['order_ok'] == result['fresh_delay'] == 1
    assert result['raw'] == 1500 and result['reads'] == 1 and result['eoc_cleared']
    assert result['sample_cycles'] == 480 and result['channel'] == 17
    assert result['calls'] == result['attempts'] == 17
    assert result['owned'] == result['stopped'] == result['preserved'] == 1
    assert 480 / 21000000 >= 10e-6
    assert (8399 + 1) * (9 + 1) / 84000000 == 0.001


@pytest.mark.parametrize('step', range(14))
def test_each_failed_stage_stops_dependent_initialization(model, step):
    result = run(model, step)
    assert not result['completed'] and result['failed_step'] == step
    assert result['order_ok'] and result['stopped'] and result['preserved']
    assert result['reads'] == 0
    assert result['calls'] <= 19


@pytest.mark.parametrize('fault', [-3, -4, -7, -8])
def test_wrong_clock_or_existing_owner_is_rejected_before_peripheral_writes(model, fault):
    result = run(model, fault)
    assert result['calls'] == 1 and result['failed_step'] == 0
    assert not result['completed'] and not result['owned'] and not result['reads']
    assert result['preserved']


def test_overrun_out_of_range_and_wrong_order_cannot_report_success(model):
    overrun, invalid, reordered = [run(model, fault) for fault in [-5, -6, -2]]
    assert not overrun['completed'] and overrun['failed_step'] == 12 and overrun['reads'] == 0
    assert not invalid['completed'] and invalid['failed_step'] == 13 and invalid['reads'] == 1
    assert invalid['raw'] == 0 and invalid['stopped']
    assert not reordered['completed'] and not reordered['order_ok']
    assert run(model, budget=0)['calls'] == 0
    # A stale UG flag cannot satisfy a too-small timer polling budget.
    short = run(model, budget=1)
    assert not short['completed'] and short['failed_step'] == 9 and not short['reads']


def test_bundle_keeps_full_tables_and_limits_support_to_adc1_internal_mode():
    bundle = Bundle(BUNDLE)
    data = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    workflow = data['workflows']['adc1_internal_reference']
    assert workflow['ready'] and workflow['required_for_publication']
    assert workflow['closure'] == ['adc', 'adc_common', 'flash', 'pwr', 'rcc', 'tim']
    assert data['workflows']['feature_adc']['ready']
    assert not data['workflows']['feature_flash']['ready']
    assert data['counts']['reviewed_subsets'] == 17
    assert data['peripherals']['adc']['registers'] == 20
    assert data['peripherals']['adc_common']['registers'] == 3
    assert data['peripherals']['adc']['reviewed_modes'] == {'single_conversion': ['ADC1']}
    assert len(bundle.manifest.sources) > 100
    assert all(len(text.encode()) <= 65536 for text in bundle.documents.values())
    session = Session(bundle)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match='rcc, flash, pwr, adc_common'):
        session.read_peripheral_doc('adc')
    for peripheral in ('rcc', 'flash', 'pwr', 'adc_common', 'adc', 'tim'):
        assert session.read_peripheral_doc(peripheral)
    assert 'st_adc_gate' in session.read_peripheral_doc('rcc')


def test_adc2_cannot_inherit_internal_reference_mode():
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-adc-v1.json').read_bytes())
    paths = {s.id: source / s.path for s in profile.sources}
    items = load_definitions(profile, paths)
    workflow = profile.workflows['adc1_internal_reference'].model_copy(update={
        'instances': {'adc': ['ADC2'], 'tim': ['TIM2']}})
    profile = profile.model_copy(update={'workflows': {'wrong_adc': workflow}, 'publication_requires': []})
    result = workflow_coverage(profile, items, {})['wrong_adc']
    assert not result['ready']
    assert any('outside reviewed mode scope' in issue for issue in result['issues'])


def test_adc_example_isolated_target_build_when_provisioned(tmp_path):
    from praxis.firmware_build import BuildService
    require_image(ROOT / 'toolchain-f407.lock.json')
    service = BuildService(BUNDLE, ROOT / 'assets/stm32f407vg', ROOT / 'examples',
                           tmp_path / 'artifacts', ROOT / 'toolchain-f407.lock.json')
    result = service.build('stm32f407g-disc1-adc/application')
    assert result['compile_passed'] and result['image_validated']
