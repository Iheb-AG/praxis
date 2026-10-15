# WWDG — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| WWDG | 0x40002C00 | Not asserted | Not asserted | header:WWDG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.CR |
| CFR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.CFR |
| SR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:WWDG_TypeDef.SR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | T | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:WWDG_CR_T_Msk |
| CR | WDGA | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CR_WDGA_Msk |
| CFR | W | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_W_Msk |
| CFR | EWI | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_EWI_Msk |
| CFR | WDGTB | 13:11 | 0x3800 | Declaration only; encoding requires reviewed semantics. | header:WWDG_CFR_WDGTB_Msk |
| SR | EWIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:WWDG_SR_EWIF_Msk |

## Operating semantics unavailable

**wwdg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
