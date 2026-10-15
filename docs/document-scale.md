# Complete documents and required-check acceptance

Praxis no longer imposes a fixed 64 KiB Markdown publication or retrieval ceiling. This is a
change to the compiler, bundle loader and reporting path. Large projects retain canonical
peripheral documents with complete register tables, bit fields, operating narratives and
provenance. Documents are neither truncated nor rejected solely because they exceed 64 KiB.

## What changed

- `read_inside` reads complete knowledge files by default; explicit limits remain available
  to callers handling bounded nonknowledge inputs.
- Compiler discovery no longer removes selected peripherals or their dependants because of
  document size. Unknown semantics and unsupported declarations remain explicit coverage gaps.
- Reviewed Markdown sources are exempt from the generic 8 MiB raw-input bound, including the
  ingestion/review services' source-registration and stability checks.
- Peripheral rows retain their complete field meanings. New coverage/feature reports and
  provenance catalogs remain together in their canonical Markdown files.
- Coverage reports use `bytes_limit: null` to describe the absence of a publication ceiling.
- Bundle manifests and all published documents are read completely before integrity checks.
  Paths, aliases, UTF-8, hashes, cross-links and dependency validation still apply.
- Historical bundles remain immutable. Old report companions and meaning dictionaries are
  readable with their original hashes; new compilation creates a new revision.

This does not make RAM or model context unlimited. The server snapshots the verified bundle
in memory, and a complete tool response can exceed an assistant's context budget. The client
must manage that budget explicitly; Praxis does not silently discard rows. Separate limits on
raw downloads, authoring packets, compilation diagnostics, process resources and hardware
operations still belong to those operations. Flash geometry and telemetry bounds are unrelated
to knowledge document size.

## Native KiCad acceptance

The installed KiCad CLI reports **10.0.7**. Running the four previously skipped native tests
exposed a difference between library pin names and endpoint-qualified XML `pinfunction` values.
The parser now accepts either the exact library name or that name qualified by the **same
physical endpoint number**, when the matching library record supplies the evidence. It never
strips an arbitrary suffix or uses the target profile to guess the original name.

The behavior follows KiCad's [XML exporter implementation](https://docs.kicad.org/doxygen/netlist__exporter__xml_8cpp_source.html).
Negative tests reject wrong endpoint numbers, different signal names, repeated suffixes,
ambiguous names and qualified values without library evidence. Conflicting MCU/package/pin
facts still fail. Both AVR and STM32 fixture schematics now pass real export, endpoint
comparison and native bundle compilation.

## Required dependencies and zero-skip checks

For work in this repository, use:

```bash
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q
```

Missing native tools, sandbox images or required Python modules fail strict acceptance.
An unexpected skipped check also makes the strict session fail. The negative policy test
intentionally constructs a skipped subprocess test and verifies that its acceptance exits
with failure; that is a tested failure case, not a skipped check in the real suite.

If a dependency required for a task is missing, stop the dependent acceptance work, report the
exact dependency and wait for installation. Do not substitute a skip or describe incomplete
verification as a pass. [AGENTS.md](../AGENTS.md) records this working rule.

## Verification

The large-document fixture compiles a registered UTF-8 Markdown source exceeding 8 MiB into a
**10,156,004-byte USART document**. A real stdio MCP client compares the complete response
against the compiled document. Tail corruption, invalid UTF-8 and unresolved links beyond
the former ceiling are detected. Source-catalog and coverage tests also preserve large tables
and full JSON without companions. Explicit nonknowledge input limits have separate tests.

Reproduce the focused checks:

```bash
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q \
  tests/test_large_documents.py tests/test_kicad_pin_names.py \
  tests/test_compiler_adapters.py tests/test_report_companions.py \
  tests/test_source_catalog.py tests/test_dependency_policy.py
```

Current local build and protocol outputs are under `.praxis-output/document-scale/`.
Use a newly compiled path to get the new publication layout. Restarting a server against an
old bundle does not regenerate that bundle. Docker users must rebuild the image to use the
new loader; the separately tested local tag is `project-praxis:complete-documents`.

Final strict acceptance passed **942 tests with zero skips**. The rebuilt Docker knowledge
runtime passed 326 calls across eight sessions, including the complete 10,156,004-byte response.
Repeated F103/G071/H743, F407 and large-AVR compilations are byte-identical.
See [recorded evidence](document-scale-evidence.json) for exact results. The documentation
website is an independent repository and was not automatically synchronized.
