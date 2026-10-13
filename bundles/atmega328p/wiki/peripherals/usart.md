# AVR USART0: frame and baud registers

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USART0 | 0x00000000 | AVR data space | CPU clock; PRR.PRUSART0=0 | header:instance:USART0; usart_review:clock:USART0 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UCSR0A | 0x0C0 | 8 | — | mixed | 0x20 | TXC0 is write-one-to-clear. Read status before UDR0 to preserve receive error association. | header:register:UCSR0A; usart_review:register:UCSR0A |
| UCSR0B | 0x0C1 | 8 | — | RW | 0x0 | Enable RXCIE0 only after receive handler/state is ready. | header:register:UCSR0B; usart_review:register:UCSR0B |
| UCSR0C | 0x0C2 | 8 | — | RW | 0x6 | 8N1 asynchronous: UMSEL=00 UPM=00 USBS=0 UCSZ01:00=11. | header:register:UCSR0C; usart_review:register:UCSR0C |
| UBRR0L | 0x0C4 | 8 | — | RW | 0x0 | Write high byte then low byte while communication is quiescent. | header:register:UBRR0L; usart_review:register:UBRR0L |
| UBRR0H | 0x0C5 | 8 | — | RW | 0x0 | Upper four bits reserved. | header:register:UBRR0H; usart_review:register:UBRR0H |
| UDR0 | 0x0C6 | 8 | — | mixed | not asserted | Reading consumes buffered RX byte; writing queues TX byte. | header:register:UDR0; usart_review:register:UDR0 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| UCSR0A | MPCM0 | 0:0 | 0x1 | See reviewed USART operating semantics | usart_review:field:MPCM0 |
| UCSR0A | U2X0 | 1:1 | 0x2 | See reviewed USART operating semantics | usart_review:field:U2X0 |
| UCSR0A | UPE0 | 2:2 | 0x4 | See reviewed USART operating semantics | usart_review:field:UPE0 |
| UCSR0A | DOR0 | 3:3 | 0x8 | See reviewed USART operating semantics | usart_review:field:DOR0 |
| UCSR0A | FE0 | 4:4 | 0x10 | See reviewed USART operating semantics | usart_review:field:FE0 |
| UCSR0A | UDRE0 | 5:5 | 0x20 | See reviewed USART operating semantics | usart_review:field:UDRE0 |
| UCSR0A | TXC0 | 6:6 | 0x40 | See reviewed USART operating semantics | usart_review:field:TXC0 |
| UCSR0A | RXC0 | 7:7 | 0x80 | See reviewed USART operating semantics | usart_review:field:RXC0 |
| UCSR0B | TXB80 | 0:0 | 0x1 | See reviewed USART operating semantics | usart_review:field:TXB80 |
| UCSR0B | RXB80 | 1:1 | 0x2 | See reviewed USART operating semantics | usart_review:field:RXB80 |
| UCSR0B | UCSZ02 | 2:2 | 0x4 | See reviewed USART operating semantics | usart_review:field:UCSZ02 |
| UCSR0B | TXEN0 | 3:3 | 0x8 | See reviewed USART operating semantics | usart_review:field:TXEN0 |
| UCSR0B | RXEN0 | 4:4 | 0x10 | See reviewed USART operating semantics | usart_review:field:RXEN0 |
| UCSR0B | UDRIE0 | 5:5 | 0x20 | See reviewed USART operating semantics | usart_review:field:UDRIE0 |
| UCSR0B | TXCIE0 | 6:6 | 0x40 | See reviewed USART operating semantics | usart_review:field:TXCIE0 |
| UCSR0B | RXCIE0 | 7:7 | 0x80 | See reviewed USART operating semantics | usart_review:field:RXCIE0 |
| UCSR0C | UCPOL0 | 0:0 | 0x1 | Clock polarity; zero in async mode | usart_review:field:UCPOL0 |
| UCSR0C | UCSZ0 | 2:1 | 0x6 | Low character-size bits; 11 selects 8-bit when UCSZ02=0 | usart_review:field:UCSZ0 |
| UCSR0C | USBS0 | 3:3 | 0x8 | 0 one; 1 two stop bits | usart_review:field:USBS0 |
| UCSR0C | UPM0 | 5:4 | 0x30 | 00 none; 10 even; 11 odd parity | usart_review:field:UPM0 |
| UCSR0C | UMSEL0 | 7:6 | 0xC0 | 00 async; 01 synchronous; 11 master SPI | usart_review:field:UMSEL0 |
| UBRR0L | UBRR0_LOW | 7:0 | 0xFF | Low baud-divider bits | usart_review:field:UBRR0_LOW |
| UBRR0H | UBRR0_HIGH | 3:0 | 0xF | High baud-divider bits | usart_review:field:UBRR0_HIGH |
| UDR0 | DATA | 7:0 | 0xFF | 8-bit data | usart_review:field:DATA |

## Reviewed operating semantics

Asynchronous baud = f_CPU / (divider × (UBRR0+1)), where divider=16 when U2X0=0 and 8 when U2X0=1. Compute and compare actual error before choosing the mode.

The fixture uses 16 MHz, 9600 baud, U2X0=0, and UBRR0=103=0x0067. Actual baud≈9615.38 (+0.160%). UBRR0 is 12 bits; reject values outside 0..4095. The normal-mode 115200-baud choice at 16 MHz has substantial error and is not the shipped default.

After [[peripherals/clock]] and [[peripherals/gpio]], quiesce USART0, write UCSR0B=0, UCSR0A=0 (clears U2X0/MPCM0 without writing a 1 to TXC0), UBRR0H then UBRR0L, UCSR0C=UCSZ01|UCSZ00, and UCSR0B=RXEN0|TXEN0. Poll UDRE0 with a finite timeout before writing UDR0. Wait for TXC0 before shutting down transmission; clear stale TXC0 by its documented write-one behavior when beginning a completion-tracked send.

UCSR0A: MPCM0 multiprocessor mode; U2X0 double-speed; UPE0 parity error; DOR0 overrun; FE0 framing error; UDRE0 data-register empty; TXC0 complete (W1C); RXC0 unread receive data. Read UCSR0A before UDR0 to associate errors with the buffered byte.

UCSR0B: TXB80/RXB80 ninth data bits; UCSZ02 high character-size bit; TXEN0/RXEN0 enable TX/RX; UDRIE0/TXCIE0/RXCIE0 enable their IRQ sources. RXC0 clears as the receive buffer is consumed; no STM32 SR/DR flag-clear sequence applies.

Proceed to [[peripherals/interrupts]] for RXCIE0. DMA is unsupported by ATmega328P. Source: [ATmega328P USART chapter](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
