"""Authored workflow scopes drive multi-hop evidence preparation without guessing."""

from types import SimpleNamespace

import pytest

from praxis.errors import PraxisError
from praxis.models import OperatingMode, WorkflowRequirement
from praxis.workflow_review import plan


def context():
    requirement = WorkflowRequirement(peripherals=["adc"], registers={"adc": ["CR", "SR"]},
                                      modes={"adc": ["single"]}, instances={"adc": ["ADC1"]})
    profile = SimpleNamespace(workflows={"sample": requirement}, discovery=SimpleNamespace(
        peripherals={"rcc": SimpleNamespace(prerequisites=[])}, default_prerequisites=["rcc"]),
        header=SimpleNamespace(required_registers={"rcc": ["GATE"]}))
    declarations = {name: SimpleNamespace(registers=[SimpleNamespace(name=register) for register in registers])
                    for name, registers in {"adc": ["CR", "SR"], "rcc": ["GATE"], "common": ["CCR"]}.items()}
    return profile, declarations


def test_missing_mode_remains_a_review_gap_and_foundation_registers_are_included():
    profile, declarations = context()
    result = plan(profile, [], declarations, "sample")
    assert result["retrieval_order"] == ["rcc", "adc"]
    assert result["registers"] == {"adc": ["CR", "SR"], "rcc": ["GATE"]}
    assert result["unresolved"] == ["adc/single: operating contract requires review"]


def test_transitive_mode_registers_and_document_prerequisites_are_expanded():
    profile, declarations = context()
    source = [{"source": "manual", "locator": "fixture"}]
    common = OperatingMode(title="Synthetic common", instances=["COMMON"], registers=["CCR"],
                           requirements=["Synthetic only"], sources=source)
    mode = OperatingMode(title="Synthetic sample", instances=["ADC1"], registers=["CR"],
        requirements=["Synthetic only"], sources=source,
        requires_modes=[{"peripheral": "common", "mode": "prescale", "instances": ["COMMON"]}])
    reviewed = [SimpleNamespace(id="adc", prerequisites=["common"], operating_modes={"single": mode}),
                SimpleNamespace(id="common", prerequisites=["rcc"], operating_modes={"prescale": common})]
    result = plan(profile, reviewed, declarations, "sample")
    assert result["retrieval_order"] == ["rcc", "common", "adc"]
    assert result["registers"]["common"] == ["CCR"]
    assert result["reviewed_mode_closure"] == ["adc/single", "common/prescale"]
    assert not result["unresolved"]


def test_unknown_workflow_register_or_dependency_is_not_guessed():
    profile, declarations = context()
    with pytest.raises(PraxisError, match="UNKNOWN_WORKFLOW"):
        plan(profile, [], declarations, "SAMPLE")
    del declarations["rcc"]
    with pytest.raises(PraxisError, match="MISSING_DECLARATION"):
        plan(profile, [], declarations, "sample")
    profile, declarations = context()
    profile.workflows["sample"] = profile.workflows["sample"].model_copy(update={"registers": {"adc": ["UNKNOWN"]}})
    with pytest.raises(PraxisError, match="MISSING_DECLARATION"):
        plan(profile, [], declarations, "sample")


def test_missing_register_scope_stays_unresolved():
    profile, declarations = context()
    profile.header.required_registers = {}
    assert "rcc: explicit register review scope is missing" in plan(profile, [], declarations, "sample")["unresolved"]


def test_cyclic_mode_dependencies_fail_review_preparation():
    profile, declarations = context()
    mode = OperatingMode(title="Synthetic cycle", instances=["ADC1"], registers=["CR"],
        requirements=["Synthetic only"], sources=[{"source": "manual", "locator": "fixture"}],
        requires_modes=[{"peripheral": "adc", "mode": "single", "instances": ["ADC1"]}])
    reviewed = [SimpleNamespace(id="adc", prerequisites=["rcc"], operating_modes={"single": mode})]
    with pytest.raises(PraxisError, match="DEPENDENCY_CYCLE"):
        plan(profile, reviewed, declarations, "sample")


def test_wrong_instance_scope_remains_explicit():
    profile, declarations = context()
    mode = OperatingMode(title="Synthetic scope", instances=["ADC2"], registers=["CR"],
        requirements=["Synthetic only"], sources=[{"source": "manual", "locator": "fixture"}])
    reviewed = [SimpleNamespace(id="adc", prerequisites=["rcc"], operating_modes={"single": mode})]
    assert "adc/single: requested instances outside the reviewed contract" in plan(
        profile, reviewed, declarations, "sample")["unresolved"]
