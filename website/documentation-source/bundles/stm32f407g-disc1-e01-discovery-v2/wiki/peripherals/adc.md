# ADC — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC1 | 0x40012000 | Not asserted | Not asserted | header:ADC1_BASE |
| ADC2 | 0x40012100 | Not asserted | Not asserted | header:ADC2_BASE |
| ADC3 | 0x40012200 | Not asserted | Not asserted | header:ADC3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SR; header:ADC_TypeDef.SR |
| CR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR1; header:ADC_TypeDef.CR1 |
| CR2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR2; header:ADC_TypeDef.CR2 |
| SMPR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR1; header:ADC_TypeDef.SMPR1 |
| SMPR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR2; header:ADC_TypeDef.SMPR2 |
| JOFR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR1; header:ADC_TypeDef.JOFR1 |
| JOFR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR2; header:ADC_TypeDef.JOFR2 |
| JOFR3 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR3; header:ADC_TypeDef.JOFR3 |
| JOFR4 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR4; header:ADC_TypeDef.JOFR4 |
| HTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR; header:ADC_TypeDef.HTR |
| LTR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR; header:ADC_TypeDef.LTR |
| SQR1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR1; header:ADC_TypeDef.SQR1 |
| SQR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR2; header:ADC_TypeDef.SQR2 |
| SQR3 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR3; header:ADC_TypeDef.SQR3 |
| JSQR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JSQR; header:ADC_TypeDef.JSQR |
| JDR1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR1; header:ADC_TypeDef.JDR1 |
| JDR2 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR2; header:ADC_TypeDef.JDR2 |
| JDR3 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR3; header:ADC_TypeDef.JDR3 |
| JDR4 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR4; header:ADC_TypeDef.JDR4 |
| DR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.DR; header:ADC_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | AWD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_AWD_Msk; header:ADC_SR_AWD_Msk |
| SR | EOC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_EOC_Msk; header:ADC_SR_EOC_Msk |
| SR | JEOC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JEOC_Msk; header:ADC_SR_JEOC_Msk |
| SR | JSTRT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JSTRT_Msk; header:ADC_SR_JSTRT_Msk |
| SR | STRT | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_STRT_Msk; header:ADC_SR_STRT_Msk |
| SR | OVR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_OVR_Msk; header:ADC_SR_OVR_Msk |
| CR1 | AWDCH | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDCH_Msk; header:ADC_CR1_AWDCH_Msk |
| CR1 | EOCIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_EOCIE_Msk; header:ADC_CR1_EOCIE_Msk |
| CR1 | AWDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDIE_Msk; header:ADC_CR1_AWDIE_Msk |
| CR1 | JEOCIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JEOCIE_Msk; header:ADC_CR1_JEOCIE_Msk |
| CR1 | SCAN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_SCAN_Msk; header:ADC_CR1_SCAN_Msk |
| CR1 | AWDSGL | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDSGL_Msk; header:ADC_CR1_AWDSGL_Msk |
| CR1 | JAUTO | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAUTO_Msk; header:ADC_CR1_JAUTO_Msk |
| CR1 | DISCEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCEN_Msk; header:ADC_CR1_DISCEN_Msk |
| CR1 | JDISCEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JDISCEN_Msk; header:ADC_CR1_JDISCEN_Msk |
| CR1 | DISCNUM | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCNUM_Msk; header:ADC_CR1_DISCNUM_Msk |
| CR1 | JAWDEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAWDEN_Msk; header:ADC_CR1_JAWDEN_Msk |
| CR1 | AWDEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDEN_Msk; header:ADC_CR1_AWDEN_Msk |
| CR1 | RES | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_RES_Msk; header:ADC_CR1_RES_Msk |
| CR1 | OVRIE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_OVRIE_Msk; header:ADC_CR1_OVRIE_Msk |
| CR2 | ADON | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_ADON_Msk; header:ADC_CR2_ADON_Msk |
| CR2 | CONT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_CONT_Msk; header:ADC_CR2_CONT_Msk |
| CR2 | DMA | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_DMA_Msk; header:ADC_CR2_DMA_Msk |
| CR2 | DDS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_DDS_Msk; header:ADC_CR2_DDS_Msk |
| CR2 | EOCS | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EOCS_Msk; header:ADC_CR2_EOCS_Msk |
| CR2 | ALIGN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_ALIGN_Msk; header:ADC_CR2_ALIGN_Msk |
| CR2 | JEXTSEL | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTSEL_Msk; header:ADC_CR2_JEXTSEL_Msk |
| CR2 | JEXTEN | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTEN_Msk; header:ADC_CR2_JEXTEN_Msk |
| CR2 | JSWSTART | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JSWSTART_Msk; header:ADC_CR2_JSWSTART_Msk |
| CR2 | EXTSEL | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EXTSEL_Msk; header:ADC_CR2_EXTSEL_Msk |
| CR2 | EXTEN | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EXTEN_Msk; header:ADC_CR2_EXTEN_Msk |
| CR2 | SWSTART | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_SWSTART_Msk; header:ADC_CR2_SWSTART_Msk |
| SMPR1 | SMP10 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP10_Msk; header:ADC_SMPR1_SMP10_Msk |
| SMPR1 | SMP11 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP11_Msk; header:ADC_SMPR1_SMP11_Msk |
| SMPR1 | SMP12 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP12_Msk; header:ADC_SMPR1_SMP12_Msk |
| SMPR1 | SMP13 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP13_Msk; header:ADC_SMPR1_SMP13_Msk |
| SMPR1 | SMP14 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP14_Msk; header:ADC_SMPR1_SMP14_Msk |
| SMPR1 | SMP15 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP15_Msk; header:ADC_SMPR1_SMP15_Msk |
| SMPR1 | SMP16 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP16_Msk; header:ADC_SMPR1_SMP16_Msk |
| SMPR1 | SMP17 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP17_Msk; header:ADC_SMPR1_SMP17_Msk |
| SMPR1 | SMP18 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP18_Msk; header:ADC_SMPR1_SMP18_Msk |
| SMPR2 | SMP0 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP0_Msk; header:ADC_SMPR2_SMP0_Msk |
| SMPR2 | SMP1 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP1_Msk; header:ADC_SMPR2_SMP1_Msk |
| SMPR2 | SMP2 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP2_Msk; header:ADC_SMPR2_SMP2_Msk |
| SMPR2 | SMP3 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP3_Msk; header:ADC_SMPR2_SMP3_Msk |
| SMPR2 | SMP4 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP4_Msk; header:ADC_SMPR2_SMP4_Msk |
| SMPR2 | SMP5 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP5_Msk; header:ADC_SMPR2_SMP5_Msk |
| SMPR2 | SMP6 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP6_Msk; header:ADC_SMPR2_SMP6_Msk |
| SMPR2 | SMP7 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP7_Msk; header:ADC_SMPR2_SMP7_Msk |
| SMPR2 | SMP8 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP8_Msk; header:ADC_SMPR2_SMP8_Msk |
| SMPR2 | SMP9 | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP9_Msk; header:ADC_SMPR2_SMP9_Msk |
| JOFR1 | JOFFSET1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR1_JOFFSET1_Msk; header:ADC_JOFR1_JOFFSET1_Msk |
| JOFR2 | JOFFSET2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR2_JOFFSET2_Msk; header:ADC_JOFR2_JOFFSET2_Msk |
| JOFR3 | JOFFSET3 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR3_JOFFSET3_Msk; header:ADC_JOFR3_JOFFSET3_Msk |
| JOFR4 | JOFFSET4 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR4_JOFFSET4_Msk; header:ADC_JOFR4_JOFFSET4_Msk |
| HTR | HT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_HTR_HT_Msk; header:ADC_HTR_HT_Msk |
| LTR | LT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_LTR_LT_Msk; header:ADC_LTR_LT_Msk |
| SQR1 | SQ13 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ13_Msk; header:ADC_SQR1_SQ13_Msk |
| SQR1 | SQ14 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ14_Msk; header:ADC_SQR1_SQ14_Msk |
| SQR1 | SQ15 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ15_Msk; header:ADC_SQR1_SQ15_Msk |
| SQR1 | SQ16 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ16_Msk; header:ADC_SQR1_SQ16_Msk |
| SQR1 | L | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_L_Msk; header:ADC_SQR1_L_Msk |
| SQR2 | SQ7 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ7_Msk; header:ADC_SQR2_SQ7_Msk |
| SQR2 | SQ8 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ8_Msk; header:ADC_SQR2_SQ8_Msk |
| SQR2 | SQ9 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ9_Msk; header:ADC_SQR2_SQ9_Msk |
| SQR2 | SQ10 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ10_Msk; header:ADC_SQR2_SQ10_Msk |
| SQR2 | SQ11 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ11_Msk; header:ADC_SQR2_SQ11_Msk |
| SQR2 | SQ12 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ12_Msk; header:ADC_SQR2_SQ12_Msk |
| SQR3 | SQ1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ1_Msk; header:ADC_SQR3_SQ1_Msk |
| SQR3 | SQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ2_Msk; header:ADC_SQR3_SQ2_Msk |
| SQR3 | SQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ3_Msk; header:ADC_SQR3_SQ3_Msk |
| SQR3 | SQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ4_Msk; header:ADC_SQR3_SQ4_Msk |
| SQR3 | SQ5 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ5_Msk; header:ADC_SQR3_SQ5_Msk |
| SQR3 | SQ6 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ6_Msk; header:ADC_SQR3_SQ6_Msk |
| JSQR | JSQ1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ1_Msk; header:ADC_JSQR_JSQ1_Msk |
| JSQR | JSQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ2_Msk; header:ADC_JSQR_JSQ2_Msk |
| JSQR | JSQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ3_Msk; header:ADC_JSQR_JSQ3_Msk |
| JSQR | JSQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ4_Msk; header:ADC_JSQR_JSQ4_Msk |
| JSQR | JL | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JL_Msk; header:ADC_JSQR_JL_Msk |
| JDR1 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR1_JDATA_Msk; header:ADC_JDR1_JDATA_Msk |
| JDR2 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR2_JDATA_Msk; header:ADC_JDR2_JDATA_Msk |
| JDR3 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR3_JDATA_Msk; header:ADC_JDR3_JDATA_Msk |
| JDR4 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR4_JDATA_Msk; header:ADC_JDR4_JDATA_Msk |
| DR | DATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_DATA_Msk; header:ADC_DR_DATA_Msk |
| DR | ADC2DATA | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_ADC2DATA_Msk; header:ADC_DR_ADC2DATA_Msk |

## Operating semantics unavailable

**adc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
