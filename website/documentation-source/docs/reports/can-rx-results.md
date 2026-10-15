# CAN RX candidate: physical internal-loopback result

Date: 2026-10-12. Target: STM32F407VGT6 on the user's STM32F407G-DISC1.
MB997-E-01 remains the documented reference; the physical PCB revision is
unconfirmed. The user approved the exact candidate and confirmed P2:34 was
externally unconnected before the operation.

**The single approved flash, exact readback and reset/run passed. Two fresh
observation windows passed internal-loopback self-report qualification.** This
result supersedes the installed image from the [failed first run](can-loopback-results.md),
which remains preserved as historical evidence.

## Exact scope and execution

| Item | Result |
| --- | --- |
| Artifact | `1f4413a435cfae5cee4ecbc500e56dc1bed56fc434642aafe5b818ba67b09b9c` |
| Image SHA-256 | `40fa85839117db8c2b36c324dd32eadf804d11711e017e1f8d1a0301efdbb494` |
| Bundle revision | `123a65450d9ff6849c1368aa595f9f575d8da71d740cdb68dcaa42cfc4e41a93` |
| Programmed and exactly verified | All 4,920 image bytes |
| Erased | Sector0 only, `0x08000000–0x08003FFF`, 16 KiB |
| Flash completion | Success, exact readback, halted |
| Reset/run | Success, exact image checked, running |
| Operator scope | One flash and one reset/run attempt, both consumed |

Knowledge retrieval, artifact revalidation, target inspection, refreshed planning,
programming, execution and observation used actual stdio MCP. Persistent result
records match the responses. There was no additional flash, reset, abort, drain or
firmware retry. The candidate runs its one-shot transaction and then publishes
the terminal result repeatedly. Raw probe/UID, grants, backend output and
observation files stay private.

## Observations and qualification

Initial observations at requested250ms spacing already reported the successful
terminal transaction, but repeated publication counters prevented freshness
qualification. `qualify-can` rejected these windows. They remain retained;
payload success was not used to bypass the freshness check.

Read-only MCP then collected two further five-sample windows at requested1000ms
spacing from the **same running image**, without changing the firmware. Every
window was bracketed by exact-image comparisons. Offline qualification recomputed
the result from raw ABI words and accepted both fresh windows together.

| Field | Stable result in all ten fresh samples |
| --- | --- |
| Application phase/status | `passed` / `ok` (status0) |
| Clock sequence | Completed, step24 |
| CAN1 RX0 interrupt count | 1 |
| FIFO words read | All four, mask `0xF` |
| Received standard identifier | `0x123` (raw identifier word `0x24600000`) |
| Data length | 8 |
| Payload | `50 52 41 58 49 53 00 FF` |
| Saved ESR/RF0R | `0` / `0` |
| Saved TSR | `0x1C000003`: requested mailbox completion, TXOK and empty state |
| Final IER/NVIC enable snapshot | `0` / `0` |
| Flags | `0xFF`: clock, configure, request, ISR, reset-required and cleanup flags |
| Window1 publication counters | `211, 213, 214, 216, 217` |
| Window2 publication counters | `218, 220, 221, 223, 224` |
| Window1 seqlock generations | `422, 426, 428, 432, 434` |
| Window2 seqlock generations | `436, 440, 442, 446, 448` |

The counters record repeated publication of **one** transaction result; these
are not ten separate CAN transactions. The previous RX synchronization
hypothesis is consistent with this success, but this is not an isolated causal
experiment. See the [source-to-model-to-build follow-up](../can-rx-followup.md)
and [sanitized evidence](../can-rx-evidence.json).

```mermaid
sequenceDiagram
    actor U as User
    participant M as Praxis MCP
    participant B as Selected board
    participant Q as Offline qualifier
    U->>M: Approve exact image and confirm P2:34 unconnected
    M->>B: Program once; verify all 4,920 bytes
    M->>B: Approved reset/run once
    B->>B: Establish RX input; require real init acknowledgements
    B->>B: Transmit internally; receive IRQ; verify payload; clean up
    M->>B: First short-spaced coherent observations
    M->>Q: Raw ABI windows
    Q-->>M: Reject repeated heartbeat counters
    M->>B: Two longer-spaced read-only windows; unchanged image
    M->>Q: Raw ABI windows with advancing generations/publications
    Q-->>M: Accept scoped internal-loopback self-report
```

## Limits and next work

This run establishes artifact-bound observation of a successful internal CAN
transaction and interrupt handler. It does not independently measure bit timing,
prove physical GPIO electrical behavior, qualify an external transceiver/bus or
establish repeatability. No boot-unique identity exists in this ABI. Source review
was by the implementing author; independent engineering review remains open.

The installed image remains in its terminal success-publication loop, with owned
interrupts disabled and no automatic transaction retry. The consumed scope cannot
authorize another reset. Next: add a source-backed, explicitly scoped verification
workflow for the next blocked capability; repeated physical starts require their
own concrete execution plan and approval. Qualified v1 also still requires KiCad
checks, independent review and resolution of earlier UART repeatability anomalies.
