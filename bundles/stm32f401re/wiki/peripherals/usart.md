# USART2: registers and baud calculation

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USART2 | 0x40004400 | APB1 | PCLK1; RCC_APB1ENR.USART2EN | header:instance:USART2; usart_review:clock:USART2 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | mixed | 0xC0 | PE/FE/NF/ORE/IDLE clear by SR-read then DR-read. RXNE clears by DR-read. TC also has SR-read then DR-write sequence. See manual for write-zero flag clears. | header:register:SR; usart_review:register:SR |
| DR | 0x004 | 32 | — | mixed | not asserted | Read consumes received data; write queues transmit data. | header:register:DR; usart_review:register:DR |
| BRR | 0x008 | 32 | — | RW | 0x0 | Change only while communication is quiescent. | header:register:BRR; usart_review:register:BRR |
| CR1 | 0x00C | 32 | — | RW | 0x0 | Configure frame/baud before UE; enable interrupt sources only with handler ready. | header:register:CR1; usart_review:register:CR1 |
| CR2 | 0x010 | 32 | — | RW | 0x0 | Asynchronous 8N1: STOP=00 and CLKEN=0. | header:register:CR2; usart_review:register:CR2 |
| CR3 | 0x014 | 32 | — | RW | 0x0 | Set DMAR/DMAT only after DMA stream configuration. | header:register:CR3; usart_review:register:CR3 |
| GTPR | 0x018 | 32 | — | RW | 0x0 | Smartcard/IrDA; unused for asynchronous fixture. | header:register:GTPR; usart_review:register:GTPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | PE | 0:0 | 0x1 | Parity error | usart_review:field:PE |
| SR | FE | 1:1 | 0x2 | Framing error | usart_review:field:FE |
| SR | NF | 2:2 | 0x4 | Noise detected | usart_review:field:NF |
| SR | ORE | 3:3 | 0x8 | Overrun | usart_review:field:ORE |
| SR | IDLE | 4:4 | 0x10 | Idle line | usart_review:field:IDLE |
| SR | RXNE | 5:5 | 0x20 | Receive data ready | usart_review:field:RXNE |
| SR | TC | 6:6 | 0x40 | Transmission complete | usart_review:field:TC |
| SR | TXE | 7:7 | 0x80 | Transmit data register empty | usart_review:field:TXE |
| SR | LBD | 8:8 | 0x100 | LIN break detected | usart_review:field:LBD |
| SR | CTS | 9:9 | 0x200 | CTS changed | usart_review:field:CTS |
| DR | DR | 8:0 | 0x1FF | Data; use low 8 bits for 8N1 | usart_review:field:DR |
| BRR | DIV_Fraction | 3:0 | 0xF | Four bits at OVER8=0; bit3 must be zero at OVER8=1 | usart_review:field:DIV_Fraction |
| BRR | DIV_Mantissa | 15:4 | 0xFFF0 | Integer USARTDIV | usart_review:field:DIV_Mantissa |
| CR1 | SBK | 0:0 | 0x1 | Send break | usart_review:field:SBK |
| CR1 | RWU | 1:1 | 0x2 | Receiver wakeup | usart_review:field:RWU |
| CR1 | RE | 2:2 | 0x4 | Receiver enable | usart_review:field:RE |
| CR1 | TE | 3:3 | 0x8 | Transmitter enable | usart_review:field:TE |
| CR1 | IDLEIE | 4:4 | 0x10 | Idle IRQ | usart_review:field:IDLEIE |
| CR1 | RXNEIE | 5:5 | 0x20 | Receive IRQ | usart_review:field:RXNEIE |
| CR1 | TCIE | 6:6 | 0x40 | Complete IRQ | usart_review:field:TCIE |
| CR1 | TXEIE | 7:7 | 0x80 | Empty IRQ | usart_review:field:TXEIE |
| CR1 | PEIE | 8:8 | 0x100 | Parity IRQ | usart_review:field:PEIE |
| CR1 | PS | 9:9 | 0x200 | Parity selection | usart_review:field:PS |
| CR1 | PCE | 10:10 | 0x400 | Parity enable | usart_review:field:PCE |
| CR1 | WAKE | 11:11 | 0x800 | Wake method | usart_review:field:WAKE |
| CR1 | M | 12:12 | 0x1000 | 0: 8 data bits; 1: 9 (parity consumes a bit) | usart_review:field:M |
| CR1 | UE | 13:13 | 0x2000 | USART enable | usart_review:field:UE |
| CR1 | OVER8 | 15:15 | 0x8000 | 0: oversample16; 1: oversample8 | usart_review:field:OVER8 |
| CR2 | ADD | 3:0 | 0xF | USART node address | usart_review:field:ADD |
| CR2 | LBDL | 5:5 | 0x20 | LIN break length | usart_review:field:LBDL |
| CR2 | LBDIE | 6:6 | 0x40 | LIN break IRQ | usart_review:field:LBDIE |
| CR2 | LBCL | 8:8 | 0x100 | Last bit clock | usart_review:field:LBCL |
| CR2 | CPHA | 9:9 | 0x200 | Clock phase | usart_review:field:CPHA |
| CR2 | CPOL | 10:10 | 0x400 | Clock polarity | usart_review:field:CPOL |
| CR2 | CLKEN | 11:11 | 0x800 | Synchronous clock enable | usart_review:field:CLKEN |
| CR2 | STOP | 13:12 | 0x3000 | 00 one; 01 half; 10 two; 11 one-and-half stop bits | usart_review:field:STOP |
| CR2 | LINEN | 14:14 | 0x4000 | LIN enable | usart_review:field:LINEN |
| CR3 | EIE | 0:0 | 0x1 | See reviewed operating semantics and RM0368 | usart_review:field:EIE |
| CR3 | IREN | 1:1 | 0x2 | See reviewed operating semantics and RM0368 | usart_review:field:IREN |
| CR3 | IRLP | 2:2 | 0x4 | See reviewed operating semantics and RM0368 | usart_review:field:IRLP |
| CR3 | HDSEL | 3:3 | 0x8 | See reviewed operating semantics and RM0368 | usart_review:field:HDSEL |
| CR3 | NACK | 4:4 | 0x10 | See reviewed operating semantics and RM0368 | usart_review:field:NACK |
| CR3 | SCEN | 5:5 | 0x20 | See reviewed operating semantics and RM0368 | usart_review:field:SCEN |
| CR3 | DMAR | 6:6 | 0x40 | See reviewed operating semantics and RM0368 | usart_review:field:DMAR |
| CR3 | DMAT | 7:7 | 0x80 | See reviewed operating semantics and RM0368 | usart_review:field:DMAT |
| CR3 | RTSE | 8:8 | 0x100 | See reviewed operating semantics and RM0368 | usart_review:field:RTSE |
| CR3 | CTSE | 9:9 | 0x200 | See reviewed operating semantics and RM0368 | usart_review:field:CTSE |
| CR3 | CTSIE | 10:10 | 0x400 | See reviewed operating semantics and RM0368 | usart_review:field:CTSIE |
| CR3 | ONEBIT | 11:11 | 0x800 | See reviewed operating semantics and RM0368 | usart_review:field:ONEBIT |
| GTPR | PSC | 7:0 | 0xFF | Prescaler | usart_review:field:PSC |
| GTPR | GT | 15:8 | 0xFF00 | Guard time | usart_review:field:GT |

## Reviewed operating semantics

Use only this STM32F401 register layout; newer STM32 USARTs with ISR/RDR/TDR have different offsets and flag-clear behavior.

For asynchronous operation:

- baud = f_PCLK / (8 × (2 − OVER8) × USARTDIV).
- OVER8=0: BRR=round(f_PCLK/baud); USARTDIV=BRR/16. Validate the mantissa is at least 1 and the value fits 16 bits.
- OVER8=1: let d=round(f_PCLK/baud), then mantissa=d//8, fraction=d%8, BRR=(mantissa<<4)|fraction. BRR bit3 stays zero. Validate the mantissa range.
- At PCLK1=16 MHz and 115200 baud with OVER8=0: BRR=139=0x008B; actual baud≈115107.91 (−0.080%). Clock tolerance is additional error.

After [[peripherals/rcc]] and [[peripherals/gpio]], keep UE=0, program BRR=0x8B, CR2=0 and CR3=0, then set CR1=UE|TE|RE for 8N1. These assignments apply to a deliberately quiesced/reset USART2 and must not overwrite another user's active configuration.

Transmit only when TXE=1, with a bounded wait; wait for TC before turning off the peripheral. Reading DR consumes RX data. For PE/FE/NF/ORE/IDLE, perform the documented SR-read then DR-read sequence. Do not invent an ICR register or clear flags by generic read-modify-write.

Bit meanings in CR3: EIE error IRQ; IREN IrDA; IRLP IrDA low power; HDSEL half duplex; NACK smartcard NACK; SCEN smartcard; DMAR receive DMA; DMAT transmit DMA; RTSE/CTSE hardware flow control; CTSIE CTS IRQ; ONEBIT one-sample receive mode. Unlisted bits are reserved and retain their reset values.

For interrupt receive, proceed to [[peripherals/nvic]] before enabling RXNEIE. DMA request bits remain zero in the shipped examples. See [RM0368 USART](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf) and [[schemas/custom_pcb_netlist]].

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
