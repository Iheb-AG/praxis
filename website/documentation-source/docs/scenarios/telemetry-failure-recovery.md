# Milestone 4: UART telemetry failure and recovery

This procedure qualifies failure detection and recovery for the installed telemetry example.
It uses real stdio MCP calls and user-performed physical stimuli. It requires no new flash
or execution-control grant. A physical power cycle restarts the application in its paused state.

## Scope and prerequisites

- Reference: STM32F407G-DISC1, MB997-E-01; the user's physical PCB revision is unconfirmed.
- Knowledge bundle: `stm32f407g-disc1-e01-uart-v1`, revision
  `1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b`.
- Installed telemetry artifact:
  `c192a736ed2958697e4c89022094ae3b896b01529c8f391e074068c1c2c71688`.
- Loopback connection from the reviewed bundle: PA2 (P1-14) to PA3 (P1-13).
- Disconnect **all board power** before changing the jumper. Reconnect through ST-LINK USB.
- Use the existing selected-probe plan; never choose a different probe automatically.

Earlier run/pause observations are recorded in [telemetry evidence](../telemetry-evidence.json).
This experiment's outcomes are recorded in the [results report](../reports/telemetry-failure-recovery-results.md).
Historical human observations of the non-telemetry UART image are separate evidence; they do
not qualify this image's failure counters. Follow the [telemetry contract](../firmware-telemetry.md)
for record validation, read limitations and tool setup.

## Procedure and acceptance checks

| Phase | User stimulus | MCP evidence required |
| --- | --- | --- |
| Preflight | Board connected | Discover telemetry tool without flash/control tools; select the expected probe; inspect target; validate artifact-bound plan. If disconnected, record that outcome and stop board calls. |
| Disconnected loopback | Power off; remove jumper; reconnect; press/release USER once; wait at least 2 seconds | Exact image matches before/after samples; coherent records report `failed` and a nonzero failure reason. Timer continues; validated frames do not increase during the failed window; blue success is false. Record the actual failure name rather than assuming timeout. |
| Restored loopback | Power off; restore jumper; reconnect; press/release USER once; leave running | Exact image matches; coherent records report running, timer progress and increasing validated frames, with no reported UART/queue errors or active failure. Capture a second window if needed to avoid an in-flight frame boundary when comparing TX/RX progress. |
| Success threshold | Leave restored loopback running for at least 12 nominal seconds | A coherent sample reports at least 100 validated frames in the current run and blue success. This is a software criterion, not a measured 12-second timing test. |
| Pause | Press/release USER once; wait at least 1 second | Application reports paused; timer continues; frames and UART bytes stop advancing after the current frame. |

The disconnected RX input can produce a UART error instead of a timeout. Such an outcome can
establish detection of an unsuccessful run, but it does not independently identify the electrical
cause. Persistently incoherent samples, image mismatches, missing probes or unchanged timer
counters leave the phase inconclusive; do not report them as a firmware pass.

## MCP observation command

Run from the repository with the preinstalled dependencies and configured native runtime.
Use a new private output directory for each phase; repeat with a new directory for recovery
and pause. The plan contains a private probe identifier and is absent from public distributions.
Other users must supply their own previously obtained matching plan/profile.

```bash
source .praxis-output/podman-env.sh
.venv/bin/python tools/check_firmware_telemetry_mcp.py \
  --artifact c192a736ed2958697e4c89022094ae3b896b01529c8f391e074068c1c2c71688 \
  --probe-from-plan .praxis-output/uart-telemetry-prepare-02/plan.json \
  --output .praxis-output/telemetry-negative-NEW \
  --samples 5 --interval-ms 1000
```

The client initializes a new MCP session, discovers tools, obtains the build profile, lists probes,
inspects the selected target, obtains a plan and reads telemetry. Planning does not perform an
erase or program operation. The client never calls build, flash, halt, reset or resume tools.

```mermaid
sequenceDiagram
    participant U as User
    participant C as Test client
    participant M as Praxis MCP
    participant B as Board
    U->>B: All power off; remove loopback; reconnect
    U->>B: Press/release USER
    C->>M: Inspect selected target; plan installed artifact
    C->>M: Read coherent artifact-bound telemetry
    M-->>C: Actual failure state and timer/frame deltas
    U->>B: All power off; restore loopback; reconnect
    U->>B: Press/release USER
    C->>M: Fresh inspection and telemetry session
    M-->>C: Frame progress, errors and success indicator
    U->>B: Press/release USER to pause
    C->>M: Read telemetry
    M-->>C: Paused frame counters; continuing timer
```

## Evidence and remaining qualification

Recompute phase acceptance with `praxis qualify-telemetry`; see
[the command, acceptance rules and sequence](../peripheral-modes.md#deterministic-observation-qualification).
The offline checker rejects failed/mixed windows rather than relying on saved pass flags.

Keep raw tool responses private. Publish sanitized artifact/bundle hashes, phase labels, actual
counter deltas, failure reasons, consistency results and image checks. Record user-reported
wiring/button actions separately from firmware observations. Do not compare counter deltas
across a power cycle; each phase is a separate observation window.

These checks establish scoped, firmware-reported failure/recovery behavior. They do not establish
independent wire capture, accurate oscillator timing, complete peripheral support, standalone
debugger qualification or independent engineering review. See [publication readiness](../PUBLICATION_READINESS.md).
