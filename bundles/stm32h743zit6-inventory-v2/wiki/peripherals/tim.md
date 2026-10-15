# TIM — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TIM1 | 0x40010000 | Not asserted | Not asserted | header:TIM1_BASE |
| TIM12 | 0x40001800 | Not asserted | Not asserted | header:TIM12_BASE |
| TIM13 | 0x40001C00 | Not asserted | Not asserted | header:TIM13_BASE |
| TIM14 | 0x40002000 | Not asserted | Not asserted | header:TIM14_BASE |
| TIM15 | 0x40014000 | Not asserted | Not asserted | header:TIM15_BASE |
| TIM16 | 0x40014400 | Not asserted | Not asserted | header:TIM16_BASE |
| TIM17 | 0x40014800 | Not asserted | Not asserted | header:TIM17_BASE |
| TIM2 | 0x40000000 | Not asserted | Not asserted | header:TIM2_BASE |
| TIM3 | 0x40000400 | Not asserted | Not asserted | header:TIM3_BASE |
| TIM4 | 0x40000800 | Not asserted | Not asserted | header:TIM4_BASE |
| TIM5 | 0x40000C00 | Not asserted | Not asserted | header:TIM5_BASE |
| TIM6 | 0x40001000 | Not asserted | Not asserted | header:TIM6_BASE |
| TIM7 | 0x40001400 | Not asserted | Not asserted | header:TIM7_BASE |
| TIM8 | 0x40010400 | Not asserted | Not asserted | header:TIM8_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CR2 |
| SMCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.SMCR |
| DIER | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.DIER |
| SR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.SR |
| EGR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.EGR |
| CCMR1 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCMR1 |
| CCMR2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCMR2 |
| CCER | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCER |
| CNT | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CNT |
| PSC | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.PSC |
| ARR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.ARR |
| RCR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.RCR |
| CCR1 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR1 |
| CCR2 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR2 |
| CCR3 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR3 |
| CCR4 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR4 |
| BDTR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.BDTR |
| DCR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.DCR |
| DMAR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.DMAR |
| CCMR3 | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCMR3 |
| CCR5 | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR5 |
| CCR6 | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR6 |
| AF1 | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.AF1 |
| AF2 | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.AF2 |
| TISEL | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.TISEL |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | CEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_CEN_Msk |
| CR1 | UDIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_UDIS_Msk |
| CR1 | URS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_URS_Msk |
| CR1 | OPM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_OPM_Msk |
| CR1 | DIR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_DIR_Msk |
| CR1 | CMS | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_CMS_Msk |
| CR1 | ARPE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_ARPE_Msk |
| CR1 | CKD | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_CKD_Msk |
| CR1 | UIFREMAP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR1_UIFREMAP_Msk |
| CR2 | CCPC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_CCPC_Msk |
| CR2 | CCUS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_CCUS_Msk |
| CR2 | CCDS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_CCDS_Msk |
| CR2 | MMS | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_MMS_Msk |
| CR2 | TI1S | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_TI1S_Msk |
| CR2 | OIS1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS1_Msk |
| CR2 | OIS1N | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS1N_Msk |
| CR2 | OIS2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS2_Msk |
| CR2 | OIS2N | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS2N_Msk |
| CR2 | OIS3 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS3_Msk |
| CR2 | OIS3N | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS3N_Msk |
| CR2 | OIS4 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS4_Msk |
| CR2 | OIS5 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS5_Msk |
| CR2 | OIS6 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS6_Msk |
| CR2 | MMS2 | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_MMS2_Msk |
| DIER | UIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_UIE_Msk |
| DIER | CC1IE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC1IE_Msk |
| DIER | CC2IE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC2IE_Msk |
| DIER | CC3IE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC3IE_Msk |
| DIER | CC4IE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC4IE_Msk |
| DIER | COMIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_COMIE_Msk |
| DIER | TIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_TIE_Msk |
| DIER | BIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_BIE_Msk |
| DIER | UDE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_UDE_Msk |
| DIER | CC1DE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC1DE_Msk |
| DIER | CC2DE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC2DE_Msk |
| DIER | CC3DE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC3DE_Msk |
| DIER | CC4DE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC4DE_Msk |
| DIER | COMDE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_COMDE_Msk |
| DIER | TDE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_TDE_Msk |
| SR | UIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_UIF_Msk |
| SR | CC1IF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC1IF_Msk |
| SR | CC2IF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC2IF_Msk |
| SR | CC3IF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC3IF_Msk |
| SR | CC4IF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC4IF_Msk |
| SR | COMIF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_COMIF_Msk |
| SR | TIF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_TIF_Msk |
| SR | BIF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_BIF_Msk |
| SR | B2IF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_B2IF_Msk |
| SR | CC1OF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC1OF_Msk |
| SR | CC2OF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC2OF_Msk |
| SR | CC3OF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC3OF_Msk |
| SR | CC4OF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC4OF_Msk |
| SR | SBIF | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_SBIF_Msk |
| SR | CC5IF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC5IF_Msk |
| SR | CC6IF | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC6IF_Msk |
| EGR | UG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_UG_Msk |
| EGR | CC1G | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC1G_Msk |
| EGR | CC2G | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC2G_Msk |
| EGR | CC3G | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC3G_Msk |
| EGR | CC4G | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC4G_Msk |
| EGR | COMG | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_COMG_Msk |
| EGR | TG | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_TG_Msk |
| EGR | BG | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_BG_Msk |
| EGR | B2G | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_B2G_Msk |
| CCER | CC1E | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC1E_Msk |
| CCER | CC1P | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC1P_Msk |
| CCER | CC1NE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC1NE_Msk |
| CCER | CC1NP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC1NP_Msk |
| CCER | CC2E | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC2E_Msk |
| CCER | CC2P | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC2P_Msk |
| CCER | CC2NE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC2NE_Msk |
| CCER | CC2NP | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC2NP_Msk |
| CCER | CC3E | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC3E_Msk |
| CCER | CC3P | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC3P_Msk |
| CCER | CC3NE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC3NE_Msk |
| CCER | CC3NP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC3NP_Msk |
| CCER | CC4E | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4E_Msk |
| CCER | CC4P | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4P_Msk |
| CCER | CC4NP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4NP_Msk |
| CCER | CC5E | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC5E_Msk |
| CCER | CC5P | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC5P_Msk |
| CCER | CC6E | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC6E_Msk |
| CCER | CC6P | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC6P_Msk |
| CNT | CNT | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CNT_CNT_Msk |
| PSC | PSC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_PSC_PSC_Msk |
| ARR | ARR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_ARR_ARR_Msk |
| RCR | REP | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:TIM_RCR_REP_Msk |
| CCR1 | CCR1 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR1_CCR1_Msk |
| CCR2 | CCR2 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR2_CCR2_Msk |
| CCR3 | CCR3 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR3_CCR3_Msk |
| CCR4 | CCR4 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR4_CCR4_Msk |
| BDTR | DTG | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_DTG_Msk |
| BDTR | LOCK | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_LOCK_Msk |
| BDTR | OSSI | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_OSSI_Msk |
| BDTR | OSSR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_OSSR_Msk |
| BDTR | BKE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BKE_Msk |
| BDTR | BKP | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BKP_Msk |
| BDTR | AOE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_AOE_Msk |
| BDTR | MOE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_MOE_Msk |
| BDTR | BKF | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BKF_Msk |
| BDTR | BK2F | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BK2F_Msk |
| BDTR | BK2E | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BK2E_Msk |
| BDTR | BK2P | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BK2P_Msk |
| DCR | DBA | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBA_Msk |
| DCR | DBL | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBL_Msk |
| DMAR | DMAB | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_DMAR_DMAB_Msk |
| CCR5 | CCR5 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR5_CCR5_Msk |
| CCR5 | GC5C1 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR5_GC5C1_Msk |
| CCR5 | GC5C2 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR5_GC5C2_Msk |
| CCR5 | GC5C3 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR5_GC5C3_Msk |
| CCR6 | CCR6 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR6_CCR6_Msk |
| TISEL | TI1SEL | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:TIM_TISEL_TI1SEL_Msk |
| TISEL | TI2SEL | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:TIM_TISEL_TI2SEL_Msk |
| TISEL | TI3SEL | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:TIM_TISEL_TI3SEL_Msk |
| TISEL | TI4SEL | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:TIM_TISEL_TI4SEL_Msk |

## Operating semantics unavailable

**tim: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps (the affected register's entire bit-field set is withheld):

- SMCR: bit fields withheld: UNSUPPORTED_MASK: TIM_SMCR_SMS_Msk: non-contiguous bit field without an exact declared component partition
- CCMR1: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR1_OC1M_Msk: non-contiguous bit field without an exact declared component partition
- CCMR2: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR2_OC3M_Msk: non-contiguous bit field without an exact declared component partition
- CCMR3: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR3_OC5M_Msk: non-contiguous bit field without an exact declared component partition

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
