# Milestone evidence and release status

Timer capture IRQ increment, 2026-10-15: **1,462 full-suite tests passed, zero skipped**,
with required external tools. The new [source-bound IRQ workflow](timer-irq.md) adds
TIM5 CH3 IRQ50 capture paired with TIM2 CH2 PWM, a fixed 180-byte software ABI,
independent exception delivery/failure models and raw period/receipt/cleanup qualification.
Coverage is **43 mode contracts and 24/39 ready authored workflows**, not all-MCU coverage.
Two ingestion MCP publications and a CLI publication match byte-for-byte. All 17
applications build/revalidate through 94 actual MCP calls; native retrieval passes 52
calls and rebuilt Docker passes 162 calls plus seven explicitly synthetic qualifier cases.
Packaging, public-link checks, pinned inputs, Ruff and the offline lock check pass.
The 5,984-byte artifact 70aab2ee7184… is not flashed. Read-only preflight cannot currently
see the selected ST-LINK; reconnect/wiring confirmation is pending. New physical IRQ
qualification, DMA, broader F407 modes and independent release review remain open.
See [exact software evidence](timer-irq-evidence.json). Next: reconnect the selected
probe, obtain fresh exact-image approval, and test IRQ success/no-edge/recovery through MCP.

Physical paired-timer trial, 2026-10-15: **wired success, clean no-edge timeout and
wired recovery all passed** for telemetry artifact `ba3ff2fcb1e2…`, with user-confirmed
unpowered PA1/P1-11 ↔ PA2/P1-14 wiring changes. One approved MCP flash verified all
4,424 bytes after sector 0 erase; one MCP reset/run followed. Later phases used user
power cycles and read-only MCP. Six windows/18 samples preserve the timeout latch;
success qualification correctly rejects the removed-jumper observations. Both positive
boots report eight periods of 1,000 local ticks and quiet shutdown. There were 25 MCP
calls total, two mutating. No independent frequency/duty measurement, formal repeatability,
physical PCB revision confirmation, timer IRQ/DMA or full MCU acceptance is implied.
See [actual results](reports/timer-route-results.md) and [sanitized evidence](timer-route-physical-evidence.json).
Next: timer capture interrupt contracts, failure models and isolated builds, then DMA.

Timer observation increment, 2026-10-15: **1,270 full-suite tests passed, zero skipped**,
with required external tools; **155 affected checks** also passed, including a stricter
raw-prefix check and two later-added regression cases. Totals overlap. The fixed
[timer telemetry ABI and offline qualifier](timer-observations.md) use the unchanged
immutable timer-routes-v1 knowledge bundle. Counts remain 39 contracts and 23/38 ready
authored workflows: this strengthens Milestone 4 without claiming new MCU modes. All 16
applications build/revalidate through 92 actual MCP calls. Native knowledge retrieval
passes 52 calls; rebuilt Docker passes 162 calls in four sessions and five clearly
synthetic qualification outcomes. Packaging/lock checks pass. Telemetry artifact
ba3ff2fcb1e2… is 4,424 bytes and has not been flashed. No physical probe/target operation
occurred; exact-bundle/asset independent review and wired physical qualification
remain open. Next: fresh wiring confirmation, exact-image approval and artifact-bound
success/no-edge/recovery observations, then timer IRQ/DMA support.

Routed timer increment, 2026-10-14: **1,165 full-suite tests passed, zero skipped**, with
required external tools. A 51-test focused run additionally checks six later-added
bundle/source validations; these overlapping totals are not added. The new immutable
[timer-routes-v1 bundle](timer-routes.md) adds exact PA1/TIM2_CH2 PWM and PA2/TIM5_CH3
rising capture, supported by generic per-mode instance scopes. Counts: **22 reviewed
subsets, 39 contracts, 23/38 ready authored workflows**. Two ingestion MCP publications
and a CLI publication are byte-identical. All 15 examples build/revalidate in 90 actual
MCP calls; rebuilt Docker passes 162 calls in four sessions. Source review used 72
actual ingestion MCP calls. Packaging and offline lock checks pass. No flash, probe,
reset, physical route test or independent sign-off occurred. Next: artifact-bound
wired route qualification, then timer IRQ/DMA contracts and the remaining F407 gaps.

This repository is an implemented development baseline. **The v1 release gate is not yet met.**

F407 timer operating continuation, 2026-10-14: **1,120 tests passed, zero skipped**, with
required external tools. Source-profile data adds owned TIM2 RCC gate/reset, internal PWM1
reference and stopped-counter software-capture contracts; core compiler/runtime code is unchanged.
Two ingestion MCP publications and an independent CLI compilation are byte-identical.
All fourteen application cases build and ELF-revalidate through86 MCP calls; a5-call focused
replay checks new mode rows and blocked external workflows. The existing Docker image passes
161 calls across four sessions without rebuilding. Instrumented effect tests cover preload
transfer, full-word/read-to-clear capture, stale and racing overcapture, wrong ownership/clock,
configuration failure and unsuccessful cleanup. Reviewed coverage is **22 subsets,35 mode
contracts and22/37 ready authored workflows**; external pin PWM/capture remains blocked.
No flash, reset, probe access or physical acceptance occurred. See [contracts and sequence](timer-modes.md)
and [exact evidence](timer-modes-evidence.json). Next: package/AF/board routes and shared-pin
ownership for external PWM and capture, then separate routed-mode and physical qualification.

F407 register interpretation continuation, 2026-10-14: **1,052 tests passed, zero skipped**,
with external tools required. Generic, profile-configured field views now preserve timer
input/output interpretations and mixed channel directions without manufacturer branches.
The new immutable timer-views-v1 bundle publishes eight complete view tables (64 rows,
28 distinct name/mask pairs) and restores eight input filter/prescaler declarations.
Repeated compilation produces 50 byte-identical files. Actual ingestion MCP yields 32
position/offset/reset candidates with no conflicts; access/reset review remains open.
Native stdio passes 52 complete-document calls, all 12 existing applications link/revalidate
in 81 MCP calls, and rebuilt Docker passes 161 calls across four sessions. An earlier
regression overlapped a source-profile edit and correctly failed `SOURCE_CHANGED`; the
final run used frozen inputs. Reviewed support remains **22 subsets, 32 modes and 20/33
ready workflows**. No hardware operation or new PWM/capture operating qualification occurred.
See [schema, algorithms and sequence](register-field-views.md) and
[exact evidence](register-field-views-evidence.json). Next: source-backed, instance-scoped
TIM2 PWM/capture contracts, instrumented failure models and isolated MCP example builds.

F407 source reconciliation, 2026-10-14: **1,022 tests passed, zero skipped**, external tools required.
A second immutable-input inventory revision resolves all 29
recorded layout items through explicit source-bound editorial records, retaining original entries,
gaps and provenance. Pending/mixed applicability falls from 741 to 299 across the same 1,683 records.
Five RM controller chapters are excluded using explicit non-F407 body restrictions; 24 scope facts
include exact-part ordering, resource counts and the LQFP100 FSMC Bank1/Bank2 constraints.
The generic ingestion MCP adds complete page-layout evidence. All 12 examples link/revalidate
in 81 actual MCP calls; the rebuilt Docker runtime passes 161 calls across four sessions. No new operating mode, physical
qualification, bundle replacement or hardware action is implied. See
[source review, algorithms and next work](inventory-reconciliation.md) and
[evidence](inventory-reconciliation-evidence.json). Next: timer PWM/capture instance/mode
requirements, remaining applicability and silicon-revision review, and source-backed package gates.

Manufacturer inventory continuation, 2026-10-14: the generic source-outline MCP adapter now
supports dotted contents and explicitly labelled table indices. **1,005 tests passed, zero skipped**,
with required external tools enabled. Four source-pinned documents
yield 1,683 indexed records, retaining 29 extraction items and 741 pending/mixed applicability
sections. The cached RM index's missing tail is now extracted; incomplete headings remain
visible. Target scope and mappings live in JSON. `praxis inventory` validates provenance and
reconciles related workflows without declaring whole-section support. The acceptance MCP client
includes these gaps and still links/revalidates all 12 applications in 81 calls. Four repeated
outline preparations are identical. The rebuilt Docker runtime passes 161 calls across four
sessions; its inventory CLI works without ingestion extras and rejects incomplete acceptance.
No hardware
operation occurred. Full source/body-mode reconciliation, topology, physical qualification and
independent review remain open. See [algorithms, source scope and reproduction](manufacturer-inventory.md)
and [evidence](manufacturer-inventory-evidence.json). Next: reconcile exact-part availability
and repair extraction gaps, then author complete instance/mode requirements for F407.

Full F407 acceptance audit, 2026-10-14: **970 passed, zero skipped**, external dependencies
required. Generic scalar-union extraction closes the ITM declaration blocker without inferring
operating semantics. Two ingestion-MCP publications produce51 byte-identical files. The candidate
publishes42/42 recognized blocks,541 register rows and2,144 field records; operating coverage
remains22 reviewed subsets and20/33 ready authored workflows. The combined real MCP replay
links/revalidates all12 existing F407 applications in81 calls. Its initial CAN RX README rejection
is preserved; moving documentation outside C/header inputs fixes the layout without relaxing
sandbox policy. The rebuilt Docker image passes161 calls across four sessions. No board writes,
reset or new physical qualification occurred. See [the full scope and closure sequence](f407-full-acceptance.md)
and [machine-readable evidence](f407-full-acceptance-evidence.json). Full F407 coverage now takes
priority over further family expansion. Next: reconcile the manufacturer-wide feature inventory,
classify unmapped declarations and close missing timer/boot/storage operating contracts.


Complete-document/native-KiCad continuation, 2026-10-14: **942 tests passed, zero skipped**
with strict required-dependency acceptance. Installed KiCad 10.0.7 now passes all four native
AVR/STM32 export and compilation checks. The parser recognizes endpoint-qualified names
only with exact same-pin library evidence; seven positive/negative cases preserve conflict
rejection. Published Markdown has no fixed byte ceiling. Size no longer prunes selected
peripherals or their dependencies; full field meanings, source catalogs and coverage JSON
remain intact. A 10,156,004-byte UTF-8 USART document passes exact native and Docker MCP
response checks, with corruption/encoding/link failures detected at its tail. The rebuilt
knowledge image passed 326 calls across eight sessions, including old and new bundles.
Historical revisions and physical firmware remain unchanged. Required task checks cannot
pass with skips; missing dependencies must be installed before acceptance continues.
See [behavior and reproduction](document-scale.md) and [evidence](document-scale-evidence.json).
Earlier proposed next step (superseded by the F407 priority above): review bounded F103/G071 clock/GPIO/UART workflows through data contracts, then qualify
compile-only firmware profiles separately. Independent review and broader physical qualification
remain release requirements.


Declarative compiler continuation, 2026-10-14: **922 tests passed, four native KiCad checks
skipped**. All 19 source profiles now require registered, hash-pinned publication contracts.
F407 minimum-register and clock policy, named array views and routing names have moved out
of compiler branches into reviewed input data. Format-specific header checks live in adapters;
historical target qualification and manifest-v1 routes use a versioned compatibility catalog.
A synthetic test changes entity names, array names and dependencies through data alone.
Missing reviewed registers, changed contract bytes and conflicting extraction identities still
block publication. Large source catalogs preserve complete tables in linked provenance documents.
Fresh F103/G071/H743 and F407 publications are byte-identical across repeated builds. Actual
stdio passed 219 calls; the rebuilt Docker image passed 313 calls across seven isolated sessions,
including historical F407/AVR revisions. Existing bundle paths and physical firmware are unchanged.
Distribution checks also verify all 19 contract files ship with their declared hashes.
This is compiler generalization, not new operating-feature coverage. See [algorithms, sequence
diagrams and migration](compiler-contracts.md) and [exact evidence](compiler-contracts-evidence.json).
Next: review bounded F103/G071 clock/GPIO/UART workflows using data contracts, then qualify
compile-only firmware profiles separately. Complete MCU support and the qualified-v1 gate remain open.

STM32 family expansion, 2026-10-14: **903 tests passed, four native KiCad checks skipped**;
Ruff, the dependency lock and source distribution checks passed. Real source-backed MCU-only
bundles now cover STM32F103C8T6 (30 published blocks), STM32G071RBT6 (35) and STM32H743ZIT6 (76).
Together they publish 1,667 register rows and 6,149 primitive field definitions. Three repeated
compilations are byte-identical to the shipped inventory-v2 revisions. Exact compound-mask
partitioning restores G0/H7 USART CR1 fields while preserving source identities and missing
operating semantics. Lossless meaning dictionaries preserve full H7 RCC/Ethernet tables;
registered JSON companions keep large coverage reports within 64 KiB. Real stdio passed 168
calls; a separately tagged Docker runtime passed 252 calls across five isolated sessions,
including the existing F407 bundle. MCU-only scope permits unknown active clocks and absent
schematics without weakening board requirements or granting F407 firmware/flash support.
All three new target inventories have zero reviewed operating subsets and blocked authored
GPIO/UART/timer workflows. No physical board operation occurred. See [architecture, sequence
and contributor workflow](stm32-family-expansion.md) and [exact evidence](stm32-family-expansion-evidence.json).
Next: review bounded clock/GPIO/UART workflows for F103/G071, then add independently scoped
compile-only firmware profiles. Complete MCU support and the qualified-v1 gate remain open.

Docker knowledge runtime, 2026-10-13: a multi-stage image installs the locked runtime package
on digest-pinned Python/uv bases. Its build context excludes working files and raw imports;
one operator-selected bundle is mounted read-only. Actual Docker stdio testing passed **110
tool calls across three fresh sessions**, comparing complete documents for the current F407
bundle and illustrative AVR fixture. Missing/corrupt bundles fail before tool service; runtime
checks confirm non-root execution, unwritable application/bundle paths and absent optional
ingestion/test extras. OpenCode/Claude Desktop examples and a CI image-check job are included.
This packages retrieval only: the existing compiler, Linux/Podman build and USB/probe services
retain separate provisioning. Local evidence is Linux amd64; no registry upload, hosted CI
run, cross-architecture qualification or hardware action occurred. See [Docker onboarding](docker.md)
and [protocol evidence](docker-evidence.json). Next: verify a clean public checkout and prepare
the experimental registry release; qualified-v1 blockers below remain unchanged.

STM32/ARM experimental continuation, 2026-10-13: **861 tests passed, four native KiCad
checks skipped**; Ruff and the dependency lock check passed. New scoped HSI16, SysTick and SCB
contracts raise coverage to22 reviewed subsets,32 mode contracts and20 ready authored workflows
out of33. Ten actual knowledge/build MCP calls passed dependency/LED retrieval, pinned rootless
ARM linking and artifact revalidation. The1,736-byte image has a strong SysTick slot15 handler
and correct0x20020000 main-SRAM stack; it is unflashed and physically untested. Repeated MCP
publication produced49 byte-identical files. PM0214 text/diagram review preserves conflicting
reset/calibration facts and stricter F407 vector-write constraints. The initial local polling
revision is superseded by PRAXIS-2026-002; its files remain unchanged. New optional reviewed
write-value masks require semantic provenance, and new STM32 parts can register explicit
knowledge adapters without inheriting F407 firmware support. The first experimental release
now prioritizes STM32F407/Cortex-M4; non-ST expansion is deferred. See [ARM contracts and
sequence](arm-core-support.md), [evidence](arm-core-evidence.json), [example](../examples/stm32f407g-disc1-arm-core/README.md)
and [experimental release scope](experimental-release.md). Next: partition the nearly full
provenance catalog losslessly, then add timer PWM/capture and SPI routing. Native KiCad and
independent review remain qualified-v1 blockers; complete STM32/ARM support is not claimed.

Reusable target adapter continuation, 2026-10-12: **802 full-suite tests passed, four native
KiCad checks skipped**; one subsequently added topology-only evaluation test passed separately,
and Ruff passed. Explicit Cortex-M knowledge adapters now configure CPU/header identity and
mask/position conventions; Clang source locations replace vendor/core naming guesses. A clearly
fictional Cortex-M3 bundle publishes four declarations-only blocks with its own dependency graph.
Four actual ingestion-MCP calls and 14 knowledge-MCP calls passed; MCP and CLI publication
produced ten byte-identical files. Custom adapters cannot override builtin target identities or
inherit F407 firmware/flash assets; the sandbox verifier rejects knowledge-only targets before
execution. Existing immutable bundle hashes remain readable. See [adapter architecture and
sequence](target-adapters.md) and [evidence](target-adapters-evidence.json). This adds reusable
extraction capacity, not a supported NXP board or additional reviewed F407 modes. Next: apply
the adapter to one exact real non-ST Cortex-M part using supplied manufacturer references,
review a bounded clock/GPIO/UART workflow, then add its compile-only profile. Independent
review and missing native KiCad remain qualified-v1 blockers.

CAN RX physical follow-up, 2026-10-12: the user-approved **4,920-byte**
image passed one actual MCP flash, exact readback and reset/run. Two five-sample
windows at requested 1000 ms spacing passed offline internal-loopback qualification:
correct payload, one receive interrupt, transmit completion, no saved errors,
cleanup and advancing software publication counters. Earlier 250 ms windows were
correctly rejected for repeated heartbeat counters and remain retained. Persistent
operation results match MCP responses; both approval budgets are consumed. No
extra flash/reset or firmware retry occurred. This is one internally looped
transaction observed through firmware self-report, not external CAN or repeatability
qualification. See [physical results and sequence](reports/can-rx-results.md) and
[sanitized evidence](can-rx-evidence.json). Next: expand the next blocked capability
through source-backed contracts and verification; any repeated physical start needs
a concrete approved execution plan. KiCad and independent reviews still block v1.

Initial CAN RX software follow-up, 2026-10-12: **772 tests passed, 4 KiCad checks skipped**;
155 focused checks and Ruff passed. Actual ingestion MCP source/image review
produced a new immutable RX-route bundle, reproduced as 49 byte-identical files.
Lossless source-path normalization keeps its largest Markdown document at 60,793
bytes. Coverage is 20 reviewed subsets, 26 mode contracts and 16 ready authored
workflows out of 29; complete MCU support remains unknown. An 18-call actual MCP
replay passed topology/dependency retrieval, pinned sandbox linking, ELF checks
and artifact revalidation. Five read-only hardware MCP calls inspected the selected
board, prepared the 4,920-byte candidate plan and rejected the older installed image
before candidate SRAM observation. **The candidate is unflashed; physical CAN success
remains unconfirmed.** No flash/reset occurred in this continuation. The prior failed
run is retained. See [source-to-test sequence](can-rx-followup.md) and
[sanitized evidence](can-rx-evidence.json). Next: confirm P2:34 is externally
unconnected, obtain fresh exact-image approval, then perform one MCP flash/reset-run
and qualify bounded raw observations. Independent review and missing KiCad still
block qualified v1 release.

CAN physical continuation, 2026-10-12: **734 tests passed, 4 skipped** in the
full regression; Ruff passed. Following explicit exact-image approval, actual
MCP programmed and verified all 4,524 bytes of the CAN telemetry image, then
reset/ran it once. Persistent audits match the returned operations; both attempt
budgets are consumed. **The CAN application test failed:** two windows containing
ten coherent samples reported stable `init_timeout`, zero CAN IRQs and no payload
receipt, while publication counters advanced. Offline success qualification
rejected both windows; expected-failure qualification accepted the fresh failure
report. A new fixed, image-bound `read_can_diagnostics` MCP tool reads only
clock-gated CAN1 MCR/MSR and init-acknowledged BTR, with bundle-layout validation.
Its live snapshot shows INRQ=0, INAK=1, RX low and the expected BTR. Root cause
is unconfirmed; RX synchronization is a hypothesis requiring source/board review.
No programming retry occurred and no revised image has been prepared. The board
remains running the terminal failure publisher. See [results and diagnosis](reports/can-loopback-results.md)
and [sanitized evidence](can-telemetry-evidence.json). Published MCU knowledge
coverage is unchanged and physical CAN success remains unqualified. Next:
establish the initialization-side RX prerequisite through MCP, extend the effect
model, then build a revised candidate before requesting fresh image approval.

CAN observation continuation, 2026-10-12: **721 tests passed, 4 skipped** in the
full regression; 125 focused telemetry/qualification checks and Ruff passed.
The [CAN observation extension](can-telemetry.md) adds an explicit fixed ABI to
the existing artifact-bound reader, a software publisher recording actual ISR
FIFO reads, and offline qualification that recomputes payload, interrupt,
completion/error, cleanup and freshness checks. UART remains the default ABI.
A sixteen-call actual knowledge/build MCP replay passed isolated compilation,
linking, IRQ-vector/ELF validation and artifact revalidation. Real stdio MCP with
a fixture probe exercised the CAN observation and qualification path; actual
OpenOCD Tcl with modeled memory exercised both ABIs' identity/image/seqlock
guards. Initial physical preflight found no matching ST-LINK. After the user
reconnected it, five actual MCP calls inspected the selected target, prepared
the 4,524-byte image/sector0 plan, and rejected the older installed image with
`READBACK_MISMATCH` before CAN SRAM observation. No flash or reset occurred.
Published MCU coverage remains 20 reviewed subsets, 24 mode contracts and
15 ready authored workflows out of 28. See [exact evidence](can-telemetry-evidence.json).
Next: obtain exact-image approval and observe the internal-loopback result
through MCP after the approved flash/reset-run.
Internal CAN loopback needs no extra wiring. Qualified v1 blockers remain KiCad
checks and independent bundle/asset review; physical CAN behavior is untested.

CAN continuation, 2026-10-12: **660 tests passed, 4 skipped** in the full
regression; Ruff passed. The [CAN extension](can-expansion.md) uses the generic
compiler to publish CAN1 silent internal-loopback and FIFO0 interrupt contracts.
The new bundle has 20 reviewed subsets, 24 mode contracts and 15 ready authored
workflows out of 28. Repeated ingestion MCP publication produced 49 byte-identical
files; the largest Markdown document is 62,364 bytes, below 64 KiB. An actual
sixteen-call knowledge/build MCP replay passed retrieval gates, matching revisions,
isolated ARM compilation/linking, ELF/vector checks and artifact revalidation.
Forty-six modeled cases check access rules, initialization, interrupt receipt,
payload validation, concurrent errors, finite waits and reset-required recovery.
The linked vector binds the real CAN1 RX0 handler. The one-shot firmware has not
been flashed or physically executed; external CAN and broad CAN workflows remain
blocked. See [exact evidence](can-expansion-evidence.json). Next: artifact-bound
CAN observation and qualification, then an explicitly approved physical internal-
loopback test requiring no CAN jumper. Missing KiCad and independent bundle/asset
review continue to block qualified v1; overall MCU completion remains unknown.

DAC continuation, 2026-10-12: **609 tests passed, 4 skipped** in the full
regression; Ruff passed. The [DAC extension](dac-expansion.md) uses the generic
compiler to add channel1 software-trigger digital completion and its RCC contract.
The bundle has 19 reviewed subsets, 20 mode contracts and 13 ready authored
workflows out of 25. Repeated ingestion MCP publication produced 49 byte-identical
files, with every Markdown document below 64 KiB. A thirteen-call real
knowledge/build MCP replay passed retrieval gates, matching revisions, isolated
ARM compilation/linking, ELF/vector checks and artifact revalidation. Thirty
modeled cases cover access restrictions, stale output, errors, ownership,
finite waits and reset-required recovery. The target-link test confirms that
the full integration entry remains in the ELF, while main leaves both analog
outputs disabled. Broad/wired DAC workflows remain blocked; no analog measurement
or board operation occurred. See [exact evidence](dac-expansion-evidence.json).
Missing KiCad and independent bundle/asset review continue to block qualified v1.

I²C continuation, 2026-10-11: **574 tests passed, 4 skipped** in the final full
regression; Ruff passed. The new [compiler expansion](i2c-expansion.md) publishes
an I2C1 seven-bit, 100 kHz polling transmitter contract. The bundle has 18 reviewed
subsets, 18 mode contracts and 12 ready authored workflows out of 23. Broader I²C
and wired-device workflows remain blocked. Reusable parent-state binding composes
successive RCC extensions, and lossless provenance normalization keeps every document
below 64 KiB. Repeated ingestion MCP publication produced 49 byte-identical files.
A ten-call real knowledge/build MCP replay passed target compilation, linking,
ELF/vector checks and artifact revalidation. Failure models cover flag-clearing,
ownership, NACK/arbitration loss, stuck commands, timeouts and reset-required retries.
No board operation occurred. See [exact evidence](i2c-expansion-evidence.json) for final
regression and artifact identities. Missing KiCad and independent bundle/asset reviews
continue to block qualified v1 release.

Podman restoration, 2026-10-11: **535 tests passed, 4 skipped** in the full available
regression; the remaining skips require KiCad. Rootless Podman6.1.3 now uses the exact
previously locked toolchain image in its default store, imported locally without downloads
or rebuilding. The unchanged ADC application passed a twelve-call actual knowledge/build
MCP replay: compilation, full linking, ELF/vector checks and artifact revalidation succeeded.
Artifact: `74a18d92fd2925ba52d343fc1c0d588b3a71afa2490a1c1d2ce28dd7b5e1c9d3`.
Live sandbox compilation/isolation checks previously skipped for Podman now passed.
No flash, reset, debugger attachment or other board operation occurred. Physical ADC behavior
remains untested. The release gate now reports missing KiCad and independent bundle/asset
reviews. See [successful build evidence](adc-build-evidence.json); the earlier missing-Podman
attempt below is retained as historical evidence.

ADC/workflow continuation, 2026-10-11: **529 tests passed, 10 skipped** in the full
available regression; Ruff passed. Four KiCad and six Podman checks could not run.
The [ADC expansion](adc-expansion.md) adds reusable hash-bound definition extensions,
dependency-driven workflow review packets, and an immutable ADC1 internal-reference/TIM2
polling bundle: 17 reviewed subsets, 16 mode contracts, 11 ready authored workflows out of21.
Actual ingestion MCP published it twice with byte-identical output; a nine-call knowledge
MCP replay passed. A separate matching knowledge/build replay correctly returned
`MISSING_TOOL` for absent Podman. The new application is host-modeled but **not target-compiled,
linked, ELF-validated or flashed**. No board operations occurred. Repeated synthetic test copies
initially filled `/tmp`; generated copies were cleaned and fixture copying now excludes private
imports. The clean complete rerun passed. See [recorded evidence](adc-expansion-evidence.json).
The generic compiler remains vectorless and contains no model calls; editorial review still
supplies operating semantics. Broader ADC/MCU support and independent release review remain open.

Support/contribution continuation, 2026-10-11: **490 tests passed, 9 skipped** in the complete
available regression; Ruff passed. Four live KiCad and five rootless Podman checks were skipped
because those executables are unavailable in this environment. The earlier 472-test zero-skip
qualification below is historical evidence, not a claim that it was reproduced here. Twenty-seven
new checks exercise deterministic read-only support assessment, exact target binding, catalog
validation, inconsistent coverage rejection and fail-closed workflow selection. `praxis support`
reports measured denominators and leaves overall MCU completion unknown. Its initial authored
catalog has 26 goals, including six planned boot/update/power goals; this is not an exhaustive
silicon inventory. A real 17-call knowledge MCP replay passed, and an installed wheel's new CLI
worked from an unrelated directory. Wheel/source contents and public links passed. Contributor
instructions, PR/issue templates and CI support preflight are included. **No reviewed operating
coverage, bundle revision or physical qualification changed; no board operation occurred.**
The release gate still fails: current tools are incomplete and independent bundle/asset reviews
are missing. See [support assessment and sequence](capability-support.md),
[contribution guide](../CONTRIBUTING.md) and [sanitized evidence](capability-support-evidence.json).

Clock-mode continuation, 2026-10-11: **472 full-suite tests passed with zero skips**, external
tools required; Ruff passed. The new immutable clock-v1 bundle has 15 reviewed subsets and
12 instance-scoped mode contracts. Exact F407 FLASH latency and PWR Scale 1 evidence resolves
the shared-manual variant conflicts within the selected scope. A reusable mode DAG expands
transitive registers, instances and document dependencies; missing references, incompatible
instances and cycles fail validation. An actual 20-call knowledge/build MCP replay passed
routing, clock/RNG publication gates, matching revisions, sandbox ARM linking and ELF validation.
Repeated ingestion MCP publication produced byte-identical files. A shared register callback
passed 27 focused model/routing checks, including failures at all 24 startup stages. The example
is compile-only: **no board operation occurred**, and installed UART firmware is unchanged.
FLASH programming, low-power transitions, unreviewed MCU modes, independent review and physical
clock qualification remain open. See [clock contracts and sequence diagrams](clock-modes.md),
[the example](../examples/stm32f407g-disc1-clock/README.md) and [sanitized evidence](clock-mode-evidence.json).

Compiler authoring extension, 2026-10-11: **438 full-suite tests passed with zero skips**,
external tools required; Ruff passed. A new shared offline review adapter is exposed through
`praxis prepare-review` and the ingestion MCP's tenth tool, `prepare_peripheral_review`.
An actual 15-call local MCP replay prepared 319 unreviewed candidates across ten F407 peripheral
groups, retained four conflict groups and rejected invalid register/part selections. Repeated
MCP requests and two CLI runs produced identical CRC packets. Configurable literal vocabulary,
exact register symbols, complete part selection, source hashes and explicit gaps support broader
ingestion without model calls. These packets are always pending review and cannot be substituted
for reviewed peripheral records. **Published MCU coverage is unchanged**; no bundle publication,
flash or other board operation occurred. See [the workflow and sequence diagrams](manual-review-compiler.md)
and [sanitized evidence](manual-review-evidence.json). FLASH/PWR and other new operating modes
still require target-specific review and verification before support can be claimed.

Mode/verification expansion, 2026-10-11: **413 full-suite tests passed with zero skips**, with
external tools required; Ruff passed. The actual ingestion MCP published and deterministically
recompiled a new feature bundle with 13 reviewed peripheral subsets, 41 published register
blocks and seven explicit operating-mode contracts. CRC/DMA/SPI/RNG/IWDG guidance is source-backed;
SPI board wiring and complete RNG clock setup remain blocked. Forty-two blocks are recognized,
but 35 have no explicit mode contract. **All MCU features are not yet supported.** A 17-call
real knowledge/build MCP replay passed, including pinned-sandbox compilation/full linking and
ELF revalidation of a new CRC/DMA compile-only example. No new hardware operation occurred.
Offline qualification now recomputes the eight earlier UART windows from ABI words and retains
failed/mixed windows; repeatability remains unqualified. See
[mode contracts, sequence diagrams and commands](peripheral-modes.md),
[sanitized evidence](feature-expansion-evidence.json), and
[the example](../examples/stm32f407g-disc1-crc-dma/README.md). Existing immutable bundles,
OpenCode selection and installed UART firmware are unchanged.

Milestone 4 qualification continuation, 2026-10-11: the installed revised telemetry image passed
an actual MCP jumper-removed failure observation. All five coherent samples reported `failed` /
`uart_error`, zero validated frames and blue success off; timer progress continued (+4,250 ticks).
UART error/received-byte counts each increased by 134. Exact image checks passed before/after
sampling. Restored loopback subsequently passed two stable windows (+42/+43 frames, no UART/queue
errors, blue success on), and the repeated final pause passed with timer progress and no frame
progress. **Repeatability remains unqualified:** the first recovery run timed out after 75 frames,
and the first intended pause instead showed a new running session. Both anomalies are preserved.
No new flash or execution-control command was issued; the user performed power cycles and the
wiring/button stimulus. Eight telemetry windows captured 40 coherent samples. See the
[results report](reports/telemetry-failure-recovery-results.md) and
[qualification evidence](telemetry-qualification-evidence.json). This supersedes the earlier
paused board-state description below: the application is now paused in run 3 with 804 validated
frames and the jumper reported fitted.

Latest extension, 2026-10-11: **369 tests passed with zero skips**, external tools required;
Ruff and public wheel/source packaging checks passed. Public documentation file links now resolve
without private `temp/` material, and the source archive includes the sandbox recipe and CI.
A separately installed wheel served an exported bundle through actual stdio MCP from `/tmp`,
using preinstalled dependencies. Hosted CI and empty-cache dependency installation are unverified.

The optional [firmware telemetry tool](firmware-telemetry.md) is now physically demonstrated through
MCP on the connected board. Both explicitly approved 3,060-byte candidates passed exact-readback
flash/reset-run; their one-shot budgets are consumed. The first 20 ms publisher was correctly
rejected as too fast for consistent live reads. The revised 250 ms publisher passed boot-paused,
two running windows and a second USER-press pause check. Running windows gained 40/43 validated
frames and 760/817 TX/RX bytes; paused windows gained zero frames while timer counters advanced.
No UART/queue errors were reported. Final run count was 509 validated frames, with two reported
button presses. Exact image checks bracketed accepted samples; an actual wrong-image guard test
also passed after the read-strategy correction. These are firmware self-reports, not independent
wire capture or measured timing. The board is left paused. See [public evidence](telemetry-evidence.json)
and [publication readiness](PUBLICATION_READINESS.md). Qualified v1 still requires independent
review and the documented hardware/reproduction qualification; general autonomous debugging is incomplete.

Latest physical confirmation, 2026-10-11: the user reports the UART loopback and pause checks
work on the connected board with the jumper fitted: green continues blinking, orange pulses,
blue latches on and red remains off; another USER press stops orange activity while green
continues and blue stays on. This is human observation for the exact programmed UART artifact,
not independently captured packets or measured timing. The user subsequently reports that
jumper-removed failure and restored-jumper recovery also work as described. Held-button behavior,
precise timing and repetition count remain unverified. See the
[updated report](reports/uart-loopback-results.md) and
[observation evidence](uart-loopback-evidence.json).

Latest ingestion/UART extension, 2026-10-10: an optional nine-tool
[ingestion MCP](ingestion-mcp.md) now exposes cataloged acquisition, offline full evidence/table
and PDF-image retrieval, declaration discovery, explicit editorial review receipts and immutable
publication. Actual MCP calls supplied the missing USART2 connector/TIM2/SYSCFG/EXTI evidence;
the new `stm32f407g-disc1-e01-uart-v1` bundle passed 23 matching knowledge/build readiness calls.
Repeated MCP publication produced byte-identical output. Seven host UART/control tests and a
**316-test full regression with zero skips** passed; a subsequent targeted run passed
14 checks, including two new PDF-preview/symlink cases. The UART application then passed actual isolated full linking and ELF/vector
checks. Wheel/source-distribution builds also passed with private/raw paths excluded.
Read-only probe inspection/plan selected a 2,568-byte image and sector0 erase (16 KiB).
**Following explicit approval, the UART image was flashed once through MCP: all 2,568 bytes
matched readback, flash reported halted, and one reset/run reported running.** Both scoped
attempt budgets are consumed and persistent audits match the responses. Physical UART/LED
behavior was subsequently confirmed by the user on 2026-10-11 for positive run/pause and failure/recovery checks. Physical PCB revision and independent review
remain unconfirmed. See [actual results](reports/uart-loopback-results.md) and
[public evidence](uart-loopback-evidence.json). Existing default launchers retain their prior bundle.

Earlier UART/timer/EXTI scenario readiness check, 2026-10-10: a direct local MCP replay made
**44 tool calls** (21 configured knowledge, one configured build-profile, 22 separate discovery
knowledge calls). The configured bundle has no TIM2/EXTI/SYSCFG documents. Both bundles return
no match for PA2, PA3, USART2_TX/RX and P1:14/13. The discovery bundle returns timer/EXTI/SYSCFG
declarations with operating semantics explicitly unreviewed. The index gate and prerequisite
routing responded as expected, but **scenario readiness failed**. No code generation, build,
probe attachment, programming or execution control was requested. The user reports fitting the
loopback jumper; this does not add connectivity evidence to the bundle. This replay used only
MCP responses for hardware facts, after aborting and undoing preparatory parser changes from
the same turn at the user's request. Existing source profiles and bundles remain unchanged.
See [the readiness report](reports/uart-readiness-before-ingestion.md)
and [the reproducible MCP client](../tools/check_uart_scenario_mcp.py).

Latest physical demonstration, 2026-10-10: after explicit approval, **one real MCP flash and
one reset/run passed**. Sector 0 (16 KiB) was erased; all 1,164 approved image bytes matched
readback; flash reported halted, then reset/run reported running. The physical halted-register
query returned SP=`0x20020000`, PC=`0x08000424`, xPSR=`0x01000000`, validating the corrected
query for this path. Persistent server audits match both actual MCP responses, and both scoped
attempt budgets are consumed. The user confirmed green blinking and orange on/off with USER,
with green continuing. No jumper was fitted or required. Precise timing, repetition count,
standalone halt/resume, arbitrary debugging and UART loopback remain untested. The physical
PCB revision remains unknown. See [the process and sequence](flash-demo.md) and
[captured evidence](flash-demo-evidence.json). Earlier failed programming evidence is preserved.

Latest discovery extension, 2026-10-10: **301 full-suite tests passed with no skips**, external
tools required; two subsequently added oversize-publication checks also passed. Ruff and
wheel/source distribution builds passed. A real MCP stdio replay passed all **21 tool calls**;
no external model or physical-board operations were used. See
[the actual response evidence](peripheral-discovery-evidence.json).

[Configurable discovery and coverage](peripheral-discovery.md) now inventory the complete
recognized CMSIS register-type set instead of selecting four types. The new schema-2 F407
reference bundle publishes 41 register blocks, 520 register rows and 2,048 field definitions.
Four documents retain reviewed subsets. FLASH/TPI have disclosed mask gaps; ITM is blocked;
eleven other types are explicitly unmapped. Workflow checks follow the dependency closure
and block publication when required operating facts are absent. The GPIO/LED/button workflow
passed its declared readiness checks in that revision; the separately published UART revision
now adds its supported timer/interrupt workflow. The board netlist remains a partial transcription: `USART2_TX` has no matching net.
The existing default client/build launchers retain their prior bundle and hardware profile.
The new bundle is separately selectable and now included in the independent-release-review gate.

| Milestone | Implemented | Remaining release evidence |
| --- | --- | --- |
| 1: vault/compiler | Three illustrative bundles plus one documented Discovery reference subset; pinned headers; safe XML; resolved DTB/overlay; deterministic publication; web evidence acquisition; board circuit validation; live KiCad export checks | Independent source/semantics review of exact bundle revisions |
| 2: FastMCP | Three stdio tools; immutable target snapshots; exact net lookup; actionable errors; locked dependencies | Integration results are recorded by the test suite |
| 3: HEDG | Session gates; serialized state; agent instructions; deterministic retrieval replay; register/configuration models | Live-assistant behavior remains client-dependent; arbitrary emitted register order is not proved |
| 4: verification | Provisioned rootless sandbox; live compilation/isolation checks; bounded repair hook; optional F407 full-link MCP, pinned startup/linker and ELF/artifact validation; ST-LINK inspection/planning and authorization-gated programming/control; real complete flash/readback/halted reporting and reset/run; human LED/button check | Independent engineering review; standalone halt/resume and broader programming qualification; measured timing/debounce and repeatability |

The implementation environment supplies ARM/AVR GCC, Clang, dtc, and libfdt. A signature-verified
KiCad 9.0.4 toolchain was extracted under `/tmp` for live ingestion checks; KiCad is not globally
installed. A signature-verified project-local Podman installation now provisions and runs the
toolchain image; both locks record its actual immutable image ID. Source
`.praxis-output/podman-env.sh` to use that runtime on this machine. The first authorized physical
attempt wrote the approved image but failed during final register reporting. A separate read-only
comparison confirmed the image. A subsequent execution-only MCP session verified the image and
successfully reset/ran it. The user confirmed green blinking, orange on/off with USER and green
continuing to blink during button interaction. Timing and repeatability remain unmeasured. Historical
counts below are superseded by the latest evidence.

Earlier validation on 2026-10-10: **291 tests passed with no skips**, with external tools required.
The OpenOCD query now uses case-sensitive `xPSR`, shared by inspection and programming, while
preserving the MCP field `xpsr`. Strict Tcl fixtures reproduce and reject the old spelling.
Execution-only grants have zero flash attempts and expose eight build MCP tools without
`flash_firmware`. The first physical attempt's failed audit remains intact; separate read-only
checks matched all 1,164 approved image bytes and confirmed the installed backend's register
spelling. The subsequent real execution-only MCP test returned success, exact image verification
and state running; the later inspection returned unknown, nominal HSI 16 MHz, SysTick LOAD=15999
and enabled GPIOA/GPIOD clocks. The user's actual OpenCode answer confirms the basic LED/button
scenario. No reflash or halt/resume occurred. The halted register-query branch and successful full
flash reporting were unqualified at that stage, before the later successful flash demonstration.
See [execution evidence](hardware-execution-evidence.json)
and the earlier [recovery evidence](hardware-recovery-evidence.json).

Earlier validation on 2026-10-10: **275 tests passed with no skips**, with external tools required.
This adds 54 programming/control tests, including real MCP calls against a fake probe, real
OpenOCD Tcl with modeled memory/writes, exact readback, persistent budgets and failure paths.
The physical board was used only for read-only preflight/planning. The corrected 1,164-byte
LED/button image would erase sector 0 (16 KiB); no operator authorization was created and no
physical programming/reset/halt/run occurred. See [programming evidence](hardware-programming-evidence.json)
and [the scope/command contract](hardware-programming.md).

Earlier validation on 2026-10-10: **221 tests passed with no skips**, with external tools required.
This includes live KiCad ingestion, rootless container isolation, F407 full linking and actual
stdio MCP build/validation calls, clock failure regressions, inspection backend fixtures and real
OpenOCD Tcl guard checks without target attachment. A separate deliberate live stdio session
successfully inspected the user's connected ST-LINK/MCU without reset, halt or programming requests.
Family/core/flash compatibility passed; execution state was `unknown`, CFSR/HFSR were zero and
the nominal RCC clock was 168 MHz under the reference HSE assumption. The running firmware and
physical PCB revision remain unidentified. The corrected OpenCode application passed isolated
full linking and artifact validation; it was not flashed. See [inspection evidence](hardware-inspection-evidence.json)
and [the tool contract](hardware-inspection.md). STM32F401 and AVR polling/interrupt examples additionally passed
isolated object compilation. Ruff and wheel/source distribution builds passed.
See [build evidence](build-service-evidence.json) and [the build service](build-service.md).
The 180-test build evidence is retained as the earlier baseline, superseded by the inspection
evidence for the current regression count.
The release checker still blocks missing independent review of all four exact bundle revisions
and the firmware asset revision; passing implementation tests is not release approval.

Validation on 2026-10-10: **84 tests passed; 4 external integration tests skipped** (two live KiCad
exports and two Podman checks). Ruff passed. Both bundle integrity/routing evaluations passed.
Wheel and source distribution builds passed. MCP stdio integration passed outside the execution
sandbox; that sandbox suppresses the cross-thread wakeups needed by the SDK's stdio file I/O.

The default bundles are illustrative partial connectivity examples, with source-backed editorial
review by Codex. That is explicitly separate from independent embedded/hardware sign-off.
Record independent review in `release-review.json` only after it actually occurs.

## STM32F407VGT6 ingestion extension

The F407 compiler extension adds automatic complete declaration discovery, reviewed UART
semantics, an explicit HSE8 → SYSCLK168/PCLK1=42/PCLK2=84 clock plan, LQFP100 pin validation,
and a separately published bundle. Its XML netlist remains a hand-authored partial example,
and its DTS remains synthetic. It does not establish the user's actual board wiring.

The declaration catalog contains 47 register rows and 463 field definitions across RCC,
GPIO, USART and NVIC. Arrays retain counts and strides. Reset values absent from headers
remain unasserted unless a reviewed import supplies them. Unsupported operating facts
remain marked unknown; required UART register semantics must be supplied before publication.

F407 checks cover deterministic compilation across input locations, exact package pins,
headers/DTS dependency provenance, publication failures, actual ARM header assertions and
real MCP stdio retrieval. Podman image provisioning, an F407-specific approved header lock,
independent review, actual-board schematic ingestion and hardware execution remain pending.

Extension validation on 2026-10-10: **110 tests passed; 4 existing external integration
tests skipped** (KiCad/Podman). Ruff, F407 bundle lint/routing, real MCP stdio sessions,
ARM header assertions, and wheel/source distribution builds passed. Largest F407
peripheral document: RCC, 40,209 bytes, below the 65,536-byte publication limit.

## Optional web ingestion extension

`praxis scrape` supports explicit HTTPS URLs and document catalogs for PDF, static HTML and
UTF-8 text. It archives original bytes, page/table extraction, requirement candidates and
provenance. The F407 catalog names official DS8626, RM0090 and ES0182 documents. Acquired
evidence remains pending review and outside MCP retrieval. `praxis review-import` records an
explicit engineering review; the compiler requires that receipt for registered web evidence.

Validation on 2026-10-10: **131 tests passed; 4 existing KiCad/Podman integration tests skipped**.
Ruff passed. Coverage includes actual PDF text/table extraction, deterministic local archives,
HTTP failures, redirect restrictions, integrity checks, review gates, compiler provenance and
serving without PDF/HTML parser imports. A live download fetched all three official ST PDFs and
extracted their first pages; a separate DS8626 check extracted pages 51 and 63. These smoke-test
archives remain unreviewed under `/tmp`, and were not published into any bundle.

OCR, JavaScript rendering, recursive crawling and automatic trusted interpretation of manual
requirements are not implemented. PDF cross-page tables remain flagged fragments requiring
review. Downloads and output are bounded; the PDF parser does not run in an OS sandbox.

## Milestone 1 implementation acceptance

The missing board semantics path is implemented: component catalogs, reviewed PDF transcription,
explicit LED/button circuit checks, source authority checks, workflow-required facts, native KiCad
hierarchy registration and Markdown-derived board retrieval. The original fixture bundles remain
unchanged. A separate `stm32f407g-disc1-e01-m1` bundle supplies the MB997 E-01 reference GPIO
subset. The user's model is confirmed as STM32F407G-DISC1; its physical PCB revision is unknown.

Reference aliases now resolve LED_A → LD4/PD12, LED_B → LD3/PD13 and USER_BUTTON → B1/PA0.
Active levels, the external pulldown, series components, separate nets, timing semantics and
source locators are included. OpenCode's `temp/opencode.json` selects this reference bundle;
reconnecting is required to replace its prior server session.

Validation on 2026-10-10 with KiCad 9.0.4 enabled: **158 tests passed; 2 Podman tests skipped**.
Both live KiCad export comparisons and both native-profile compilation checks passed. Real stdio
MCP tests include the new board aliases. Ruff and wheel/source distribution builds passed.
The dedicated Milestone 1 acceptance suite passed **131 tests with no skips**.

See [the evidence report](milestone1-evidence.json), [board ingestion](board-ingestion.md) and
[the acceptance gate](milestone1.md). **Milestone 1's v1 implementation acceptance passes.**
Independent engineering review remains part of release qualification and is not fabricated or
replaced by implementing-agent editorial review. Physical-board qualification and the overall
v1 release gate remain open.
