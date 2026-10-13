# UART — declarations only

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/pins]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| UART0 | 0x40002000 | Not asserted | Not asserted | header:UART0_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTRL | 0x000 | 32 | — | unknown | 0x0 | Not asserted; consult reviewed operating semantics. | vendor_blocks:UART_Type.CTRL; header:UART_CTRL_RESET_VALUE; vendor_blocks:UART_Type.CTRL; header:UART_CTRL_RESET_VALUE | 1 | 4 |
| DATA | 0x010 | 8 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | vendor_blocks:UART_Type.DATA; vendor_blocks:UART_Type.DATA | 4 | 1 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CTRL | ENABLE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UART_CTRL_ENABLE_MASK; header:UART_CTRL_ENABLE_MASK |

## Operating semantics unavailable

**uart: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
