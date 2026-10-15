"""Independent dual-timer effects and exact, source-bound board route contracts."""
import json
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle, digest
from praxis.compiler import compile_bundle
from praxis.definitions import load_definitions
from praxis.models import Profile
from praxis.reports import read_report

APP = ROOT / 'examples/stm32f407g-disc1-timer/routes_application'
SOURCE = ROOT / 'sources/stm32f407g-disc1'
WORKFLOW = 'tim2_tim5_pwm_capture_loopback'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    output = tmp_path_factory.mktemp('timer-routes') / 'model'
    subprocess.run(['gcc', '-std=c11', '-Wall', '-Wextra', '-Werror', '-isystem',
        str(ROOT / 'assets/stm32f407vg/include'), '-I', str(APP),
        str(ROOT / 'tests/fixtures/f407_timer_route_model.c'), '-o', str(output)],
        check=True, capture_output=True, timeout=30)
    return output


def run(model, fault=0, wrap=False):
    args = [str(model), str(fault)] + (['wrap'] if wrap else [])
    row = json.loads(subprocess.run(args, capture_output=True, text=True,
                                   check=True, timeout=5).stdout)
    assert row['violations'] == 0
    assert row['reads'] < 400 and row['writes'] < 60
    assert row['gate'] & (1 << 17) and row['ahb'] & (1 << 3)
    if row['failed']:
        assert row['retry'] == 8 and row['retry_writes'] == 0
    return row


@pytest.mark.parametrize('wrap', [False, True])
def test_independent_free_running_capture_measures_eight_periods_and_wrap(model, wrap):
    row = run(model, wrap=wrap)
    assert row['start'] == row['operation'] == row['stop'] == 0
    assert row['frames'] == 8 and row['delta'] == 1000 and row['quiet']
    assert row['enables'] == row['ccr_writes'] == 1
    assert row['moder'] == 0xA8000000  # SWD preserved, owned pins released to input.
    assert row['afrl'] == 0x90000210 and row['pull'] == 0x64000020


@pytest.mark.parametrize('fault,status,writes', [(2,2,0),(3,3,0),(4,4,0),(5,4,0),
                                                 (6,4,1),(7,4,1),(31,1,0)])
def test_context_clock_timer_pin_lock_and_wiring_ownership_preconditions(model, fault, status, writes):
    row = run(model, fault)
    assert row['start'] == status and row['writes'] == writes and not row['enables']


@pytest.mark.parametrize('fault,quiet', [(8,True),(9,True),(10,True),(11,False),
    (12,False),(13,True),(14,False),(15,True),(16,True),(17,True),(18,True),
    (19,True),(20,True)])
def test_lost_configuration_gate_reset_preload_or_enable_never_succeeds(model, fault, quiet):
    row = run(model, fault)
    assert row['start'] == 5 and row['failed'] and bool(row['quiet']) == quiet
    if fault in [9,10]:
        assert row['ccr_writes'] == 0  # Direction checked before an output CCR write.
    if fault in [8,9,10,11,12,13,14,15,16,18,19,20]:
        assert not row['enables']


@pytest.mark.parametrize('fault,status', [(1,6),(21,7),(22,7),(23,7),(24,5),(30,5)])
def test_missing_wire_overcapture_new_event_wrong_period_and_changed_af_fail_closed(model, fault, status):
    row = run(model, fault)
    assert row['operation'] == status and row['failed'] and row['quiet']
    assert row['frames'] == 0
    if fault in [21,22,23]:
        assert row['value'] == 0xDEADBEEF


@pytest.mark.parametrize('fault', [25,26,27])
def test_lost_clock_avoids_inaccessible_cleanup_and_cannot_claim_quiet(model, fault):
    row = run(model, fault)
    assert row['operation'] == 3 and row['failed'] and not row['quiet']


@pytest.mark.parametrize('fault', [28,29])
def test_failed_pin_release_or_output_disable_is_reported_without_retry(model, fault):
    row = run(model, fault)
    assert row['operation'] == 0 and row['stop'] == 5 and row['failed']
    assert not row['quiet']


def test_routed_example_reuses_the_existing_checked_arithmetic_bytes():
    assert (APP / 'timer_controller.h').read_bytes() == (
        APP.parent / 'pwm_application/timer_controller.h').read_bytes()


@pytest.fixture(scope='module')
def route_bundle(tmp_path_factory):
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    return Bundle(compile_bundle(SOURCE / 'profile-timer-routes-v1.json',
        tmp_path_factory.mktemp('routed-bundle') / 'bundle'))


def test_exact_route_views_scopes_and_dependency_order_are_published(route_bundle):
    report = read_report(route_bundle, 'coverage')
    row = report['workflows'][WORKFLOW]
    assert row['ready'] and row['mode_instance_scope'] == {
        'tim': {'capture_ch3_pa2': ['TIM5'], 'pwm_ch2_pa1': ['TIM2']}}
    sequence = row['mode_order']
    assert sequence.index('rcc/hsi16_core_checked') < sequence.index('rcc/timer_pair_gates')
    assert sequence.index('rcc/timer_pair_gates') < sequence.index('gpio/pa1_tim2_ch2_pa2_tim5_ch3')
    assert sequence.index('gpio/pa1_tim2_ch2_pa2_tim5_ch3') < sequence.index('tim/pwm_ch2_pa1')
    assert sum(r['ready'] for r in report['workflows'].values()) == 23
    assert len(report['workflows']) == 38
    # Channel2/3 scope does not silently qualify the old, different channel1 routes.
    for name in ['tim2_pwm_ch1_pin','tim2_capture_ch1_external']:
        assert not report['workflows'][name]['ready']
    text = route_bundle.read('wiki/peripherals/tim.md')
    assert 'CCMR2: input_output' in text and 'CCMR1: output_output' in text
    assert 'low16' in text and 'independent' in text


def test_route_aliases_resolve_exact_complete_separate_fixed_nets(route_bundle):
    from praxis.routing import Session
    session = Session(route_bundle)
    session.read_wiki_index()
    output = session.query_schematic_netlist('TIM2_PWM_OUT')
    capture = session.query_schematic_netlist('TIM5_CAPTURE_IN')
    assert all(token in output for token in ['PA1','U4:24','P1:11'])
    assert all(token in capture for token in ['PA2','U4:25','P1:14'])
    assert 'U4:25' not in output and 'U4:24' not in capture
    assert session.query_schematic_netlist('PA10').startswith('No match')
    assert 'P1:14' in session.query_schematic_netlist('USART2_TX')


def test_another_timer_cannot_inherit_the_routed_mode():
    from praxis.coverage import workflow_coverage
    profile = Profile.model_validate_json((SOURCE / 'profile-timer-routes-v1.json').read_bytes())
    raw = profile.workflows[WORKFLOW].model_dump()
    raw['mode_instances']['tim']['capture_ch3_pa2'] = ['TIM3']
    raw['instances']['tim'] = ['TIM2','TIM3']
    from praxis.models import WorkflowRequirement
    req = WorkflowRequirement.model_validate(raw)
    profile = profile.model_copy(update={'workflows': {WORKFLOW: req}})
    items = load_definitions(profile, {s.id: SOURCE / s.path for s in profile.sources})
    row = workflow_coverage(profile, items, {})[WORKFLOW]
    assert not row['ready']
    assert any('outside reviewed mode scope' in s for s in row['issues'])


def test_all_new_evidence_locators_resolve_to_pinned_mcp_source_artifacts():
    profile = Profile.model_validate_json((SOURCE / 'profile-timer-routes-v1.json').read_bytes())
    paths = {s.id: SOURCE / s.path for s in profile.sources}
    evidence = {}
    for source in profile.sources:
        if source.id.startswith('timer_routes_'):
            assert source.expected_sha256 == digest(paths[source.id].read_bytes())
            if source.id.endswith('evidence'):
                evidence[source.id] = json.loads(paths[source.id].read_text())['pages']
    items = load_definitions(profile, paths)
    refs = []
    for item in items:
        refs += [s for m in item.operating_modes.values() for s in m.sources]
        refs += [s for i in item.instances for s in i.sources]
        for r in item.registers:
            refs += r.sources + [s for f in r.fields for s in f.sources]
            for v in r.field_views.values():
                refs += v.sources + [s for f in v.fields for s in f.sources]
    for ref in refs:
        if ref.source in evidence:
            record = evidence[ref.source][ref.locator]
            assert all(len(record[k]) == 64 for k in [
                'artifact_sha256','source_sha256','import_revision'])


def test_new_acceptance_plan_retains_every_previous_case():
    from praxis.acceptance import AcceptancePlan
    old = AcceptancePlan.model_validate_json((ROOT /
        'examples/acceptance/stm32f407g-disc1-timer.json').read_bytes())
    new = AcceptancePlan.model_validate_json((ROOT /
        'examples/acceptance/stm32f407g-disc1-timer-routes.json').read_bytes())
    assert new.cases[:-1] == old.cases and len(new.cases) == 15
    assert new.cases[-1].workflows == [WORKFLOW]


def test_repeated_compilation_is_byte_identical(route_bundle, tmp_path):
    other = Bundle(compile_bundle(SOURCE / 'profile-timer-routes-v1.json', tmp_path / 'bundle'))
    assert route_bundle.manifest.file_hashes == other.manifest.file_hashes
    assert route_bundle.manifest.bundle_revision == other.manifest.bundle_revision
