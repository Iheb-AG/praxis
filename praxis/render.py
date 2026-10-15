"""Stable Markdown generation; no summaries or table chunking."""

import html
import json

from praxis.models import Net, Peripheral, Source, SourceRef, Target, TopologyNode


def cell(value) -> str:
    return html.escape(str(value), quote=False).replace("\\", "\\\\").replace("|", "&#124;").replace("\r", " ").replace("\n", "<br>")


def table(headers: list[str], rows: list[list]) -> str:
    return "\n".join("| " + " | ".join(cell(c) for c in row) + " |"
                     for row in [headers, ["---"] * len(headers), *rows]) + "\n"


def refs(sources: list[SourceRef]) -> str:
    return "; ".join(f"{s.source}:{s.locator}" for s in sources)


def identity(target: Target) -> str:
    return (f"Target: `{target.id}`; MCU: `{target.mcu}`; package: `{target.package}`; "
            f"board revision: `{target.board_revision}`; silicon: `{target.silicon_revision}`.\n\n"
            + ("**Experimental MCU-only knowledge; no board wiring, active clock configuration "
               "or physical qualification is supplied.**\n" if target.scope == "mcu" else
             "**Illustrative fixture; not a manufactured or hardware-qualified board.**\n"
             if target.example_only else
             "**Documented reference board revision; physical board revision and modifications "
             "must be checked. Not hardware-qualified by Praxis.**\n"))


def source_catalog(sources: list[Source]) -> str:
    """Lossless normalization of repeated page-level provenance metadata.

    Retain each artifact's identity/path/hash and each complete metadata tuple.
    This is registry normalization, never a reduction of hardware fact tables.
    """
    def metadata(source):
        return (source.authority, source.version, source.license, source.origin)

    shared = {value: f"metadata_{number:03}" for number, value in enumerate(
        sorted({metadata(source) for source in sources}), 1)}
    def path_parts(source):
        directory, separator, filename = source.path.rpartition('/')
        return directory + separator, filename

    prefixes = {value: f"prefix_{number:03}" for number, value in enumerate(
        sorted({path_parts(source)[0] for source in sources}), 1)}
    return ("Every artifact row references one complete metadata row below. "
            "Reconstruct its exact path by concatenating the referenced directory prefix and File; "
            "a dash in the prefix registry means the empty prefix. "
            "The manifest also retains the expanded registry.\n\n" +
            table(["ID", "Prefix", "File", "SHA-256", "Metadata"],
                  [[s.id, prefixes[path_parts(s)[0]], path_parts(s)[1], s.sha256, shared[metadata(s)]]
                   for s in sorted(sources, key=lambda s: s.id)]) +
            "\n## Shared path prefixes\n\n" +
            table(["Prefix", "Exact directory prefix"],
                  [[key, value or '—'] for value, key in prefixes.items()]) +
            "\n## Shared source metadata\n\n" +
            table(["Metadata", "Authority", "Version", "License", "Origin"],
                  [[key, *value] for value, key in shared.items()]))


def source_documents(target, sources, review) -> dict[str, str]:
    """Publish the complete source registry without a per-document size ceiling."""
    header = "# Source provenance\n\n" + identity(target) + "\n"
    footer = (f"\nEditorial reviewer: {review.reviewer}. Basis: {review.basis}.\n\n"
              "Editorial review is not independent hardware sign-off. See [[index]].\n")
    return {"wiki/sources.md": header + source_catalog(sources) + footer}


def peripheral(target: Target, item: Peripheral, narrative: str) -> str:
    arrays = any(r.count > 1 for r in item.registers)
    columns = ["Register", "Offset / data address", "Width", "I/O address", "Access", "Reset", "Side effects", "Sources"]
    access_widths = any(r.access_widths for r in item.registers)
    write_masks = any(r.write_mask is not None for r in item.registers)
    if access_widths:
        columns.append("Permitted bus access widths")
    if write_masks:
        columns.append("Reviewed write-value mask")
    if arrays:
        columns.extend(["Count", "Stride bytes"])
    rows = []
    for r in item.registers:
        row = [r.name, f"0x{r.offset:03X}", r.width,
               "—" if r.io_address is None else f"0x{r.io_address:02X}", r.access,
               "not asserted" if r.reset is None else f"0x{r.reset:X}", r.side_effects, refs(r.sources)]
        if access_widths:
            row.append(", ".join(map(str, r.access_widths)) or "not asserted")
        if write_masks:
            row.append(f"0x{r.write_mask:X}" if r.write_mask is not None else "not asserted")
        if arrays:
            row.extend([r.count, r.width // 8])
        rows.append(row)
    output = [f"# {item.title}\n", identity(target),
              "Prerequisites: " + (", ".join(f"[[peripherals/{n}]]" for n in item.prerequisites)
                                   or "[[index]]") + ".\n",
              "## Instances and clock dependencies\n",
              table(["Instance", "Base address", "Bus", "Clock", "Sources"],
                    [[i.name, f"0x{i.base_address:08X}", i.bus, i.clock, refs(i.sources)]
                     for i in item.instances]),
              "## Register map\n",
              table(columns, rows),
              "## Bit fields\n",
              table(["Register", "Field", "Bits", "Mask", "Meaning", "Sources"],
                    [[r.name, f.name, f"{f.lsb + f.width - 1}:{f.lsb}", f"0x{f.mask:X}",
                      f.meaning, refs(f.sources)] for r in item.registers for f in r.fields]),
              "## Reviewed operating semantics\n" if item.review is not None else "## Operating semantics unavailable\n",
              narrative.strip() + "\n",
              "## Review\n", (f"Reviewer: {item.review.reviewer}. Basis: {item.review.basis}.\n"
                                 if item.review is not None else "Not reviewed. Declaration extraction is not semantic review.\n"),
              "See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].\n"]
    if write_masks:
        output.insert(-1, "Reviewed write-value masks constrain values used by this operating subset: "
            "do not set bits outside the mask. A zero mask permits only a zero write to writable "
            "registers; RO registers remain non-writable. This is not a complete hardware "
            "writable-bit claim or permission for RMW: obey access, action and side-effect rules.\n")
    if item.operating_modes:
        mode_columns = ["Mode", "Instances", "Registers", "Required fields", "Operating requirements", "Sources"]
        mode_rows = [[name, ", ".join(mode.instances), ", ".join(mode.registers),
            "; ".join(f"{r}: {', '.join(fields)}" for r, fields in sorted(mode.fields.items())),
            "\n".join(mode.requirements), refs(mode.sources)]
            for name, mode in sorted(item.operating_modes.items())]
        if any(mode.requires_modes for mode in item.operating_modes.values()):
            mode_columns.append("Required modes")
            for row, (_, mode) in zip(mode_rows, sorted(item.operating_modes.items()), strict=True):
                row.append("; ".join(f"[[peripherals/{dep.peripheral}]] / {dep.mode}: "
                                     + ", ".join(dep.instances) for dep in mode.requires_modes))
        if any(mode.field_views for mode in item.operating_modes.values()):
            mode_columns.append("Selected register field views")
            for row, (_, mode) in zip(mode_rows, sorted(item.operating_modes.items()), strict=True):
                row.append("; ".join(f"{register}: {view}" for register, view in sorted(mode.field_views.items())))
        output.insert(-3, "## Reviewed operating modes\n\n" + table(
            mode_columns, mode_rows))
    text = "\n".join(output)
    if any(register.field_views for register in item.registers):
        views = ["## Alternative register field views\n",
                 "Each table is a separate interpretation of the same register. Select exactly one view "
                 "per register as required by a reviewed operating contract. Fields in different views "
                 "must never be combined into one write. Declaration sets alone do not establish "
                 "selection conditions, instance availability, pin routing or operating support.\n"]
        for register in item.registers:
            for name, view in sorted(register.field_views.items()):
                views.extend([f"### {register.name}: {name}\n",
                    f"Selection: {view.selection}\n\nSources: {refs(view.sources)}\n",
                    table(["Register", "Field", "Bits", "Mask", "Meaning", "Sources"],
                          [[register.name, f.name, f"{f.lsb + f.width - 1}:{f.lsb}",
                            f"0x{f.mask:X}", f.meaning, refs(f.sources)] for f in register.fields_for(name)])])
        text = text.replace("## Bit fields\n", "\n".join(views) + "\n## Bit fields\n", 1)
    if any(register.storage_views for register in item.registers):
        views = ("## Declared C storage views\n\n"
            "These union members share storage; the register map records its ABI size and array stride. "
            "Declared C widths do not establish legal hardware access widths, permissions, reset values "
            "or operating semantics. Those require separate reviewed evidence.\n\n" +
            table(["Register", "Union member", "Declared C type", "Width bits", "Sources"],
                  [[register.name, view.name, view.c_type, view.width, refs(view.sources)]
                   for register in item.registers for view in register.storage_views]))
        text = text.replace("## Bit fields\n", views + "\n## Bit fields\n", 1)
    return text


NET_COLUMNS = ["Net", "Endpoint", "Pin", "Sheet", "Package", "Aliases", "Sources"]


def netlist(target: Target, nets: list[Net], *, pin_document: str | None = "gpio") -> str:
    rows = []
    for net in nets:
        for pin in net.pins:
            sources = sorted(set(net.sources + pin.sources), key=lambda s: (s.source, s.locator))
            rows.append([net.name, pin.endpoint, pin.name, pin.sheet, pin.package,
                         ";".join(net.aliases), refs(sources)])
    return ("# Resolved schematic netlist\n\n" + identity(target) +
            ("\nConnectivity status: unavailable (MCU-only). No schematic or package pin mapping was ingested. "
             "Do not infer LED, button, connector or peripheral wiring from MCU declarations. "
             if target.scope == "mcu" else
             "\nElectrical nets are direct exported memberships. Components do not join their two nets. ") +
            "Device Tree configuration is separate evidence. See [[index]], " +
            (f"[[peripherals/{pin_document}]], " if pin_document else "") +
            "and [[sources]].\n\n" + table(NET_COLUMNS, rows))


def topology(target: Target, nodes: list[TopologyNode]) -> str:
    return ("# Synthetic Device Tree fixture\n\n" + identity(target) +
            "\nThis synthetic topology exercises ingestion; it is not a board wiring claim. "
            "Unresolved properties are retained as hexadecimal bytes. See [[index]] and [[sources]].\n\n" +
            table(["Node", "Enabled", "Decoded", "Raw properties", "Unresolved", "Sources"],
                  [[n.path, n.enabled, json.dumps(n.decoded, sort_keys=True),
                    json.dumps(n.properties, sort_keys=True), "; ".join(n.unresolved), refs(n.sources)]
                   for n in nodes]))
