# STM32F407 DMA — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1 | 0x40026000 | AHB1 | RCC_AHB1ENR.DMA1EN or DMA2EN | header:DMA1_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2 | 0x40026400 | AHB1 | RCC_AHB1ENR.DMA1EN or DMA2EN | header:DMA2_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LISR | 0x000 | 32 | — | RO | 0x0 | Read status; flags are cleared by writing 1 to the corresponding IFCR bit. | header:DMA_TypeDef.LISR; header:DMA_TypeDef.LISR; rm_features_327:page:327 | 32 |
| HISR | 0x004 | 32 | — | RO | 0x0 | Read status; flags are cleared by writing 1 to the corresponding IFCR bit. | header:DMA_TypeDef.HISR; header:DMA_TypeDef.HISR; rm_features_328:page:328 | 32 |
| LIFCR | 0x008 | 32 | — | WO | 0x0 | Write 1 only to flags selected for clearing; write 0 to others; never read-modify-write a flag-clear register. | header:DMA_TypeDef.LIFCR; header:DMA_TypeDef.LIFCR; rm_features_329:page:329 | 32 |
| HIFCR | 0x00C | 32 | — | WO | 0x0 | Write 1 only to flags selected for clearing; write 0 to others; never read-modify-write a flag-clear register. | header:DMA_TypeDef.HIFCR; header:DMA_TypeDef.HIFCR; rm_features_330:page:330 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| LISR | FEIF0 | 0:0 | 0x1 | Stream 0 FIFO error flag. | header:DMA_LISR_FEIF0_Msk; header:DMA_LISR_FEIF0_Msk; rm_features_327:page:327 |
| LISR | DMEIF0 | 2:2 | 0x4 | Stream 0 direct-mode error flag. | header:DMA_LISR_DMEIF0_Msk; header:DMA_LISR_DMEIF0_Msk; rm_features_327:page:327 |
| LISR | TEIF0 | 3:3 | 0x8 | Stream 0 transfer error flag. | header:DMA_LISR_TEIF0_Msk; header:DMA_LISR_TEIF0_Msk; rm_features_327:page:327 |
| LISR | HTIF0 | 4:4 | 0x10 | Stream 0 half transfer flag. | header:DMA_LISR_HTIF0_Msk; header:DMA_LISR_HTIF0_Msk; rm_features_327:page:327 |
| LISR | TCIF0 | 5:5 | 0x20 | Stream 0 transfer complete flag. | header:DMA_LISR_TCIF0_Msk; header:DMA_LISR_TCIF0_Msk; rm_features_327:page:327 |
| LISR | FEIF1 | 6:6 | 0x40 | Stream 1 FIFO error flag. | header:DMA_LISR_FEIF1_Msk; header:DMA_LISR_FEIF1_Msk; rm_features_327:page:327 |
| LISR | DMEIF1 | 8:8 | 0x100 | Stream 1 direct-mode error flag. | header:DMA_LISR_DMEIF1_Msk; header:DMA_LISR_DMEIF1_Msk; rm_features_327:page:327 |
| LISR | TEIF1 | 9:9 | 0x200 | Stream 1 transfer error flag. | header:DMA_LISR_TEIF1_Msk; header:DMA_LISR_TEIF1_Msk; rm_features_327:page:327 |
| LISR | HTIF1 | 10:10 | 0x400 | Stream 1 half transfer flag. | header:DMA_LISR_HTIF1_Msk; header:DMA_LISR_HTIF1_Msk; rm_features_327:page:327 |
| LISR | TCIF1 | 11:11 | 0x800 | Stream 1 transfer complete flag. | header:DMA_LISR_TCIF1_Msk; header:DMA_LISR_TCIF1_Msk; rm_features_327:page:327 |
| LISR | FEIF2 | 16:16 | 0x10000 | Stream 2 FIFO error flag. | header:DMA_LISR_FEIF2_Msk; header:DMA_LISR_FEIF2_Msk; rm_features_327:page:327 |
| LISR | DMEIF2 | 18:18 | 0x40000 | Stream 2 direct-mode error flag. | header:DMA_LISR_DMEIF2_Msk; header:DMA_LISR_DMEIF2_Msk; rm_features_327:page:327 |
| LISR | TEIF2 | 19:19 | 0x80000 | Stream 2 transfer error flag. | header:DMA_LISR_TEIF2_Msk; header:DMA_LISR_TEIF2_Msk; rm_features_327:page:327 |
| LISR | HTIF2 | 20:20 | 0x100000 | Stream 2 half transfer flag. | header:DMA_LISR_HTIF2_Msk; header:DMA_LISR_HTIF2_Msk; rm_features_327:page:327 |
| LISR | TCIF2 | 21:21 | 0x200000 | Stream 2 transfer complete flag. | header:DMA_LISR_TCIF2_Msk; header:DMA_LISR_TCIF2_Msk; rm_features_327:page:327 |
| LISR | FEIF3 | 22:22 | 0x400000 | Stream 3 FIFO error flag. | header:DMA_LISR_FEIF3_Msk; header:DMA_LISR_FEIF3_Msk; rm_features_327:page:327 |
| LISR | DMEIF3 | 24:24 | 0x1000000 | Stream 3 direct-mode error flag. | header:DMA_LISR_DMEIF3_Msk; header:DMA_LISR_DMEIF3_Msk; rm_features_327:page:327 |
| LISR | TEIF3 | 25:25 | 0x2000000 | Stream 3 transfer error flag. | header:DMA_LISR_TEIF3_Msk; header:DMA_LISR_TEIF3_Msk; rm_features_327:page:327 |
| LISR | HTIF3 | 26:26 | 0x4000000 | Stream 3 half transfer flag. | header:DMA_LISR_HTIF3_Msk; header:DMA_LISR_HTIF3_Msk; rm_features_327:page:327 |
| LISR | TCIF3 | 27:27 | 0x8000000 | Stream 3 transfer complete flag. | header:DMA_LISR_TCIF3_Msk; header:DMA_LISR_TCIF3_Msk; rm_features_327:page:327 |
| HISR | FEIF4 | 0:0 | 0x1 | Stream 4 FIFO error flag. | header:DMA_HISR_FEIF4_Msk; header:DMA_HISR_FEIF4_Msk; rm_features_328:page:328 |
| HISR | DMEIF4 | 2:2 | 0x4 | Stream 4 direct-mode error flag. | header:DMA_HISR_DMEIF4_Msk; header:DMA_HISR_DMEIF4_Msk; rm_features_328:page:328 |
| HISR | TEIF4 | 3:3 | 0x8 | Stream 4 transfer error flag. | header:DMA_HISR_TEIF4_Msk; header:DMA_HISR_TEIF4_Msk; rm_features_328:page:328 |
| HISR | HTIF4 | 4:4 | 0x10 | Stream 4 half transfer flag. | header:DMA_HISR_HTIF4_Msk; header:DMA_HISR_HTIF4_Msk; rm_features_328:page:328 |
| HISR | TCIF4 | 5:5 | 0x20 | Stream 4 transfer complete flag. | header:DMA_HISR_TCIF4_Msk; header:DMA_HISR_TCIF4_Msk; rm_features_328:page:328 |
| HISR | FEIF5 | 6:6 | 0x40 | Stream 5 FIFO error flag. | header:DMA_HISR_FEIF5_Msk; header:DMA_HISR_FEIF5_Msk; rm_features_328:page:328 |
| HISR | DMEIF5 | 8:8 | 0x100 | Stream 5 direct-mode error flag. | header:DMA_HISR_DMEIF5_Msk; header:DMA_HISR_DMEIF5_Msk; rm_features_328:page:328 |
| HISR | TEIF5 | 9:9 | 0x200 | Stream 5 transfer error flag. | header:DMA_HISR_TEIF5_Msk; header:DMA_HISR_TEIF5_Msk; rm_features_328:page:328 |
| HISR | HTIF5 | 10:10 | 0x400 | Stream 5 half transfer flag. | header:DMA_HISR_HTIF5_Msk; header:DMA_HISR_HTIF5_Msk; rm_features_328:page:328 |
| HISR | TCIF5 | 11:11 | 0x800 | Stream 5 transfer complete flag. | header:DMA_HISR_TCIF5_Msk; header:DMA_HISR_TCIF5_Msk; rm_features_328:page:328 |
| HISR | FEIF6 | 16:16 | 0x10000 | Stream 6 FIFO error flag. | header:DMA_HISR_FEIF6_Msk; header:DMA_HISR_FEIF6_Msk; rm_features_328:page:328 |
| HISR | DMEIF6 | 18:18 | 0x40000 | Stream 6 direct-mode error flag. | header:DMA_HISR_DMEIF6_Msk; header:DMA_HISR_DMEIF6_Msk; rm_features_328:page:328 |
| HISR | TEIF6 | 19:19 | 0x80000 | Stream 6 transfer error flag. | header:DMA_HISR_TEIF6_Msk; header:DMA_HISR_TEIF6_Msk; rm_features_328:page:328 |
| HISR | HTIF6 | 20:20 | 0x100000 | Stream 6 half transfer flag. | header:DMA_HISR_HTIF6_Msk; header:DMA_HISR_HTIF6_Msk; rm_features_328:page:328 |
| HISR | TCIF6 | 21:21 | 0x200000 | Stream 6 transfer complete flag. | header:DMA_HISR_TCIF6_Msk; header:DMA_HISR_TCIF6_Msk; rm_features_328:page:328 |
| HISR | FEIF7 | 22:22 | 0x400000 | Stream 7 FIFO error flag. | header:DMA_HISR_FEIF7_Msk; header:DMA_HISR_FEIF7_Msk; rm_features_328:page:328 |
| HISR | DMEIF7 | 24:24 | 0x1000000 | Stream 7 direct-mode error flag. | header:DMA_HISR_DMEIF7_Msk; header:DMA_HISR_DMEIF7_Msk; rm_features_328:page:328 |
| HISR | TEIF7 | 25:25 | 0x2000000 | Stream 7 transfer error flag. | header:DMA_HISR_TEIF7_Msk; header:DMA_HISR_TEIF7_Msk; rm_features_328:page:328 |
| HISR | HTIF7 | 26:26 | 0x4000000 | Stream 7 half transfer flag. | header:DMA_HISR_HTIF7_Msk; header:DMA_HISR_HTIF7_Msk; rm_features_328:page:328 |
| HISR | TCIF7 | 27:27 | 0x8000000 | Stream 7 transfer complete flag. | header:DMA_HISR_TCIF7_Msk; header:DMA_HISR_TCIF7_Msk; rm_features_328:page:328 |
| LIFCR | CFEIF0 | 0:0 | 0x1 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CFEIF0_Msk; header:DMA_LIFCR_CFEIF0_Msk; rm_features_329:page:329 |
| LIFCR | CDMEIF0 | 2:2 | 0x4 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CDMEIF0_Msk; header:DMA_LIFCR_CDMEIF0_Msk; rm_features_329:page:329 |
| LIFCR | CTEIF0 | 3:3 | 0x8 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTEIF0_Msk; header:DMA_LIFCR_CTEIF0_Msk; rm_features_329:page:329 |
| LIFCR | CHTIF0 | 4:4 | 0x10 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CHTIF0_Msk; header:DMA_LIFCR_CHTIF0_Msk; rm_features_329:page:329 |
| LIFCR | CTCIF0 | 5:5 | 0x20 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTCIF0_Msk; header:DMA_LIFCR_CTCIF0_Msk; rm_features_329:page:329 |
| LIFCR | CFEIF1 | 6:6 | 0x40 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CFEIF1_Msk; header:DMA_LIFCR_CFEIF1_Msk; rm_features_329:page:329 |
| LIFCR | CDMEIF1 | 8:8 | 0x100 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CDMEIF1_Msk; header:DMA_LIFCR_CDMEIF1_Msk; rm_features_329:page:329 |
| LIFCR | CTEIF1 | 9:9 | 0x200 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTEIF1_Msk; header:DMA_LIFCR_CTEIF1_Msk; rm_features_329:page:329 |
| LIFCR | CHTIF1 | 10:10 | 0x400 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CHTIF1_Msk; header:DMA_LIFCR_CHTIF1_Msk; rm_features_329:page:329 |
| LIFCR | CTCIF1 | 11:11 | 0x800 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTCIF1_Msk; header:DMA_LIFCR_CTCIF1_Msk; rm_features_329:page:329 |
| LIFCR | CFEIF2 | 16:16 | 0x10000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CFEIF2_Msk; header:DMA_LIFCR_CFEIF2_Msk; rm_features_329:page:329 |
| LIFCR | CDMEIF2 | 18:18 | 0x40000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CDMEIF2_Msk; header:DMA_LIFCR_CDMEIF2_Msk; rm_features_329:page:329 |
| LIFCR | CTEIF2 | 19:19 | 0x80000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTEIF2_Msk; header:DMA_LIFCR_CTEIF2_Msk; rm_features_329:page:329 |
| LIFCR | CHTIF2 | 20:20 | 0x100000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CHTIF2_Msk; header:DMA_LIFCR_CHTIF2_Msk; rm_features_329:page:329 |
| LIFCR | CTCIF2 | 21:21 | 0x200000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTCIF2_Msk; header:DMA_LIFCR_CTCIF2_Msk; rm_features_329:page:329 |
| LIFCR | CFEIF3 | 22:22 | 0x400000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CFEIF3_Msk; header:DMA_LIFCR_CFEIF3_Msk; rm_features_329:page:329 |
| LIFCR | CDMEIF3 | 24:24 | 0x1000000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CDMEIF3_Msk; header:DMA_LIFCR_CDMEIF3_Msk; rm_features_329:page:329 |
| LIFCR | CTEIF3 | 25:25 | 0x2000000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTEIF3_Msk; header:DMA_LIFCR_CTEIF3_Msk; rm_features_329:page:329 |
| LIFCR | CHTIF3 | 26:26 | 0x4000000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CHTIF3_Msk; header:DMA_LIFCR_CHTIF3_Msk; rm_features_329:page:329 |
| LIFCR | CTCIF3 | 27:27 | 0x8000000 | Write 1 to clear the corresponding stream flag. | header:DMA_LIFCR_CTCIF3_Msk; header:DMA_LIFCR_CTCIF3_Msk; rm_features_329:page:329 |
| HIFCR | CFEIF4 | 0:0 | 0x1 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CFEIF4_Msk; header:DMA_HIFCR_CFEIF4_Msk; rm_features_330:page:330 |
| HIFCR | CDMEIF4 | 2:2 | 0x4 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CDMEIF4_Msk; header:DMA_HIFCR_CDMEIF4_Msk; rm_features_330:page:330 |
| HIFCR | CTEIF4 | 3:3 | 0x8 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTEIF4_Msk; header:DMA_HIFCR_CTEIF4_Msk; rm_features_330:page:330 |
| HIFCR | CHTIF4 | 4:4 | 0x10 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CHTIF4_Msk; header:DMA_HIFCR_CHTIF4_Msk; rm_features_330:page:330 |
| HIFCR | CTCIF4 | 5:5 | 0x20 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTCIF4_Msk; header:DMA_HIFCR_CTCIF4_Msk; rm_features_330:page:330 |
| HIFCR | CFEIF5 | 6:6 | 0x40 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CFEIF5_Msk; header:DMA_HIFCR_CFEIF5_Msk; rm_features_330:page:330 |
| HIFCR | CDMEIF5 | 8:8 | 0x100 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CDMEIF5_Msk; header:DMA_HIFCR_CDMEIF5_Msk; rm_features_330:page:330 |
| HIFCR | CTEIF5 | 9:9 | 0x200 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTEIF5_Msk; header:DMA_HIFCR_CTEIF5_Msk; rm_features_330:page:330 |
| HIFCR | CHTIF5 | 10:10 | 0x400 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CHTIF5_Msk; header:DMA_HIFCR_CHTIF5_Msk; rm_features_330:page:330 |
| HIFCR | CTCIF5 | 11:11 | 0x800 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTCIF5_Msk; header:DMA_HIFCR_CTCIF5_Msk; rm_features_330:page:330 |
| HIFCR | CFEIF6 | 16:16 | 0x10000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CFEIF6_Msk; header:DMA_HIFCR_CFEIF6_Msk; rm_features_330:page:330 |
| HIFCR | CDMEIF6 | 18:18 | 0x40000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CDMEIF6_Msk; header:DMA_HIFCR_CDMEIF6_Msk; rm_features_330:page:330 |
| HIFCR | CTEIF6 | 19:19 | 0x80000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTEIF6_Msk; header:DMA_HIFCR_CTEIF6_Msk; rm_features_330:page:330 |
| HIFCR | CHTIF6 | 20:20 | 0x100000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CHTIF6_Msk; header:DMA_HIFCR_CHTIF6_Msk; rm_features_330:page:330 |
| HIFCR | CTCIF6 | 21:21 | 0x200000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTCIF6_Msk; header:DMA_HIFCR_CTCIF6_Msk; rm_features_330:page:330 |
| HIFCR | CFEIF7 | 22:22 | 0x400000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CFEIF7_Msk; header:DMA_HIFCR_CFEIF7_Msk; rm_features_330:page:330 |
| HIFCR | CDMEIF7 | 24:24 | 0x1000000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CDMEIF7_Msk; header:DMA_HIFCR_CDMEIF7_Msk; rm_features_330:page:330 |
| HIFCR | CTEIF7 | 25:25 | 0x2000000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTEIF7_Msk; header:DMA_HIFCR_CTEIF7_Msk; rm_features_330:page:330 |
| HIFCR | CHTIF7 | 26:26 | 0x4000000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CHTIF7_Msk; header:DMA_HIFCR_CHTIF7_Msk; rm_features_330:page:330 |
| HIFCR | CTCIF7 | 27:27 | 0x8000000 | Write 1 to clear the corresponding stream flag. | header:DMA_HIFCR_CTCIF7_Msk; header:DMA_HIFCR_CTCIF7_Msk; rm_features_330:page:330 |

## Reviewed operating semantics

The controller owns status and W1C flag-clear groups; [[peripherals/dma_stream]] owns each transfer configuration. A net is not a DMA request mapping. This review covers polling status/clear behavior and the DMA2 memory-copy subset, not every peripheral channel assignment.

Use the exact controller/stream flag group. Direct W1C writes clear selected flags; a read-modify-write is inappropriate. Enable the clock through [[peripherals/rcc]] first. See [[features]] and [[coverage]].

Evidence: rm_features_324:page:324, rm_features_325:page:325, rm_features_327:page:327, rm_features_328:page:328, rm_features_329:page:329, rm_features_330:page:330. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| poll_status_clear | DMA1, DMA2 | LISR, HISR, LIFCR, HIFCR | HIFCR: CFEIF4, CDMEIF4, CTEIF4, CHTIF4, CTCIF4, CFEIF5, CDMEIF5, CTEIF5, CHTIF5, CTCIF5, CFEIF6, CDMEIF6, CTEIF6, CHTIF6, CTCIF6, CFEIF7, CDMEIF7, CTEIF7, CHTIF7, CTCIF7; HISR: FEIF4, DMEIF4, TEIF4, HTIF4, TCIF4, FEIF5, DMEIF5, TEIF5, HTIF5, TCIF5, FEIF6, DMEIF6, TEIF6, HTIF6, TCIF6, FEIF7, DMEIF7, TEIF7, HTIF7, TCIF7; LIFCR: CFEIF0, CDMEIF0, CTEIF0, CHTIF0, CTCIF0, CFEIF1, CDMEIF1, CTEIF1, CHTIF1, CTCIF1, CFEIF2, CDMEIF2, CTEIF2, CHTIF2, CTCIF2, CFEIF3, CDMEIF3, CTEIF3, CHTIF3, CTCIF3; LISR: FEIF0, DMEIF0, TEIF0, HTIF0, TCIF0, FEIF1, DMEIF1, TEIF1, HTIF1, TCIF1, FEIF2, DMEIF2, TEIF2, HTIF2, TCIF2, FEIF3, DMEIF3, TEIF3, HTIF3, TCIF3 | Select the flag group for the exact controller and stream.<br>Clear existing stream flags before enabling a stream.<br>Poll transfer-complete and error flags with bounded waits.<br>Clear flags by direct W1C masks, never read-modify-write. | rm_features_324:page:324; rm_features_325:page:325; rm_features_327:page:327; rm_features_328:page:328; rm_features_329:page:329; rm_features_330:page:330 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
