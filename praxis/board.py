"""Reviewed board semantics, checked against explicit electrical net membership.

Paths traverse only named, fitted two-terminal components. They do not union nets
or infer polarity from a reference prefix. PDF transcriptions use the same checks.
"""

from __future__ import annotations

import json
from typing import Annotated, Literal

from pydantic import Field, ValidationError, model_validator

from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Identifier, Record, Review, Schematic, SourceRef
from praxis.render import identity, refs, table

SIGNAL_COLUMNS = ["Signal", "Aliases", "Kind", "MCU pin", "Endpoint", "Active level",
                  "Pull", "Circuit nets", "Sources"]
COMPONENT_COLUMNS = ["Reference", "Value", "Kind", "Fitted", "Package", "Sheet", "Pins", "Properties", "Sources"]


class BoardFact(Record):
    id: Identifier
    value: str = Field(min_length=1, max_length=4096)
    state: Literal["documented", "design-assumption", "unresolved"]
    sources: list[SourceRef] = Field(min_length=1)


class Signal(Record):
    id: Identifier
    aliases: list[str] = Field(min_length=1)
    pin: str = Field(min_length=1)
    endpoint: str = Field(min_length=1)
    active_level: Literal["high", "low"]
    sources: list[SourceRef] = Field(min_length=1)


class LedSignal(Signal):
    kind: Literal["led"]
    led: str
    anode: str
    cathode: str
    series_path: list[str] = Field(min_length=1)


class ButtonSignal(Signal):
    kind: Literal["button"]
    switch: str
    signal_terminal: str
    pressed_terminal: str
    signal_path: list[str]
    pressed_path: list[str]
    pull_resistor: str
    pull: Literal["external-up", "external-down"]


class BoardDefinition(Record):
    schema_version: Literal[1] = 1
    model: str = Field(min_length=1)
    board_revision: str = Field(min_length=1)
    applicability: str = Field(min_length=1)
    coverage: Literal["partial", "complete"]
    omissions: list[str]
    ground_nets: list[str] = Field(min_length=1)
    supply_nets: list[str] = Field(min_length=1)
    signals: list[Annotated[LedSignal | ButtonSignal, Field(discriminator="kind")]] = Field(min_length=1)
    facts: list[BoardFact] = Field(min_length=1)
    review: Review

    @model_validator(mode="after")
    def identities(self):
        identities, aliases = set(), set()
        for signal in self.signals:
            if signal.id in identities:
                raise ValueError("Duplicate board signal identity")
            identities.add(signal.id)
            for alias in [signal.id, *signal.aliases]:
                if (alias in aliases or not alias or len(alias) > 128 or
                        any(c in alias for c in (";", "\n", "\r", "|"))):
                    raise ValueError("Duplicate or invalid board signal alias")
                aliases.add(alias)
        if len({fact.id for fact in self.facts}) != len(self.facts):
            raise ValueError("Duplicate board fact identity")
        if self.coverage == "partial" and not self.omissions:
            raise ValueError("Partial board knowledge must identify omitted circuits")
        return self


def load(path):
    try:
        return BoardDefinition.model_validate(load_json(path.read_bytes()))
    except ValidationError as exc:
        raise PraxisError("INVALID_BOARD", str(exc)) from exc


def validate_schematic(schematic: Schematic, target, pin_map, source_ids):
    components = {c.ref: c for c in schematic.components}
    if len(components) != len(schematic.components):
        raise PraxisError("DUPLICATE_ENTITY", "Duplicate component identity")
    mcu = components.get(target.primary_mcu_ref)
    if not mcu or (mcu.value, mcu.package) != (target.mcu, target.package):
        raise PraxisError("PACKAGE_MISMATCH", "Schematic MCU value/package differs from target")
    endpoints, names = {}, set()
    references = [s for component in schematic.components for s in component.sources]
    for net in schematic.nets:
        if net.name in names:
            raise PraxisError("DUPLICATE_ENTITY", "Duplicate net identity")
        names.add(net.name)
        references.extend(net.sources)
        for pin in net.pins:
            component = components.get(pin.ref)
            if (component is None or pin.number not in component.pins or
                    component.pins[pin.number] != pin.name or component.package != pin.package or
                    component.sheet != pin.sheet):
                raise PraxisError("PIN_MISMATCH", f"Undeclared component/pin metadata: {pin.endpoint}")
            if pin.endpoint in endpoints:
                raise PraxisError("INVALID_NETLIST", f"Endpoint belongs to multiple nets: {pin.endpoint}")
            endpoints[pin.endpoint] = net.name
            if pin.ref == target.primary_mcu_ref and pin_map.get(pin.number) != pin.name:
                raise PraxisError("PIN_MISMATCH", f"Wrong MCU package pin: {pin.endpoint}")
            references.extend(pin.sources)
    if any(ref.source not in source_ids for ref in references):
        raise PraxisError("UNKNOWN_SOURCE", "Schematic fact has unregistered provenance")
    return components, endpoints


def validate(board: BoardDefinition, schematic, target, pin_map, authorities, workflows):
    components, endpoints = validate_schematic(schematic, target, pin_map, set(authorities))
    if board.board_revision != target.board_revision:
        raise PraxisError("TARGET_MISMATCH", "Board semantics and target revision differ")
    if set(board.ground_nets) & set(board.supply_nets):
        raise PraxisError("BOARD_CONFLICT", "Ground and supply rail identities overlap")
    if not set(board.ground_nets + board.supply_nets) <= set(endpoints.values()):
        raise PraxisError("UNKNOWN_NET", "Board rail absent from schematic")
    pins = {pin.endpoint: pin for net in schematic.nets for pin in net.pins}
    circuits = {}

    def component(ref, allowed):
        item = components.get(ref)
        if item is None or item.kind not in allowed or not item.fitted:
            raise PraxisError("BOARD_CONFLICT", f"Expected a fitted {sorted(allowed)}: {ref}")
        return item

    def pair(ref, allowed):
        item = component(ref, allowed)
        terms = [f"{ref}:{number}" for number in item.pins]
        if len(terms) != 2 or any(term not in endpoints for term in terms):
            raise PraxisError("BOARD_CONFLICT", f"Require two connected terminals: {ref}")
        if endpoints[terms[0]] == endpoints[terms[1]]:
            raise PraxisError("BOARD_CONFLICT", f"Component terminals shorted in topology: {ref}")
        return terms

    def walk(start, through):
        if start not in endpoints or len(through) != len(set(through)):
            raise PraxisError("BOARD_CONFLICT", "Unknown endpoint or repeated component in circuit path")
        current = endpoints[start]
        traversed = [current]
        for ref in through:
            terms = pair(ref, {"resistor", "bridge"})
            nets = [endpoints[term] for term in terms]
            if current not in nets:
                raise PraxisError("BOARD_CONFLICT", f"Disconnected series path through {ref}")
            current = nets[1 - nets.index(current)]
            traversed.append(current)
        return current, traversed

    all_refs = [ref for fact in board.facts for ref in fact.sources]
    for signal in board.signals:
        all_refs.extend(signal.sources)
        if not any(authorities.get(ref.source) == "connectivity" for ref in signal.sources):
            raise PraxisError("SOURCE_AUTHORITY", "Board signal requires schematic connectivity provenance")
        pin = pins.get(signal.endpoint)
        if not pin or pin.ref != target.primary_mcu_ref or pin.name != signal.pin:
            raise PraxisError("PIN_MISMATCH", f"Board signal {signal.id} disagrees with MCU endpoint")
        if isinstance(signal, LedSignal):
            led = component(signal.led, {"led"})
            if (signal.anode not in endpoints or signal.cathode not in endpoints or
                    signal.anode == signal.cathode or
                    not signal.anode.startswith(led.ref + ":") or
                    not signal.cathode.startswith(led.ref + ":") or
                    led.pins.get(signal.anode.split(":")[1]) != "A" or
                    led.pins.get(signal.cathode.split(":")[1]) != "K"):
                raise PraxisError("BOARD_CONFLICT", "LED terminal identities must establish anode and cathode")
            reached, nets = walk(signal.endpoint, signal.series_path)
            for ref in signal.series_path:
                component(ref, {"resistor"})
            driven = signal.anode if signal.active_level == "high" else signal.cathode
            returned = signal.cathode if signal.active_level == "high" else signal.anode
            rail = board.ground_nets if signal.active_level == "high" else board.supply_nets
            if reached != endpoints[driven] or endpoints[returned] not in rail:
                raise PraxisError("BOARD_CONFLICT", "LED polarity/active level conflicts with its connected rails")
            circuits[signal.id] = sorted(set([*nets, endpoints[returned]]))
        else:
            switch = component(signal.switch, {"switch"})
            terminals = {f"{switch.ref}:{number}" for number in switch.pins}
            if (not {signal.signal_terminal, signal.pressed_terminal} <= terminals or
                    not terminals <= endpoints.keys() or
                    len({endpoints[term] for term in terminals}) != 2 or
                    endpoints[signal.signal_terminal] == endpoints[signal.pressed_terminal] or
                    switch.properties.get("contact") != "normally-open"):
                raise PraxisError("BOARD_CONFLICT", "Button switch terminals disagree")
            reached, nets = walk(signal.endpoint, signal.signal_path)
            if reached != endpoints[signal.signal_terminal]:
                raise PraxisError("BOARD_CONFLICT", "Button is disconnected from its declared MCU pin")
            pull_terms = pair(signal.pull_resistor, {"resistor"})
            pull_nets = {endpoints[term] for term in pull_terms}
            down = signal.pull == "external-down"
            idle_rails = board.ground_nets if down else board.supply_nets
            pressed_rails = board.supply_nets if down else board.ground_nets
            if reached not in pull_nets or not (pull_nets - {reached}) <= set(idle_rails):
                raise PraxisError("BOARD_CONFLICT", "Button pull resistor does not establish the declared idle level")
            pressed, extra = walk(signal.pressed_terminal, signal.pressed_path)
            if pressed not in pressed_rails or signal.active_level != ("high" if down else "low"):
                raise PraxisError("BOARD_CONFLICT", "Button pressed rail and active level conflict")
            circuits[signal.id] = sorted(set([*nets, *extra, *pull_nets]))
    if any(ref.source not in authorities for ref in all_refs):
        raise PraxisError("UNKNOWN_SOURCE", "Board fact has unregistered provenance")
    if "led_button_polling" in workflows:
        selected = {alias: signal for signal in board.signals for alias in signal.aliases}
        if (not {"LED_A", "LED_B", "USER_BUTTON"} <= selected.keys() or
                any(selected[name].kind != "led" for name in ("LED_A", "LED_B")) or
                selected["USER_BUTTON"].kind != "button"):
            raise PraxisError("UNREVIEWED_REQUIRED_FACT", "LED/button workflow requires LED_A, LED_B and USER_BUTTON")
        if len({selected[name].endpoint for name in ("LED_A", "LED_B", "USER_BUTTON")}) != 3:
            raise PraxisError("BOARD_CONFLICT", "LED/button workflow requires three distinct MCU pins")
        facts = {fact.id: fact for fact in board.facts}
        required = {"clock_recipe", "timing_source", "systick_clock_source", "systick_ms_formula"}
        if not required <= facts.keys() or any(facts[name].state == "unresolved" for name in required):
            raise PraxisError("UNREVIEWED_REQUIRED_FACT", "LED/button workflow requires reviewed clock/timing facts")
    return circuits


def render_components(target, schematic):
    return ("# Schematic component catalog\n\n" + identity(target) +
        "\nValues and fitted status describe imported sources. Circuit roles and electrical suitability "
        "require reviewed semantics. See [[schemas/custom_pcb_netlist]] and [[sources]].\n\n" +
        table(COMPONENT_COLUMNS, [[c.ref, c.value, c.kind, c.fitted, c.package, c.sheet,
            "; ".join(f"{number}={name}" for number, name in sorted(c.pins.items())),
            json.dumps(c.properties, sort_keys=True), refs(c.sources)]
            for c in sorted(schematic.components, key=lambda c: c.ref)]))


def render_board(target, board, circuits, *, prerequisite_documents=("rcc", "gpio")):
    rows = [[s.id, ";".join(s.aliases), s.kind, s.pin, s.endpoint, s.active_level,
             s.pull if isinstance(s, ButtonSignal) else "none; output",
             ";".join(circuits[s.id]), refs(s.sources)] for s in sorted(board.signals, key=lambda s: s.id)]
    return ("# Reviewed board wiring and operating assumptions\n\n" + identity(target) +
        f"\nBoard model: {board.model}. Reference revision: {board.board_revision}.\n\n"
        f"Applicability: {board.applicability}\n\nCoverage: {board.coverage}. "
        "Net memberships are complete for the imported scope; this is not a full-board electrical audit.\n\n"
        "## GPIO signal assignments\n\n" + table(SIGNAL_COLUMNS, rows) +
        "\n## Clock and timing facts\n\n" + table(["Fact", "State", "Value", "Sources"],
            [[fact.id, fact.state, fact.value, refs(fact.sources)] for fact in sorted(board.facts, key=lambda f: f.id)]) +
        "\n## Circuit interpretation\n\n" +
        "Paths cross only explicitly reviewed fitted components. Adjacent nets remain distinct. "
        "Solder bridges and board modifications must match the reference before physical use.\n\n" +
        "\n".join(f"- {s.id}: " + (f"MCU → {' → '.join(s.series_path)} → {s.led}; "
            f"anode {s.anode}, cathode {s.cathode}." if isinstance(s, LedSignal) else
            f"MCU → {' → '.join(s.signal_path)} → {s.switch}; pull {s.pull_resistor}; "
            f"pressed rail path {' → '.join(s.pressed_path) or 'direct'}." )
            for s in sorted(board.signals, key=lambda s: s.id)) +
        "\n\n## Omitted scope\n\n" + "\n".join(f"- {item}" for item in board.omissions) +
        f"\n\nEditorial reviewer: {board.review.reviewer}. Basis: {board.review.basis}. "
        "Independent hardware sign-off remains separate.\n\n"
        "See [[index]], [[schemas/components]], [[schemas/custom_pcb_netlist]], " +
        "".join(f"[[peripherals/{name}]], " for name in prerequisite_documents) + "and [[sources]].\n")
