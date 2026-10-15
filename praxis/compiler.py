from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from pydantic import ValidationError

from praxis import __version__
from praxis.adapters.constraints import validate_headers
from praxis.bundle import Bundle, decode, digest, read_inside, read_source_inside, revision
from praxis.contracts import load_contract, validate_required_registers
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Dependency, Instance, Manifest, Net, Peripheral, Profile, Register, Source, SourceRef
from praxis.process import run
from praxis.render import identity, netlist, peripheral, source_documents, table, topology



def _web_sources(profile, paths, sources, root):
    """Require exact-byte review for any registered source inside a web archive."""
    if not profile.web_imports and not any((p.parent / "import.json").exists()
            or any((parent / "import.json").exists() for parent in p.parents if parent.is_relative_to(root))
            for p in paths.values()):
        return
    from praxis.web_import import FORMAT, require_review
    groups = {}
    for source_id, directory in profile.web_imports.items():
        if source_id not in paths:
            raise PraxisError("UNKNOWN_SOURCE", f"Unknown web evidence source: {source_id}")
        # Validate the relative path and its resolved boundary before reading archives.
        read_inside(root, f"{directory}/import.json", 4 * 1024 * 1024)
        archive = (root / directory).resolve(strict=True)
        if not archive.is_relative_to(root):
            raise PraxisError("INVALID_PATH", "Web import archive escapes the source tree")
        record, receipt = require_review(archive, profile.target.mcu)
        if not paths[source_id].is_relative_to(archive):
            raise PraxisError("IMPORT_INTEGRITY", "Registered source is outside its declared web archive")
        artifact = paths[source_id].relative_to(archive).as_posix()
        if artifact not in record["file_hashes"]:
            raise PraxisError("IMPORT_INTEGRITY", "Web source is not a hash-registered imported artifact")
        groups[archive] = (record, receipt)
    # Metadata markers are checked even when a profile omitted web_imports.
    # Removing/moving evidence is not a substitute for checking its provenance.
    for source_id, path in paths.items():
        for parent in path.parents:
            if not parent.is_relative_to(root):
                break
            marker = parent / "import.json"
            if marker.is_file():
                data = load_json(read_inside(parent, "import.json", 4 * 1024 * 1024))
                if isinstance(data, dict) and data.get("format") == FORMAT and (
                        source_id not in profile.web_imports or (root / profile.web_imports[source_id]).resolve() != parent):
                    raise PraxisError("UNDECLARED_WEB_IMPORT", f"Declare source {source_id} in profile.web_imports and review its archive")
    for archive, (record, receipt) in sorted(groups.items()):
        prefix = "web_" + digest(archive.relative_to(root).as_posix().encode())[:16]
        for suffix, authority in (("record", "configuration"), ("review", "semantics")):
            source_id = f"{prefix}_{suffix}"
            if source_id in paths:
                raise PraxisError("DUPLICATE_SOURCE", "Web provenance source identity collision")
            name = "import.json" if suffix == "record" else "review.json"
            relative = (archive / name).relative_to(root).as_posix()
            contents = read_inside(root, relative, 4 * 1024 * 1024)
            paths[source_id] = archive / name
            sources.append(Source(id=source_id, path=relative, sha256=digest(contents), authority=authority,
                version=record["import_revision"], license="Source terms apply; review metadata is local",
                origin=f"{record['download']['final_url']}; reviewer: {receipt['reviewer']}"))


def parse_cmsis_headers(header: Path, **kwargs):
    """Public offline adapter: complete declaration maps, without guessed semantics."""
    from praxis.adapters.discovery import parse_cmsis_headers as discover
    return discover(header, **kwargs)


def parse_kicad_netlist(path: Path, *, target, pin_map: dict[str, str],
                        source_id: str = "netlist"):
    """Return flat, complete net memberships with validated physical MCU pins.

    A signal name is a schematic net/declared alias, not proof of an enabled AF.
    Pin-to-peripheral AF capability must come from the reviewed datasheet import.
    """
    from praxis.adapters.kicad import parse
    return parse(path, source_id, target, pin_map)


def parse_device_tree(path: Path, *, overlays: list[Path] | None = None,
                      include_directories: list[Path] | None = None, source_id: str = "dts",
                      registered_sources: list[Path] | None = None):
    """Resolve DTS/includes/overlays to a DTB, then decode supported relationships."""
    from praxis.adapters.devicetree import compile_dts
    return compile_dts(path, overlays or [], include_directories or [path.parent], source_id,
                       registered_sources=registered_sources)


def _discover(profile, paths, items, root, contract):
    if profile.discovery is None and not contract.legacy_discovery:
        raise PraxisError("INVALID_CONTRACT", "Discovery requires explicit peripheral mappings or inventory policy")
    include_dirs = []
    for name in profile.header.include_directories:
        directory = (root / name).resolve(strict=True)
        if not directory.is_relative_to(root) or not directory.is_dir():
            raise PraxisError("INVALID_PATH", "Header include directory escapes source tree")
        include_dirs.append(directory)
    coverage_entries = None
    if profile.discovery is not None:
        from praxis.coverage import inventory, order
        catalog, coverage_entries = inventory(profile, paths, items, root)
        selected = {name for name, row in coverage_entries.items()
                    if row["selected"] and name in catalog}
        known = {item.id: item for item in items}
        for name in sorted(selected):
            spec = profile.discovery.peripherals.get(name)
            if name in known:
                if spec is not None and spec.prerequisites is not None:
                    known[name] = known[name].model_copy(update={"prerequisites": spec.prerequisites})
                continue
            declaration = catalog[name]
            parents = (spec.prerequisites if spec is not None and spec.prerequisites is not None
                       else profile.discovery.default_prerequisites)
            known[name] = Peripheral(id=name, title=f"{name.upper()} — declarations only",
                prerequisites=parents, registers=declaration.registers,
                instances=[Instance(name=instance, base_address=base, bus="Not asserted",
                           clock="Not asserted", sources=[SourceRef(source=declaration.instance_sources[instance],
                           locator=declaration.base_macros[instance]),
                           *([SourceRef(source="profile", locator=f"discovery.peripherals.{name}.instances.{instance}")]
                             if spec is not None and instance in spec.instances else [])])
                           for instance, base in sorted(declaration.instances.items())],
                reviewed_markdown="", review=None)
        # Size never removes a selected block or its dependencies.
        order({name: item.prerequisites for name, item in known.items()})
        items = [known[name] for name in sorted(known)]
        catalog = {item.id: catalog[item.id] for item in items}
    else:
        catalog = parse_cmsis_headers(paths[profile.header.source], include_directories=include_dirs,
                                 defines=profile.header.defines, source_id=profile.header.source,
                                 core_source_id=contract.core_source or profile.header.source,
                                 registered_sources=list(paths.values()), cpu=contract.cpu,
                                 structures={k: v.structure for k, v in contract.legacy_discovery.items()},
                                 prefixes={k: v.prefix or k.upper() for k, v in contract.legacy_discovery.items()},
                                 stm32_views=False,
                                 member_views={k: v.member_views for k, v in contract.legacy_discovery.items()},
                                 view_sources={k: {member: SourceRef(source=profile.compilation_contract,
                                     locator=f"legacy_discovery.{k}.member_views.{member}")
                                     for member in v.member_views}
                                     for k, v in contract.legacy_discovery.items()})
    if set(catalog) != {item.id for item in items}:
        raise PraxisError("MISSING_DECLARATION", "Selected declarations and peripheral definitions disagree")
    if not profile.header.required_registers.keys() <= catalog.keys():
        raise PraxisError("INVALID_PROFILE", "Required-register policy names an unknown peripheral")
    field_expressions, members, bases = {}, {}, {}
    merged = []
    for item in items:
        declared = catalog[item.id]
        # Discovered records are declarations, not semantic overrides of
        # themselves. Merging them duplicated provenance and inflated tables.
        reviewed = {r.name: r for r in item.registers} if item.review is not None else {}
        available = {r.name for r in declared.registers}
        if not reviewed.keys() <= available:
            raise PraxisError("DECLARATION_CONFLICT", f"Unknown reviewed registers in {item.id}")
        registers = []
        for register in declared.registers:
            previous = reviewed.get(register.name)
            if previous is None:
                registers.append(register)
                continue
            if ((previous.offset, previous.width, previous.count) !=
                    (register.offset, register.width, register.count)):
                raise PraxisError("DECLARATION_CONFLICT", f"{item.id}.{register.name}: reviewed layout differs")
            if previous.reset is not None and register.reset is not None and previous.reset != register.reset:
                raise PraxisError("DECLARATION_CONFLICT", f"{item.id}.{register.name}: reset values conflict")
            if previous.storage_views and [v.model_dump(exclude={"sources"}) for v in previous.storage_views] != [
                    v.model_dump(exclude={"sources"}) for v in register.storage_views]:
                raise PraxisError("DECLARATION_CONFLICT", f"{item.id}.{register.name}: union storage views conflict")
            masks = {f.mask: f for f in register.fields}
            if any(f.mask not in masks for f in previous.fields):
                raise PraxisError("DECLARATION_CONFLICT", f"{item.id}.{register.name}: reviewed field not in header")
            semantic_fields = {f.mask: f for f in previous.fields}
            fields = []
            for field in register.fields:
                semantic = semantic_fields.get(field.mask)
                fields.append(field if semantic is None else field.model_copy(update={
                    "meaning": semantic.meaning, "sources": [*field.sources, *semantic.sources]}))
            if not previous.field_views.keys() <= register.field_views.keys():
                raise PraxisError("DECLARATION_CONFLICT", f"{item.id}.{register.name}: reviewed view not configured")
            alternatives = {}
            for name, view in register.field_views.items():
                semantic = previous.field_views.get(name)
                if semantic is None:
                    alternatives[name] = view
                    continue
                reviewed_fields = {field.name: field for field in semantic.fields}
                declared_fields = {field.name: field for field in view.fields}
                if any(field not in declared_fields or value.mask != declared_fields[field].mask
                       for field, value in reviewed_fields.items()):
                    raise PraxisError("DECLARATION_CONFLICT",
                                      f"{item.id}.{register.name}.{name}: reviewed field differs from header")
                alternatives[name] = view.model_copy(update={
                    "selection": semantic.selection, "sources": [*view.sources, *semantic.sources],
                    "fields": [field if field.name not in reviewed_fields else field.model_copy(update={
                        "meaning": reviewed_fields[field.name].meaning,
                        "sources": [*field.sources, *reviewed_fields[field.name].sources]}) for field in view.fields]})
            registers.append(Register.model_validate({**previous.model_dump(),
                "reset": previous.reset if previous.reset is not None else register.reset,
                "fields": fields, "storage_views": register.storage_views, "field_views": alternatives,
                "sources": [*register.sources, *previous.sources]}))
        instances = {i.name: i for i in item.instances}
        if not instances.keys() <= declared.instances.keys():
            raise PraxisError("DECLARATION_CONFLICT", f"{item.id}: reviewed instance not declared")
        for name, address in declared.instances.items():
            bases[name] = declared.base_macros[name]
            if name in instances:
                if instances[name].base_address != address:
                    raise PraxisError("DECLARATION_CONFLICT", f"{name}: reviewed base differs")
                continue
            instances[name] = Instance(name=name, base_address=address, bus="Not asserted",
                clock="Not asserted outside reviewed workflow",
                sources=[SourceRef(source=declared.instance_sources[name],
                                   locator=declared.base_macros[name])])
        merged.append(Peripheral.model_validate({**item.model_dump(), "registers": registers,
                      "instances": [instances[name] for name in sorted(instances)]}))
        field_expressions.update(declared.field_expressions)
        members[item.id] = declared.members
    # Explicit profile expressions remain constraints; never silently replace a conflict.
    from praxis.adapters.headers import macros
    from praxis.expressions import integer
    definitions = macros(paths[profile.header.source], "arm-none-eabi-gcc",
                         [f"-mcpu={contract.cpu}", "-mthumb",
                          *profile.header.defines, *[f"-I{p}" for p in include_dirs]])
    for field, expression in profile.header.field_expressions.items():
        if field not in field_expressions or integer(expression, definitions) != integer(field_expressions[field], definitions):
            raise PraxisError("DECLARATION_CONFLICT", f"Explicit field expression differs: {field}")
    for instance, macro in profile.header.base_macros.items():
        if instance not in bases or macro not in definitions or integer(definitions[macro], definitions) != integer(definitions.get(bases[instance], bases[instance]), definitions):
            raise PraxisError("DECLARATION_CONFLICT", f"Explicit base expression differs: {instance}")
    spec = profile.header.model_copy(update={"structures": {k: v.structure for k, v in catalog.items()},
        "members": members, "base_macros": bases, "field_expressions": field_expressions})
    return merged, profile.model_copy(update={"header": spec}), coverage_entries


def _declaration_notice(name, declaration=None, *, gaps=None, notes=None):
    gaps = declaration.unresolved_masks if declaration is not None else gaps or []
    notes = declaration.notes if declaration is not None else notes or []
    return (f"**{name}: declarations only; operating semantics are NOT reviewed.**\n\n"
            "Do not generate initialization code from this document alone. Register access modes, "
            "side effects, readiness checks, clock domains, pin routing, and supported modes require "
            "reviewed manual/datasheet/errata evidence. Dependencies are configuration policy "
            "from `profile:discovery`, not operating facts. See the coverage report in [[index]].\n" +
            ("\nMask extraction gaps (the affected register's entire bit-field set is withheld):\n\n" +
             "\n".join("- " + note for note in gaps) + "\n" if gaps else "") +
            ("\nCompound declaration masks:\n\n" +
             "\n".join("- " + note for note in notes if note.startswith("Compound mask ")) + "\n"
             if any(note.startswith("Compound mask ") for note in notes) else ""))


def _aliases(profile, items):
    aliases = dict(profile.aliases)
    if profile.discovery is None:
        return aliases
    canonical = {item.id for item in items}
    for item in items:
        for instance in item.instances:
            alias = instance.name.lower()
            if alias == item.id:
                continue
            if alias in canonical or alias in aliases and aliases[alias] != item.id:
                raise PraxisError("INVALID_ALIAS", f"Instance alias collision: {alias}")
            aliases[alias] = item.id
    return dict(sorted(aliases.items()))


def _definitions(profile, paths, root):
    from praxis.definitions import load_definitions
    items = load_definitions(profile, paths)
    source_ids = set(paths) | {"profile"}
    for item in items:
        if item.review is None:
            raise PraxisError("INVALID_DEFINITIONS", "Authored operating definitions require an actual review")
        read_inside(root, item.reviewed_markdown)
        references = [s for instance in item.instances for s in instance.sources]
        for register in item.registers:
            references.extend(register.sources)
            references.extend(ref for view in register.storage_views for ref in view.sources)
            for field in register.fields:
                references.extend(field.sources)
            for view in register.field_views.values():
                references.extend(view.sources)
                references.extend(ref for field in view.fields for ref in field.sources)
        authorities = {s.id: s.authority for s in profile.sources}
        for register in item.registers:
            if register.write_mask is not None and not any(
                    authorities.get(ref.source) == "semantics" for ref in register.sources):
                raise PraxisError("SOURCE_AUTHORITY", f"{item.id}.{register.name}: reviewed write masks require semantic evidence")
        for mode in item.operating_modes.values():
            references.extend(mode.sources)
            if any(authorities.get(ref.source) != "semantics" for ref in mode.sources):
                raise PraxisError("SOURCE_AUTHORITY", f"{item.id}: operating modes require registered semantic evidence")
            registers = {r.name: r for r in item.registers}
            for name in mode.registers:
                register = registers[name]
                if (not register.access_widths
                        or not any(authorities.get(ref.source) == "semantics" for ref in register.sources)):
                    raise PraxisError("SOURCE_AUTHORITY", f"{item.id}.{name}: mode needs reviewed bus access widths and semantics")
                view = mode.field_views.get(name)
                if view is not None and not any(authorities.get(ref.source) == "semantics"
                                                for ref in register.field_views[view].sources):
                    raise PraxisError("SOURCE_AUTHORITY", f"{item.id}.{name}.{view}: mode needs reviewed view selection")
                fields = {f.name: f for f in register.fields_for(view)}
                for field in mode.fields.get(name, []):
                    if not any(authorities.get(ref.source) == "semantics" for ref in fields[field].sources):
                        raise PraxisError("SOURCE_AUTHORITY", f"{item.id}.{name}.{field}: mode needs reviewed field semantics")
        if any(ref.source not in source_ids for ref in references):
            raise PraxisError("UNKNOWN_SOURCE", f"Unregistered provenance in {item.id}")
        if item.reviewed_markdown not in {s.path for s in profile.sources}:
            raise PraxisError("UNKNOWN_SOURCE", "Reviewed Markdown must be hash-registered as a source")
    from praxis.coverage import mode_order
    mode_order(items)
    return sorted(items, key=lambda p: p.id)



def compile_bundle(profile_path: Path, output: Path, *, _coverage_only: bool = False) -> Path:
    profile_path = profile_path.resolve(strict=True)
    root = profile_path.parent
    try:
        profile = Profile.model_validate(load_json(read_inside(root, profile_path.name, 8 * 1024 * 1024)))
    except ValidationError as exc:
        raise PraxisError("INVALID_PROFILE", str(exc)) from exc
    source_ids = [s.id for s in profile.sources]
    if len(source_ids) != len(set(source_ids)) or "profile" in source_ids:
        raise PraxisError("DUPLICATE_SOURCE", "Source IDs must be unique; 'profile' is reserved")
    paths, sources = {}, []
    for source in profile.sources:
        # Provenance is hashed before any compiler processes it; paths stay inside the input tree.
        contents = read_source_inside(root, source.path)
        if source.expected_sha256 is not None and digest(contents) != source.expected_sha256:
            raise PraxisError("SOURCE_HASH_MISMATCH", f"Pinned source {source.id} changed; restore its declared bytes or review a new source version")
        paths[source.id] = (root / source.path).resolve()
        sources.append(Source(**source.model_dump(exclude={"expected_sha256"}), sha256=digest(contents)))
    sources.append(Source(id="profile", path=profile_path.name, sha256=digest(profile_path.read_bytes()),
                          authority="configuration", version="1", license="MIT", origin="Local target profile"))
    _web_sources(profile, paths, sources, root)
    required = {profile.definitions, profile.header.source, *profile.definition_extensions}
    if profile.netlist is not None:
        required.add(profile.netlist)
    if profile.board:
        required.add(profile.board)
    if profile.devicetree:
        required |= {profile.devicetree.source, *profile.devicetree.overlays, *profile.devicetree.includes}
    if not required <= paths.keys():
        raise PraxisError("UNKNOWN_SOURCE", f"Missing sources: {required - paths.keys()}")
    contract = load_contract(profile, root)
    items = _definitions(profile, paths, root)
    coverage_entries = None
    if profile.header.discover:
        if profile.header.kind != "cmsis":
            raise PraxisError("INVALID_PROFILE", "Automatic discovery currently supports CMSIS only")
        items, profile, coverage_entries = _discover(profile, paths, items, root, contract)
    validate_required_registers(profile, contract, items)
    versions = {"praxis": __version__, "publication-contract": "v1",
                **validate_headers(profile, paths, items, root, contract)}
    if profile.header.discover:
        versions["cmsis-discovery"] = "v1; Clang layouts and restricted object-macro evaluation"
    from praxis.adapters.kicad import import_schematic, parse_schematic
    from praxis.board import load as load_board
    from praxis.board import render_board, render_components, validate, validate_schematic

    net_path = paths[profile.netlist] if profile.netlist is not None else None
    if net_path is None:
        schematic = None
        versions["netlist"] = "Unavailable: MCU-only scope; no schematic ingested"
    elif profile.netlist_format == "reviewed":
        from praxis.adapters.reviewed import parse as parse_reviewed
        schematic = parse_reviewed(net_path, profile.target)
        versions["netlist"] = "Reviewed PDF transcription adapter v1; no geometry inference"
    elif net_path.suffix == ".kicad_sch":
        schematic = import_schematic(net_path, profile.netlist, profile.target, profile.pin_map,
                                     list(paths.values()))
        versions["kicad-cli"] = run(["kicad-cli", "version"]).strip()
    else:
        schematic = parse_schematic(net_path, profile.netlist, profile.target, profile.pin_map)
        versions["netlist"] = "KiCad XML adapter v1 (pre-exported source)"
    authorities = {source.id: source.authority for source in sources}
    if schematic is not None:
        if authorities[profile.netlist] != "connectivity":
            raise PraxisError("SOURCE_AUTHORITY", "Schematic sources must have connectivity authority")
        validate_schematic(schematic, profile.target, profile.pin_map, set(authorities))
    nets = schematic.nets if schematic is not None else []
    board = load_board(paths[profile.board]) if profile.board else None
    if board and (authorities[profile.board] != "semantics" or
                  getattr(schematic, "coverage", board.coverage) != board.coverage):
        raise PraxisError("SOURCE_AUTHORITY", "Board semantics authority or schematic coverage disagrees")
    circuits = validate(board, schematic, profile.target, profile.pin_map, authorities,
                        profile.required_workflows) if board else None
    signal_aliases = {name: list(aliases) for name, aliases in profile.signal_aliases.items()}
    if board:
        for signal in board.signals:
            net = next(n.name for n in nets if any(p.endpoint == signal.endpoint for p in n.pins))
            for alias in [signal.id, *signal.aliases]:
                if any(alias in aliases for aliases in signal_aliases.values()) or any(alias == n.name and n.name != net for n in nets):
                    raise PraxisError("INVALID_ALIAS", f"Board signal alias collision: {alias}")
                signal_aliases.setdefault(net, []).append(alias)
    known_nets = {n.name for n in nets}
    if not signal_aliases.keys() <= known_nets:
        raise PraxisError("UNKNOWN_NET", "Signal aliases reference an unknown net")
    nets = [Net.model_validate({**n.model_dump(), "aliases": signal_aliases.get(n.name, []),
                               "sources": [*n.sources, SourceRef(source="profile", locator=f"pin_map/net:{n.name}")]})
            for n in nets]
    documents = {}
    for item in items:
        narrative = (decode(read_inside(root, item.reviewed_markdown), item.reviewed_markdown)
                     if item.review is not None else _declaration_notice(item.id,
                         gaps=coverage_entries[item.id].get("unresolved_masks", []) if coverage_entries else [],
                         notes=coverage_entries[item.id]["issues"] if coverage_entries else []))
        documents[f"wiki/peripherals/{item.id}.md"] = peripheral(profile.target, item, narrative)
    coverage_report = None
    pin_document = contract.pin_document
    if coverage_entries is not None:
        from praxis.coverage import markdown, report
        from praxis.netlist import NetlistIndex
        coverage_report = report(profile, coverage_entries, items,
                                 NetlistIndex(netlist(profile.target, nets, pin_document=pin_document),
                                              profile.target.primary_mcu_ref,
                                              allow_empty=profile.target.scope == "mcu"))
        # The complete hash/version registry already lives in sources.md and the
        # manifest. Repeating it here exhausted the document budget as reviewed
        # evidence grew. Keep the selected profile identity and link the complete
        # registry; never shorten register tables or omit coverage gaps.
        coverage_report["sources"] = {s.id: {"sha256": s.sha256, "version": s.version}
                                      for s in sources if s.id == "profile"}
        coverage_report["source_catalog"] = "[[sources]]"
        coverage_report["sources_scope"] = "Selected profile only; complete source hashes and versions in source_catalog and manifest"
        coverage_report["extractor_versions"] = dict(sorted(versions.items()))
        if not coverage_report["publication_ready"] and not _coverage_only:
            blocked = [name for name, row in coverage_report["workflows"].items()
                       if row["required_for_publication"] and not row["ready"]]
            raise PraxisError("PUBLICATION_BLOCKED", f"Required workflows lack evidence: {blocked}; run praxis coverage")
        documents["wiki/coverage.md"] = ("# Coverage report\n\n" + markdown(coverage_report) +
            "\n## Machine-readable report\n\n```json\n" +
            json.dumps(coverage_report, sort_keys=True, separators=(",", ":")) + "\n```\n")
        from praxis.features import feature_report, markdown as feature_markdown
        documents["wiki/features.md"] = feature_markdown(feature_report(coverage_report))
    netlist_path = "wiki/schemas/custom_pcb_netlist.md"
    documents[netlist_path] = netlist(profile.target, nets, pin_document=pin_document)
    if board:
        documents["wiki/schemas/board.md"] = render_board(profile.target, board, circuits,
            prerequisite_documents=tuple(contract.board_prerequisites))
        documents["wiki/schemas/components.md"] = render_components(profile.target, schematic)
        documents[netlist_path] = documents[netlist_path].replace(
            "Electrical nets are direct exported memberships.",
            f"Electrical nets are explicit source memberships. Coverage: {board.coverage}. "
            "See [[schemas/board]] for omitted scope and reviewed circuit interpretation.")
    topology_paths = []
    if profile.devicetree:
        dt = profile.devicetree
        nodes = parse_device_tree(paths[dt.source], overlays=[paths[s] for s in dt.overlays],
                    include_directories=[root, *sorted({paths[s].parent for s in dt.includes})],
                    source_id=dt.source, registered_sources=list(paths.values()))
        nodes = [node.model_copy(update={"sources": [*node.sources,
                 *[SourceRef(source=s, locator=f"resolved-topology:{node.path}")
                   for s in [*dt.overlays, *dt.includes]]]}) for node in nodes]
        topology_paths = ["wiki/schemas/devicetree.md"]
        documents[topology_paths[0]] = topology(profile.target, nodes)
        versions["dtc"] = run(["dtc", "--version"]).strip()
        if dt.overlays:
            versions["fdtoverlay"] = run(["fdtoverlay", "--version"]).strip()
    from praxis.coverage import order as graph_order
    graph = {item.id: item.prerequisites for item in items}
    route = graph_order(graph)
    index = ["# Project Praxis hardware execution index\n", identity(profile.target),
             "## Hardware Execution Dependency Graph\n",
             "Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.\n",
             "\n".join(f"- [[peripherals/{name}]] requires " +
                       (", ".join(f"[[peripherals/{parent}]]" for parent in graph[name]) or "[[index]]")
                       for name in route),
             "Read this index first. Retrieve the matching net when board connectivity is available, "
             "then follow the applicable prerequisite edges. A topological listing does not impose "
             "dependencies between unrelated entities. Requested workflows determine the required "
             "operating modes. Tool gates establish retrieval evidence, not code correctness or physical behavior.\n",
             "## Clock assumptions\n", *[f"- {v}" for v in profile.target.clock_assumptions],
             *[f"- Fuse assumption: {v}" for v in profile.target.fuse_assumptions],
             "\n## Routing\n", "- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.",
             *[f"- [[{p.removeprefix('wiki/').removesuffix('.md')}]]: synthetic topology." for p in topology_paths],
             "- [[sources]]: provenance, licenses, and editorial review.\n",
             "## Startup boundary\n",
             "Provide startup code and a vector table separately. Keep interrupts masked until their "
             "sources and handlers are safe. Quiesce active peripherals before changing clocks. "
             "Use bounded readiness waits. No flashing or runtime probe operations are provided.\n"]
    documents["wiki/index.md"] = "\n".join(index)
    if profile.target.knowledge_adapter is not None:
        adapter = profile.target.knowledge_adapter
        documents["wiki/index.md"] += (
            "\n## Extraction scope\n\n"
            f"Adapter: `{adapter.kind}`; declared CPU: `{adapter.cpu}` "
            "(source: `profile:target.knowledge_adapter`). "
            "Header identity checks: " + ", ".join(f"`{name}`" for name in adapter.header_identity) +
            ". This is a knowledge-only target. No target firmware assets, sandbox compiler "
            "profile, flashing or physical qualification are supplied by this adapter. "
            "Clock assumptions and HEDG edges are explicit profile policy, not inferred from a diagram.\n")
    if profile.target.scope == "mcu":
        documents["wiki/index.md"] = documents["wiki/index.md"].replace(
            "Retrieve the matching net, then follow every stage in order.",
            "Board connectivity is unavailable; retrieve the requested declaration dependency closure.").replace(
            "- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.",
            "- [[schemas/custom_pcb_netlist]]: explicit absence of board connectivity.")
        documents["wiki/index.md"] += (
            "\n## MCU-only applicability\n\nScope: `profile:target.scope=mcu`. "
            "No evaluation board, package pin map, LED/button aliases, active bus clocks or "
            "firmware/flash assets are supplied. A missing schematic query is missing evidence, "
            "not proof that a signal is absent from the silicon. "
            "Register layouts and masks do not establish initialization sequences.\n")
    if coverage_report is not None:
        from praxis.coverage import markdown
        documents["wiki/index.md"] += "\n" + markdown(coverage_report) + "\nSee [[coverage]] and [[sources]].\n"
        documents["wiki/index.md"] += ("\n## Mode-specific support\n\nSee [[features]] for instance-scoped "
            "operating contracts. Header coverage does not establish complete MCU feature support.\n\n" +
            table(["Entity", "Reviewed mode", "Instances"],
                  [[item.id, name, ", ".join(mode.instances)] for item in items
                   for name, mode in sorted(item.operating_modes.items())]))
    if board:
        documents["wiki/index.md"] += ("\n## Board-specific workflow\n\n" +
            f"Model: {board.model}; reference revision: {board.board_revision}. "
            f"Applicability: {board.applicability}\n\n" +
            "Signals: " + ", ".join(alias for signal in board.signals for alias in signal.aliases) +
            ". Query a signal to retrieve its reviewed board context and separate circuit nets.\n\n" +
            "Retrieve each requested signal, then its peripheral dependency closure. "
            "Use reviewed workflow contracts to determine whether interrupt or core setup is required.\n\n" +
            "See [[schemas/board]] and [[schemas/components]].\n")
    if profile.header.discover:
        documents["wiki/index.md"] += ("\nMetadata and clock assumptions: `profile:target`. "
            "These are declared operating assumptions, not measurements. "
            "All register declarations are retained; unknown access/reset/encoding facts remain "
            "explicitly unasserted and must not be used to generate unsupported operations.\n")
    documents["wiki/index.md"] += (
        f"\nPublication policy: `{profile.compilation_contract}:{contract.id}`; "
        "its exact input hash and review scope are recorded in [[sources]]. "
        "See [[policy]] for the complete declarative contract. Requirements constrain publication; "
        "they do not manufacture missing hardware facts.\n")
    documents["wiki/policy.md"] = (
        "# Publication contract\n\n"
        f"Source: `{profile.compilation_contract}`; hash and origin: [[sources]].\n\n"
        "This reviewed scope defines minimum evidence, extraction identity, and routing links. "
        "It does not establish complete MCU coverage, independently certify its sources, or grant "
        "firmware build/flash qualification. Changing it requires an explicit new source pin "
        "and produces a new immutable revision. See [[index]] for available workflow coverage.\n\n```json\n" +
        json.dumps(contract.model_dump(), sort_keys=True, indent=2, ensure_ascii=False) + "\n```\n")
    documents.update(source_documents(profile.target, sources, profile.review))
    manifest_data = dict(schema_version=2 if profile.discovery is not None else 1,
                         compiler_version=__version__, bundle_revision="0" * 64,
                         target=profile.target, review=profile.review,
                         sources=sorted(sources, key=lambda s: s.id), extractor_versions=versions,
                         documents={p.removeprefix("wiki/").removesuffix(".md"): p for p in sorted(documents)},
                         peripherals={p.id: f"wiki/peripherals/{p.id}.md" for p in items}, aliases=_aliases(profile, items),
                         dependencies=[Dependency(entity=p.id, requires=p.prerequisites) for p in items],
                         netlist=netlist_path, topology=topology_paths,
                         file_hashes={p: digest(text.encode()) for p, text in sorted(documents.items())})
    manifest_data["documents"]["index"] = "wiki/index.md"
    draft = Manifest(**manifest_data).model_dump()
    draft["bundle_revision"] = revision(draft)
    manifest = Manifest(**draft)
    for source in sources:
        if digest(read_source_inside(root, source.path)) != source.sha256:
            raise PraxisError("SOURCE_CHANGED", "An input changed during compilation; retry with stable sources")
    output = output.absolute()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".praxis-staging-", dir=output.parent) as directory:
        staging = Path(directory) / "bundle"
        staging.mkdir()
        for name, text in documents.items():
            destination = staging / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(text.encode("utf-8"))
        (staging / "manifest.json").write_text(json.dumps(manifest.model_dump(), indent=2, sort_keys=True,
                                                        ensure_ascii=False) + "\n", encoding="utf-8")
        Bundle(staging)
        if output.exists() or output.is_symlink():
            existing = Bundle(output)
            if existing.manifest.bundle_revision != manifest.bundle_revision:
                raise PraxisError("IMMUTABLE_BUNDLE", "Output already contains a different revision; choose a new output directory")
            return output
        # Atomic directory publication on the same filesystem; output revisions are never replaced.
        os.rename(staging, output)
    return output
