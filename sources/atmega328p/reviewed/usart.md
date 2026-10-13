Asynchronous baud = f_CPU / (divider × (UBRR0+1)), where divider=16 when U2X0=0 and 8 when U2X0=1. Compute and compare actual error before choosing the mode.

The fixture uses 16 MHz, 9600 baud, U2X0=0, and UBRR0=103=0x0067. Actual baud≈9615.38 (+0.160%). UBRR0 is 12 bits; reject values outside 0..4095. The normal-mode 115200-baud choice at 16 MHz has substantial error and is not the shipped default.

After [[peripherals/clock]] and [[peripherals/gpio]], quiesce USART0, write UCSR0B=0, UCSR0A=0 (clears U2X0/MPCM0 without writing a 1 to TXC0), UBRR0H then UBRR0L, UCSR0C=UCSZ01|UCSZ00, and UCSR0B=RXEN0|TXEN0. Poll UDRE0 with a finite timeout before writing UDR0. Wait for TXC0 before shutting down transmission; clear stale TXC0 by its documented write-one behavior when beginning a completion-tracked send.

UCSR0A: MPCM0 multiprocessor mode; U2X0 double-speed; UPE0 parity error; DOR0 overrun; FE0 framing error; UDRE0 data-register empty; TXC0 complete (W1C); RXC0 unread receive data. Read UCSR0A before UDR0 to associate errors with the buffered byte.

UCSR0B: TXB80/RXB80 ninth data bits; UCSZ02 high character-size bit; TXEN0/RXEN0 enable TX/RX; UDRIE0/TXCIE0/RXCIE0 enable their IRQ sources. RXC0 clears as the receive buffer is consumed; no STM32 SR/DR flag-clear sequence applies.

Proceed to [[peripherals/interrupts]] for RXCIE0. DMA is unsupported by ATmega328P. Source: [ATmega328P USART chapter](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

