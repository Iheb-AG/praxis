# WWDG — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| WWDG | 0x40002C00 | Not asserted | Not asserted | header:WWDG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.CR; header:WWDG_TypeDef.CR |
| CFR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.CFR; header:WWDG_TypeDef.CFR |
| SR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.SR; header:WWDG_TypeDef.SR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | T | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:WWDG_CR_T_Msk; header:WWDG_CR_T_Msk |
| CR | WDGA | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CR_WDGA_Msk; header:WWDG_CR_WDGA_Msk |
| CFR | W | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_W_Msk; header:WWDG_CFR_W_Msk |
| CFR | WDGTB | 8:7 | 0x180 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_WDGTB_Msk; header:WWDG_CFR_WDGTB_Msk |
| CFR | EWI | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_EWI_Msk; header:WWDG_CFR_EWI_Msk |
| SR | EWIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:WWDG_SR_EWIF_Msk; header:WWDG_SR_EWIF_Msk |

## Operating semantics unavailable

**wwdg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
