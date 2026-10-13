"""Offline declaration inventory and honest, deterministic publication coverage.

A discovered register block is not reviewed operating support. Dependencies are
profile policy, never inferred from the order of declarations in a C header.
"""
from __future__ import annotations

import re

from pydantic import ValidationError

from praxis.adapters.discovery import parse_cmsis_headers
from praxis.adapters.headers import cmsis, macros
from praxis.bundle import check_graph
from praxis.errors import PraxisError
from praxis.models import PeripheralDiscovery
from praxis.render import table
from praxis.targets import check_header_identity, cmsis_cpu


def order(graph: dict[str, list[str]]) -> list[str]:
    check_graph(set(graph), graph)
    result, done = [], set()

    def visit(entity):
        if entity in done:
            return
        for parent in sorted(graph[entity]):
            visit(parent)
        done.add(entity)
        result.append(entity)

    for entity in sorted(graph):
        visit(entity)
    return result


def inventory(profile, paths, reviewed, root):
    policy = profile.discovery
    include_dirs = [(root / name).resolve(strict=True) for name in profile.header.include_directories]
    if any(not path.is_relative_to(root) or not path.is_dir() for path in include_dirs):
        raise PraxisError("INVALID_PATH", "Header include directory escapes the source tree")
    flags = [*profile.header.defines, *[f"-I{path}" for path in include_dirs]]
    header = paths[profile.header.source]
    cpu = cmsis_cpu(profile.target)
    definitions = macros(header, "arm-none-eabi-gcc", [f"-mcpu={cpu}", "-mthumb", *flags])
    check_header_identity(profile.target, definitions)
    failures, origins, macro_origins = {}, {}, {}
    explicit_structures = [spec.structure for spec in policy.peripherals.values()]
    layouts = cmsis(header, None, flags, registered_sources=list(paths.values()), failures=failures,
                    cpu=cpu, origins=origins, macro_origins=macro_origins,
                    additional_structures=explicit_structures)
    source_paths = {path.resolve(): name for name, path in paths.items()}
    structure_sources = {}
    macro_sources = {name: source_paths[path] for name, path in macro_origins.items() if path in source_paths}
    for structure, path in origins.items():
        if path not in source_paths:
            raise PraxisError("UNKNOWN_SOURCE", f"Register structure {structure} needs a hash-registered source")
        structure_sources[structure] = source_paths[path]
    all_types = set(layouts) | set(failures)
    choices = {re.sub(r"_?(TypeDef|Type)$", "", name).lower():
               PeripheralDiscovery(structure=name) for name in sorted(all_types)}
    if len(set(explicit_structures)) != len(explicit_structures):
        raise PraxisError("DUPLICATE_ENTITY", "Multiple configured identities select the same structure")
    for entity, spec in policy.peripherals.items():
        for old in list(choices):
            if choices[old].structure == spec.structure:
                del choices[old]
        choices[entity] = spec
    if len({spec.structure for spec in choices.values()}) != len(choices):
        raise PraxisError("DUPLICATE_ENTITY", "Multiple canonical identities select the same structure")
    catalog, entries = {}, {}
    reviewed_ids = {p.id for p in reviewed}
    unknown_exclusions = set(policy.exclude) - choices.keys()
    if unknown_exclusions:
        raise PraxisError("INVALID_PROFILE", f"Unknown exclusions: {sorted(unknown_exclusions)}")
    for entity, spec in sorted(choices.items()):
        typed = {name: value for name, value in definitions.items()
                 if re.match(r"^\(\(\s*" + re.escape(spec.structure) + r"\s*\*", value)}
        typed.update(spec.instances)
        source = structure_sources.get(spec.structure, profile.header.source)
        entry = dict(structure=spec.structure, instances=sorted(typed), registers=0,
                     fields=0, selected=False, published=False, status="not_selected", issues=[],
                     provenance=f"{source}:{spec.structure}")
        entries[entity] = entry
        explicit = entity in policy.peripherals or entity in reviewed_ids
        selected = (policy.automatic or explicit) and entity not in policy.exclude
        entry["selected"] = selected and bool(typed)
        if not typed:
            entry["status"] = "unmapped_type"
            entry["issues"] = ["No typed instances: helper type or additional instance mapping required"]
            if explicit:
                raise PraxisError("MISSING_DECLARATION", f"{entity}: no supported typed instance macros")
            continue
        try:
            if spec.structure not in all_types:
                raise PraxisError("MISSING_DECLARATION", f"Structure not declared: {spec.structure}")
            if spec.structure in failures:
                raise PraxisError("UNSUPPORTED_DECLARATION", failures[spec.structure])
            found = parse_cmsis_headers(header, include_directories=include_dirs,
                defines=profile.header.defines, source_id=profile.header.source,
                core_source_id=source, registered_sources=list(paths.values()),
                cpu=cpu, structure_sources=structure_sources,
                macro_sources=macro_sources,
                stm32_views=profile.target.family == "stm32",
                mask_suffix=(profile.target.knowledge_adapter.mask_suffix
                             if profile.target.knowledge_adapter else "_Msk"),
                position_suffix=(profile.target.knowledge_adapter.position_suffix
                                 if profile.target.knowledge_adapter else "_Pos"),
                structures={entity: spec.structure}, prefixes={entity: spec.prefix or entity.upper()},
                layouts=layouts, definitions=definitions, relaxed=entity not in reviewed_ids,
                instance_expressions={entity: spec.instances},
                register_prefixes={entity: spec.register_prefixes},
                expand_arrays={entity: spec.expand_arrays},
                register_fields={entity: spec.register_fields})[entity]
            # Validate generic names/layout overlap before it can be selected for publication.
            if len({r.name for r in found.registers}) != len(found.registers):
                raise PraxisError("DUPLICATE_ENTITY", f"{entity}: flattened register name collision")
            catalog[entity] = found
            entry.update(instances=sorted(found.instances), registers=len(found.registers),
                         fields=sum(len(r.fields) for r in found.registers),
                         status="declarations_only" if selected else "not_selected")
            entry["issues"] = [*found.notes, *found.unresolved_masks]
            if spec.register_fields:
                entry["issues"].append("Configured field views: " + ", ".join(sorted(spec.register_fields)) +
                                       "; other overlapping mode encodings are not published")
            entry["unresolved_masks"] = found.unresolved_masks
        except (PraxisError, ValidationError) as exc:
            entry.update(status="blocked", issues=[str(exc)])
            if explicit and entity not in policy.exclude:
                raise PraxisError("DISCOVERY_BLOCKED", f"Configured peripheral {entity}: {exc}") from exc
    if not reviewed_ids <= catalog.keys() or reviewed_ids & set(policy.exclude):
        raise PraxisError("INVALID_PROFILE", "Reviewed definitions must have selected, extractable declarations")
    return catalog, entries


def mode_order(items):
    """Validate a separate, instance-scoped mode DAG; document retrieval stays independent."""
    modes = {f'{item.id}/{name}': mode for item in items for name, mode in item.operating_modes.items()}
    graph = {}
    for key, mode in modes.items():
        parents = []
        for dependency in mode.requires_modes:
            parent = f'{dependency.peripheral}/{dependency.mode}'
            if parent not in modes:
                raise PraxisError('UNKNOWN_MODE_DEPENDENCY', f'{key}: required mode {parent} is not published')
            if not set(dependency.instances) <= set(modes[parent].instances):
                raise PraxisError('MODE_INSTANCE_MISMATCH', f'{key}: required instances outside {parent} scope')
            parents.append(parent)
        graph[key] = parents
    return order(graph)


def workflow_coverage(profile, items, entries, topology=None):
    by_id = {item.id: item for item in items}
    graph = {item.id: item.prerequisites for item in items}
    order(graph)
    ordered_modes = mode_order(items)
    result = {}
    for workflow_name, requirement in sorted(profile.workflows.items()):
        issues, closure = [], set()
        if not requirement.registers.keys() <= set(requirement.peripherals):
            raise PraxisError("INVALID_PROFILE", f"{workflow_name}: registers name an undeclared workflow peripheral")

        def visit(entity, closure=closure, issues=issues, requirement=requirement):
            if entity in closure:
                return
            closure.add(entity)
            if entity not in by_id:
                issues.append(f"{entity}: not published")
                return
            item = by_id[entity]
            if requirement.operating_semantics and item.review is None:
                issues.append(f"{entity}: operating semantics not reviewed")
            for parent in graph[entity]:
                visit(parent)

        for entity in requirement.peripherals:
            visit(entity)
        mode_registers, selected_modes = {}, set()

        def visit_mode(entity, name, instances, issues=issues, selected_modes=selected_modes,
                       mode_registers=mode_registers, visit_document=visit):
            key = f'{entity}/{name}'
            visit_document(entity)
            item = by_id.get(entity)
            mode = item.operating_modes.get(name) if item else None
            if not instances:
                issues.append(f"{entity}: specify instance scope before claiming mode readiness")
            if mode is None:
                issues.append(f"{entity}.{name}: operating mode not reviewed")
                return
            if not set(instances) <= set(mode.instances):
                issues.append(f"{entity}.{name}: requested instances outside reviewed mode scope")
            if key in selected_modes:
                return
            selected_modes.add(key)
            mode_registers.setdefault(entity, set()).update(mode.registers)
            for dependency in mode.requires_modes:
                visit_mode(dependency.peripheral, dependency.mode, dependency.instances)

        for entity, modes in sorted(requirement.modes.items()):
            for name in modes:
                visit_mode(entity, name, requirement.instances.get(entity, []))
        for entity in sorted(closure):
            names = set(requirement.registers.get(entity, profile.header.required_registers.get(entity, [])))
            names.update(mode_registers.get(entity, set()))
            if requirement.operating_semantics and not names:
                issues.append(f"{entity}: specify workflow register requirements before claiming readiness")
            registers = {r.name: r for r in by_id[entity].registers} if entity in by_id else {}
            for register in sorted(names):
                if register not in registers:
                    issues.append(f"{entity}.{register}: register not published")
                elif requirement.operating_semantics and registers[register].access == "unknown":
                    issues.append(f"{entity}.{register}: access/operating semantics unreviewed")
        for entity, names in requirement.instances.items():
            available = {i.name for i in by_id[entity].instances} if entity in by_id else set()
            for name in names:
                if name not in available:
                    issues.append(f"{entity}.{name}: instance not published")
        for signal in requirement.signals:
            if topology is None:
                issues.append(f"{signal}: topology evidence unavailable")
                continue
            try:
                if topology.query(signal).startswith("No match"):
                    issues.append(f"{signal}: board connectivity not published")
            except PraxisError as exc:
                issues.append(f"{signal}: {exc.code}")
        result[workflow_name] = dict(ready=not issues, closure=sorted(closure), issues=sorted(set(issues)),
                            mode_scope=requirement.modes, instance_scope=requirement.instances,
                            required_signals=requirement.signals,
                            required_for_publication=workflow_name in profile.publication_requires)
        if any(by_id[key.split('/')[0]].operating_modes[key.split('/')[1]].requires_modes for key in selected_modes):
            result[workflow_name]['mode_order'] = [key for key in ordered_modes if key in selected_modes]
    return result


def report(profile, entries, items, topology=None):
    rows = {key: dict(value) for key, value in sorted(entries.items())}
    for item in items:
        rows[item.id].update(published=True,
            status=("reviewed_subset" if item.review is not None else
                    "partial_declarations" if rows[item.id].get("unresolved_masks") else "declarations_only"),
            prerequisites=item.prerequisites,
            reviewed_registers=sum(r.access != "unknown" for r in item.registers),
                            reviewed_modes={name: mode.instances for name, mode in sorted(item.operating_modes.items())},
            bytes_limit=65536)
    workflows = workflow_coverage(profile, items, rows, topology)
    blocks = [r for r in rows.values() if r["status"] != "unmapped_type"]
    return dict(format="praxis-coverage-v1", target=profile.target.id,
                scope="CMSIS register types and configured instances; not every MCU capability or board connection",
                counts=dict(register_blocks=len(blocks), published=sum(r["published"] for r in blocks),
                            unmapped_types=sum(r["status"] == "unmapped_type" for r in rows.values()),
                            reviewed_subsets=sum(r["status"] == "reviewed_subset" for r in blocks),
                            blocked=sum(r["status"] == "blocked" for r in blocks),
                            registers=sum(r["registers"] for r in blocks if r["published"]),
                            fields=sum(r["fields"] for r in blocks if r["published"])),
                publication_ready=all(w["ready"] for w in workflows.values()
                                      if w["required_for_publication"]),
                peripherals=rows, workflows=workflows,
                limits=["Reviewed subsets do not establish support for every mode or instance.",
                        "Unreviewed declarations must not be used as initialization guidance.",
                        "Header absence does not prove that silicon lacks a capability.",
                        "Package availability, routing, timing and physical tests remain separate evidence."])


def markdown(data):
    rows = [[name, r["structure"], ", ".join(r["instances"]), r["status"],
             r["registers"], r["fields"], r.get("reviewed_registers", 0),
             ", ".join(r.get("prerequisites", [])), "; ".join(r["issues"]), r["provenance"]]
            for name, r in data["peripherals"].items()]
    text = ("## Peripheral coverage\n\n" + data["scope"] + ". "
            "Dependencies are profile retrieval policy, not a proven hardware initialization sequence. "
            "`reviewed_subset` covers only the facts explicitly reviewed. "
            "`declarations_only` supplies layouts and masks, never operating guidance.\n\n" +
            table(["Entity", "Structure", "Instances", "Status", "Registers", "Fields", "Reviewed registers",
                   "Requires", "Issues", "Provenance"], rows))
    headers = ["Workflow", "Ready", "Required", "Dependency closure", "Missing evidence"]
    rows = [[name, w["ready"], w["required_for_publication"], ", ".join(w["closure"]),
             "; ".join(w["issues"])] for name, w in data["workflows"].items()]
    if any('mode_order' in w for w in data['workflows'].values()):
        headers.append('Required mode order')
        for row, workflow in zip(rows, data['workflows'].values(), strict=True):
            row.append(' → '.join(workflow.get('mode_order', [])))
    text += "\n## Workflow readiness\n\n" + table(headers, rows)
    return (text + "\n" + "\n".join("- " + limit for limit in data["limits"])
            + "\n\nComplete source hashes, versions and origins: [[sources]].\n")
