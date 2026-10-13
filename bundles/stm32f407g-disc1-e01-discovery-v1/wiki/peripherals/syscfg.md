# SYSCFG — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SYSCFG | 0x40013800 | Not asserted | Not asserted | header:SYSCFG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MEMRMP | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.MEMRMP; header:SYSCFG_TypeDef.MEMRMP | 1 | 4 |
| PMC | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.PMC; header:SYSCFG_TypeDef.PMC | 1 | 4 |
| EXTICR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.EXTICR; header:SYSCFG_TypeDef.EXTICR | 4 | 4 |
| CMPCR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CMPCR; header:SYSCFG_TypeDef.CMPCR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MEMRMP | MEM_MODE | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_MEMRMP_MEM_MODE_Msk; header:SYSCFG_MEMRMP_MEM_MODE_Msk |
| PMC | MII_RMII_SEL | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMC_MII_RMII_SEL_Msk; header:SYSCFG_PMC_MII_RMII_SEL_Msk |
| CMPCR | CMP_PD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CMPCR_CMP_PD_Msk; header:SYSCFG_CMPCR_CMP_PD_Msk |
| CMPCR | READY | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CMPCR_READY_Msk; header:SYSCFG_CMPCR_READY_Msk |

## Operating semantics unavailable

**syscfg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
