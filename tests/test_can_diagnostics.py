"""Gated, source-bound CAN reads; actual Tcl interpreter uses modeled memory only."""
import re
import subprocess

import pytest

from conftest import ROOT, require_tool
from praxis.bundle import Bundle
from praxis.can_diagnostics import parse, script, validate_bundle
from praxis.errors import PraxisError
from praxis.telemetry import get_contract, read_telemetry_script


def record(enabled=True, msr=3):
    gate = '02000000' if enabled else '00000000'
    rows = [f'PRAXIS_CAN_STATE|gate_before|{gate}']
    if enabled:
        rows += ['PRAXIS_CAN_STATE|mcr|00010019',f'PRAXIS_CAN_STATE|msr|{msr:08x}']
        if msr & 1:
            rows += ['PRAXIS_CAN_STATE|btr|01230000']
    rows += [f'PRAXIS_CAN_STATE|gate_after|{gate}']
    return '\n'.join(['PRAXIS_IMAGE_VERIFIED',*rows,'PRAXIS_IMAGE_REVERIFIED'])


def test_selected_bundle_layout_and_diagnostic_contract_required():
    validate_bundle(Bundle(ROOT/'bundles/stm32f407g-disc1-e01-can-v1'))
    with pytest.raises(PraxisError,match='DIAGNOSTIC_UNSUPPORTED'):
        validate_bundle(Bundle(ROOT/'bundles/stm32f407g-disc1-e01-m1'))
    with pytest.raises(PraxisError,match='DIAGNOSTIC_UNSUPPORTED'):
        read_telemetry_script('000000010000000200000003',bytes(392),0x20000004,1,100,can_state=True)
    text = read_telemetry_script('000000010000000200000003',bytes(392),0x20000004,1,100,
                                contract=get_contract('can-loopback-v1'),can_state=True)
    assert not re.search(r'^\s*(halt|resume|reset|write_memory|mww|flash|program|step|bp)\b',text,re.M)
    assert text.index('PRAXIS_IMAGE_VERIFIED') < text.index('PRAXIS_CAN_STATE') < text.index('PRAXIS_IMAGE_REVERIFIED')


@pytest.mark.parametrize('change', ['gate_changed','duplicate','outside','missing','order','extra','no_image'])
def test_malformed_unbracketed_and_wrong_gate_states_fail(change):
    text = record()
    if change == 'gate_changed':
        text = text.replace('gate_after|02000000','gate_after|00000000')
    elif change == 'duplicate':
        text = text.replace('PRAXIS_IMAGE_REVERIFIED','PRAXIS_CAN_STATE|msr|00000003\nPRAXIS_IMAGE_REVERIFIED')
    elif change == 'outside':
        text += '\nPRAXIS_CAN_STATE|mcr|00010019'
    elif change == 'missing':
        text = text.replace('PRAXIS_CAN_STATE|msr|00000003\n','')
    elif change == 'order':
        text = text.replace('gate_before','gate_swap').replace('gate_after','gate_before').replace('gate_swap','gate_after')
    elif change == 'extra':
        text = text.replace('PRAXIS_IMAGE_REVERIFIED','PRAXIS_CAN_STATE|fifo_action|00000020\nPRAXIS_IMAGE_REVERIFIED')
    else:
        text = text.replace('PRAXIS_IMAGE_VERIFIED','')
    with pytest.raises(PraxisError,match='DIAGNOSTIC_PROTOCOL'):
        parse(text)


@pytest.mark.parametrize('gate,msr', [(0,0),(1<<25,0),(1<<25,1),(1<<25,3),(1<<25,0xC00)])
def test_actual_tcl_only_reads_enabled_can_and_btr_when_inak(tmp_path,gate,msr):
    require_tool('openocd')
    prelude = ('gdb_port disabled\ntcl_port disabled\ntelnet_port disabled\n'
        f'set test_gate {gate}\nset test_msr {msr}\nset test_reads {{}}\n'
        'proc read_memory {addr width count} {\n'
        ' global test_gate test_msr test_reads\n lappend test_reads $addr\n'
        ' if {$width != 32 || $count != 1} {error "unexpected access"}\n'
        ' if {$addr == 0x40023840} {return [list $test_gate]}\n'
        ' if {!($test_gate & 0x02000000)} {error "gated CAN read"}\n'
        ' if {$addr == 0x40006400} {return {0x10019}}\n'
        ' if {$addr == 0x40006404} {return [list $test_msr]}\n'
        ' if {$addr == 0x4000641c && ($test_msr & 1)} {return {0x01230000}}\n'
        ' error "unapproved read"\n}\n'
        'echo PRAXIS_IMAGE_VERIFIED\n')
    path=tmp_path/'read.tcl'
    path.write_text(prelude+'\n'.join(script())+'\necho PRAXIS_IMAGE_REVERIFIED\nshutdown\n')
    result=subprocess.run(['openocd','-f',str(path)],capture_output=True,text=True,timeout=5)
    assert result.returncode==0,result.stdout+result.stderr
    state=parse(result.stdout+result.stderr)
    assert state['clock_enabled']==bool(gate)
    assert ('btr' in state['raw'])==bool(gate and msr&1)
    if gate:
        assert state['init_acknowledged']==bool(msr&1)
