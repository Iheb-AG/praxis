# Coverage report

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

## Machine-readable report

```json
{
  "counts": {
    "blocked": 3,
    "fields": 1991,
    "published": 39,
    "register_blocks": 42,
    "registers": 496,
    "reviewed_subsets": 4,
    "unmapped_types": 11
  },
  "format": "praxis-coverage-v1",
  "limits": [
    "Reviewed subsets do not establish support for every mode or instance.",
    "Unreviewed declarations must not be used as initialization guidance.",
    "Header absence does not prove that silicon lacks a capability.",
    "Package availability, routing, timing and physical tests remain separate evidence."
  ],
  "peripherals": {
    "adc": {
      "bytes_limit": 65536,
      "fields": 85,
      "instances": [
        "ADC1",
        "ADC2",
        "ADC3"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:ADC_TypeDef",
      "published": true,
      "registers": 20,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "ADC_TypeDef"
    },
    "adc_common": {
      "bytes_limit": 65536,
      "fields": 27,
      "instances": [
        "ADC123_COMMON"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:ADC_Common_TypeDef",
      "published": true,
      "registers": 3,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "ADC_Common_TypeDef"
    },
    "apsr": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "cmsis_core:APSR_Type",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "APSR_Type"
    },
    "can": {
      "bytes_limit": 65536,
      "fields": 77,
      "instances": [
        "CAN1",
        "CAN2"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:CAN_TypeDef",
      "published": true,
      "registers": 89,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "CAN_TypeDef"
    },
    "can_fifomailbox": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:CAN_FIFOMailBox_TypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "CAN_FIFOMailBox_TypeDef"
    },
    "can_filterregister": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:CAN_FilterRegister_TypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "CAN_FilterRegister_TypeDef"
    },
    "can_txmailbox": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:CAN_TxMailBox_TypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "CAN_TxMailBox_TypeDef"
    },
    "control": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "cmsis_core:CONTROL_Type",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "CONTROL_Type"
    },
    "coredebug": {
      "bytes_limit": 65536,
      "fields": 21,
      "instances": [
        "CoreDebug"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [],
      "provenance": "cmsis_core:CoreDebug_Type",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "CoreDebug_Type"
    },
    "crc": {
      "bytes_limit": 65536,
      "fields": 3,
      "instances": [
        "CRC"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:CRC_TypeDef",
      "published": true,
      "registers": 3,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "CRC_TypeDef"
    },
    "dac": {
      "bytes_limit": 65536,
      "fields": 34,
      "instances": [
        "DAC",
        "DAC1"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:DAC_TypeDef",
      "published": true,
      "registers": 14,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DAC_TypeDef"
    },
    "dbgmcu": {
      "bytes_limit": 65536,
      "fields": 7,
      "instances": [
        "DBGMCU"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:DBGMCU_TypeDef",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DBGMCU_TypeDef"
    },
    "dcmi": {
      "bytes_limit": 65536,
      "fields": 35,
      "instances": [
        "DCMI"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:DCMI_TypeDef",
      "published": true,
      "registers": 11,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DCMI_TypeDef"
    },
    "dma": {
      "bytes_limit": 65536,
      "fields": 80,
      "instances": [
        "DMA1",
        "DMA2"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:DMA_TypeDef",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DMA_TypeDef"
    },
    "dma_stream": {
      "bytes_limit": 65536,
      "fields": 27,
      "instances": [
        "DMA1_Stream0",
        "DMA1_Stream1",
        "DMA1_Stream2",
        "DMA1_Stream3",
        "DMA1_Stream4",
        "DMA1_Stream5",
        "DMA1_Stream6",
        "DMA1_Stream7",
        "DMA2_Stream0",
        "DMA2_Stream1",
        "DMA2_Stream2",
        "DMA2_Stream3",
        "DMA2_Stream4",
        "DMA2_Stream5",
        "DMA2_Stream6",
        "DMA2_Stream7"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "dma"
      ],
      "provenance": "header:DMA_Stream_TypeDef",
      "published": true,
      "registers": 6,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DMA_Stream_TypeDef"
    },
    "dwt": {
      "bytes_limit": 65536,
      "fields": 23,
      "instances": [
        "DWT"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "cmsis_core:DWT_Type",
      "published": true,
      "registers": 20,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "DWT_Type"
    },
    "eth": {
      "bytes_limit": 65536,
      "fields": 212,
      "instances": [
        "ETH"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:ETH_TypeDef",
      "published": true,
      "registers": 56,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "ETH_TypeDef"
    },
    "exti": {
      "bytes_limit": 65536,
      "fields": 116,
      "instances": [
        "EXTI"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "syscfg"
      ],
      "provenance": "header:EXTI_TypeDef",
      "published": true,
      "registers": 6,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "EXTI_TypeDef"
    },
    "flash": {
      "fields": 0,
      "instances": [
        "FLASH"
      ],
      "issues": [
        "UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field"
      ],
      "provenance": "header:FLASH_TypeDef",
      "published": false,
      "registers": 0,
      "selected": true,
      "status": "blocked",
      "structure": "FLASH_TypeDef"
    },
    "fpu": {
      "bytes_limit": 65536,
      "fields": 27,
      "instances": [
        "FPU"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "cmsis_core:FPU_Type",
      "published": true,
      "registers": 6,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "FPU_Type"
    },
    "fsmc_bank1": {
      "bytes_limit": 65536,
      "fields": 0,
      "instances": [
        "FSMC_Bank1"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:FSMC_Bank1_TypeDef",
      "published": true,
      "registers": 1,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "FSMC_Bank1_TypeDef"
    },
    "fsmc_bank1e": {
      "bytes_limit": 65536,
      "fields": 0,
      "instances": [
        "FSMC_Bank1E"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:FSMC_Bank1E_TypeDef",
      "published": true,
      "registers": 1,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "FSMC_Bank1E_TypeDef"
    },
    "fsmc_bank2_3": {
      "bytes_limit": 65536,
      "fields": 0,
      "instances": [
        "FSMC_Bank2_3"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:FSMC_Bank2_3_TypeDef",
      "published": true,
      "registers": 10,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "FSMC_Bank2_3_TypeDef"
    },
    "fsmc_bank4": {
      "bytes_limit": 65536,
      "fields": 0,
      "instances": [
        "FSMC_Bank4"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:FSMC_Bank4_TypeDef",
      "published": true,
      "registers": 5,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "FSMC_Bank4_TypeDef"
    },
    "gpio": {
      "bytes_limit": 65536,
      "fields": 161,
      "instances": [
        "GPIOA",
        "GPIOB",
        "GPIOC",
        "GPIOD",
        "GPIOE",
        "GPIOF",
        "GPIOG",
        "GPIOH",
        "GPIOI"
      ],
      "issues": [],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:GPIO_TypeDef",
      "published": true,
      "registers": 10,
      "reviewed_registers": 10,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "GPIO_TypeDef"
    },
    "i2c": {
      "bytes_limit": 65536,
      "fields": 60,
      "instances": [
        "I2C1",
        "I2C2",
        "I2C3"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:I2C_TypeDef",
      "published": true,
      "registers": 9,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "I2C_TypeDef"
    },
    "ipsr": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "cmsis_core:IPSR_Type",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "IPSR_Type"
    },
    "irqn": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "cmsis_core:IRQn_Type",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "IRQn_Type"
    },
    "itm": {
      "fields": 0,
      "instances": [
        "ITM"
      ],
      "issues": [
        "UNSUPPORTED_DECLARATION: UNSUPPORTED_DECLARATION: Unsupported nested member: PORT"
      ],
      "provenance": "cmsis_core:ITM_Type",
      "published": false,
      "registers": 0,
      "selected": true,
      "status": "blocked",
      "structure": "ITM_Type"
    },
    "iwdg": {
      "bytes_limit": 65536,
      "fields": 5,
      "instances": [
        "IWDG"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:IWDG_TypeDef",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "IWDG_TypeDef"
    },
    "mpu": {
      "bytes_limit": 65536,
      "fields": 14,
      "instances": [
        "MPU"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "cmsis_core:MPU_Type",
      "published": true,
      "registers": 11,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "MPU_Type"
    },
    "nvic": {
      "bytes_limit": 65536,
      "fields": 7,
      "instances": [
        "NVIC"
      ],
      "issues": [],
      "prerequisites": [
        "usart"
      ],
      "provenance": "cmsis_core:NVIC_Type",
      "published": true,
      "registers": 7,
      "reviewed_registers": 7,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "NVIC_Type"
    },
    "pwr": {
      "bytes_limit": 65536,
      "fields": 16,
      "instances": [
        "PWR"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:PWR_TypeDef",
      "published": true,
      "registers": 2,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "PWR_TypeDef"
    },
    "rcc": {
      "bytes_limit": 65536,
      "fields": 244,
      "instances": [
        "RCC"
      ],
      "issues": [],
      "prerequisites": [],
      "provenance": "header:RCC_TypeDef",
      "published": true,
      "registers": 23,
      "reviewed_registers": 6,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "RCC_TypeDef"
    },
    "rng": {
      "bytes_limit": 65536,
      "fields": 7,
      "instances": [
        "RNG"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:RNG_TypeDef",
      "published": true,
      "registers": 3,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "RNG_TypeDef"
    },
    "rtc": {
      "bytes_limit": 65536,
      "fields": 142,
      "instances": [
        "RTC"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:RTC_TypeDef",
      "published": true,
      "registers": 39,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "RTC_TypeDef"
    },
    "scb": {
      "bytes_limit": 65536,
      "fields": 56,
      "instances": [
        "SCB"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [],
      "provenance": "cmsis_core:SCB_Type",
      "published": true,
      "registers": 20,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SCB_Type"
    },
    "scnscb": {
      "bytes_limit": 65536,
      "fields": 0,
      "instances": [
        "SCnSCB"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "cmsis_core:SCnSCB_Type",
      "published": true,
      "registers": 2,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SCnSCB_Type"
    },
    "sdio": {
      "bytes_limit": 65536,
      "fields": 98,
      "instances": [
        "SDIO"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:SDIO_TypeDef",
      "published": true,
      "registers": 18,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SDIO_TypeDef"
    },
    "spi": {
      "bytes_limit": 65536,
      "fields": 45,
      "instances": [
        "I2S2ext",
        "I2S3ext",
        "SPI1",
        "SPI2",
        "SPI3"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:SPI_TypeDef",
      "published": true,
      "registers": 9,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SPI_TypeDef"
    },
    "syscfg": {
      "bytes_limit": 65536,
      "fields": 4,
      "instances": [
        "SYSCFG"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "gpio"
      ],
      "provenance": "header:SYSCFG_TypeDef",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SYSCFG_TypeDef"
    },
    "systick": {
      "bytes_limit": 65536,
      "fields": 9,
      "instances": [
        "SysTick"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [],
      "provenance": "cmsis_core:SysTick_Type",
      "published": true,
      "registers": 4,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "SysTick_Type"
    },
    "tim": {
      "bytes_limit": 65536,
      "fields": 111,
      "instances": [
        "TIM1",
        "TIM10",
        "TIM11",
        "TIM12",
        "TIM13",
        "TIM14",
        "TIM2",
        "TIM3",
        "TIM4",
        "TIM5",
        "TIM6",
        "TIM7",
        "TIM8",
        "TIM9"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:TIM_TypeDef",
      "published": true,
      "registers": 21,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "TIM_TypeDef"
    },
    "tpi": {
      "fields": 0,
      "instances": [
        "TPI"
      ],
      "issues": [
        "DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree"
      ],
      "provenance": "cmsis_core:TPI_Type",
      "published": false,
      "registers": 0,
      "selected": true,
      "status": "blocked",
      "structure": "TPI_Type"
    },
    "usart": {
      "bytes_limit": 65536,
      "fields": 51,
      "instances": [
        "UART4",
        "UART5",
        "USART1",
        "USART2",
        "USART3",
        "USART6"
      ],
      "issues": [],
      "prerequisites": [
        "gpio"
      ],
      "provenance": "header:USART_TypeDef",
      "published": true,
      "registers": 7,
      "reviewed_registers": 7,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "USART_TypeDef"
    },
    "usb_otg_device": {
      "bytes_limit": 65536,
      "fields": 56,
      "instances": [
        "USB_OTG_FS_DEVICE",
        "USB_OTG_HS_DEVICE"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:USB_OTG_DeviceTypeDef",
      "published": true,
      "registers": 15,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "USB_OTG_DeviceTypeDef"
    },
    "usb_otg_global": {
      "bytes_limit": 65536,
      "fields": 115,
      "instances": [
        "USB_OTG_FS",
        "USB_OTG_FS_GLOBAL",
        "USB_OTG_HS",
        "USB_OTG_HS_GLOBAL"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:USB_OTG_GlobalTypeDef",
      "published": true,
      "registers": 16,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "USB_OTG_GlobalTypeDef"
    },
    "usb_otg_host": {
      "bytes_limit": 65536,
      "fields": 10,
      "instances": [
        "USB_OTG_FS_HOST",
        "USB_OTG_HS_HOST"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:USB_OTG_HostTypeDef",
      "published": true,
      "registers": 6,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "USB_OTG_HostTypeDef"
    },
    "usb_otg_hostchannel": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:USB_OTG_HostChannelTypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "USB_OTG_HostChannelTypeDef"
    },
    "usb_otg_inendpoint": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:USB_OTG_INEndpointTypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "USB_OTG_INEndpointTypeDef"
    },
    "usb_otg_outendpoint": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "header:USB_OTG_OUTEndpointTypeDef",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "USB_OTG_OUTEndpointTypeDef"
    },
    "wwdg": {
      "bytes_limit": 65536,
      "fields": 6,
      "instances": [
        "WWDG"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted."
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:WWDG_TypeDef",
      "published": true,
      "registers": 3,
      "reviewed_registers": 0,
      "selected": true,
      "status": "declarations_only",
      "structure": "WWDG_TypeDef"
    },
    "xpsr": {
      "fields": 0,
      "instances": [],
      "issues": [
        "No typed instances: helper type or additional instance mapping required"
      ],
      "provenance": "cmsis_core:xPSR_Type",
      "published": false,
      "registers": 0,
      "selected": false,
      "status": "unmapped_type",
      "structure": "xPSR_Type"
    }
  },
  "publication_ready": true,
  "scope": "CMSIS typed register blocks; not every MCU capability or board connection",
  "target": "stm32f407g_disc1_mb997_e01",
  "workflows": {
    "gpio_led_button": {
      "closure": [
        "gpio",
        "rcc"
      ],
      "issues": [],
      "ready": true,
      "required_for_publication": true
    },
    "uart_timer_interrupts": {
      "closure": [
        "exti",
        "gpio",
        "nvic",
        "rcc",
        "syscfg",
        "tim",
        "usart"
      ],
      "issues": [
        "exti: operating semantics not reviewed",
        "syscfg: operating semantics not reviewed",
        "tim.ARR: access/operating semantics unreviewed",
        "tim.CR1: access/operating semantics unreviewed",
        "tim.DIER: access/operating semantics unreviewed",
        "tim.PSC: access/operating semantics unreviewed",
        "tim.SR: access/operating semantics unreviewed",
        "tim: operating semantics not reviewed"
      ],
      "ready": false,
      "required_for_publication": false
    }
  }
}
```
