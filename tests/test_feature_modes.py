"""Mode, instance, topology and semantic provenance gates use explicit records."""

import json
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from praxis.coverage import mode_order, workflow_coverage
from praxis.errors import PraxisError
from praxis.features import feature_report
from praxis.models import OperatingMode, Peripheral, WorkflowRequirement


def peripheral():
    return Peripheral.model_validate(
        dict(
            id="test",
            title="Test",
            prerequisites=[],
            instances=[
                dict(
                    name="TEST1",
                    base_address=0,
                    bus="fixture",
                    clock="fixture",
                    sources=[dict(source="header", locator="TEST1")],
                )
            ],
            registers=[
                dict(
                    name="CR",
                    offset=0,
                    width=32,
                    access="RW",
                    access_widths=[32],
                    reset=0,
                    side_effects="Fixture only",
                    sources=[dict(source="manual", locator="page:1")],
                    fields=[
                        dict(
                            name="EN",
                            lsb=0,
                            width=1,
                            mask=1,
                            meaning="Fixture enable",
                            sources=[dict(source="manual", locator="page:1")],
                        )
                    ],
                )
            ],
            operating_modes={
                "basic": dict(
                    title="Fixture mode",
                    instances=["TEST1"],
                    registers=["CR"],
                    fields={"CR": ["EN"]},
                    requirements=["Configure before enable"],
                    sources=[dict(source="manual", locator="page:1")],
                )
            },
            reviewed_markdown="reviewed.md",
            review=dict(status="reviewed", reviewer="Fixture", basis="Test"),
        )
    )


def readiness(requirement, items=None, topology=None):
    profile = SimpleNamespace(
        workflows={"test_flow": WorkflowRequirement.model_validate(requirement)},
        header=SimpleNamespace(required_registers={}),
        publication_requires=["test_flow"],
    )
    return workflow_coverage(profile, items or [peripheral()], {}, topology)["test_flow"]


def request():
    return dict(
        peripherals=["test"],
        registers={"test": ["CR"]},
        modes={"test": ["basic"]},
        instances={"test": ["TEST1"]},
    )


def test_exact_mode_instance_scope_required():
    assert readiness(request())["ready"]
    for change in (
        {"modes": {"test": ["unknown"]}},
        {"instances": {"test": ["TEST2"]}},
        {"instances": {}},
    ):
        assert not readiness({**request(), **change})["ready"]
    item = peripheral().model_copy(update={"operating_modes": {}})
    assert not readiness(request(), [item])["ready"]


def test_unknown_topology_blocks_even_reviewed_registers():
    r = {**request(), "signals": ["MISSING"]}
    assert not readiness(r)["ready"]

    class Missing:
        def query(self, name):
            return f"No match for {name}"

    assert not readiness(r, topology=Missing())["ready"]


@pytest.mark.parametrize(
    "change",
    [
        {"instances": ["TEST2"]},
        {"registers": ["MISSING"]},
        {"fields": {"CR": ["MISSING"]}},
    ],
)
def test_mode_cannot_reference_unknown_hardware(change):
    raw = peripheral().model_dump()
    raw["operating_modes"]["basic"].update(change)
    with pytest.raises(ValidationError):
        Peripheral.model_validate(raw)


def test_unreviewed_record_and_unknown_access_cannot_define_mode():
    for key in ("review", "access"):
        raw = peripheral().model_dump()
        if key == "review":
            raw["review"] = None
        else:
            raw["registers"][0]["access"] = "unknown"
        with pytest.raises(ValidationError):
            Peripheral.model_validate(raw)


def test_explicit_bus_width_independent_of_c_member_width():
    raw = peripheral().model_dump()
    raw["registers"][0].update(width=8, access_widths=[32])
    assert Peripheral.model_validate(raw).registers[0].access_widths == [32]
    raw["registers"][0]["offset"] = 1
    with pytest.raises(ValidationError):
        Peripheral.model_validate(raw)


@pytest.mark.parametrize('change', ['mode_source', 'register_source', 'field_source', 'bus_width'])
def test_authored_modes_require_semantic_evidence_for_used_facts(tmp_path, change):
    from praxis.compiler import _definitions
    from praxis.errors import PraxisError

    raw = peripheral().model_dump()
    raw['reviewed_markdown'] = 'reviewed.md'
    if change == 'mode_source':
        raw['operating_modes']['basic']['sources'] = [dict(source='header', locator='CR')]
    elif change == 'register_source':
        raw['registers'][0]['sources'] = [dict(source='header', locator='CR')]
    elif change == 'field_source':
        raw['registers'][0]['fields'][0]['sources'] = [dict(source='header', locator='CR.EN')]
    else:
        raw['registers'][0]['access_widths'] = []
    path = tmp_path / 'facts.json'
    path.write_text(json.dumps([raw]))
    (tmp_path / 'reviewed.md').write_text('Fixture editorial record')
    profile = SimpleNamespace(definitions='facts', definition_extensions=[], sources=[
        SimpleNamespace(id='manual', authority='semantics', path='reviewed.md'),
        SimpleNamespace(id='header', authority='declarations', path='header.h'),
    ])
    with pytest.raises(PraxisError, match='SOURCE_AUTHORITY'):
        _definitions(profile, {'facts': path, 'manual': tmp_path / 'reviewed.md',
                               'header': tmp_path / 'header.h'}, tmp_path)


def test_partial_catalog_never_claims_complete_mcu_support():
    row = dict(
        status="reviewed_subset",
        published=True,
        instances=["TEST1"],
        reviewed_modes={"basic": ["TEST1"]},
        provenance="header:Test_TypeDef",
        issues=[],
    )
    report = feature_report(dict(target="fixture", peripherals={"test": row}, workflows={}))
    assert not report["all_features_supported"]
    assert report["counts"]["reviewed_mode_contracts"] == 1
    assert (
        report["features"]["test"]["hardware_qualification"]
        == "separate workflow evidence required"
    )


def test_duplicate_empty_and_semantics_bypass_scope_rejected():
    for change in (
        {"modes": {"test": []}},
        {"instances": {"test": ["TEST1", "TEST1"]}},
        {"operating_semantics": False},
        {"modes": {"foreign": ["mode"]}},
    ):
        with pytest.raises(ValidationError):
            WorkflowRequirement.model_validate({**request(), **change})
    with pytest.raises(ValidationError):
        OperatingMode.model_validate(
            {**peripheral().operating_modes["basic"].model_dump(), "requirements": [" "]}
        )


def dependent_pair():
    root = peripheral().model_dump()
    child = peripheral().model_dump()
    child['id'] = 'foundation'
    child['operating_modes']['basic']['title'] = 'Foundation setup'
    root['operating_modes']['basic']['requires_modes'] = [dict(
        peripheral='foundation', mode='basic', instances=['TEST1'])]
    return [Peripheral.model_validate(root), Peripheral.model_validate(child)]


def test_required_modes_expand_workflow_without_implicit_document_cycle():
    items = dependent_pair()
    report = readiness(request(), items)
    assert report['ready']
    assert report['closure'] == ['foundation', 'test']
    assert report['mode_order'] == ['foundation/basic', 'test/basic']
    assert all(not item.prerequisites for item in items)


@pytest.mark.parametrize('kind', ['unknown', 'instance', 'cycle'])
def test_invalid_mode_graph_rejected(kind):
    items = [item.model_dump() for item in dependent_pair()]
    if kind == 'unknown':
        items[0]['operating_modes']['basic']['requires_modes'][0]['mode'] = 'missing'
        code = 'UNKNOWN_MODE_DEPENDENCY'
    elif kind == 'instance':
        items[0]['operating_modes']['basic']['requires_modes'][0]['instances'] = ['TEST2']
        code = 'MODE_INSTANCE_MISMATCH'
    else:
        items[1]['operating_modes']['basic']['requires_modes'] = [dict(
            peripheral='test', mode='basic', instances=['TEST1'])]
        code = 'DEPENDENCY_CYCLE'
    with pytest.raises(PraxisError, match=code):
        mode_order([Peripheral.model_validate(item) for item in items])


def test_required_mode_cannot_hide_unreviewed_document_dependency():
    items = [item.model_dump() for item in dependent_pair()]
    items[1]['prerequisites'] = ['unreviewed']
    third = peripheral().model_dump()
    third.update(id='unreviewed', review=None, operating_modes={})
    report = readiness(request(), [Peripheral.model_validate(item) for item in [*items, third]])
    assert not report['ready']
    assert 'unreviewed: operating semantics not reviewed' in report['issues']


def test_mode_contract_supplies_register_requirements_to_workflow():
    result = readiness({**request(), 'registers': {}}, dependent_pair())
    assert result['ready'] and result['closure'] == ['foundation', 'test']
    # Additional workflow requirements still apply alongside the mode contract.
    result = readiness({**request(), 'registers': {'test': ['EXTRA']}}, dependent_pair())
    assert not result['ready'] and 'test.EXTRA: register not published' in result['issues']


def test_duplicate_or_empty_mode_dependency_scope_rejected():
    raw = dependent_pair()[0].model_dump()
    dependency = raw['operating_modes']['basic']['requires_modes'][0]
    for instances in ([], ['TEST1', 'TEST1'], [' ']):
        changed = {**dependency, 'instances': instances}
        mode = {**raw['operating_modes']['basic'], 'requires_modes': [changed]}
        with pytest.raises(ValidationError):
            OperatingMode.model_validate(mode)
    with pytest.raises(ValidationError):
        OperatingMode.model_validate({**raw['operating_modes']['basic'], 'requires_modes': [dependency, dependency]})
