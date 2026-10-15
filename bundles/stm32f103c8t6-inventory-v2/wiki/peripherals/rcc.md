# RCC — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RCC | 0x40021000 | Not asserted | Not asserted | header:RCC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CR |
| CFGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CFGR |
| CIR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIR |
| APB2RSTR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2RSTR |
| APB1RSTR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1RSTR |
| AHBENR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHBENR |
| APB2ENR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2ENR |
| APB1ENR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1ENR |
| BDCR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.BDCR |
| CSR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSION_Msk |
| CR | HSIRDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSIRDY_Msk |
| CR | HSITRIM | 7:3 | 0xF8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSITRIM_Msk |
| CR | HSICAL | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSICAL_Msk |
| CR | HSEON | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSEON_Msk |
| CR | HSERDY | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSERDY_Msk |
| CR | HSEBYP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSEBYP_Msk |
| CR | CSSON | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_CSSON_Msk |
| CR | PLLON | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_PLLON_Msk |
| CR | PLLRDY | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_PLLRDY_Msk |
| CIR | LSIRDYF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYF_Msk |
| CIR | LSERDYF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYF_Msk |
| CIR | HSIRDYF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYF_Msk |
| CIR | HSERDYF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYF_Msk |
| CIR | PLLRDYF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYF_Msk |
| CIR | CSSF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_CSSF_Msk |
| CIR | LSIRDYIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYIE_Msk |
| CIR | LSERDYIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYIE_Msk |
| CIR | HSIRDYIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYIE_Msk |
| CIR | HSERDYIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYIE_Msk |
| CIR | PLLRDYIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYIE_Msk |
| CIR | LSIRDYC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYC_Msk |
| CIR | LSERDYC | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYC_Msk |
| CIR | HSIRDYC | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYC_Msk |
| CIR | HSERDYC | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYC_Msk |
| CIR | PLLRDYC | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYC_Msk |
| CIR | CSSC | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_CSSC_Msk |
| APB2RSTR | AFIORST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_AFIORST_Msk |
| APB2RSTR | IOPARST | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_IOPARST_Msk |
| APB2RSTR | IOPBRST | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_IOPBRST_Msk |
| APB2RSTR | IOPCRST | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_IOPCRST_Msk |
| APB2RSTR | IOPDRST | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_IOPDRST_Msk |
| APB2RSTR | IOPERST | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_IOPERST_Msk |
| APB2RSTR | ADC1RST | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_ADC1RST_Msk |
| APB2RSTR | ADC2RST | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_ADC2RST_Msk |
| APB2RSTR | TIM1RST | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM1RST_Msk |
| APB2RSTR | SPI1RST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_SPI1RST_Msk |
| APB2RSTR | USART1RST | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_USART1RST_Msk |
| APB1RSTR | TIM2RST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_TIM2RST_Msk |
| APB1RSTR | TIM3RST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_TIM3RST_Msk |
| APB1RSTR | TIM4RST | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_TIM4RST_Msk |
| APB1RSTR | WWDGRST | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_WWDGRST_Msk |
| APB1RSTR | SPI2RST | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_SPI2RST_Msk |
| APB1RSTR | USART2RST | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_USART2RST_Msk |
| APB1RSTR | USART3RST | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_USART3RST_Msk |
| APB1RSTR | I2C1RST | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_I2C1RST_Msk |
| APB1RSTR | I2C2RST | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_I2C2RST_Msk |
| APB1RSTR | USBRST | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_USBRST_Msk |
| APB1RSTR | CAN1RST | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_CAN1RST_Msk |
| APB1RSTR | BKPRST | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_BKPRST_Msk |
| APB1RSTR | PWRRST | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1RSTR_PWRRST_Msk |
| AHBENR | DMA1EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_DMA1EN_Msk |
| AHBENR | SRAMEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_SRAMEN_Msk |
| AHBENR | FLITFEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_FLITFEN_Msk |
| AHBENR | CRCEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_CRCEN_Msk |
| APB2ENR | AFIOEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_AFIOEN_Msk |
| APB2ENR | IOPAEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_IOPAEN_Msk |
| APB2ENR | IOPBEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_IOPBEN_Msk |
| APB2ENR | IOPCEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_IOPCEN_Msk |
| APB2ENR | IOPDEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_IOPDEN_Msk |
| APB2ENR | IOPEEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_IOPEEN_Msk |
| APB2ENR | ADC1EN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_ADC1EN_Msk |
| APB2ENR | ADC2EN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_ADC2EN_Msk |
| APB2ENR | TIM1EN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM1EN_Msk |
| APB2ENR | SPI1EN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_SPI1EN_Msk |
| APB2ENR | USART1EN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_USART1EN_Msk |
| APB1ENR | TIM2EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_TIM2EN_Msk |
| APB1ENR | TIM3EN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_TIM3EN_Msk |
| APB1ENR | TIM4EN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_TIM4EN_Msk |
| APB1ENR | WWDGEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_WWDGEN_Msk |
| APB1ENR | SPI2EN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_SPI2EN_Msk |
| APB1ENR | USART2EN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_USART2EN_Msk |
| APB1ENR | USART3EN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_USART3EN_Msk |
| APB1ENR | I2C1EN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_I2C1EN_Msk |
| APB1ENR | I2C2EN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_I2C2EN_Msk |
| APB1ENR | USBEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_USBEN_Msk |
| APB1ENR | CAN1EN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_CAN1EN_Msk |
| APB1ENR | BKPEN | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_BKPEN_Msk |
| APB1ENR | PWREN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1ENR_PWREN_Msk |
| BDCR | LSEON | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEON_Msk |
| BDCR | LSERDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSERDY_Msk |
| BDCR | LSEBYP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEBYP_Msk |
| BDCR | RTCSEL | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCSEL_Msk |
| BDCR | RTCEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCEN_Msk |
| BDCR | BDRST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_BDRST_Msk |
| CSR | LSION | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSION_Msk |
| CSR | LSIRDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSIRDY_Msk |
| CSR | RMVF | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_RMVF_Msk |
| CSR | PINRSTF | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PINRSTF_Msk |
| CSR | PORRSTF | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PORRSTF_Msk |
| CSR | SFTRSTF | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_SFTRSTF_Msk |
| CSR | IWDGRSTF | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_IWDGRSTF_Msk |
| CSR | WWDGRSTF | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_WWDGRSTF_Msk |
| CSR | LPWRRSTF | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LPWRRSTF_Msk |

## Operating semantics unavailable

**rcc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps (the affected register's entire bit-field set is withheld):

- CFGR: bit fields withheld: UNSUPPORTED_MASK: RCC_CFGR_PLLMULL11_Msk: non-contiguous bit field without an exact declared component partition

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
