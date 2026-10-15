# Paired timer physical trial — 2026-10-15

**All three scoped phases passed** through actual Praxis MCP calls on the operator's
STM32F407G-DISC1: wired PWM/capture success, clean timeout after unpowered jumper
removal, and a successful new boot after restoration. The physical PCB revision is
still unconfirmed; the knowledge reference is MB997-E-01.

The explicitly approved image was flashed once, all 4,424 bytes verified, then
reset/run once. Only sector 0 (0x08000000–0x08003FFF, 16 KiB) was erased. No programming
or execution-control retry occurred. Later phase changes used operator power cycles;
no additional MCP flash/reset/halt/write was requested.

| Identity | Value |
| --- | --- |
| Artifact | `ba3ff2fcb1e2b2083af0849bdef3135f19d6bb04fca70184d13bb4e6106c246a` |
| Image SHA-256 | `4c3ae24a5c68b25aa1a2b258d7e4ac7c935a6bda9adcec1375b5caff2d026ec2` |
| Bundle revision | `2dbfa901ec294c0f8edc5e37e87d41a3aa69f169dcce18b4acf088d48f5c0167` |
| Wiring | Passive PA1/P1-11 ↔ PA2/P1-14; user verified labels/orientation and unpowered changes |
| Functions | TIM2 CH2 PWM1 output / TIM5 CH3 direct rising capture, polling |

## Actual results

| Phase | Reported phase/status | Valid periods | Stored timestamps | Relative period ticks | Qualification |
| --- | --- | --- | --- | --- | --- |
| Wired success | passed / ok | 8 | 9 | 1000 each | Passed |
| Jumper removed | failed / timeout | 0 | 0 | No stored captures | Passed |
| Wired recovery | passed / ok | 8 | 9 | 1000 each | Passed |

Each phase has two three-sample windows: six windows and 18 samples total.
Complete image verification brackets every window, and the target/artifact plan
matches across all three boots. Across preflight/execution/negative/recovery there
were 25 actual MCP calls: 23 read-only calls, one flash and one reset/run.

The initial wired timestamps were `1009, 2009, 3009, 4009, 5009, 6009, 7009, 8009, 9009`.
All eight differences are 1,000 local timer ticks. Publication counts advanced
7→11→15 and 18→22→26 while that one-shot terminal result stayed stable. Recovery
again produced eight 1,000-tick periods; its first window advanced 61→65→69.

With the jumper removed, both windows reported phase=failed, status=timeout,
zero stored captures and zero validated periods. Expected-timeout qualification
passed; success qualification correctly rejected the same real observations.
The timeout latch was preserved. Restoring the jumper required a new power-up,
not an automatic firmware retry, and the recovery result passed independently.
Windows across different power cycles were qualified separately, never concatenated.

All phases report complete readable shutdown snapshots: both timers' CR1/CCER/DIER
are zero and the two owned pin MODER fields are input. Flags 11 mean quiet timers/pins
and masked IRQs on success; flags 15 additionally preserve the failure latch on timeout.
The preflash exact-image mismatch guard also correctly refused candidate SRAM sampling.
Raw probe/UID/authorization logs remain private; the public evidence contains sanitized
raw timestamp records, reported image checks and recomputed qualifications.

## Sequence

```mermaid
sequenceDiagram
    participant Operator
    participant MCP as Praxis MCP
    participant Board
    participant Qualifier
    Operator->>MCP: Approve exact image, sector0 erase and one reset/run
    MCP->>Board: Flash once, verify every image byte, reset/run once
    MCP->>Board: Read two coherent windows with image checks
    MCP->>Qualifier: Wired raw timestamps
    Qualifier-->>MCP: Eight valid periods and quiet shutdown
    Operator->>Board: Remove jumper unpowered; reconnect
    MCP->>Board: Read two new-boot windows, no writes
    MCP->>Qualifier: Timeout records
    Qualifier-->>MCP: Clean timeout passes; success expectation fails
    Operator->>Board: Restore jumper unpowered; reconnect
    MCP->>Board: Read two recovery windows, no writes
    MCP->>Qualifier: Recovery raw timestamps
    Qualifier-->>MCP: Eight valid periods and quiet shutdown
```

## What this establishes

This is one artifact-bound, operator-assisted physical trial of a specific polling
PWM/capture route. Firmware-reported input capture values and shutdown evidence
match the source-backed recipe under deliberate wire removal and recovery.
It is not independent calibrated frequency/duty measurement, statistical repeatability,
32-bit hardware-wrap testing, timer IRQ/DMA support, arbitrary firmware correctness
or full MCU acceptance. Both timers share HSI. A no-edge timeout cannot identify
its physical cause by itself. Heartbeat progress republishes a terminal result;
it does not rerun the loopback. Physical PCB revision and independent release review
remain open. Historical model/build-only evidence is retained separately.

Next: source-backed, instance-scoped timer capture interrupts, ISR/overcapture/cleanup
failure models and isolated builds, followed by separately approved physical testing.
DMA, other timer modes and the remaining F407 inventory follow their own contracts.

See [sanitized raw observations and qualification](../timer-route-physical-evidence.json)
and [ABI, algorithm and procedure](../timer-observations.md).
