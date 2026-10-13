"""Clock-mode scope, the shared target callback's ordering, and bounded failure paths."""
import json
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.routing import Session
from praxis.errors import PraxisError

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-clock-v1'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    output = tmp_path_factory.mktemp('clock-model') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
        '-isystem', str(ROOT / 'assets/stm32f407vg/include'),
        '-I', str(ROOT / 'examples/stm32f407g-disc1-clock/application'),
        str(ROOT / 'tests/fixtures/f407_clock_model.c'), '-o', str(output)],
        check=True, capture_output=True, timeout=30)
    return output


def run(model, fault=-1, budget=3):
    result = subprocess.run([str(model), str(fault), str(budget)], check=True,
                            capture_output=True, timeout=5, text=True)
    return json.loads(result.stdout)


def test_same_register_callback_selects_reviewed_operating_point(model):
    result = run(model)
    assert result['completed'] == 1 and result['order_ok'] == 1
    assert result['system_core_clock'] == result['sysclk'] == 168000000
    assert result['pll48'] == 48000000
    assert result['latency'] == 5 and result['scale1'] == 1
    assert result['commands_clear'] == 1 and result['preserved'] == 1
    assert result['attempts'] == result['calls'] == 24


@pytest.mark.parametrize('step', range(24))
def test_failure_at_each_stage_stops_dependent_initialization(model, step):
    result = run(model, step)
    assert result['completed'] == 0 and result['failed_step'] == step
    assert result['order_ok'] == 1 and result['system_core_clock'] == 16000000
    assert step + 1 <= result['calls'] <= step + 3


def test_zero_budget_and_out_of_order_enable_rejected(model):
    result = run(model, budget=0)
    assert result['completed'] == 0 and result['calls'] == 0
    reordered = run(model, -2)
    assert reordered['completed'] == 0 and reordered['order_ok'] == 0
    assert reordered['system_core_clock'] == 16000000


def test_bundle_has_mode_closure_but_no_flash_programming_claim():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    workflow = coverage['workflows']['rng_pll_polling']
    assert workflow['ready'] and workflow['closure'] == ['flash', 'pwr', 'rcc', 'rng']
    assert workflow['mode_order'] == ['flash/latency_168mhz', 'rcc/power_interface_gate',
        'pwr/voltage_scale', 'rcc/pll_hse8_168mhz', 'rng/pll_polling']
    assert not coverage['workflows']['feature_flash']['ready']
    assert 'FLASH_ACR_BYTE0_ADDRESS' not in bundle.read('wiki/peripherals/flash.md')
    assert '| CR | VOS | 14:14 | 0x4000 |' in bundle.read('wiki/peripherals/pwr.md')
    session = Session(bundle)
    session.read_wiki_index()
    session.read_peripheral_doc('rcc')
    with pytest.raises(PraxisError, match='flash, pwr'):
        session.read_peripheral_doc('rng')
    session.read_peripheral_doc('flash')
    session.read_peripheral_doc('pwr')
    assert 'pll_polling' in session.read_peripheral_doc('rng')
