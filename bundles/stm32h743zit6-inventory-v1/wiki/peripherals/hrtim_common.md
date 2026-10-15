# HRTIM_COMMON — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| HRTIM1_COMMON | 0x40017780 | Not asserted | Not asserted | header:HRTIM1_COMMON_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.CR2 |
| ISR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ISR |
| ICR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ICR |
| IER | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.IER |
| OENR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.OENR |
| ODISR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ODISR |
| ODSR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ODSR |
| BMCR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BMCR |
| BMTRGR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BMTRGR |
| BMCMPR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BMCMPR |
| BMPER | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BMPER |
| EECR1 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.EECR1 |
| EECR2 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.EECR2 |
| EECR3 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.EECR3 |
| ADC1R | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ADC1R |
| ADC2R | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ADC2R |
| ADC3R | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ADC3R |
| ADC4R | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.ADC4R |
| FLTINR1 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.FLTINR1 |
| FLTINR2 | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.FLTINR2 |
| BDMUPR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDMUPR |
| BDTAUPR | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDTAUPR |
| BDTBUPR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDTBUPR |
| BDTCUPR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDTCUPR |
| BDTDUPR | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDTDUPR |
| BDTEUPR | 0x06C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDTEUPR |
| BDMADR | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Common_TypeDef.BDMADR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**hrtim_common: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
