"""RX route ownership and real finite synchronization effects; no physical claims."""
import json
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.coverage import workflow_coverage
from praxis.definitions import load_definitions
from praxis.errors import PraxisError
from praxis.models import Profile
from praxis.routing import Session

APPLICATION = ROOT / 'examples/stm32f407g-disc1-can/telemetry_rx_application'
BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-can-rx-v1'


@pytest.fixture(scope='module')
def models(tmp_path_factory):
    require_tool('gcc')
    output = tmp_path_factory.mktemp('can-rx-models')
    result = {}
    for name, source in [('route', 'f407_can_rx_route_model.c'), ('can', 'f407_can_rx_model.c')]:
        binary = output / name
        subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror',
            '-isystem', str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APPLICATION),
            str(ROOT / 'tests/fixtures' / source), '-o', str(binary)],
            check=True, capture_output=True, timeout=30)
        result[name] = binary
    return result


def run(models, name, fault):
    result = subprocess.run([str(models[name]), str(fault)], check=True,
                            capture_output=True, timeout=5, text=True)
    data = json.loads(result.stdout)
    assert not data['violation']
    return data


@pytest.mark.parametrize('fault,status', [(0, 0), (1, 2), (2, 3), (3, 3), (4, 3),
    (5, 3), (6, 3), (7, 4), (8, 4), (9, 4), (10, 5), (11, 0), (12, 1), (13, 1)])
def test_gpio_gate_ownership_bias_order_readback_and_bounded_input(models, fault, status):
    data = run(models, 'route', fault)
    assert data['status'] == status
    assert data['reads'] < 30 and data['writes'] <= 4 and data['inputs'] <= 8
    assert data['gate'] & ~8 == 0x20000000
    assert data['mode'] & ~3 == 0xA0000000
    assert data['pull'] & ~3 == 0x40000000
    assert data['af'] & ~15 == 0x70000000
    if fault in [6, 12, 13]:
        assert data['writes'] == data['reads'] == 0
    if fault in [2, 3, 4, 5]:
        assert data['writes'] == 1 and data['stage'] == 0
    if fault == 10:
        assert data['inputs'] == 8 and data['stage'] == 3
    if fault == 11:
        assert data['inputs'] == 3


@pytest.mark.parametrize('fault,status', [(0, 0), (46, 2), (47, 3), (48, 2), (49, 0), (50, 3), (51, 2)])
def test_can_requires_route_and_consecutive_recessive_progress(models, fault, status):
    data = run(models, 'can', fault)
    assert data['status'] == status and data['calls'] < 240
    if status:
        assert not data['requests'] and not data['ier'] and not data['irq_enabled']
        assert data['reset_required'] and data['retry_blocked']
    else:
        assert data['received'] and data['irq_count'] == 1
        assert data['requests'] == data['releases'] == data['acks'] == 1
        assert data['rx_reads'] == 15 and data['sync_samples'] == 11
    if fault == 49:
        assert data['exit_reads'] == 13  # Two dominant samples cannot count toward eleven recessive ones.
    if fault == 50:
        assert data['exit_reads'] == 10 and data['sync_samples'] == 10
    if fault == 48:
        assert not data['config_writes']


@pytest.mark.parametrize('fault,status', [(1, 3), (2, 3), (6, 4), (8, 4), (14, 7),
    (19, 7), (22, 4), (23, 9), (24, 10), (25, 10), (26, 10), (27, 2), (45, 4)])
def test_rx_candidate_retains_prior_error_and_cleanup_guards(models, fault, status):
    data = run(models, 'can', fault)
    assert data['status'] == status and data['reset_required'] and data['retry_blocked']
    if fault not in [24, 25]:
        assert not data['ier'] and not data['irq_enabled']


def test_bundle_has_exact_topology_and_dependency_contracts():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    assert coverage['workflows']['can1_rx_guarded_loopback_irq']['ready']
    assert not coverage['workflows']['can1_external_bus']['ready']
    topology = bundle.read('wiki/schemas/custom_pcb_netlist.md')
    assert 'PD0' in topology and 'P2' in topology and '81' in topology and '34' in topology
    assert 'can1_rx_pd0' in bundle.read('wiki/peripherals/gpio.md')
    assert all("## Register map" in bundle.read(path) and "## Bit fields" in bundle.read(path)
               for path in bundle.manifest.peripherals.values())


def test_removing_gpio_mode_blocks_dependent_can_publication_workflow():
    source = ROOT / 'sources/stm32f407g-disc1'
    profile = Profile.model_validate_json((source / 'profile-can-rx-v1.json').read_bytes())
    records = load_definitions(profile, {s.id: source / s.path for s in profile.sources})
    topology = Session(Bundle(BUNDLE)).netlist
    assert workflow_coverage(profile, records, {}, topology)['can1_rx_guarded_loopback_irq']['ready']
    records = [r.model_copy(update={'operating_modes': {}}) if r.id == 'gpio' else r for r in records]
    with pytest.raises(PraxisError, match='required mode gpio/can1_rx_pd0 is not published') as error:
        workflow_coverage(profile, records, {}, topology)
    assert error.value.code == 'UNKNOWN_MODE_DEPENDENCY'
