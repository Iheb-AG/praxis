# DMA — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1 | 0x40020000 | Not asserted | Not asserted | header:DMA1_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.ISR |
| IFCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.IFCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISR | GIF1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF1_Msk |
| ISR | TCIF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF1_Msk |
| ISR | HTIF1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF1_Msk |
| ISR | TEIF1 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF1_Msk |
| ISR | GIF2 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF2_Msk |
| ISR | TCIF2 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF2_Msk |
| ISR | HTIF2 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF2_Msk |
| ISR | TEIF2 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF2_Msk |
| ISR | GIF3 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF3_Msk |
| ISR | TCIF3 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF3_Msk |
| ISR | HTIF3 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF3_Msk |
| ISR | TEIF3 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF3_Msk |
| ISR | GIF4 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF4_Msk |
| ISR | TCIF4 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF4_Msk |
| ISR | HTIF4 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF4_Msk |
| ISR | TEIF4 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF4_Msk |
| ISR | GIF5 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF5_Msk |
| ISR | TCIF5 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF5_Msk |
| ISR | HTIF5 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF5_Msk |
| ISR | TEIF5 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF5_Msk |
| ISR | GIF6 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF6_Msk |
| ISR | TCIF6 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF6_Msk |
| ISR | HTIF6 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF6_Msk |
| ISR | TEIF6 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF6_Msk |
| ISR | GIF7 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_GIF7_Msk |
| ISR | TCIF7 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TCIF7_Msk |
| ISR | HTIF7 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_HTIF7_Msk |
| ISR | TEIF7 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_ISR_TEIF7_Msk |
| IFCR | CGIF1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF1_Msk |
| IFCR | CTCIF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF1_Msk |
| IFCR | CHTIF1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF1_Msk |
| IFCR | CTEIF1 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF1_Msk |
| IFCR | CGIF2 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF2_Msk |
| IFCR | CTCIF2 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF2_Msk |
| IFCR | CHTIF2 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF2_Msk |
| IFCR | CTEIF2 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF2_Msk |
| IFCR | CGIF3 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF3_Msk |
| IFCR | CTCIF3 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF3_Msk |
| IFCR | CHTIF3 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF3_Msk |
| IFCR | CTEIF3 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF3_Msk |
| IFCR | CGIF4 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF4_Msk |
| IFCR | CTCIF4 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF4_Msk |
| IFCR | CHTIF4 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF4_Msk |
| IFCR | CTEIF4 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF4_Msk |
| IFCR | CGIF5 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF5_Msk |
| IFCR | CTCIF5 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF5_Msk |
| IFCR | CHTIF5 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF5_Msk |
| IFCR | CTEIF5 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF5_Msk |
| IFCR | CGIF6 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF6_Msk |
| IFCR | CTCIF6 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF6_Msk |
| IFCR | CHTIF6 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF6_Msk |
| IFCR | CTEIF6 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF6_Msk |
| IFCR | CGIF7 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CGIF7_Msk |
| IFCR | CTCIF7 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTCIF7_Msk |
| IFCR | CHTIF7 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CHTIF7_Msk |
| IFCR | CTEIF7 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_IFCR_CTEIF7_Msk |

## Operating semantics unavailable

**dma: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
