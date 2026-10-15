# COMP — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| COMP1 | 0x40010200 | Not asserted | Not asserted | header:COMP1_BASE |
| COMP2 | 0x40010204 | Not asserted | Not asserted | header:COMP2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:COMP_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CSR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_EN_Msk |
| CSR | INMSEL | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_INMSEL_Msk |
| CSR | INPSEL | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_INPSEL_Msk |
| CSR | WINMODE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_WINMODE_Msk |
| CSR | WINOUT | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_WINOUT_Msk |
| CSR | POLARITY | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_POLARITY_Msk |
| CSR | HYST | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_HYST_Msk |
| CSR | PWRMODE | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_PWRMODE_Msk |
| CSR | BLANKING | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_BLANKING_Msk |
| CSR | VALUE | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_VALUE_Msk |
| CSR | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:COMP_CSR_LOCK_Msk |

## Operating semantics unavailable

**comp: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
