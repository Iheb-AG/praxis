"""Deterministic routing scenarios, not a benchmark of a live language model."""

from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.routing import Session


def evaluate(bundle: Bundle) -> dict:
    family = bundle.manifest.target.family
    route = ["rcc", "gpio", "usart", "nvic"] if family == "stm32" else ["clock", "gpio", "usart", "interrupts"]
    if bundle.manifest.schema_version == 2:
        from praxis.coverage import order
        route = order(bundle.dependencies)
    custom = bundle.manifest.target.knowledge_adapter is not None
    unknown = "praxis_nonexistent"
    while unknown in bundle.manifest.peripherals or unknown in bundle.manifest.aliases:
        unknown += "_x"
    guarded = next((name for name in reversed(route) if bundle.dependencies[name]),
                   route[-1] if route else unknown)
    requested = guarded if custom else "usart"
    session = Session(bundle)
    trace = []

    def step(tool, argument=None, expected=None):
        try:
            result = getattr(session, tool)(*(() if argument is None else (argument,)))
            status = "ok"
        except PraxisError as exc:
            result, status = str(exc), exc.code
        passed = status == (expected or "ok")
        trace.append({"tool": tool, "argument": argument, "status": status, "passed": passed,
                      "result_sha256": digest(result.encode())})
        return result

    step("read_peripheral_doc", requested, "PREREQUISITE_REQUIRED")
    step("read_wiki_index")
    step("read_peripheral_doc", requested,
         "UNKNOWN_PERIPHERAL" if custom and not route else
         "PREREQUISITE_REQUIRED" if not custom or bundle.dependencies[requested] else None)
    net = next(iter(session.netlist.nets)) if custom else "USART2_TX" if family == "stm32" else "USART0_TX"
    step("query_schematic_netlist", net)
    missing_query = "praxis_absent_net" if custom else "PA99" if family == "stm32" else "PD99"
    while custom and (missing_query in session.netlist.exact or missing_query.casefold() in session.netlist.pins):
        missing_query += "_x"
    missing = step("query_schematic_netlist", missing_query)
    foreign = unknown if custom else "clock" if family == "stm32" else "rcc"
    step("read_peripheral_doc", foreign, "UNKNOWN_PERIPHERAL")
    for name in route:
        step("read_peripheral_doc", name)
    if bundle.manifest.schema_version == 2:
        step("read_peripheral_doc", unknown, "UNKNOWN_PERIPHERAL")
    else:
        step("read_peripheral_doc", "dma", "UNKNOWN_PERIPHERAL")
    return {"target": bundle.manifest.target.id, "revision": bundle.manifest.bundle_revision,
            "kind": "deterministic retrieval replay; no model calls",
            "passed": all(t["passed"] for t in trace) and missing.startswith("No match"),
            "trace": trace,
            "limits": "Does not validate a live assistant, arbitrary emitted C, or physical behavior"}
