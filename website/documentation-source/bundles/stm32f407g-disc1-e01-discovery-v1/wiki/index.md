# Project Praxis hardware execution index

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

## Hardware Execution Dependency Graph

Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.

- [[peripherals/rcc]] requires [[index]]
- [[peripherals/adc]] requires [[peripherals/rcc]]
- [[peripherals/adc_common]] requires [[peripherals/rcc]]
- [[peripherals/can]] requires [[peripherals/rcc]]
- [[peripherals/coredebug]] requires [[index]]
- [[peripherals/crc]] requires [[peripherals/rcc]]
- [[peripherals/dac]] requires [[peripherals/rcc]]
- [[peripherals/dbgmcu]] requires [[peripherals/rcc]]
- [[peripherals/dcmi]] requires [[peripherals/rcc]]
- [[peripherals/dma]] requires [[peripherals/rcc]]
- [[peripherals/dma_stream]] requires [[peripherals/dma]]
- [[peripherals/dwt]] requires [[peripherals/rcc]]
- [[peripherals/eth]] requires [[peripherals/rcc]]
- [[peripherals/gpio]] requires [[peripherals/rcc]]
- [[peripherals/syscfg]] requires [[peripherals/gpio]]
- [[peripherals/exti]] requires [[peripherals/syscfg]]
- [[peripherals/fpu]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank1]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank1e]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank2_3]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank4]] requires [[peripherals/rcc]]
- [[peripherals/i2c]] requires [[peripherals/rcc]]
- [[peripherals/iwdg]] requires [[peripherals/rcc]]
- [[peripherals/mpu]] requires [[peripherals/rcc]]
- [[peripherals/usart]] requires [[peripherals/gpio]]
- [[peripherals/nvic]] requires [[peripherals/usart]]
- [[peripherals/pwr]] requires [[peripherals/rcc]]
- [[peripherals/rng]] requires [[peripherals/rcc]]
- [[peripherals/rtc]] requires [[peripherals/rcc]]
- [[peripherals/scb]] requires [[index]]
- [[peripherals/scnscb]] requires [[peripherals/rcc]]
- [[peripherals/sdio]] requires [[peripherals/rcc]]
- [[peripherals/spi]] requires [[peripherals/rcc]]
- [[peripherals/systick]] requires [[index]]
- [[peripherals/tim]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_device]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_global]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_host]] requires [[peripherals/rcc]]
- [[peripherals/wwdg]] requires [[peripherals/rcc]]

Read this index first. Retrieve the matching net, then follow the applicable graph prefix. GPIO polling stops at GPIO; UART polling stops at USART. Peripheral interrupts require the final stage. Core timer/startup requirements are documented separately. Tool gates establish retrieval evidence, not code correctness or physical behavior.

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

## Peripheral coverage

CMSIS typed register blocks; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

| Entity | Structure | Instances | Status | Registers | Fields | Reviewed registers | Requires | Issues | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adc | ADC_TypeDef | ADC1, ADC2, ADC3 | declarations_only | 20 | 85 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_TypeDef |
| adc_common | ADC_Common_TypeDef | ADC123_COMMON | declarations_only | 3 | 27 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ADC_Common_TypeDef |
| apsr | APSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:APSR_Type |
| can | CAN_TypeDef | CAN1, CAN2 | declarations_only | 89 | 77 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CAN_TypeDef |
| can_fifomailbox | CAN_FIFOMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FIFOMailBox_TypeDef |
| can_filterregister | CAN_FilterRegister_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FilterRegister_TypeDef |
| can_txmailbox | CAN_TxMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_TxMailBox_TypeDef |
| control | CONTROL_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:CONTROL_Type |
| coredebug | CoreDebug_Type | CoreDebug | declarations_only | 4 | 21 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:CoreDebug_Type |
| crc | CRC_TypeDef | CRC | declarations_only | 3 | 3 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:CRC_TypeDef |
| dac | DAC_TypeDef | DAC, DAC1 | declarations_only | 14 | 34 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DAC_TypeDef |
| dbgmcu | DBGMCU_TypeDef | DBGMCU | declarations_only | 4 | 7 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DBGMCU_TypeDef |
| dcmi | DCMI_TypeDef | DCMI | declarations_only | 11 | 35 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DCMI_TypeDef |
| dma | DMA_TypeDef | DMA1, DMA2 | declarations_only | 4 | 80 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_TypeDef |
| dma_stream | DMA_Stream_TypeDef | DMA1_Stream0, DMA1_Stream1, DMA1_Stream2, DMA1_Stream3, DMA1_Stream4, DMA1_Stream5, DMA1_Stream6, DMA1_Stream7, DMA2_Stream0, DMA2_Stream1, DMA2_Stream2, DMA2_Stream3, DMA2_Stream4, DMA2_Stream5, DMA2_Stream6, DMA2_Stream7 | declarations_only | 6 | 27 | 0 | dma | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DMA_Stream_TypeDef |
| dwt | DWT_Type | DWT | declarations_only | 20 | 23 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:DWT_Type |
| eth | ETH_TypeDef | ETH | declarations_only | 56 | 212 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ETH_TypeDef |
| exti | EXTI_TypeDef | EXTI | declarations_only | 6 | 116 | 0 | syscfg | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:EXTI_TypeDef |
| flash | FLASH_TypeDef | FLASH | blocked | 0 | 0 | 0 |  | UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field | header:FLASH_TypeDef |
| fpu | FPU_Type | FPU | declarations_only | 6 | 27 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:FPU_Type |
| fsmc_bank1 | FSMC_Bank1_TypeDef | FSMC_Bank1 | declarations_only | 1 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank1_TypeDef |
| fsmc_bank1e | FSMC_Bank1E_TypeDef | FSMC_Bank1E | declarations_only | 1 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank1E_TypeDef |
| fsmc_bank2_3 | FSMC_Bank2_3_TypeDef | FSMC_Bank2_3 | declarations_only | 10 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank2_3_TypeDef |
| fsmc_bank4 | FSMC_Bank4_TypeDef | FSMC_Bank4 | declarations_only | 5 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank4_TypeDef |
| gpio | GPIO_TypeDef | GPIOA, GPIOB, GPIOC, GPIOD, GPIOE, GPIOF, GPIOG, GPIOH, GPIOI | reviewed_subset | 10 | 161 | 10 | rcc |  | header:GPIO_TypeDef |
| i2c | I2C_TypeDef | I2C1, I2C2, I2C3 | declarations_only | 9 | 60 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:I2C_TypeDef |
| ipsr | IPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:IPSR_Type |
| irqn | IRQn_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:IRQn_Type |
| itm | ITM_Type | ITM | blocked | 0 | 0 | 0 |  | UNSUPPORTED_DECLARATION: UNSUPPORTED_DECLARATION: Unsupported nested member: PORT | cmsis_core:ITM_Type |
| iwdg | IWDG_TypeDef | IWDG | declarations_only | 4 | 5 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:IWDG_TypeDef |
| mpu | MPU_Type | MPU | declarations_only | 11 | 14 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:MPU_Type |
| nvic | NVIC_Type | NVIC | reviewed_subset | 7 | 7 | 7 | usart |  | cmsis_core:NVIC_Type |
| pwr | PWR_TypeDef | PWR | declarations_only | 2 | 16 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:PWR_TypeDef |
| rcc | RCC_TypeDef | RCC | reviewed_subset | 23 | 244 | 6 |  |  | header:RCC_TypeDef |
| rng | RNG_TypeDef | RNG | declarations_only | 3 | 7 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RNG_TypeDef |
| rtc | RTC_TypeDef | RTC | declarations_only | 39 | 142 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RTC_TypeDef |
| scb | SCB_Type | SCB | declarations_only | 20 | 56 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SCB_Type |
| scnscb | SCnSCB_Type | SCnSCB | declarations_only | 2 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SCnSCB_Type |
| sdio | SDIO_TypeDef | SDIO | declarations_only | 18 | 98 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SDIO_TypeDef |
| spi | SPI_TypeDef | I2S2ext, I2S3ext, SPI1, SPI2, SPI3 | declarations_only | 9 | 45 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SPI_TypeDef |
| syscfg | SYSCFG_TypeDef | SYSCFG | declarations_only | 4 | 4 | 0 | gpio | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SYSCFG_TypeDef |
| systick | SysTick_Type | SysTick | declarations_only | 4 | 9 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SysTick_Type |
| tim | TIM_TypeDef | TIM1, TIM10, TIM11, TIM12, TIM13, TIM14, TIM2, TIM3, TIM4, TIM5, TIM6, TIM7, TIM8, TIM9 | declarations_only | 21 | 111 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:TIM_TypeDef |
| tpi | TPI_Type | TPI | blocked | 0 | 0 | 0 |  | DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree | cmsis_core:TPI_Type |
| usart | USART_TypeDef | UART4, UART5, USART1, USART2, USART3, USART6 | reviewed_subset | 7 | 51 | 7 | gpio |  | header:USART_TypeDef |
| usb_otg_device | USB_OTG_DeviceTypeDef | USB_OTG_FS_DEVICE, USB_OTG_HS_DEVICE | declarations_only | 15 | 56 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:USB_OTG_DeviceTypeDef |
| usb_otg_global | USB_OTG_GlobalTypeDef | USB_OTG_FS, USB_OTG_FS_GLOBAL, USB_OTG_HS, USB_OTG_HS_GLOBAL | declarations_only | 16 | 115 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:USB_OTG_GlobalTypeDef |
| usb_otg_host | USB_OTG_HostTypeDef | USB_OTG_FS_HOST, USB_OTG_HS_HOST | declarations_only | 6 | 10 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:USB_OTG_HostTypeDef |
| usb_otg_hostchannel | USB_OTG_HostChannelTypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:USB_OTG_HostChannelTypeDef |
| usb_otg_inendpoint | USB_OTG_INEndpointTypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:USB_OTG_INEndpointTypeDef |
| usb_otg_outendpoint | USB_OTG_OUTEndpointTypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:USB_OTG_OUTEndpointTypeDef |
| wwdg | WWDG_TypeDef | WWDG | declarations_only | 3 | 6 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:WWDG_TypeDef |
| xpsr | xPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:xPSR_Type |

## Workflow readiness

| Workflow | Ready | Required | Dependency closure | Missing evidence |
| --- | --- | --- | --- | --- |
| gpio_led_button | True | True | gpio, rcc |  |
| uart_timer_interrupts | False | False | exti, gpio, nvic, rcc, syscfg, tim, usart | exti: operating semantics not reviewed; syscfg: operating semantics not reviewed; tim.ARR: access/operating semantics unreviewed; tim.CR1: access/operating semantics unreviewed; tim.DIER: access/operating semantics unreviewed; tim.PSC: access/operating semantics unreviewed; tim.SR: access/operating semantics unreviewed; tim: operating semantics not reviewed |

- Reviewed subsets do not establish support for every mode or instance.
- Unreviewed declarations must not be used as initialization guidance.
- Header absence does not prove that silicon lacks a capability.
- Package availability, routing, timing and physical tests remain separate evidence.

See [[coverage]] and [[sources]].

## Board-specific workflow

Model: STM32F407G-DISC1; reference revision: MB997-E-01. Applicability: Reference E-01 circuit only. User confirmed the board model but not the PCB revision. Verify MB997 revision and SB20 before flashing; no equivalence to other revisions is asserted.

Signals: LED_A, LD4, GREEN_USER_LED, LED_B, LD3, ORANGE_USER_LED, RED_LED, LD5, RED_USER_LED, BLUE_LED, LD6, BLUE_USER_LED, USER_BUTTON, B1. Query a signal to retrieve its reviewed board context and separate circuit nets.

GPIO polling route: index → net query → clocks → GPIO. USART is needed only for UART; button polling does not require EXTI. Core timer/interrupt setup is a separate startup concern.

See [[schemas/board]] and [[schemas/components]].

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.
