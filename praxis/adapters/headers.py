from __future__ import annotations

import re
from pathlib import Path

from praxis.errors import PraxisError
from praxis.expressions import integer
from praxis.process import run
from praxis.models import CortexCPU


def macros(header: Path, compiler: str, flags: list[str]) -> dict[str, str]:
    output = run([compiler, *flags, "-E", "-dM", "-x", "c", str(header)])
    result = {}
    for line in output.splitlines():
        match = re.fullmatch(r"#define ([A-Za-z_]\w*)(?: (.*))?", line)
        if match:
            result[match[1]] = match[2] or ""
    return result


def cmsis(header: Path, structures: list[str] | None, defines: list[str], *,
          registered_sources: list[Path] | None = None,
          failures: dict[str, str] | None = None, cpu: CortexCPU = "cortex-m4",
          origins: dict[str, Path] | None = None,
          macro_origins: dict[str, Path] | None = None,
          additional_structures: list[str] | None = None) -> dict[str, dict[str, dict]]:
    from typing import get_args
    if cpu not in get_args(CortexCPU):
        raise PraxisError("INVALID_PROFILE", "Unsupported Cortex-M extraction CPU")
    try:
        from clang import cindex
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[ingest] for libclang") from exc
    try:
        index = cindex.Index.create()
        search = run(["arm-none-eabi-gcc", "-E", "-Wp,-v", "-x", "c", "/dev/null"],
                     include_stderr=True)
        includes = [line.strip() for line in search.splitlines()
                    if line.startswith(" ") and Path(line.strip()).is_dir()]
        system_flags = [flag for path in includes for flag in ("-isystem", path)]
        unit = index.parse(str(header), args=["-target", "arm-none-eabi", f"-mcpu={cpu}",
                                             "-mfloat-abi=soft", "-ffreestanding", "-nostdinc",
                                             "-std=c11", *system_flags, *defines],
                           options=(cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD
                                    if macro_origins is not None else 0))
    except (cindex.LibclangError, cindex.TranslationUnitLoadError) as exc:
        raise PraxisError("EXTRACTOR_FAILED", f"Clang could not parse {header.name}: {exc}") from exc
    errors = [str(d) for d in unit.diagnostics if d.severity >= cindex.Diagnostic.Error]
    if errors:
        raise PraxisError("EXTRACTOR_FAILED", "\n".join(errors))
    if registered_sources is not None:
        registered = {path.resolve(strict=True) for path in registered_sources}
        local_dirs = [Path(flag[2:]).resolve() for flag in defines if flag.startswith("-I")]
        local_dirs.append(header.parent.resolve())
        for inclusion in unit.get_includes():
            included = Path(inclusion.include.name).resolve(strict=True)
            if included in registered:
                continue
            if (any(included.is_relative_to(path) for path in local_dirs) or
                    not any(included.is_relative_to(Path(path)) for path in includes)):
                raise PraxisError("UNREGISTERED_INCLUDE", f"Hash-register transitive header: {included.name}")
    if macro_origins is not None:
        for cursor in unit.cursor.get_children():
            if cursor.kind == cindex.CursorKind.MACRO_DEFINITION and cursor.location.file is not None:
                macro_origins[cursor.spelling] = Path(cursor.location.file.name).resolve(strict=True)

    def flatten(record, prefix="", base=0):
        fields = {}
        for field in record.get_children():
            if field.kind != cindex.CursorKind.FIELD_DECL:
                continue
            offset_bits = field.get_field_offsetof()
            if offset_bits < 0 or offset_bits % 8 or field.is_bitfield():
                raise PraxisError("UNSUPPORTED_DECLARATION", f"Unsupported layout: {field.spelling}")
            field_type = field.type
            count = 1
            if field_type.kind == cindex.TypeKind.CONSTANTARRAY:
                count = field_type.element_count
                field_type = field_type.element_type
            spelling = prefix + field.spelling
            offset = base + offset_bits // 8
            canonical = field_type.get_canonical()
            if canonical.kind == cindex.TypeKind.RECORD:
                nested = canonical.get_declaration()
                if nested.kind == cindex.CursorKind.UNION_DECL:
                    views = []
                    for alternative in nested.get_children():
                        if alternative.kind != cindex.CursorKind.FIELD_DECL:
                            continue
                        view_type = alternative.type.get_canonical()
                        width = view_type.get_size() * 8
                        if (alternative.is_bitfield() or alternative.get_field_offsetof() != 0
                                or not alternative.spelling or width not in (8, 16, 32)
                                or view_type.kind not in (cindex.TypeKind.CHAR_U, cindex.TypeKind.UCHAR,
                                    cindex.TypeKind.CHAR_S, cindex.TypeKind.SCHAR, cindex.TypeKind.USHORT,
                                    cindex.TypeKind.SHORT, cindex.TypeKind.UINT, cindex.TypeKind.INT,
                                    cindex.TypeKind.ULONG, cindex.TypeKind.LONG)):
                            raise PraxisError("UNSUPPORTED_DECLARATION", f"Unsupported union view: {spelling}.{alternative.spelling}")
                        views.append({"name": alternative.spelling, "width": width,
                                      "c_type": alternative.type.spelling})
                    width = canonical.get_size() * 8
                    if (not views or width not in (8, 16, 32) or not 0 < count <= 1024
                            or width != max(view["width"] for view in views)):
                        raise PraxisError("UNSUPPORTED_DECLARATION", f"Unsupported union storage: {spelling}")
                    fields[spelling] = {"offset": offset, "width": width, "count": count, "views": views}
                    continue
                if nested.kind != cindex.CursorKind.STRUCT_DECL or not 0 < count <= 1024:
                    raise PraxisError("UNSUPPORTED_DECLARATION", f"Unsupported nested member: {spelling}")
                for index in range(count):
                    suffix = f"[{index}]" if field.type.kind == cindex.TypeKind.CONSTANTARRAY else ""
                    fields.update(flatten(nested, spelling + suffix + ".",
                                          offset + index * canonical.get_size()))
                continue
            width = field_type.get_size() * 8
            if width not in (8, 16, 32) or not 0 < count <= 1024:
                raise PraxisError("UNSUPPORTED_DECLARATION", f"Unsupported field: {spelling}")
            fields[spelling] = {"offset": offset, "width": width, "count": count}
        return fields

    layouts = {}
    for cursor in unit.cursor.get_children():
        if cursor.kind != cindex.CursorKind.TYPEDEF_DECL:
            continue
        if structures is not None and cursor.spelling not in structures:
            continue
        if (structures is None and not cursor.spelling.endswith(("TypeDef", "_Type"))
                and cursor.spelling not in (additional_structures or [])):
            continue
        declaration = cursor.underlying_typedef_type.get_declaration()
        if origins is not None:
            origins[cursor.spelling] = Path(cursor.location.file.name).resolve(strict=True)
        try:
            layouts[cursor.spelling] = flatten(declaration)
        except PraxisError as exc:
            if failures is None:
                raise
            failures[cursor.spelling] = str(exc)
    if structures is not None and set(layouts) != set(structures):
        raise PraxisError("MISSING_DECLARATION", f"Missing structures: {set(structures) - set(layouts)}")
    return layouts


def avr(header: Path, names: list[str], flags: list[str]) -> dict[str, dict]:
    # Assembly preprocessing preserves _SFR_IO8/_SFR_MEM8 information in the fixture input.
    definitions = macros(header, "avr-gcc", [*flags, "-D__ASSEMBLER__"])
    result = {}
    for name in names:
        raw = definitions.get(name, "")
        match = re.fullmatch(r"_SFR_(IO|MEM)(8|16)\((.+)\)", raw)
        if not match:
            # avr-libc expands function macros during -dM consumers, not -dM itself;
            # source register definitions remain available in the macro replacement text.
            raise PraxisError("UNSUPPORTED_EXPRESSION", f"{name}: expected supported SFR macro, got {raw}")
        address = integer(match[3], definitions)
        io_address = address if match[1] == "IO" else None
        memory_address = address + 0x20 if match[1] == "IO" else address
        result[name] = {"offset": memory_address, "width": int(match[2]), "count": 1,
                        "io_address": io_address}
    return result

