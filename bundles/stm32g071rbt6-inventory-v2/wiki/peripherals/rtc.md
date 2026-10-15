# RTC — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RTC | 0x40002800 | Not asserted | Not asserted | header:RTC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TR |
| DR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.DR |
| SSR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SSR |
| ICSR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ICSR |
| PRER | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.PRER |
| WUTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.WUTR |
| CR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CR |
| WPR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.WPR |
| CALR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CALR |
| SHIFTR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SHIFTR |
| TSTR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSTR |
| TSDR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSDR |
| TSSSR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.TSSSR |
| ALRMAR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMAR |
| ALRMASSR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMASSR |
| ALRMBR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMBR |
| ALRMBSSR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRMBSSR |
| SR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SR |
| MISR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.MISR |
| SCR | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.SCR |
| OR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.OR |

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
| SSR | SS | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_SSR_SS_Msk |
| ICSR | ALRAWF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_ALRAWF_Msk |
| ICSR | ALRBWF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_ALRBWF_Msk |
| ICSR | WUTWF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_WUTWF_Msk |
| ICSR | SHPF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_SHPF_Msk |
| ICSR | INITS | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_INITS_Msk |
| ICSR | RSF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_RSF_Msk |
| ICSR | INITF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_INITF_Msk |
| ICSR | INIT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_INIT_Msk |
| ICSR | RECALPF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ICSR_RECALPF_Msk |
| PRER | PREDIV_S | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_PRER_PREDIV_S_Msk |
| PRER | PREDIV_A | 22:16 | 0x7F0000 | Declaration only; encoding requires reviewed semantics. | header:RTC_PRER_PREDIV_A_Msk |
| WUTR | WUT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_WUTR_WUT_Msk |
| CR | WUCKSEL | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_WUCKSEL_Msk |
| CR | TSEDGE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TSEDGE_Msk |
| CR | REFCKON | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_REFCKON_Msk |
| CR | BYPSHAD | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_BYPSHAD_Msk |
| CR | FMT | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_FMT_Msk |
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
| CR | ITSE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_ITSE_Msk |
| CR | TAMPTS | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TAMPTS_Msk |
| CR | TAMPOE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TAMPOE_Msk |
| CR | TAMPALRM_PU | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TAMPALRM_PU_Msk |
| CR | TAMPALRM_TYPE | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_TAMPALRM_TYPE_Msk |
| CR | OUT2EN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CR_OUT2EN_Msk |
| WPR | KEY | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:RTC_WPR_KEY_Msk |
| CALR | CALM | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALM_Msk |
| CALR | CALW16 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALW16_Msk |
| CALR | CALW8 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALW8_Msk |
| CALR | CALP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RTC_CALR_CALP_Msk |
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
| ALRMASSR | SS | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMASSR_SS_Msk |
| ALRMASSR | MASKSS | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMASSR_MASKSS_Msk |
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
| ALRMBSSR | SS | 14:0 | 0x7FFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBSSR_SS_Msk |
| ALRMBSSR | MASKSS | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRMBSSR_MASKSS_Msk |
| SR | ALRAF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_ALRAF_Msk |
| SR | ALRBF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_ALRBF_Msk |
| SR | WUTF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_WUTF_Msk |
| SR | TSF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_TSF_Msk |
| SR | TSOVF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_TSOVF_Msk |
| SR | ITSF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_SR_ITSF_Msk |
| MISR | ALRAMF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_ALRAMF_Msk |
| MISR | ALRBMF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_ALRBMF_Msk |
| MISR | WUTMF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_WUTMF_Msk |
| MISR | TSMF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_TSMF_Msk |
| MISR | TSOVMF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_TSOVMF_Msk |
| MISR | ITSMF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_MISR_ITSMF_Msk |
| SCR | CALRAF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CALRAF_Msk |
| SCR | CALRBF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CALRBF_Msk |
| SCR | CWUTF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CWUTF_Msk |
| SCR | CTSF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CTSF_Msk |
| SCR | CTSOVF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CTSOVF_Msk |
| SCR | CITSF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_SCR_CITSF_Msk |

## Operating semantics unavailable

**rtc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
