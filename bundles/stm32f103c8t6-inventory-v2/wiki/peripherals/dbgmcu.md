# DBGMCU — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DBGMCU | 0xE0042000 | Not asserted | Not asserted | header:DBGMCU_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IDCODE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.IDCODE |
| CR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.CR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| IDCODE | DEV_ID | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_IDCODE_DEV_ID_Msk |
| IDCODE | REV_ID | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_IDCODE_REV_ID_Msk |
| CR | DBG_SLEEP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_SLEEP_Msk |
| CR | DBG_STOP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_STOP_Msk |
| CR | DBG_STANDBY | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_STANDBY_Msk |
| CR | TRACE_IOEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_TRACE_IOEN_Msk |
| CR | TRACE_MODE | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_TRACE_MODE_Msk |
| CR | DBG_IWDG_STOP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_IWDG_STOP_Msk |
| CR | DBG_WWDG_STOP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_WWDG_STOP_Msk |
| CR | DBG_TIM1_STOP | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TIM1_STOP_Msk |
| CR | DBG_TIM2_STOP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TIM2_STOP_Msk |
| CR | DBG_TIM3_STOP | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TIM3_STOP_Msk |
| CR | DBG_TIM4_STOP | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_TIM4_STOP_Msk |
| CR | DBG_CAN1_STOP | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_CAN1_STOP_Msk |
| CR | DBG_I2C1_SMBUS_TIMEOUT | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_I2C1_SMBUS_TIMEOUT_Msk |
| CR | DBG_I2C2_SMBUS_TIMEOUT | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DBGMCU_CR_DBG_I2C2_SMBUS_TIMEOUT_Msk |

## Operating semantics unavailable

**dbgmcu: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
