"""Versioned compiler IR and bundle manifest. No vendor guesses or implicit targets."""

from __future__ import annotations

import re
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator, model_serializer, model_validator

Identifier = Annotated[str, Field(pattern=r"^[a-z][a-z0-9_]*$", max_length=64)]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SourceRef(Record):
    source: str = Field(min_length=1)
    locator: str = Field(min_length=1)


class Source(Record):
    id: Identifier
    path: str
    sha256: Digest
    authority: Literal["declarations", "connectivity", "semantics", "pinout", "configuration"]
    version: str
    license: str
    origin: str


class Review(Record):
    status: Literal["reviewed"]
    reviewer: str = Field(min_length=1)
    basis: str = Field(min_length=1)

    @field_validator("reviewer", "basis")
    @classmethod
    def meaningful(cls, value):
        if not value.strip():
            raise ValueError("Review identity and basis cannot be whitespace")
        return value


CortexCPU = Literal["cortex-m0", "cortex-m0plus", "cortex-m3", "cortex-m4", "cortex-m7"]
MacroName = Annotated[str, Field(pattern=r"^[A-Za-z_]\w*$", max_length=128)]


class CortexMKnowledgeAdapter(Record):
    """Declarative extraction contract; conveys no firmware or probe qualification."""

    kind: Literal["cmsis_cortex_m"] = "cmsis_cortex_m"
    cpu: CortexCPU
    header_identity: list[MacroName] = Field(min_length=1)
    mask_suffix: Literal["_Msk", "_MASK"] = "_Msk"
    position_suffix: Literal["_Pos", "_SHIFT"] = "_Pos"

    @model_validator(mode="after")
    def unique_identity(self):
        if len(set(self.header_identity)) != len(self.header_identity):
            raise ValueError("Header identity macros must be unique")
        return self


class Target(Record):
    id: Identifier
    family: Identifier
    mcu: str
    package: str
    silicon_revision: str
    board_revision: str
    primary_mcu_ref: str
    example_only: bool = True
    clock_hz: int | None = Field(default=None, gt=0)
    clock_assumptions: list[str] = Field(min_length=1)
    fuse_assumptions: list[str] = []
    knowledge_adapter: CortexMKnowledgeAdapter | None = None
    scope: Literal["board", "mcu"] = "board"

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        # Existing immutable bundle revisions must retain their original bytes/hash input.
        value = handler(self)
        if self.knowledge_adapter is None:
            value.pop("knowledge_adapter", None)
        if self.scope == "board":
            value.pop("scope", None)
        return value

    @model_validator(mode="after")
    def supported_fixture(self):
        if self.scope == "mcu":
            if self.knowledge_adapter is None or not self.example_only:
                raise ValueError("MCU-only targets require an explicit experimental knowledge adapter")
            if self.board_revision != "not-applicable" or self.primary_mcu_ref != "not-applicable":
                raise ValueError("MCU-only targets must declare board_revision and primary_mcu_ref as not-applicable")
        elif self.clock_hz is None:
            raise ValueError("Board targets require an explicit clock assumption")
        from praxis.compatibility import catalog, qualified_target
        compatibility = catalog()
        if self.knowledge_adapter is not None:
            if any(not value.strip() for value in (self.mcu, self.package, self.silicon_revision,
                                                  self.board_revision, self.primary_mcu_ref)):
                raise ValueError("Custom knowledge targets require explicit nonempty identity fields")
            pattern = compatibility["identity_patterns"].get(self.family)
            if pattern is not None and not re.fullmatch(pattern, self.mcu):
                raise ValueError("Target identity does not match its declared family")
            if self.family in compatibility["adapter_excluded_families"] or any(
                    self.mcu == entry["mcu"] for entry in compatibility["targets"]):
                raise ValueError("Knowledge adapters cannot override validated builtin target identities")
            return self
        qualified = qualified_target(self)
        if qualified is None:
            raise ValueError("Unsupported MCU/package for the v1 validated target adapters")
        if self.clock_hz != qualified["clock_hz"]:
            raise ValueError("Target must use its validated clock profile")
        if qualified["require_fuses"] and not self.fuse_assumptions:
            raise ValueError("AVR profiles must state the external clock/fuse assumptions")
        return self


class BitField(Record):
    name: str
    lsb: int = Field(ge=0, lt=32)
    width: int = Field(gt=0, le=32)
    mask: int = Field(ge=0, le=0xFFFFFFFF)
    meaning: str
    sources: list[SourceRef] = Field(min_length=1)

    @model_validator(mode="after")
    def check_mask(self):
        if self.lsb + self.width > 32 or self.mask != ((1 << self.width) - 1) << self.lsb:
            raise ValueError(f"{self.name}: mask disagrees with lsb/width")
        return self


class StorageView(Record):
    """A C union member, without a claim about legal hardware bus accesses."""
    name: MacroName
    c_type: str = Field(min_length=1)
    width: Literal[8, 16, 32]
    sources: list[SourceRef] = Field(min_length=1)


class FieldView(Record):
    """Alternative interpretation of register bits, not a C storage alias."""

    selection: str = Field(min_length=1)
    fields: list[BitField] = Field(min_length=1)
    sources: list[SourceRef] = Field(min_length=1)


class Register(Record):
    name: str
    offset: int = Field(ge=0)
    width: Literal[8, 16, 32]
    count: int = Field(default=1, ge=1, le=1024)
    io_address: int | None = None
    access: Literal["RO", "RW", "WO", "mixed", "unknown"]
    access_widths: list[Literal[8, 16, 32]] = []
    write_mask: int | None = Field(default=None, ge=0, le=0xFFFFFFFF)
    reset: int | None = None
    side_effects: str = Field(min_length=1)
    fields: list[BitField] = []
    sources: list[SourceRef] = Field(min_length=1)
    storage_views: list[StorageView] = []
    field_views: dict[Identifier, FieldView] = {}

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if self.write_mask is None:
            value.pop("write_mask", None)
        if not self.storage_views:
            value.pop("storage_views", None)
        if not self.field_views:
            value.pop("field_views", None)
        return value

    def fields_for(self, view: str | None = None) -> list[BitField]:
        """Common fields plus exactly one explicitly selected interpretation."""
        return [*self.fields, *(self.field_views[view].fields if view is not None else [])]

    @model_validator(mode="after")
    def check_fields(self):
        if (len({view.name for view in self.storage_views}) != len(self.storage_views)
                or any(view.width > self.width for view in self.storage_views)):
            raise ValueError(f"{self.name}: storage views must be unique and fit the declared storage")
        if self.write_mask is not None and (
                self.write_mask >= 1 << self.width or self.access == "unknown"
                or self.access == "RO" and self.write_mask != 0):
            raise ValueError(f"{self.name}: reviewed write mask requires known access and valid width")
        if (len(set(self.access_widths)) != len(self.access_widths)
                or any(self.offset % (width // 8) for width in self.access_widths)):
            raise ValueError(f"{self.name}: access widths must be unique and naturally aligned")
        if self.reset is not None and not 0 <= self.reset < 1 << self.width:
            raise ValueError(f"{self.name}: reset exceeds register width")
        envelope = 0
        for view in [None, *self.field_views]:
            used = 0
            fields = self.fields_for(view)
            if len({field.name for field in fields}) != len(fields):
                raise ValueError(f"{self.name}: duplicate canonical field name in view {view}")
            for field in fields:
                if field.mask >= 1 << self.width or used & field.mask:
                    raise ValueError(f"{self.name}: overlapping or out-of-range fields in view {view}")
                used |= field.mask
            envelope |= used
        if self.write_mask is not None and envelope and self.write_mask & ~envelope:
            raise ValueError(f"{self.name}: reviewed write mask exceeds the declared field envelope")
        return self


class Instance(Record):
    name: str
    base_address: int = Field(ge=0)
    bus: str
    clock: str
    sources: list[SourceRef] = Field(min_length=1)


class ModeDependency(Record):
    peripheral: Identifier
    mode: Identifier
    instances: list[str] = Field(min_length=1)

    @model_validator(mode="after")
    def exact_instances(self):
        if (len(set(self.instances)) != len(self.instances) or any(
                not name or name != name.strip() or len(name) > 128
                or any(ord(c) < 32 or ord(c) == 127 for c in name) for name in self.instances)):
            raise ValueError("Mode dependencies require unique exact instance identities")
        return self


class OperatingMode(Record):
    """Reviewed, instance-scoped operating contract; not a whole-peripheral claim."""

    title: str = Field(min_length=1)
    instances: list[str] = Field(min_length=1)
    registers: list[str] = Field(min_length=1)
    fields: dict[str, list[str]] = {}
    field_views: dict[str, Identifier] = {}
    requirements: list[str] = Field(min_length=1)
    sources: list[SourceRef] = Field(min_length=1)
    requires_modes: list[ModeDependency] = []

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if not self.field_views:
            value.pop("field_views", None)
        return value

    @model_validator(mode="after")
    def explicit_scope(self):
        for values in (self.instances, self.registers, self.requirements, *self.fields.values()):
            if not values or any(not v.strip() for v in values) or len(set(values)) != len(values):
                raise ValueError("Operating mode scope and requirements must be nonempty and unique")
        if not self.fields.keys() <= set(self.registers):
            raise ValueError("Mode fields must name required registers")
        if not self.field_views.keys() <= set(self.registers):
            raise ValueError("Mode field views must name required registers")
        keys = [(dependency.peripheral, dependency.mode) for dependency in self.requires_modes]
        if len(keys) != len(set(keys)):
            raise ValueError("Duplicate required mode; combine its exact instance scope")
        return self


class Peripheral(Record):
    id: Identifier
    title: str
    prerequisites: list[Identifier] = []
    instances: list[Instance] = Field(min_length=1)
    registers: list[Register] = Field(min_length=1)
    reviewed_markdown: str
    review: Review | None
    operating_modes: dict[Identifier, OperatingMode] = {}

    @model_validator(mode="after")
    def unique_registers(self):
        if self.operating_modes and self.review is None:
            raise ValueError("Operating modes require an actual editorial review")
        if len({i.name for i in self.instances}) != len(self.instances):
            raise ValueError(f"{self.id}: duplicate canonical instance name")
        names = [r.name for r in self.registers]
        offsets = [r.offset for r in self.registers]
        if len(names) != len(set(names)) or len(offsets) != len(set(offsets)):
            raise ValueError(f"{self.id}: duplicate register name or offset")
        end = 0
        for register in sorted(self.registers, key=lambda r: r.offset):
            if register.offset < end:
                raise ValueError(f"{self.id}: overlapping register arrays")
            end = register.offset + register.count * register.width // 8
        available = {r.name: r for r in self.registers}
        for mode in self.operating_modes.values():
            if not set(mode.instances) <= {i.name for i in self.instances}:
                raise ValueError("Operating mode names an undeclared instance")
            if not set(mode.registers) <= available.keys():
                raise ValueError("Operating mode names an undeclared register")
            if any(available[r].access == "unknown" for r in mode.registers):
                raise ValueError("Operating mode requires reviewed register access semantics")
            for name in mode.registers:
                view = mode.field_views.get(name)
                if available[name].field_views and view is None:
                    raise ValueError("Operating mode must select an explicit register field view")
                if view is not None and view not in available[name].field_views:
                    raise ValueError("Operating mode selects an undeclared register field view")
            for register, fields in mode.fields.items():
                if not set(fields) <= {f.name for f in available[register].fields_for(mode.field_views.get(register))}:
                    raise ValueError("Operating mode names an undeclared bit field")
        return self


class DefinitionExtension(Record):
    """Reviewed additions/replacements pinned to exact base definition bytes."""

    schema_version: Literal[1] = 1
    base_sha256: Digest
    parent_definitions_sha256: Digest | None = None
    applicable_mcus: list[str] = Field(min_length=1)
    additions: list[Peripheral] = []
    replacements: list[Peripheral] = []

    @model_validator(mode="after")
    def explicit_changes(self):
        names = [p.id for p in self.additions + self.replacements]
        if (not names or len(names) != len(set(names))
                or len(self.applicable_mcus) != len(set(self.applicable_mcus))
                or any(not name.strip() for name in self.applicable_mcus)):
            raise ValueError("Extensions require changes, unique identities and explicit MCU applicability")
        return self


class Pin(Record):
    ref: str = Field(min_length=1, max_length=64)
    number: str = Field(min_length=1, max_length=16)
    name: str = Field(min_length=1, max_length=128)
    sheet: str
    package: str
    sources: list[SourceRef] = Field(min_length=1)

    @field_validator("ref", "number", "name")
    @classmethod
    def clean_identity(cls, value):
        if value != value.strip() or any(ord(c) < 32 or ord(c) == 127 for c in value):
            raise ValueError("Pin identities cannot contain controls or surrounding whitespace")
        return value

    @field_validator("ref", "number")
    @classmethod
    def endpoint_components(cls, value):
        if ":" in value:
            raise ValueError("Endpoint components cannot contain ':'")
        return value

    @property
    def endpoint(self) -> str:
        return f"{self.ref}:{self.number}"


class Net(Record):
    name: str = Field(min_length=1, max_length=128)
    pins: list[Pin] = Field(min_length=1)
    aliases: list[str] = []
    sources: list[SourceRef] = Field(min_length=1)

    @field_validator("name")
    @classmethod
    def clean_identity(cls, value):
        if value != value.strip() or any(ord(c) < 32 or ord(c) == 127 for c in value):
            raise ValueError("Net identities cannot contain controls or surrounding whitespace")
        return value

    @field_validator("aliases")
    @classmethod
    def clean_aliases(cls, values):
        for value in values:
            cls.clean_identity(value)
            if not value or len(value) > 128 or ";" in value:
                raise ValueError("Signal aliases must have 1–128 characters and no ';'")
        return values


class Component(Record):
    ref: str = Field(min_length=1, max_length=64)
    value: str = Field(min_length=1, max_length=256)
    package: str = Field(max_length=256)
    sheet: str = Field(min_length=1, max_length=256)
    kind: Literal["mcu", "resistor", "led", "switch", "bridge", "other"] = "other"
    fitted: bool = True
    pins: dict[str, str] = Field(max_length=256)
    properties: dict[str, str] = {}
    sources: list[SourceRef] = Field(min_length=1)

    @field_validator("ref")
    @classmethod
    def reference(cls, value):
        Pin.clean_identity(value)
        return Pin.endpoint_components(value)

    @field_validator("pins")
    @classmethod
    def pin_identities(cls, values):
        for number, name in values.items():
            Pin.clean_identity(number)
            Pin.endpoint_components(number)
            Pin.clean_identity(name)
        return values


class Schematic(Record):
    components: list[Component] = Field(min_length=1)
    nets: list[Net] = Field(min_length=1)


class ReviewedSchematic(Schematic):
    schema_version: Literal[1] = 1
    mcu: str
    package: str
    board_revision: str
    coverage: Literal["partial", "complete"]
    omissions: list[str]
    review: Review


class Dependency(Record):
    entity: Identifier
    requires: list[Identifier]


class Manifest(Record):
    schema_version: Literal[1, 2] = 1
    compiler_version: str
    bundle_revision: Digest
    target: Target
    review: Review
    sources: list[Source] = Field(min_length=1)
    extractor_versions: dict[str, str]
    documents: dict[str, str]
    peripherals: dict[str, str]
    aliases: dict[str, str]
    dependencies: list[Dependency]
    netlist: str
    topology: list[str] = []
    file_hashes: dict[str, Digest]

    @field_validator("peripherals", "aliases")
    @classmethod
    def canonical_keys(cls, value):
        if any(not re.fullmatch(r"[a-z][a-z0-9_]{0,63}", key) for key in value):
            raise ValueError("Peripheral names and aliases must be canonical identifiers")
        return value


class TopologyNode(Record):
    path: str
    enabled: bool
    properties: dict[str, str]
    decoded: dict[str, object]
    unresolved: list[str]
    sources: list[SourceRef] = Field(min_length=1)


class SourceSpec(Record):
    id: Identifier
    path: str
    authority: Literal["declarations", "connectivity", "semantics", "pinout", "configuration"]
    version: str
    license: str
    origin: str
    expected_sha256: Digest | None = None

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if self.expected_sha256 is None:
            value.pop("expected_sha256", None)
        return value


class HeaderSpec(Record):
    source: Identifier
    kind: Literal["cmsis", "avr"]
    defines: list[str] = []
    include_directories: list[str] = []
    structures: dict[str, str] = {}
    members: dict[str, dict[str, str]] = {}
    base_macros: dict[str, str] = {}
    constant_macros: dict[str, int] = {}
    field_expressions: dict[str, str] = {}
    discover: bool = False
    required_registers: dict[str, list[str]] = {}

    @field_validator("defines")
    @classmethod
    def only_defines(cls, value):
        if any(not re.fullmatch(r"-D[A-Za-z_]\w*(?:=[A-Za-z0-9_]+)?", flag) for flag in value):
            raise ValueError("Only literal -D definitions are permitted")
        return value


class PeripheralDiscovery(Record):
    structure: str = Field(pattern=r"^[A-Za-z_]\w*$")
    prefix: str | None = Field(default=None, pattern=r"^[A-Za-z_]\w*$")
    prerequisites: list[Identifier] | None = None
    instances: dict[str, str] = {}
    register_prefixes: dict[str, str] = {}
    expand_arrays: list[str] = []
    member_views: dict[MacroName, list[MacroName]] = {}
    register_fields: dict[str, list[str]] = {}
    field_views: dict[str, dict[Identifier, list[str]]] = {}

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if not self.field_views:
            value.pop("field_views", None)
        return value

    @model_validator(mode="after")
    def explicit_views(self):
        if len(set(self.expand_arrays)) != len(self.expand_arrays):
            raise ValueError("Duplicate expanded array member")
        if self.member_views.keys() & set(self.expand_arrays):
            raise ValueError("A member cannot have both a named view and numeric expansion")
        for names in self.member_views.values():
            if not names or len(set(names)) != len(names):
                raise ValueError("Member views require unique, nonempty register names")
        for names in self.register_fields.values():
            if not names or len(set(names)) != len(names):
                raise ValueError("Register field views require unique, nonempty field names")
        if self.field_views.keys() & self.register_fields.keys():
            raise ValueError("A register cannot have both a legacy field selection and alternative field views")
        for views in self.field_views.values():
            if not views or any(not names or len(set(names)) != len(names) for names in views.values()):
                raise ValueError("Alternative field views require nonempty, unique field names")
        return self


class DiscoveryPolicy(Record):
    """Inventory all typed register blocks; publish only an explicitly selected policy."""

    automatic: bool = False
    peripherals: dict[Identifier, PeripheralDiscovery] = {}
    exclude: list[Identifier] = []
    default_prerequisites: list[Identifier] = []


class ManualSpec(Record):
    """Literal document vocabulary and explicit symbol/table scope, never code."""

    register_symbols: dict[Identifier, dict[str, list[str]]] = {}
    table_scopes: dict[str, Identifier] = {}
    labels: dict[Literal["register", "offset", "reset", "access", "field", "bits"], list[str]] = {
        "register": ["Register", "Register name"],
        "offset": ["Address offset", "Offset"],
        "reset": ["Reset value", "Reset"],
        "access": ["Access", "Access type"],
        "field": ["Field", "Field name"],
        "bits": ["Bits", "Bit positions"],
    }

    @model_validator(mode="after")
    def unambiguous_vocabulary(self):
        seen = set()
        for names in self.labels.values():
            for name in names:
                normalized = " ".join(name.split()).casefold()
                if not normalized or len(name) > 64 or normalized in seen or ':' in name:
                    raise ValueError("Manual labels must be unique bounded literal names without ':'")
                seen.add(normalized)
        for registers in self.register_symbols.values():
            for symbols in registers.values():
                if not symbols or len(symbols) != len(set(symbols)) or any(
                    not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,127}", s) for s in symbols
                ):
                    raise ValueError("Manual register symbols must be unique literal identifiers")
        return self


class WorkflowRequirement(Record):
    peripherals: list[Identifier] = Field(min_length=1)
    registers: dict[Identifier, list[str]] = {}
    operating_semantics: bool = True
    instances: dict[Identifier, list[str]] = {}
    modes: dict[Identifier, list[Identifier]] = {}
    mode_instances: dict[Identifier, dict[Identifier, list[str]]] = {}
    signals: list[str] = []

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if not self.mode_instances:
            value.pop("mode_instances", None)
        return value

    @model_validator(mode="after")
    def mode_scope(self):
        if not (self.instances.keys() | self.modes.keys()) <= set(self.peripherals):
            raise ValueError("Instance/mode requirements must name workflow peripherals")
        if self.modes and not self.operating_semantics:
            raise ValueError("Mode requirements cannot disable operating-semantic checks")
        for values in (*self.instances.values(), *self.modes.values()):
            if not values or len(set(values)) != len(values):
                raise ValueError("Instance/mode requirements must be nonempty and unique")
        if not self.mode_instances.keys() <= self.modes.keys():
            raise ValueError("Per-mode instances must name selected workflow modes")
        for entity, scopes in self.mode_instances.items():
            if scopes.keys() != set(self.modes[entity]):
                raise ValueError("Per-mode instances must cover every selected mode of that entity")
            for names in scopes.values():
                ModeDependency(peripheral=entity, mode="scope", instances=names)
            union = {name for names in scopes.values() for name in names}
            if entity in self.instances and union != set(self.instances[entity]):
                raise ValueError("Workflow instance scope must equal the union of its per-mode instances")
        if (len(set(self.signals)) != len(self.signals) or any(not s.strip() or len(s) > 128
                or any(ord(c) < 32 or ord(c) == 127 for c in s) for s in self.signals)):
            raise ValueError("Workflow signal queries must be unique, bounded and nonempty")
        return self


class DtsSpec(Record):
    source: Identifier
    overlays: list[Identifier] = []
    includes: list[Identifier] = []


class Profile(Record):
    schema_version: Literal[1] = 1
    target: Target
    review: Review
    sources: list[SourceSpec] = Field(min_length=1)
    definitions: Identifier
    compilation_contract: Identifier
    definition_extensions: list[Identifier] = []
    header: HeaderSpec
    netlist: Identifier | None = None
    pin_map: dict[str, str] = {}
    aliases: dict[str, Identifier] = {}
    signal_aliases: dict[str, list[str]] = {}
    devicetree: DtsSpec | None = None
    clock_plan: dict[MacroName, StrictInt] | None = None
    web_imports: dict[Identifier, str] = {}
    netlist_format: Literal["kicad", "reviewed"] = "kicad"
    board: Identifier | None = None
    required_workflows: list[Literal["led_button_polling"]] = []
    discovery: DiscoveryPolicy | None = None
    manuals: dict[Identifier, ManualSpec] = {}
    workflows: dict[Identifier, WorkflowRequirement] = {}
    publication_requires: list[Identifier] = []

    @model_validator(mode="after")
    def clock_applicability(self):
        if self.target.scope == "mcu":
            if self.netlist is not None or self.pin_map or self.signal_aliases or self.board or self.required_workflows:
                raise ValueError("MCU-only profiles cannot claim board sources, pin mappings or board workflows")
        elif self.netlist is None:
            raise ValueError("Board profiles require a schematic netlist source")
        if self.target.knowledge_adapter is not None and (
                self.discovery is None or not self.header.discover or self.header.kind != "cmsis"):
            raise ValueError("Custom knowledge targets require configurable CMSIS discovery")
        if len(self.definition_extensions) != len(set(self.definition_extensions)):
            raise ValueError("Definition extension sources must be unique")
        if self.discovery is not None and (not self.header.discover or self.header.kind != "cmsis"):
            raise ValueError("Configurable discovery requires header.discover and the CMSIS adapter")
        if not set(self.publication_requires) <= self.workflows.keys():
            raise ValueError("publication_requires must name declared workflows")
        if (not self.target.example_only or self.required_workflows) and self.board is None:
            raise ValueError("Documented boards and board workflows require a reviewed board source")
        return self


