ATmega328P-PU uses a 28-pin DIP package. USART0 has fixed alternate pin functions; no AFR register, AF7 selection, RCC, or NVIC exists on this target.

| MCU pin | Physical DIP28 pin | Function |
| --- | --- | --- |
| PD0 | 2 | USART0_RXD |
| PD1 | 3 | USART0_TXD |

After [[peripherals/clock]], keep PD0 input and select PD1 output while preserving other DDRD bits. Clear PD0 pull-up for the fixture's externally driven RX; do not assume floating RX is valid. Enabling RXEN0/TXEN0 activates the USART pin overrides described by the datasheet. Never read-modify-write PIND: writing ones toggles PORTD.

The tables distinguish I/O addresses (used by IN/OUT when accessible) from data-space addresses (used by C SFR access). These are not interchangeable literal pointers. Confirm [[schemas/custom_pcb_netlist]] then retrieve [[peripherals/usart]]. Source: [ATmega328P package and Port D tables](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

