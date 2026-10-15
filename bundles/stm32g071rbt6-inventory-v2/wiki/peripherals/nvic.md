# NVIC — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| NVIC | 0xE000E100 | Not asserted | Not asserted | core_cm0plus_h:NVIC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:NVIC_Type.ISER | 1 | 4 |
| ICER | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:NVIC_Type.ICER | 1 | 4 |
| ISPR | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:NVIC_Type.ISPR | 1 | 4 |
| ICPR | 0x180 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:NVIC_Type.ICPR | 1 | 4 |
| IP | 0x300 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:NVIC_Type.IP | 8 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm0plus_h:NVIC_Type.ISER |
| ICER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm0plus_h:NVIC_Type.ICER |
| ISPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm0plus_h:NVIC_Type.ISPR |
| ICPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm0plus_h:NVIC_Type.ICPR |
| IP | PRIORITY | 7:6 | 0xC0 | Implemented high priority bits per byte. | header:__NVIC_PRIO_BITS; core_cm0plus_h:NVIC_Type.IP |

## Operating semantics unavailable

**nvic: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
