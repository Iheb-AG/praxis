"""Versioned compiler IR and bundle manifest. No vendor guesses or implicit targets."""

from __future__ import annotations

import re
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_serializer, model_validator

Identifier = Annotated[str, Field(pattern=r"^[a-z][a-z0-9_]*$", max_length=64)]
Digest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]
MAX_DOCUMENT_BYTES = 64 * 1024


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
    clock_hz: int = Field(gt=0)
    clock_assumptions: list[str] = Field(min_length=1)
    fuse_assumptions: list[str] = []
    knowledge_adapter: CortexMKnowledgeAdapter | None = None

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        # Existing immutable bundle revisions must retain their original bytes/hash input.
        value = handler(self)
        if self.knowledge_adapter is None:
            value.pop("knowledge_adapter", None)
        return value

    @model_validator(mode="after")
    def supported_fixture(self):
        supported = {
            "stm32": {
                ("STM32F401RE", "Package_QFP:LQFP-64_10x10mm_P0.5mm"): 16_000_000,
                ("STM32F407VGT6", "Package_QFP:LQFP-100_14x14mm_P0.5mm"): 168_000_000,
            },
            "avr": {("ATmega328P-PU", "Package_DIP:DIP-28_W7.62mm"): 16_000_000},
        }
        if self.knowledge_adapter is not None:
            if any(not value.strip() for value in (self.mcu, self.package, self.silicon_revision,
                                                  self.board_revision, self.primary_mcu_ref)):
                raise ValueError("Custom knowledge targets require explicit nonempty identity fields")
            if self.family == "stm32" and not re.fullmatch(r"STM32[A-Z0-9]{4,24}", self.mcu):
                raise ValueError("Custom STM32 profiles require an explicit STM32 part identity")
            if self.family == "avr" or any(
                    self.mcu == model for entries in supported.values() for model, _ in entries):
                raise ValueError("Knowledge adapters cannot override validated builtin target identities")
            return self
        clock = supported.get(self.family, {}).get((self.mcu, self.package))
        if clock is None:
            raise ValueError("Unsupported MCU/package for the v1 validated target adapters")
        if self.clock_hz != clock:
            raise ValueError("Target must use its validated clock profile")
        if self.family == "avr" and not self.fuse_assumptions:
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

    @model_serializer(mode="wrap")
    def serialize(self, handler):
        value = handler(self)
        if self.write_mask is None:
            value.pop("write_mask", None)
        return value

    @model_validator(mode="after")
    def check_fields(self):
        if self.write_mask is not None and (
                self.write_mask >= 1 << self.width or self.access == "unknown"
                or self.access == "RO" and self.write_mask != 0):
            raise ValueError(f"{self.name}: reviewed write mask requires known access and valid width")
        if (len(set(self.access_widths)) != len(self.access_widths)
                or any(self.offset % (width // 8) for width in self.access_widths)):
            raise ValueError(f"{self.name}: access widths must be unique and naturally aligned")
        used = 0
        if len({field.name for field in self.fields}) != len(self.fields):
            raise ValueError(f"{self.name}: duplicate canonical field name")
        if self.reset is not None and not 0 <= self.reset < 1 << self.width:
            raise ValueError(f"{self.name}: reset exceeds register width")
        for field in self.fields:
            if field.mask >= 1 << self.width or used & field.mask:
                raise ValueError(f"{self.name}: overlapping or out-of-range fields")
            used |= field.mask
        if self.write_mask is not None and self.fields and self.write_mask & ~used:
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
    requirements: list[str] = Field(min_length=1)
    sources: list[SourceRef] = Field(min_length=1)
    requires_modes: list[ModeDependency] = []

    @model_validator(mode="after")
    def explicit_scope(self):
        for values in (self.instances, self.registers, self.requirements, *self.fields.values()):
            if not values or any(not v.strip() for v in values) or len(set(values)) != len(values):
                raise ValueError("Operating mode scope and requirements must be nonempty and unique")
        if not self.fields.keys() <= set(self.registers):
            raise ValueError("Mode fields must name required registers")
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
            for register, fields in mode.fields.items():
                if not set(fields) <= {f.name for f in available[register].fields}:
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
    register_fields: dict[str, list[str]] = {}

    @model_validator(mode="after")
    def explicit_views(self):
        if len(set(self.expand_arrays)) != len(self.expand_arrays):
            raise ValueError("Duplicate expanded array member")
        for names in self.register_fields.values():
            if not names or len(set(names)) != len(names):
                raise ValueError("Register field views require unique, nonempty field names")
        return self


class DiscoveryPolicy(Record):
    """Inventory all typed register blocks; publish only an explicitly selected policy."""

    automatic: bool = False
    peripherals: dict[Identifier, PeripheralDiscovery] = {}
    exclude: list[Identifier] = []
    default_prerequisites: list[Identifier] = ["rcc"]


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
    signals: list[str] = []

    @model_validator(mode="after")
    def mode_scope(self):
        if not (self.instances.keys() | self.modes.keys()) <= set(self.peripherals):
            raise ValueError("Instance/mode requirements must name workflow peripherals")
        if self.modes and not self.operating_semantics:
            raise ValueError("Mode requirements cannot disable operating-semantic checks")
        for values in (*self.instances.values(), *self.modes.values()):
            if not values or len(set(values)) != len(values):
                raise ValueError("Instance/mode requirements must be nonempty and unique")
        if (len(set(self.signals)) != len(self.signals) or any(not s.strip() or len(s) > 128
                or any(ord(c) < 32 or ord(c) == 127 for c in s) for s in self.signals)):
            raise ValueError("Workflow signal queries must be unique, bounded and nonempty")
        return self


class DtsSpec(Record):
    source: Identifier
    overlays: list[Identifier] = []
    includes: list[Identifier] = []


class F407ClockPlan(Record):
    hse_hz: int = Field(gt=0)
    pll_m: int = Field(ge=2, le=63)
    pll_n: int = Field(ge=192, le=432)
    pll_p: Literal[2, 4, 6, 8]
    pll_q: int = Field(ge=2, le=15)
    ahb_div: Literal[1, 2, 4, 8, 16, 64, 128, 256, 512]
    apb1_div: Literal[1, 2, 4, 8, 16]
    apb2_div: Literal[1, 2, 4, 8, 16]
    vdd_mv: int
    flash_wait_states: int

    @model_validator(mode="after")
    def validated_clock_profile(self):
        # A deliberately narrow, source-reviewed v1 operating point.
        if ((self.hse_hz, self.pll_m, self.pll_n, self.pll_p, self.pll_q,
             self.ahb_div, self.apb1_div, self.apb2_div) !=
                (8_000_000, 8, 336, 2, 7, 1, 4, 2)):
            raise ValueError("F407 workflow requires HSE8, M8/N336/P2/Q7, AHB/1, APB1/4, APB2/2")
        if not 2700 <= self.vdd_mv <= 3600 or self.flash_wait_states != 5:
            raise ValueError("168 MHz profile requires reviewed 2.7–3.6 V supply and 5 FLASH wait states")
        return self


class Profile(Record):
    schema_version: Literal[1] = 1
    target: Target
    review: Review
    sources: list[SourceSpec] = Field(min_length=1)
    definitions: Identifier
    definition_extensions: list[Identifier] = []
    header: HeaderSpec
    netlist: Identifier
    pin_map: dict[str, str]
    aliases: dict[str, Identifier] = {}
    signal_aliases: dict[str, list[str]] = {}
    devicetree: DtsSpec | None = None
    clock_plan: F407ClockPlan | None = None
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
        if self.target.knowledge_adapter is not None and (
                self.discovery is None or not self.header.discover or self.header.kind != "cmsis"):
            raise ValueError("Custom knowledge targets require configurable CMSIS discovery")
        if len(self.definition_extensions) != len(set(self.definition_extensions)):
            raise ValueError("Definition extension sources must be unique")
        if self.discovery is not None and (not self.header.discover or self.header.kind != "cmsis"):
            raise ValueError("Configurable discovery requires header.discover and the CMSIS adapter")
        if not set(self.publication_requires) <= self.workflows.keys():
            raise ValueError("publication_requires must name declared workflows")
        if (self.target.mcu == "STM32F407VGT6") != (self.clock_plan is not None):
            raise ValueError("Only STM32F407VGT6 requires the explicit F407 clock plan")
        if (not self.target.example_only or self.required_workflows) and self.board is None:
            raise ValueError("Documented boards and board workflows require a reviewed board source")
        return self


