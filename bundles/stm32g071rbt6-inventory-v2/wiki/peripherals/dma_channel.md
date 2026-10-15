# DMA_CHANNEL — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1_Channel1 | 0x40020008 | Not asserted | Not asserted | header:DMA1_Channel1_BASE |
| DMA1_Channel2 | 0x4002001C | Not asserted | Not asserted | header:DMA1_Channel2_BASE |
| DMA1_Channel3 | 0x40020030 | Not asserted | Not asserted | header:DMA1_Channel3_BASE |
| DMA1_Channel4 | 0x40020044 | Not asserted | Not asserted | header:DMA1_Channel4_BASE |
| DMA1_Channel5 | 0x40020058 | Not asserted | Not asserted | header:DMA1_Channel5_BASE |
| DMA1_Channel6 | 0x4002006C | Not asserted | Not asserted | header:DMA1_Channel6_BASE |
| DMA1_Channel7 | 0x40020080 | Not asserted | Not asserted | header:DMA1_Channel7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Channel_TypeDef.CCR |
| CNDTR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Channel_TypeDef.CNDTR |
| CPAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Channel_TypeDef.CPAR |
| CMAR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Channel_TypeDef.CMAR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dma_channel: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
