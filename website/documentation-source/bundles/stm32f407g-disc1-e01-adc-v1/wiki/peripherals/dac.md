# DAC — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DAC | 0x40007400 | Not asserted | Not asserted | header:DAC_BASE |
| DAC1 | 0x40007400 | Not asserted | Not asserted | header:DAC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.CR; header:DAC_TypeDef.CR |
| SWTRIGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SWTRIGR; header:DAC_TypeDef.SWTRIGR |
| DHR12R1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12R1; header:DAC_TypeDef.DHR12R1 |
| DHR12L1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12L1; header:DAC_TypeDef.DHR12L1 |
| DHR8R1 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8R1; header:DAC_TypeDef.DHR8R1 |
| DHR12R2 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12R2; header:DAC_TypeDef.DHR12R2 |
| DHR12L2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12L2; header:DAC_TypeDef.DHR12L2 |
| DHR8R2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8R2; header:DAC_TypeDef.DHR8R2 |
| DHR12RD | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12RD; header:DAC_TypeDef.DHR12RD |
| DHR12LD | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12LD; header:DAC_TypeDef.DHR12LD |
| DHR8RD | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8RD; header:DAC_TypeDef.DHR8RD |
| DOR1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DOR1; header:DAC_TypeDef.DOR1 |
| DOR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DOR2; header:DAC_TypeDef.DOR2 |
| SR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SR; header:DAC_TypeDef.SR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_EN1_Msk; header:DAC_CR_EN1_Msk |
| CR | BOFF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_BOFF1_Msk; header:DAC_CR_BOFF1_Msk |
| CR | TEN1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TEN1_Msk; header:DAC_CR_TEN1_Msk |
| CR | TSEL1 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TSEL1_Msk; header:DAC_CR_TSEL1_Msk |
| CR | WAVE1 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_WAVE1_Msk; header:DAC_CR_WAVE1_Msk |
| CR | MAMP1 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_MAMP1_Msk; header:DAC_CR_MAMP1_Msk |
| CR | DMAEN1 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAEN1_Msk; header:DAC_CR_DMAEN1_Msk |
| CR | DMAUDRIE1 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAUDRIE1_Msk; header:DAC_CR_DMAUDRIE1_Msk |
| CR | EN2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_EN2_Msk; header:DAC_CR_EN2_Msk |
| CR | BOFF2 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_BOFF2_Msk; header:DAC_CR_BOFF2_Msk |
| CR | TEN2 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TEN2_Msk; header:DAC_CR_TEN2_Msk |
| CR | TSEL2 | 21:19 | 0x380000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TSEL2_Msk; header:DAC_CR_TSEL2_Msk |
| CR | WAVE2 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_WAVE2_Msk; header:DAC_CR_WAVE2_Msk |
| CR | MAMP2 | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_MAMP2_Msk; header:DAC_CR_MAMP2_Msk |
| CR | DMAEN2 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAEN2_Msk; header:DAC_CR_DMAEN2_Msk |
| CR | DMAUDRIE2 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAUDRIE2_Msk; header:DAC_CR_DMAUDRIE2_Msk |
| SWTRIGR | SWTRIG1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DAC_SWTRIGR_SWTRIG1_Msk; header:DAC_SWTRIGR_SWTRIG1_Msk |
| SWTRIGR | SWTRIG2 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DAC_SWTRIGR_SWTRIG2_Msk; header:DAC_SWTRIGR_SWTRIG2_Msk |
| DHR12R1 | DACC1DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12R1_DACC1DHR_Msk; header:DAC_DHR12R1_DACC1DHR_Msk |
| DHR12L1 | DACC1DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12L1_DACC1DHR_Msk; header:DAC_DHR12L1_DACC1DHR_Msk |
| DHR8R1 | DACC1DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8R1_DACC1DHR_Msk; header:DAC_DHR8R1_DACC1DHR_Msk |
| DHR12R2 | DACC2DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12R2_DACC2DHR_Msk; header:DAC_DHR12R2_DACC2DHR_Msk |
| DHR12L2 | DACC2DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12L2_DACC2DHR_Msk; header:DAC_DHR12L2_DACC2DHR_Msk |
| DHR8R2 | DACC2DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8R2_DACC2DHR_Msk; header:DAC_DHR8R2_DACC2DHR_Msk |
| DHR12RD | DACC1DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12RD_DACC1DHR_Msk; header:DAC_DHR12RD_DACC1DHR_Msk |
| DHR12RD | DACC2DHR | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12RD_DACC2DHR_Msk; header:DAC_DHR12RD_DACC2DHR_Msk |
| DHR12LD | DACC1DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12LD_DACC1DHR_Msk; header:DAC_DHR12LD_DACC1DHR_Msk |
| DHR12LD | DACC2DHR | 31:20 | 0xFFF00000 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12LD_DACC2DHR_Msk; header:DAC_DHR12LD_DACC2DHR_Msk |
| DHR8RD | DACC1DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8RD_DACC1DHR_Msk; header:DAC_DHR8RD_DACC1DHR_Msk |
| DHR8RD | DACC2DHR | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8RD_DACC2DHR_Msk; header:DAC_DHR8RD_DACC2DHR_Msk |
| DOR1 | DACC1DOR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DOR1_DACC1DOR_Msk; header:DAC_DOR1_DACC1DOR_Msk |
| DOR2 | DACC2DOR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DOR2_DACC2DOR_Msk; header:DAC_DOR2_DACC2DOR_Msk |
| SR | DMAUDR1 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DAC_SR_DMAUDR1_Msk; header:DAC_SR_DMAUDR1_Msk |
| SR | DMAUDR2 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_SR_DMAUDR2_Msk; header:DAC_SR_DMAUDR2_Msk |

## Operating semantics unavailable

**dac: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
