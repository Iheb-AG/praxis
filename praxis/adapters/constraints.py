"""Source-format-specific header verification, independent of target publication policy."""
from __future__ import annotations

import re
from importlib.metadata import version

from praxis.errors import PraxisError
from praxis.process import run


def validate_headers(profile, paths, items, root, contract):
    from praxis.adapters.headers import avr, cmsis, macros
    from praxis.expressions import integer

    spec = profile.header
    header = paths[spec.source]
    include_flags = []
    for name in spec.include_directories:
        directory = (root / name).resolve(strict=True)
        if not directory.is_relative_to(root) or not directory.is_dir():
            raise PraxisError("INVALID_PATH", "Header include directory escapes source tree")
        include_flags.append(f"-I{directory}")
    defines = [*spec.defines, *include_flags]
    by_id = {p.id: p for p in items}
    versions = {}
    if spec.kind == "cmsis":
        layouts = cmsis(header, sorted(set(spec.structures.values())), defines,
                        registered_sources=list(paths.values()), cpu=contract.cpu)
        versions["clang"] = run(["clang", "--version"]).splitlines()[0]
        versions["libclang"] = version("libclang")
        compiler = "arm-none-eabi-gcc"
        flags = [f"-mcpu={contract.cpu}", "-mthumb", *defines]
        for name, item in by_id.items():
            if name not in spec.structures or name not in spec.members:
                raise PraxisError("MISSING_DECLARATION", f"No header mapping for {name}")
            fields = layouts[spec.structures[name]]
            for register in item.registers:
                member = spec.members[name].get(register.name, register.name)
                if member in fields:
                    layout = fields[member]
                    if [view.model_dump(exclude={"sources"}) for view in register.storage_views] != layout.get("views", []):
                        raise PraxisError("DECLARATION_CONFLICT", f"{name}.{member}: union storage views differ")
                    if (register.offset, register.width, register.count) != (layout["offset"], layout["width"], layout["count"]):
                        raise PraxisError("DECLARATION_CONFLICT", f"{name}.{member}: register layout differs")
                    continue
                match = re.fullmatch(r"(\w+)(?:\[(\d+)\])?", member)
                if not match or match[1] not in fields:
                    raise PraxisError("MISSING_DECLARATION", f"Missing {name}.{member}")
                layout = fields[match[1]]
                if [view.model_dump(exclude={"sources"}) for view in register.storage_views] != layout.get("views", []):
                    raise PraxisError("DECLARATION_CONFLICT", f"{name}.{member}: union storage views differ")
                index = int(match[2] or 0)
                if index >= layout["count"]:
                    raise PraxisError("DECLARATION_CONFLICT", f"Array index out of bounds: {member}")
                offset = layout["offset"] + index * layout["width"] // 8
                if register.offset != offset or register.width != layout["width"]:
                    raise PraxisError("DECLARATION_CONFLICT", f"{name}.{member}: header layout differs from reviewed facts")
                if register.count > 1 and (match[2] is not None or register.count != layout["count"]):
                    raise PraxisError("DECLARATION_CONFLICT", f"{name}.{member}: register array count differs")
    else:
        compiler = "avr-gcc"
        flags = [f"-mmcu={contract.avr_mcu}", *defines]
        registers = avr(header, sorted({r.name for p in items for r in p.registers}), flags)
        for item in items:
            for register in item.registers:
                extracted = registers[register.name]
                if (register.offset != extracted["offset"] or register.width != extracted["width"]
                        or register.io_address != extracted["io_address"]):
                    raise PraxisError("DECLARATION_CONFLICT", f"{register.name}: AVR address/width mismatch")
    versions[compiler] = run([compiler, "--version"]).splitlines()[0]
    definitions = macros(header, compiler, flags)
    missing = sorted(set(contract.header_identity) - definitions.keys())
    if missing:
        raise PraxisError("TARGET_MISMATCH", f"Header identity does not match contract; missing {missing}")
    instances = {i.name: i for p in items for i in p.instances}
    for name, expression in spec.base_macros.items():
        if name not in instances or (re.fullmatch(r"[A-Za-z_]\w*", expression) and expression not in definitions):
            raise PraxisError("MISSING_DECLARATION", f"Missing instance or macro {name}:{expression}")
        if integer(definitions.get(expression, expression), definitions) != instances[name].base_address:
            raise PraxisError("DECLARATION_CONFLICT", f"Base address mismatch: {name}")
    for name, expected in spec.constant_macros.items():
        if name not in definitions or integer(definitions[name], definitions) != expected:
            raise PraxisError("DECLARATION_CONFLICT", f"Constant macro mismatch: {name}")
    fields = {f"{p.id}.{r.name}.{f.name}": f for p in items for r in p.registers for f in r.fields}
    fields.update({f"{p.id}.{r.name}.{view}.{f.name}": f for p in items for r in p.registers
                   for view, record in r.field_views.items() for f in record.fields})
    if set(spec.field_expressions) != set(fields):
        raise PraxisError("MISSING_DECLARATION", "Every published field requires exactly one header-backed mask expression")
    for name, field in fields.items():
        if integer(spec.field_expressions[name], definitions) != field.mask:
            raise PraxisError("DECLARATION_CONFLICT", f"Bit-field mask differs from header: {name}")
    return versions

