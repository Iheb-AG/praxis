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

