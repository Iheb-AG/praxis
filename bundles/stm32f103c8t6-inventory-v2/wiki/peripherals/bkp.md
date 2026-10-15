# BKP — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| BKP | 0x40006C00 | Not asserted | Not asserted | header:BKP_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR1 |
| DR2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR2 |
| DR3 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR3 |
| DR4 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR4 |
| DR5 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR5 |
| DR6 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR6 |
| DR7 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR7 |
| DR8 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR8 |
| DR9 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR9 |
| DR10 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.DR10 |
| RTCCR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.RTCCR |
| CR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.CR |
| CSR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:BKP_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DR1 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR1_D_Msk |
| DR2 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR2_D_Msk |
| DR3 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR3_D_Msk |
| DR4 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR4_D_Msk |
| DR5 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR5_D_Msk |
| DR6 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR6_D_Msk |
| DR7 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR7_D_Msk |
| DR8 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR8_D_Msk |
| DR9 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR9_D_Msk |
| DR10 | D | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:BKP_DR10_D_Msk |
| RTCCR | CAL | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:BKP_RTCCR_CAL_Msk |
| RTCCR | CCO | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:BKP_RTCCR_CCO_Msk |
| RTCCR | ASOE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:BKP_RTCCR_ASOE_Msk |
| RTCCR | ASOS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:BKP_RTCCR_ASOS_Msk |
| CR | TPE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:BKP_CR_TPE_Msk |
| CR | TPAL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:BKP_CR_TPAL_Msk |
| CSR | CTE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:BKP_CSR_CTE_Msk |
| CSR | CTI | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:BKP_CSR_CTI_Msk |
| CSR | TPIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:BKP_CSR_TPIE_Msk |
| CSR | TEF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:BKP_CSR_TEF_Msk |
| CSR | TIF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:BKP_CSR_TIF_Msk |

## Operating semantics unavailable

**bkp: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
