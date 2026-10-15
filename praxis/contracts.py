"""Declarative publication policy. Contracts contain data, never executable rules.

Extraction establishes declarations; reviewed contracts define the minimum
evidence for a published scope. Neither one grants firmware/probe qualification.
"""
from __future__ import annotations

from typing import Literal

from pydantic import Field, StrictInt, ValidationError, model_validator

from praxis.bundle import digest, read_inside
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import CortexCPU, Identifier, MacroName, PeripheralDiscovery, Record, Review, SourceRef


class IntegerConstraint(Record):
    equals: StrictInt | None = None
    minimum: StrictInt | None = None
    maximum: StrictInt | None = None

    @model_validator(mode="after")
    def consistent(self):
        if self.equals is None and self.minimum is None and self.maximum is None:
            raise ValueError("An operating constraint must constrain a value")
        if self.minimum is not None and self.maximum is not None and self.minimum > self.maximum:
            raise ValueError("Inverted operating range")
        if self.equals is not None and not self.accepts(self.equals):
            raise ValueError("Exact value lies outside the operating range")
        return self

    def accepts(self, value):
        return (type(value) is int and (self.equals is None or value == self.equals)
                and (self.minimum is None or value >= self.minimum)
                and (self.maximum is None or value <= self.maximum))


class PublicationContract(Record):
    schema_version: Literal[1] = 1
    id: Identifier
    review: Review
    sources: list[SourceRef] = Field(min_length=1)
    family: Identifier
    mcu: str = Field(min_length=1)
    package: str = Field(min_length=1)
    header_kind: Literal["cmsis", "avr"]
    cpu: CortexCPU | None = None
    header_identity: list[MacroName] = []
    avr_mcu: MacroName | None = None
    required_registers: dict[Identifier, list[MacroName]] = {}
    member_views: dict[Identifier, dict[MacroName, list[MacroName]]] = {}
    clock_plan: dict[MacroName, IntegerConstraint] | None = None
    legacy_discovery: dict[Identifier, PeripheralDiscovery] = {}
    core_source: Identifier | None = None
    pin_document: Identifier | None = None
    board_prerequisites: list[Identifier] = []

    @model_validator(mode="after")
    def adapter_scope(self):
        if self.header_kind == "cmsis":
            if self.cpu is None or not self.header_identity or self.avr_mcu is not None:
                raise ValueError("CMSIS contracts require CPU and header identities, without AVR options")
        elif self.avr_mcu is None or self.cpu is not None or self.legacy_discovery:
            raise ValueError("AVR contracts require an explicit compiler MCU, without CMSIS options")
        for values in (*self.required_registers.values(), self.header_identity, self.board_prerequisites):
            if len(values) != len(set(values)):
                raise ValueError("Duplicate contract identities")
        for views in self.member_views.values():
            for names in views.values():
                if not names or len(set(names)) != len(names):
                    raise ValueError("Member views need unique, nonempty register names")
        return self


def load_contract(profile, root):
    """Read and check the exact registered policy before invoking any extractor."""
    spec = next((s for s in profile.sources if s.id == profile.compilation_contract), None)
    if spec is None:
        raise PraxisError("UNKNOWN_SOURCE", "compilation_contract must name a registered source")
    if spec.authority != "configuration" or spec.expected_sha256 is None:
        raise PraxisError("INVALID_CONTRACT", "Publication policy needs configuration authority and expected_sha256")
    raw = read_inside(root, spec.path, 1024 * 1024)
    if digest(raw) != spec.expected_sha256:
        raise PraxisError("SOURCE_HASH_MISMATCH", "Publication contract changed; review and pin a new policy version")
    try:
        contract = PublicationContract.model_validate(load_json(raw))
    except ValidationError as exc:
        raise PraxisError("INVALID_CONTRACT", str(exc)) from exc
    registered = {s.id for s in profile.sources} | {"profile"}
    if any(ref.source not in registered for ref in contract.sources):
        raise PraxisError("UNKNOWN_SOURCE", "Contract provenance names an unregistered source")
    if contract.core_source is not None and contract.core_source not in registered:
        raise PraxisError("UNKNOWN_SOURCE", "Contract core_source needs a registered declaration source")
    target = profile.target
    if (target.family, target.mcu) != (contract.family, contract.mcu):
        raise PraxisError("TARGET_MISMATCH", "Publication contract applies to a different target")
    if target.package != contract.package:
        raise PraxisError("PACKAGE_MISMATCH", "Publication contract applies to a different package")
    if profile.header.kind != contract.header_kind:
        raise PraxisError("TARGET_MISMATCH", "Header adapter differs from the publication contract")
    if target.knowledge_adapter is not None:
        adapter = target.knowledge_adapter
        if adapter.cpu != contract.cpu or set(adapter.header_identity) != set(contract.header_identity):
            raise PraxisError("TARGET_MISMATCH", "Extraction CPU/header identities differ from the pinned contract")
    if contract.clock_plan is None:
        if profile.clock_plan is not None:
            raise PraxisError("INVALID_PROFILE", "No operating clock plan is declared by this contract")
    elif (profile.clock_plan is None or profile.clock_plan.keys() != contract.clock_plan.keys()
          or any(not constraint.accepts(profile.clock_plan[name])
                 for name, constraint in contract.clock_plan.items())):
        raise PraxisError("INVALID_PROFILE", "Operating clock plan does not satisfy the reviewed contract")
    return contract


def validate_required_registers(profile, contract, items):
    """Union additive profile requirements with the pinned minimum; never subtract."""
    requirements = {name: set(registers) for name, registers in contract.required_registers.items()}
    for name, registers in profile.header.required_registers.items():
        requirements.setdefault(name, set()).update(registers)
    entities = {item.id: item for item in items}
    if not requirements.keys() <= entities.keys():
        raise PraxisError("MISSING_DECLARATION", "Required-register policy names an unpublished peripheral")
    for name, required in sorted(requirements.items()):
        item = entities[name]
        reviewed = {r.name for r in item.registers if item.review is not None and r.access != "unknown"}
        missing = sorted(required - reviewed)
        if missing:
            raise PraxisError("UNREVIEWED_REQUIRED_FACT", f"{name}: required registers need reviewed operating semantics: {missing}")
    published = set(entities)
    links = set(contract.board_prerequisites) | ({contract.pin_document} if contract.pin_document else set())
    if not links <= published:
        raise PraxisError("MISSING_DECLARATION", "Contract routing links name unpublished peripherals")
