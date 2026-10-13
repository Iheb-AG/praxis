# COREDEBUG — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CoreDebug | 0xE000EDF0 | Not asserted | Not asserted | cmsis_core:CoreDebug_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DHCSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:CoreDebug_Type.DHCSR; cmsis_core:CoreDebug_Type.DHCSR |
| DCRSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:CoreDebug_Type.DCRSR; cmsis_core:CoreDebug_Type.DCRSR |
| DCRDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:CoreDebug_Type.DCRDR; cmsis_core:CoreDebug_Type.DCRDR |
| DEMCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:CoreDebug_Type.DEMCR; cmsis_core:CoreDebug_Type.DEMCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DHCSR | C_DEBUGEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_C_DEBUGEN_Msk; cmsis_core:CoreDebug_DHCSR_C_DEBUGEN_Msk |
| DHCSR | C_HALT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_C_HALT_Msk; cmsis_core:CoreDebug_DHCSR_C_HALT_Msk |
| DHCSR | C_STEP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_C_STEP_Msk; cmsis_core:CoreDebug_DHCSR_C_STEP_Msk |
| DHCSR | C_MASKINTS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_C_MASKINTS_Msk; cmsis_core:CoreDebug_DHCSR_C_MASKINTS_Msk |
| DHCSR | C_SNAPSTALL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_C_SNAPSTALL_Msk; cmsis_core:CoreDebug_DHCSR_C_SNAPSTALL_Msk |
| DHCSR | DBGKEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DHCSR_DBGKEY_Msk; cmsis_core:CoreDebug_DHCSR_DBGKEY_Msk |
| DCRSR | REGSEL | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DCRSR_REGSEL_Msk; cmsis_core:CoreDebug_DCRSR_REGSEL_Msk |
| DCRSR | REGWnR | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DCRSR_REGWnR_Msk; cmsis_core:CoreDebug_DCRSR_REGWnR_Msk |
| DEMCR | VC_CORERESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_CORERESET_Msk; cmsis_core:CoreDebug_DEMCR_VC_CORERESET_Msk |
| DEMCR | VC_MMERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_MMERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_MMERR_Msk |
| DEMCR | VC_NOCPERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_NOCPERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_NOCPERR_Msk |
| DEMCR | VC_CHKERR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_CHKERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_CHKERR_Msk |
| DEMCR | VC_STATERR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_STATERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_STATERR_Msk |
| DEMCR | VC_BUSERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_BUSERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_BUSERR_Msk |
| DEMCR | VC_INTERR | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_INTERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_INTERR_Msk |
| DEMCR | VC_HARDERR | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_VC_HARDERR_Msk; cmsis_core:CoreDebug_DEMCR_VC_HARDERR_Msk |
| DEMCR | MON_EN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_MON_EN_Msk; cmsis_core:CoreDebug_DEMCR_MON_EN_Msk |
| DEMCR | MON_PEND | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_MON_PEND_Msk; cmsis_core:CoreDebug_DEMCR_MON_PEND_Msk |
| DEMCR | MON_STEP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_MON_STEP_Msk; cmsis_core:CoreDebug_DEMCR_MON_STEP_Msk |
| DEMCR | MON_REQ | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_MON_REQ_Msk; cmsis_core:CoreDebug_DEMCR_MON_REQ_Msk |
| DEMCR | TRCENA | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:CoreDebug_DEMCR_TRCENA_Msk; cmsis_core:CoreDebug_DEMCR_TRCENA_Msk |

## Operating semantics unavailable

**coredebug: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
