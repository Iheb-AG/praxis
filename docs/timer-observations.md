# Artifact-bound timer observations and qualification

For the subsequent operator-approved physical trial and its current phase results,
see [the physical report](reports/timer-route-results.md) and
[sanitized raw evidence](timer-route-physical-evidence.json). The software-only
increment below remains a historical record; physical results bind to their exact artifact.

Milestone 4 now supports a fixed `timer-routes-v1` software telemetry ABI through
the existing read-only `read_firmware_telemetry` MCP tool. Its offline qualifier
recomputes all eight measured periods from nine raw captured timestamps and checks
terminal shutdown evidence. This increment has **no physical board observation or
flash**; fake probes, independent effects models and isolated target builds establish
software behavior only.

The hardware knowledge remains the unchanged
[timer-routes-v1 bundle](../bundles/stm32f407g-disc1-e01-timer-routes-v1/wiki/index.md),
revision `2dbfa901ec294c0f8edc5e37e87d41a3aa69f169dcce18b4acf088d48f5c0167`.
Counts stay at 39 mode contracts and 23/38 ready authored workflows. This strengthens
verification of an existing route; it does not add MCU modes or establish full F407 acceptance.

## Separate contracts

- Hardware operating facts, AF/package constraints, board connections and prerequisite
  edges remain in the versioned source profile and immutable Markdown bundle.
- The [versioned telemetry contract](../praxis/data/timer-route-telemetry-v1.json)
  defines application-owned words and a fixed example recipe. It is not MCU register
  metadata, a caller-supplied schema or a new manufacturer branch in the compiler.
- The [new application snapshot](../examples/stm32f407g-disc1-timer/routes_telemetry_application/main.c)
  retains byte-identical timer controller headers from the preceding example. It adds
  a shared one-shot procedure and a coherent terminal-result publisher. Earlier source
  snapshots and published bundles are unchanged.

The 136-byte global `.bss` object `praxis_timer_route_telemetry` contains 34 uint32
words: generation, ABI identity, publication count, phase/status/flags, recipe and
frame counts, nine raw capture values and final timer/pin snapshots with a validity
mask. Invalid or inaccessible snapshots cannot count as quiet just because their
initial values are zero.

A sole main publisher sets generation odd, executes a memory barrier, writes named
fields, executes another barrier, then publishes the next even generation. It repeats
only that stable terminal report. The busy-loop spacing is not a timing reference,
a repeated test or an IRQ heartbeat. No timer, GPIO or IRQ activity is restarted by
the publisher. Explicit scalar initialization avoids introducing a hosted `memset`
dependency into the separately pinned freestanding assets.

## Application and observation sequence

The source-backed procedure still checks privileged startup, actual nominal HSI16
and divisor assumptions, gates, reset transitions, pin ownership and register direction.
It arms TIM5 capture before TIM2 PWM output, discards the enable edge, primes a natural
edge, then records eight periods. Raw words preserve a rejected interval too. It stops
the owned timers, releases only PA1/PA2 to input, and reads end-state snapshots only from
accessible domains. Failed readback or lost gates prevent a quiet-result qualification.

```mermaid
sequenceDiagram
    participant Assistant
    participant Knowledge as Knowledge MCP
    participant Build as Isolated build MCP
    participant Firmware
    participant Reader as Read-only observation MCP
    participant Qualifier as Offline qualifier
    Assistant->>Knowledge: Index, PA1/PA2 aliases, RCC/GPIO/TIM documents
    Knowledge-->>Assistant: Exact route and prerequisite contracts
    Assistant->>Build: Build separate telemetry application snapshot
    Build-->>Assistant: Accepted artifact and pinned ELF/image identities
    Note over Assistant,Firmware: Future physical run requires wiring confirmation and exact-image approval
    Firmware->>Firmware: Run one-shot paired capture; latch status and quiesce
    Firmware->>Firmware: Publish coherent stable terminal results
    Assistant->>Reader: Launch-selected artifact/kind; connection_id and bounded samples
    Reader->>Reader: Validate ELF object, target UID and all image bytes
    Reader->>Firmware: Read matching duplicate SRAM records between even generation checks
    Reader->>Reader: Verify all image bytes again
    Reader-->>Assistant: Raw timestamp records, image identities and recomputed assessment
    Assistant->>Qualifier: Recorded windows, exact artifact/revision, expected outcome
    Qualifier->>Qualifier: Recompute every interval; check identity, freshness and shutdown
    Qualifier-->>Assistant: Scoped reported result, failures and limits
```

The reader uses the existing fixed, launch-selected artifact path. ELF validation
requires one correctly sized global object in allocated writable main SRAM `.bss`,
below the reserved stack area. It verifies the complete image before and after
sampling, checks target identity and compares duplicate coherent records. The request
contains only `connection_id`, `samples` and `interval_ms`. SDK v1 may ignore surplus
keys; tests prove supplied address/symbol/artifact keys cannot redirect the reader.
No arbitrary memory or caller-selected object is exposed. This launch has no
programming/control authorization, so flash/reset/control tools are absent.

## Qualification algorithm

[`praxis/timer_route_telemetry.py`](../praxis/timer_route_telemetry.py) accepts only
complete uint32 records with the fixed magic, ABI, size and bounded encodings.
It re-decodes raw values; supplied labels and assessments have no authority.

```text
for each recorded window:
    require exact artifact, bundle, ABI and well-formed image/ELF identities
    require reported before/after image verification and running CPU
    decode every raw record; reject malformed or torn records
    require advancing publication/generation with matching increments
    require all terminal fields stable across samples
    require the fixed application recipe and zero unused capture words
    recompute unsigned32-bit deltas between the stored capture words
    check reported validated-prefix counts against those deltas
    require all end snapshots present, zero, and corresponding quiet flags
    passed: require nine captures, eight valid periods, success status
    timeout: require clean latched failure, timeout status, zero captured edges
    failed: require a clean latched failure, preserving any captured prefix

across ordered windows:
    require the same image/ELF, stable terminal result and advancing publications
    reject stale/reused, discontinuous or mixed windows
    report no repeatability or independent physical qualification
```

A passing result checks 1,000±2 local timer ticks for all eight intervals. Both
counters share HSI; this does not calibrate frequency or duty cycle. A qualified
no-edge timeout reports what the firmware observed; it does not identify a removed
jumper or exclude another physical fault. Repeating the same terminal report does
not rerun the test. There is no boot-unique identity: reset versus rollover has
limits, and debug reads can perturb timing. Recorded image checks are reported
evidence; the offline qualifier does not re-read the board.

## Commands

Use existing dependencies and pinned Podman images. Every output directory/report
must be new. Build acceptance exposes no hardware tools:

```bash
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 .venv/bin/pytest -q
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 .venv/bin/python tools/check_target_acceptance_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-timer-routes-v1 \
  --plan examples/acceptance/stm32f407g-disc1-timer-observations.json \
  --catalog examples/capabilities/stm32f407g-disc1-timer-routes.json \
  --workspace examples --assets assets/stm32f407vg --lock toolchain-f407.lock.json \
  --inventory examples/inventory/stm32f407g-disc1/inventory-v2.json \
  --output /tmp/praxis-timer-observations-build-new
```

All fifteen earlier source cases remain unchanged; the new plan adds only the
telemetry application. It uses the existing workflow's knowledge contract.

For a **future approved physical test**, launch the read-only build service using
absolute bundle, assets, workspace, artifact-store, lock and matching hardware-profile
paths. Add `--telemetry-artifact EXACT_ARTIFACT_ID --telemetry-kind timer-routes-v1`.
Do not add a programming authorization to the observation launch. Once the exact
image is installed and running, the existing observation helper supports an explicit
artifact store:

```bash
.venv/bin/python tools/check_firmware_telemetry_mcp.py \
  --bundle /absolute/path/to/bundles/stm32f407g-disc1-e01-timer-routes-v1 \
  --hardware-profile /absolute/path/to/matching-hardware-profile.json \
  --artifacts /absolute/path/to/exact-artifact-store \
  --artifact EXACT_ARTIFACT_ID --telemetry-kind timer-routes-v1 \
  --probe-serial EXACT_PROBE_SERIAL --samples 3 --interval-ms 1000 \
  --output /absolute/path/to/new-private-observation-directory

praxis qualify-timer \
  --bundle /absolute/path/to/bundles/stm32f407g-disc1-e01-timer-routes-v1 \
  --artifact EXACT_ARTIFACT_ID --expect passed \
  --observation /absolute/path/to/observation-00.json \
  --output /absolute/path/to/new-qualification.json
```

Choose longer sample spacing if publications have not advanced; stale samples fail
qualification. `--expect timeout` checks a clean terminal no-edge timeout and
`--expect failed` checks a clean terminal failure. They do not weaken success checks.
Exit 0 means the requested reported outcome passed, exit 1 means qualification failed,
and malformed input produces an error. Reports omit probe identifiers and include
input hashes. Never combine reset/reflash runs or reuse an old passing window.

## Evidence and remaining work

Validation: **1,270 full-suite tests passed, zero skipped**, with required external
tools. A 155-test affected-suite rerun includes the later stricter raw-prefix check
and its two new regression cases; counts overlap. All 16 applications built/revalidated
in 92 actual MCP calls. Native knowledge retrieval passed 52 calls. Final Docker passed 162
calls across four sessions and five explicitly synthetic qualification cases. Wheel,
source-distribution, provenance/link and offline lock checks passed. Independent
release review remains blocked; no physical hardware operation occurred.

[The evidence record](timer-observations-evidence.json) distinguishes real MCP transport,
explicit fake-probe responses, independently modeled target effects, actual Tcl guards,
isolated compiler/ELF checks and Docker fixture qualification. Synthetic fixture image
metadata is labelled synthetic; it is not promoted to a physical image readback.

Tests exercise all 31 earlier timer faults through the actual shared application procedure,
32-bit counter wrap, ABI/object layout, every raw interval, malformed/forged metadata,
publication continuity, no-edge timeout, failed cleanup and unchanged controller snapshots.
Real stdio MCP runs use explicitly configured fake probes. Actual OpenOCD Tcl runs replace
the read functions with fixture effects and never initialize an adapter. The three-tool
knowledge runtime remains unchanged and performs no observation or hardware operation.

Next: confirm board revision/orientation and current wiring, prepare the reviewed passive
PA1/P1-11 ↔ PA2/P1-14 fixture with all power disconnected, obtain fresh exact-image approval,
and collect artifact-bound success/no-edge/recovery observations. Any prior PA2↔PA3 wire and
other attachments must be removed for this route. Physical qualification and independent
review remain open. Timer IRQ/DMA, other modes, boot/update, USB, Ethernet, storage and the
remaining F407 inventory still need their own contracts and acceptance evidence.
