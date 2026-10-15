# Coverage report

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

## Machine-readable report

```json
{"counts":{"blocked":0,"fields":4,"published":4,"register_blocks":4,"registers":5,"reviewed_subsets":0,"unmapped_types":0},"extractor_versions":{"arm-none-eabi-gcc":"arm-none-eabi-gcc (Arch Repository) 16.2.0","clang":"clang version 23.1.1","cmsis-discovery":"v1; Clang layouts and restricted object-macro evaluation","libclang":"18.1.1","netlist":"KiCad XML adapter v1 (pre-exported source)","praxis":"0.1.0"},"format":"praxis-coverage-v1","limits":["Reviewed subsets do not establish support for every mode or instance.","Unreviewed declarations must not be used as initialization guidance.","Header absence does not prove that silicon lacks a capability.","Package availability, routing, timing and physical tests remain separate evidence."],"peripherals":{"clock":{"bytes_limit":65536,"fields":1,"instances":["CLOCK0"],"issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"prerequisites":[],"provenance":"vendor_blocks:CLOCK_Type","published":true,"registers":1,"reviewed_modes":{},"reviewed_registers":0,"selected":true,"status":"declarations_only","structure":"CLOCK_Type","unresolved_masks":[]},"interrupts":{"bytes_limit":65536,"fields":1,"instances":["IRQCTRL0"],"issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"prerequisites":["uart"],"provenance":"vendor_blocks:IRQCTRL_Type","published":true,"registers":1,"reviewed_modes":{},"reviewed_registers":0,"selected":true,"status":"declarations_only","structure":"IRQCTRL_Type","unresolved_masks":[]},"pins":{"bytes_limit":65536,"fields":1,"instances":["PINMUX0"],"issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"prerequisites":["clock"],"provenance":"vendor_blocks:PINMUX_Type","published":true,"registers":1,"reviewed_modes":{},"reviewed_registers":0,"selected":true,"status":"declarations_only","structure":"PINMUX_Type","unresolved_masks":[]},"uart":{"bytes_limit":65536,"fields":1,"instances":["UART0"],"issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"prerequisites":["pins"],"provenance":"vendor_blocks:UART_Type","published":true,"registers":2,"reviewed_modes":{},"reviewed_registers":0,"selected":true,"status":"declarations_only","structure":"UART_Type","unresolved_masks":[]}},"publication_ready":true,"scope":"CMSIS register types and configured instances; not every MCU capability or board connection","source_catalog":"[[sources]]","sources":{"profile":{"sha256":"df9855c1fdad1671abf293f3465fa62e8255f58cc64bfbf72475684bd8ad7d48","version":"1"}},"sources_scope":"Selected profile only; complete source hashes and versions in source_catalog and manifest","target":"synthetic_cortex_m3","workflows":{"uart_polling":{"closure":["clock","pins","uart"],"instance_scope":{"uart":["UART0"]},"issues":["clock: operating semantics not reviewed","clock: specify workflow register requirements before claiming readiness","pins: operating semantics not reviewed","pins: specify workflow register requirements before claiming readiness","uart.CTRL: access/operating semantics unreviewed","uart.DATA: access/operating semantics unreviewed","uart: operating semantics not reviewed"],"mode_scope":{},"ready":false,"required_for_publication":false,"required_signals":[]}}}
```
