# BDMA — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| BDMA | 0x58025400 | Not asserted | Not asserted | header:BDMA_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_TypeDef.ISR |
| IFCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BDMA_TypeDef.IFCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISR | GIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF0_Msk |
| ISR | TCIF0 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF0_Msk |
| ISR | HTIF0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF0_Msk |
| ISR | TEIF0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF0_Msk |
| ISR | GIF1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF1_Msk |
| ISR | TCIF1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF1_Msk |
| ISR | HTIF1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF1_Msk |
| ISR | TEIF1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF1_Msk |
| ISR | GIF2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF2_Msk |
| ISR | TCIF2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF2_Msk |
| ISR | HTIF2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF2_Msk |
| ISR | TEIF2 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF2_Msk |
| ISR | GIF3 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF3_Msk |
| ISR | TCIF3 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF3_Msk |
| ISR | HTIF3 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF3_Msk |
| ISR | TEIF3 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF3_Msk |
| ISR | GIF4 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF4_Msk |
| ISR | TCIF4 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF4_Msk |
| ISR | HTIF4 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF4_Msk |
| ISR | TEIF4 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF4_Msk |
| ISR | GIF5 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF5_Msk |
| ISR | TCIF5 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF5_Msk |
| ISR | HTIF5 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF5_Msk |
| ISR | TEIF5 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF5_Msk |
| ISR | GIF6 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF6_Msk |
| ISR | TCIF6 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF6_Msk |
| ISR | HTIF6 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF6_Msk |
| ISR | TEIF6 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF6_Msk |
| ISR | GIF7 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_GIF7_Msk |
| ISR | TCIF7 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TCIF7_Msk |
| ISR | HTIF7 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_HTIF7_Msk |
| ISR | TEIF7 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_ISR_TEIF7_Msk |
| IFCR | CGIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF0_Msk |
| IFCR | CTCIF0 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF0_Msk |
| IFCR | CHTIF0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF0_Msk |
| IFCR | CTEIF0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF0_Msk |
| IFCR | CGIF1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF1_Msk |
| IFCR | CTCIF1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF1_Msk |
| IFCR | CHTIF1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF1_Msk |
| IFCR | CTEIF1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF1_Msk |
| IFCR | CGIF2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF2_Msk |
| IFCR | CTCIF2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF2_Msk |
| IFCR | CHTIF2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF2_Msk |
| IFCR | CTEIF2 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF2_Msk |
| IFCR | CGIF3 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF3_Msk |
| IFCR | CTCIF3 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF3_Msk |
| IFCR | CHTIF3 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF3_Msk |
| IFCR | CTEIF3 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF3_Msk |
| IFCR | CGIF4 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF4_Msk |
| IFCR | CTCIF4 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF4_Msk |
| IFCR | CHTIF4 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF4_Msk |
| IFCR | CTEIF4 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF4_Msk |
| IFCR | CGIF5 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF5_Msk |
| IFCR | CTCIF5 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF5_Msk |
| IFCR | CHTIF5 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF5_Msk |
| IFCR | CTEIF5 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF5_Msk |
| IFCR | CGIF6 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF6_Msk |
| IFCR | CTCIF6 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF6_Msk |
| IFCR | CHTIF6 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF6_Msk |
| IFCR | CTEIF6 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF6_Msk |
| IFCR | CGIF7 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CGIF7_Msk |
| IFCR | CTCIF7 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTCIF7_Msk |
| IFCR | CHTIF7 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CHTIF7_Msk |
| IFCR | CTEIF7 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:BDMA_IFCR_CTEIF7_Msk |

## Operating semantics unavailable

**bdma: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
