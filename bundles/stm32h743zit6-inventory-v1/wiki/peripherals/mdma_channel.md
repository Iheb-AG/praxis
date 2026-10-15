# MDMA_CHANNEL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| MDMA_Channel0 | 0x52000040 | Not asserted | Not asserted | header:MDMA_Channel0_BASE |
| MDMA_Channel1 | 0x52000080 | Not asserted | Not asserted | header:MDMA_Channel1_BASE |
| MDMA_Channel10 | 0x520002C0 | Not asserted | Not asserted | header:MDMA_Channel10_BASE |
| MDMA_Channel11 | 0x52000300 | Not asserted | Not asserted | header:MDMA_Channel11_BASE |
| MDMA_Channel12 | 0x52000340 | Not asserted | Not asserted | header:MDMA_Channel12_BASE |
| MDMA_Channel13 | 0x52000380 | Not asserted | Not asserted | header:MDMA_Channel13_BASE |
| MDMA_Channel14 | 0x520003C0 | Not asserted | Not asserted | header:MDMA_Channel14_BASE |
| MDMA_Channel15 | 0x52000400 | Not asserted | Not asserted | header:MDMA_Channel15_BASE |
| MDMA_Channel2 | 0x520000C0 | Not asserted | Not asserted | header:MDMA_Channel2_BASE |
| MDMA_Channel3 | 0x52000100 | Not asserted | Not asserted | header:MDMA_Channel3_BASE |
| MDMA_Channel4 | 0x52000140 | Not asserted | Not asserted | header:MDMA_Channel4_BASE |
| MDMA_Channel5 | 0x52000180 | Not asserted | Not asserted | header:MDMA_Channel5_BASE |
| MDMA_Channel6 | 0x520001C0 | Not asserted | Not asserted | header:MDMA_Channel6_BASE |
| MDMA_Channel7 | 0x52000200 | Not asserted | Not asserted | header:MDMA_Channel7_BASE |
| MDMA_Channel8 | 0x52000240 | Not asserted | Not asserted | header:MDMA_Channel8_BASE |
| MDMA_Channel9 | 0x52000280 | Not asserted | Not asserted | header:MDMA_Channel9_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CISR |
| CIFCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CIFCR |
| CESR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CESR |
| CCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CCR |
| CTCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CTCR |
| CBNDTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CBNDTR |
| CSAR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CSAR |
| CDAR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CDAR |
| CBRUR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CBRUR |
| CLAR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CLAR |
| CTBR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CTBR |
| CMAR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CMAR |
| CMDR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_Channel_TypeDef.CMDR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**mdma_channel: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
