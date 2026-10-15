# USART — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USART1 | 0x40013800 | Not asserted | Not asserted | header:USART1_BASE |
| USART2 | 0x40004400 | Not asserted | Not asserted | header:USART2_BASE |
| USART3 | 0x40004800 | Not asserted | Not asserted | header:USART3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.SR |
| DR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.DR |
| BRR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.BRR |
| CR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR1 |
| CR2 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR2 |
| CR3 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR3 |
| GTPR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.GTPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | PE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_PE_Msk |
| SR | FE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_FE_Msk |
| SR | NE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_NE_Msk |
| SR | ORE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_ORE_Msk |
| SR | IDLE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_IDLE_Msk |
| SR | RXNE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_RXNE_Msk |
| SR | TC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_TC_Msk |
| SR | TXE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_TXE_Msk |
| SR | LBD | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_LBD_Msk |
| SR | CTS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_SR_CTS_Msk |
| DR | DR | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | header:USART_DR_DR_Msk |
| BRR | DIV_Fraction | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USART_BRR_DIV_Fraction_Msk |
| BRR | DIV_Mantissa | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:USART_BRR_DIV_Mantissa_Msk |
| CR1 | SBK | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_SBK_Msk |
| CR1 | RWU | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_RWU_Msk |
| CR1 | RE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_RE_Msk |
| CR1 | TE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_TE_Msk |
| CR1 | IDLEIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_IDLEIE_Msk |
| CR1 | RXNEIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_RXNEIE_Msk |
| CR1 | TCIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_TCIE_Msk |
| CR1 | TXEIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_TXEIE_Msk |
| CR1 | PEIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_PEIE_Msk |
| CR1 | PS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_PS_Msk |
| CR1 | PCE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_PCE_Msk |
| CR1 | WAKE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_WAKE_Msk |
| CR1 | M | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_M_Msk |
| CR1 | UE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR1_UE_Msk |
| CR2 | ADD | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_ADD_Msk |
| CR2 | LBDL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBDL_Msk |
| CR2 | LBDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBDIE_Msk |
| CR2 | LBCL | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBCL_Msk |
| CR2 | CPHA | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CPHA_Msk |
| CR2 | CPOL | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CPOL_Msk |
| CR2 | CLKEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CLKEN_Msk |
| CR2 | STOP | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_STOP_Msk |
| CR2 | LINEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LINEN_Msk |
| CR3 | EIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_EIE_Msk |
| CR3 | IREN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_IREN_Msk |
| CR3 | IRLP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_IRLP_Msk |
| CR3 | HDSEL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_HDSEL_Msk |
| CR3 | NACK | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_NACK_Msk |
| CR3 | SCEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_SCEN_Msk |
| CR3 | DMAR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_DMAR_Msk |
| CR3 | DMAT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_DMAT_Msk |
| CR3 | RTSE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_RTSE_Msk |
| CR3 | CTSE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_CTSE_Msk |
| CR3 | CTSIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_CTSIE_Msk |
| GTPR | PSC | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:USART_GTPR_PSC_Msk |
| GTPR | GT | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:USART_GTPR_GT_Msk |

## Operating semantics unavailable

**usart: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
