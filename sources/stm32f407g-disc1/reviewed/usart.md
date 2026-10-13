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
