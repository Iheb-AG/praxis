"""One generic block may use different exact instances for different modes."""
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from praxis.coverage import markdown, workflow_coverage
from praxis.models import Peripheral, WorkflowRequirement
from praxis.support import _Workflow, _workflow


def requirement(**changes):
    return WorkflowRequirement.model_validate(dict(peripherals=['serial'],modes={'serial':['send','receive']},
        mode_instances={'serial':{'send':['UNIT_A'],'receive':['UNIT_B']}},**changes))


def block():
    ref=[dict(source='synthetic',locator='test only')]
    return Peripheral(id='serial',title='Unrelated synthetic hardware',prerequisites=[],
        instances=[dict(name=n,base_address=i,bus='test',clock='test',sources=ref)
                   for i,n in enumerate(['UNIT_A','UNIT_B'])],
        registers=[dict(name='CTRL',offset=0,width=32,access='RW',access_widths=[32],
                        side_effects='synthetic',sources=ref)],reviewed_markdown='test.md',
        review=dict(status='reviewed',reviewer='unit fixture',basis='synthetic'),
        operating_modes={name:dict(title=name,instances=[instance],registers=['CTRL'],
            requirements=['synthetic scope'],sources=ref)
            for name,instance in [('send','UNIT_A'),('receive','UNIT_B')]})


def report(req):
    profile=SimpleNamespace(workflows={'exchange':req},header=SimpleNamespace(required_registers={}),
                            publication_requires=[])
    return workflow_coverage(profile,[block()],{})['exchange']


def test_exact_per_mode_scopes_make_a_mixed_instance_workflow_ready():
    row=report(requirement())
    assert row['ready'] and row['instance_scope']=={'serial':['UNIT_A','UNIT_B']}
    assert row['mode_instance_scope']=={'serial':{'send':['UNIT_A'],'receive':['UNIT_B']}}
    value=_workflow(_Workflow.model_validate(row))
    assert value['mode_instance_scope']==row['mode_instance_scope']
    text=markdown(dict(scope='synthetic',peripherals={},workflows={'exchange':row},limits=[]))
    assert 'Exact instances per mode' in text and 'serial/receive: UNIT_B' in text


def test_legacy_scope_remains_uniform_and_does_not_infer_a_matching_instance():
    req=WorkflowRequirement(peripherals=['serial'],modes={'serial':['send','receive']},
                             instances={'serial':['UNIT_A','UNIT_B']})
    row=report(req)
    assert not row['ready'] and any('outside reviewed mode scope' in s for s in row['issues'])
    assert 'mode_instance_scope' not in row and 'mode_instances' not in req.model_dump()


def test_swapping_explicit_instances_cannot_bypass_reviewed_mode_scope():
    req=requirement().model_copy(update={'mode_instances':{'serial':{'send':['UNIT_B'],'receive':['UNIT_A']}}})
    assert not report(req)['ready']


@pytest.mark.parametrize('scopes',[
    {},{'send':['UNIT_A']},{'send':['UNIT_A'],'receive':['UNIT_B'],'extra':['UNIT_A']},
    {'send':[],'receive':['UNIT_B']},{'send':['UNIT_A','UNIT_A'],'receive':['UNIT_B']},
    {'send':[' bad '],'receive':['UNIT_B']},
])
def test_incomplete_unknown_or_noncanonical_mode_scopes_are_rejected(scopes):
    raw=requirement().model_dump()
    raw['mode_instances']={'serial':scopes}
    with pytest.raises(ValidationError):
        WorkflowRequirement.model_validate(raw)


def test_union_constraint_prevents_an_unaccounted_instance_request():
    raw=requirement().model_dump()
    raw['instances']={'serial':['UNIT_A']}
    with pytest.raises(ValidationError,match='union'):
        WorkflowRequirement.model_validate(raw)
    raw['instances']['serial'].append('UNIT_B')
    assert WorkflowRequirement.model_validate(raw)


def test_mode_scope_cannot_name_an_entity_without_selected_modes():
    raw=requirement().model_dump()
    raw['mode_instances']['absent']={'send':['UNIT_A']}
    with pytest.raises(ValidationError,match='selected workflow modes'):
        WorkflowRequirement.model_validate(raw)
