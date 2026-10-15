# LTDC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| LTDC | 0x50001000 | Not asserted | Not asserted | header:LTDC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.SSCR |
| BPCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.BPCR |
| AWCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.AWCR |
| TWCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.TWCR |
| GCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.GCR |
| SRCR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.SRCR |
| BCCR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.BCCR |
| IER | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.IER |
| ISR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.ISR |
| ICR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.ICR |
| LIPCR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.LIPCR |
| CPSR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.CPSR |
| CDSR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:LTDC_TypeDef.CDSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SSCR | VSH | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:LTDC_SSCR_VSH_Msk |
| SSCR | HSW | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_SSCR_HSW_Msk |
| BPCR | AVBP | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:LTDC_BPCR_AVBP_Msk |
| BPCR | AHBP | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_BPCR_AHBP_Msk |
| AWCR | AAH | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:LTDC_AWCR_AAH_Msk |
| AWCR | AAW | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_AWCR_AAW_Msk |
| TWCR | TOTALH | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:LTDC_TWCR_TOTALH_Msk |
| TWCR | TOTALW | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_TWCR_TOTALW_Msk |
| GCR | LTDCEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_LTDCEN_Msk |
| GCR | DBW | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_DBW_Msk |
| GCR | DGW | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_DGW_Msk |
| GCR | DRW | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_DRW_Msk |
| GCR | DEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_DEN_Msk |
| GCR | PCPOL | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_PCPOL_Msk |
| GCR | DEPOL | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_DEPOL_Msk |
| GCR | VSPOL | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_VSPOL_Msk |
| GCR | HSPOL | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_GCR_HSPOL_Msk |
| SRCR | IMR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_SRCR_IMR_Msk |
| SRCR | VBR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LTDC_SRCR_VBR_Msk |
| BCCR | BCBLUE | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:LTDC_BCCR_BCBLUE_Msk |
| BCCR | BCGREEN | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:LTDC_BCCR_BCGREEN_Msk |
| BCCR | BCRED | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_BCCR_BCRED_Msk |
| IER | LIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_IER_LIE_Msk |
| IER | FUIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LTDC_IER_FUIE_Msk |
| IER | TERRIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LTDC_IER_TERRIE_Msk |
| IER | RRIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LTDC_IER_RRIE_Msk |
| ISR | LIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ISR_LIF_Msk |
| ISR | FUIF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ISR_FUIF_Msk |
| ISR | TERRIF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ISR_TERRIF_Msk |
| ISR | RRIF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ISR_RRIF_Msk |
| ICR | CLIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ICR_CLIF_Msk |
| ICR | CFUIF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ICR_CFUIF_Msk |
| ICR | CTERRIF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ICR_CTERRIF_Msk |
| ICR | CRRIF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LTDC_ICR_CRRIF_Msk |
| LIPCR | LIPOS | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:LTDC_LIPCR_LIPOS_Msk |
| CPSR | CYPOS | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:LTDC_CPSR_CYPOS_Msk |
| CPSR | CXPOS | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:LTDC_CPSR_CXPOS_Msk |
| CDSR | VDES | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:LTDC_CDSR_VDES_Msk |
| CDSR | HDES | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:LTDC_CDSR_HDES_Msk |
| CDSR | VSYNCS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:LTDC_CDSR_VSYNCS_Msk |
| CDSR | HSYNCS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:LTDC_CDSR_HSYNCS_Msk |

## Operating semantics unavailable

**ltdc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
