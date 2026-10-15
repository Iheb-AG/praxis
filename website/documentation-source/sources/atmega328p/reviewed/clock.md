Fixture assumption: an externally supplied 16 MHz clock, suitable supply conditions, CKDIV8 unprogrammed, and CLKPR=/1 after startup. This is not the ATmega328P factory-default clock configuration. The fuse choice is a precondition, never a generated fuse-write operation.

Confirm the clock assumptions, preserve interrupt state, and use avr-libc clock_prescale_set or a reviewed timed assembly sequence if a prescaler change is needed; ordinary separated C writes do not guarantee the four-cycle window. The shipped example instead checks CLKPR=/1 and fails if it differs. Clear PRR.PRUSART0 to power USART0. Preserve other power reduction bits.

The fixture omits a complete crystal/resonator, power, reset, and decoupling design; it is a topology sample. No oscillator or fuse is read through a runtime probe. Continue to [[peripherals/gpio]]. Source: [ATmega328P datasheet clock and power chapters](https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf).

