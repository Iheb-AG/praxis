# BDMA_CHANNEL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| BDMA_Channel0 | 0x58025408 | Not asserted | Not asserted | header:BDMA_Channel0_BASE |
| BDMA_Channel1 | 0x5802541C | Not asserted | Not asserted | header:BDMA_Channel1_BASE |
| BDMA_Channel2 | 0x58025430 | Not asserted | Not asserted | header:BDMA_Channel2_BASE |
| BDMA_Channel3 | 0x58025444 | Not asserted | Not asserted | header:BDMA_Channel3_BASE |
| BDMA_Channel4 | 0x58025458 | Not asserted | Not asserted | header:BDMA_Channel4_BASE |
| BDMA_Channel5 | 0x5802546C | Not asserted | Not asserted | header:BDMA_Channel5_BASE |
| BDMA_Channel6 | 0x58025480 | Not asserted | Not asserted | header:BDMA_Channel6_BASE |
| BDMA_Channel7 | 0x58025494 | Not asserted | Not asserted | header:BDMA_Channel7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_Channel_TypeDef.CCR |
| CNDTR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_Channel_TypeDef.CNDTR |
| CPAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_Channel_TypeDef.CPAR |
| CM0AR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_Channel_TypeDef.CM0AR |
| CM1AR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_Channel_TypeDef.CM1AR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**bdma_channel: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
