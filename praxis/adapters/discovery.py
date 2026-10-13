"""Target-aware CMSIS declaration discovery. Operating semantics are never guessed.

Clang computes ABI offsets, including reserved gaps and arrays. The target C
preprocessor resolves includes/conditionals; the restricted integer evaluator
decodes object macros. Core register arrays remain arrays, rather than hundreds
of repeated Markdown rows. This module executes no input build scripts.
"""

from __future__ import annotations

import re
from pathlib import Path

from pydantic import Field

from praxis.adapters.headers import cmsis, macros
from praxis.errors import PraxisError
from praxis.expressions import integer
from praxis.models import BitField, CortexCPU, Record, Register, SourceRef

STRUCTURES = {"rcc": "RCC_TypeDef", "gpio": "GPIO_TypeDef",
              "usart": "USART_TypeDef", "nvic": "NVIC_Type"}


class Declaration(Record):
    structure: str
    source_id: str = "header"
    instance_sources: dict[str, str] = {}
    instances: dict[str, int]
    registers: list[Register] = Field(min_length=1)
    members: dict[str, str]
    field_expressions: dict[str, str]
    base_macros: dict[str, str] = {}
    notes: list[str] = []
    unresolved_masks: list[str] = []


def _fields(prefix: str, width: int, definitions: dict[str, str], source: str,
            *, aggregate: bool = False, selected: list[str] | None = None,
            mask_suffix: str = "_Msk", position_suffix: str = "_Pos",
            macro_sources: dict[str, str] | None = None):
    if selected is not None:
        missing = [name for name in selected if f"{prefix}_{name}{mask_suffix}" not in definitions]
        if missing:
            raise PraxisError("MISSING_DECLARATION", f"{prefix}: unknown configured fields {missing}")
    candidates = []
    for macro in sorted(definitions):
        if not macro.startswith(prefix + "_") or not macro.endswith(mask_suffix):
            continue
        name = macro[len(prefix) + 1:-len(mask_suffix)]
        if selected is not None and name not in selected:
            continue
        mask = integer(definitions[macro], definitions)
        if aggregate:
            # Vendor headers also label encoded enumeration values *_Msk.
            # An explicit name extension contained by a parent field is an encoding,
            # including non-contiguous values; it is not a separate field definition.
            parts = name.split("_")
            contained = False
            for stop in range(1, len(parts)):
                parent = prefix + "_" + "_".join(parts[:stop]) + mask_suffix
                if parent not in definitions:
                    continue
                enclosing = integer(definitions[parent], definitions)
                if enclosing > 0 and mask & enclosing == mask:
                    contained = True
                    break
            if contained:
                continue
        if mask <= 0 or mask >= 1 << width:
            raise PraxisError("INVALID_MASK", f"{macro}: mask exceeds register width")
        lsb = (mask & -mask).bit_length() - 1
        size = (mask >> lsb).bit_length()
        if ((1 << size) - 1) << lsb != mask:
            raise PraxisError("UNSUPPORTED_MASK", f"{macro}: non-contiguous bit field")
        position = macro.removesuffix(mask_suffix) + position_suffix
        if position in definitions and integer(definitions[position], definitions) != lsb:
            raise PraxisError("DECLARATION_CONFLICT", f"{macro}: position and mask disagree")
        alias = definitions[macro].strip()
        if alias.endswith(mask_suffix) and alias in definitions and alias.startswith(prefix + "_"):
            continue
        candidates.append((name, mask, lsb, size, macro))
    # CMSIS sometimes declares encoded-value aliases such as PLLSRC_HSE_Msk.
    # Collapse only equal masks whose names explicitly extend a parent name.
    selected = []
    ordering = (lambda c: (-c[3], len(c[0]), c[0])) if aggregate else (lambda c: (len(c[0]), c[0]))
    for entry in sorted(candidates, key=ordering):
        name, mask, lsb, size, macro = entry
        if any(mask == old[1] and name.startswith(old[0] + "_") for old in selected):
            continue
        if aggregate and any(mask & old[1] == mask for old in selected):
            # Keep the complete enclosing field, rather than overlapping encoded aliases.
            continue
        if any(mask & old[1] for old in selected):
            raise PraxisError("AMBIGUOUS_MASK", f"{prefix}: overlapping field declarations at {name}")
        selected.append(entry)
    fields, expressions = [], {}
    for name, mask, lsb, size, macro in sorted(selected, key=lambda c: (c[2], c[0])):
        fields.append(BitField(name=name, lsb=lsb, width=size, mask=mask,
                               meaning="Declaration only; encoding requires reviewed semantics.",
                               sources=[SourceRef(source=(macro_sources or {}).get(macro, source), locator=macro)]))
        expressions[name] = macro
    return fields, expressions


def parse_cmsis_headers(header: Path, *, include_directories: list[Path] | None = None,
                        defines: list[str] | None = None, source_id: str = "header",
                        core_source_id: str = "cmsis_core",
                        registered_sources: list[Path] | None = None,
                        structures: dict[str, str] | None = None,
                        prefixes: dict[str, str] | None = None,
                        layouts: dict | None = None, definitions: dict | None = None,
                        relaxed: bool = False,
                        instance_expressions: dict[str, dict[str, str]] | None = None,
                        register_prefixes: dict[str, dict[str, str]] | None = None,
                        expand_arrays: dict[str, list[str]] | None = None,
                        register_fields: dict[str, dict[str, list[str]]] | None = None,
                        cpu: CortexCPU = "cortex-m4",
                        structure_sources: dict[str, str] | None = None,
                        mask_suffix: str = "_Msk", position_suffix: str = "_Pos",
                        macro_sources: dict[str, str] | None = None,
                        stm32_views: bool = True) -> dict[str, Declaration]:
    """Discover complete RCC/GPIO/USART/NVIC layouts, bases and contiguous masks.

    Reset values are extracted only from explicit *_RESET_VALUE or *_RESET
    macros that are not named bit fields. Their absence stays None. C qualifiers do not establish hardware
    read/write behavior, so access and side effects require reviewed imports.
    GPIO AFR[2] becomes AFRL/AFRH; NVIC banks retain count and byte stride.
    """
    header = header.resolve(strict=True)
    if mask_suffix not in ("_Msk", "_MASK") or position_suffix not in ("_Pos", "_SHIFT"):
        raise PraxisError("INVALID_PROFILE", "Unsupported field macro naming convention")
    flags = list(defines or [])
    if any(not re.fullmatch(r"-D[A-Za-z_]\w*(?:=[A-Za-z0-9_]+)?", flag) for flag in flags):
        raise PraxisError("INVALID_FLAGS", "Only literal -D preprocessor definitions are accepted")
    for path in include_directories or [header.parent]:
        path = path.resolve(strict=True)
        if not path.is_dir():
            raise PraxisError("INVALID_PATH", "CMSIS include path must be a directory")
        flags.append(f"-I{path}")
    structures = STRUCTURES if structures is None else structures
    if layouts is None:
        layouts = cmsis(header, sorted(set(structures.values())), flags,
                        registered_sources=registered_sources, cpu=cpu)
    if definitions is None:
        definitions = macros(header, "arm-none-eabi-gcc", [f"-mcpu={cpu}", "-mthumb", *flags])
    catalog = {}
    for entity, structure in sorted(structures.items()):
        instances, bases = {}, {}
        for instance in sorted(definitions):
            match = re.fullmatch(r"\(\(\s*" + re.escape(structure) +
                                 r"\s*\*\s*\)\s*([A-Za-z_]\w*)\s*\)",
                                 definitions.get(instance, ""))
            if match:
                instances[instance] = integer(definitions[match[1]], definitions)
                bases[instance] = match[1]
        for instance, expression in (instance_expressions or {}).get(entity, {}).items():
            value = integer(expression, definitions)
            if instance in instances and value != instances[instance]:
                raise PraxisError("DECLARATION_CONFLICT", f"{instance}: explicit base differs from header")
            instances[instance], bases[instance] = value, expression
        if not instances:
            raise PraxisError("MISSING_DECLARATION", f"No base-address macros for {structure}")
        registers, members, expressions, unresolved = [], {}, {}, []
        expanded = set((expand_arrays or {}).get(entity, []))
        if not expanded <= layouts[structure].keys():
            raise PraxisError("MISSING_DECLARATION", f"{entity}: unknown expanded member")
        source = (structure_sources or {}).get(structure,
            core_source_id if structure in ("NVIC_Type", "SCB_Type", "SysTick_Type", "MPU_Type",
                                           "DWT_Type", "ITM_Type", "TPI_Type", "CoreDebug_Type") else source_id)
        for member, layout in sorted(layouts[structure].items(), key=lambda item: item[1]["offset"]):
            if any(part.upper().startswith("RESERVED") for part in member.split(".")):
                continue
            count = layout["count"]
            pieces = [(member, member, layout["offset"], count)]
            if member in expanded:
                if count < 2:
                    raise PraxisError("INVALID_PROFILE", f"{entity}.{member}: not an array")
                pieces = [(f"{member}{i}", f"{member}[{i}]",
                           layout["offset"] + i * layout["width"] // 8, 1) for i in range(count)]
            if stm32_views and entity == "gpio" and member == "AFR":
                if count != 2:
                    raise PraxisError("UNSUPPORTED_DECLARATION", "GPIO AFR must contain two registers")
                pieces = [("AFRL", "AFR[0]", layout["offset"], 1),
                          ("AFRH", "AFR[1]", layout["offset"] + layout["width"] // 8, 1)]
            for name, spelling, offset, length in pieces:
                # Nested register records retain the exact C member path for ABI checks.
                name = re.sub(r"[^A-Za-z0-9_]", "_", name).rstrip("_")
                macro_member = (re.sub(r"\[\d+\]", "", spelling).split(".")[-1]
                                if "." in spelling else name)
                prefix = f"{(prefixes or {}).get(entity, entity.upper())}_{macro_member}"
                prefix = (register_prefixes or {}).get(entity, {}).get(name, prefix)
                try:
                    fields, masks = _fields(prefix, layout["width"], definitions, source, aggregate=relaxed,
                        selected=(register_fields or {}).get(entity, {}).get(name),
                        mask_suffix=mask_suffix, position_suffix=position_suffix, macro_sources=macro_sources)
                except PraxisError as exc:
                    if not relaxed or name in (register_fields or {}).get(entity, {}):
                        raise
                    # Layouts remain useful even when a register's masks are ambiguous.
                    # Omit the entire field set for that register and report the failure.
                    fields, masks = [], {}
                    unresolved.append(f"{name}: bit fields withheld: {exc}")
                if entity == "nvic" and structure == "NVIC_Type" and name != "STIR":
                    if name == "IP":
                        expression = "((1 << __NVIC_PRIO_BITS) - 1) << (8 - __NVIC_PRIO_BITS)"
                        bits = integer(definitions["__NVIC_PRIO_BITS"], definitions)
                        if not 1 <= bits <= 8:
                            raise PraxisError("INVALID_MASK", "Invalid implemented NVIC priority width")
                        field = BitField(name="PRIORITY", lsb=8 - bits, width=bits,
                                         mask=integer(expression, definitions),
                                         meaning="Implemented high priority bits per byte.",
                                         sources=[SourceRef(source=source_id, locator="__NVIC_PRIO_BITS"),
                                                  SourceRef(source=core_source_id, locator="NVIC_Type.IP")])
                    else:
                        expression = "(1 << 32) - 1"
                        field = BitField(name="IRQ_BITS", lsb=0, width=32, mask=0xFFFFFFFF,
                                         meaning="Core bank width; only device IRQs are implemented.",
                                         sources=[SourceRef(source=core_source_id,
                                                            locator=f"NVIC_Type.{member}")])
                    fields, masks = [field], {field.name: expression}
                # Data/address registers need not have field macros. Preserve
                # their layout without inventing a full-width mask. Unsupported
                # or overlapping expressions still fail above in strict mode.
                resets = [macro for macro in (prefix + "_RESET_VALUE", prefix + "_RESET")
                          if macro in definitions
                          and not any(macro + suffix in definitions for suffix in (position_suffix, mask_suffix))]
                reset_values = {integer(definitions[macro], definitions) for macro in resets}
                if len(reset_values) > 1:
                    raise PraxisError("DECLARATION_CONFLICT", f"Conflicting reset macros for {prefix}")
                references = [SourceRef(source=source, locator=f"{structure}.{spelling}")]
                references.extend(SourceRef(source=(macro_sources or {}).get(macro, source), locator=macro)
                                  for macro in resets)
                registers.append(Register(name=name, offset=offset, width=layout["width"],
                                          count=length, access="unknown",
                                          reset=next(iter(reset_values), None),
                                          side_effects="Not asserted; consult reviewed operating semantics.",
                                          fields=fields, sources=references))
                members[name] = spelling
                expressions.update({f"{entity}.{name}.{field}": expr for field, expr in masks.items()})
        if not (register_fields or {}).get(entity, {}).keys() <= members.keys():
            raise PraxisError("MISSING_DECLARATION", f"{entity}: field view names an unknown register")
        catalog[entity] = Declaration(structure=structure, source_id=source,
                                      instance_sources={name: (macro_sources or {}).get(bases[name],
                                                         (macro_sources or {}).get(name, source))
                                                        for name in instances},
                                      instances=instances, registers=registers,
                                      members=members, field_expressions=expressions, base_macros=bases,
                                      notes=(["Enclosing masks represent contained aliases; absent masks remain unasserted."]
                                             if relaxed else []), unresolved_masks=unresolved)
    return catalog
