# IWDG — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| IWDG | 0x40003000 | Not asserted | Not asserted | header:IWDG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| KR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:IWDG_TypeDef.KR |
| PR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:IWDG_TypeDef.PR |
| RLR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:IWDG_TypeDef.RLR |
| SR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:IWDG_TypeDef.SR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| KR | KEY | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:IWDG_KR_KEY_Msk |
| PR | PR | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:IWDG_PR_PR_Msk |
| RLR | RL | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:IWDG_RLR_RL_Msk |
| SR | PVU | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:IWDG_SR_PVU_Msk |
| SR | RVU | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:IWDG_SR_RVU_Msk |

## Operating semantics unavailable

**iwdg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
