# DBGMCU — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DBGMCU | 0xE0042000 | Not asserted | Not asserted | header:DBGMCU_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IDCODE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.IDCODE |
| CR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.CR |
| APB1FZ | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB1FZ |
| APB2FZ | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBGMCU_TypeDef.APB2FZ |

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

## Operating semantics unavailable

**dbgmcu: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
