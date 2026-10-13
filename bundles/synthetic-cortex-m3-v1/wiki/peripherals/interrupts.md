# INTERRUPTS — declarations only

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/uart]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| IRQCTRL0 | 0x40003000 | Not asserted | Not asserted | header:IRQCTRL0_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ENABLE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | vendor_blocks:IRQCTRL_Type.ENABLE; vendor_blocks:IRQCTRL_Type.ENABLE |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ENABLE | LINE | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:IRQ_ENABLE_LINE_MASK; header:IRQ_ENABLE_LINE_MASK |

## Operating semantics unavailable

**interrupts: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
