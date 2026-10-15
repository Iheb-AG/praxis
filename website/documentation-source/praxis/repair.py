"""Optional local orchestration hook; no model SDK or shell command interface."""

from collections.abc import Callable


def repair_loop(verify: Callable[[], dict], repair: Callable[[dict], bool]) -> dict:
    """At most three verification attempts; callbacks own source edits, never vault edits.

    A repair callback must return False when facts are missing or unsupported. Hosts should
    snapshot the vault independently; no automatic source edits occur without a callback.
    """
    attempts, diagnostics = [], set()
    for attempt in range(1, 4):
        report = verify()
        attempts.append({"attempt": attempt, **report})
        if report["compile_passed"]:
            return {"stop": "passed", "attempts": attempts}
        signature = tuple((r.get("failure"), r.get("diagnostics")) for r in report["records"])
        if signature in diagnostics:
            return {"stop": "repeated_diagnostics", "attempts": attempts}
        diagnostics.add(signature)
        if attempt == 3:
            return {"stop": "attempt_limit", "attempts": attempts}
        if not repair(report):
            return {"stop": "unsupported_or_missing_facts", "attempts": attempts}
    raise AssertionError("Unreachable")

