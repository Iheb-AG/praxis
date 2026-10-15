# PINS — declarations only

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/clock]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PINMUX0 | 0x40001000 | Not asserted | Not asserted | header:PINMUX0_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROUTE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | vendor_blocks:PINMUX_Type.ROUTE; vendor_blocks:PINMUX_Type.ROUTE | 2 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ROUTE | SELECT | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:PIN_ROUTE_SELECT_MASK; header:PIN_ROUTE_SELECT_MASK |

## Operating semantics unavailable

**pins: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
