"""F407 scoped timer semantics, independent MMIO effects and source-bound modes."""
import json
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.compiler import compile_bundle
from praxis.definitions import load_definitions
from praxis.models import Peripheral, Profile
from praxis.reports import read_report

SOURCE=ROOT/'sources/stm32f407g-disc1'
APP=ROOT/'examples/stm32f407g-disc1-timer'


@pytest.fixture(scope='module')
def model(tmp_path_factory):
    require_tool('gcc')
    output=tmp_path_factory.mktemp('timer-effects')/'model'
    subprocess.run(['gcc','-std=c11','-Wall','-Wextra','-Werror','-isystem',
        str(ROOT/'assets/stm32f407vg/include'),'-I',str(APP/'pwm_application'),
        str(ROOT/'tests/fixtures/f407_timer_model.c'),'-o',str(output)],
        check=True,capture_output=True,timeout=30)
    return output


def run(model,*args):
    result=subprocess.run([str(model),*(str(a) for a in args)],capture_output=True,
                          check=True,text=True,timeout=5)
    row=json.loads(result.stdout)
    if 'violation' in row:
        assert row['violation']==0
        assert row['reads']<110 and row['writes']<35
        assert row['gate']&(1<<17) and row['reset']&(1<<21)
        if row['failed']:
            assert row['retry']==9 and row['retry_writes']==0
    return row


@pytest.mark.parametrize('high',[0,1,250,999,1000])
def test_pwm_endpoints_and_natural_update_latch_have_expected_waveform(model,high):
    row=run(model,0,0,high)
    assert row['start']==row['operation']==row['stop']==0 and row['quiet']
    assert row['active_before']==row['ones_before']==high
    assert row['active_after']==row['ones']==750
    assert row['ccer']==row['dier']==row['cr1']==0


def test_capture_uses_full_word_and_consumes_flag_without_writing_read_only_ccr(model):
    row=run(model,1,0)
    assert row['start']==row['operation']==row['stop']==0
    assert row['value']==0x12345678 and row['events']==row['ccr_reads']==1
    assert row['ccr_writes']==0 and row['quiet']


@pytest.mark.parametrize('mode',[0,1])
@pytest.mark.parametrize('fault,status',[(1,2),(2,2),(3,3),(4,3),(5,3),(6,4),(7,3)])
def test_wrong_context_clock_or_owner_rejected_before_writes(model,mode,fault,status):
    row=run(model,mode,fault)
    assert row['start']==status and row['writes']==0 and not row['events']


@pytest.mark.parametrize('mode',[0,1])
@pytest.mark.parametrize('fault,quiet',[(8,False),(9,True),(10,False),(11,True),(24,True),(25,True),(26,True)])
def test_gate_reset_direction_stale_update_or_enable_failure_never_succeeds(model,mode,fault,quiet):
    row=run(model,mode,fault)
    assert row['start']==5 and row['failed'] and bool(row['quiet'])==quiet
    if fault==26:
        assert row['ccr_writes']==0  # Wrong direction must be caught BEFORE a CCR write.


@pytest.mark.parametrize('fault,status',[(14,6),(15,8),(16,8),(17,8),(18,5),(21,5),(22,7)])
def test_missing_stale_corrupt_or_racing_capture_never_publishes_a_sample(model,fault,status):
    row=run(model,1,fault)
    assert row['operation']==status and row['value']==0xDEADBEEF
    assert row['failed'] and row['quiet'] and row['ccr_writes']==0


@pytest.mark.parametrize('fault,status',[(12,6),(13,5),(21,5),(23,5)])
def test_pwm_timeout_failed_preload_or_wrong_view_latches_failure(model,fault,status):
    row=run(model,0,fault)
    assert row['operation']==status and row['failed'] and row['quiet']


@pytest.mark.parametrize('mode',[0,1])
def test_lost_gate_never_attempts_timer_cleanup_access(model,mode):
    row=run(model,mode,19)
    assert row['operation']==3 and row['failed'] and not row['quiet']


def test_failed_shutdown_is_reported_and_never_retried(model):
    row=run(model,0,20)
    assert row['stop']==5 and row['failed'] and not row['quiet'] and row['cr1']!=0


@pytest.mark.parametrize('clock,tick,period,high,prescaler',[
    (16000000,1000000,1000,250,15),(84000000,1000000,1000,1000,83),
    (65536,1,2,0,65535),(16000000,16000000,0xFFFFFFFF,0xFFFFFFFF,0),
])
def test_integer_parameter_plan_handles_dividers_and_32_bit_periods(model,clock,tick,period,high,prescaler):
    row=run(model,2,clock,tick,period,high)
    assert row==dict(valid=1,prescaler=prescaler,period=period,high=high)


@pytest.mark.parametrize('clock,tick,period,high',[
    (0,1,2,0),(16,0,2,0),(16,32,2,0),(17,2,2,0),(65537,1,2,0),
    (16000000,1000000,0,0),(16000000,1000000,1,0),(16000000,1000000,1000,1001),
])
def test_unsupported_dividers_zero_arr_or_unrepresentable_duty_are_rejected(model,clock,tick,period,high):
    assert not run(model,2,clock,tick,period,high)['valid']


def test_two_isolated_source_snapshots_share_exact_controller_and_mmio_bytes():
    for name in ['timer_controller.h','timer_mmio.h']:
        assert (APP/'pwm_application'/name).read_bytes()==(APP/'capture_application'/name).read_bytes()


@pytest.fixture(scope='module')
def timer_bundle(tmp_path_factory):
    require_tool('clang')
    require_tool('arm-none-eabi-gcc')
    return Bundle(compile_bundle(SOURCE/'profile-timer-modes-v1.json',
                                tmp_path_factory.mktemp('timer-modes')/'bundle'))


def test_scoped_mode_dependencies_views_access_semantics_and_workflow_readiness(timer_bundle):
    row=read_report(timer_bundle,'coverage')
    for mode in ['tim2_pwm_ch1_reference','tim2_software_capture_ch1']:
        assert row['workflows'][mode]['ready']
        assert 'rcc/hsi16_core_checked' in row['workflows'][mode]['mode_order']
        assert 'rcc/tim2_owned_gate_reset' in row['workflows'][mode]['mode_order']
    assert row['counts']['reviewed_subsets']==22
    assert sum(r['ready'] for r in row['workflows'].values())==22
    assert row['peripherals']['tim']['reviewed_modes']['pwm_ch1_reference']==['TIM2']
    assert row['peripherals']['tim']['reviewed_modes']['software_capture_ch1']==['TIM2']
    for name in ['tim2_pwm_ch1_pin','tim2_capture_ch1_external']:
        assert not row['workflows'][name]['ready']
        assert any('not reviewed' in issue for issue in row['workflows'][name]['issues'])
    text=timer_bundle.read('wiki/peripherals/tim.md')
    assert 'CCMR1: output_output' in text and 'CCMR1: input_output' in text
    assert 'read-only' in text and 'CC1OF' in text and 'not a pin waveform' in text


def test_definition_modes_cannot_reuse_input_fields_in_pwm_view():
    from pydantic import ValidationError
    profile=Profile.model_validate_json((SOURCE/'profile-timer-modes-v1.json').read_bytes())
    paths={s.id:SOURCE/s.path for s in profile.sources}
    tim=next(i for i in load_definitions(profile,paths) if i.id=='tim')
    raw=tim.model_dump()
    raw['operating_modes']['pwm_ch1_reference']['fields']['CCMR1']=['IC1PSC']
    with pytest.raises(ValidationError,match='undeclared bit field'):
        Peripheral.model_validate(raw)


def test_repeated_compilation_keeps_the_same_revision(timer_bundle,tmp_path):
    other=Bundle(compile_bundle(SOURCE/'profile-timer-modes-v1.json',tmp_path/'bundle'))
    assert timer_bundle.manifest.file_hashes==other.manifest.file_hashes
    assert timer_bundle.manifest.bundle_revision==other.manifest.bundle_revision


@pytest.mark.parametrize('workflow',['tim2_pwm_ch1_reference','tim2_software_capture_ch1'])
def test_similar_timer_instance_cannot_inherit_tim2_mode_readiness(workflow):
    from praxis.coverage import workflow_coverage
    profile=Profile.model_validate_json((SOURCE/'profile-timer-modes-v1.json').read_bytes())
    requirement=profile.workflows[workflow].model_copy(update={'instances':{'tim':['TIM3']}})
    profile=profile.model_copy(update={'workflows':{workflow:requirement}})
    items=load_definitions(profile,{s.id:SOURCE/s.path for s in profile.sources})
    report=workflow_coverage(profile,items,{})
    assert not report[workflow]['ready']
    assert any('outside reviewed mode scope' in issue for issue in report[workflow]['issues'])


def test_new_semantic_locators_resolve_to_actual_mcp_source_parts():
    from praxis.bundle import digest
    profile=Profile.model_validate_json((SOURCE/'profile-timer-modes-v1.json').read_bytes())
    paths={s.id:SOURCE/s.path for s in profile.sources}
    evidence=json.loads(paths['timer_modes_evidence'].read_text())
    for source in profile.sources:
        if source.id.startswith('timer_modes_'):
            assert source.expected_sha256==digest((SOURCE/source.path).read_bytes())
    items=load_definitions(profile,paths)
    refs=[]
    for item in items:
        for r in item.registers:
            refs+=r.sources+[s for f in r.fields for s in f.sources]
            for v in r.field_views.values():
                refs+=v.sources+[s for f in v.fields for s in f.sources]
        refs += [s for mode in item.operating_modes.values() for s in mode.sources]
    for ref in refs:
        if ref.source=='timer_modes_evidence':
            assert ref.locator in evidence['pages']
            assert evidence['pages'][ref.locator]['artifact_sha256']


def test_timer_acceptance_keeps_all_existing_cases_and_uses_isolated_source_snapshots(tmp_path):
    from praxis.acceptance import AcceptancePlan
    from praxis.verify import snapshot
    old=AcceptancePlan.model_validate_json((ROOT/'examples/acceptance/stm32f407g-disc1.json').read_bytes())
    new=AcceptancePlan.model_validate_json((ROOT/'examples/acceptance/stm32f407g-disc1-timer.json').read_bytes())
    assert new.cases[:len(old.cases)]==old.cases and len(new.cases)==len(old.cases)+2
    for case in new.cases[-2:]:
        destination=tmp_path/case.id
        destination.mkdir()
        units,fingerprint=snapshot(ROOT/'examples'/case.source_directory,destination)
        assert units and len(fingerprint)==64
