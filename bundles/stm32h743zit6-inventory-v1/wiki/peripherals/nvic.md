# NVIC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| NVIC | 0xE000E100 | Not asserted | Not asserted | core_cm7_h:NVIC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.ISER | 8 | 4 |
| ICER | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.ICER | 8 | 4 |
| ISPR | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.ISPR | 8 | 4 |
| ICPR | 0x180 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.ICPR | 8 | 4 |
| IABR | 0x200 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.IABR | 8 | 4 |
| IP | 0x300 | 8 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.IP | 240 | 1 |
| STIR | 0xE00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:NVIC_Type.STIR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm7_h:NVIC_Type.ISER |
| ICER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm7_h:NVIC_Type.ICER |
| ISPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm7_h:NVIC_Type.ISPR |
| ICPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm7_h:NVIC_Type.ICPR |
| IABR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Core bank width; only device IRQs are implemented. | core_cm7_h:NVIC_Type.IABR |
| IP | PRIORITY | 7:4 | 0xF0 | Implemented high priority bits per byte. | header:__NVIC_PRIO_BITS; core_cm7_h:NVIC_Type.IP |
| STIR | INTID | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:NVIC_STIR_INTID_Msk |

## Operating semantics unavailable

**nvic: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
