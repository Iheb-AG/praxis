# CRC — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CRC | 0x40023000 | Not asserted | Not asserted | header:CRC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.DR; header:CRC_TypeDef.DR |
| IDR | 0x004 | 8 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.IDR; header:CRC_TypeDef.IDR |
| CR | 0x008 | 32 | — | unknown | 0x1 | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.CR; header:CRC_CR_RESET; header:CRC_TypeDef.CR; header:CRC_CR_RESET |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DR | DR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:CRC_DR_DR_Msk; header:CRC_DR_DR_Msk |
| IDR | IDR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:CRC_IDR_IDR_Msk; header:CRC_IDR_IDR_Msk |
| CR | RESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CRC_CR_RESET_Msk; header:CRC_CR_RESET_Msk |

## Operating semantics unavailable

**crc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
