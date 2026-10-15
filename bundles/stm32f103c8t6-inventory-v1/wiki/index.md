# Project Praxis hardware execution index

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

## Hardware Execution Dependency Graph

Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.

- [[peripherals/adc]] requires [[index]]
- [[peripherals/adc_common]] requires [[index]]
- [[peripherals/afio]] requires [[index]]
- [[peripherals/bkp]] requires [[index]]
- [[peripherals/can]] requires [[index]]
- [[peripherals/coredebug]] requires [[index]]
- [[peripherals/crc]] requires [[index]]
- [[peripherals/dbgmcu]] requires [[index]]
- [[peripherals/dma]] requires [[index]]
- [[peripherals/dma_channel]] requires [[index]]
- [[peripherals/dwt]] requires [[index]]
- [[peripherals/exti]] requires [[index]]
- [[peripherals/flash]] requires [[index]]
- [[peripherals/gpio]] requires [[index]]
- [[peripherals/i2c]] requires [[index]]
- [[peripherals/iwdg]] requires [[index]]
- [[peripherals/nvic]] requires [[index]]
- [[peripherals/ob]] requires [[index]]
- [[peripherals/pwr]] requires [[index]]
- [[peripherals/rcc]] requires [[index]]
- [[peripherals/rtc]] requires [[index]]
- [[peripherals/scb]] requires [[index]]
- [[peripherals/scnscb]] requires [[index]]
- [[peripherals/spi]] requires [[index]]
- [[peripherals/systick]] requires [[index]]
- [[peripherals/tim]] requires [[index]]
- [[peripherals/tpi]] requires [[index]]
- [[peripherals/usart]] requires [[index]]
- [[peripherals/usb]] requires [[index]]
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

Adapter: `cmsis_cortex_m`; declared CPU: `cortex-m3` (source: `profile:target.knowledge_adapter`). Header identity checks: `__STM32F103xB_H`, `STM32F103xB`. This is a knowledge-only target. No target firmware assets, sandbox compiler profile, flashing or physical qualification are supplied by this adapter. Clock assumptions and HEDG edges are explicit profile policy, not inferred from a diagram.

## MCU-only applicability

Scope: `profile:target.scope=mcu`. No evaluation board, package pin map, LED/button aliases, active bus clocks or firmware/flash assets are supplied. A missing schematic query is missing evidence, not proof that a signal is absent from the silicon. Register layouts and masks do not establish initialization sequences.

## Peripheral coverage

CMSIS register types and configured instances; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

| Entity | Structure | Instances | Status | Registers | Fields | Reviewed registers | Requires | Issues | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adc | ADC_TypeDef | ADC1, ADC2 | declarations_only | 20 | 83 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_TypeDef |
| adc_common | ADC_Common_TypeDef | ADC12_COMMON | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_Common_TypeDef |
| afio | AFIO_TypeDef | AFIO | declarations_only | 4 | 15 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:AFIO_TypeDef |
| apsr | APSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm3_h:APSR_Type |
| bkp | BKP_TypeDef | BKP | declarations_only | 13 | 21 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:BKP_TypeDef |
| can | CAN_TypeDef | CAN1 | declarations_only | 61 | 77 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CAN_TypeDef |
| can_fifomailbox | CAN_FIFOMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FIFOMailBox_TypeDef |
| can_filterregister | CAN_FilterRegister_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FilterRegister_TypeDef |
| can_txmailbox | CAN_TxMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_TxMailBox_TypeDef |
| control | CONTROL_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm3_h:CONTROL_Type |
| coredebug | CoreDebug_Type | CoreDebug | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:CoreDebug_Type |
| crc | CRC_TypeDef | CRC | declarations_only | 3 | 3 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CRC_TypeDef |
| dbgmcu | DBGMCU_TypeDef | DBGMCU | declarations_only | 2 | 16 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DBGMCU_TypeDef |
| dma | DMA_TypeDef | DMA1 | declarations_only | 2 | 56 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_TypeDef |
| dma_channel | DMA_Channel_TypeDef | DMA1_Channel1, DMA1_Channel2, DMA1_Channel3, DMA1_Channel4, DMA1_Channel5, DMA1_Channel6, DMA1_Channel7 | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_Channel_TypeDef |
| dwt | DWT_Type | DWT | declarations_only | 20 | 23 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:DWT_Type |
| exti | EXTI_TypeDef | EXTI | declarations_only | 6 | 114 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:EXTI_TypeDef |
| flash | FLASH_TypeDef | FLASH | declarations_only | 8 | 27 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FLASH_TypeDef |
| gpio | GPIO_TypeDef | GPIOA, GPIOB, GPIOC, GPIOD, GPIOE | partial_declarations | 7 | 97 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; CRL: bit fields withheld: UNSUPPORTED_MASK: GPIO_CRL_CNF_Msk: non-contiguous bit field; CRH: bit fields withheld: UNSUPPORTED_MASK: GPIO_CRH_CNF_Msk: non-contiguous bit field | header:GPIO_TypeDef |
| i2c | I2C_TypeDef | I2C1, I2C2 | declarations_only | 9 | 60 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:I2C_TypeDef |
| ipsr | IPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm3_h:IPSR_Type |
| irqn | IRQn_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:IRQn_Type |
| itm | ITM_Type | ITM | blocked | 0 | 0 | 0 |  | UNSUPPORTED_DECLARATION: UNSUPPORTED_DECLARATION: Unsupported nested member: PORT | core_cm3_h:ITM_Type |
| iwdg | IWDG_TypeDef | IWDG | declarations_only | 4 | 5 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:IWDG_TypeDef |
| nvic | NVIC_Type | NVIC | declarations_only | 7 | 7 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:NVIC_Type |
| ob | OB_TypeDef | OB | declarations_only | 8 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:OB_TypeDef |
| pwr | PWR_TypeDef | PWR | declarations_only | 2 | 11 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:PWR_TypeDef |
| rcc | RCC_TypeDef | RCC | partial_declarations | 10 | 94 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; CFGR: bit fields withheld: UNSUPPORTED_MASK: RCC_CFGR_PLLMULL11_Msk: non-contiguous bit field | header:RCC_TypeDef |
| rtc | RTC_TypeDef | RTC | declarations_only | 10 | 17 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RTC_TypeDef |
| scb | SCB_Type | SCB | declarations_only | 20 | 57 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:SCB_Type |
| scnscb | SCnSCB_Type | SCnSCB | declarations_only | 2 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:SCnSCB_Type |
| spi | SPI_TypeDef | SPI1, SPI2 | declarations_only | 8 | 33 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SPI_TypeDef |
| systick | SysTick_Type | SysTick | declarations_only | 4 | 0 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | core_cm3_h:SysTick_Type |
| tim | TIM_TypeDef | TIM1, TIM2, TIM3, TIM4 | declarations_only | 21 | 107 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:TIM_TypeDef |
| tpi | TPI_Type | TPI | partial_declarations | 17 | 32 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted.; DEVTYPE: bit fields withheld: DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree | core_cm3_h:TPI_Type |
| usart | USART_TypeDef | USART1, USART2, USART3 | declarations_only | 7 | 49 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:USART_TypeDef |
| usb | USB_TypeDef | USB | declarations_only | 13 | 111 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:USB_TypeDef |
| wwdg | WWDG_TypeDef | WWDG | declarations_only | 3 | 6 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:WWDG_TypeDef |
| xpsr | xPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | core_cm3_h:xPSR_Type |

## Workflow readiness

| Workflow | Ready | Required | Dependency closure | Missing evidence |
| --- | --- | --- | --- | --- |
| gpio_output | False | False | gpio, rcc | LED_A: board connectivity not published; gpio.CRL: access/operating semantics unreviewed; gpio.ODR: access/operating semantics unreviewed; gpio: operating semantics not reviewed; rcc: operating semantics not reviewed; rcc: specify workflow register requirements before claiming readiness |
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
