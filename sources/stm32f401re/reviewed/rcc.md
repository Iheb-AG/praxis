Supported scope: HSI16-based USART2 bring-up; this is not a complete PLL/power-mode guide.

1. Keep interrupts masked; set HSION and wait for HSIRDY with a finite timeout.
2. Select SW=00, wait for SWS=00, and use HPRE=/1, PPRE1=/1, PPRE2=/1 only after active peripherals are quiescent.
3. The fixture assumes SYSCLK=HCLK=PCLK1=PCLK2=16,000,000 Hz. APB1 must never exceed 42 MHz; SYSCLK/HCLK max is 84 MHz.
4. Enable GPIOAEN and USART2EN and read back the enable registers before access. USART2 uses PCLK1; timer clock doubling does not apply to USART.
5. Pulse USART2RST only when resetting this peripheral is intended. Preserve other gates and reserved fields.

Physical supply stabilization, decoupling, FLASH latency, and voltage scaling are board/startup responsibilities. No PLL increase is performed here. DMA1EN is needed before any future DMA stream access.

Continue to [[peripherals/gpio]], then [[peripherals/usart]]. Source: [RM0368, RCC chapter](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf).

