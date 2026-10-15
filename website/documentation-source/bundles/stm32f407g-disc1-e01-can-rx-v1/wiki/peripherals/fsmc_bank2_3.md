# FSMC_BANK2_3 — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FSMC_Bank2_3 | 0xA0000060 | Not asserted | Not asserted | header:FSMC_Bank2_3_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PCR2 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PCR2; header:FSMC_Bank2_3_TypeDef.PCR2 |
| SR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.SR2; header:FSMC_Bank2_3_TypeDef.SR2 |
| PMEM2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PMEM2; header:FSMC_Bank2_3_TypeDef.PMEM2 |
| PATT2 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PATT2; header:FSMC_Bank2_3_TypeDef.PATT2 |
| ECCR2 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.ECCR2; header:FSMC_Bank2_3_TypeDef.ECCR2 |
| PCR3 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PCR3; header:FSMC_Bank2_3_TypeDef.PCR3 |
| SR3 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.SR3; header:FSMC_Bank2_3_TypeDef.SR3 |
| PMEM3 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PMEM3; header:FSMC_Bank2_3_TypeDef.PMEM3 |
| PATT3 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.PATT3; header:FSMC_Bank2_3_TypeDef.PATT3 |
| ECCR3 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FSMC_Bank2_3_TypeDef.ECCR3; header:FSMC_Bank2_3_TypeDef.ECCR3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**fsmc_bank2_3: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
