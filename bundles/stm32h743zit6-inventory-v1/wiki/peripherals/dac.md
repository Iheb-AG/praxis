# DAC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DAC1 | 0x40007400 | Not asserted | Not asserted | header:DAC1_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.CR |
| SWTRIGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SWTRIGR |
| DHR12R1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12R1 |
| DHR12L1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12L1 |
| DHR8R1 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8R1 |
| DHR12R2 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12R2 |
| DHR12L2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12L2 |
| DHR8R2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8R2 |
| DHR12RD | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12RD |
| DHR12LD | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR12LD |
| DHR8RD | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DHR8RD |
| DOR1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DOR1 |
| DOR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.DOR2 |
| SR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SR |
| CCR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.CCR |
| MCR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.MCR |
| SHSR1 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SHSR1 |
| SHSR2 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SHSR2 |
| SHHR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SHHR |
| SHRR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DAC_TypeDef.SHRR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_EN1_Msk |
| CR | TEN1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TEN1_Msk |
| CR | TSEL1 | 5:2 | 0x3C | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TSEL1_Msk |
| CR | WAVE1 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_WAVE1_Msk |
| CR | MAMP1 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_MAMP1_Msk |
| CR | DMAEN1 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAEN1_Msk |
| CR | DMAUDRIE1 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAUDRIE1_Msk |
| CR | CEN1 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_CEN1_Msk |
| CR | EN2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_EN2_Msk |
| CR | TEN2 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TEN2_Msk |
| CR | TSEL2 | 21:18 | 0x3C0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_TSEL2_Msk |
| CR | WAVE2 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_WAVE2_Msk |
| CR | MAMP2 | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_MAMP2_Msk |
| CR | DMAEN2 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAEN2_Msk |
| CR | DMAUDRIE2 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_DMAUDRIE2_Msk |
| CR | CEN2 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CR_CEN2_Msk |
| SWTRIGR | SWTRIG1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DAC_SWTRIGR_SWTRIG1_Msk |
| SWTRIGR | SWTRIG2 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DAC_SWTRIGR_SWTRIG2_Msk |
| DHR12R1 | DACC1DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12R1_DACC1DHR_Msk |
| DHR12L1 | DACC1DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12L1_DACC1DHR_Msk |
| DHR8R1 | DACC1DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8R1_DACC1DHR_Msk |
| DHR12R2 | DACC2DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12R2_DACC2DHR_Msk |
| DHR12L2 | DACC2DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12L2_DACC2DHR_Msk |
| DHR8R2 | DACC2DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8R2_DACC2DHR_Msk |
| DHR12RD | DACC1DHR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12RD_DACC1DHR_Msk |
| DHR12RD | DACC2DHR | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12RD_DACC2DHR_Msk |
| DHR12LD | DACC1DHR | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12LD_DACC1DHR_Msk |
| DHR12LD | DACC2DHR | 31:20 | 0xFFF00000 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR12LD_DACC2DHR_Msk |
| DHR8RD | DACC1DHR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8RD_DACC1DHR_Msk |
| DHR8RD | DACC2DHR | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DAC_DHR8RD_DACC2DHR_Msk |
| DOR1 | DACC1DOR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DOR1_DACC1DOR_Msk |
| DOR2 | DACC2DOR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DAC_DOR2_DACC2DOR_Msk |
| CCR | OTRIM1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:DAC_CCR_OTRIM1_Msk |
| CCR | OTRIM2 | 20:16 | 0x1F0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_CCR_OTRIM2_Msk |
| MCR | MODE1 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:DAC_MCR_MODE1_Msk |
| MCR | MODE2 | 18:16 | 0x70000 | Declaration only; encoding requires reviewed semantics. | header:DAC_MCR_MODE2_Msk |
| SHSR1 | TSAMPLE1 | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:DAC_SHSR1_TSAMPLE1_Msk |
| SHSR2 | TSAMPLE2 | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:DAC_SHSR2_TSAMPLE2_Msk |
| SHHR | THOLD1 | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:DAC_SHHR_THOLD1_Msk |
| SHHR | THOLD2 | 25:16 | 0x3FF0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_SHHR_THOLD2_Msk |
| SHRR | TREFRESH1 | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DAC_SHRR_TREFRESH1_Msk |
| SHRR | TREFRESH2 | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DAC_SHRR_TREFRESH2_Msk |

## Operating semantics unavailable

**dac: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- SR: bit fields withheld: UNSUPPORTED_MASK: DAC_SR_BWST1_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
