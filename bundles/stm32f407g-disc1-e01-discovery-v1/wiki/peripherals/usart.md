# USART: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| UART4 | 0x40004C00 | APB1 | PCLK1=42 MHz | header:UART4_BASE; usart_review:instance:UART4 |
| UART5 | 0x40005000 | APB1 | PCLK1=42 MHz | header:UART5_BASE; usart_review:instance:UART5 |
| USART1 | 0x40011000 | APB2 | PCLK2=84 MHz | header:USART1_BASE; usart_review:instance:USART1 |
| USART2 | 0x40004400 | APB1 | PCLK1=42 MHz | header:USART2_BASE; usart_review:instance:USART2 |
| USART3 | 0x40004800 | APB1 | PCLK1=42 MHz | header:USART3_BASE; usart_review:instance:USART3 |
| USART6 | 0x40011400 | APB2 | PCLK2=84 MHz | header:USART6_BASE; usart_review:instance:USART6 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | mixed | 0xC0 | PE/FE/NF/ORE/IDLE clear by SR-read then DR-read. RXNE clears by DR-read. TC also has SR-read then DR-write sequence. See manual for write-zero flag clears. | header:USART_TypeDef.SR; usart_review:SR |
| DR | 0x004 | 32 | — | mixed | not asserted | Read consumes received data; write queues transmit data. | header:USART_TypeDef.DR; usart_review:DR |
| BRR | 0x008 | 32 | — | RW | 0x0 | Change only while communication is quiescent. | header:USART_TypeDef.BRR; usart_review:BRR |
| CR1 | 0x00C | 32 | — | RW | 0x0 | Configure frame/baud before UE; enable interrupt sources only with handler ready. | header:USART_TypeDef.CR1; usart_review:CR1 |
| CR2 | 0x010 | 32 | — | RW | 0x0 | Asynchronous 8N1: STOP=00 and CLKEN=0. | header:USART_TypeDef.CR2; usart_review:CR2 |
| CR3 | 0x014 | 32 | — | RW | 0x0 | Set DMAR/DMAT only after DMA stream configuration. | header:USART_TypeDef.CR3; usart_review:CR3 |
| GTPR | 0x018 | 32 | — | RW | 0x0 | Smartcard/IrDA; unused for asynchronous fixture. | header:USART_TypeDef.GTPR; usart_review:GTPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | PE | 0:0 | 0x1 | Parity error | header:USART_SR_PE_Msk; usart_review:SR.PE |
| SR | FE | 1:1 | 0x2 | Framing error | header:USART_SR_FE_Msk; usart_review:SR.FE |
| SR | NE | 2:2 | 0x4 | Noise detected | header:USART_SR_NE_Msk; usart_review:SR.NE |
| SR | ORE | 3:3 | 0x8 | Overrun | header:USART_SR_ORE_Msk; usart_review:SR.ORE |
| SR | IDLE | 4:4 | 0x10 | Idle line | header:USART_SR_IDLE_Msk; usart_review:SR.IDLE |
| SR | RXNE | 5:5 | 0x20 | Receive data ready | header:USART_SR_RXNE_Msk; usart_review:SR.RXNE |
| SR | TC | 6:6 | 0x40 | Transmission complete | header:USART_SR_TC_Msk; usart_review:SR.TC |
| SR | TXE | 7:7 | 0x80 | Transmit data register empty | header:USART_SR_TXE_Msk; usart_review:SR.TXE |
| SR | LBD | 8:8 | 0x100 | LIN break detected | header:USART_SR_LBD_Msk; usart_review:SR.LBD |
| SR | CTS | 9:9 | 0x200 | CTS changed | header:USART_SR_CTS_Msk; usart_review:SR.CTS |
| DR | DR | 8:0 | 0x1FF | Data; use low 8 bits for 8N1 | header:USART_DR_DR_Msk; usart_review:DR.DR |
| BRR | DIV_Fraction | 3:0 | 0xF | OVER8=0; BRR=0x016D at PCLK1=42 MHz and 115200 baud; see reviewed formula. | header:USART_BRR_DIV_Fraction_Msk; usart_review:baud; profile:clock_plan |
| BRR | DIV_Mantissa | 15:4 | 0xFFF0 | OVER8=0; BRR=0x016D at PCLK1=42 MHz and 115200 baud; see reviewed formula. | header:USART_BRR_DIV_Mantissa_Msk; usart_review:baud; profile:clock_plan |
| CR1 | SBK | 0:0 | 0x1 | Send break | header:USART_CR1_SBK_Msk; usart_review:CR1.SBK |
| CR1 | RWU | 1:1 | 0x2 | Receiver wakeup | header:USART_CR1_RWU_Msk; usart_review:CR1.RWU |
| CR1 | RE | 2:2 | 0x4 | Receiver enable | header:USART_CR1_RE_Msk; usart_review:CR1.RE |
| CR1 | TE | 3:3 | 0x8 | Transmitter enable | header:USART_CR1_TE_Msk; usart_review:CR1.TE |
| CR1 | IDLEIE | 4:4 | 0x10 | Idle IRQ | header:USART_CR1_IDLEIE_Msk; usart_review:CR1.IDLEIE |
| CR1 | RXNEIE | 5:5 | 0x20 | Receive IRQ | header:USART_CR1_RXNEIE_Msk; usart_review:CR1.RXNEIE |
| CR1 | TCIE | 6:6 | 0x40 | Complete IRQ | header:USART_CR1_TCIE_Msk; usart_review:CR1.TCIE |
| CR1 | TXEIE | 7:7 | 0x80 | Empty IRQ | header:USART_CR1_TXEIE_Msk; usart_review:CR1.TXEIE |
| CR1 | PEIE | 8:8 | 0x100 | Parity IRQ | header:USART_CR1_PEIE_Msk; usart_review:CR1.PEIE |
| CR1 | PS | 9:9 | 0x200 | Parity selection | header:USART_CR1_PS_Msk; usart_review:CR1.PS |
| CR1 | PCE | 10:10 | 0x400 | Parity enable | header:USART_CR1_PCE_Msk; usart_review:CR1.PCE |
| CR1 | WAKE | 11:11 | 0x800 | Wake method | header:USART_CR1_WAKE_Msk; usart_review:CR1.WAKE |
| CR1 | M | 12:12 | 0x1000 | 0: 8 data bits; 1: 9 (parity consumes a bit) | header:USART_CR1_M_Msk; usart_review:CR1.M |
| CR1 | UE | 13:13 | 0x2000 | USART enable | header:USART_CR1_UE_Msk; usart_review:CR1.UE |
| CR1 | OVER8 | 15:15 | 0x8000 | 0: oversample16; 1: oversample8 | header:USART_CR1_OVER8_Msk; usart_review:CR1.OVER8 |
| CR2 | ADD | 3:0 | 0xF | USART node address | header:USART_CR2_ADD_Msk; usart_review:CR2.ADD |
| CR2 | LBDL | 5:5 | 0x20 | LIN break length | header:USART_CR2_LBDL_Msk; usart_review:CR2.LBDL |
| CR2 | LBDIE | 6:6 | 0x40 | LIN break IRQ | header:USART_CR2_LBDIE_Msk; usart_review:CR2.LBDIE |
| CR2 | LBCL | 8:8 | 0x100 | Last bit clock | header:USART_CR2_LBCL_Msk; usart_review:CR2.LBCL |
| CR2 | CPHA | 9:9 | 0x200 | Clock phase | header:USART_CR2_CPHA_Msk; usart_review:CR2.CPHA |
| CR2 | CPOL | 10:10 | 0x400 | Clock polarity | header:USART_CR2_CPOL_Msk; usart_review:CR2.CPOL |
| CR2 | CLKEN | 11:11 | 0x800 | Synchronous clock enable | header:USART_CR2_CLKEN_Msk; usart_review:CR2.CLKEN |
| CR2 | STOP | 13:12 | 0x3000 | 00 one; 01 half; 10 two; 11 one-and-half stop bits | header:USART_CR2_STOP_Msk; usart_review:CR2.STOP |
| CR2 | LINEN | 14:14 | 0x4000 | LIN enable | header:USART_CR2_LINEN_Msk; usart_review:CR2.LINEN |
| CR3 | EIE | 0:0 | 0x1 | See reviewed operating semantics and RM0368 | header:USART_CR3_EIE_Msk; usart_review:CR3.EIE |
| CR3 | IREN | 1:1 | 0x2 | See reviewed operating semantics and RM0368 | header:USART_CR3_IREN_Msk; usart_review:CR3.IREN |
| CR3 | IRLP | 2:2 | 0x4 | See reviewed operating semantics and RM0368 | header:USART_CR3_IRLP_Msk; usart_review:CR3.IRLP |
| CR3 | HDSEL | 3:3 | 0x8 | See reviewed operating semantics and RM0368 | header:USART_CR3_HDSEL_Msk; usart_review:CR3.HDSEL |
| CR3 | NACK | 4:4 | 0x10 | See reviewed operating semantics and RM0368 | header:USART_CR3_NACK_Msk; usart_review:CR3.NACK |
| CR3 | SCEN | 5:5 | 0x20 | See reviewed operating semantics and RM0368 | header:USART_CR3_SCEN_Msk; usart_review:CR3.SCEN |
| CR3 | DMAR | 6:6 | 0x40 | See reviewed operating semantics and RM0368 | header:USART_CR3_DMAR_Msk; usart_review:CR3.DMAR |
| CR3 | DMAT | 7:7 | 0x80 | See reviewed operating semantics and RM0368 | header:USART_CR3_DMAT_Msk; usart_review:CR3.DMAT |
| CR3 | RTSE | 8:8 | 0x100 | See reviewed operating semantics and RM0368 | header:USART_CR3_RTSE_Msk; usart_review:CR3.RTSE |
| CR3 | CTSE | 9:9 | 0x200 | See reviewed operating semantics and RM0368 | header:USART_CR3_CTSE_Msk; usart_review:CR3.CTSE |
| CR3 | CTSIE | 10:10 | 0x400 | See reviewed operating semantics and RM0368 | header:USART_CR3_CTSIE_Msk; usart_review:CR3.CTSIE |
| CR3 | ONEBIT | 11:11 | 0x800 | See reviewed operating semantics and RM0368 | header:USART_CR3_ONEBIT_Msk; usart_review:CR3.ONEBIT |
| GTPR | PSC | 7:0 | 0xFF | Prescaler | header:USART_GTPR_PSC_Msk; usart_review:GTPR.PSC |
| GTPR | GT | 15:8 | 0xFF00 | Guard time | header:USART_GTPR_GT_Msk; usart_review:GTPR.GT |

## Reviewed operating semantics

Supported workflow: asynchronous USART2 on PA2/PA3, 8N1, OVER8=0. The complete
USART structure is retained; UART4/5 expose the same declaration type but not
every USART-specific operating feature. Their unsupported modes need review.

- Baud = f_PCLK / (8 * (2 - OVER8) * USARTDIV).
- OVER8=0: BRR=round(f_PCLK/baud), with a nonzero mantissa and a 16-bit BRR.
- At PCLK1=42,000,000 Hz and 115200 baud, BRR=365=0x016D. The resulting nominal
  baud is 115068.493, about -0.1142%; oscillator tolerance is additional error.
- OVER8=1 requires a different fractional encoding and is outside this example.

After [[peripherals/rcc]] and [[peripherals/gpio]], keep UE=0, program BRR=0x16D,
CR2=0 and CR3=0, then set CR1=UE|TE|RE. These assignments apply to a deliberately
reset/quiesced USART2 and must not overwrite an active configuration owned by
other firmware. All other unlisted bits retain their documented reset values.

Transmit only after TXE=1 with a bounded wait. Wait for TC before disabling an
active transmitter. Reading DR consumes receive data. Clear PE/FE/NE/ORE/IDLE
using the specified SR-read followed by DR-read sequence. This USART has SR/DR,
not ISR/RDR/TDR or an invented ICR. Other SR flags have their own clear behavior;
generic read-modify-write is not a substitute for the manual.

Polling stops at this stage. For receive interrupts, retrieve [[peripherals/nvic]]
before enabling RXNEIE. DMAR/DMAT remain zero; DMA register configuration has not
been supplied and must not be generated from this UART document alone.

Evidence: `usart_review` (RM0090 USART operating semantics), `header`
(USART_TypeDef and USART_* masks), and `profile:clock_plan` (PCLK1 and baud basis).
See [[schemas/custom_pcb_netlist]], [[sources]], and [[index]].

## Review

Reviewer: Codex source-backed F407 fixture editorial review. Basis: Pinned ST/Arm declarations, DS8626 and ST clock example; independent board and semantics sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
