# CAN1 internal-loopback physical attempt

Date: 2026-10-12. Target: STM32F407VGT6 on the user's STM32F407G-DISC1;
MB997-E-01 is the reference revision, not a confirmed physical PCB revision.

**Programming succeeded; the CAN application test failed.** The result is
retained as failed physical evidence. No interrupt-driven CAN transfer has been
demonstrated by this run.

Historical snapshot: this report describes the failed first image. The
[subsequent RX candidate](can-rx-results.md) replaced it after fresh user approval
and passed scoped internal-loopback qualification. Its success does not erase
this failed result or establish an isolated causal explanation.

## Approved image and programming

| Item | Recorded result |
| --- | --- |
| Artifact | `02474f0ac4cdab793ec3baf1f1ee496daefafcfb54ff262e0ffa4c4323e02eb4` |
| Image SHA-256 | `4a2170686b5d1a896f165ce2d9b2a325219d23d754416d109141f99b87064f6f` |
| Bundle revision | `c16f763c075ac70682f8fda1bc64d012397c733feb156213707d691781b4f5d4` |
| Programmed / verified | All 4,524 image bytes |
| Erased | Sector 0 only: `0x08000000–0x08003FFF`, 16 KiB |
| Flash completion | Success, exact readback, halted |
| Reset/run | Success, exact readback, running |
| Scope consumption | One flash attempt and one reset/run attempt; both consumed |

The user explicitly approved this image and erase range before the operator
scope was provisioned. Actual MCP calls performed knowledge retrieval, artifact
validation, target inspection, refreshed planning, flashing and reset/run.
Persistent reservation/result records agree with the returned operations. Raw
scope, probe/UID and backend logs remain private. The previous UART application
has been replaced by the CAN telemetry image. No programming retry or additional
execution control occurred.

## Captured CAN result

Two actual MCP observation windows each returned five coherent samples.
Every window was bracketed by exact-image comparisons and reported a running
CPU. The terminal result was identical across all ten samples:

| Field | Result |
| --- | --- |
| Application phase / status | `failed` / `init_timeout` (status 3) |
| Clock sequence | Completed, step 24 |
| CAN IRQ count | 0 |
| FIFO words read | None; read mask 0 |
| RX identifier and payload words | 0; no receipt established |
| Last saved ESR / RF0R | 0 / 0 |
| Last saved TSR | `0x1C000000`: mailbox-empty state, no successful completion |
| Final IER / NVIC enable snapshot | 0 / 0 |
| Flags | `0xF1`: clock complete, reset required, source/line disabled, global interrupts masked |
| Publication progress, window 1 | 138 → 159 |
| Publication progress, window 2 | 162 → 184 |

Offline `qualify-can --expect passed` rejected both windows. The separately
requested `--expect failed` qualification accepted the stable, freshly published
failure report. That establishes observation of failure, not a successful CAN
transaction. Zero saved CAN error flags do not establish a healthy bus when no
transaction was started.

## Read-only diagnosis

The first ABI reports the same timeout code for initialization entry and exit.
To investigate without another flash, the optional CAN telemetry MCP now exposes
`read_can_diagnostics(connection_id)`. It permits only named, clock-gated CAN1
MCR/MSR reads; BTR is read only while INAK is set. Register layout is checked
against the selected immutable Markdown. Exact UID/image checks, backend/probe
guards and duplicate coherent ABI reads remain in place. There are no caller
addresses, FIFO actions, W1C operations, halt/reset commands or writes.

The actual MCP response reported:

| Live snapshot | Value / interpretation |
| --- | --- |
| RCC APB1ENR, before and after | `0x12000000`; CAN1 clock enabled, gate snapshot unchanged |
| CAN1 MCR | `0x00010018`; INRQ=0 and SLEEP=0 |
| CAN1 MSR | `0x00000009`; INAK=1, SLAK=0, RX signal low |
| CAN1 BTR | `0xC01A0005`; requested silent-loopback/timing value present |

This snapshot is consistent with initialization exit remaining unacknowledged.
It is sequential evidence captured after the timeout, not a trace of the earlier
transition. Cached RM0090 pages were re-read through the ingestion MCP: the
manual describes an 11-recessive-bit synchronization requirement for mode exit
and CANRX isolation in combined silent/loopback operation. The interaction with
initial synchronization and the low RX signal needs further source-backed
investigation. **A required RX routing/pull configuration is a hypothesis; its
causal role has not been demonstrated.** No board-specific CAN pin or transceiver
has been inferred or programmed as a fallback.

```mermaid
sequenceDiagram
    actor U as User
    participant M as Praxis MCP
    participant B as Selected board
    participant Q as Offline qualifier
    U->>M: Approve exact image and sector-0 erase
    M->>B: Flash once and verify all 4,524 bytes
    M->>B: Approved reset/run once
    B->>B: Clock setup completes; CAN init wait expires
    loop Two observation windows
        M->>B: Verify exact image, read coherent ABI, reverify image
        B-->>M: Stable init_timeout; publication counter advances
    end
    M->>Q: Raw samples, exact artifact and bundle identities
    Q-->>M: Success rejected; expected failure report qualified
    M->>B: Exact-image-bound named CAN mode/status reads
    B-->>M: INRQ=0, INAK=1, RX low, expected BTR
```

## State and next work at the end of this attempt

The board remains running this image's terminal failure-publication loop, with
global interrupts masked and no automatic CAN retry. This software observation
does not establish optical output, physical timing, external CAN interoperability
or repeatability. Physical PCB/silicon revision and errata qualification remain
open. Independent release review and live KiCad checks remain blockers.

Next: use MCP to establish any initialization-side RX prerequisite and its exact
board routing, extend the effect model for that condition, then build and review
a revised candidate. Any changed image or additional reset/run needs fresh
exact-image approval because this run's budgets are consumed. Preserve this
failed run alongside any later success. See [sanitized evidence](../can-telemetry-evidence.json)
and [the observation contract](../can-telemetry.md).
