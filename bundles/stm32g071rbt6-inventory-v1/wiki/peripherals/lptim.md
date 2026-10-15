# LPTIM — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| LPTIM1 | 0x40007C00 | Not asserted | Not asserted | header:LPTIM1_BASE |
| LPTIM2 | 0x40009400 | Not asserted | Not asserted | header:LPTIM2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.ISR |
| ICR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.ICR |
| IER | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.IER |
| CFGR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.CFGR |
| CR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.CR |
| CMP | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.CMP |
| ARR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.ARR |
| CNT | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.CNT |
| CFGR2 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LPTIM_TypeDef.CFGR2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISR | CMPM | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_CMPM_Msk |
| ISR | ARRM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_ARRM_Msk |
| ISR | EXTTRIG | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_EXTTRIG_Msk |
| ISR | CMPOK | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_CMPOK_Msk |
| ISR | ARROK | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_ARROK_Msk |
| ISR | UP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_UP_Msk |
| ISR | DOWN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ISR_DOWN_Msk |
| ICR | CMPMCF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_CMPMCF_Msk |
| ICR | ARRMCF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_ARRMCF_Msk |
| ICR | EXTTRIGCF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_EXTTRIGCF_Msk |
| ICR | CMPOKCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_CMPOKCF_Msk |
| ICR | ARROKCF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_ARROKCF_Msk |
| ICR | UPCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_UPCF_Msk |
| ICR | DOWNCF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ICR_DOWNCF_Msk |
| IER | CMPMIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_CMPMIE_Msk |
| IER | ARRMIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_ARRMIE_Msk |
| IER | EXTTRIGIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_EXTTRIGIE_Msk |
| IER | CMPOKIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_CMPOKIE_Msk |
| IER | ARROKIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_ARROKIE_Msk |
| IER | UPIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_UPIE_Msk |
| IER | DOWNIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_IER_DOWNIE_Msk |
| CFGR | CKSEL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_CKSEL_Msk |
| CFGR | CKPOL | 2:1 | 0x6 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_CKPOL_Msk |
| CFGR | CKFLT | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_CKFLT_Msk |
| CFGR | TRGFLT | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_TRGFLT_Msk |
| CFGR | PRESC | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_PRESC_Msk |
| CFGR | TRIGSEL | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_TRIGSEL_Msk |
| CFGR | TRIGEN | 18:17 | 0x60000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_TRIGEN_Msk |
| CFGR | TIMOUT | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_TIMOUT_Msk |
| CFGR | WAVE | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_WAVE_Msk |
| CFGR | WAVPOL | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_WAVPOL_Msk |
| CFGR | PRELOAD | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_PRELOAD_Msk |
| CFGR | COUNTMODE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_COUNTMODE_Msk |
| CFGR | ENC | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR_ENC_Msk |
| CR | ENABLE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CR_ENABLE_Msk |
| CR | SNGSTRT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CR_SNGSTRT_Msk |
| CR | CNTSTRT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CR_CNTSTRT_Msk |
| CR | COUNTRST | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CR_COUNTRST_Msk |
| CR | RSTARE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CR_RSTARE_Msk |
| CMP | CMP | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CMP_CMP_Msk |
| ARR | ARR | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:LPTIM_ARR_ARR_Msk |
| CNT | CNT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CNT_CNT_Msk |
| CFGR2 | IN1SEL | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR2_IN1SEL_Msk |
| CFGR2 | IN2SEL | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:LPTIM_CFGR2_IN2SEL_Msk |

## Operating semantics unavailable

**lptim: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
