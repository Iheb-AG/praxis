# LTDC_LAYER — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| LTDC_Layer1 | 0x50001084 | Not asserted | Not asserted | header:LTDC_Layer1_BASE |
| LTDC_Layer2 | 0x50001104 | Not asserted | Not asserted | header:LTDC_Layer2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CR |
| WHPCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.WHPCR |
| WVPCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.WVPCR |
| CKCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CKCR |
| PFCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.PFCR |
| CACR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CACR |
| DCCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.DCCR |
| BFCR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.BFCR |
| CFBAR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CFBAR |
| CFBLR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CFBLR |
| CFBLNR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CFBLNR |
| CLUTWR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_Layer_TypeDef.CLUTWR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**ltdc_layer: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
