Supported scope: USART2 external IRQ38. Vector table entry is 16+38=54; provide USART2_IRQHandler in startup integration. The core NVIC register fields are write-one actions, not ordinary peripheral read-modify-write bits.

1. Keep USART2 RXNEIE and its NVIC line disabled while installing a handler and initializing receive state.
2. Configure GPIO/USART first. Drain pending receive/error data according to [[peripherals/usart]] and clear the peripheral cause before NVIC pending state.
3. Program priority through IP[38], using the implemented high four bits. Write bit6 of ICPR[1] to clear IRQ38 pending.
4. Enable RXNEIE, enable NVIC ISER[1] bit6, and only then restore the intended global interrupt state. The example does not globally unmask interrupts.
5. The handler must consume DR when RXNE is asserted and handle the documented error sequence without unbounded waits.

DMA is not implemented by the examples. Future USART2 DMA uses DMA1 stream5/channel4 RX or stream6/channel4 TX; IRQs 16/17 respectively. Enable the DMA clock, disable and wait for stream EN=0, configure addresses/length/channel/direction, clear flags, enable the stream, and enable USART DMA requests last. Detailed DMA register knowledge must be added before generating DMA code.

Sources: [RM0368 interrupt/DMA chapters](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf), pinned ST IRQ declarations and Arm CMSIS core header. See [[peripherals/usart]] and [[index]].

