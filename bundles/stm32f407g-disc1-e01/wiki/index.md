# Project Praxis hardware execution index

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

## Hardware Execution Dependency Graph

[[peripherals/rcc]] → [[peripherals/gpio]] → [[peripherals/usart]] → [[peripherals/nvic]]

Read this index first. Retrieve the matching net, then follow every stage in order. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- Reference board: STM32F407G-DISC1, MB997 E-01 schematic. Actual card revision is unconfirmed.
- 8 MHz X2 crystal is documented for E-01; verify oscillator assembly and solder bridges against the actual card.
- 168 MHz is a validated software clock recipe, NOT a claim about the running firmware. Preserve a known working clock setup for GPIO tests.
- Recipe only: PLLM=8, PLLN=336, PLLP=2, PLLQ=7; AHB /1; APB1 /4 (42 MHz); APB2 /2 (84 MHz); 5 FLASH wait states, supply within the reviewed range.
- SysTick_Config uses the processor clock. For 1 ms use actual SystemCoreClock / 1000 after synchronizing SystemCoreClock; do not divide by 8.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.

## Board-specific workflow

Model: STM32F407G-DISC1; reference revision: MB997-E-01. Applicability: Reference E-01 circuit only. User confirmed the board model but not the PCB revision. Verify MB997 revision and SB20 before flashing; no equivalence to other revisions is asserted.

Signals: LED_A, LD4, GREEN_USER_LED, LED_B, LD3, ORANGE_USER_LED, RED_LED, LD5, RED_USER_LED, BLUE_LED, LD6, BLUE_USER_LED, USER_BUTTON, B1. Query a signal to retrieve its reviewed board context and separate circuit nets.

GPIO polling route: index → net query → clocks → GPIO. USART is needed only for UART; button polling does not require EXTI. Core timer/interrupt setup is a separate startup concern.

See [[schemas/board]] and [[schemas/components]].

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.
