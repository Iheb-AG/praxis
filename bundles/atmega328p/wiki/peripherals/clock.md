# AVR clock prescaler and power reduction

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CPU | 0x00000000 | AVR data space | 16 MHz external fixture clock | header:instance:CPU; clock_review:clock:CPU |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CLKPR | 0x061 | 8 | — | RW | not asserted | Timed unlock sequence; CLKPS change must follow CLKPCE within four cycles. | header:register:CLKPR; clock_review:register:CLKPR |
| PRR | 0x064 | 8 | — | RW | 0x0 | 0 enables peripheral clock; do not confuse with STM32 gate polarity. | header:register:PRR; clock_review:register:PRR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CLKPR | CLKPS | 3:0 | 0xF | 0000 /1; 0001 /2; ... 1000 /256; higher codes reserved | clock_review:field:CLKPS |
| CLKPR | CLKPCE | 7:7 | 0x80 | Clock prescaler change enable | clock_review:field:CLKPCE |
| PRR | PRADC | 0:0 | 0x1 | ADC power reduction | clock_review:field:PRADC |
| PRR | PRUSART0 | 1:1 | 0x2 | USART0 power reduction | clock_review:field:PRUSART0 |
| PRR | PRSPI | 2:2 | 0x4 | SPI power reduction | clock_review:field:PRSPI |
| PRR | PRTIM1 | 3:3 | 0x8 | Timer1 power reduction | clock_review:field:PRTIM1 |
| PRR | PRTIM0 | 5:5 | 0x20 | Timer0 power reduction | clock_review:field:PRTIM0 |
| PRR | PRTIM2 | 6:6 | 0x40 | Timer2 power reduction | clock_review:field:PRTIM2 |
| PRR | PRTWI | 7:7 | 0x80 | TWI power reduction | clock_review:field:PRTWI |

## Reviewed operating semantics

Fixture assumption: an externally supplied 16 MHz clock, suitable supply conditions, CKDIV8 unprogrammed, and CLKPR=/1 after startup. This is not the ATmega328P factory-default clock configuration. The fuse choice is a precondition, never a generated fuse-write operation.

Confirm the clock assumptions, preserve interrupt state, and use avr-libc clock_prescale_set or a reviewed timed assembly sequence if a prescaler change is needed; ordinary separated C writes do not guarantee the four-cycle window. The shipped example instead checks CLKPR=/1 and fails if it differs. Clear PRR.PRUSART0 to power USART0. Preserve other power reduction bits.

The fixture omits a complete crystal/resonator, power, reset, and decoupling design; it is a topology sample. No oscillator or fuse is read through a runtime probe. Continue to [[peripherals/gpio]]. Source: [ATmega328P datasheet clock and power chapters](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
