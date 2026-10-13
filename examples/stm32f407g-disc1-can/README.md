# CAN1 silent-loopback/FIFO0 interrupt example

Bundle: `stm32f407g-disc1-e01-can-v1`, STM32F407VGT6/LQFP100, MB997-E-01
reference. Physical PCB/silicon revision remains unconfirmed. The base application
is source-reviewed, modeled and ARM compile/link checked and has not been flashed.
The telemetry variant was subsequently flashed, but its CAN application test
failed with `init_timeout`; see [physical results](../../docs/reports/can-loopback-results.md).
Interrupt-driven CAN operation remains physically unqualified.

The firmware performs one internal silent-loopback transaction after its owned
clock startup: nominal500kbit/s at42MHz PCLK1, standard identifier0x123, eight
bytes, transmit mailbox0, 32-bit list filter bank0 and receive FIFO0. It requires
CAN1/CAN2/shared-filter ownership and IRQ20. Both SILM and LBKM are set while
initialization is acknowledged. Combined mode disconnects CANRX internally and
holds CANTX recessive. **No external CAN jumper or transceiver is needed for this
internal workflow.** It does not configure CAN GPIO alternate functions or
qualify a real CAN network.

The main application enables FIFO0 reception interrupts after preparing handler,
software state, source and NVIC. It stages all eight bytes, requests transmission,
unmasks interrupts and waits with a finite iteration budget. The handler checks
ID/length/payload/errors, reads all FIFO words before releasing the mailbox, and
disables the owned source/line. Completion needs both valid ISR receipt and
RQCP0/TXOK0/TME0. A one-shot success, failed acknowledgement or other failure
requires reset before another transaction. No automatic abort/drain/retry occurs.

`can_controller.h` is also executed by the host effect model. The ARM ELF test
checks vector slot36 points to the real CAN1_RX0_IRQHandler. Target compilation
uses the build MCP, pinned rootless Podman image and approved startup/system/linker
assets. Main runs the self-test if this image is later programmed; building it
does not execute it on the board. The debug-visible `praxis_can_*` globals are
**not** the existing UART telemetry ABI, and its telemetry tool must not be used
to interpret them. Artifact-bound CAN observation is a next step before an MCP
physical qualification run.

The subsequent `telemetry_application` variant implements a separate fixed
`praxis_can_telemetry` ABI and captures the actual FIFO words read by the ISR.
Its controller and clock headers match this base application byte-for-byte.
Build that variant, select `--telemetry-kind can-loopback-v1`, and qualify
recorded observations with `praxis qualify-can`. See
[the CAN observation procedure](../../docs/can-telemetry.md) for the sequence,
artifact checks and approval boundary. Its first physical run is retained as failed
evidence; a revised candidate and new approval are needed for further execution.

See [architecture, sequence and evidence](../../docs/can-expansion.md) and the
[matching client configuration](../opencode.can.example.json). Existing client
selection and installed board firmware are unchanged.

Suggested MCP prompt:

```text
Test CAN1 knowledge/build readiness through MCP only. Do not access hardware or flash.
Read the wiki index and confirm stm32f407g_disc1_mb997_e01, MB997-E-01.
Require can1_silent_loopback_irq ready, with feature_can and can1_external_bus blocked.
Follow every declared prerequisite and retrieve complete CAN/RCC/NVIC/clock documents.
Explain nested mailbox field mappings, unknown mailbox resets, preserved FMR bits,
SILM+LBKM isolation, CAN1-only filters, IRQ20/vector36, literal status actions and
bounded waits. Do not infer a transceiver, external bus pins or CAN2 support.
Get the build profile and require the same bundle revision as the knowledge MCP.
Build source_directory stm32f407g-disc1-can/application and validate that exact artifact.
Write a report separating source review, model cases, ARM/ELF evidence and physical
behavior. The existing UART telemetry ABI does not decode this example's globals.
No physical interrupt delivery, external-bus operation or timing measurement is claimed.
```

The subsequent [RX initialization candidate](telemetry_rx_application/README.md)
publishes an explicit source-backed PD0 prerequisite and preserves the failed
run above. Its [follow-up report](../../docs/can-rx-followup.md) separates
software/model/MCP evidence from the subsequent approved physical test, which
passed scoped internal-loopback qualification. See
[the physical result](../../docs/reports/can-rx-results.md).
