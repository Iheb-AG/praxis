"""Dependency-driven review scopes; requirements are authored, never inferred from prose."""

from praxis.coverage import order
from praxis.errors import PraxisError


def plan(profile, reviewed, declarations, workflow_name):
    if workflow_name not in profile.workflows:
        raise PraxisError("UNKNOWN_WORKFLOW", "Select an exact workflow declared by the profile")
    requirement = profile.workflows[workflow_name]
    by_id = {item.id: item for item in reviewed}
    graph = {}
    for entity in declarations:
        spec = profile.discovery.peripherals.get(entity)
        graph[entity] = (spec.prerequisites if spec and spec.prerequisites is not None else
                         by_id[entity].prerequisites if entity in by_id else
                         profile.discovery.default_prerequisites)
    # Validate only the requested document closure; unrelated unmapped types are not prerequisites.
    closure = {}

    def visit(entity):
        if entity in closure:
            return
        if entity not in graph:
            raise PraxisError("MISSING_DECLARATION", f"{entity}: no extractable declaration for workflow review")
        closure[entity] = graph[entity]
        for parent in graph[entity]:
            visit(parent)

    for entity in requirement.peripherals:
        visit(entity)
    registers, modes, unresolved, active_modes = {}, set(), [], set()

    def visit_mode(entity, name, instances):
        visit(entity)
        key = f"{entity}/{name}"
        if not instances:
            unresolved.append(f"{key}: requested instance scope is missing")
        mode = by_id.get(entity).operating_modes.get(name) if entity in by_id else None
        if mode is None:
            unresolved.append(f"{key}: operating contract requires review")
            return
        if not set(instances) <= set(mode.instances):
            unresolved.append(f"{key}: requested instances outside the reviewed contract")
        if key in active_modes:
            raise PraxisError("DEPENDENCY_CYCLE", f"Operating-mode dependency cycle at {key}")
        if key in modes:
            return
        modes.add(key)
        active_modes.add(key)
        registers.setdefault(entity, set()).update(mode.registers)
        for dependency in mode.requires_modes:
            visit_mode(dependency.peripheral, dependency.mode, dependency.instances)
        active_modes.remove(key)

    for entity, names in sorted(requirement.modes.items()):
        for name in names:
            visit_mode(entity, name, requirement.instances.get(entity, []))
    route = order(closure)
    for entity in route:
        names = set(requirement.registers.get(entity, profile.header.required_registers.get(entity, [])))
        names.update(registers.get(entity, set()))
        if not names:
            unresolved.append(f"{entity}: explicit register review scope is missing")
        available = {register.name for register in declarations[entity].registers}
        if not names <= available:
            raise PraxisError("MISSING_DECLARATION", f"{entity}: unknown review registers {sorted(names - available)}")
        registers[entity] = sorted(names)
    return dict(workflow=workflow_name, retrieval_order=route, registers=registers,
                requested_instances=requirement.instances, requested_modes=requirement.modes,
                reviewed_mode_closure=sorted(modes), required_signals=requirement.signals,
                unresolved=sorted(set(unresolved)))
