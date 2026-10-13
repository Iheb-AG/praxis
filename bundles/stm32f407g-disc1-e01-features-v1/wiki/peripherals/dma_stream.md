# STM32F407 DMA_STREAM — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/dma]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1_Stream0 | 0x40026010 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream0_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream1 | 0x40026028 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream1_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream2 | 0x40026040 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream2_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream3 | 0x40026058 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream3_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream4 | 0x40026070 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream4_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream5 | 0x40026088 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream5_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream6 | 0x400260A0 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream6_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA1_Stream7 | 0x400260B8 | AHB1 | Clock from owning DMA controller | header:DMA1_Stream7_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream0 | 0x40026410 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream0_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream1 | 0x40026428 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream1_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream2 | 0x40026440 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream2_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream3 | 0x40026458 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream3_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream4 | 0x40026470 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream4_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream5 | 0x40026488 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream5_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream6 | 0x400264A0 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream6_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |
| DMA2_Stream7 | 0x400264B8 | AHB1 | Clock from owning DMA controller | header:DMA2_Stream7_BASE; rm_features_243:page:243; rm_features_244:page:244; rm_features_306:page:306 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | RW | 0x0 | Configure protected fields only after EN reads zero. Hardware may clear EN. Bit 20 is reserved for this target according to RM0090; the CMSIS ACK mask is not operating authority. | header:DMA_Stream_TypeDef.CR; header:DMA_Stream_TypeDef.CR; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 | 32 |
| NDTR | 0x004 | 32 | — | RW | 0x0 | Low 16 bits count transfer items (1..65535); hardware decrements. Write only while disabled. Zero means no transaction. Reserved upper bits remain zero. | header:DMA_Stream_TypeDef.NDTR; header:DMA_Stream_TypeDef.NDTR; rm_features_333:page:333 | 32 |
| PAR | 0x008 | 32 | — | RW | 0x0 | Peripheral address; source address in memory-to-memory. Addresses must be aligned to the configured width. In this mode write only while EN=0. | header:DMA_Stream_TypeDef.PAR; header:DMA_Stream_TypeDef.PAR; rm_features_333:page:333; rm_features_334:page:334; rm_features_335:page:335 | 32 |
| M0AR | 0x00C | 32 | — | RW | 0x0 | Memory bank 0 address; destination in memory-to-memory. Addresses must be aligned to the configured width. In this mode write only while EN=0. | header:DMA_Stream_TypeDef.M0AR; header:DMA_Stream_TypeDef.M0AR; rm_features_334:page:334; rm_features_334:page:334; rm_features_335:page:335 | 32 |
| M1AR | 0x010 | 32 | — | RW | 0x0 | Memory bank 1 address for double buffering, excluded from the reviewed copy mode. Addresses must be aligned to the configured width. In this mode write only while EN=0. | header:DMA_Stream_TypeDef.M1AR; header:DMA_Stream_TypeDef.M1AR; rm_features_334:page:334; rm_features_334:page:334; rm_features_335:page:335 | 32 |
| FCR | 0x014 | 32 | — | mixed | 0x21 | FS is read-only. Configure FTH and DMDIS only when EN=0. Memory-to-memory requires FIFO; direct mode is forbidden. | header:DMA_Stream_TypeDef.FCR; header:DMA_Stream_TypeDef.FCR; rm_features_335:page:335; rm_features_336:page:336 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN | 0:0 | 0x1 | Set to enable; clear to request disable and wait until readback is zero. | header:DMA_SxCR_EN_Msk; header:DMA_SxCR_EN_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | DMEIE | 1:1 | 0x2 | Direct-mode error interrupt enable. | header:DMA_SxCR_DMEIE_Msk; header:DMA_SxCR_DMEIE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | TEIE | 2:2 | 0x4 | Transfer-error interrupt enable. | header:DMA_SxCR_TEIE_Msk; header:DMA_SxCR_TEIE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | HTIE | 3:3 | 0x8 | Half-transfer interrupt enable. | header:DMA_SxCR_HTIE_Msk; header:DMA_SxCR_HTIE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | TCIE | 4:4 | 0x10 | Transfer-complete interrupt enable. | header:DMA_SxCR_TCIE_Msk; header:DMA_SxCR_TCIE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | PFCTRL | 5:5 | 0x20 | 0 selects DMA flow controller; peripheral flow control is unavailable in memory-to-memory. | header:DMA_SxCR_PFCTRL_Msk; header:DMA_SxCR_PFCTRL_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | DIR | 7:6 | 0xC0 | 0 peripheral-to-memory, 1 memory-to-peripheral, 2 memory-to-memory; 3 reserved. | header:DMA_SxCR_DIR_Msk; header:DMA_SxCR_DIR_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | CIRC | 8:8 | 0x100 | Circular mode; forbidden in the supported memory-to-memory mode. | header:DMA_SxCR_CIRC_Msk; header:DMA_SxCR_CIRC_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | PINC | 9:9 | 0x200 | Increment peripheral/source address after each transfer. | header:DMA_SxCR_PINC_Msk; header:DMA_SxCR_PINC_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | MINC | 10:10 | 0x400 | Increment memory/destination address after each transfer. | header:DMA_SxCR_MINC_Msk; header:DMA_SxCR_MINC_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | PSIZE | 12:11 | 0x1800 | 0 byte, 1 halfword, 2 word; 3 reserved. Source width in memory-to-memory. | header:DMA_SxCR_PSIZE_Msk; header:DMA_SxCR_PSIZE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | MSIZE | 14:13 | 0x6000 | 0 byte, 1 halfword, 2 word; 3 reserved. Destination width in memory-to-memory. | header:DMA_SxCR_MSIZE_Msk; header:DMA_SxCR_MSIZE_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | PINCOS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PINCOS_Msk; header:DMA_SxCR_PINCOS_Msk |
| CR | PL | 17:16 | 0x30000 | Stream priority, 0 low through 3 very high. | header:DMA_SxCR_PL_Msk; header:DMA_SxCR_PL_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | DBM | 18:18 | 0x40000 | Double-buffer mode; excluded from the supported memory-copy mode. | header:DMA_SxCR_DBM_Msk; header:DMA_SxCR_DBM_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | CT | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_CT_Msk; header:DMA_SxCR_CT_Msk |
| CR | ACK | 20:20 | 0x100000 | Declaration conflict resolved by fact authority: RM0090 reserves bit 20 on this target; keep zero, do not use the header ACK symbol. | header:DMA_SxCR_ACK_Msk; header:DMA_SxCR_ACK_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | PBURST | 22:21 | 0x600000 | Peripheral burst selection; 0 single transfer for the supported mode. | header:DMA_SxCR_PBURST_Msk; header:DMA_SxCR_PBURST_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | MBURST | 24:23 | 0x1800000 | Memory burst selection; 0 single transfer for the supported mode. | header:DMA_SxCR_MBURST_Msk; header:DMA_SxCR_MBURST_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| CR | CHSEL | 27:25 | 0xE000000 | Channel selection; irrelevant to memory-to-memory requests. | header:DMA_SxCR_CHSEL_Msk; header:DMA_SxCR_CHSEL_Msk; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332 |
| PAR | PA | 31:0 | 0xFFFFFFFF | Peripheral address; source address in memory-to-memory. | header:DMA_SxPAR_PA_Msk; header:DMA_SxPAR_PA_Msk; rm_features_333:page:333 |
| M0AR | M0A | 31:0 | 0xFFFFFFFF | Memory bank 0 address; destination in memory-to-memory. | header:DMA_SxM0AR_M0A_Msk; header:DMA_SxM0AR_M0A_Msk; rm_features_334:page:334 |
| M1AR | M1A | 31:0 | 0xFFFFFFFF | Memory bank 1 address for double buffering, excluded from the reviewed copy mode. | header:DMA_SxM1AR_M1A_Msk; header:DMA_SxM1AR_M1A_Msk; rm_features_334:page:334 |
| FCR | FTH | 1:0 | 0x3 | FIFO threshold: 0 quarter, 1 half, 2 three quarters, 3 full. | header:DMA_SxFCR_FTH_Msk; header:DMA_SxFCR_FTH_Msk; rm_features_335:page:335; rm_features_336:page:336 |
| FCR | DMDIS | 2:2 | 0x4 | 1 enables FIFO (disables direct mode); mandatory for memory-to-memory. | header:DMA_SxFCR_DMDIS_Msk; header:DMA_SxFCR_DMDIS_Msk; rm_features_335:page:335; rm_features_336:page:336 |
| FCR | FS | 5:3 | 0x38 | Read-only FIFO fill status. | header:DMA_SxFCR_FS_Msk; header:DMA_SxFCR_FS_Msk; rm_features_335:page:335; rm_features_336:page:336 |
| FCR | FEIE | 7:7 | 0x80 | FIFO-error interrupt enable. | header:DMA_SxFCR_FEIE_Msk; header:DMA_SxFCR_FEIE_Msk; rm_features_335:page:335; rm_features_336:page:336 |

## Reviewed operating semantics

Only DMA2 supports the reviewed memory-to-memory mode. DMA1 is excluded. Use PAR as source, M0AR as destination, equal word widths, increments, FIFO, single bursts and a bounded item count. Buffers must be approved DMA-reachable memory; a C pointer value does not prove reachability.

Disable and wait for EN=0 before writing protected configuration. Clear flags through [[peripherals/dma]], configure, then set EN last. Completion polling must test errors and expire. Peripheral shutdown must follow stream disable/acknowledgement.

**Resolved source conflict:** the CMSIS header declares DMA_SxCR_ACK at bit 20. RM0090 pp.330–332 reserves that bit for this target. Header authority establishes the declaration, while the operating manual governs use: keep it zero.

Circular mode, direct mode, double buffering, peripheral handshakes and peripheral DMA routing are outside this memory-copy contract. See [[features]] and [[coverage]].

Evidence: rm_features_306:page:306, rm_features_311:page:311, rm_features_313:page:313, rm_features_324:page:324, rm_features_325:page:325, rm_features_330:page:330, rm_features_331:page:331, rm_features_332:page:332, rm_features_333:page:333, rm_features_334:page:334, rm_features_335:page:335, rm_features_336:page:336. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| memory_copy_polling | DMA2_Stream0, DMA2_Stream1, DMA2_Stream2, DMA2_Stream3, DMA2_Stream4, DMA2_Stream5, DMA2_Stream6, DMA2_Stream7 | CR, NDTR, PAR, M0AR, FCR | CR: EN, DIR, PFCTRL, CIRC, PINC, MINC, PSIZE, MSIZE, DBM, PBURST, MBURST; FCR: DMDIS, FTH, FS; M0AR: M0A; PAR: PA | Only DMA2 supports memory-to-memory; DMA1 is explicitly excluded.<br>Use validated DMA-reachable source/destination buffers and 32-bit alignment; address existence alone is insufficient.<br>Disable the stream and wait for EN=0 before setting protected fields; clear that stream flags.<br>Select DIR=2, PSIZE=MSIZE=2, PINC=MINC=1, PFCTRL=CIRC=DBM=0 and single bursts.<br>Set NDTR in 1..65535 items; PAR is source and M0AR is destination.<br>Enable FIFO with a compatible threshold; direct mode and circular mode are forbidden.<br>Enable EN last, bound completion waits and fail on transfer/FIFO/direct-mode errors.<br>Disable and wait for EN=0 before reconfiguration or disabling an attached peripheral. | rm_features_306:page:306; rm_features_311:page:311; rm_features_313:page:313; rm_features_324:page:324; rm_features_325:page:325; rm_features_330:page:330; rm_features_331:page:331; rm_features_332:page:332; rm_features_333:page:333; rm_features_334:page:334; rm_features_335:page:335; rm_features_336:page:336 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
