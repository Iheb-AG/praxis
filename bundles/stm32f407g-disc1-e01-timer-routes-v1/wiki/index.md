# Project Praxis hardware execution index

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

## Hardware Execution Dependency Graph

Graph prerequisites are listed below. Retrieve only the requested entity's dependency closure.

- [[peripherals/rcc]] requires [[index]]
- [[peripherals/flash]] requires [[peripherals/rcc]]
- [[peripherals/pwr]] requires [[peripherals/rcc]]
- [[peripherals/adc_common]] requires [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]]
- [[peripherals/adc]] requires [[peripherals/adc_common]]
- [[peripherals/gpio]] requires [[peripherals/rcc]]
- [[peripherals/syscfg]] requires [[peripherals/gpio]]
- [[peripherals/exti]] requires [[peripherals/syscfg]]
- [[peripherals/tim]] requires [[peripherals/rcc]]
- [[peripherals/usart]] requires [[peripherals/gpio]]
- [[peripherals/nvic]] requires [[peripherals/usart]], [[peripherals/tim]], [[peripherals/exti]]
- [[peripherals/can]] requires [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]], [[peripherals/nvic]]
- [[peripherals/coredebug]] requires [[index]]
- [[peripherals/crc]] requires [[peripherals/rcc]]
- [[peripherals/dac]] requires [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]], [[peripherals/gpio]], [[peripherals/tim]]
- [[peripherals/dbgmcu]] requires [[peripherals/rcc]]
- [[peripherals/dcmi]] requires [[peripherals/rcc]]
- [[peripherals/dma]] requires [[peripherals/rcc]]
- [[peripherals/dma_stream]] requires [[peripherals/dma]]
- [[peripherals/dwt]] requires [[peripherals/rcc]]
- [[peripherals/eth]] requires [[peripherals/rcc]]
- [[peripherals/fpu]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank1]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank1e]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank2_3]] requires [[peripherals/rcc]]
- [[peripherals/fsmc_bank4]] requires [[peripherals/rcc]]
- [[peripherals/i2c]] requires [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]]
- [[peripherals/itm]] requires [[peripherals/rcc]]
- [[peripherals/iwdg]] requires [[peripherals/rcc]]
- [[peripherals/mpu]] requires [[peripherals/rcc]]
- [[peripherals/rng]] requires [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]]
- [[peripherals/rtc]] requires [[peripherals/rcc]]
- [[peripherals/scb]] requires [[index]]
- [[peripherals/scnscb]] requires [[peripherals/rcc]]
- [[peripherals/sdio]] requires [[peripherals/rcc]]
- [[peripherals/spi]] requires [[peripherals/rcc]], [[peripherals/gpio]]
- [[peripherals/systick]] requires [[peripherals/rcc]], [[peripherals/scb]]
- [[peripherals/tpi]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_device]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_global]] requires [[peripherals/rcc]]
- [[peripherals/usb_otg_host]] requires [[peripherals/rcc]]
- [[peripherals/wwdg]] requires [[peripherals/rcc]]
Read this index first. Retrieve the matching net when board connectivity is available, then follow the applicable prerequisite edges. A topological listing does not impose dependencies between unrelated entities. Requested workflows determine the required operating modes. Tool gates establish retrieval evidence, not code correctness or physical behavior.

## Clock assumptions

- Reference board: STM32F407G-DISC1, MB997 E-01 schematic. Actual card revision is unconfirmed.
- 8 MHz X2 crystal is documented for E-01; verify oscillator assembly and solder bridges against the actual card.
- 168 MHz is a validated software clock recipe, NOT a claim about the running firmware. Preserve a known working clock setup for GPIO tests.
- Recipe only: PLLM=8, PLLN=336, PLLP=2, PLLQ=7; AHB /1; APB1 /4 (42 MHz); APB2 /2 (84 MHz); 5 FLASH wait states, supply within the reviewed range.
- SysTick_Config uses the processor clock. For 1 ms use actual SystemCoreClock / 1000 after synchronizing SystemCoreClock; do not divide by 8.
- UART loopback application explicitly selects HSI nominal 16 MHz, AHB/APB1/APB2 all /1; the 168 MHz recipe is not used for this scenario. See RCC/USART/TIM2 reviewed notes; timing remains unmeasured.
- ADC example additionally assumes VDDA/VREF+ in the reviewed 2.7–3.6 V operating range; analog supply is not measured or physically qualified.

## Routing

- [[schemas/custom_pcb_netlist]]: direct electrical connectivity.
- [[sources]]: provenance, licenses, and editorial review.

## Startup boundary

Provide startup code and a vector table separately. Keep interrupts masked until their sources and handlers are safe. Quiesce active peripherals before changing clocks. Use bounded readiness waits. No flashing or runtime probe operations are provided.

## Peripheral coverage

CMSIS register types and configured instances; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

| Entity | Structure | Instances | Status | Registers | Fields | Reviewed registers | Requires | Issues | Provenance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| adc | ADC_TypeDef | ADC1, ADC2, ADC3 | reviewed_subset | 20 | 85 | 8 | adc_common |  | header:ADC_TypeDef |
| adc_common | ADC_Common_TypeDef | ADC123_COMMON | reviewed_subset | 3 | 27 | 1 | rcc, flash, pwr |  | header:ADC_Common_TypeDef |
| apsr | APSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:APSR_Type |
| can | CAN_TypeDef | CAN1, CAN2 | reviewed_subset | 89 | 108 | 23 | rcc, flash, pwr, nvic | Configured field views: BTR, ESR, FA1R, FFA1R, FM1R, FMR, FS1R, IER, MCR, MSR, RF0R, RF1R, TSR, sFIFOMailBox_0__RDHR, sFIFOMailBox_0__RDLR, sFIFOMailBox_0__RDTR, sFIFOMailBox_0__RIR, sTxMailBox_0__TDHR, sTxMailBox_0__TDLR, sTxMailBox_0__TDTR, sTxMailBox_0__TIR; other overlapping mode encodings are not published | header:CAN_TypeDef |
| can_fifomailbox | CAN_FIFOMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FIFOMailBox_TypeDef |
| can_filterregister | CAN_FilterRegister_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_FilterRegister_TypeDef |
| can_txmailbox | CAN_TxMailBox_TypeDef |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:CAN_TxMailBox_TypeDef |
| control | CONTROL_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:CONTROL_Type |
| coredebug | CoreDebug_Type | CoreDebug | declarations_only | 4 | 21 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:CoreDebug_Type |
| crc | CRC_TypeDef | CRC | reviewed_subset | 3 | 3 | 3 | rcc |  | header:CRC_TypeDef |
| dac | DAC_TypeDef | DAC, DAC1 | reviewed_subset | 14 | 34 | 14 | rcc, flash, pwr, gpio, tim |  | header:DAC_TypeDef |
| dbgmcu | DBGMCU_TypeDef | DBGMCU | declarations_only | 4 | 7 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DBGMCU_TypeDef |
| dcmi | DCMI_TypeDef | DCMI | declarations_only | 11 | 35 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:DCMI_TypeDef |
| dma | DMA_TypeDef | DMA1, DMA2 | reviewed_subset | 4 | 80 | 4 | rcc |  | header:DMA_TypeDef |
| dma_stream | DMA_Stream_TypeDef | DMA1_Stream0, DMA1_Stream1, DMA1_Stream2, DMA1_Stream3, DMA1_Stream4, DMA1_Stream5, DMA1_Stream6, DMA1_Stream7, DMA2_Stream0, DMA2_Stream1, DMA2_Stream2, DMA2_Stream3, DMA2_Stream4, DMA2_Stream5, DMA2_Stream6, DMA2_Stream7 | reviewed_subset | 6 | 27 | 6 | dma |  | header:DMA_Stream_TypeDef |
| dwt | DWT_Type | DWT | declarations_only | 20 | 23 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:DWT_Type |
| eth | ETH_TypeDef | ETH | declarations_only | 56 | 212 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:ETH_TypeDef |
| exti | EXTI_TypeDef | EXTI | reviewed_subset | 6 | 138 | 6 | syscfg | Configured field views: EMR, IMR; other overlapping mode encodings are not published | header:EXTI_TypeDef |
| flash | FLASH_TypeDef | FLASH | reviewed_subset | 7 | 31 | 1 | rcc | Configured field views: ACR; other overlapping mode encodings are not published | header:FLASH_TypeDef |
| fpu | FPU_Type | FPU | declarations_only | 6 | 27 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:FPU_Type |
| fsmc_bank1 | FSMC_Bank1_TypeDef | FSMC_Bank1 | declarations_only | 1 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank1_TypeDef |
| fsmc_bank1e | FSMC_Bank1E_TypeDef | FSMC_Bank1E | declarations_only | 1 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank1E_TypeDef |
| fsmc_bank2_3 | FSMC_Bank2_3_TypeDef | FSMC_Bank2_3 | declarations_only | 10 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank2_3_TypeDef |
| fsmc_bank4 | FSMC_Bank4_TypeDef | FSMC_Bank4 | declarations_only | 5 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:FSMC_Bank4_TypeDef |
| gpio | GPIO_TypeDef | GPIOA, GPIOB, GPIOC, GPIOD, GPIOE, GPIOF, GPIOG, GPIOH, GPIOI | reviewed_subset | 10 | 161 | 10 | rcc |  | header:GPIO_TypeDef |
| i2c | I2C_TypeDef | I2C1, I2C2, I2C3 | reviewed_subset | 9 | 60 | 9 | rcc, flash, pwr |  | header:I2C_TypeDef |
| ipsr | IPSR_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | cmsis_core:IPSR_Type |
| irqn | IRQn_Type |  | unmapped_type | 0 | 0 | 0 |  | No typed instances: helper type or additional instance mapping required | header:IRQn_Type |
| itm | ITM_Type | ITM | declarations_only | 18 | 13 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:ITM_Type |
| iwdg | IWDG_TypeDef | IWDG | reviewed_subset | 4 | 5 | 4 | rcc |  | header:IWDG_TypeDef |
| mpu | MPU_Type | MPU | declarations_only | 11 | 14 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:MPU_Type |
| nvic | NVIC_Type | NVIC | reviewed_subset | 7 | 7 | 7 | usart, tim, exti |  | cmsis_core:NVIC_Type |
| pwr | PWR_TypeDef | PWR | reviewed_subset | 2 | 16 | 2 | rcc |  | header:PWR_TypeDef |
| rcc | RCC_TypeDef | RCC | reviewed_subset | 23 | 244 | 8 |  |  | header:RCC_TypeDef |
| rng | RNG_TypeDef | RNG | reviewed_subset | 3 | 7 | 3 | rcc, flash, pwr |  | header:RNG_TypeDef |
| rtc | RTC_TypeDef | RTC | declarations_only | 39 | 142 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RTC_TypeDef |
| scb | SCB_Type | SCB | reviewed_subset | 20 | 56 | 3 |  | Configured field views: AIRCR, CCR, CFSR, CPUID, DFSR, HFSR, SCR, SHCSR; other overlapping mode encodings are not published | cmsis_core:SCB_Type |
| scnscb | SCnSCB_Type | SCnSCB | declarations_only | 2 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SCnSCB_Type |
| sdio | SDIO_TypeDef | SDIO | declarations_only | 18 | 98 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SDIO_TypeDef |
| spi | SPI_TypeDef | I2S2ext, I2S3ext, SPI1, SPI2, SPI3 | reviewed_subset | 9 | 45 | 9 | rcc, gpio |  | header:SPI_TypeDef |
| syscfg | SYSCFG_TypeDef | SYSCFG | reviewed_subset | 7 | 20 | 4 | gpio |  | header:SYSCFG_TypeDef |
| systick | SysTick_Type | SysTick | reviewed_subset | 4 | 9 | 4 | rcc, scb |  | cmsis_core:SysTick_Type |
| tim | TIM_TypeDef | TIM1, TIM10, TIM11, TIM12, TIM13, TIM14, TIM2, TIM3, TIM4, TIM5, TIM6, TIM7, TIM8, TIM9 | reviewed_subset | 21 | 127 | 15 | rcc | Alternative field views preserve separate declared interpretations; they do not establish instance applicability or reviewed operating modes | header:TIM_TypeDef |
| tpi | TPI_Type | TPI | partial_declarations | 17 | 32 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted.; DEVTYPE: bit fields withheld: DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree | cmsis_core:TPI_Type |
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

| Workflow | Ready | Required | Dependency closure | Missing evidence | Required mode order | Exact instances per mode |
| --- | --- | --- | --- | --- | --- | --- |
| adc1_internal_reference | True | True | adc, adc_common, flash, pwr, rcc, tim |  | rcc/adc_timer_gates → flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → adc_common/internal_reference_prescale4 → adc/single_conversion → tim/polling_update_delay |  |
| arm_flash_vector_table | True | True | rcc, scb, systick |  | systick/quiescent_owned → scb/flash_vector_table |  |
| arm_hsi16_core_checked | True | True | rcc |  |  |  |
| can1_external_bus | False | False | can, exti, flash, gpio, nvic, pwr, rcc, syscfg, tim, usart | CAN1_TX: board connectivity not published; CAN_TRANSCEIVER: board connectivity not published; can.normal_bus: operating mode not reviewed; flash: specify workflow register requirements before claiming readiness; pwr: specify workflow register requirements before claiming readiness |  |  |
| can1_rx_guarded_loopback_irq | True | True | can, exti, flash, gpio, nvic, pwr, rcc, syscfg, tim, usart |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/can1_rx_gpio_gate → gpio/can1_rx_pd0 → rcc/can1_gate_reset → can/silent_loopback → nvic/can1_rx0_prepare → can/silent_loopback_fifo0_irq |  |
| can1_silent_loopback | True | False | can, exti, flash, gpio, nvic, pwr, rcc, syscfg, tim, usart |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/can1_rx_gpio_gate → gpio/can1_rx_pd0 → rcc/can1_gate_reset → can/silent_loopback |  |
| can1_silent_loopback_irq | True | True | can, exti, flash, gpio, nvic, pwr, rcc, syscfg, tim, usart |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/can1_rx_gpio_gate → gpio/can1_rx_pd0 → rcc/can1_gate_reset → can/silent_loopback → nvic/can1_rx0_prepare → can/silent_loopback_fifo0_irq |  |
| crc_word_feed | True | True | crc, rcc |  |  |  |
| dac_channel1_software_trigger | True | True | dac, flash, gpio, pwr, rcc, tim |  | rcc/adc_timer_gates → flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/dac_gate_reset → tim/polling_update_delay → dac/channel1_software_trigger |  |
| dac_channel1_wired_output | False | False | dac, flash, gpio, pwr, rcc, tim | DAC1_OUT: board connectivity not published; DAC_REFERENCE: board connectivity not published | rcc/adc_timer_gates → flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/dac_gate_reset → tim/polling_update_delay → dac/channel1_software_trigger |  |
| dma2_memory_copy | True | True | dma, dma_stream, rcc |  |  |  |
| feature_adc | True | True | adc, adc_common, flash, pwr, rcc |  | rcc/adc_timer_gates → flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → adc_common/internal_reference_prescale4 → adc/single_conversion |  |
| feature_can | False | False | can, exti, flash, gpio, nvic, pwr, rcc, syscfg, tim, usart | can.normal_bus: operating mode not reviewed; flash: specify workflow register requirements before claiming readiness; pwr: specify workflow register requirements before claiming readiness |  |  |
| feature_dac | False | False | dac, flash, gpio, pwr, rcc, tim | dac.single_output: operating mode not reviewed; flash: specify workflow register requirements before claiming readiness; pwr: specify workflow register requirements before claiming readiness |  |  |
| feature_eth | False | False | eth, rcc | eth.DMAOMR: access/operating semantics unreviewed; eth.MACCR: access/operating semantics unreviewed; eth.ethernet: operating mode not reviewed; eth: operating semantics not reviewed |  |  |
| feature_flash | False | False | flash, rcc | flash.CR: access/operating semantics unreviewed; flash.KEYR: access/operating semantics unreviewed; flash.SR: access/operating semantics unreviewed; flash.program_erase: operating mode not reviewed |  |  |
| feature_fsmc_bank1 | False | False | fsmc_bank1, rcc | fsmc_bank1.BTCR: access/operating semantics unreviewed; fsmc_bank1.external_memory: operating mode not reviewed; fsmc_bank1: operating semantics not reviewed |  |  |
| feature_i2c | False | False | flash, i2c, pwr, rcc | flash: specify workflow register requirements before claiming readiness; i2c.master_polling: operating mode not reviewed; pwr: specify workflow register requirements before claiming readiness |  |  |
| feature_pwr | True | True | pwr, rcc |  | rcc/power_interface_gate → pwr/voltage_scale |  |
| feature_rtc | False | False | rcc, rtc | rtc.CR: access/operating semantics unreviewed; rtc.DR: access/operating semantics unreviewed; rtc.ISR: access/operating semantics unreviewed; rtc.PRER: access/operating semantics unreviewed; rtc.TR: access/operating semantics unreviewed; rtc.calendar: operating mode not reviewed; rtc: operating semantics not reviewed |  |  |
| feature_sdio | False | False | rcc, sdio | sdio.ARG: access/operating semantics unreviewed; sdio.CLKCR: access/operating semantics unreviewed; sdio.CMD: access/operating semantics unreviewed; sdio.POWER: access/operating semantics unreviewed; sdio.STA: access/operating semantics unreviewed; sdio.card_transfer: operating mode not reviewed; sdio: operating semantics not reviewed |  |  |
| feature_usb_otg_global | False | False | rcc, usb_otg_global | usb_otg_global.GAHBCFG: access/operating semantics unreviewed; usb_otg_global.GUSBCFG: access/operating semantics unreviewed; usb_otg_global.usb_device: operating mode not reviewed; usb_otg_global: operating semantics not reviewed |  |  |
| flash_latency_168mhz | True | True | flash, rcc |  |  |  |
| gpio_led_button | True | True | gpio, rcc |  |  |  |
| i2c1_controller_transmit | True | True | flash, i2c, pwr, rcc |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/i2c1_gate_reset → i2c/controller_transmit_polling |  |
| i2c1_wired_transmit | False | False | flash, i2c, pwr, rcc | I2C1_SCL: board connectivity not published; I2C1_SDA: board connectivity not published | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rcc/i2c1_gate_reset → i2c/controller_transmit_polling |  |
| iwdg_configure_refresh | True | False | iwdg, rcc |  |  |  |
| pll_hse8_168mhz | True | True | flash, pwr, rcc |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz |  |
| rng_pll_polling | True | True | flash, pwr, rcc, rng |  | flash/latency_168mhz → rcc/power_interface_gate → pwr/voltage_scale → rcc/pll_hse8_168mhz → rng/pll_polling |  |
| spi1_wired_polling | False | False | gpio, rcc, spi | SPI1_MISO: board connectivity not published; SPI1_MOSI: board connectivity not published; SPI1_SCK: board connectivity not published |  |  |
| systick_1khz_interrupt | True | True | rcc, scb, systick |  | rcc/hsi16_core_checked → systick/quiescent_owned → scb/flash_vector_table → scb/systick_exception_setup → systick/core_clock_interrupt |  |
| systick_core_polling | True | True | rcc, scb, systick |  | rcc/hsi16_core_checked → systick/core_clock_polling |  |
| tim2_capture_ch1_external | False | False | gpio, rcc, tim | TIM2_CH1_EXTERNAL: board connectivity not published; tim.capture_ch1_external: operating mode not reviewed |  |  |
| tim2_pwm_ch1_pin | False | False | gpio, rcc, tim | TIM2_CH1_EXTERNAL: board connectivity not published; tim.pwm_ch1_pin: operating mode not reviewed |  |  |
| tim2_pwm_ch1_reference | True | True | rcc, tim |  | rcc/hsi16_core_checked → rcc/tim2_owned_gate_reset → tim/pwm_ch1_reference |  |
| tim2_software_capture_ch1 | True | True | rcc, tim |  | rcc/hsi16_core_checked → rcc/tim2_owned_gate_reset → tim/software_capture_ch1 |  |
| tim2_tim5_pwm_capture_loopback | True | True | gpio, rcc, tim |  | rcc/hsi16_core_checked → rcc/timer_pair_gates → gpio/pa1_tim2_ch2_pa2_tim5_ch3 → tim/capture_ch3_pa2 → tim/pwm_ch2_pa1 | tim/capture_ch3_pa2: TIM5; tim/pwm_ch2_pa1: TIM2 |
| uart_timer_interrupts | True | True | exti, gpio, nvic, rcc, syscfg, tim, usart |  |  |  |

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
| adc | single_conversion | ADC1 |
| adc_common | internal_reference_prescale4 | ADC123_COMMON |
| can | silent_loopback | CAN1 |
| can | silent_loopback_fifo0_irq | CAN1 |
| crc | word_feed | CRC |
| dac | channel1_software_trigger | DAC, DAC1 |
| dma | poll_status_clear | DMA1, DMA2 |
| dma_stream | memory_copy_polling | DMA2_Stream0, DMA2_Stream1, DMA2_Stream2, DMA2_Stream3, DMA2_Stream4, DMA2_Stream5, DMA2_Stream6, DMA2_Stream7 |
| flash | latency_168mhz | FLASH |
| gpio | can1_rx_pd0 | GPIOD |
| gpio | pa1_tim2_ch2_pa2_tim5_ch3 | GPIOA |
| i2c | controller_transmit_polling | I2C1 |
| iwdg | configure_refresh | IWDG |
| nvic | can1_rx0_prepare | NVIC |
| pwr | voltage_scale | PWR |
| rcc | adc_timer_gates | RCC |
| rcc | can1_gate_reset | RCC |
| rcc | can1_rx_gpio_gate | RCC |
| rcc | dac_gate_reset | RCC |
| rcc | hsi16_core_checked | RCC |
| rcc | i2c1_gate_reset | RCC |
| rcc | peripheral_clock_gates | RCC |
| rcc | pll_hse8_168mhz | RCC |
| rcc | power_interface_gate | RCC |
| rcc | tim2_owned_gate_reset | RCC |
| rcc | timer_pair_gates | RCC |
| rng | pll_polling | RNG |
| rng | polling_health_checks | RNG |
| scb | flash_vector_table | SCB |
| scb | systick_exception_setup | SCB |
| spi | master_full_duplex_polling | SPI1, SPI2, SPI3 |
| systick | core_clock_interrupt | SysTick |
| systick | core_clock_polling | SysTick |
| systick | quiescent_owned | SysTick |
| tim | capture_ch3_pa2 | TIM5 |
| tim | polling_update_delay | TIM2 |
| tim | pwm_ch1_reference | TIM2 |
| tim | pwm_ch2_pa1 | TIM2 |
| tim | software_capture_ch1 | TIM2 |

## Board-specific workflow

Model: STM32F407G-DISC1; reference revision: MB997-E-01. Applicability: Reference E-01 circuit only. User confirmed the board model but not the PCB revision. Verify MB997 revision and SB20 before flashing; no equivalence to other revisions is asserted.

Signals: LED_A, LD4, GREEN_USER_LED, LED_B, LD3, ORANGE_USER_LED, RED_LED, LD5, RED_USER_LED, BLUE_LED, LD6, BLUE_USER_LED, USER_BUTTON, B1. Query a signal to retrieve its reviewed board context and separate circuit nets.

Retrieve each requested signal, then its peripheral dependency closure. Use reviewed workflow contracts to determine whether interrupt or core setup is required.

See [[schemas/board]] and [[schemas/components]].

Metadata and clock assumptions: `profile:target`. These are declared operating assumptions, not measurements. All register declarations are retained; unknown access/reset/encoding facts remain explicitly unasserted and must not be used to generate unsupported operations.

Publication policy: `compilation_policy:publication_policy`; its exact input hash and review scope are recorded in [[sources]]. See [[policy]] for the complete declarative contract. Requirements constrain publication; they do not manufacture missing hardware facts.
