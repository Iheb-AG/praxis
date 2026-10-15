# PWR — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PWR | 0x40007000 | Not asserted | Not asserted | header:PWR_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR; header:PWR_TypeDef.CR |
| CSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CSR; header:PWR_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | LPDS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_LPDS_Msk; header:PWR_CR_LPDS_Msk |
| CR | PDDS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PDDS_Msk; header:PWR_CR_PDDS_Msk |
| CR | CWUF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CWUF_Msk; header:PWR_CR_CWUF_Msk |
| CR | CSBF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CSBF_Msk; header:PWR_CR_CSBF_Msk |
| CR | PVDE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PVDE_Msk; header:PWR_CR_PVDE_Msk |
| CR | PLS | 7:5 | 0xE0 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PLS_Msk; header:PWR_CR_PLS_Msk |
| CR | DBP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_DBP_Msk; header:PWR_CR_DBP_Msk |
| CR | FPDS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_FPDS_Msk; header:PWR_CR_FPDS_Msk |
| CR | VOS | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_VOS_Msk; header:PWR_CR_VOS_Msk |
| CSR | WUF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_WUF_Msk; header:PWR_CSR_WUF_Msk |
| CSR | SBF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_SBF_Msk; header:PWR_CSR_SBF_Msk |
| CSR | PVDO | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_PVDO_Msk; header:PWR_CSR_PVDO_Msk |
| CSR | BRR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_BRR_Msk; header:PWR_CSR_BRR_Msk |
| CSR | EWUP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_EWUP_Msk; header:PWR_CSR_EWUP_Msk |
| CSR | BRE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_BRE_Msk; header:PWR_CSR_BRE_Msk |
| CSR | VOSRDY | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_VOSRDY_Msk; header:PWR_CSR_VOSRDY_Msk |

## Operating semantics unavailable

**pwr: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
