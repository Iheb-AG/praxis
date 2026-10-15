# MDIOS — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| MDIOS | 0x40009400 | Not asserted | Not asserted | header:MDIOS_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.CR |
| WRFR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.WRFR |
| CWRFR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.CWRFR |
| RDFR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.RDFR |
| CRDFR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.CRDFR |
| SR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.SR |
| CLRFR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.CLRFR |
| DINR0 | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR0 |
| DINR1 | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR1 |
| DINR2 | 0x108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR2 |
| DINR3 | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR3 |
| DINR4 | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR4 |
| DINR5 | 0x114 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR5 |
| DINR6 | 0x118 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR6 |
| DINR7 | 0x11C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR7 |
| DINR8 | 0x120 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR8 |
| DINR9 | 0x124 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR9 |
| DINR10 | 0x128 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR10 |
| DINR11 | 0x12C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR11 |
| DINR12 | 0x130 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR12 |
| DINR13 | 0x134 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR13 |
| DINR14 | 0x138 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR14 |
| DINR15 | 0x13C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR15 |
| DINR16 | 0x140 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR16 |
| DINR17 | 0x144 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR17 |
| DINR18 | 0x148 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR18 |
| DINR19 | 0x14C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR19 |
| DINR20 | 0x150 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR20 |
| DINR21 | 0x154 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR21 |
| DINR22 | 0x158 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR22 |
| DINR23 | 0x15C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR23 |
| DINR24 | 0x160 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR24 |
| DINR25 | 0x164 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR25 |
| DINR26 | 0x168 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR26 |
| DINR27 | 0x16C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR27 |
| DINR28 | 0x170 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR28 |
| DINR29 | 0x174 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR29 |
| DINR30 | 0x178 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR30 |
| DINR31 | 0x17C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DINR31 |
| DOUTR0 | 0x180 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR0 |
| DOUTR1 | 0x184 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR1 |
| DOUTR2 | 0x188 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR2 |
| DOUTR3 | 0x18C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR3 |
| DOUTR4 | 0x190 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR4 |
| DOUTR5 | 0x194 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR5 |
| DOUTR6 | 0x198 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR6 |
| DOUTR7 | 0x19C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR7 |
| DOUTR8 | 0x1A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR8 |
| DOUTR9 | 0x1A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR9 |
| DOUTR10 | 0x1A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR10 |
| DOUTR11 | 0x1AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR11 |
| DOUTR12 | 0x1B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR12 |
| DOUTR13 | 0x1B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR13 |
| DOUTR14 | 0x1B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR14 |
| DOUTR15 | 0x1BC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR15 |
| DOUTR16 | 0x1C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR16 |
| DOUTR17 | 0x1C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR17 |
| DOUTR18 | 0x1C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR18 |
| DOUTR19 | 0x1CC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR19 |
| DOUTR20 | 0x1D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR20 |
| DOUTR21 | 0x1D4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR21 |
| DOUTR22 | 0x1D8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR22 |
| DOUTR23 | 0x1DC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR23 |
| DOUTR24 | 0x1E0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR24 |
| DOUTR25 | 0x1E4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR25 |
| DOUTR26 | 0x1E8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR26 |
| DOUTR27 | 0x1EC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR27 |
| DOUTR28 | 0x1F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR28 |
| DOUTR29 | 0x1F4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR29 |
| DOUTR30 | 0x1F8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR30 |
| DOUTR31 | 0x1FC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDIOS_TypeDef.DOUTR31 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_EN_Msk |
| CR | WRIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_WRIE_Msk |
| CR | RDIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_RDIE_Msk |
| CR | EIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_EIE_Msk |
| CR | DPC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_DPC_Msk |
| CR | PORT_ADDRESS | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_CR_PORT_ADDRESS_Msk |
| SR | PERF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_SR_PERF_Msk |
| SR | SERF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_SR_SERF_Msk |
| SR | TERF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:MDIOS_SR_TERF_Msk |

## Operating semantics unavailable

**mdios: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
