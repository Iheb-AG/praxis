# QUADSPI — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| QUADSPI | 0x52005000 | Not asserted | Not asserted | header:QSPI_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.CR |
| DCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.DCR |
| SR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.SR |
| FCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.FCR |
| DLR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.DLR |
| CCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.CCR |
| AR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.AR |
| ABR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.ABR |
| DR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.DR |
| PSMKR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.PSMKR |
| PSMAR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.PSMAR |
| PIR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.PIR |
| LPTR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:QUADSPI_TypeDef.LPTR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_EN_Msk |
| CR | ABORT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_ABORT_Msk |
| CR | DMAEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_DMAEN_Msk |
| CR | TCEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_TCEN_Msk |
| CR | SSHIFT | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_SSHIFT_Msk |
| CR | DFM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_DFM_Msk |
| CR | FSEL | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_FSEL_Msk |
| CR | FTHRES | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_FTHRES_Msk |
| CR | TEIE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_TEIE_Msk |
| CR | TCIE | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_TCIE_Msk |
| CR | FTIE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_FTIE_Msk |
| CR | SMIE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_SMIE_Msk |
| CR | TOIE | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_TOIE_Msk |
| CR | APMS | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_APMS_Msk |
| CR | PMM | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_PMM_Msk |
| CR | PRESCALER | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CR_PRESCALER_Msk |
| DCR | CKMODE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_DCR_CKMODE_Msk |
| DCR | CSHT | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_DCR_CSHT_Msk |
| DCR | FSIZE | 20:16 | 0x1F0000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_DCR_FSIZE_Msk |
| SR | TEF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_TEF_Msk |
| SR | TCF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_TCF_Msk |
| SR | FTF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_FTF_Msk |
| SR | SMF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_SMF_Msk |
| SR | TOF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_TOF_Msk |
| SR | BUSY | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_BUSY_Msk |
| SR | FLEVEL | 13:8 | 0x3F00 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_SR_FLEVEL_Msk |
| FCR | CTEF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_FCR_CTEF_Msk |
| FCR | CTCF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_FCR_CTCF_Msk |
| FCR | CSMF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_FCR_CSMF_Msk |
| FCR | CTOF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_FCR_CTOF_Msk |
| DLR | DL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_DLR_DL_Msk |
| CCR | INSTRUCTION | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_INSTRUCTION_Msk |
| CCR | IMODE | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_IMODE_Msk |
| CCR | ADMODE | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_ADMODE_Msk |
| CCR | ADSIZE | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_ADSIZE_Msk |
| CCR | ABMODE | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_ABMODE_Msk |
| CCR | ABSIZE | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_ABSIZE_Msk |
| CCR | DCYC | 22:18 | 0x7C0000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_DCYC_Msk |
| CCR | DMODE | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_DMODE_Msk |
| CCR | FMODE | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_FMODE_Msk |
| CCR | SIOO | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_SIOO_Msk |
| CCR | FRCM | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_FRCM_Msk |
| CCR | DHHC | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_DHHC_Msk |
| CCR | DDRM | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_CCR_DDRM_Msk |
| AR | ADDRESS | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_AR_ADDRESS_Msk |
| ABR | ALTERNATE | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_ABR_ALTERNATE_Msk |
| DR | DATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_DR_DATA_Msk |
| PSMKR | MASK | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_PSMKR_MASK_Msk |
| PSMAR | MATCH | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_PSMAR_MATCH_Msk |
| PIR | INTERVAL | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_PIR_INTERVAL_Msk |
| LPTR | TIMEOUT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:QUADSPI_LPTR_TIMEOUT_Msk |

## Operating semantics unavailable

**quadspi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
