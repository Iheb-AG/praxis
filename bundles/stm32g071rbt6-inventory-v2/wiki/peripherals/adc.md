# ADC — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC1 | 0x40012400 | Not asserted | Not asserted | header:ADC1_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.ISR |
| IER | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.IER |
| CR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CR |
| CFGR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CFGR1 |
| CFGR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CFGR2 |
| SMPR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SMPR |
| AWD1TR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD1TR |
| AWD2TR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD2TR |
| CHSELR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CHSELR |
| AWD3TR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD3TR |
| DR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.DR |
| AWD2CR | 0x0A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD2CR |
| AWD3CR | 0x0A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.AWD3CR |
| CALFACT | 0x0B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.CALFACT |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISR | ADRDY | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_ADRDY_Msk |
| ISR | EOSMP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOSMP_Msk |
| ISR | EOC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOC_Msk |
| ISR | EOS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOS_Msk |
| ISR | OVR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_OVR_Msk |
| ISR | AWD1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD1_Msk |
| ISR | AWD2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD2_Msk |
| ISR | AWD3 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_AWD3_Msk |
| ISR | EOCAL | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_EOCAL_Msk |
| ISR | CCRDY | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_ISR_CCRDY_Msk |
| IER | ADRDYIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_ADRDYIE_Msk |
| IER | EOSMPIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOSMPIE_Msk |
| IER | EOCIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOCIE_Msk |
| IER | EOSIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOSIE_Msk |
| IER | OVRIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_OVRIE_Msk |
| IER | AWD1IE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD1IE_Msk |
| IER | AWD2IE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD2IE_Msk |
| IER | AWD3IE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_AWD3IE_Msk |
| IER | EOCALIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_EOCALIE_Msk |
| IER | CCRDYIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_IER_CCRDYIE_Msk |
| CR | ADEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADEN_Msk |
| CR | ADDIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADDIS_Msk |
| CR | ADSTART | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADSTART_Msk |
| CR | ADSTP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADSTP_Msk |
| CR | ADVREGEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADVREGEN_Msk |
| CR | ADCAL | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR_ADCAL_Msk |
| CFGR1 | DMAEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_DMAEN_Msk |
| CFGR1 | DMACFG | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_DMACFG_Msk |
| CFGR1 | SCANDIR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_SCANDIR_Msk |
| CFGR1 | RES | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_RES_Msk |
| CFGR1 | ALIGN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_ALIGN_Msk |
| CFGR1 | EXTSEL | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_EXTSEL_Msk |
| CFGR1 | EXTEN | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_EXTEN_Msk |
| CFGR1 | OVRMOD | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_OVRMOD_Msk |
| CFGR1 | CONT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_CONT_Msk |
| CFGR1 | WAIT | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_WAIT_Msk |
| CFGR1 | AUTOFF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_AUTOFF_Msk |
| CFGR1 | DISCEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_DISCEN_Msk |
| CFGR1 | CHSELRMOD | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_CHSELRMOD_Msk |
| CFGR1 | AWD1SGL | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_AWD1SGL_Msk |
| CFGR1 | AWD1EN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_AWD1EN_Msk |
| CFGR1 | AWD1CH | 30:26 | 0x7C000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR1_AWD1CH_Msk |
| CFGR2 | OVSE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_OVSE_Msk |
| CFGR2 | OVSR | 4:2 | 0x1C | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_OVSR_Msk |
| CFGR2 | OVSS | 8:5 | 0x1E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_OVSS_Msk |
| CFGR2 | TOVS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_TOVS_Msk |
| CFGR2 | LFTRIG | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_LFTRIG_Msk |
| CFGR2 | CKMODE | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CFGR2_CKMODE_Msk |
| SMPR | SMP1 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR_SMP1_Msk |
| SMPR | SMP2 | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR_SMP2_Msk |
| SMPR | SMPSEL | 26:8 | 0x7FFFF00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR_SMPSEL_Msk |
| AWD1TR | LT1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD1TR_LT1_Msk |
| AWD1TR | HT1 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD1TR_HT1_Msk |
| AWD2TR | LT2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD2TR_LT2_Msk |
| AWD2TR | HT2 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD2TR_HT2_Msk |
| CHSELR | SQ_ALL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_CHSELR_SQ_ALL_Msk |
| AWD3TR | LT3 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD3TR_LT3_Msk |
| AWD3TR | HT3 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD3TR_HT3_Msk |
| DR | DATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_DATA_Msk |
| AWD2CR | AWD2CH | 18:0 | 0x7FFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD2CR_AWD2CH_Msk |
| AWD3CR | AWD3CH | 18:0 | 0x7FFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_AWD3CR_AWD3CH_Msk |
| CALFACT | CALFACT | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:ADC_CALFACT_CALFACT_Msk |

## Operating semantics unavailable

**adc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
