# Project Praxis hardware execution index

Target: `stm32f407vgt6_fixture`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `praxis-f407-example-1`; silicon: `Unspecified; errata review pending`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

## Hardware Execution Dependency Graph

[[peripherals/rcc]] → [[peripherals/gpio]] → [[peripherals/usart]] → [[peripherals/nvic]]

Read this index first. Retrieve the matching net, then follow every stage in order. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- LQFP100; assumed 8 MHz HSE crystal, HSEBYP=0; VDD=3.3 V, internal regulator Scale 1.
- PLLM=8, PLLN=336, PLLP=2, PLLQ=7; SYSCLK=HCLK=168 MHz; AHB /1.
- APB1 /4: PCLK1=42 MHz; APB2 /2: PCLK2=84 MHz; 5 FLASH wait states before raising HCLK.
- Validate actual oscillator, supply, board routing and silicon errata before hardware use.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[schemas/devicetree]]: synthetic topology.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.
