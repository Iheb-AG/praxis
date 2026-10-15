# DLYB — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DLYB_QUADSPI | 0x52006000 | Not asserted | Not asserted | header:DLYB_QSPI_BASE |
| DLYB_SDMMC1 | 0x52008000 | Not asserted | Not asserted | header:DLYB_SDMMC1_BASE |
| DLYB_SDMMC2 | 0x48022800 | Not asserted | Not asserted | header:DLYB_SDMMC2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DLYB_TypeDef.CR |
| CFGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DLYB_TypeDef.CFGR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | DEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DLYB_CR_DEN_Msk |
| CR | SEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DLYB_CR_SEN_Msk |
| CFGR | SEL | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:DLYB_CFGR_SEL_Msk |
| CFGR | UNIT | 14:8 | 0x7F00 | Declaration only; encoding requires reviewed semantics. | header:DLYB_CFGR_UNIT_Msk |
| CFGR | LNG | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DLYB_CFGR_LNG_Msk |
| CFGR | LNGF | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:DLYB_CFGR_LNGF_Msk |

## Operating semantics unavailable

**dlyb: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
