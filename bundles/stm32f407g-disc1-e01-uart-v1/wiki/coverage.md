# Coverage report

## Peripheral coverage

CMSIS register types and configured instances; not every MCU capability or board connection. Dependencies are profile retrieval policy, not a proven hardware initialization sequence. `reviewed_subset` covers only the facts explicitly reviewed. `declarations_only` supplies layouts and masks, never operating guidance.

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
| exti | EXTI_TypeDef | EXTI | reviewed_subset | 6 | 138 | 6 | syscfg | Configured field views: EMR, IMR; other overlapping mode encodings are not published | header:EXTI_TypeDef |
| flash | FLASH_TypeDef | FLASH | partial_declarations | 7 | 25 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted.; ACR: bit fields withheld: UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field | header:FLASH_TypeDef |
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
| nvic | NVIC_Type | NVIC | reviewed_subset | 7 | 7 | 7 | usart, tim, exti |  | cmsis_core:NVIC_Type |
| pwr | PWR_TypeDef | PWR | declarations_only | 2 | 16 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:PWR_TypeDef |
| rcc | RCC_TypeDef | RCC | reviewed_subset | 23 | 244 | 7 |  |  | header:RCC_TypeDef |
| rng | RNG_TypeDef | RNG | declarations_only | 3 | 7 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RNG_TypeDef |
| rtc | RTC_TypeDef | RTC | declarations_only | 39 | 142 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:RTC_TypeDef |
| scb | SCB_Type | SCB | declarations_only | 20 | 56 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SCB_Type |
| scnscb | SCnSCB_Type | SCnSCB | declarations_only | 2 | 0 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SCnSCB_Type |
| sdio | SDIO_TypeDef | SDIO | declarations_only | 18 | 98 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SDIO_TypeDef |
| spi | SPI_TypeDef | I2S2ext, I2S3ext, SPI1, SPI2, SPI3 | declarations_only | 9 | 45 | 0 | rcc | Enclosing masks represent contained aliases; absent masks remain unasserted. | header:SPI_TypeDef |
| syscfg | SYSCFG_TypeDef | SYSCFG | reviewed_subset | 7 | 20 | 4 | gpio |  | header:SYSCFG_TypeDef |
| systick | SysTick_Type | SysTick | declarations_only | 4 | 9 | 0 |  | Enclosing masks represent contained aliases; absent masks remain unasserted. | cmsis_core:SysTick_Type |
| tim | TIM_TypeDef | TIM1, TIM10, TIM11, TIM12, TIM13, TIM14, TIM2, TIM3, TIM4, TIM5, TIM6, TIM7, TIM8, TIM9 | reviewed_subset | 21 | 119 | 7 | rcc | Configured field views: CCMR1, CCMR2; other overlapping mode encodings are not published | header:TIM_TypeDef |
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

| Workflow | Ready | Required | Dependency closure | Missing evidence |
| --- | --- | --- | --- | --- |
| gpio_led_button | True | True | gpio, rcc |  |
| uart_timer_interrupts | True | True | exti, gpio, nvic, rcc, syscfg, tim, usart |  |

- Reviewed subsets do not establish support for every mode or instance.
- Unreviewed declarations must not be used as initialization guidance.
- Header absence does not prove that silicon lacks a capability.
- Package availability, routing, timing and physical tests remain separate evidence.

## Machine-readable report

```json
{
  "counts": {
    "blocked": 1,
    "fields": 2094,
    "published": 41,
    "register_blocks": 42,
    "registers": 523,
    "reviewed_subsets": 7,
    "unmapped_types": 11
  },
  "extractor_versions": {
    "arm-none-eabi-gcc": "arm-none-eabi-gcc (Arch Repository) 16.2.0",
    "clang": "clang version 23.1.1",
    "cmsis-discovery": "v1; Clang layouts and restricted object-macro evaluation",
    "libclang": "18.1.1",
    "netlist": "Reviewed PDF transcription adapter v1; no geometry inference",
    "praxis": "0.1.0"
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
      "structure": "ADC_TypeDef",
      "unresolved_masks": []
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
      "structure": "ADC_Common_TypeDef",
      "unresolved_masks": []
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
      "structure": "CAN_TypeDef",
      "unresolved_masks": []
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
      "structure": "CoreDebug_Type",
      "unresolved_masks": []
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
      "structure": "CRC_TypeDef",
      "unresolved_masks": []
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
      "structure": "DAC_TypeDef",
      "unresolved_masks": []
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
      "structure": "DBGMCU_TypeDef",
      "unresolved_masks": []
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
      "structure": "DCMI_TypeDef",
      "unresolved_masks": []
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
      "structure": "DMA_TypeDef",
      "unresolved_masks": []
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
      "structure": "DMA_Stream_TypeDef",
      "unresolved_masks": []
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
      "structure": "DWT_Type",
      "unresolved_masks": []
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
      "structure": "ETH_TypeDef",
      "unresolved_masks": []
    },
    "exti": {
      "bytes_limit": 65536,
      "fields": 138,
      "instances": [
        "EXTI"
      ],
      "issues": [
        "Configured field views: EMR, IMR; other overlapping mode encodings are not published"
      ],
      "prerequisites": [
        "syscfg"
      ],
      "provenance": "header:EXTI_TypeDef",
      "published": true,
      "registers": 6,
      "reviewed_registers": 6,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "EXTI_TypeDef",
      "unresolved_masks": []
    },
    "flash": {
      "bytes_limit": 65536,
      "fields": 25,
      "instances": [
        "FLASH"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted.",
        "ACR: bit fields withheld: UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field"
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:FLASH_TypeDef",
      "published": true,
      "registers": 7,
      "reviewed_registers": 0,
      "selected": true,
      "status": "partial_declarations",
      "structure": "FLASH_TypeDef",
      "unresolved_masks": [
        "ACR: bit fields withheld: UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field"
      ]
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
      "structure": "FPU_Type",
      "unresolved_masks": []
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
      "structure": "FSMC_Bank1_TypeDef",
      "unresolved_masks": []
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
      "structure": "FSMC_Bank1E_TypeDef",
      "unresolved_masks": []
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
      "structure": "FSMC_Bank2_3_TypeDef",
      "unresolved_masks": []
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
      "structure": "FSMC_Bank4_TypeDef",
      "unresolved_masks": []
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
      "structure": "GPIO_TypeDef",
      "unresolved_masks": []
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
      "structure": "I2C_TypeDef",
      "unresolved_masks": []
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
      "structure": "IWDG_TypeDef",
      "unresolved_masks": []
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
      "structure": "MPU_Type",
      "unresolved_masks": []
    },
    "nvic": {
      "bytes_limit": 65536,
      "fields": 7,
      "instances": [
        "NVIC"
      ],
      "issues": [],
      "prerequisites": [
        "usart",
        "tim",
        "exti"
      ],
      "provenance": "cmsis_core:NVIC_Type",
      "published": true,
      "registers": 7,
      "reviewed_registers": 7,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "NVIC_Type",
      "unresolved_masks": []
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
      "structure": "PWR_TypeDef",
      "unresolved_masks": []
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
      "reviewed_registers": 7,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "RCC_TypeDef",
      "unresolved_masks": []
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
      "structure": "RNG_TypeDef",
      "unresolved_masks": []
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
      "structure": "RTC_TypeDef",
      "unresolved_masks": []
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
      "structure": "SCB_Type",
      "unresolved_masks": []
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
      "structure": "SCnSCB_Type",
      "unresolved_masks": []
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
      "structure": "SDIO_TypeDef",
      "unresolved_masks": []
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
      "structure": "SPI_TypeDef",
      "unresolved_masks": []
    },
    "syscfg": {
      "bytes_limit": 65536,
      "fields": 20,
      "instances": [
        "SYSCFG"
      ],
      "issues": [],
      "prerequisites": [
        "gpio"
      ],
      "provenance": "header:SYSCFG_TypeDef",
      "published": true,
      "registers": 7,
      "reviewed_registers": 4,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "SYSCFG_TypeDef",
      "unresolved_masks": []
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
      "structure": "SysTick_Type",
      "unresolved_masks": []
    },
    "tim": {
      "bytes_limit": 65536,
      "fields": 119,
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
        "Configured field views: CCMR1, CCMR2; other overlapping mode encodings are not published"
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "header:TIM_TypeDef",
      "published": true,
      "registers": 21,
      "reviewed_registers": 7,
      "selected": true,
      "status": "reviewed_subset",
      "structure": "TIM_TypeDef",
      "unresolved_masks": []
    },
    "tpi": {
      "bytes_limit": 65536,
      "fields": 32,
      "instances": [
        "TPI"
      ],
      "issues": [
        "Enclosing masks represent contained aliases; absent masks remain unasserted.",
        "DEVTYPE: bit fields withheld: DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree"
      ],
      "prerequisites": [
        "rcc"
      ],
      "provenance": "cmsis_core:TPI_Type",
      "published": true,
      "registers": 17,
      "reviewed_registers": 0,
      "selected": true,
      "status": "partial_declarations",
      "structure": "TPI_Type",
      "unresolved_masks": [
        "DEVTYPE: bit fields withheld: DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree"
      ]
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
      "structure": "USART_TypeDef",
      "unresolved_masks": []
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
      "structure": "USB_OTG_DeviceTypeDef",
      "unresolved_masks": []
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
      "structure": "USB_OTG_GlobalTypeDef",
      "unresolved_masks": []
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
      "structure": "USB_OTG_HostTypeDef",
      "unresolved_masks": []
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
      "structure": "WWDG_TypeDef",
      "unresolved_masks": []
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
  "scope": "CMSIS register types and configured instances; not every MCU capability or board connection",
  "sources": {
    "board": {
      "sha256": "6a9cfe8c355ccf6b3f94cae999716ad6dc2b4d2f55e2860e81ef9a49dfb0ea4e",
      "version": "MB997-E-01 subset v1"
    },
    "board_manual": {
      "sha256": "9444efaa35b893134df31825580fbcafa01348cf1d7c85a85bae365a6f4280b6",
      "version": "UM1472 Rev 9"
    },
    "board_netlist": {
      "sha256": "53bef9ad2e341fe531f2d151bbfef3391192f813677a9924ef6c935817af744c",
      "version": "MB997-E-01 subset v1"
    },
    "clock_review": {
      "sha256": "a7457a224958f949e69bbebf17abec2fabead2a6932a0cf8016fb342bfab6553",
      "version": "STM32CubeF4 v1.28.1"
    },
    "cmsis_core": {
      "sha256": "f5b63d52dd1557b15ca414cb59c264f595a7b5669db2a5878dffe22f4caedc8c",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "definitions": {
      "sha256": "8ab6616e039367946e6a39bb07a29053d4de3a3b04f105c2affda6fa5dbe9098",
      "version": "f407-fixture-1"
    },
    "exti_review": {
      "sha256": "4c450207f30ed487c07ce8998754135c6a09717145a981f5bbf63c6e012022d6",
      "version": "uart-scenario-1"
    },
    "gpio_review": {
      "sha256": "a280e74dd8268f123dd5d4a9ca68e5a2904ad06a9924a23e75f27308211cc16e",
      "version": "f407-fixture-1"
    },
    "header": {
      "sha256": "ae1ab57d8ab750f64f04fd73476bc2760c761e18e45bde648e0bc350c9a1d9ac",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "nvic_review": {
      "sha256": "96987eb48e54f7b2222117a533948302348f17e6e5a0f590f66a7431b9b9badf",
      "version": "f407-fixture-1"
    },
    "profile": {
      "sha256": "90bef88e691b0fe0efe9f22e45c3c5e23c89f581582e0f1df19e56592935cd8d",
      "version": "1"
    },
    "rcc_review": {
      "sha256": "11de8499c45ca9cbbbf2e44dadb6eac92afe83e495e320d9daae0eac854cc917",
      "version": "f407-fixture-1"
    },
    "rm_apb2_gate": {
      "sha256": "7cc7bf3d478ae58995e038840c66f8d862443082224390435bc187bde9a6ef47",
      "version": "RM0090 Rev22"
    },
    "rm_apb2_reset": {
      "sha256": "2ad6df88298b01f105c40c238eaebe5220c995b2b98e3f6b17ebf0ea1657178d",
      "version": "RM0090 Rev22"
    },
    "rm_clock": {
      "sha256": "7c971d840eb5cb8122a3e36cebe03556d1107562c8b5bf04c3c96c1277ea813a",
      "version": "RM0090 Rev22"
    },
    "rm_exti_edges": {
      "sha256": "3c42ee653ac9356c00a0ec6463c4afd7ade6ee670b5e315929f1af69f8c74cf5",
      "version": "RM0090 Rev22"
    },
    "rm_exti_mask": {
      "sha256": "985cd9d67a1e631873384aff2118171126449d2942911d164efa513081117a73",
      "version": "RM0090 Rev22"
    },
    "rm_exti_pending": {
      "sha256": "3b24ca38b00bcc0a9f2318c12cd869e6f29c1a9c86d348bd2c7c358d70795439",
      "version": "RM0090 Rev22"
    },
    "rm_gpio_speed": {
      "sha256": "c2a20d3e10ecf4b59815d3f67d18144633a323905738cdb7a3780a4b060ab25c",
      "version": "RM0090 Rev22"
    },
    "rm_hsi": {
      "sha256": "fc01b727c474b457fc29b109e8dae3de6adb3e49d9a99ebdd6b0dab16f4b04e8",
      "version": "RM0090 Rev22"
    },
    "rm_syscfg1": {
      "sha256": "2f777c1f659e6d3fb2c03840f59d27170897f9ae8cd1524d3e73974d65476807",
      "version": "RM0090 Rev22"
    },
    "rm_syscfg2": {
      "sha256": "3e4e0256d049fd12ad698f255141a0604174a9eb77b30a96f169307fb3692e7b",
      "version": "RM0090 Rev22"
    },
    "rm_syscfg3": {
      "sha256": "29be3ef7bbc980ad402c4aa6175e93446deb684a1495c7864540256bd6e5b9d4",
      "version": "RM0090 Rev22"
    },
    "rm_tim_arr": {
      "sha256": "5dc00b215b723c282d9a6029d8e96f36405cff1b8ee0e9a2346cc392ae51cf7d",
      "version": "RM0090 Rev22"
    },
    "rm_tim_control": {
      "sha256": "37d32e0a0d38b741dc4ecbfc752e56e3e2f5a76a3c6a2723e4109d43f977cd92",
      "version": "RM0090 Rev22"
    },
    "rm_tim_cr1": {
      "sha256": "0aa49dfc56131b2af8bc0b1e2107581cd7a766b28286f78cbe0b15d50d92d7eb",
      "version": "RM0090 Rev22"
    },
    "rm_tim_dier": {
      "sha256": "2a9bd44e140cafa227b2b488002d391f15b8db997d9f5e6df420b989912aef1b",
      "version": "RM0090 Rev22"
    },
    "rm_tim_egr": {
      "sha256": "b871f4981b9e69feb0cd9a728e31787c42e6cbdcbcce4c025db4e929f19244fc",
      "version": "RM0090 Rev22"
    },
    "rm_tim_sr": {
      "sha256": "6994ebfc114dab48aecafb188ef1ec72655398f2abc06b3b5e0f0b6a7bfb5ea7",
      "version": "RM0090 Rev22"
    },
    "rm_tim_status": {
      "sha256": "5a691da085255144af2d3975f4e800de7964733742d3250c2224b25332d3a14d",
      "version": "RM0090 Rev22"
    },
    "rm_tim_values": {
      "sha256": "464a8ff413acfbbadbcb71a4faef9b5400e704dd23e6d865c18f1870fca9cff6",
      "version": "RM0090 Rev22"
    },
    "rm_uart_baud": {
      "sha256": "b7a2ae78379f5654588c46a54768c698c83d49bab0f64babfb00fb96caf0a4fc",
      "version": "RM0090 Rev22"
    },
    "rm_uart_brr": {
      "sha256": "3759698af5feb911c1f7bc7c016751c4b5a13a42f1e4c450e5bcdf6703091261",
      "version": "RM0090 Rev22"
    },
    "rm_uart_cr1": {
      "sha256": "1934d5561fca3f1faa1fdc4f8709f4be931b04be774526fb29a3160044169690",
      "version": "RM0090 Rev22"
    },
    "rm_uart_cr3": {
      "sha256": "cd4d131ebf3f4cb399b8023aafb2cbd22ced60d8337b78ef276ae978b449ff9d",
      "version": "RM0090 Rev22"
    },
    "rm_uart_errors": {
      "sha256": "57fae8fcd0d65b45f77454f8d66d636e0aedcc1f378cd432fb7da0789cb5d947",
      "version": "RM0090 Rev22"
    },
    "rm_uart_irq": {
      "sha256": "ee35bdf85478859ef1fe388c63fc2f7d75f7eb8314462f85c781781de486e926",
      "version": "RM0090 Rev22"
    },
    "rm_uart_rx": {
      "sha256": "c84be24cf2dfda0202279ff9b0806a14bd125841970ed675af1a9d937a8a2c49",
      "version": "RM0090 Rev22"
    },
    "rm_uart_sr": {
      "sha256": "4ea76039c0a9ef2a5483e6592a163cceed855bf4cf484ebcb2a70b8b415c9b87",
      "version": "RM0090 Rev22"
    },
    "schematic_e01": {
      "sha256": "730be31b0809943920e0a4e635d2a5d40e9e8fcff9d4e0aea2587de8dcdfdd26",
      "version": "MB997-E-01 2020-04-09"
    },
    "schematic_mcu": {
      "sha256": "f2d38d551d7c48a039e1175d945efcb9d112639fdefe699ee1473fa1b1191641",
      "version": "MB997 E-01"
    },
    "schematic_uart": {
      "sha256": "f3fa9ba26d87ae8e68c8ed3467b56bc4f3b7539886e4d9bdbda93a3333014293",
      "version": "MB997 E-01"
    },
    "syscfg_review": {
      "sha256": "8cdbf264b821f9ce95cd0a4c8335d131f5296c4e72a2e53eae9de0e5980b8119",
      "version": "uart-scenario-1"
    },
    "tim_review": {
      "sha256": "e6fb909c88b2d846cf7b34de805166ca7dee87f5d14d1164d65f3f34ed5a999d",
      "version": "uart-scenario-1"
    },
    "uart_connector": {
      "sha256": "ccec888b7ed470a363c7d41a10d15d5d421064278dcbd5dcf0b3296d091a3424",
      "version": "UM1472 Rev9"
    },
    "uart_connector_table": {
      "sha256": "6cd2a4094c7458551fb0b6430b6342ada3d06480bbf510b6bd741745eeb78562",
      "version": "UM1472 Rev9"
    },
    "usart_review": {
      "sha256": "17f4158562f76b73799bf726a47c1a95c02e9daf3ff319d548c257bcb3d73dfa",
      "version": "f407-fixture-1"
    },
    "vendor_0": {
      "sha256": "b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_1": {
      "sha256": "dadb755f51d36614173b28c5790cb4a991e8f4cc822e5b634fd66a4f4145824d",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_2": {
      "sha256": "b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_3": {
      "sha256": "43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_4": {
      "sha256": "184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_6": {
      "sha256": "29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_7": {
      "sha256": "d942d06c396ff3f1dc9be5135ef1546f458c24702f027dca93afe60909872d91",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "vendor_9": {
      "sha256": "02c067d5a135f540c03215dc834b1e60a97bbd4e55bfd3994b0c82a15ea3012a",
      "version": "ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0"
    },
    "web_2dc587a15e007a69_record": {
      "sha256": "0a3a6be204f5a68fb824250c096bd645dc7fbfaf68ee40bc55282ecffbdc0fee",
      "version": "5df1bd175a17d667d2120eb5bbb0607c4d2e1e9d694dafb4e4fb8defbeae0780"
    },
    "web_2dc587a15e007a69_review": {
      "sha256": "0281bb81b8b9d7f0b7f414647cb455d8a754894addb4d3044d06758df2bf1232",
      "version": "5df1bd175a17d667d2120eb5bbb0607c4d2e1e9d694dafb4e4fb8defbeae0780"
    },
    "web_3c53cb6dfbd89b0d_record": {
      "sha256": "97daa42197e5a9f3ce6961550f6517257345dcfa8a80db4e47502e0e5be2102d",
      "version": "4851fddc08411f666380bff2a8dcbc8ad5886601a16daea2e40a2ac110af84f2"
    },
    "web_3c53cb6dfbd89b0d_review": {
      "sha256": "c655ae23a964abb3542ee0064bdf8188cd19c5243f20ca630ed1fa6eb2b31e4d",
      "version": "4851fddc08411f666380bff2a8dcbc8ad5886601a16daea2e40a2ac110af84f2"
    },
    "web_ae28c6908f2bceed_record": {
      "sha256": "fc8ca7deefa0714177b54f732a7caff503d701e555c18f6aad66bf3fe7252400",
      "version": "66b6a105745383c9f3e1c382ccd7823370d8ff83e3b089a91386d71dd556e010"
    },
    "web_ae28c6908f2bceed_review": {
      "sha256": "e8705efa68fc6f32c9f717b39e707bdd4d8b3a87700de0b6ab4cb8ebff76e80a",
      "version": "66b6a105745383c9f3e1c382ccd7823370d8ff83e3b089a91386d71dd556e010"
    }
  },
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
      "issues": [],
      "ready": true,
      "required_for_publication": true
    }
  }
}
```
