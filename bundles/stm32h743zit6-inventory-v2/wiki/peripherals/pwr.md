# PWR — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PWR | 0x58024800 | Not asserted | Not asserted | header:PWR_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR1 |
| CSR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CSR1 |
| CR2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR2 |
| CR3 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR3 |
| CPUCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CPUCR |
| D3CR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.D3CR |
| WKUPCR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.WKUPCR |
| WKUPFR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.WKUPFR |
| WKUPEPR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.WKUPEPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | LPDS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_LPDS_Msk |
| CR1 | PVDEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_PVDEN_Msk |
| CR1 | PLS | 7:5 | 0xE0 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_PLS_Msk |
| CR1 | DBP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_DBP_Msk |
| CR1 | FLPS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_FLPS_Msk |
| CR1 | SVOS | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_SVOS_Msk |
| CR1 | AVDEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_AVDEN_Msk |
| CR1 | ALS | 18:17 | 0x60000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_ALS_Msk |
| CSR1 | PVDO | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR1_PVDO_Msk |
| CSR1 | ACTVOSRDY | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR1_ACTVOSRDY_Msk |
| CSR1 | ACTVOS | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR1_ACTVOS_Msk |
| CSR1 | AVDO | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR1_AVDO_Msk |
| CR2 | BREN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_BREN_Msk |
| CR2 | MONEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_MONEN_Msk |
| CR2 | BRRDY | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_BRRDY_Msk |
| CR2 | VBATL | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_VBATL_Msk |
| CR2 | VBATH | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_VBATH_Msk |
| CR2 | TEMPL | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_TEMPL_Msk |
| CR2 | TEMPH | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_TEMPH_Msk |
| CR3 | BYPASS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_BYPASS_Msk |
| CR3 | LDOEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_LDOEN_Msk |
| CR3 | SCUEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_SCUEN_Msk |
| CR3 | VBE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_VBE_Msk |
| CR3 | VBRS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_VBRS_Msk |
| CR3 | USB33DEN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_USB33DEN_Msk |
| CR3 | USBREGEN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_USBREGEN_Msk |
| CR3 | USB33RDY | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR3_USB33RDY_Msk |
| CPUCR | PDDS_D1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_PDDS_D1_Msk |
| CPUCR | PDDS_D2 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_PDDS_D2_Msk |
| CPUCR | PDDS_D3 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_PDDS_D3_Msk |
| CPUCR | STOPF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_STOPF_Msk |
| CPUCR | SBF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_SBF_Msk |
| CPUCR | SBF_D1 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_SBF_D1_Msk |
| CPUCR | SBF_D2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_SBF_D2_Msk |
| CPUCR | CSSF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_CSSF_Msk |
| CPUCR | RUN_D3 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_CPUCR_RUN_D3_Msk |
| D3CR | VOSRDY | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_D3CR_VOSRDY_Msk |
| D3CR | VOS | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:PWR_D3CR_VOS_Msk |
| WKUPCR | WKUPC1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC1_Msk |
| WKUPCR | WKUPC2 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC2_Msk |
| WKUPCR | WKUPC3 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC3_Msk |
| WKUPCR | WKUPC4 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC4_Msk |
| WKUPCR | WKUPC5 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC5_Msk |
| WKUPCR | WKUPC6 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPCR_WKUPC6_Msk |
| WKUPFR | WKUPF1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF1_Msk |
| WKUPFR | WKUPF2 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF2_Msk |
| WKUPFR | WKUPF3 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF3_Msk |
| WKUPFR | WKUPF4 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF4_Msk |
| WKUPFR | WKUPF5 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF5_Msk |
| WKUPFR | WKUPF6 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPFR_WKUPF6_Msk |
| WKUPEPR | WKUPEN | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPEN_Msk |
| WKUPEPR | WKUPP1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP1_Msk |
| WKUPEPR | WKUPP2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP2_Msk |
| WKUPEPR | WKUPP3 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP3_Msk |
| WKUPEPR | WKUPP4 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP4_Msk |
| WKUPEPR | WKUPP5 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP5_Msk |
| WKUPEPR | WKUPP6 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPP6_Msk |
| WKUPEPR | WKUPPUPD1 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD1_Msk |
| WKUPEPR | WKUPPUPD2 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD2_Msk |
| WKUPEPR | WKUPPUPD3 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD3_Msk |
| WKUPEPR | WKUPPUPD4 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD4_Msk |
| WKUPEPR | WKUPPUPD5 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD5_Msk |
| WKUPEPR | WKUPPUPD6 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:PWR_WKUPEPR_WKUPPUPD6_Msk |

## Operating semantics unavailable

**pwr: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
