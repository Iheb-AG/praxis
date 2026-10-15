# RTC — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RTC | 0x40002800 | Not asserted | Not asserted | header:RTC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TR |
| DR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.DR |
| CR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CR |
| ISR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ISR |
| PRER | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.PRER |
| WUTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.WUTR |
| CALIBR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CALIBR |
| ALRMAR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMAR |
| ALRMBR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMBR |
| WPR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.WPR |
| SSR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SSR |
| SHIFTR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SHIFTR |
| TSTR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSTR |
| TSDR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSDR |
| TSSSR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSSSR |
| CALR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CALR |
| TAFCR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TAFCR |
| ALRMASSR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMASSR |
| ALRMBSSR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMBSSR |
| BKP0R | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP0R |
| BKP1R | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP1R |
| BKP2R | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP2R |
| BKP3R | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP3R |
| BKP4R | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP4R |
| BKP5R | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP5R |
| BKP6R | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP6R |
| BKP7R | 0x06C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP7R |
| BKP8R | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP8R |
| BKP9R | 0x074 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP9R |
| BKP10R | 0x078 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP10R |
| BKP11R | 0x07C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP11R |
| BKP12R | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP12R |
| BKP13R | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP13R |
| BKP14R | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP14R |
| BKP15R | 0x08C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP15R |
| BKP16R | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP16R |
| BKP17R | 0x094 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP17R |
| BKP18R | 0x098 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP18R |
| BKP19R | 0x09C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.BKP19R |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| TR | SU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_SU_Msk |
| TR | ST | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_ST_Msk |
| TR | MNU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_MNU_Msk |
| TR | MNT | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_MNT_Msk |
| TR | HU | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_HU_Msk |
| TR | HT | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_HT_Msk |
| TR | PM | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TR_PM_Msk |
| DR | DU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_DU_Msk |
| DR | DT | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_DT_Msk |
| DR | MU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_MU_Msk |
| DR | MT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_MT_Msk |
| DR | WDU | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_WDU_Msk |
| DR | YU | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_YU_Msk |
| DR | YT | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:RTC_DR_YT_Msk |
| CR | WUCKSEL | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_WUCKSEL_Msk |
| CR | TSEDGE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TSEDGE_Msk |
| CR | REFCKON | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_REFCKON_Msk |
| CR | BYPSHAD | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_BYPSHAD_Msk |
| CR | FMT | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_FMT_Msk |
| CR | DCE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_DCE_Msk |
| CR | ALRAE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ALRAE_Msk |
| CR | ALRBE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ALRBE_Msk |
| CR | WUTE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_WUTE_Msk |
| CR | TSE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TSE_Msk |
| CR | ALRAIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ALRAIE_Msk |
| CR | ALRBIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ALRBIE_Msk |
| CR | WUTIE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_WUTIE_Msk |
| CR | TSIE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TSIE_Msk |
| CR | ADD1H | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ADD1H_Msk |
| CR | SUB1H | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_SUB1H_Msk |
| CR | BKP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_BKP_Msk |
| CR | COSEL | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_COSEL_Msk |
| CR | POL | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_POL_Msk |
| CR | OSEL | 22:21 | 0x600000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_OSEL_Msk |
| CR | COE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_COE_Msk |
| ISR | ALRAWF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_ALRAWF_Msk |
| ISR | ALRBWF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_ALRBWF_Msk |
| ISR | WUTWF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_WUTWF_Msk |
| ISR | SHPF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_SHPF_Msk |
| ISR | INITS | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_INITS_Msk |
| ISR | RSF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_RSF_Msk |
| ISR | INITF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_INITF_Msk |
| ISR | INIT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_INIT_Msk |
| ISR | ALRAF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_ALRAF_Msk |
| ISR | ALRBF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_ALRBF_Msk |
| ISR | WUTF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_WUTF_Msk |
| ISR | TSF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_TSF_Msk |
| ISR | TSOVF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_TSOVF_Msk |
| ISR | TAMP1F | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_TAMP1F_Msk |
| ISR | TAMP2F | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_TAMP2F_Msk |
| ISR | RECALPF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ISR_RECALPF_Msk |
| PRER | PREDIV_S | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_PRER_PREDIV_S_Msk |
| PRER | PREDIV_A | 22:16 | 0x7F0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_PRER_PREDIV_A_Msk |
| WUTR | WUT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_WUTR_WUT_Msk |
| CALIBR | DC | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:RTC_CALIBR_DC_Msk |
| CALIBR | DCS | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALIBR_DCS_Msk |
| ALRMAR | SU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_SU_Msk |
| ALRMAR | ST | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_ST_Msk |
| ALRMAR | MSK1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MSK1_Msk |
| ALRMAR | MNU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MNU_Msk |
| ALRMAR | MNT | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MNT_Msk |
| ALRMAR | MSK2 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MSK2_Msk |
| ALRMAR | HU | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_HU_Msk |
| ALRMAR | HT | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_HT_Msk |
| ALRMAR | PM | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_PM_Msk |
| ALRMAR | MSK3 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MSK3_Msk |
| ALRMAR | DU | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_DU_Msk |
| ALRMAR | DT | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_DT_Msk |
| ALRMAR | WDSEL | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_WDSEL_Msk |
| ALRMAR | MSK4 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMAR_MSK4_Msk |
| ALRMBR | SU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_SU_Msk |
| ALRMBR | ST | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_ST_Msk |
| ALRMBR | MSK1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MSK1_Msk |
| ALRMBR | MNU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MNU_Msk |
| ALRMBR | MNT | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MNT_Msk |
| ALRMBR | MSK2 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MSK2_Msk |
| ALRMBR | HU | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_HU_Msk |
| ALRMBR | HT | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_HT_Msk |
| ALRMBR | PM | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_PM_Msk |
| ALRMBR | MSK3 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MSK3_Msk |
| ALRMBR | DU | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_DU_Msk |
| ALRMBR | DT | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_DT_Msk |
| ALRMBR | WDSEL | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_WDSEL_Msk |
| ALRMBR | MSK4 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBR_MSK4_Msk |
| WPR | KEY | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:RTC_WPR_KEY_Msk |
| SSR | SS | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_SSR_SS_Msk |
| SHIFTR | SUBFS | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_SHIFTR_SUBFS_Msk |
| SHIFTR | ADD1S | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_SHIFTR_ADD1S_Msk |
| TSTR | SU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_SU_Msk |
| TSTR | ST | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_ST_Msk |
| TSTR | MNU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_MNU_Msk |
| TSTR | MNT | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_MNT_Msk |
| TSTR | HU | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_HU_Msk |
| TSTR | HT | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_HT_Msk |
| TSTR | PM | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSTR_PM_Msk |
| TSDR | DU | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_TSDR_DU_Msk |
| TSDR | DT | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSDR_DT_Msk |
| TSDR | MU | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSDR_MU_Msk |
| TSDR | MT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSDR_MT_Msk |
| TSDR | WDU | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TSDR_WDU_Msk |
| TSSSR | SS | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_TSSSR_SS_Msk |
| CALR | CALM | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALM_Msk |
| CALR | CALW16 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALW16_Msk |
| CALR | CALW8 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALW8_Msk |
| CALR | CALP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALP_Msk |
| TAFCR | TAMP1E | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMP1E_Msk |
| TAFCR | TAMP1TRG | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMP1TRG_Msk |
| TAFCR | TAMPIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPIE_Msk |
| TAFCR | TAMP2E | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMP2E_Msk |
| TAFCR | TAMP2TRG | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMP2TRG_Msk |
| TAFCR | TAMPTS | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPTS_Msk |
| TAFCR | TAMPFREQ | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPFREQ_Msk |
| TAFCR | TAMPFLT | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPFLT_Msk |
| TAFCR | TAMPPRCH | 14:13 | 0x6000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPPRCH_Msk |
| TAFCR | TAMPPUDIS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMPPUDIS_Msk |
| TAFCR | TAMP1INSEL | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TAMP1INSEL_Msk |
| TAFCR | TSINSEL | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_TSINSEL_Msk |
| TAFCR | ALARMOUTTYPE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RTC_TAFCR_ALARMOUTTYPE_Msk |
| ALRMASSR | SS | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMASSR_SS_Msk |
| ALRMASSR | MASKSS | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMASSR_MASKSS_Msk |
| ALRMBSSR | SS | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBSSR_SS_Msk |
| ALRMBSSR | MASKSS | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBSSR_MASKSS_Msk |
| BKP0R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP0R_Msk |
| BKP1R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP1R_Msk |
| BKP2R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP2R_Msk |
| BKP3R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP3R_Msk |
| BKP4R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP4R_Msk |
| BKP5R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP5R_Msk |
| BKP6R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP6R_Msk |
| BKP7R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP7R_Msk |
| BKP8R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP8R_Msk |
| BKP9R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP9R_Msk |
| BKP10R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP10R_Msk |
| BKP11R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP11R_Msk |
| BKP12R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP12R_Msk |
| BKP13R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP13R_Msk |
| BKP14R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP14R_Msk |
| BKP15R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP15R_Msk |
| BKP16R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP16R_Msk |
| BKP17R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP17R_Msk |
| BKP18R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP18R_Msk |
| BKP19R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_BKP19R_Msk |

## Operating semantics unavailable

**rtc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
