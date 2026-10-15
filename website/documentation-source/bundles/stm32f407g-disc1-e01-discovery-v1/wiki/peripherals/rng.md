# RNG — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RNG | 0x50060800 | Not asserted | Not asserted | header:RNG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.CR; header:RNG_TypeDef.CR |
| SR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.SR; header:RNG_TypeDef.SR |
| DR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RNG_TypeDef.DR; header:RNG_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | RNGEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RNG_CR_RNGEN_Msk; header:RNG_CR_RNGEN_Msk |
| CR | IE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RNG_CR_IE_Msk; header:RNG_CR_IE_Msk |
| SR | DRDY | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_DRDY_Msk; header:RNG_SR_DRDY_Msk |
| SR | CECS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_CECS_Msk; header:RNG_SR_CECS_Msk |
| SR | SECS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_SECS_Msk; header:RNG_SR_SECS_Msk |
| SR | CEIS | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_CEIS_Msk; header:RNG_SR_CEIS_Msk |
| SR | SEIS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RNG_SR_SEIS_Msk; header:RNG_SR_SEIS_Msk |

## Operating semantics unavailable

**rng: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
