"""Deterministic routing scenarios, not a benchmark of a live language model."""

from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.routing import Session


def evaluate(bundle: Bundle) -> dict:
    from praxis.coverage import order
    route = order(bundle.dependencies)
    unknown = "praxis_nonexistent"
    while unknown in bundle.manifest.peripherals or unknown in bundle.manifest.aliases:
        unknown += "_x"
    guarded = next((name for name in reversed(route) if bundle.dependencies[name]),
                   route[-1] if route else unknown)
    requested = guarded
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
         "UNKNOWN_PERIPHERAL" if not route else
         "PREREQUISITE_REQUIRED" if bundle.dependencies[requested] else None)
    net = next(iter(session.netlist.nets), "praxis_connectivity_unavailable")
    step("query_schematic_netlist", net)
    missing_query = "praxis_absent_net"
    while missing_query in session.netlist.exact or missing_query.casefold() in session.netlist.pins:
        missing_query += "_x"
    missing = step("query_schematic_netlist", missing_query)
    step("read_peripheral_doc", unknown, "UNKNOWN_PERIPHERAL")
    for name in route:
        step("read_peripheral_doc", name)
    step("read_peripheral_doc", unknown, "UNKNOWN_PERIPHERAL")
    return {"target": bundle.manifest.target.id, "revision": bundle.manifest.bundle_revision,
            "kind": "deterministic retrieval replay; no model calls",
            "passed": all(t["passed"] for t in trace) and missing.startswith("No match"),
            "trace": trace,
            "limits": "Does not validate a live assistant, arbitrary emitted C, or physical behavior"}
