# USART — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| LPUART1 | 0x58000C00 | Not asserted | Not asserted | header:LPUART1_BASE |
| UART4 | 0x40004C00 | Not asserted | Not asserted | header:UART4_BASE |
| UART5 | 0x40005000 | Not asserted | Not asserted | header:UART5_BASE |
| UART7 | 0x40007800 | Not asserted | Not asserted | header:UART7_BASE |
| UART8 | 0x40007C00 | Not asserted | Not asserted | header:UART8_BASE |
| USART1 | 0x40011000 | Not asserted | Not asserted | header:USART1_BASE |
| USART2 | 0x40004400 | Not asserted | Not asserted | header:USART2_BASE |
| USART3 | 0x40004800 | Not asserted | Not asserted | header:USART3_BASE |
| USART6 | 0x40011400 | Not asserted | Not asserted | header:USART6_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR2 |
| CR3 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.CR3 |
| BRR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.BRR |
| GTPR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.GTPR |
| RTOR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.RTOR |
| RQR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.RQR |
| ISR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.ISR |
| ICR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.ICR |
| RDR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.RDR |
| TDR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.TDR |
| PRESC | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USART_TypeDef.PRESC |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR2 | SLVEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_SLVEN_Msk |
| CR2 | DIS_NSS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_DIS_NSS_Msk |
| CR2 | ADDM7 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_ADDM7_Msk |
| CR2 | LBDL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBDL_Msk |
| CR2 | LBDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBDIE_Msk |
| CR2 | LBCL | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LBCL_Msk |
| CR2 | CPHA | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CPHA_Msk |
| CR2 | CPOL | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CPOL_Msk |
| CR2 | CLKEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_CLKEN_Msk |
| CR2 | STOP | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_STOP_Msk |
| CR2 | LINEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_LINEN_Msk |
| CR2 | SWAP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_SWAP_Msk |
| CR2 | RXINV | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_RXINV_Msk |
| CR2 | TXINV | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_TXINV_Msk |
| CR2 | DATAINV | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_DATAINV_Msk |
| CR2 | MSBFIRST | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_MSBFIRST_Msk |
| CR2 | ABREN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_ABREN_Msk |
| CR2 | ABRMODE | 22:21 | 0x600000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_ABRMODE_Msk |
| CR2 | RTOEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_RTOEN_Msk |
| CR2 | ADD | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR2_ADD_Msk |
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
| CR3 | ONEBIT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_ONEBIT_Msk |
| CR3 | OVRDIS | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_OVRDIS_Msk |
| CR3 | DDRE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_DDRE_Msk |
| CR3 | DEM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_DEM_Msk |
| CR3 | DEP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_DEP_Msk |
| CR3 | SCARCNT | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_SCARCNT_Msk |
| CR3 | WUS | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_WUS_Msk |
| CR3 | WUFIE | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_WUFIE_Msk |
| CR3 | TXFTIE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_TXFTIE_Msk |
| CR3 | TCBGTIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_TCBGTIE_Msk |
| CR3 | RXFTCFG | 27:25 | 0xE000000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_RXFTCFG_Msk |
| CR3 | RXFTIE | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_RXFTIE_Msk |
| CR3 | TXFTCFG | 31:29 | 0xE0000000 | Declaration only; encoding requires reviewed semantics. | header:USART_CR3_TXFTCFG_Msk |
| BRR | DIV_FRACTION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USART_BRR_DIV_FRACTION_Msk |
| BRR | DIV_MANTISSA | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | header:USART_BRR_DIV_MANTISSA_Msk |
| GTPR | PSC | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:USART_GTPR_PSC_Msk |
| GTPR | GT | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:USART_GTPR_GT_Msk |
| RTOR | RTO | 23:0 | 0xFFFFFF | Declaration only; encoding requires reviewed semantics. | header:USART_RTOR_RTO_Msk |
| RTOR | BLEN | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:USART_RTOR_BLEN_Msk |
| RQR | ABRRQ | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_RQR_ABRRQ_Msk |
| RQR | SBKRQ | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_RQR_SBKRQ_Msk |
| RQR | MMRQ | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_RQR_MMRQ_Msk |
| RQR | RXFRQ | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_RQR_RXFRQ_Msk |
| RQR | TXFRQ | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_RQR_TXFRQ_Msk |
| ISR | PE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_PE_Msk |
| ISR | FE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_FE_Msk |
| ISR | NE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_NE_Msk |
| ISR | ORE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_ORE_Msk |
| ISR | IDLE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_IDLE_Msk |
| ISR | RXNE_RXFNE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_RXNE_RXFNE_Msk |
| ISR | TC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TC_Msk |
| ISR | TXE_TXFNF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TXE_TXFNF_Msk |
| ISR | LBDF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_LBDF_Msk |
| ISR | CTSIF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_CTSIF_Msk |
| ISR | CTS | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_CTS_Msk |
| ISR | RTOF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_RTOF_Msk |
| ISR | EOBF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_EOBF_Msk |
| ISR | UDR | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_UDR_Msk |
| ISR | ABRE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_ABRE_Msk |
| ISR | ABRF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_ABRF_Msk |
| ISR | BUSY | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_BUSY_Msk |
| ISR | CMF | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_CMF_Msk |
| ISR | SBKF | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_SBKF_Msk |
| ISR | RWU | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_RWU_Msk |
| ISR | WUF | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_WUF_Msk |
| ISR | TEACK | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TEACK_Msk |
| ISR | REACK | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_REACK_Msk |
| ISR | TXFE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TXFE_Msk |
| ISR | RXFF | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_RXFF_Msk |
| ISR | TCBGT | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TCBGT_Msk |
| ISR | RXFT | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_RXFT_Msk |
| ISR | TXFT | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:USART_ISR_TXFT_Msk |
| ICR | PECF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_PECF_Msk |
| ICR | FECF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_FECF_Msk |
| ICR | NECF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_NECF_Msk |
| ICR | ORECF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_ORECF_Msk |
| ICR | IDLECF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_IDLECF_Msk |
| ICR | TXFECF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_TXFECF_Msk |
| ICR | TCCF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_TCCF_Msk |
| ICR | TCBGTCF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_TCBGTCF_Msk |
| ICR | LBDCF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_LBDCF_Msk |
| ICR | CTSCF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_CTSCF_Msk |
| ICR | RTOCF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_RTOCF_Msk |
| ICR | EOBCF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_EOBCF_Msk |
| ICR | UDRCF | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_UDRCF_Msk |
| ICR | CMCF | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_CMCF_Msk |
| ICR | WUCF | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USART_ICR_WUCF_Msk |
| RDR | RDR | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | header:USART_RDR_RDR_Msk |
| TDR | TDR | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | header:USART_TDR_TDR_Msk |
| PRESC | PRESCALER | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USART_PRESC_PRESCALER_Msk |

## Operating semantics unavailable

**usart: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- CR1: bit fields withheld: UNSUPPORTED_MASK: USART_CR1_M_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
