# DMA_STREAM — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1_Stream0 | 0x40020010 | Not asserted | Not asserted | header:DMA1_Stream0_BASE |
| DMA1_Stream1 | 0x40020028 | Not asserted | Not asserted | header:DMA1_Stream1_BASE |
| DMA1_Stream2 | 0x40020040 | Not asserted | Not asserted | header:DMA1_Stream2_BASE |
| DMA1_Stream3 | 0x40020058 | Not asserted | Not asserted | header:DMA1_Stream3_BASE |
| DMA1_Stream4 | 0x40020070 | Not asserted | Not asserted | header:DMA1_Stream4_BASE |
| DMA1_Stream5 | 0x40020088 | Not asserted | Not asserted | header:DMA1_Stream5_BASE |
| DMA1_Stream6 | 0x400200A0 | Not asserted | Not asserted | header:DMA1_Stream6_BASE |
| DMA1_Stream7 | 0x400200B8 | Not asserted | Not asserted | header:DMA1_Stream7_BASE |
| DMA2_Stream0 | 0x40020410 | Not asserted | Not asserted | header:DMA2_Stream0_BASE |
| DMA2_Stream1 | 0x40020428 | Not asserted | Not asserted | header:DMA2_Stream1_BASE |
| DMA2_Stream2 | 0x40020440 | Not asserted | Not asserted | header:DMA2_Stream2_BASE |
| DMA2_Stream3 | 0x40020458 | Not asserted | Not asserted | header:DMA2_Stream3_BASE |
| DMA2_Stream4 | 0x40020470 | Not asserted | Not asserted | header:DMA2_Stream4_BASE |
| DMA2_Stream5 | 0x40020488 | Not asserted | Not asserted | header:DMA2_Stream5_BASE |
| DMA2_Stream6 | 0x400204A0 | Not asserted | Not asserted | header:DMA2_Stream6_BASE |
| DMA2_Stream7 | 0x400204B8 | Not asserted | Not asserted | header:DMA2_Stream7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.CR |
| NDTR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.NDTR |
| PAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.PAR |
| M0AR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.M0AR |
| M1AR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.M1AR |
| FCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.FCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dma_stream: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
