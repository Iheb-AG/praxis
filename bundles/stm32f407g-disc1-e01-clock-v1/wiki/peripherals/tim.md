# TIM2: reviewed update interrupt subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TIM1 | 0x40010000 | Not asserted | Not asserted outside reviewed workflow | header:TIM1_BASE |
| TIM10 | 0x40014400 | Not asserted | Not asserted outside reviewed workflow | header:TIM10_BASE |
| TIM11 | 0x40014800 | Not asserted | Not asserted outside reviewed workflow | header:TIM11_BASE |
| TIM12 | 0x40001800 | Not asserted | Not asserted outside reviewed workflow | header:TIM12_BASE |
| TIM13 | 0x40001C00 | Not asserted | Not asserted outside reviewed workflow | header:TIM13_BASE |
| TIM14 | 0x40002000 | Not asserted | Not asserted outside reviewed workflow | header:TIM14_BASE |
| TIM2 | 0x40000000 | APB1 | Explicitly selected HSI scenario; see RCC and reviewed notes | header:TIM2_BASE |
| TIM3 | 0x40000400 | Not asserted | Not asserted outside reviewed workflow | header:TIM3_BASE |
| TIM4 | 0x40000800 | Not asserted | Not asserted outside reviewed workflow | header:TIM4_BASE |
| TIM5 | 0x40000C00 | Not asserted | Not asserted outside reviewed workflow | header:TIM5_BASE |
| TIM6 | 0x40001000 | Not asserted | Not asserted outside reviewed workflow | header:TIM6_BASE |
| TIM7 | 0x40001400 | Not asserted | Not asserted outside reviewed workflow | header:TIM7_BASE |
| TIM8 | 0x40010400 | Not asserted | Not asserted outside reviewed workflow | header:TIM8_BASE |
| TIM9 | 0x40014000 | Not asserted | Not asserted outside reviewed workflow | header:TIM9_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | RW | 0x0 | CEN/URS/UDIS/ARPE; supported TIM2 upcounter controls. | header:TIM_TypeDef.CR1; header:TIM_TypeDef.CR1; rm_tim_cr1:page:624 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CR2 |
| SMCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.SMCR |
| DIER | 0x00C | 32 | — | RW | 0x0 | UIE only; leave DMA/channel requests disabled. | header:TIM_TypeDef.DIER; header:TIM_TypeDef.DIER; rm_tim_dier:page:629 |
| SR | 0x010 | 32 | — | mixed | 0x0 | rc_w0 flags: write zero to clear; SR=0 clears all flags in the update-only workflow. | header:TIM_TypeDef.SR; header:TIM_TypeDef.SR; rm_tim_sr:page:630 |
| EGR | 0x014 | 32 | — | WO | 0x0 | Write UG to reload prescaler/counter; self-clearing action, may set UIF. | header:TIM_TypeDef.EGR; header:TIM_TypeDef.EGR; rm_tim_egr:page:632 |
| CCMR1 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCMR1 |
| CCMR2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCMR2 |
| CCER | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCER |
| CNT | 0x024 | 32 | — | RW | 0x0 | TIM2 32-bit counter; writes only while stopped in this workflow. | header:TIM_TypeDef.CNT; header:TIM_TypeDef.CNT; rm_tim_values:page:638 |
| PSC | 0x028 | 32 | — | RW | 0x0 | 16-bit prescaler; update event transfers buffered value. | header:TIM_TypeDef.PSC; header:TIM_TypeDef.PSC; rm_tim_values:page:638 |
| ARR | 0x02C | 32 | — | RW | 0xFFFFFFFF | TIM2 32-bit auto-reload; nonzero period required. | header:TIM_TypeDef.ARR; header:TIM_TypeDef.ARR; rm_tim_arr:page:639 |
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
| CCMR1 | OC1FE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1FE_Msk |
| CCMR1 | OC1PE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1PE_Msk |
| CCMR1 | OC1M | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1M_Msk |
| CCMR1 | OC1CE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1CE_Msk |
| CCMR1 | CC2S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC2S_Msk |
| CCMR1 | OC2FE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC2FE_Msk |
| CCMR1 | OC2PE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC2PE_Msk |
| CCMR1 | OC2M | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC2M_Msk |
| CCMR1 | OC2CE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC2CE_Msk |
| CCMR2 | CC3S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC3S_Msk |
| CCMR2 | OC3FE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3FE_Msk |
| CCMR2 | OC3PE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3PE_Msk |
| CCMR2 | OC3M | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3M_Msk |
| CCMR2 | OC3CE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3CE_Msk |
| CCMR2 | CC4S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC4S_Msk |
| CCMR2 | OC4FE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4FE_Msk |
| CCMR2 | OC4PE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4PE_Msk |
| CCMR2 | OC4M | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4M_Msk |
| CCMR2 | OC4CE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4CE_Msk |
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
| OR | TI1_RMP | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_TI1_RMP_Msk |
| OR | TI4_RMP | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_TI4_RMP_Msk |
| OR | ITR1_RMP | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_ITR1_RMP_Msk |

## Reviewed operating semantics

Supported operating subset: **TIM2 internal-clock, edge-aligned upcounter, update interrupt**.
The shared vendor structure also describes other timers; its full declaration map does not
establish that all members exist on TIM2 or that other timer modes are reviewed. RCR and BDTR
are not TIM2 operating registers. CCMR tables select the output view to avoid overlapping
input/output encodings; capture/compare operation is outside this workflow.

TIM2 is on APB1. If the APB1 prescaler is one, TIM2CLK=PCLK1; otherwise TIM2CLK=2×PCLK1.
For this scenario explicitly establish HSI nominal 16 MHz, AHB /1, APB1 /1 and APB2 /1.
TIM2CLK is then nominal 16 MHz. PSC=15 and ARR=999 give
16,000,000 / ((15+1)×(999+1)) = 1,000 updates/second. This is a design calculation,
not a timing measurement. PSC is 16 bits; TIM2 CNT and ARR are 32 bits.
Evidence: `rm_clock:page:218`, `rm_tim_values:page:638`, `rm_tim_arr:page:639`.

1. Mask interrupts; enable TIM2EN and read back the gate. Reset only owned TIM2 through
   TIM2RST and release reset. Keep CEN and UIE zero while initializing software state.
2. Use CR1=0 (upcounter, edge-aligned, continuous, UDIS=0, URS=0), PSC=15, ARR=999, CNT=0.
3. Write EGR.UG to load the buffered prescaler and reinitialize the counter. This is an
   action register; do not use a read-modify-write. UG can set UIF with this configuration.
4. Clear stale flags with **SR=0** while all channel/trigger uses are disabled. SR flags
   are **rc_w0**, not W1C. In this update-only ISR, SR=0 deliberately clears all timer flags;
   this is inappropriate if unrelated capture/compare owners share the timer.
5. Clear NVIC pending, set priority and enable the TIM2 line only after its handler/state
   are ready; enable UIE and CEN, restore global interrupts last. The bounded ISR checks
   UIF, writes SR=0, increments the millisecond counter and returns. It does not delay.

TIM2_IRQn=28, external vector slot 44, handler TIM2_IRQHandler, from `header:TIM2_IRQn`;
the pinned startup supplies the vector slot. All startup/ELF assets remain separately pinned.
Use unsigned subtraction for millisecond wrap; do not assume SysTick is the time source here.

Source-backed editorial subset: RM0090 Rev22 sections 7.2, 18.4.1/4/5/6/10/11/12,
read through the ingestion MCP. Header masks for shared advanced-timer fields do not change
reserved-bit rules for TIM2. See [[peripherals/rcc]], [[peripherals/nvic]] and [[sources]].

## Review

Reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
