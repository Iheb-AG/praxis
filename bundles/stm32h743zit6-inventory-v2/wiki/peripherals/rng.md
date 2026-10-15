# RNG — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RNG | 0x48021800 | Not asserted | Not asserted | header:RNG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.CR |
| SR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.SR |
| DR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | RNGEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RNG_CR_RNGEN_Msk |
| CR | IE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RNG_CR_IE_Msk |
| CR | CED | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RNG_CR_CED_Msk |
| SR | DRDY | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_DRDY_Msk |
| SR | CECS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_CECS_Msk |
| SR | SECS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_SECS_Msk |
| SR | CEIS | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_CEIS_Msk |
| SR | SEIS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_SEIS_Msk |

## Operating semantics unavailable

**rng: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
