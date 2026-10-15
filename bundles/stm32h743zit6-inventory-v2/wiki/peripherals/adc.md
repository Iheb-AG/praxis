# ADC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC1 | 0x40022000 | Not asserted | Not asserted | header:ADC1_BASE |
| ADC2 | 0x40022100 | Not asserted | Not asserted | header:ADC2_BASE |
| ADC3 | 0x58026000 | Not asserted | Not asserted | header:ADC3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.ISR |
| IER | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.IER |
| CR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR |
| CFGR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CFGR |
| CFGR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CFGR2 |
| SMPR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR1 |
| SMPR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR2 |
| PCSEL | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.PCSEL |
| LTR1 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR1 |
| HTR1 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR1 |
| SQR1 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR1 |
| SQR2 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR2 |
| SQR3 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR3 |
| SQR4 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR4 |
| DR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.DR |
| JSQR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JSQR |
| OFR1 | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.OFR1 |
| OFR2 | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.OFR2 |
| OFR3 | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.OFR3 |
| OFR4 | 0x06C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.OFR4 |
| JDR1 | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR1 |
| JDR2 | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR2 |
| JDR3 | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR3 |
| JDR4 | 0x08C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR4 |
| AWD2CR | 0x0A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD2CR |
| AWD3CR | 0x0A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD3CR |
| LTR2 | 0x0B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR2 |
| HTR2 | 0x0B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR2 |
| LTR3 | 0x0B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR3 |
| HTR3 | 0x0BC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR3 |
| DIFSEL | 0x0C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.DIFSEL |
| CALFACT | 0x0C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CALFACT |
| CALFACT2 | 0x0C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CALFACT2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISR | ADRDY | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_ADRDY_Msk |
| ISR | EOSMP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOSMP_Msk |
| ISR | EOC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOC_Msk |
| ISR | EOS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOS_Msk |
| ISR | OVR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_OVR_Msk |
| ISR | JEOC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_JEOC_Msk |
| ISR | JEOS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_JEOS_Msk |
| ISR | AWD1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD1_Msk |
| ISR | AWD2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD2_Msk |
| ISR | AWD3 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD3_Msk |
| ISR | JQOVF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_JQOVF_Msk |
| ISR | LDORDY | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_LDORDY_Msk |
| IER | ADRDYIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_ADRDYIE_Msk |
| IER | EOSMPIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOSMPIE_Msk |
| IER | EOCIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOCIE_Msk |
| IER | EOSIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOSIE_Msk |
| IER | OVRIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_OVRIE_Msk |
| IER | JEOCIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_JEOCIE_Msk |
| IER | JEOSIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_JEOSIE_Msk |
| IER | AWD1IE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD1IE_Msk |
| IER | AWD2IE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD2IE_Msk |
| IER | AWD3IE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD3IE_Msk |
| IER | JQOVFIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_JQOVFIE_Msk |
| CR | ADEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADEN_Msk |
| CR | ADDIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADDIS_Msk |
| CR | ADSTART | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADSTART_Msk |
| CR | JADSTART | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_JADSTART_Msk |
| CR | ADSTP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADSTP_Msk |
| CR | JADSTP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_JADSTP_Msk |
| CR | BOOST | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_BOOST_Msk |
| CR | ADCALLIN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADCALLIN_Msk |
| CR | LINCALRDYW1 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW1_Msk |
| CR | LINCALRDYW2 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW2_Msk |
| CR | LINCALRDYW3 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW3_Msk |
| CR | LINCALRDYW4 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW4_Msk |
| CR | LINCALRDYW5 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW5_Msk |
| CR | LINCALRDYW6 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_LINCALRDYW6_Msk |
| CR | ADVREGEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADVREGEN_Msk |
| CR | DEEPPWD | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_DEEPPWD_Msk |
| CR | ADCALDIF | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADCALDIF_Msk |
| CR | ADCAL | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADCAL_Msk |
| CFGR | DMNGT | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_DMNGT_Msk |
| CFGR | RES | 4:2 | 0x1C | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_RES_Msk |
| CFGR | EXTSEL | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_EXTSEL_Msk |
| CFGR | EXTEN | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_EXTEN_Msk |
| CFGR | OVRMOD | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_OVRMOD_Msk |
| CFGR | CONT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_CONT_Msk |
| CFGR | AUTDLY | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_AUTDLY_Msk |
| CFGR | DISCEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_DISCEN_Msk |
| CFGR | DISCNUM | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_DISCNUM_Msk |
| CFGR | JDISCEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_JDISCEN_Msk |
| CFGR | JQM | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_JQM_Msk |
| CFGR | AWD1SGL | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_AWD1SGL_Msk |
| CFGR | AWD1EN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_AWD1EN_Msk |
| CFGR | JAWD1EN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_JAWD1EN_Msk |
| CFGR | JAUTO | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_JAUTO_Msk |
| CFGR | AWD1CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_AWD1CH_Msk |
| CFGR | JQDIS | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR_JQDIS_Msk |
| CFGR2 | ROVSE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_ROVSE_Msk |
| CFGR2 | JOVSE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_JOVSE_Msk |
| CFGR2 | OVSS | 8:5 | 0x1E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_OVSS_Msk |
| CFGR2 | TROVS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_TROVS_Msk |
| CFGR2 | ROVSM | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_ROVSM_Msk |
| CFGR2 | RSHIFT1 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_RSHIFT1_Msk |
| CFGR2 | RSHIFT2 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_RSHIFT2_Msk |
| CFGR2 | RSHIFT3 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_RSHIFT3_Msk |
| CFGR2 | RSHIFT4 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_RSHIFT4_Msk |
| CFGR2 | OVSR | 25:16 | 0x3FF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_OVSR_Msk |
| CFGR2 | LSHIFT | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_LSHIFT_Msk |
| SMPR1 | SMP0 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP0_Msk |
| SMPR1 | SMP1 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP1_Msk |
| SMPR1 | SMP2 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP2_Msk |
| SMPR1 | SMP3 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP3_Msk |
| SMPR1 | SMP4 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP4_Msk |
| SMPR1 | SMP5 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP5_Msk |
| SMPR1 | SMP6 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP6_Msk |
| SMPR1 | SMP7 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP7_Msk |
| SMPR1 | SMP8 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP8_Msk |
| SMPR1 | SMP9 | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP9_Msk |
| SMPR2 | SMP10 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP10_Msk |
| SMPR2 | SMP11 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP11_Msk |
| SMPR2 | SMP12 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP12_Msk |
| SMPR2 | SMP13 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP13_Msk |
| SMPR2 | SMP14 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP14_Msk |
| SMPR2 | SMP15 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP15_Msk |
| SMPR2 | SMP16 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP16_Msk |
| SMPR2 | SMP17 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP17_Msk |
| SMPR2 | SMP18 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP18_Msk |
| SMPR2 | SMP19 | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP19_Msk |
| PCSEL | PCSEL | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_PCSEL_PCSEL_Msk |
| SQR1 | L | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_L_Msk |
| SQR1 | SQ1 | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ1_Msk |
| SQR1 | SQ2 | 16:12 | 0x1F000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ2_Msk |
| SQR1 | SQ3 | 22:18 | 0x7C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ3_Msk |
| SQR1 | SQ4 | 28:24 | 0x1F000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ4_Msk |
| SQR2 | SQ5 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ5_Msk |
| SQR2 | SQ6 | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ6_Msk |
| SQR2 | SQ7 | 16:12 | 0x1F000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ7_Msk |
| SQR2 | SQ8 | 22:18 | 0x7C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ8_Msk |
| SQR2 | SQ9 | 28:24 | 0x1F000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ9_Msk |
| SQR3 | SQ10 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ10_Msk |
| SQR3 | SQ11 | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ11_Msk |
| SQR3 | SQ12 | 16:12 | 0x1F000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ12_Msk |
| SQR3 | SQ13 | 22:18 | 0x7C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ13_Msk |
| SQR3 | SQ14 | 28:24 | 0x1F000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ14_Msk |
| SQR4 | SQ15 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR4_SQ15_Msk |
| SQR4 | SQ16 | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR4_SQ16_Msk |
| DR | RDATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_RDATA_Msk |
| JSQR | JL | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JL_Msk |
| JSQR | JEXTSEL | 6:2 | 0x7C | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JEXTSEL_Msk |
| JSQR | JEXTEN | 8:7 | 0x180 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JEXTEN_Msk |
| JSQR | JSQ1 | 13:9 | 0x3E00 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ1_Msk |
| JSQR | JSQ2 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ2_Msk |
| JSQR | JSQ3 | 25:21 | 0x3E00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ3_Msk |
| JSQR | JSQ4 | 31:27 | 0xF8000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ4_Msk |
| OFR1 | OFFSET1 | 25:0 | 0x3FFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR1_OFFSET1_Msk |
| OFR1 | OFFSET1_CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR1_OFFSET1_CH_Msk |
| OFR1 | SSATE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR1_SSATE_Msk |
| OFR2 | OFFSET2 | 25:0 | 0x3FFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR2_OFFSET2_Msk |
| OFR2 | OFFSET2_CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR2_OFFSET2_CH_Msk |
| OFR2 | SSATE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR2_SSATE_Msk |
| OFR3 | OFFSET3 | 25:0 | 0x3FFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR3_OFFSET3_Msk |
| OFR3 | OFFSET3_CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR3_OFFSET3_CH_Msk |
| OFR3 | SSATE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR3_SSATE_Msk |
| OFR4 | OFFSET4 | 25:0 | 0x3FFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR4_OFFSET4_Msk |
| OFR4 | OFFSET4_CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR4_OFFSET4_CH_Msk |
| OFR4 | SSATE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_OFR4_SSATE_Msk |
| JDR1 | JDATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR1_JDATA_Msk |
| JDR2 | JDATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR2_JDATA_Msk |
| JDR3 | JDATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR3_JDATA_Msk |
| JDR4 | JDATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR4_JDATA_Msk |
| AWD2CR | AWD2CH | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD2CR_AWD2CH_Msk |
| AWD3CR | AWD3CH | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD3CR_AWD3CH_Msk |
| DIFSEL | DIFSEL | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_DIFSEL_DIFSEL_Msk |
| CALFACT | CALFACT_S | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:ADC_CALFACT_CALFACT_S_Msk |
| CALFACT | CALFACT_D | 26:16 | 0x7FF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CALFACT_CALFACT_D_Msk |
| CALFACT2 | LINCALFACT | 29:0 | 0x3FFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_CALFACT2_LINCALFACT_Msk |

## Operating semantics unavailable

**adc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
