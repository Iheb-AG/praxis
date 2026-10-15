# Publication contract

Source: `compilation_policy`; hash and origin: [[sources]].

This reviewed scope defines minimum evidence, extraction identity, and routing links. It does not establish complete MCU coverage, independently certify its sources, or grant firmware build/flash qualification. Changing it requires an explicit new source pin and produces a new immutable revision. See [[index]] for available workflow coverage.

```json
{
  "avr_mcu": null,
  "board_prerequisites": [
    "rcc",
    "gpio"
  ],
  "clock_plan": {
    "ahb_div": {
      "equals": 1,
      "maximum": null,
      "minimum": null
    },
    "apb1_div": {
      "equals": 4,
      "maximum": null,
      "minimum": null
    },
    "apb2_div": {
      "equals": 2,
      "maximum": null,
      "minimum": null
    },
    "flash_wait_states": {
      "equals": 5,
      "maximum": null,
      "minimum": null
    },
    "hse_hz": {
      "equals": 8000000,
      "maximum": null,
      "minimum": null
    },
    "pll_m": {
      "equals": 8,
      "maximum": null,
      "minimum": null
    },
    "pll_n": {
      "equals": 336,
      "maximum": null,
      "minimum": null
    },
    "pll_p": {
      "equals": 2,
      "maximum": null,
      "minimum": null
    },
    "pll_q": {
      "equals": 7,
      "maximum": null,
      "minimum": null
    },
    "vdd_mv": {
      "equals": null,
      "maximum": 3600,
      "minimum": 2700
    }
  },
  "core_source": "cmsis_core",
  "cpu": "cortex-m4",
  "family": "stm32",
  "header_identity": [
    "__STM32F407xx_H"
  ],
  "header_kind": "cmsis",
  "id": "publication_policy",
  "legacy_discovery": {},
  "mcu": "STM32F407VGT6",
  "member_views": {
    "gpio": {
      "AFR": [
        "AFRL",
        "AFRH"
      ]
    }
  },
  "package": "Package_QFP:LQFP-100_14x14mm_P0.5mm",
  "pin_document": "gpio",
  "required_registers": {
    "crc": [
      "CR",
      "DR",
      "IDR"
    ],
    "dma": [
      "HIFCR",
      "HISR",
      "LIFCR",
      "LISR"
    ],
    "dma_stream": [
      "CR",
      "FCR",
      "M0AR",
      "NDTR",
      "PAR"
    ],
    "exti": [
      "EMR",
      "FTSR",
      "IMR",
      "PR",
      "RTSR",
      "SWIER"
    ],
    "gpio": [
      "AFRH",
      "AFRL",
      "BSRR",
      "IDR",
      "LCKR",
      "MODER",
      "ODR",
      "OSPEEDR",
      "OTYPER",
      "PUPDR"
    ],
    "iwdg": [
      "KR",
      "PR",
      "RLR",
      "SR"
    ],
    "nvic": [
      "IABR",
      "ICER",
      "ICPR",
      "IP",
      "ISER",
      "ISPR",
      "STIR"
    ],
    "rcc": [
      "AHB1ENR",
      "AHB2ENR",
      "APB1ENR",
      "APB1RSTR",
      "APB2ENR",
      "CFGR",
      "CR",
      "PLLCFGR"
    ],
    "rng": [
      "CR",
      "DR",
      "SR"
    ],
    "spi": [
      "CR1",
      "CR2",
      "DR",
      "I2SCFGR",
      "SR"
    ],
    "syscfg": [
      "EXTICR0"
    ],
    "tim": [
      "ARR",
      "CNT",
      "CR1",
      "DIER",
      "EGR",
      "PSC",
      "SR"
    ],
    "usart": [
      "BRR",
      "CR1",
      "CR2",
      "CR3",
      "DR",
      "GTPR",
      "SR"
    ]
  },
  "review": {
    "basis": "RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending.; ADC1 internal-reference and TIM2 polling subset reviewed from complete MCP evidence; independent review pending; scoped I2C1 standard-mode transmitter reviewed from actual ingestion MCP; no wiring/errata qualification; MCP evidence-backed candidate PD0 AF9 pull-up prerequisite and finite RX/ack checks; hypothesis only, physical success and independent review pending.",
    "reviewer": "Codex source-backed editorial review through Praxis ingestion MCP",
    "status": "reviewed"
  },
  "schema_version": 1,
  "sources": [
    {
      "locator": "reviewed peripheral publication scope",
      "source": "definitions"
    },
    {
      "locator": "target, header and clock assumptions",
      "source": "profile"
    }
  ]
}
```
