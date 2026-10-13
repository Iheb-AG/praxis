ATmega328P has no NVIC and no DMA controller. USART receive uses avr-libc ISR(USART_RX_vect), vector index 18 as defined by the target header. Do not substitute another AVR's vector list or hand-encode a Cortex-M IRQ number.

Keep SREG.I clear while setting up receive state and its handler. Configure [[peripherals/usart]] first, read UCSR0A then UDR0 if draining buffered data is intended, enable UCSR0B.RXCIE0, and restore or deliberately enable the desired global interrupt state last. Reading UDR0 consumes data; there is no generic pending-clear register.

The example installs the ISR and enables the peripheral source while leaving global interrupt enablement to startup/application integration. It stores status and received data without unbounded waits inside the ISR. Preserve prior SREG when entering/leaving critical sections.

Sources: [ATmega328P interrupt and USART chapters](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf), pinned avr-libc vector and ISR definitions. See [[index]] and [[peripherals/usart]].

