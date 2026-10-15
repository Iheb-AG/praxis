# AVR Port D: fixed USART0 pins

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/clock]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PORTD | 0x00000000 | AVR data space | CPU I/O clock | header:instance:PORTD; gpio_review:clock:PORTD |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PIND | 0x029 | 8 | 0x09 | mixed | not asserted | Read samples pins. Writing a 1 toggles the PORTD latch. | header:register:PIND; gpio_review:register:PIND |
| DDRD | 0x02A | 8 | 0x0A | RW | 0x0 | Preserve unrelated pins. | header:register:DDRD; gpio_review:register:DDRD |
| PORTD | 0x02B | 8 | 0x0B | RW | 0x0 | When DDR=0, latch enables pull-up unless globally disabled. | header:register:PORTD; gpio_review:register:PORTD |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| PIND | PIND0 | 0:0 | 0x1 | Input sample / write-one toggle | gpio_review:field:PIND0 |
| PIND | PIND1 | 1:1 | 0x2 | Input sample / write-one toggle | gpio_review:field:PIND1 |
| PIND | PIND2 | 2:2 | 0x4 | Input sample / write-one toggle | gpio_review:field:PIND2 |
| PIND | PIND3 | 3:3 | 0x8 | Input sample / write-one toggle | gpio_review:field:PIND3 |
| PIND | PIND4 | 4:4 | 0x10 | Input sample / write-one toggle | gpio_review:field:PIND4 |
| PIND | PIND5 | 5:5 | 0x20 | Input sample / write-one toggle | gpio_review:field:PIND5 |
| PIND | PIND6 | 6:6 | 0x40 | Input sample / write-one toggle | gpio_review:field:PIND6 |
| PIND | PIND7 | 7:7 | 0x80 | Input sample / write-one toggle | gpio_review:field:PIND7 |
| DDRD | DDD0 | 0:0 | 0x1 | 0 input; 1 output | gpio_review:field:DDD0 |
| DDRD | DDD1 | 1:1 | 0x2 | 0 input; 1 output | gpio_review:field:DDD1 |
| DDRD | DDD2 | 2:2 | 0x4 | 0 input; 1 output | gpio_review:field:DDD2 |
| DDRD | DDD3 | 3:3 | 0x8 | 0 input; 1 output | gpio_review:field:DDD3 |
| DDRD | DDD4 | 4:4 | 0x10 | 0 input; 1 output | gpio_review:field:DDD4 |
| DDRD | DDD5 | 5:5 | 0x20 | 0 input; 1 output | gpio_review:field:DDD5 |
| DDRD | DDD6 | 6:6 | 0x40 | 0 input; 1 output | gpio_review:field:DDD6 |
| DDRD | DDD7 | 7:7 | 0x80 | 0 input; 1 output | gpio_review:field:DDD7 |
| PORTD | PORTD0 | 0:0 | 0x1 | Output latch / input pull-up | gpio_review:field:PORTD0 |
| PORTD | PORTD1 | 1:1 | 0x2 | Output latch / input pull-up | gpio_review:field:PORTD1 |
| PORTD | PORTD2 | 2:2 | 0x4 | Output latch / input pull-up | gpio_review:field:PORTD2 |
| PORTD | PORTD3 | 3:3 | 0x8 | Output latch / input pull-up | gpio_review:field:PORTD3 |
| PORTD | PORTD4 | 4:4 | 0x10 | Output latch / input pull-up | gpio_review:field:PORTD4 |
| PORTD | PORTD5 | 5:5 | 0x20 | Output latch / input pull-up | gpio_review:field:PORTD5 |
| PORTD | PORTD6 | 6:6 | 0x40 | Output latch / input pull-up | gpio_review:field:PORTD6 |
| PORTD | PORTD7 | 7:7 | 0x80 | Output latch / input pull-up | gpio_review:field:PORTD7 |

## Reviewed operating semantics

ATmega328P-PU uses a 28-pin DIP package. USART0 has fixed alternate pin functions; no AFR register, AF7 selection, RCC, or NVIC exists on this target.

| MCU pin | Physical DIP28 pin | Function |
| --- | --- | --- |
| PD0 | 2 | USART0_RXD |
| PD1 | 3 | USART0_TXD |

After [[peripherals/clock]], keep PD0 input and select PD1 output while preserving other DDRD bits. Clear PD0 pull-up for the fixture's externally driven RX; do not assume floating RX is valid. Enabling RXEN0/TXEN0 activates the USART pin overrides described by the datasheet. Never read-modify-write PIND: writing ones toggles PORTD.

The tables distinguish I/O addresses (used by IN/OUT when accessible) from data-space addresses (used by C SFR access). These are not interchangeable literal pointers. Confirm [[schemas/custom_pcb_netlist]] then retrieve [[peripherals/usart]]. Source: [ATmega328P package and Port D tables](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
