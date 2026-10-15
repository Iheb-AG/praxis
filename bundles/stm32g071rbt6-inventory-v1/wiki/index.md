# Project Praxis hardware execution index

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

## Hardware Execution Dependency Graph

Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.

- [[peripherals/adc]] requires [[index]]
- [[peripherals/adc_common]] requires [[index]]
- [[peripherals/cec]] requires [[index]]
- [[peripherals/comp]] requires [[index]]
- [[peripherals/comp_common]] requires [[index]]
- [[peripherals/crc]] requires [[index]]
- [[peripherals/dac]] requires [[index]]
- [[peripherals/dbg]] requires [[index]]
- [[peripherals/dma]] requires [[index]]
- [[peripherals/dma_channel]] requires [[index]]
- [[peripherals/dmamux_channel]] requires [[index]]
- [[peripherals/dmamux_channelstatus]] requires [[index]]
- [[peripherals/dmamux_requestgen]] requires [[index]]
- [[peripherals/dmamux_requestgenstatus]] requires [[index]]
- [[peripherals/exti]] requires [[index]]
- [[peripherals/flash]] requires [[index]]
- [[peripherals/gpio]] requires [[index]]
- [[peripherals/i2c]] requires [[index]]
- [[peripherals/iwdg]] requires [[index]]
- [[peripherals/lptim]] requires [[index]]
- [[peripherals/mpu]] requires [[index]]
- [[peripherals/nvic]] requires [[index]]
- [[peripherals/pwr]] requires [[index]]
- [[peripherals/rcc]] requires [[index]]
- [[peripherals/rtc]] requires [[index]]
- [[peripherals/scb]] requires [[index]]
- [[peripherals/spi]] requires [[index]]
- [[peripherals/syscfg]] requires [[index]]
- [[peripherals/systick]] requires [[index]]
- [[peripherals/tamp]] requires [[index]]
- [[peripherals/tim]] requires [[index]]
- [[peripherals/ucpd]] requires [[index]]
- [[peripherals/usart]] requires [[index]]
- [[peripherals/vrefbuf]] requires [[index]]
- [[peripherals/wwdg]] requires [[index]]

Read this index first. Board connectivity is unavailable; retrieve the requested declaration dependency closure. Polling stops at peripheral control; interrupts/DMA require the final stage. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- Active SYSCLK, peripheral clocks, oscillators and prescalers are unknown; no board or startup configuration is represented.

## Routing

- [[schemas/custom_pcb_netlist]]: explicit absence of board connectivity.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.

## Extraction scope

Adapter: `cmsis_cortex_m`; declared CPU: `cortex-m0plus` (source: `profile:target.knowledge_adapter`). Header identity checks: `STM32G071xx_H`, `STM32G071xx`. This is a knowledge-only target. No target firmware assets, sandbox compiler profile, flashing or physical qualification are supplied by this adapter. Clock assumptions and HEDG edges are explicit profile policy, not inferred from a diagram.

## MCU-only applicability

Scope: `profile:target.scope=mcu`. No evaluation board, package pin map, LED/button aliases, active bus clocks or firmware/flash assets are supplied. A missing schematic query is missing evidence, not proof that a signal is absent from the silicon. Register layouts and masks do not establish initialization sequences.

## Peripheral coverage

CMSIS register types and configured instances; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

| Entity | Structure | Instances | Status | Registers | Fields | Reviewed registers | Requires | Issues | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adc | ADC_TypeDef | ADC1 | declarations_only | 14 | 62 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_TypeDef |
| adc_common | ADC_Common_TypeDef | ADC1_COMMON | declarations_only | 1 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_Common_TypeDef |
| apsr | APSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm0plus_h:APSR_Type |
| cec | CEC_TypeDef | CEC | declarations_only | 6 | 40 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CEC_TypeDef |
| comp | COMP_TypeDef | COMP1, COMP2 | declarations_only | 1 | 11 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:COMP_TypeDef |
| comp_common | COMP_Common_TypeDef | COMP12_COMMON | declarations_only | 2 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:COMP_Common_TypeDef |
| control | CONTROL_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm0plus_h:CONTROL_Type |
| crc | CRC_TypeDef | CRC | declarations_only | 5 | 8 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CRC_TypeDef |
| dac | DAC_TypeDef | DAC, DAC1 | declarations_only | 20 | 48 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DAC_TypeDef |
| dbg | DBG_TypeDef | DBG | declarations_only | 4 | 4 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DBG_TypeDef |
| dma | DMA_TypeDef | DMA1 | declarations_only | 2 | 56 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_TypeDef |
| dma_channel | DMA_Channel_TypeDef | DMA1_Channel1, DMA1_Channel2, DMA1_Channel3, DMA1_Channel4, DMA1_Channel5, DMA1_Channel6, DMA1_Channel7 | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_Channel_TypeDef |
| dmamux_channel | DMAMUX_Channel_TypeDef | DMAMUX1, DMAMUX1_Channel0, DMAMUX1_Channel1, DMAMUX1_Channel2, DMAMUX1_Channel3, DMAMUX1_Channel4, DMAMUX1_Channel5, DMAMUX1_Channel6 | declarations_only | 1 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMAMUX_Channel_TypeDef |
| dmamux_channelstatus | DMAMUX_ChannelStatus_TypeDef | DMAMUX1_ChannelStatus | declarations_only | 2 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMAMUX_ChannelStatus_TypeDef |
| dmamux_requestgen | DMAMUX_RequestGen_TypeDef | DMAMUX1_RequestGenerator0, DMAMUX1_RequestGenerator1, DMAMUX1_RequestGenerator2, DMAMUX1_RequestGenerator3 | declarations_only | 1 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMAMUX_RequestGen_TypeDef |
| dmamux_requestgenstatus | DMAMUX_RequestGenStatus_TypeDef | DMAMUX1_RequestGenStatus | declarations_only | 2 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMAMUX_RequestGenStatus_TypeDef |
| exti | EXTI_TypeDef | EXTI | partial_declarations | 10 | 127 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; IMR1: bit fields withheld: UNSUPPORTED_MASK: EXTI_IMR1_IM_Msk: non-contiguous bit field | header:EXTI_TypeDef |
| flash | FLASH_TypeDef | FLASH | declarations_only | 14 | 66 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FLASH_TypeDef |
| gpio | GPIO_TypeDef | GPIOA, GPIOB, GPIOC, GPIOD, GPIOF | declarations_only | 11 | 177 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:GPIO_TypeDef |
| i2c | I2C_TypeDef | I2C1, I2C2 | partial_declarations | 11 | 74 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; OAR2: bit fields withheld: UNSUPPORTED_MASK: I2C_OAR2_OA2MASK05_Msk: non-contiguous bit field | header:I2C_TypeDef |
| ipsr | IPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm0plus_h:IPSR_Type |
| irqn | IRQn_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:IRQn_Type |
| iwdg | IWDG_TypeDef | IWDG | declarations_only | 5 | 7 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:IWDG_TypeDef |
| lptim | LPTIM_TypeDef | LPTIM1, LPTIM2 | declarations_only | 9 | 44 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:LPTIM_TypeDef |
| mpu | MPU_Type | MPU | declarations_only | 5 | 14 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm0plus_h:MPU_Type |
| nvic | NVIC_Type | NVIC | declarations_only | 5 | 5 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm0plus_h:NVIC_Type |
| pwr | PWR_TypeDef | PWR | partial_declarations | 17 | 141 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; CR3: bit fields withheld: UNSUPPORTED_MASK: PWR_CR3_EWUP_Msk: non-contiguous bit field; CR4: bit fields withheld: UNSUPPORTED_MASK: PWR_CR4_WP_Msk: non-contiguous bit field; SR1: bit fields withheld: UNSUPPORTED_MASK: PWR_SR1_WUF_Msk: non-contiguous bit field; SCR: bit fields withheld: UNSUPPORTED_MASK: PWR_SCR_CWUF_Msk: non-contiguous bit field | header:PWR_TypeDef |
| rcc | RCC_TypeDef | RCC | declarations_only | 22 | 191 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RCC_TypeDef |
| rtc | RTC_TypeDef | RTC | declarations_only | 21 | 123 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RTC_TypeDef |
| scb | SCB_Type | SCB | declarations_only | 8 | 25 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm0plus_h:SCB_Type |
| spi | SPI_TypeDef | SPI1, SPI2 | declarations_only | 9 | 53 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SPI_TypeDef |
| syscfg | SYSCFG_TypeDef | SYSCFG | declarations_only | 3 | 21 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SYSCFG_TypeDef |
| systick | SysTick_Type | SysTick | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm0plus_h:SysTick_Type |
| tamp | TAMP_TypeDef | TAMP | declarations_only | 12 | 45 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:TAMP_TypeDef |
| tim | TIM_TypeDef | TIM1, TIM14, TIM15, TIM16, TIM17, TIM2, TIM3, TIM6, TIM7 | partial_declarations | 27 | 119 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; SMCR: bit fields withheld: UNSUPPORTED_MASK: TIM_SMCR_SMS_Msk: non-contiguous bit field; CCMR1: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR1_OC1M_Msk: non-contiguous bit field; CCMR2: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR2_OC3M_Msk: non-contiguous bit field; CCMR3: bit fields withheld: UNSUPPORTED_MASK: TIM_CCMR3_OC5M_Msk: non-contiguous bit field | header:TIM_TypeDef |
| ucpd | UCPD_TypeDef | UCPD1, UCPD2 | declarations_only | 14 | 82 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:UCPD_TypeDef |
| usart | USART_TypeDef | LPUART1, USART1, USART2, USART3, USART4 | partial_declarations | 12 | 95 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; CR1: bit fields withheld: UNSUPPORTED_MASK: USART_CR1_M_Msk: non-contiguous bit field | header:USART_TypeDef |
| vrefbuf | VREFBUF_TypeDef | VREFBUF | declarations_only | 2 | 5 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:VREFBUF_TypeDef |
| wwdg | WWDG_TypeDef | WWDG | declarations_only | 3 | 6 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:WWDG_TypeDef |
| xpsr | xPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm0plus_h:xPSR_Type |

## Workflow readiness

| Workflow | Ready | Required | Dependency closure | Missing evidence |
| --- | --- | --- | --- | --- |
| gpio_output | False | False | gpio, rcc | LED_A: board connectivity not published; gpio.MODER: access/operating semantics unreviewed; gpio.ODR: access/operating semantics unreviewed; gpio: operating semantics not reviewed; rcc: operating semantics not reviewed; rcc: specify workflow register requirements before claiming readiness |
| timer_interrupt | False | False | nvic, rcc, tim | nvic: operating semantics not reviewed; nvic: specify workflow register requirements before claiming readiness; rcc: operating semantics not reviewed; rcc: specify workflow register requirements before claiming readiness; tim.ARR: access/operating semantics unreviewed; tim.CR1: access/operating semantics unreviewed; tim.DIER: access/operating semantics unreviewed; tim.PSC: access/operating semantics unreviewed; tim: operating semantics not reviewed |
| uart_polling | False | False | gpio, rcc, usart | gpio: operating semantics not reviewed; gpio: specify workflow register requirements before claiming readiness; rcc: operating semantics not reviewed; rcc: specify workflow register requirements before claiming readiness; usart.BRR: access/operating semantics unreviewed; usart.CR1: access/operating semantics unreviewed; usart: operating semantics not reviewed |

- Reviewed subsets do not establish support for every mode or instance.
- Unreviewed declarations must not be used as initialization guidance.
- Header absence does not prove that silicon lacks a capability.
- Package availability, routing, timing and physical tests remain separate evidence.

Complete source hashes, versions and origins: [[sources]].

See [[coverage]] and [[sources]].

## Mode-specific support

See [[features]] for instance-scoped operating contracts. Header coverage does not establish complete MCU feature support.

| Entity | Reviewed mode | Instances |
| --- | --- | --- |

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.
