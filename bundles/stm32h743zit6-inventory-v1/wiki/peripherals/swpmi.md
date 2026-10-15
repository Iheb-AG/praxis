# SWPMI — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SWPMI1 | 0x40008800 | Not asserted | Not asserted | header:SWPMI1_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.CR |
| BRR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.BRR |
| ISR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.ISR |
| ICR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.ICR |
| IER | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.IER |
| RFL | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.RFL |
| TDR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.TDR |
| RDR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.RDR |
| OR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SWPMI_TypeDef.OR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | RXDMA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_RXDMA_Msk |
| CR | TXDMA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_TXDMA_Msk |
| CR | RXMODE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_RXMODE_Msk |
| CR | TXMODE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_TXMODE_Msk |
| CR | LPBK | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_LPBK_Msk |
| CR | SWPACT | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_SWPACT_Msk |
| CR | DEACT | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_DEACT_Msk |
| CR | SWPEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_CR_SWPEN_Msk |
| BRR | BR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:SWPMI_BRR_BR_Msk |
| ISR | RXBFF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_RXBFF_Msk |
| ISR | TXBEF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_TXBEF_Msk |
| ISR | RXBERF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_RXBERF_Msk |
| ISR | RXOVRF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_RXOVRF_Msk |
| ISR | TXUNRF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_TXUNRF_Msk |
| ISR | RXNE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_RXNE_Msk |
| ISR | TXE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_TXE_Msk |
| ISR | TCF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_TCF_Msk |
| ISR | SRF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_SRF_Msk |
| ISR | SUSP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_SUSP_Msk |
| ISR | DEACTF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_DEACTF_Msk |
| ISR | RDYF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ISR_RDYF_Msk |
| ICR | CRXBFF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CRXBFF_Msk |
| ICR | CTXBEF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CTXBEF_Msk |
| ICR | CRXBERF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CRXBERF_Msk |
| ICR | CRXOVRF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CRXOVRF_Msk |
| ICR | CTXUNRF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CTXUNRF_Msk |
| ICR | CTCF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CTCF_Msk |
| ICR | CSRF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CSRF_Msk |
| ICR | CRDYF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_ICR_CRDYF_Msk |
| IER | RXBFIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_RXBFIE_Msk |
| IER | TXBEIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_TXBEIE_Msk |
| IER | RXBERIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_RXBERIE_Msk |
| IER | RXOVRIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_RXOVRIE_Msk |
| IER | TXUNRIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_TXUNRIE_Msk |
| IER | RIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_RIE_Msk |
| IER | TIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_TIE_Msk |
| IER | TCIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_TCIE_Msk |
| IER | SRIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_SRIE_Msk |
| IER | RDYIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_IER_RDYIE_Msk |
| RFL | RFL | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:SWPMI_RFL_RFL_Msk |
| TDR | TD | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SWPMI_TDR_TD_Msk |
| RDR | RD | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SWPMI_RDR_RD_Msk |
| OR | TBYP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_OR_TBYP_Msk |
| OR | CLASS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SWPMI_OR_CLASS_Msk |

## Operating semantics unavailable

**swpmi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
