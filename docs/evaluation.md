# Evaluation, evidence and publication claims

## What can be claimed now

Praxis implements offline, target-bound hardware compilation and deterministic vectorless
retrieval through three MCP tools. Milestone 1's implementation acceptance passed. The complete
v1 release gate remains open. This document separates existing evidence from proposed experiments
so a publication does not conflate tests, model behavior and physical operation.

| Claim | Existing evidence | Limit |
| --- | --- | --- |
| Identical supported inputs/tools reproduce a bundle | Cross-location deterministic compilation tests | Not all tool versions or arbitrary source formats |
| Published knowledge is internally validated | Hash, link, graph, size, encoding and negative fixture tests | Not proof that the external source or reviewer is correct |
| Exact net retrieval preserves imported connectivity | Golden endpoint checks, live KiCad exports and board circuit tests | Partial fixtures do not establish full-board electrical coverage |
| HEDG gates require prerequisite reads | Session negative/concurrency tests and real stdio tests | Cannot prove emitted instruction order |
| Runtime retrieval is independent of ingestion tools | Copied-bundle subprocess tests block ingestion imports, network and subprocess use | Host/model may independently use other capabilities |
| Discovery reference aliases resolve | Board tests, real stdio test and reported OpenCode walkthrough | Physical PCB revision and behavior unconfirmed |
| Selected example configuration/order checks pass | Reviewed golden cases, target compilation and instrumented host models | Not arbitrary generated code or full silicon simulation |
| Compilation isolation is implemented | Runner and policy tests | Live Podman integration remains unqualified in this environment |

Recorded on 2026-10-10: the dedicated Milestone 1 suite passed **131 tests without skips**.
The broader suite passed **158 tests with two Podman checks skipped**, with KiCad 9.0.4 available.
Ruff and wheel/source-distribution builds passed. These are implementation results, not model
accuracy percentages. Exact bundle revisions and tool paths are in
[milestone1-evidence.json](milestone1-evidence.json). CI configuration exists, but local test
results do not assert that a hosted CI run has completed.

## Separate outcome layers

1. **Acquisition:** the intended source bytes were obtained and their revision recorded.
2. **Knowledge validity:** supported extracted/reviewed records agree with their source scope and
   pass mechanical checks.
3. **Retrieval compliance:** actual calls selected the intended bundle and met read prerequisites.
4. **Generated configuration:** code uses reviewed pins, masks, clock arithmetic and flag semantics.
5. **Execution order evidence:** supported instrumentation checks prerequisite writes and final
   enablement; arbitrary direct-register code needs additional analysis/review.
6. **Compilation/linking:** executed tools produced the stated syntax, objects or linked image.
7. **Physical behavior:** a documented board setup behaved as measured.

Passing a later compiler step does not retroactively establish an earlier wiring assumption.
Passing retrieval does not establish any compile or physical result. A report should mark
unperformed layers NOT RUN rather than converting an assistant's expectation into evidence.

The current verify CLI covers syntax/object modes, not linking. A client-generated Makefile
build is separate host activity; record its commands and environment without labeling it as a
Praxis sandbox result.

## Reproduction map

| Evidence | Entry point |
| --- | --- |
| Header layouts, macros, native KiCad and DTS | [test_compiler_adapters.py](../tests/test_compiler_adapters.py) |
| Complete supported F407 declarations and package facts | [test_f407_ingestion.py](../tests/test_f407_ingestion.py) |
| Discovery board paths, aliases and negative facts | [test_board_ingestion.py](../tests/test_board_ingestion.py) |
| Snapshot integrity, paths, exact lookup and session gates | [test_bundle_routing.py](../tests/test_bundle_routing.py) |
| Actual tool discovery/calls over stdio | [test_mcp_stdio.py](../tests/test_mcp_stdio.py) |
| Web archive extraction, integrity and review | [test_web_import.py](../tests/test_web_import.py) |
| Checked-in firmware examples and configuration models | [test_examples.py](../tests/test_examples.py) |
| Sandbox policy and external integration | [test_verification.py](../tests/test_verification.py) |
| No-skip Milestone 1 gate | [milestone1_check.py](../tools/milestone1_check.py) |
| Overall release qualification | [release_check.py](../tools/release_check.py) |

Install the documented external dependencies before reproducing these results. KiCad was
temporarily extracted under /tmp for the recorded local checks; it is not globally installed.
An ordinary pytest run can skip unavailable external integration tests. The milestone/release
gates must not interpret such skips as qualification. The acceptance command and prerequisites
are documented in [Milestone 1](milestone1.md).

`praxis evaluate` replays deterministic routing scenarios without a model. It is not a live
agent benchmark. Current status and outstanding review/sandbox items are in [STATUS.md](STATUS.md).

The current release checker's exact-revision review comparison covers the original F401/AVR
bundles. It must be extended to cover any additional F407/Discovery targets before using it to
qualify a release that includes those targets. The Milestone 1 report lists all four bundles,
but does not provision the sandbox or replace an independent release review.

## Proposed controlled assistant evaluation

This is a protocol for future experiments, not an experiment already run. Use a frozen repository
revision, dependency lock, bundle revisions, task set and model/client configuration. Preserve
actual tool traces and generated artifacts. Define pass conditions before inspecting outputs.

Suggested task groups are GPIO blinking/button polling, polling UART, interrupt-driven UART,
wrong-target requests, unavailable board pins, clock-dependent divisors and unsupported DMA.
Separate tested fixture tasks from held-out tasks. If board support is added during evaluation,
report that change rather than mixing pre- and post-curation scores.

Compare controlled conditions such as:

- Host/model with a fixed firmware project but no Praxis evidence.
- The same host/model/project with curated documents and no read gates.
- The same host/model/project with exact Praxis retrieval and gates.

A dense-retrieval baseline is optional. If included, freeze its corpus, chunking, embedding and
ranking settings, and give it the same source scope and context budget. Do not attribute a result
to vectorless retrieval when one condition has better sources or more reviewed semantics.

Useful ablations include removing board semantics, removing prerequisite gates and changing
canonical aliases. Intentionally incomplete evidence should be scored on correct abstention as
well as task completion. Prevent a reference solution or expected pins in the prompt from
substituting for retrieval evidence.

| Metric | Definition or recording rule |
| --- | --- |
| Target identification | Fraction of runs that correctly verify or reject the selected target |
| Evidence coverage | Required supported facts retrieved with valid source locators |
| Retrieval compliance | Required successful read sequence in actual tool traces |
| Unsupported-fact rate | Unsupported hardware assertions divided by scored hardware assertions |
| Abstention behavior | Correct stop/report on intentionally missing or conflicting facts |
| Configuration correctness | Reviewed expected pins, masks, clock basis and side-effect handling |
| Compilation/link success | Actual tool outcomes, separated by syntax, object and link stage |
| Ordering evidence | Supported instrumented checks; manual review reported separately |
| Context cost | Actual returned token counts, including repeated board context |
| Retrieval latency | Cold startup and warm calls measured separately, with environment details |
| Authoring cost | Review time, normalization effort and corrections per supported board/workflow |
| Physical result | Recorded hardware observation on a confirmed revision and setup |

Repeat runs across the chosen model settings and report sample counts and uncertainty. Publish
failure cases, source omissions and unsupported tasks. A single successful OpenCode conversation
establishes a walkthrough, not a general hallucination reduction rate.

## Validity and deployment limits

Fixture size and curation can inflate apparent success. Model prior knowledge can supply correct
answers without using the server. Pin answers placed in prompts can leak the scoring key. An
assistant may claim tool execution or compilation that never occurred. Require actual traces and
tool outputs, and distinguish model reports from independently captured evidence.

The server cannot prevent a host from reading other files, calling other tools or ignoring its
instructions. Imported source text is untrusted evidence; keeping it separate from authored
instructions reduces ambiguity but is not a proof against prompt injection. Parser hardening does
not constitute a general OS sandbox for offline acquisition/ingestion. The PDF parser currently
does not run in an OS sandbox.

Internal hashes are not signatures. Review records are not independent sign-off unless an
independent reviewer actually performed the review. Software licensing does not automatically
grant redistribution rights for downloaded engineering documents. Record source terms when
assembling a publication artifact.

## Publication checklist

Before publishing an implementation report, include the supported target/package/clock scope,
partial connectivity coverage, review status, input/tool/bundle revisions, reproducible commands,
actual outcomes and skipped checks. Label proposed features and unperformed experiments explicitly.
Use the [sequence diagrams](sequences.md) as explanatory figures, not as captured traces.

Before describing an overall v1 release as qualified, satisfy the existing release checks,
and record independent review. The sandbox is now provisioned and exercised, with optional
F407 full linking and ELF checks recorded in [build evidence](build-service-evidence.json).
Read-only MCU diagnostics and the corrected application's clock regression are separately
recorded in [inspection evidence](hardware-inspection-evidence.json); they do not establish
physical LED behavior or that the corrected artifact is running.
The [programming evidence](hardware-programming-evidence.json) separates fake-backend/Tcl/protocol
tests from real read-only planning. No successful physical programming or execution-control
experiment is implied by those wrapper checks.
Physical claims additionally
need a confirmed PCB revision and documented hardware measurements. Avoid claims of universal
board onboarding, automatic PDF schematic understanding, complete firmware asset delivery, or
proven model correctness with the current implementation.
