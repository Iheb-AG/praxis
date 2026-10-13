# DMA_STREAM — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/dma]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA1_Stream0 | 0x40026010 | Not asserted | Not asserted | header:DMA1_Stream0_BASE |
| DMA1_Stream1 | 0x40026028 | Not asserted | Not asserted | header:DMA1_Stream1_BASE |
| DMA1_Stream2 | 0x40026040 | Not asserted | Not asserted | header:DMA1_Stream2_BASE |
| DMA1_Stream3 | 0x40026058 | Not asserted | Not asserted | header:DMA1_Stream3_BASE |
| DMA1_Stream4 | 0x40026070 | Not asserted | Not asserted | header:DMA1_Stream4_BASE |
| DMA1_Stream5 | 0x40026088 | Not asserted | Not asserted | header:DMA1_Stream5_BASE |
| DMA1_Stream6 | 0x400260A0 | Not asserted | Not asserted | header:DMA1_Stream6_BASE |
| DMA1_Stream7 | 0x400260B8 | Not asserted | Not asserted | header:DMA1_Stream7_BASE |
| DMA2_Stream0 | 0x40026410 | Not asserted | Not asserted | header:DMA2_Stream0_BASE |
| DMA2_Stream1 | 0x40026428 | Not asserted | Not asserted | header:DMA2_Stream1_BASE |
| DMA2_Stream2 | 0x40026440 | Not asserted | Not asserted | header:DMA2_Stream2_BASE |
| DMA2_Stream3 | 0x40026458 | Not asserted | Not asserted | header:DMA2_Stream3_BASE |
| DMA2_Stream4 | 0x40026470 | Not asserted | Not asserted | header:DMA2_Stream4_BASE |
| DMA2_Stream5 | 0x40026488 | Not asserted | Not asserted | header:DMA2_Stream5_BASE |
| DMA2_Stream6 | 0x400264A0 | Not asserted | Not asserted | header:DMA2_Stream6_BASE |
| DMA2_Stream7 | 0x400264B8 | Not asserted | Not asserted | header:DMA2_Stream7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.CR; header:DMA_Stream_TypeDef.CR |
| NDTR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.NDTR; header:DMA_Stream_TypeDef.NDTR |
| PAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.PAR; header:DMA_Stream_TypeDef.PAR |
| M0AR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.M0AR; header:DMA_Stream_TypeDef.M0AR |
| M1AR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.M1AR; header:DMA_Stream_TypeDef.M1AR |
| FCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA_Stream_TypeDef.FCR; header:DMA_Stream_TypeDef.FCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_EN_Msk; header:DMA_SxCR_EN_Msk |
| CR | DMEIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_DMEIE_Msk; header:DMA_SxCR_DMEIE_Msk |
| CR | TEIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_TEIE_Msk; header:DMA_SxCR_TEIE_Msk |
| CR | HTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_HTIE_Msk; header:DMA_SxCR_HTIE_Msk |
| CR | TCIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_TCIE_Msk; header:DMA_SxCR_TCIE_Msk |
| CR | PFCTRL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PFCTRL_Msk; header:DMA_SxCR_PFCTRL_Msk |
| CR | DIR | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_DIR_Msk; header:DMA_SxCR_DIR_Msk |
| CR | CIRC | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_CIRC_Msk; header:DMA_SxCR_CIRC_Msk |
| CR | PINC | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PINC_Msk; header:DMA_SxCR_PINC_Msk |
| CR | MINC | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_MINC_Msk; header:DMA_SxCR_MINC_Msk |
| CR | PSIZE | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PSIZE_Msk; header:DMA_SxCR_PSIZE_Msk |
| CR | MSIZE | 14:13 | 0x6000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_MSIZE_Msk; header:DMA_SxCR_MSIZE_Msk |
| CR | PINCOS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PINCOS_Msk; header:DMA_SxCR_PINCOS_Msk |
| CR | PL | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PL_Msk; header:DMA_SxCR_PL_Msk |
| CR | DBM | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_DBM_Msk; header:DMA_SxCR_DBM_Msk |
| CR | CT | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_CT_Msk; header:DMA_SxCR_CT_Msk |
| CR | ACK | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_ACK_Msk; header:DMA_SxCR_ACK_Msk |
| CR | PBURST | 22:21 | 0x600000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_PBURST_Msk; header:DMA_SxCR_PBURST_Msk |
| CR | MBURST | 24:23 | 0x1800000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_MBURST_Msk; header:DMA_SxCR_MBURST_Msk |
| CR | CHSEL | 27:25 | 0xE000000 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxCR_CHSEL_Msk; header:DMA_SxCR_CHSEL_Msk |
| PAR | PA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA_SxPAR_PA_Msk; header:DMA_SxPAR_PA_Msk |
| M0AR | M0A | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA_SxM0AR_M0A_Msk; header:DMA_SxM0AR_M0A_Msk |
| M1AR | M1A | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA_SxM1AR_M1A_Msk; header:DMA_SxM1AR_M1A_Msk |
| FCR | FTH | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxFCR_FTH_Msk; header:DMA_SxFCR_FTH_Msk |
| FCR | DMDIS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxFCR_DMDIS_Msk; header:DMA_SxFCR_DMDIS_Msk |
| FCR | FS | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxFCR_FS_Msk; header:DMA_SxFCR_FS_Msk |
| FCR | FEIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DMA_SxFCR_FEIE_Msk; header:DMA_SxFCR_FEIE_Msk |

## Operating semantics unavailable

**dma_stream: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
