# Project Praxis hardware execution index

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

## Hardware Execution Dependency Graph

[[peripherals/clock]] → [[peripherals/gpio]] → [[peripherals/usart]] → [[peripherals/interrupts]]

Read this index first. Retrieve the matching net, then follow every stage in order. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- External 16 MHz clock supplied; CLKPR=/1; suitable supply assumed.
- Partial connectivity fixture omits complete power/reset/oscillator circuitry.
- Fuse assumption: CKDIV8 unprogrammed; external clock selection configured before application startup.
- Fuse assumption: Factory defaults are not assumed; no fuse write is performed.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.
