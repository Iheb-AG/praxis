# Publication readiness

Assessment date: 2026-10-15. Praxis is suitable for publication as an explicitly labeled
**experimental development alpha**, once the public export and licensing review below are
completed. It is **not ready for a qualified v1 release**. Passing tests and one working board
do not establish universal MCU coverage or production hardware reliability.

## Current milestone state

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

The [paired timer physical trial](reports/timer-route-results.md) now passes its
three exact-artifact phases: wired success, clean no-edge timeout and wired recovery.
One explicitly approved flash/readback and reset/run were followed by operator-driven
power cycles and read-only MCP observations. Six windows/18 samples show eight
1,000-tick periods in both positive boots, preserved timeout failure and quiet shutdown.
This is scoped firmware/capture evidence; independent frequency/duty measurement,
formal repeatability, physical PCB revision, timer IRQ/DMA, full F407 acceptance and
independent release sign-off remain open. The prior software-only evidence below
remains historical and is not retroactively qualified.

The [timer observation increment](timer-observations.md) passes 1,270 strict full-suite
tests with zero skips, plus 155 overlapping affected checks including two added later.
All 16 examples build/revalidate through 92 MCP calls; Docker passes 162 retrieval calls
and five synthetic qualification cases. It adds exact-artifact timer SRAM observation
and recomputed raw-period/cleanup checks. Knowledge mode counts stay 39 and 23/38 ready
workflows. No new flash, physical observation, independent review or all-mode MCU
acceptance is implied. The release gate still exits 2 for missing exact-bundle and
firmware-asset independent review.

The [routed timer increment](timer-routes.md) passes **1,165 strict full-suite tests,
zero skipped**, plus 51 focused checks including six added after full-suite collection.
It adds generic exact per-mode instance scopes and data-defined PA1/TIM2_CH2 PWM /
PA2/TIM5_CH3 capture, reaching 39 contracts and 23/38 ready authored workflows. All 15
applications build/revalidate in 90 actual MCP calls; Docker passes 162 calls across
four sessions. Three publications are byte-identical; distribution checks pass.
The external route is source/model/compiler checked only: physical wiring/revision,
exact-artifact execution and independent bundle/asset sign-off remain open. Full
F407 acceptance is false; no hardware operation occurred in this increment.

The [timer operating increment](timer-modes.md) passes **1,120 strict tests, zero skipped**.
Two new internal TIM2 workflows and an RCC prerequisite contract raise mode support to35
contracts and22/37 ready workflows. All fourteen examples link/revalidate through86 actual
MCP calls;161 container calls pass using the existing image. These are modeled/compile-tested
internal reference and software-event scopes. External PWM/capture, physical execution and
independent exact-bundle/asset review remain open; no runtime/compiler specialization was added.

The [register interpretation increment](register-field-views.md) passes **1,052 strict tests,
zero skipped**. Its new immutable F407 bundle preserves full input/output and mixed-channel
timer field tables through generic source-profile data. Native MCP passes 52 calls, all 12
existing application builds/revalidations pass in 81 calls, and Docker passes 161 calls.
This closes a compiler representation gap; the 22 reviewed subsets, 32 mode contracts and
20/33 ready workflows remain unchanged. PWM/capture operating contracts, their matching
example/physical qualification and independent release review remain open.

The [second F407 source-scope review](inventory-reconciliation.md) resolves all 29 original layout
items with source-bound editorial records, retains all 1,683 indexed records, and reduces pending/
mixed applicability to 299 sections. It records 24 target/package facts without claiming new
operating support. **1,022 strict tests pass with zero skips**; all 12 builds/revalidations and 161
Docker MCP calls pass. Source interpretation is implementing-author editorial review, not
independent sign-off; full body/mode, physical and release qualification remain open.

The [manufacturer scope stage](manufacturer-inventory.md) adds a source-pinned inventory CLI
and outline MCP tool. Strict regression passes **1,005 tests with zero skips**; all twelve
F407 examples still build/revalidate through 81 MCP calls, and the rebuilt Docker runtime passes
161 calls across four sessions. The 1,683 indexed records are source sections/errata rows,
not a new feature-support percentage. Applicability, extraction, complete mode requirements,
physical qualification and independent review remain open.

The [full F407 audit](f407-full-acceptance.md) supersedes the older validation counts below:
**970 tests passed, zero skipped**, with required external tools enabled. Installed KiCad
10.0.7 passes native export/compilation checks. The fixed document ceiling has been removed.
The new candidate publishes42/42 recognized blocks, while reviewed coverage remains22 subsets
and20/33 authored workflows. All12 existing F407 applications link and ELF-revalidate through
actual MCP against that revision;161 rebuilt Docker MCP calls pass across four sessions.
Full manufacturer-mode coverage, complete board topology, broader physical qualification and
independent review remain open. The next priority is closing F407 gaps, not expanding families.

Earlier [STM32/ARM extension](arm-core-support.md) evidence passed **861 tests with four native
KiCad skips**, Ruff, the lock check and actual MCP retrieval/build revalidation. It publishes22
reviewed subsets and32 mode contracts, with20/33 ready authored workflows. The new core image
is unflashed. [Experimental release scope](experimental-release.md) centers on F407/Cortex-M4;
this is distinct from qualified-v1 approval and broad STM32 family support. Source catalogs
and Markdown now retain complete content without the former fixed document ceiling.

The [reusable Cortex-M knowledge adapter](target-adapters.md) now demonstrates CPU/header
and macro-convention portability through a fictional Cortex-M3 bundle. Full regression:
802 passed, four native KiCad skips; a topology-only evaluation check passed separately.
Actual ingestion publication and 14-call knowledge retrieval passed. This expands the compiler
architecture while adding no real board, reviewed operating mode or flash qualification.

| Work | State | Evidence and remaining boundary |
| --- | --- | --- |
| M1: ingestion and vault | Implementation acceptance passed | Deterministic publication, structured adapters, source provenance, exact topology, web evidence and review gates. Independent review of current bundle revisions remains pending. |
| M2: retrieval MCP | Implemented and protocol tested | Three tools, target isolation, full documents, exact lookup, integrity errors. Installed dependencies allow offline retrieval. |
| M3: HEDG routing | Implemented and tested | Serialized prerequisite retrieval and branching dependencies; this does not prove arbitrary generated firmware ordering. |
| M4: isolated verification | Implemented and strengthened for supported profiles | Rootless target compilation/isolation; F407 full linking/ELF validation; offline ABI phase qualification preserves failed windows; qualification remains scoped. |
| Board programming extension | Demonstrated on one board | Exact-artifact flash/readback/reset-run and user-confirmed LED/button and UART loopback/failure/recovery. Physical PCB revision, measured timing and broader qualification remain open. |
| Telemetry extension | Implemented; scoped failure/recovery/pause observed | Artifact-bound coherent samples detected disconnected-loopback failure and later healthy progress/pause. Initial recovery timeout and unexpected restart remain unresolved; repeatability is unqualified. See [follow-up results](reports/telemetry-failure-recovery-results.md) and [earlier evidence](telemetry-evidence.json). |
| General autonomous hardware debugging | Incomplete | No general breakpoint/step/debugger workflow, independent packet capture, programmable button fixture or qualified autonomous repair loop. |

Vectorless retrieval is already implemented. More ingestion sources improve coverage; embeddings
are not a planned dependency. MCU declaration discovery is broad, while reviewed operating modes
and actual-board connectivity are deliberately narrower. Publishing register declarations does
not make every SPI, I2C, CAN, ADC, DMA or USB workflow supported.

The [feature expansion](peripheral-modes.md) adds six reviewed subsets for 13 total and seven
explicit instance-scoped mode contracts. A 17-call real knowledge/build MCP replay passed,
including CRC/DMA sandbox linking and ELF revalidation. It performed no board operations.
SPI wiring, complete RNG clock setup and many other MCU operating modes remain blocked.
The new qualifier preserves both successful and anomalous UART observations; it does not
establish repeatability or independent physical truth.

The [shared manual evidence compiler](manual-review-compiler.md) now prepares header-checked
review packets through both the CLI and the ten-tool ingestion MCP. An actual replay produced
319 candidates across ten peripheral groups while retaining four conflicts. These unreviewed
packets do not expand qualified operating-mode coverage or satisfy independent review.

The subsequent [clock-mode extension](clock-modes.md) publishes reviewed F407 FLASH latency
and PWR Scale 1 subsets, bringing the selected bundle to 15 reviewed subsets and 12 mode
contracts. Generic transitive mode dependencies now gate PLL-backed RNG knowledge. A 20-call
actual MCP replay passed sandbox compilation/linking and ELF revalidation; 27 focused checks
exercise the same register callback's modeled order and failures. The example has not been
flashed or physically qualified. FLASH erase/programming and broad MCU support remain incomplete.

The [ADC workflow expansion](adc-expansion.md) adds ADC1 internal-reference sampling,
shared prescale/reference configuration and a TIM2 polling settling mode. Reusable definition
extensions preserve the base records and reject stale hashes, target mismatches and competing
changes. Workflow review packets expand authored dependency/register scopes but never approve
facts automatically. The new bundle has 17 reviewed subsets and 16 mode contracts. Nine actual
knowledge MCP calls and deterministic repeated publication passed. Its initial isolated build
attempt was blocked by missing Podman. After restoration, a twelve-call actual MCP replay
passed target compilation, linking, ELF/vector validation and artifact revalidation. The
example has not been flashed or physically qualified; see [build evidence](adc-build-evidence.json).

The [support assessment](capability-support.md) now makes these scopes measurable through a
read-only CLI and an optional target-bound contributor catalog. Its current 26 goals include
planned boot/update work; nine are knowledge-ready. The catalog is not an exhaustive MCU feature
denominator and does not add operating coverage. [CONTRIBUTING.md](../CONTRIBUTING.md), PR/issue
templates, authoring schema and a CI preflight step describe how to add reviewed modes and boards.

The subsequent [I²C expansion](i2c-expansion.md) adds scoped I2C1 controller transmission,
bringing its bundle to 18 reviewed subsets and 18 operating contracts, with 12 ready authored
workflows out of 23. Actual MCP retrieval, rootless ARM build/link, ELF checks and artifact
revalidation pass. Broad I²C, wired-device readiness and physical transactions remain blocked.
Successive definition amendments bind the exact composed parent state; source catalogs retain
complete provenance with deduplicated metadata. See [latest evidence](i2c-expansion-evidence.json).

## Alpha publication checklist

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

The entries below retain earlier development and physical-test evidence.

The latest [physical CAN attempt](reports/can-loopback-results.md) passed its
approved single flash/readback/reset-run, but **the CAN application failed** with
`init_timeout` in all ten coherent samples. Success qualification rejects the
result; expected-failure qualification confirms the stable, freshly published
failure report. A fixed read-only MCP diagnostic extension reports INRQ=0,
INAK=1 and RX low, with the expected BTR. Root cause and any RX prerequisite
remain unconfirmed. The new reader passes **734 tests with 4 KiCad skips** and
Ruff; physical CAN success, repeatability and independent review remain open.
Both operation budgets are consumed; the installed CAN image remains in its
terminal failure-publication loop. See [current evidence](can-telemetry-evidence.json).

The preceding [CAN telemetry continuation](can-telemetry.md) passes **721 tests
with 4 KiCad skips**, including 125 focused telemetry/qualification checks,
and an actual sixteen-call knowledge/build MCP replay. An explicit fixed CAN
ABI preserves the existing UART default and rejects mismatched ELF symbols.
Actual stdio MCP with a fixture probe and actual OpenOCD Tcl with modeled memory
exercise observation and guard failures. After reconnection, five actual MCP
preflight calls inspected the selected target, prepared the 4,524-byte sector0
plan and rejected the older installed image before CAN SRAM reads. No write or
reset occurred. The image is unflashed and physical CAN behavior unqualified;
exact-image approval is pending. Coverage counts are unchanged.
See [current evidence](can-telemetry-evidence.json).

The preceding [CAN continuation](can-expansion.md) passes **660 tests with 4 KiCad skips**,
Ruff and an actual sixteen-call knowledge/build MCP replay. Its bundle has
20 reviewed subsets, 24 mode contracts and 15 ready authored workflows out of 28.
Forty-six digital effect cases exercise the shared controller; the isolated target
build binds the real CAN1 RX0 handler. The one-shot image remains unflashed.
External CAN and general CAN workflows remain blocked. Artifact-bound CAN
observation is required before its physical qualification; the existing UART
telemetry decoder cannot interpret CAN globals. See [current evidence](can-expansion-evidence.json).
No hardware operations occurred; overall MCU completion remains unknown.

The preceding [DAC continuation](dac-expansion.md) passes **609 tests with 4 KiCad skips**,
Ruff and an actual thirteen-call knowledge/build MCP replay. Its bundle has
19 reviewed subsets, 20 mode contracts and 13 ready authored workflows out of 25.
The transfer entry is retained in the ARM ELF while main leaves EN1=EN2=0.
Analog accuracy, wired DAC operation and independent review remain unqualified;
see [current evidence](dac-expansion-evidence.json). This increment performed no
hardware operations and does not establish an overall MCU completion percentage.

The preceding I²C continuation passes **574 tests with 4 KiCad skips**, Ruff and
actual MCP knowledge/build checks; [its evidence](i2c-expansion-evidence.json)
records the final source, bundle and artifact identities. Physical I²C remains untested.

Earlier provisioned checks passed **472 tests, zero skips**. The Podman restoration
continuation passed **535 tests with 4 skips**, Ruff, wheel/source archive contents and public
documentation links. Six previously skipped Podman checks now pass; four KiCad checks remain
unavailable. Strict qualification of all external tools is not claimed. A real 17-call knowledge MCP replay and an
installed-wheel support CLI from an unrelated directory passed in the preceding support-only
continuation. See [support evidence](capability-support-evidence.json) and
[initial ADC evidence](adc-expansion-evidence.json) and [successful build follow-up](adc-build-evidence.json).
A separately installed wheel previously served an exported bundle through real
stdio MCP from `/tmp`, using preinstalled dependencies. A fresh offline dependency installation
could not resolve uncached packages; no empty-cache offline installation or hosted CI pass is claimed.
Private/raw paths are excluded from the checked archive. The release checker retains two review blockers:
missing independent bundle review and missing independent firmware-asset review. It additionally
reports missing KiCad in the current environment. Other qualification
limits below remain explicit even when they are not mechanically checked by that release script.

1. Export the public source distribution or a clean source checkout. Keep `.praxis-output`,
   `temp`, probe identifiers, operator grants, raw downloaded manuals, private logs, caches and
   generated firmware artifacts out of publication. Preserve ST/Arm notices accompanying
   redistributable headers/assets. Review rights for source-derived extracts and schematics;
   Praxis's MIT license does not automatically relicense third-party material.
2. Build and inspect distributions with the commands below. The wheel contains Python runtime
   modules; obtain bundles/assets/examples from the source distribution. The source archive now
   includes the sandbox recipe and CI definition. Some source-backed profiles require acquiring
   their cataloged manual archives again before recompilation; serving shipped bundles does not.
3. Publish test commands, exact dependency/image locks, bundle and asset revisions, and the
   distinction between modeled tests, compile outcomes, human observations and live telemetry.
   Local test evidence does not claim a successful run on hosted CI or all operating systems.
4. Configure and run hosted CI from the clean public repository. This workspace's Git metadata
   is not usable as a normal checkout, so it supplies no verified public commit/release identity.
   Initialize a clean publishing checkout rather than treating workspace metadata as provenance.
5. Review the public documentation export. Curated UART reports and portable client/test examples
   now live under `docs/` and `examples/`; public file links pass archive checks. Historical raw
   `temp/` sessions and local launchers are omitted. Use the CLI configurations in the archive.
   A public website or paper should link only to exported material.

```bash
uv sync --locked --extra ingest --extra build --extra test --extra web
uv run ruff check praxis tests tools server.py compiler.py
uv run pytest -q
uv build --out-dir /tmp/praxis-dist
uv run python tools/check_distribution.py /tmp/praxis-dist
# Full qualification requires provisioned native tools and the rootless image:
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q
uv run python tools/release_check.py
```

The release checker intentionally fails while `release-review.json` lacks an independent
reviewer's sign-off for all current shipped bundle revisions and the firmware asset revision. Do not
change that status to obtain a passing release check. No external publication or deployment
has been performed as part of this assessment.

## Qualified v1 blockers

- Independent embedded/hardware review with exact source, bundle and startup/linker revisions.
- Confirmed board revision/solder-bridge configuration for each claimed hardware setup, repeated
  physical runs, measured timing and debounce, and explicitly scoped supported modes.
- Broader programming failure/recovery qualification and standalone halt/resume evidence.
- Resolve the follow-up UART recovery timeout and unexpected restart before claiming repeatability;
  preserve the successful and unsuccessful windows in [qualification evidence](telemetry-qualification-evidence.json).
- Clean-machine/hosted CI reproduction, finalized public provenance and third-party rights review.
- Clear limitations for partially reviewed peripheral discovery and binding-specific DTS support.
  Automated PDF extraction still produces evidence requiring review; it is not trusted circuit
  interpretation or automatic complete operating-semantics publication.

General autonomous debugging and support for every MCU peripheral are roadmap work, not claims
of this alpha. A useful next development sequence is: investigate the recorded telemetry anomalies
and repeat qualification, add external test stimuli/capture adapters, then
scoped debugger operations and a bounded repair loop. Add operating coverage per reviewed workflow
rather than declaring whole peripherals ready because their headers parse successfully.
