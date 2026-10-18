# Changelog

## Unreleased — experimental alpha

First public release candidate, centered on STM32F407VGT6 / Cortex-M4 and the
STM32F407G-DISC1 MB997-E-01 reference bundle. No public release or image upload is implied.

### Included

- Bounded transient retries for exact source restoration, longer HTTP read waits,
  single-job manufacturer-source acquisition and hash-verified shared CI caching.
  Historical extraction uses a manifest-pinned Python runtime in a separate offline
  environment, preserving exact PDF geometry hashes across application test versions.
  Python matrix tests and all original integrity/review checks remain required;
  persistent failures and source changes remain blockers.

- Optional requested-project reporting over CLI and build MCP: standalone HTML,
  Markdown, white formal styling, complete scoped net connectivity SVG, schema-validated
  authored sequence diagrams, design explanations,
  source attachments and revalidated build evidence. A recordable F407 UART protocol
  supervisor scenario demonstrates the flow; physical acceptance and attachment-to-build
  source binding remain explicitly unassessed.

- Multi-part LaTeX authoring kit, native CircuitikZ electrical reference sheets and
  controlled LuaLaTeX PDF typesetting. Electrical symbols require published component
  kinds, terminal roles and exact nets; unknown internals remain terminal blocks. Document
  status uses plain engineering control text rather than colored warning banners.

- Source-bound TIM5 CH3 capture interrupt/TIM2 CH2 PWM workflow, fixed vector and
  priority checks, independent NVIC delivery/failure model and seventeenth isolated
  application. Separate timer IRQ software telemetry and offline qualification reject
  missed delivery as a no-edge timeout and failed source/line/pending/active cleanup
  as quiet. Historical polling bundles and evidence remain unchanged; new physical
  IRQ qualification, DMA and independent release sign-off remain pending.

- Artifact-bound physical polling PWM/capture trial: one approved flash, successful
  wired capture, clean no-edge timeout after unpowered jumper removal, and recovery
  after restoration. Raw-value qualifiers preserve failures; no calibration, formal
  repeatability, interrupt/DMA or full MCU acceptance claim.

- Fixed timer-route telemetry ABI, coherent terminal publisher, exact-image read-only MCP
  observation and raw-timestamp offline qualification. Shared application/effect-model
  failure checks and a sixteenth isolated firmware case; no new physical qualification.

- Generic per-mode instance scopes with exact validation and transparent readiness
  reporting. New source-backed F407 PA1/TIM2_CH2 PWM and PA2/TIM5_CH3 capture contracts,
  separate fixed board nets, independent dual-timer failure models and one paired
  isolated application. Physical qualification and independent sign-off remain open.

- Source-backed TIM2 internal PWM reference and software-capture modes, owned RCC
  gate/reset dependencies, explicit blocked external routes, independent timer effect
  models and two isolated MCP-built examples. No new runtime/compiler branch or physical
  qualification; existing modes and application acceptance cases are retained.

- Generic, data-configured alternate register field views with explicit operating-mode
  selection, header/provenance checks, complete tables and view-aware manual candidates.
  A new immutable F407 bundle preserves input/output and mixed timer channel directions;
  PWM/capture operating contracts and physical qualification remain pending.

- Source-bound editorial inventory repairs, complete PDF layout evidence through MCP, and
  F407 applicability/package reconciliation. Original scope records and extraction gaps remain
  reproducible; repairs do not approve modes or reduce the section inventory.

- Generic source-outline preparation through ingestion MCP, explicit table-index columns,
  source-pinned manufacturer inventory schema and CLI, and applicability/workflow reconciliation.
- F407 source scope across RM0090, DS8626, PM0214 and ES0182, preserving incomplete headings,
  mixed-family applicability and missing mode/board/boot evidence. No new operating-mode support
  or physical qualification is implied by indexing those documents.

- F407 full-scope acceptance audit and data-defined MCP replay of all twelve existing applications
  against one immutable candidate; generic scalar-union views close ITM declaration extraction.
- Preserved operating/topology/qualification gaps and the first CAN RX source-layout failure;
  corrected example layout without weakening the C/header-only sandbox contract.

- Complete Markdown publication/retrieval without the former 64 KiB ceiling, retaining full
  tables, source provenance and validation. Size does not prune selected peripherals.
- KiCad 10 XML pin-name compatibility backed by same-endpoint library evidence; all four
  native export/compilation checks pass. Strict acceptance rejects skipped required checks.

- Declarative, hash-pinned publication contracts replacing target-specific compiler register,
  clock, array-view and routing policy; all existing source profiles migrated.
- Complete linked provenance registries when the source catalog exceeds one document.

- Experimental STM32F1/G0/H7 MCU-only bundles, hash-pinned inputs and offline target-matrix
  compilation; full register/field tables and honest missing-board/operating coverage.
- Lossless large-document meaning normalization and registered coverage JSON companions.
- Deterministic offline compilation into validated, source-backed Markdown bundles.
- Vectorless, read-only MCP retrieval with exact topology lookup, target isolation and
  prerequisite-document gates.
- A Docker knowledge runtime, OpenCode / Claude Desktop configurations, and real stdio checks.
- Reviewed F407 operating subsets, Cortex-M4 core contracts and scoped coverage reporting.
- Optional Linux/Podman compilation, pinned firmware assets and ELF validation.
- Opt-in ST-LINK programming/control and artifact-bound telemetry for supported examples.
- Contribution guides, examples, evidence reports and publication checks.

### Validation and boundaries

Latest F407 audit: 970 tests passed, zero skips; all twelve existing applications linked
and ELF-revalidated against one candidate through81 actual MCP calls. The rebuilt Docker
runtime passed161 calls across four sessions. Earlier complete-document evidence also passed
326 Docker calls across eight sessions, including a10,156,004-byte response. No physical
operation occurred in these audit passes. Full MCU acceptance remains open.

The declarative compiler continuation passed 922 tests with four native KiCad skips,
219 direct MCP calls and 313 Docker MCP calls across seven sessions. Nineteen source profiles
now use pinned policy; repeated F103/G071/H743/F407 publication is byte-identical. This adds
compiler flexibility, with no new operating semantics or physical qualification.

The earlier multi-family continuation passed 903 software tests with four native KiCad skips,
168 direct MCP calls and 252 Docker MCP calls across five sessions. New STM32 target inventories
remain declarations-only; no new board programming or physical qualification is claimed.

Earlier recorded evidence includes 861 passing software tests with four native KiCad skips, plus
110 Docker MCP calls across three sessions and 50 passing native routing/protocol checks.
Earlier physical LED/button, UART and scoped CAN demonstrations have separate evidence;
the latest ARM-core example is unflashed.

This is not complete STM32/ARM support or qualified production firmware tooling. Docker
verification currently covers Linux amd64 knowledge retrieval. Independent review, clean
hosted-CI evidence, broader operating modes and hardware qualification remain open.

See [experimental scope](docs/experimental-release.md), [status](docs/STATUS.md),
[Docker evidence](docs/docker-evidence.json) and [launch preparation](docs/alpha-launch.md).
