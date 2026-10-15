# CAN RX initialization candidate

This source directory targets the immutable `stm32f407g-disc1-e01-can-rx-v1`
bundle and STM32F407VGT6/LQFP100 on the MB997-E-01 documented reference board.
Physical PCB revision remains unconfirmed. It is modeled, target-built and
ELF-validated through actual MCP. A subsequent approved single flash/reset-run
and two fresh observation windows passed scoped internal-loopback self-report
qualification. See [physical results](../../docs/reports/can-rx-results.md).
External CAN and repeatability remain unqualified.

The prior physical CAN telemetry run failed initialization. This candidate
tests a source-backed RX synchronization hypothesis. It owns PD0 (U4:81,
P2:34), requires that expansion pin to be externally unconnected, enables
GPIOD, checks fresh unlocked pin configuration, applies an internal pull-up,
selects AF9 and alternate-function mode, and requires high IDR/MSR.RX samples.
No GPIO output drive, CAN TX pin, external transceiver or extra jumper is used.
All other GPIO configuration bits are preserved. A high sample alone is not
normal-entry acknowledgement; the controller still requires bounded INAK/SLAK
transitions before submitting a frame or enabling the receive interrupt.

The one-shot payload, filter, IRQ, completion, cleanup and92-byte software
telemetry ABI are inherited from the prior application. Failures publish a
terminal report and require reset; there is no autonomous retry. The route
helper's detailed failure status is not separately encoded in this ABI, so
a pre-controller failure requires scoped follow-up evidence rather than a
guessed root cause. Software publication progress is not a timing measurement.

Use the command in [the source/review/model/MCP report](../../docs/can-rx-followup.md)
to retrieve dependencies and build this directory through the pinned sandbox.
The [evidence record](../../docs/can-rx-evidence.json) identifies the exact
candidate. The approved single programming/control scope is now consumed. Any further
programming or execution control requires its own target-bound approved grant. Preserve the older
failed sources and report for comparison. After an approved run, qualify raw
observations with `praxis qualify-can`; compile success alone cannot establish
interrupt delivery or correct physical behavior.

The C/header-only build inputs remain in `telemetry_rx_application/`. This
documentation lives outside that directory so the strict source snapshot accepts
the example without filtering files or weakening sandbox input restrictions.
