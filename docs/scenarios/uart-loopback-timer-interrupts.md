# UART loopback, timer and external-interrupt scenario

Status, 2026-10-11: **implemented, compiled and flashed through MCP; loopback, pause, failure and recovery confirmed by the user**.
The user authorized an ingestion MCP after the original 44-call readiness replay failed.
It supplied complete source evidence and schematic images for a separately reviewed/published
UART/TIM2/EXTI bundle. The matching knowledge/build pair then passed 23 readiness calls.
The application passed host checks, actual isolated full linking, ELF/vector validation and
read-only board planning. After explicit approval, one MCP flash passed exact readback and
one reset/run reported running. Both attempt budgets are consumed. On 2026-10-11 the user confirmed
positive-loopback LED behavior, pause, jumper-removed failure and restored-jumper recovery.
Measured timing, packet capture, held-button behavior and repetition count remain unverified.
See [actual results](../reports/uart-loopback-results.md) and the
[ingestion sequence](../ingestion-mcp.md). The original
[failed replay](../reports/uart-readiness-before-ingestion.md) is preserved.

## Purpose and available equipment

Use the STM32F407G-DISC1, its ST-LINK USB connection and one jumper wire. The user has jumper
wires only. A USB-to-UART adapter is not required for this local loopback test. It tests one UART's
TX/RX electrical path and interrupt-driven handling; it does not establish interoperability with
a PC, another device, RS-232, RS-485, USB CDC or a network protocol.

For the reference board, ST documents USART2 TX at PA2/P1 pin 14 and RX at PA3/P1 pin 13 in
[UM1472 Rev 9 section 7.3.3 and Table 7](https://www.st.com/resource/en/user_manual/dm00039084-discovery-kit-with-stm32f407vg-mcu-stmicroelectronics.pdf).
After verifying the actual board connector identity/orientation, connect **P1-14 to P1-13** with
the board unpowered. This wire joins two signal pins on the same board; do not connect it to a
power pin. ST-LINK USB remains the programming/debug connection. Its VCP is not connected to the
application UART by default, and this scenario does not modify ST-LINK wiring or solder bridges.
The user's physical PCB revision remains unknown; the published bundle must retain that limitation.

## Application specification

Use bare-metal C with the approved startup/linker/system assets. Establish nominal HSI 16 MHz
with explicit bus divisors; derive UART baud and TIM2 timing from the resulting verified clock
tree. Do not copy the earlier bundle's 42 MHz PCLK1 baud constant into this clock configuration.
Use USART2 at nominal 115200 baud, 8N1. Target timing is approximate unless measured externally.

| Facility | Required behavior |
| --- | --- |
| TIM2 update interrupt | 1 ms software time base; bounded ISR increments a counter and returns |
| USART2 interrupt | Receive bytes into a bounded ring buffer; service an interrupt-driven TX queue; count hardware errors and overflow |
| PA0/USER external interrupt | Capture button edges through the correct SYSCFG/EXTI route; debounce for 50 ms outside the ISR; act only on a qualified press |
| Green LD4 / LED_A | Change state every 500 ms independently of UART success, pause or failure |
| Orange LD3 / LED_B | Pulse for 30 ms after each completely validated received frame |
| Blue LD6 | Latch on after 100 consecutive valid frames; clear when a new run starts or a failure occurs |
| Red LD5 | Latch on after a timeout, CRC/payload/sequence error, UART error or queue overflow; clear only on an explicit new run |

Start paused, with only the heartbeat active. Each debounced button press switches RUNNING to
PAUSED or starts a fresh run from PAUSED/FAILED. Pausing stops new transmissions, drains any
in-flight frame with a bounded deadline, then disables test deadlines. Retain the completed
run's blue/red result until the next start. A failure stops new transmissions but leaves the
heartbeat responsive. Button release rearms the next press and must not start another run.
Allow only one frame in flight. The interval between frame starts is at least 100 ms, and each
frame must complete within 250 ms; do not build an unbounded catch-up backlog after a pause.

### Loopback framing

Each frame is 19 bytes:

| Bytes | Meaning |
| --- | --- |
| 0–1 | Synchronization bytes `A5 5A` |
| 2 | Version `01` |
| 3 | Message type `01` (test frame) |
| 4–7 | Unsigned sequence number, little-endian |
| 8 | Payload length `08` |
| 9–16 | Eight deterministic payload bytes derived from the sequence |
| 17–18 | CRC-16, most-significant byte first, covering bytes 2–16 |

Specify CRC parameters as polynomial `0x1021`, initial value `0xFFFF`, no input/output reflection,
and final XOR `0x0000`. Define the payload generator and sequence wrap behavior in the application
contract. Compare the received frame with the outstanding expected sequence and payload, not just
with its CRC. The receiver consumes the returned packet; it never echoes it again. The main loop
parses and checks frames, schedules work and updates LEDs. ISRs must not format logs, calculate
whole-frame CRCs, delay, allocate memory or wait for another interrupt. Keep shared state/ring
ownership and overflow handling explicit; `volatile` alone is not a synchronization design.

## Knowledge readiness gate

The separate `stm32f407g-disc1-e01-uart-v1` bundle now publishes PA2/PA3 connector nets,
reviewed TIM2 update semantics, SYSCFG/EXTI0 routing and expanded USART2 interrupt handling.
Canonical timer identity is `tim`, alias `tim2`. NVIC requires USART, TIM and EXTI prerequisites.
The prior default bundles and launchers remain unchanged. Select the same new revision for
knowledge, build and hardware profiles; old artifact authorization does not apply.
The publication includes source locators and complete declaration tables within64 KiB,
while unsupported modes remain unreviewed. See the actual readiness response evidence above.

The dependency graph must require clock and pin routing before UART, timer and external-event
configuration. Configure/clear each interrupt source and initialize its handler state before
enabling that source and its NVIC line; restore global interrupts last. Resolve the real IRQs
and vector slots from the reviewed bundle and approved startup, rather than remembering them.

## Verification and physical procedure

1. Validate bundle provenance, links, graph, connector endpoints and register/IRQ semantics.
2. Verify protocol vectors with an independently specified CRC reference and reviewed expected
   frames. Check corruption, truncation, sequence mismatch/wrap, ring wrap/overflow and timeouts.
   Instrument fixture accessors to check source setup/clear before final interrupt enablement.
3. Cross-compile and link in the existing rootless sandbox, then validate the ELF and register
   a new content-addressed artifact. Compilation cannot establish physical UART behavior.
4. Review the exact new artifact, board identity and complete erase range; provision a fresh
   operator scope. Flash once, require exact readback and a successful halted result, then use
   authorized reset/run. Stop on any failed/uncertain programming operation.
5. With the loopback wire fitted, press USER to start. Green should continue blinking; orange
   should show received-frame activity. Blue should latch on after roughly ten seconds with no
   red error. Visual orange pulses are not an independent count of received frames.
6. Press USER to pause. Orange activity should stop after the bounded in-flight drain; green
   should continue. Holding USER must not cause repeated starts/stops. Release and press again
   to start a fresh run with result indicators cleared.
7. For the negative wiring test, pause, power off and remove the jumper. Power on, then start
   with USER. Red should latch after the receive deadline, blue remain off and green continue.
   Do not claim the exact 250 ms deadline from visual observation alone.
8. Power off, restore the jumper and start a new run. Require a fresh blue success result with
   no red error. Record actual human observations and repetitions, including unexpected behavior.

There is no existing Praxis tool for reading arbitrary application counters or driving the USER
button. LED results are firmware-reported status interpreted by a human, not an independently
captured UART trace. Do not invent counter values or claim a measured 100-frame transaction trace.
A future scoped observer can expose approved status fields or an external serial adapter can
capture packets. Current inspection tools can still record approved clock/fault/GPIO samples;
halt/resume tests additionally require applicable scope and do not by themselves prove ISR entry.

## Results contract

Record knowledge retrieval, host protocol checks, cross-compilation/ELF validation, programming,
execution control, human observations and unmeasured conditions separately. Save actual MCP run
IDs and target/artifact/bundle identities; redact full probe serial and MCU UID. Never substitute
expected LED behavior for a user answer. Successful loopback does not qualify unrelated board
revisions, DMA, a host serial connection, electrical timing tolerance or an arbitrary protocol.
