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


## Reviewed interrupt-driven USART2 loopback subset

For explicitly established PCLK1=16,000,000 Hz and OVER8=0, BRR=round(16000000/115200)=139 (0x008B); nominal baud=115107.914, error about -0.080%. Do not use 0x016D from the optional 42 MHz recipe in this configuration. HSI tolerance and physical timing remain unmeasured. Set UE=0 on a reset/quiesced owned USART2; program BRR, CR2=0 and CR3=0, then UE|TE|RE. Mask interrupts and prepare queues before RXNEIE or the NVIC line. TXEIE is enabled only when a queued byte exists and disabled when the transmit queue empties; TXE means DR available, not final stop-bit completion (TC).

The bounded ISR reads SR once, then DR on RXNE or receive error, capturing/discarding the affected byte as appropriate. SR-read then DR-read clears ORE/FE/NE; RXNE clears on DR read. Parity is disabled; if enabling parity in a future workflow, obey the PE/RXNE clearing condition separately. RXNEIE also enables ORE notification. FE/NE are sampled with RXNE in this single-buffer mode; CR3.EIE is not used and must not be described as a universal standalone error interrupt. No DMA, IDLE interrupt or TC interrupt is enabled. Shared queue indices and CR1.TXEIE updates require bounded critical sections or a proven single-producer/consumer scheme. Main performs frame CRC/validation; ISRs never delay or parse whole frames. Sources: rm_uart_irq:page:1001; rm_uart_sr:page:1003; rm_uart_errors:page:1004; rm_uart_brr:page:1005; rm_uart_cr1:page:1006; rm_uart_rx:page:1007; rm_uart_baud:page:973.
