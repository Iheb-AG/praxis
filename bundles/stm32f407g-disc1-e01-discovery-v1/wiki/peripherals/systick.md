# SYSTICK — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SysTick | 0xE000E010 | Not asserted | Not asserted | cmsis_core:SysTick_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CTRL | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SysTick_Type.CTRL; cmsis_core:SysTick_Type.CTRL |
| LOAD | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SysTick_Type.LOAD; cmsis_core:SysTick_Type.LOAD |
| VAL | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SysTick_Type.VAL; cmsis_core:SysTick_Type.VAL |
| CALIB | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SysTick_Type.CALIB; cmsis_core:SysTick_Type.CALIB |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CTRL | ENABLE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CTRL_ENABLE_Msk; cmsis_core:SysTick_CTRL_ENABLE_Msk |
| CTRL | TICKINT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CTRL_TICKINT_Msk; cmsis_core:SysTick_CTRL_TICKINT_Msk |
| CTRL | CLKSOURCE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CTRL_CLKSOURCE_Msk; cmsis_core:SysTick_CTRL_CLKSOURCE_Msk |
| CTRL | COUNTFLAG | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CTRL_COUNTFLAG_Msk; cmsis_core:SysTick_CTRL_COUNTFLAG_Msk |
| LOAD | RELOAD | 23:0 | 0xFFFFFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_LOAD_RELOAD_Msk; cmsis_core:SysTick_LOAD_RELOAD_Msk |
| VAL | CURRENT | 23:0 | 0xFFFFFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_VAL_CURRENT_Msk; cmsis_core:SysTick_VAL_CURRENT_Msk |
| CALIB | TENMS | 23:0 | 0xFFFFFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CALIB_TENMS_Msk; cmsis_core:SysTick_CALIB_TENMS_Msk |
| CALIB | SKEW | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CALIB_SKEW_Msk; cmsis_core:SysTick_CALIB_SKEW_Msk |
| CALIB | NOREF | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SysTick_CALIB_NOREF_Msk; cmsis_core:SysTick_CALIB_NOREF_Msk |

## Operating semantics unavailable

**systick: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
