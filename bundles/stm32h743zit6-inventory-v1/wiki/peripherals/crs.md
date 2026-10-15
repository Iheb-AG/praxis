# CRS — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CRS | 0x40008400 | Not asserted | Not asserted | header:CRS_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRS_TypeDef.CR |
| CFGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRS_TypeDef.CFGR |
| ISR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRS_TypeDef.ISR |
| ICR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRS_TypeDef.ICR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | SYNCOKIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_SYNCOKIE_Msk |
| CR | SYNCWARNIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_SYNCWARNIE_Msk |
| CR | ERRIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_ERRIE_Msk |
| CR | ESYNCIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_ESYNCIE_Msk |
| CR | CEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_CEN_Msk |
| CR | AUTOTRIMEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_AUTOTRIMEN_Msk |
| CR | SWSYNC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_SWSYNC_Msk |
| CR | TRIM | 13:8 | 0x3F00 | Declaration only; encoding requires reviewed semantics. | header:CRS_CR_TRIM_Msk |
| CFGR | RELOAD | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:CRS_CFGR_RELOAD_Msk |
| CFGR | FELIM | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:CRS_CFGR_FELIM_Msk |
| CFGR | SYNCDIV | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:CRS_CFGR_SYNCDIV_Msk |
| CFGR | SYNCSRC | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:CRS_CFGR_SYNCSRC_Msk |
| CFGR | SYNCPOL | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:CRS_CFGR_SYNCPOL_Msk |
| ISR | SYNCOKF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_SYNCOKF_Msk |
| ISR | SYNCWARNF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_SYNCWARNF_Msk |
| ISR | ERRF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_ERRF_Msk |
| ISR | ESYNCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_ESYNCF_Msk |
| ISR | SYNCERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_SYNCERR_Msk |
| ISR | SYNCMISS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_SYNCMISS_Msk |
| ISR | TRIMOVF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_TRIMOVF_Msk |
| ISR | FEDIR | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_FEDIR_Msk |
| ISR | FECAP | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:CRS_ISR_FECAP_Msk |
| ICR | SYNCOKC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CRS_ICR_SYNCOKC_Msk |
| ICR | SYNCWARNC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CRS_ICR_SYNCWARNC_Msk |
| ICR | ERRC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CRS_ICR_ERRC_Msk |
| ICR | ESYNCC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CRS_ICR_ESYNCC_Msk |

## Operating semantics unavailable

**crs: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
