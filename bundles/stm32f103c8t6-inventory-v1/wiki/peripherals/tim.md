# TIM — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TIM1 | 0x40012C00 | Not asserted | Not asserted | header:TIM1_BASE |
| TIM2 | 0x40000000 | Not asserted | Not asserted | header:TIM2_BASE |
| TIM3 | 0x40000400 | Not asserted | Not asserted | header:TIM3_BASE |
| TIM4 | 0x40000800 | Not asserted | Not asserted | header:TIM4_BASE |

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
| OR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.OR |

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
| SMCR | SMS | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_SMS_Msk |
| SMCR | TS | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_TS_Msk |
| SMCR | MSM | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_MSM_Msk |
| SMCR | ETF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETF_Msk |
| SMCR | ETPS | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETPS_Msk |
| SMCR | ECE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ECE_Msk |
| SMCR | ETP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETP_Msk |
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
| SR | CC1OF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC1OF_Msk |
| SR | CC2OF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC2OF_Msk |
| SR | CC3OF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC3OF_Msk |
| SR | CC4OF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC4OF_Msk |
| EGR | UG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_UG_Msk |
| EGR | CC1G | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC1G_Msk |
| EGR | CC2G | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC2G_Msk |
| EGR | CC3G | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC3G_Msk |
| EGR | CC4G | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC4G_Msk |
| EGR | COMG | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_COMG_Msk |
| EGR | TG | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_TG_Msk |
| EGR | BG | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_BG_Msk |
| CCMR1 | CC1S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC1S_Msk |
| CCMR1 | IC1PSC | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC1PSC_Msk |
| CCMR1 | IC1F | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC1F_Msk |
| CCMR1 | CC2S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC2S_Msk |
| CCMR1 | IC2PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2PSC_Msk |
| CCMR1 | IC2F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2F_Msk |
| CCMR2 | CC3S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC3S_Msk |
| CCMR2 | IC3PSC | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC3PSC_Msk |
| CCMR2 | IC3F | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC3F_Msk |
| CCMR2 | CC4S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC4S_Msk |
| CCMR2 | IC4PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4PSC_Msk |
| CCMR2 | IC4F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4F_Msk |
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
| DCR | DBA | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBA_Msk |
| DCR | DBL | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBL_Msk |
| DMAR | DMAB | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_DMAR_DMAB_Msk |

## Operating semantics unavailable

**tim: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
