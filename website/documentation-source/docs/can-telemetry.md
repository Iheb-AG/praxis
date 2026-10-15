# Artifact-bound CAN observation and qualification

Praxis can now read the CAN1 internal-loopback example through the existing
`read_firmware_telemetry` MCP tool. Select `can-loopback-v1` explicitly when
launching the build/hardware server. The default remains `uart-loopback-v1` for
existing clients. The knowledge bundle and its 24 mode contracts are unchanged;
this increment strengthens Milestone 4 observation and qualification.

Physical attempt, 2026-10-12: the approved image passed flashing, exact readback
and reset/run, but two live observation windows reported `init_timeout` with no
CAN interrupt or payload receipt. **The CAN application test failed.** See the
[full results and read-only diagnosis](reports/can-loopback-results.md). The
first image's one-shot programming/control scope was consumed. The subsequent
[RX candidate](reports/can-rx-results.md) replaced it after fresh approval and
passed scoped internal-loopback qualification; repeatability remains open.

The [telemetry application](../examples/stm32f407g-disc1-can/telemetry_application/main.c)
uses byte-identical copies of the previously reviewed controller and clock
helpers. Its MMIO adapter records the four actual FIFO words read by the ISR.
After the one-shot attempt, main masks interrupts, snapshots diagnostics and
cleanup state, then repeatedly publishes that fixed result with a software
publication counter. It performs no further CAN transactions or automatic
recovery. Busy-loop publication spacing is not a clock measurement. Internal
silent loopback requires no extra wiring or button press.

The new image was built and revalidated through an actual sixteen-call
knowledge/build MCP replay. The telemetry endpoint was also exercised through
real stdio MCP using a **fixture probe/backend**. Actual OpenOCD Tcl tests use
modeled memory and exercise identity, image and consistency failures for both
ABIs. None of those fixtures establish physical interrupt delivery. See
[recorded development evidence](can-telemetry-evidence.json) for current physical
preflight status and exact artifact identity.

## Fixed software ABI

`praxis_can_telemetry` is a global, aligned 92-byte object in allocated writable
main-SRAM `.bss`, below the reserved stack. It contains 23 little-endian uint32
words. Magic is `0x50524331`, ABI version is 1. The
[C publisher](../examples/stm32f407g-disc1-can/telemetry_application/telemetry.h)
and [Python decoder](../praxis/can_telemetry.py) agree on this order:

| Words | Meaning |
| --- | --- |
| generation, magic, abi, size_bytes | Seqlock and fixed format identity |
| publications | Main-loop publication counter; not elapsed time |
| phase, status | Boot/passed/failed and scoped controller result |
| flags | Clock complete, configured, TX requested, ISR received, reset required, source disabled, line disabled, global IRQ masked: bits 0–7 |
| clock_step, irq_count | Clock sequence terminal step and CAN FIFO0 handler count |
| rx_words_read_mask | Bits 0–3 record identifier, length, low-data and high-data reads |
| rx_identifier, rx_length, rx_low, rx_high | Actual saved FIFO words from the MMIO adapter |
| last_esr, last_tsr, last_rf0 | Controller's last checked diagnostic/progress snapshot, before successful TX acknowledgement |
| expected_identifier, expected_low, expected_high | Fixed standard ID 0x123 and bytes `50 52 41 58 49 53 00 FF` |
| end_ier, end_irq_enabled | Final source and NVIC enable snapshots |

The reader resolves only the launch-selected contract's symbol. The two ABIs
have distinct symbols and magic values even though their record sizes coincide.
It cannot select an ABI, address, expression or artifact per tool call. A
wrong-contract ELF is rejected during server launch. Every observation still
requires a valid fixed artifact, selected probe/UID, backend identity, exclusive
probe lock and exact flash-byte checks before and after bounded coherent reads.
There is no halt/reset/write fallback. See [shared reader controls](firmware-telemetry.md).

## Acceptance logic

`praxis qualify-can` works offline. It recomputes labels and checks from raw words;
a saved assessment or a Markdown claim cannot promote a failed sample. A success
window needs 2–5 coherent samples with increasing publication counts, matching
generation deltas and an unchanged terminal result. It requires:

- Matching artifact, bundle, CAN ABI, image identities and reported image checks.
- Running CPU state, passed phase/status, all eight state/cleanup flags and clock completion.
- Actual interrupt receipt and all four FIFO reads.
- Correct standard identifier, data length, filter index and complete eight-byte payload.
- Saved RQCP0/TXOK0/TME0 completion and no saved CAN/FIFO errors.
- Disabled owned peripheral interrupt source and CAN1 RX0 NVIC line.

The `--expect failed` option qualifies a stable, freshly published failure report;
it does not call a failed transaction successful. Multiple windows must retain
the same image and terminal result, with ordered publication progress across
boundaries. Repeated stale windows, intermediate failures and backward counters
remain failures. Uint32 rollover is supported within bounded positive deltas;
there is no boot-unique identity, so some resets can mimic rollover.

```mermaid
sequenceDiagram
    participant F as CAN firmware
    participant M as Build/hardware MCP
    participant D as Pinned OpenOCD
    participant Q as Offline qualifier
    F->>F: Configure clocks and CAN; submit one frame
    F->>F: ISR validates payload, releases FIFO, disables owned IRQ
    F->>F: Require TX completion; snapshot terminal result
    loop Software publication loop
        F->>F: Odd generation, copy result, even generation
    end
    M->>D: Check selected UID and exact image
    D->>F: Read generation and duplicate complete CAN records
    D->>F: Recheck generation and exact image
    M-->>Q: Raw ABI samples and artifact/bundle identities
    Q->>Q: Recompute payload, ISR, completion, cleanup and freshness checks
    Q-->>M: Recorded self-report qualification with explicit limits
```

## Reproduce

Build `stm32f407g-disc1-can/telemetry_application` through the matching knowledge
and build MCP; [the example](../examples/stm32f407g-disc1-can/README.md) describes
the source review and scope. Validate the returned artifact before launching:

```bash
praxis build-serve \
  --bundle /absolute/path/bundles/stm32f407g-disc1-e01-can-v1 \
  --assets /absolute/path/assets/stm32f407vg \
  --workspace /absolute/path/examples \
  --artifacts /absolute/path/.praxis-output/firmware-artifacts \
  --lock /absolute/path/toolchain-f407.lock.json \
  --hardware-profile /absolute/path/hardware-profile-can.json \
  --telemetry-artifact ARTIFACT_ID --telemetry-kind can-loopback-v1
```

Without a hardware authorization file, programming/control tools are absent.
The [OpenCode example](../examples/opencode.can-telemetry.example.json) shows the
same launch. Replace every absolute-path and artifact placeholder. A hardware
profile must bind the current bundle/assets and installed backend.

For the CAN kind, `read_can_diagnostics(connection_id)` additionally returns a
single ABI sample and named CAN1 MCR/MSR state after exact-image checks. It reads
CAN registers only when the CAN1 gate is enabled; BTR requires INAK=1. Equal gate
snapshots bracket those reads. The allowlist is checked against the selected
CAN/RCC Markdown and exposes no caller-selected register/address. One sample
cannot establish publication progress or qualify a result window.

```bash
python tools/check_firmware_telemetry_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-can-v1 \
  --hardware-profile /absolute/path/hardware-profile-can.json \
  --telemetry-kind can-loopback-v1 --artifact ARTIFACT_ID \
  --probe-serial YOUR_SELECTED_SERIAL \
  --samples 5 --interval-ms 1000 --output /new/private/can-observation

praxis qualify-can --bundle bundles/stm32f407g-disc1-e01-can-v1 \
  --artifact ARTIFACT_ID \
  --observation /new/private/can-observation/observation-00.json \
  --output /new/private/can-qualification.json
```

Before installation, adding `--expect-mismatch` to the reader tests rejection of
an older installed image. The reader saves a read-only programming plan; it never
authorizes, flashes or resets. Installation requires separate approval for the
exact new image and erase range, enforced by Praxis's existing programming scope.

For a diagnostic-only capture, add `--can-diagnostics` to the reader command.
The returned `can_state` is a sequential live snapshot, not a trace or an
independent explanation of an earlier failure. The reader requests no writes,
FIFO releases, W1C actions or execution control.

Next: investigate the captured initialization-exit timeout through MCP, establish
any board-specific RX prerequisite, extend the model and validate a revised
candidate before requesting fresh exact-image approval. External CAN interoperability,
physical timing, repeatability and independent hardware review remain open.
