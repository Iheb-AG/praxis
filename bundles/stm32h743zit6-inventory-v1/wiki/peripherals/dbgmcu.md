# DBGMCU — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DBGMCU | 0x5C001000 | Not asserted | Not asserted | header:DBGMCU_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IDCODE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.IDCODE |
| CR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.CR |
| APB3FZ1 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB3FZ1 |
| APB1LFZ1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB1LFZ1 |
| APB1HFZ1 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB1HFZ1 |
| APB2FZ1 | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB2FZ1 |
| APB4FZ1 | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB4FZ1 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| IDCODE | DEV_ID | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_IDCODE_DEV_ID_Msk |
| IDCODE | REV_ID | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_IDCODE_REV_ID_Msk |
| CR | DBG_SLEEPD1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_SLEEPD1_Msk |
| CR | DBG_STOPD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_STOPD1_Msk |
| CR | DBG_STANDBYD1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_STANDBYD1_Msk |
| CR | DBG_TRACECKEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TRACECKEN_Msk |
| CR | DBG_CKD1EN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_CKD1EN_Msk |
| CR | DBG_CKD3EN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_CKD3EN_Msk |
| CR | DBG_TRGOEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TRGOEN_Msk |
| APB3FZ1 | DBG_WWDG1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB3FZ1_DBG_WWDG1_Msk |
| APB1LFZ1 | DBG_TIM2 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM2_Msk |
| APB1LFZ1 | DBG_TIM3 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM3_Msk |
| APB1LFZ1 | DBG_TIM4 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM4_Msk |
| APB1LFZ1 | DBG_TIM5 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM5_Msk |
| APB1LFZ1 | DBG_TIM6 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM6_Msk |
| APB1LFZ1 | DBG_TIM7 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM7_Msk |
| APB1LFZ1 | DBG_TIM12 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM12_Msk |
| APB1LFZ1 | DBG_TIM13 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM13_Msk |
| APB1LFZ1 | DBG_TIM14 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_TIM14_Msk |
| APB1LFZ1 | DBG_LPTIM1 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_LPTIM1_Msk |
| APB1LFZ1 | DBG_I2C1 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_I2C1_Msk |
| APB1LFZ1 | DBG_I2C2 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_I2C2_Msk |
| APB1LFZ1 | DBG_I2C3 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1LFZ1_DBG_I2C3_Msk |
| APB1HFZ1 | DBG_FDCAN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB1HFZ1_DBG_FDCAN_Msk |
| APB2FZ1 | DBG_TIM1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_TIM1_Msk |
| APB2FZ1 | DBG_TIM8 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_TIM8_Msk |
| APB2FZ1 | DBG_TIM15 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_TIM15_Msk |
| APB2FZ1 | DBG_TIM16 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_TIM16_Msk |
| APB2FZ1 | DBG_TIM17 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_TIM17_Msk |
| APB2FZ1 | DBG_HRTIM | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB2FZ1_DBG_HRTIM_Msk |
| APB4FZ1 | DBG_I2C4 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_I2C4_Msk |
| APB4FZ1 | DBG_LPTIM2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_LPTIM2_Msk |
| APB4FZ1 | DBG_LPTIM3 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_LPTIM3_Msk |
| APB4FZ1 | DBG_LPTIM4 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_LPTIM4_Msk |
| APB4FZ1 | DBG_LPTIM5 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_LPTIM5_Msk |
| APB4FZ1 | DBG_RTC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_RTC_Msk |
| APB4FZ1 | DBG_IWDG1 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_APB4FZ1_DBG_IWDG1_Msk |

## Operating semantics unavailable

**dbgmcu: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
