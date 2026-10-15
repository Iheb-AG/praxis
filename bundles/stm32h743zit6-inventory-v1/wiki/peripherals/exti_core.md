# EXTI_CORE — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| EXTI_D1 | 0x58000080 | Not asserted | Not asserted | header:EXTI_D1_BASE |
| EXTI_D2 | 0x580000C0 | Not asserted | Not asserted | header:EXTI_D2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.IMR1 |
| EMR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.EMR1 |
| PR1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.PR1 |
| IMR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.IMR2 |
| EMR2 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.EMR2 |
| PR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.PR2 |
| IMR3 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.IMR3 |
| EMR3 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.EMR3 |
| PR3 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_Core_TypeDef.PR3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**exti_core: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
