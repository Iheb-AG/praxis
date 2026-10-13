# AVR global interrupt state and USART0 vector

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/usart]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CPU_IRQ | 0x00000000 | AVR data space | CPU clock | header:instance:CPU_IRQ; interrupts_review:clock:CPU_IRQ |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SREG | 0x05F | 8 | 0x3F | RW | 0x0 | I gates global interrupts. Save/restore prior state around protected operations. | header:register:SREG; interrupts_review:register:SREG |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SREG | C | 0:0 | 0x1 | CPU status flag | interrupts_review:field:C |
| SREG | Z | 1:1 | 0x2 | CPU status flag | interrupts_review:field:Z |
| SREG | N | 2:2 | 0x4 | CPU status flag | interrupts_review:field:N |
| SREG | V | 3:3 | 0x8 | CPU status flag | interrupts_review:field:V |
| SREG | S | 4:4 | 0x10 | CPU status flag | interrupts_review:field:S |
| SREG | H | 5:5 | 0x20 | CPU status flag | interrupts_review:field:H |
| SREG | T | 6:6 | 0x40 | CPU status flag | interrupts_review:field:T |
| SREG | I | 7:7 | 0x80 | Global interrupt enable | interrupts_review:field:I |

## Reviewed operating semantics

ATmega328P has no NVIC and no DMA controller. USART receive uses avr-libc ISR(USART_RX_vect), vector index 18 as defined by the target header. Do not substitute another AVR's vector list or hand-encode a Cortex-M IRQ number.

Keep SREG.I clear while setting up receive state and its handler. Configure [[peripherals/usart]] first, read UCSR0A then UDR0 if draining buffered data is intended, enable UCSR0B.RXCIE0, and restore or deliberately enable the desired global interrupt state last. Reading UDR0 consumes data; there is no generic pending-clear register.

The example installs the ISR and enables the peripheral source while leaving global interrupt enablement to startup/application integration. It stores status and received data without unbounded waits inside the ISR. Preserve prior SREG when entering/leaving critical sections.

Sources: [ATmega328P interrupt and USART chapters](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf), pinned avr-libc vector and ISR definitions. See [[index]] and [[peripherals/usart]].

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
