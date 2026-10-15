# Project Praxis hardware execution index

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

## Hardware Execution Dependency Graph

[[peripherals/rcc]] → [[peripherals/gpio]] → [[peripherals/usart]] → [[peripherals/nvic]]

Read this index first. Retrieve the matching net, then follow every stage in order. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- HSI16 selected; HCLK, PCLK1 and PCLK2 all /1 at nominal 16 MHz.
- Startup must confirm readiness; HSI tolerance is not simulated.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[schemas/devicetree]]: synthetic topology.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.
