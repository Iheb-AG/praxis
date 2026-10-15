# ADC_COMMON — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC12_COMMON | 0x40022300 | Not asserted | Not asserted | header:ADC12_COMMON_BASE |
| ADC3_COMMON | 0x58026300 | Not asserted | Not asserted | header:ADC3_COMMON_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CSR |
| CCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CCR |
| CDR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CDR |
| CDR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CDR2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**adc_common: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
