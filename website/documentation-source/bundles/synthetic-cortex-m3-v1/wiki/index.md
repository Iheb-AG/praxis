# Project Praxis hardware execution index

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

## Hardware Execution Dependency Graph

Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.

- [[peripherals/clock]] requires [[index]]
- [[peripherals/pins]] requires [[peripherals/clock]]
- [[peripherals/uart]] requires [[peripherals/pins]]
- [[peripherals/interrupts]] requires [[peripherals/uart]]

Read this index first. Retrieve the matching net, then follow every stage in order. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- Fictional fixed 12 MHz clock. No manufactured MCU or board is represented.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.

## Extraction scope

Adapter: `cmsis_cortex_m`; declared CPU: `cortex-m3` (source: `profile:target.knowledge_adapter`). Header identity checks: `PRAXIS_DEMO_M3_H`, `PRAXIS_DEMO_PART`. This is a knowledge-only target. No target firmware assets, sandbox compiler profile, flashing or physical qualification are supplied by this adapter. Clock assumptions and HEDG edges are explicit profile policy, not inferred from a diagram.

## Peripheral coverage

CMSIS register types and configured instances; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

| Entity | Structure | Instances | Status | Registers | Fields | Reviewed registers | Requires | Issues | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clock | CLOCK_Type | CLOCK0 | declarations_only | 1 | 1 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | vendor_blocks:CLOCK_Type |
| interrupts | IRQCTRL_Type | IRQCTRL0 | declarations_only | 1 | 1 | 0 | uart | Enclosing masks represent contained aliases; absent masks remain unasserted. | vendor_blocks:IRQCTRL_Type |
| pins | PINMUX_Type | PINMUX0 | declarations_only | 1 | 1 | 0 | clock | Enclosing masks represent contained aliases; absent masks remain unasserted. | vendor_blocks:PINMUX_Type |
| uart | UART_Type | UART0 | declarations_only | 2 | 1 | 0 | pins | Enclosing masks represent contained aliases; absent masks remain unasserted. | vendor_blocks:UART_Type |

## Workflow readiness

| Workflow | Ready | Required | Dependency closure | Missing evidence |
| --- | --- | --- | --- | --- |
| uart_polling | False | False | clock, pins, uart | clock: operating semantics not reviewed; clock: specify workflow register requirements before claiming readiness; pins: operating semantics not reviewed; pins: specify workflow register requirements before claiming readiness; uart.CTRL: access/operating semantics unreviewed; uart.DATA: access/operating semantics unreviewed; uart: operating semantics not reviewed |

- Reviewed subsets do not establish support for every mode or instance.
- Unreviewed declarations must not be used as initialization guidance.
- Header absence does not prove that silicon lacks a capability.
- Package availability, routing, timing and physical tests remain separate evidence.

Complete source hashes, versions and origins: [[sources]].

See [[coverage]] and [[sources]].

## Mode-specific support

See [[features]] for instance-scoped operating contracts. Header coverage does not establish complete MCU feature support.

| Entity | Reviewed mode | Instances |
| --- | --- | --- |

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.
