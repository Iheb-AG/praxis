# Reliability stabilization

The immediate objective is a usable experimental MCP that reliably completes a
small declared set of real projects. Full F407/all-mode coverage is not a prerequisite
for that experimental release. Add support incrementally after existing project
paths work reproducibly; keep unsupported requests and qualification limits explicit.
This plan does not convert historical evidence into current acceptance. Independent
review remains pending in `release-review.json`.

## Usable experimental scope

Prioritize the existing LED/button and UART loopback project paths, with timer
PWM/capture as a further scoped path. For each selected path, acceptance should cover
fresh project setup, correct knowledge/service selection, complete application
generation, isolated build and ELF validation, report generation, and separately
approved exact-artifact board testing where physical behavior is claimed.
Historical examples are starting points, not proof that these fresh end-to-end
acceptance runs have already passed. The external-component scanner remains a
software-prepared reference project until its actual interfaces are validated.

Do not delay usability work to enumerate every MCU mode. Publish a finite supported
project list with prerequisites, tested revisions, known limits and reproducible
commands. Add a new project or peripheral mode only with matching source contracts
and verification. Qualified v1/production claims remain separate from alpha usability.

## 1. Detect provisioning failures

Implemented: `praxis project-check --root PROJECT` checks project isolation, selected
bundle integrity, build/inspection bindings and local launch settings without starting
processes or accessing hardware. It rejects drift instead of silently changing state.
Tests cover corrupted/missing inputs, wrong-project settings, disabled services,
unexpected environment settings and selection changes during diagnosis.

The test dependency helper now distinguishes a Podman runtime error from a missing
image, preserving bounded diagnostic output instead of requesting needless installation.

Implemented next: `project-check --live` initializes fresh sessions using validated
canonical commands, checks tool catalogs and compares returned target/revision/generation.
It reads only the index and service descriptions/inventory, with bounded timeouts.
Unreviewed launch overrides block diagnosis; no probe operations are invoked.
Both static and live checks leave client trust and existing chat sessions unverified.

## 2. Establish one current support record

Implemented: `praxis status --registry current-status.json --format markdown` generates
[CURRENT_STATUS.md](CURRENT_STATUS.md). Knowledge scope comes from the verified bundle;
the registry pins each reported evidence file by digest and selects exact JSON fields.
Other bundle revisions are explicitly historical. Independent review is a separate
record, not inferred from source hashes or test outcomes. No overlapping counts are
added and no all-MCU percentage is reported. The README links to this snapshot.

To update the selected public baseline, explicitly choose its immutable bundle and
revision in `current-status.json`, register evidence hashes/fields and regenerate the
Markdown. `tests/test_status.py` rejects a stale checked-in snapshot. The registry
is not a complete catalog of every experiment; its chosen reports remain historical
observations and do not certify current source code. Running the status command is
offline and does not execute tests or upgrade release qualification.

## 3. Strengthen repeatable execution

Require the existing project-isolation, persistent-session handoff, rootless-build,
artifact-validation and source-replay checks with `PRAXIS_REQUIRE_EXTERNAL_TOOLS=1`.
Add failure/recovery cases as defects are reproduced. Retain external-tool failures;
do not replace them with skipped checks. Verify a clean checkout and installed-package
path before claiming release reproducibility.

## 4. Qualify engineering outcomes

Use fixed, supported tasks with the same model and inputs, with and without Praxis.
Record unsupported assumptions, source correctness, build success, task completion,
tokens/time and separately approved physical observations. Existing retrieval-load
benchmarks establish transport performance, not improvement in generated firmware.

Keep physical trials bound to exact images and configurations. Acquire independent
review for the supported operating contracts and integration assets. Neither PDF
generation nor a passing build can establish electrical correctness.

## 5. Harden evidence ingestion

Move untrusted PDF processing into bounded isolated workers, retaining complete
source provenance and explicit extraction failures. Keep author interpretation and
independent review separate. Only publish hardware meaning supported by reviewed
evidence; unknown visual relationships remain unresolved.

## Current increment validation

The project-check increment is configuration diagnostics, not a full release
qualification. Run its tests together with project and handoff integration:

```sh
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q tests/test_project_live.py tests/test_project_check.py tests/test_project_workspace.py tests/test_bundle_handoff.py
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run ruff check praxis tests tools server.py compiler.py
```

Next: clean-checkout reproducibility and ingestion isolation. Keep independent review
and full F407 acceptance open. Live service diagnosis does not certify generated firmware.
