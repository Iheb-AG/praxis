# ADC — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC1 | 0x40012400 | Not asserted | Not asserted | header:ADC1_BASE |
| ADC2 | 0x40012800 | Not asserted | Not asserted | header:ADC2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SR |
| CR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR1 |
| CR2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR2 |
| SMPR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR1 |
| SMPR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR2 |
| JOFR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR1 |
| JOFR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR2 |
| JOFR3 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR3 |
| JOFR4 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR4 |
| HTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR |
| LTR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR |
| SQR1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR1 |
| SQR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR2 |
| SQR3 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR3 |
| JSQR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JSQR |
| JDR1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR1 |
| JDR2 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR2 |
| JDR3 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR3 |
| JDR4 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR4 |
| DR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | AWD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_AWD_Msk |
| SR | EOS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_EOS_Msk |
| SR | JEOS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JEOS_Msk |
| SR | JSTRT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JSTRT_Msk |
| SR | STRT | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_STRT_Msk |
| CR1 | AWDCH | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDCH_Msk |
| CR1 | EOSIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_EOSIE_Msk |
| CR1 | AWDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDIE_Msk |
| CR1 | JEOSIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JEOSIE_Msk |
| CR1 | SCAN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_SCAN_Msk |
| CR1 | AWDSGL | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDSGL_Msk |
| CR1 | JAUTO | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAUTO_Msk |
| CR1 | DISCEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCEN_Msk |
| CR1 | JDISCEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JDISCEN_Msk |
| CR1 | DISCNUM | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCNUM_Msk |
| CR1 | DUALMOD | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DUALMOD_Msk |
| CR1 | JAWDEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAWDEN_Msk |
| CR1 | AWDEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDEN_Msk |
| CR2 | ADON | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_ADON_Msk |
| CR2 | CONT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_CONT_Msk |
| CR2 | CAL | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_CAL_Msk |
| CR2 | RSTCAL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_RSTCAL_Msk |
| CR2 | DMA | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_DMA_Msk |
| CR2 | ALIGN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_ALIGN_Msk |
| CR2 | JEXTSEL | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTSEL_Msk |
| CR2 | JEXTTRIG | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTTRIG_Msk |
| CR2 | EXTSEL | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EXTSEL_Msk |
| CR2 | EXTTRIG | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EXTTRIG_Msk |
| CR2 | JSWSTART | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JSWSTART_Msk |
| CR2 | SWSTART | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_SWSTART_Msk |
| CR2 | TSVREFE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_TSVREFE_Msk |
| SMPR1 | SMP10 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP10_Msk |
| SMPR1 | SMP11 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP11_Msk |
| SMPR1 | SMP12 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP12_Msk |
| SMPR1 | SMP13 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP13_Msk |
| SMPR1 | SMP14 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP14_Msk |
| SMPR1 | SMP15 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP15_Msk |
| SMPR1 | SMP16 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP16_Msk |
| SMPR1 | SMP17 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP17_Msk |
| SMPR2 | SMP0 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP0_Msk |
| SMPR2 | SMP1 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP1_Msk |
| SMPR2 | SMP2 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP2_Msk |
| SMPR2 | SMP3 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP3_Msk |
| SMPR2 | SMP4 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP4_Msk |
| SMPR2 | SMP5 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP5_Msk |
| SMPR2 | SMP6 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP6_Msk |
| SMPR2 | SMP7 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP7_Msk |
| SMPR2 | SMP8 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP8_Msk |
| SMPR2 | SMP9 | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP9_Msk |
| JOFR1 | JOFFSET1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR1_JOFFSET1_Msk |
| JOFR2 | JOFFSET2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR2_JOFFSET2_Msk |
| JOFR3 | JOFFSET3 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR3_JOFFSET3_Msk |
| JOFR4 | JOFFSET4 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR4_JOFFSET4_Msk |
| HTR | HT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_HTR_HT_Msk |
| LTR | LT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_LTR_LT_Msk |
| SQR1 | SQ13 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ13_Msk |
| SQR1 | SQ14 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ14_Msk |
| SQR1 | SQ15 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ15_Msk |
| SQR1 | SQ16 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ16_Msk |
| SQR1 | L | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_L_Msk |
| SQR2 | SQ7 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ7_Msk |
| SQR2 | SQ8 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ8_Msk |
| SQR2 | SQ9 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ9_Msk |
| SQR2 | SQ10 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ10_Msk |
| SQR2 | SQ11 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ11_Msk |
| SQR2 | SQ12 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ12_Msk |
| SQR3 | SQ1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ1_Msk |
| SQR3 | SQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ2_Msk |
| SQR3 | SQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ3_Msk |
| SQR3 | SQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ4_Msk |
| SQR3 | SQ5 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ5_Msk |
| SQR3 | SQ6 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ6_Msk |
| JSQR | JSQ1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ1_Msk |
| JSQR | JSQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ2_Msk |
| JSQR | JSQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ3_Msk |
| JSQR | JSQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ4_Msk |
| JSQR | JL | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JL_Msk |
| JDR1 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR1_JDATA_Msk |
| JDR2 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR2_JDATA_Msk |
| JDR3 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR3_JDATA_Msk |
| JDR4 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR4_JDATA_Msk |
| DR | DATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_DATA_Msk |
| DR | ADC2DATA | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_ADC2DATA_Msk |

## Operating semantics unavailable

**adc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
