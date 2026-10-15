# DMA — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1 | 0x40020000 | Not asserted | Not asserted | header:DMA1_BASE |
| DMA2 | 0x40020400 | Not asserted | Not asserted | header:DMA2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.LISR |
| HISR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.HISR |
| LIFCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.LIFCR |
| HIFCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_TypeDef.HIFCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| LISR | FEIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_FEIF0_Msk |
| LISR | DMEIF0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_DMEIF0_Msk |
| LISR | TEIF0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TEIF0_Msk |
| LISR | HTIF0 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_HTIF0_Msk |
| LISR | TCIF0 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TCIF0_Msk |
| LISR | FEIF1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_FEIF1_Msk |
| LISR | DMEIF1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_DMEIF1_Msk |
| LISR | TEIF1 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TEIF1_Msk |
| LISR | HTIF1 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_HTIF1_Msk |
| LISR | TCIF1 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TCIF1_Msk |
| LISR | FEIF2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_FEIF2_Msk |
| LISR | DMEIF2 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_DMEIF2_Msk |
| LISR | TEIF2 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TEIF2_Msk |
| LISR | HTIF2 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_HTIF2_Msk |
| LISR | TCIF2 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TCIF2_Msk |
| LISR | FEIF3 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_FEIF3_Msk |
| LISR | DMEIF3 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_DMEIF3_Msk |
| LISR | TEIF3 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TEIF3_Msk |
| LISR | HTIF3 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_HTIF3_Msk |
| LISR | TCIF3 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LISR_TCIF3_Msk |
| HISR | FEIF4 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_FEIF4_Msk |
| HISR | DMEIF4 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_DMEIF4_Msk |
| HISR | TEIF4 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TEIF4_Msk |
| HISR | HTIF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_HTIF4_Msk |
| HISR | TCIF4 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TCIF4_Msk |
| HISR | FEIF5 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_FEIF5_Msk |
| HISR | DMEIF5 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_DMEIF5_Msk |
| HISR | TEIF5 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TEIF5_Msk |
| HISR | HTIF5 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_HTIF5_Msk |
| HISR | TCIF5 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TCIF5_Msk |
| HISR | FEIF6 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_FEIF6_Msk |
| HISR | DMEIF6 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_DMEIF6_Msk |
| HISR | TEIF6 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TEIF6_Msk |
| HISR | HTIF6 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_HTIF6_Msk |
| HISR | TCIF6 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TCIF6_Msk |
| HISR | FEIF7 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_FEIF7_Msk |
| HISR | DMEIF7 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_DMEIF7_Msk |
| HISR | TEIF7 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TEIF7_Msk |
| HISR | HTIF7 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_HTIF7_Msk |
| HISR | TCIF7 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HISR_TCIF7_Msk |
| LIFCR | CFEIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CFEIF0_Msk |
| LIFCR | CDMEIF0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CDMEIF0_Msk |
| LIFCR | CTEIF0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTEIF0_Msk |
| LIFCR | CHTIF0 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CHTIF0_Msk |
| LIFCR | CTCIF0 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTCIF0_Msk |
| LIFCR | CFEIF1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CFEIF1_Msk |
| LIFCR | CDMEIF1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CDMEIF1_Msk |
| LIFCR | CTEIF1 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTEIF1_Msk |
| LIFCR | CHTIF1 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CHTIF1_Msk |
| LIFCR | CTCIF1 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTCIF1_Msk |
| LIFCR | CFEIF2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CFEIF2_Msk |
| LIFCR | CDMEIF2 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CDMEIF2_Msk |
| LIFCR | CTEIF2 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTEIF2_Msk |
| LIFCR | CHTIF2 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CHTIF2_Msk |
| LIFCR | CTCIF2 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTCIF2_Msk |
| LIFCR | CFEIF3 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CFEIF3_Msk |
| LIFCR | CDMEIF3 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CDMEIF3_Msk |
| LIFCR | CTEIF3 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTEIF3_Msk |
| LIFCR | CHTIF3 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CHTIF3_Msk |
| LIFCR | CTCIF3 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_LIFCR_CTCIF3_Msk |
| HIFCR | CFEIF4 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CFEIF4_Msk |
| HIFCR | CDMEIF4 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CDMEIF4_Msk |
| HIFCR | CTEIF4 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTEIF4_Msk |
| HIFCR | CHTIF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CHTIF4_Msk |
| HIFCR | CTCIF4 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTCIF4_Msk |
| HIFCR | CFEIF5 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CFEIF5_Msk |
| HIFCR | CDMEIF5 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CDMEIF5_Msk |
| HIFCR | CTEIF5 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTEIF5_Msk |
| HIFCR | CHTIF5 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CHTIF5_Msk |
| HIFCR | CTCIF5 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTCIF5_Msk |
| HIFCR | CFEIF6 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CFEIF6_Msk |
| HIFCR | CDMEIF6 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CDMEIF6_Msk |
| HIFCR | CTEIF6 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTEIF6_Msk |
| HIFCR | CHTIF6 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CHTIF6_Msk |
| HIFCR | CTCIF6 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTCIF6_Msk |
| HIFCR | CFEIF7 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CFEIF7_Msk |
| HIFCR | CDMEIF7 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CDMEIF7_Msk |
| HIFCR | CTEIF7 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTEIF7_Msk |
| HIFCR | CHTIF7 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CHTIF7_Msk |
| HIFCR | CTCIF7 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_HIFCR_CTCIF7_Msk |

## Operating semantics unavailable

**dma: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
