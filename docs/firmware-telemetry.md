# Artifact-bound firmware telemetry

The optional build/hardware MCP can observe the UART example's software counters on a running
STM32F407. The knowledge server retains its three read-only tools. Hardware addresses and
configuration came from the selected bundle through MCP; the telemetry layout is a separate
software ABI implemented by the example firmware.

The reader also supports the explicitly selected [CAN internal-loopback ABI](can-telemetry.md).
Set `--telemetry-kind can-loopback-v1` together with its accepted artifact. UART
remains the default; no automatic ABI inference or arbitrary symbol access is introduced.

Current board state, 2026-10-12: the approved CAN telemetry image has replaced
the UART image. It reports an initialization timeout; the captured CAN test failed.
See [current physical results](reports/can-loopback-results.md). The UART observations
below remain historical evidence for their earlier images.

Physical evidence, 2026-10-11: the revised artifact passed MCP programming/readback/reset-run,
boot-paused observation, two running observations and a user-triggered pause observation. Running
windows gained 40/43 validated frames with no reported UART/queue errors; paused windows retained
timer progress with zero frame progress. Final per-run count: 509 frames. Both programming grants
used during development are consumed; the board is left paused. See [captured evidence](telemetry-evidence.json).
The first candidate and rejected live reads are preserved as development history rather than
presented as successful telemetry. No independent wire capture or optical measurement occurred.

A follow-up [failure/recovery experiment](reports/telemetry-failure-recovery-results.md) detected
failure with the jumper removed, observed restored-loopback progress and confirmed final pause.
Its initial recovery timeout and unexpected restart remain unresolved; it does not qualify
repeatability. The final observed application state is paused in run 3 with 804 validated frames.

Enable this tool only for a previously accepted artifact:

```bash
praxis build-serve --bundle /absolute/path/bundles/stm32f407g-disc1-e01-uart-v1 \
  --assets /absolute/path/assets/stm32f407vg --workspace /absolute/path/examples \
  --artifacts /absolute/path/.praxis-output/firmware-artifacts \
  --lock /absolute/path/toolchain-f407.lock.json \
  --hardware-profile /absolute/path/hardware-profile.json \
  --telemetry-artifact ARTIFACT_ID
```

Install the `build` extra and provision the pinned hardware profile first; see
[build service](build-service.md) and [hardware inspection](hardware-inspection.md).
Without `--hardware-authorization`, no programming or execution-control tools are exposed.
Telemetry does not require a write grant. Each process has its own connection IDs.

## Tool contract

`read_firmware_telemetry(connection_id, samples=2, interval_ms=100)` reads 1–5 samples with
10–1000 ms requested spacing. Call `inspect_target` in that MCP process first. The tool accepts
no arbitrary address, symbol, expression, register, backend command or ELF path. It resolves
the one fixed `praxis_telemetry` global object from the validated launch-selected artifact.
It must be a 92-byte aligned object inside writable main-SRAM `.bss`, below the reserved stack.

Every call revalidates artifact hashes and backend identity, locks the selected probe, checks
MCU identity, compares all image bytes before reading SRAM, and compares the image again after
sampling. A block-word mismatch requires two individual reads both matching the expected word;
otherwise it fails. Rechecks are counted in the response. This handles inconsistent running-target
block reads observed on the connected probe without silently accepting mismatches. The current
bounded implementation supports images of 392 bytes through 64 KiB and
has a 15-second backend timeout with bounded diagnostics. It requests no halt, reset, resume,
programming or memory write. Debug attachment and reads can still perturb timing.

The companion `telemetry_application` retains the UART/timer/button behavior and publishes
software state every 250 nominal milliseconds. Main is the sole publisher. A short interrupt
mask snapshots ISR-owned counters; barriers surround an odd/even generation counter. The
reader accepts two identical complete records only when generation is unchanged and even across
both reads. A first 20 ms publisher was physically too fast for this probe's reads and was rejected;
the slower publisher is a separate artifact requiring a separate programming grant.
Four unsuccessful consistency attempts return `TELEMETRY_BUSY`; they never halt the board.

Fields include uptime, timer/UART/EXTI IRQ counts, transmitted/received bytes, started/validated
frames, run number, application state, button presses, UART/queue errors and a failure reason.
ABI/header size/state encodings are validated before results are returned. Failure reasons
distinguish timeout, invalid frame, unexpected receive, UART error and queue overflow.

The assessment separates fresh timer progress, continuity, run changes, UART progress, reported
failure and the firmware's blue-success indicator. A paused application is expected to have
timer progress without UART progress. Stale/repeated samples do not establish progress. Counters
are uint32 values; a reset can mimic rollover, and no boot-unique identity is implemented.

## Observation sequence

```mermaid
sequenceDiagram
    participant A as Assistant or test client
    participant M as Build/hardware MCP
    participant S as Artifact store
    participant D as Pinned OpenOCD
    participant F as Running firmware
    A->>M: inspect_target(selected_probe)
    M-->>A: Connection identity
    A->>M: read_firmware_telemetry(connection, 2, 100)
    M->>S: Revalidate fixed artifact and ABI object
    M->>D: Lock probe; verify backend and MCU identity
    D->>F: Exact flash comparison
    alt Image mismatch
        M-->>A: READBACK_MISMATCH; no SRAM observation
    else Image matches
        loop Bounded samples and consistency attempts
            D->>F: Read generation, whole ABI record, generation
        end
        D->>F: Repeat exact flash comparison
        M-->>A: Coherent samples, deltas, outcome limits
    end
```

These are firmware self-reports, not an independent logic analyzer, electrical continuity check,
optical sensor or oscillator measurement. Matching flash does not prove that a truthful image
is executing. The tool creates no button stimulus and does not replace engineering review.
General breakpoints, stepping, variable inspection and autonomous repair remain future work.

## Reproduce through MCP

Build `stm32f407g-disc1-uart-loopback/telemetry_application` with `build_firmware`, validate it,
then use the read-only client below. Output directories must be new; raw logs contain target
identifiers and should stay private.

```bash
python tools/check_firmware_telemetry_mcp.py \
  --artifact ARTIFACT_ID --probe-serial YOUR_SELECTED_SERIAL \
  --hardware-profile /absolute/path/hardware-profile.json \
  --output .praxis-output/telemetry-read-01 --samples 5 --interval-ms 1000
```

Before installing this candidate, `--expect-mismatch` checks that the older installed firmware
is rejected. The client also saves an exact read-only programming plan, but never creates a
grant or performs a write. Installing the candidate needs its own exact-image flash approval.
After installation, observe paused counters, press USER to start loopback and observe increasing
validated-frame counts; press USER again and confirm those counts stop while timer counts advance.
Human LED observations and telemetry outcomes must be recorded separately.

Continue with the [Milestone 4 failure/recovery procedure](scenarios/telemetry-failure-recovery.md)
to test a removed jumper, restored loopback and pause using the same installed image.
