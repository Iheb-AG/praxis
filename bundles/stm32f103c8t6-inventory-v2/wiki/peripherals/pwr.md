# PWR — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PWR | 0x40007000 | Not asserted | Not asserted | header:PWR_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR |
| CSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | LPDS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_LPDS_Msk |
| CR | PDDS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PDDS_Msk |
| CR | CWUF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CWUF_Msk |
| CR | CSBF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CSBF_Msk |
| CR | PVDE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PVDE_Msk |
| CR | PLS | 7:5 | 0xE0 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PLS_Msk |
| CR | DBP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_DBP_Msk |
| CSR | WUF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_WUF_Msk |
| CSR | SBF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_SBF_Msk |
| CSR | PVDO | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_PVDO_Msk |
| CSR | EWUP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_EWUP_Msk |

## Operating semantics unavailable

**pwr: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
