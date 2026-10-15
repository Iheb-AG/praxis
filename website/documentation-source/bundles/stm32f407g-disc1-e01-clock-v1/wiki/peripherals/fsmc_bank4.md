# FSMC_BANK4 — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FSMC_Bank4 | 0xA00000A0 | Not asserted | Not asserted | header:FSMC_Bank4_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PCR4 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank4_TypeDef.PCR4; header:FSMC_Bank4_TypeDef.PCR4 |
| SR4 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank4_TypeDef.SR4; header:FSMC_Bank4_TypeDef.SR4 |
| PMEM4 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank4_TypeDef.PMEM4; header:FSMC_Bank4_TypeDef.PMEM4 |
| PATT4 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank4_TypeDef.PATT4; header:FSMC_Bank4_TypeDef.PATT4 |
| PIO4 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank4_TypeDef.PIO4; header:FSMC_Bank4_TypeDef.PIO4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**fsmc_bank4: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
