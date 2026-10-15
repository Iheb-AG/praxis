# RCC — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

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
| ICSCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.ICSCR |
| CFGR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CFGR |
| PLLCFGR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLLCFGR |
| CIER | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIER |
| CIFR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIFR |
| CICR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CICR |
| IOPRSTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.IOPRSTR |
| AHBRSTR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHBRSTR |
| APBRSTR1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBRSTR1 |
| APBRSTR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBRSTR2 |
| IOPENR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.IOPENR |
| AHBENR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHBENR |
| APBENR1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBENR1 |
| APBENR2 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBENR2 |
| IOPSMENR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.IOPSMENR |
| AHBSMENR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHBSMENR |
| APBSMENR1 | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBSMENR1 |
| APBSMENR2 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APBSMENR2 |
| CCIPR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CCIPR |
| BDCR | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.BDCR |
| CSR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSION_Msk |
| CR | HSIKERON | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSIKERON_Msk |
| CR | HSIRDY | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSIRDY_Msk |
| CR | HSIDIV | 13:11 | 0x3800 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSIDIV_Msk |
| CR | HSEON | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSEON_Msk |
| CR | HSERDY | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSERDY_Msk |
| CR | HSEBYP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_HSEBYP_Msk |
| CR | CSSON | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_CSSON_Msk |
| CR | PLLON | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_PLLON_Msk |
| CR | PLLRDY | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CR_PLLRDY_Msk |
| ICSCR | HSICAL | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:RCC_ICSCR_HSICAL_Msk |
| ICSCR | HSITRIM | 14:8 | 0x7F00 | Declaration only; encoding requires reviewed semantics. | header:RCC_ICSCR_HSITRIM_Msk |
| CFGR | SW | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_SW_Msk |
| CFGR | SWS | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_SWS_Msk |
| CFGR | HPRE | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_HPRE_Msk |
| CFGR | PPRE | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_PPRE_Msk |
| CFGR | MCOSEL | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_MCOSEL_Msk |
| CFGR | MCOPRE | 30:28 | 0x70000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CFGR_MCOPRE_Msk |
| PLLCFGR | PLLSRC | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLSRC_Msk |
| PLLCFGR | PLLM | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLM_Msk |
| PLLCFGR | PLLN | 14:8 | 0x7F00 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLN_Msk |
| PLLCFGR | PLLPEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLPEN_Msk |
| PLLCFGR | PLLP | 21:17 | 0x3E0000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLP_Msk |
| PLLCFGR | PLLQEN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLQEN_Msk |
| PLLCFGR | PLLQ | 27:25 | 0xE000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLQ_Msk |
| PLLCFGR | PLLREN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLREN_Msk |
| PLLCFGR | PLLR | 31:29 | 0xE0000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLCFGR_PLLR_Msk |
| CIER | LSIRDYIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIER_LSIRDYIE_Msk |
| CIER | LSERDYIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIER_LSERDYIE_Msk |
| CIER | HSIRDYIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIER_HSIRDYIE_Msk |
| CIER | HSERDYIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIER_HSERDYIE_Msk |
| CIER | PLLRDYIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIER_PLLRDYIE_Msk |
| CIFR | LSIRDYF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_LSIRDYF_Msk |
| CIFR | LSERDYF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_LSERDYF_Msk |
| CIFR | HSIRDYF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_HSIRDYF_Msk |
| CIFR | HSERDYF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_HSERDYF_Msk |
| CIFR | PLLRDYF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_PLLRDYF_Msk |
| CIFR | CSSF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_CSSF_Msk |
| CIFR | LSECSSF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIFR_LSECSSF_Msk |
| CICR | LSIRDYC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_LSIRDYC_Msk |
| CICR | LSERDYC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_LSERDYC_Msk |
| CICR | HSIRDYC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_HSIRDYC_Msk |
| CICR | HSERDYC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_HSERDYC_Msk |
| CICR | PLLRDYC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_PLLRDYC_Msk |
| CICR | CSSC | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_CSSC_Msk |
| CICR | LSECSSC | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_CICR_LSECSSC_Msk |
| IOPRSTR | GPIOARST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPRSTR_GPIOARST_Msk |
| IOPRSTR | GPIOBRST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPRSTR_GPIOBRST_Msk |
| IOPRSTR | GPIOCRST | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPRSTR_GPIOCRST_Msk |
| IOPRSTR | GPIODRST | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPRSTR_GPIODRST_Msk |
| IOPRSTR | GPIOFRST | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPRSTR_GPIOFRST_Msk |
| AHBRSTR | DMA1RST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBRSTR_DMA1RST_Msk |
| AHBRSTR | FLASHRST | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBRSTR_FLASHRST_Msk |
| AHBRSTR | CRCRST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBRSTR_CRCRST_Msk |
| APBRSTR1 | TIM2RST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_TIM2RST_Msk |
| APBRSTR1 | TIM3RST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_TIM3RST_Msk |
| APBRSTR1 | TIM6RST | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_TIM6RST_Msk |
| APBRSTR1 | TIM7RST | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_TIM7RST_Msk |
| APBRSTR1 | SPI2RST | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_SPI2RST_Msk |
| APBRSTR1 | USART2RST | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_USART2RST_Msk |
| APBRSTR1 | USART3RST | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_USART3RST_Msk |
| APBRSTR1 | USART4RST | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_USART4RST_Msk |
| APBRSTR1 | LPUART1RST | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_LPUART1RST_Msk |
| APBRSTR1 | I2C1RST | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_I2C1RST_Msk |
| APBRSTR1 | I2C2RST | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_I2C2RST_Msk |
| APBRSTR1 | CECRST | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_CECRST_Msk |
| APBRSTR1 | UCPD1RST | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_UCPD1RST_Msk |
| APBRSTR1 | UCPD2RST | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_UCPD2RST_Msk |
| APBRSTR1 | DBGRST | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_DBGRST_Msk |
| APBRSTR1 | PWRRST | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_PWRRST_Msk |
| APBRSTR1 | DAC1RST | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_DAC1RST_Msk |
| APBRSTR1 | LPTIM2RST | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_LPTIM2RST_Msk |
| APBRSTR1 | LPTIM1RST | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR1_LPTIM1RST_Msk |
| APBRSTR2 | SYSCFGRST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_SYSCFGRST_Msk |
| APBRSTR2 | TIM1RST | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_TIM1RST_Msk |
| APBRSTR2 | SPI1RST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_SPI1RST_Msk |
| APBRSTR2 | USART1RST | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_USART1RST_Msk |
| APBRSTR2 | TIM14RST | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_TIM14RST_Msk |
| APBRSTR2 | TIM15RST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_TIM15RST_Msk |
| APBRSTR2 | TIM16RST | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_TIM16RST_Msk |
| APBRSTR2 | TIM17RST | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_TIM17RST_Msk |
| APBRSTR2 | ADCRST | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBRSTR2_ADCRST_Msk |
| IOPENR | GPIOAEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPENR_GPIOAEN_Msk |
| IOPENR | GPIOBEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPENR_GPIOBEN_Msk |
| IOPENR | GPIOCEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPENR_GPIOCEN_Msk |
| IOPENR | GPIODEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPENR_GPIODEN_Msk |
| IOPENR | GPIOFEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPENR_GPIOFEN_Msk |
| AHBENR | DMA1EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_DMA1EN_Msk |
| AHBENR | FLASHEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_FLASHEN_Msk |
| AHBENR | CRCEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBENR_CRCEN_Msk |
| APBENR1 | TIM2EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_TIM2EN_Msk |
| APBENR1 | TIM3EN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_TIM3EN_Msk |
| APBENR1 | TIM6EN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_TIM6EN_Msk |
| APBENR1 | TIM7EN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_TIM7EN_Msk |
| APBENR1 | RTCAPBEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_RTCAPBEN_Msk |
| APBENR1 | WWDGEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_WWDGEN_Msk |
| APBENR1 | SPI2EN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_SPI2EN_Msk |
| APBENR1 | USART2EN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_USART2EN_Msk |
| APBENR1 | USART3EN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_USART3EN_Msk |
| APBENR1 | USART4EN | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_USART4EN_Msk |
| APBENR1 | LPUART1EN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_LPUART1EN_Msk |
| APBENR1 | I2C1EN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_I2C1EN_Msk |
| APBENR1 | I2C2EN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_I2C2EN_Msk |
| APBENR1 | CECEN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_CECEN_Msk |
| APBENR1 | UCPD1EN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_UCPD1EN_Msk |
| APBENR1 | UCPD2EN | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_UCPD2EN_Msk |
| APBENR1 | DBGEN | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_DBGEN_Msk |
| APBENR1 | PWREN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_PWREN_Msk |
| APBENR1 | DAC1EN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_DAC1EN_Msk |
| APBENR1 | LPTIM2EN | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_LPTIM2EN_Msk |
| APBENR1 | LPTIM1EN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR1_LPTIM1EN_Msk |
| APBENR2 | SYSCFGEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_SYSCFGEN_Msk |
| APBENR2 | TIM1EN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_TIM1EN_Msk |
| APBENR2 | SPI1EN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_SPI1EN_Msk |
| APBENR2 | USART1EN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_USART1EN_Msk |
| APBENR2 | TIM14EN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_TIM14EN_Msk |
| APBENR2 | TIM15EN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_TIM15EN_Msk |
| APBENR2 | TIM16EN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_TIM16EN_Msk |
| APBENR2 | TIM17EN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_TIM17EN_Msk |
| APBENR2 | ADCEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBENR2_ADCEN_Msk |
| IOPSMENR | GPIOASMEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPSMENR_GPIOASMEN_Msk |
| IOPSMENR | GPIOBSMEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPSMENR_GPIOBSMEN_Msk |
| IOPSMENR | GPIOCSMEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPSMENR_GPIOCSMEN_Msk |
| IOPSMENR | GPIODSMEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPSMENR_GPIODSMEN_Msk |
| IOPSMENR | GPIOFSMEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_IOPSMENR_GPIOFSMEN_Msk |
| AHBSMENR | DMA1SMEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBSMENR_DMA1SMEN_Msk |
| AHBSMENR | FLASHSMEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBSMENR_FLASHSMEN_Msk |
| AHBSMENR | SRAMSMEN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBSMENR_SRAMSMEN_Msk |
| AHBSMENR | CRCSMEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHBSMENR_CRCSMEN_Msk |
| APBSMENR1 | TIM2SMEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_TIM2SMEN_Msk |
| APBSMENR1 | TIM3SMEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_TIM3SMEN_Msk |
| APBSMENR1 | TIM6SMEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_TIM6SMEN_Msk |
| APBSMENR1 | TIM7SMEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_TIM7SMEN_Msk |
| APBSMENR1 | RTCAPBSMEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_RTCAPBSMEN_Msk |
| APBSMENR1 | WWDGSMEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_WWDGSMEN_Msk |
| APBSMENR1 | SPI2SMEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_SPI2SMEN_Msk |
| APBSMENR1 | USART2SMEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_USART2SMEN_Msk |
| APBSMENR1 | USART3SMEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_USART3SMEN_Msk |
| APBSMENR1 | USART4SMEN | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_USART4SMEN_Msk |
| APBSMENR1 | LPUART1SMEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_LPUART1SMEN_Msk |
| APBSMENR1 | I2C1SMEN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_I2C1SMEN_Msk |
| APBSMENR1 | I2C2SMEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_I2C2SMEN_Msk |
| APBSMENR1 | CECSMEN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_CECSMEN_Msk |
| APBSMENR1 | UCPD1SMEN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_UCPD1SMEN_Msk |
| APBSMENR1 | UCPD2SMEN | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_UCPD2SMEN_Msk |
| APBSMENR1 | DBGSMEN | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_DBGSMEN_Msk |
| APBSMENR1 | PWRSMEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_PWRSMEN_Msk |
| APBSMENR1 | DAC1SMEN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_DAC1SMEN_Msk |
| APBSMENR1 | LPTIM2SMEN | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_LPTIM2SMEN_Msk |
| APBSMENR1 | LPTIM1SMEN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR1_LPTIM1SMEN_Msk |
| APBSMENR2 | SYSCFGSMEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_SYSCFGSMEN_Msk |
| APBSMENR2 | TIM1SMEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_TIM1SMEN_Msk |
| APBSMENR2 | SPI1SMEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_SPI1SMEN_Msk |
| APBSMENR2 | USART1SMEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_USART1SMEN_Msk |
| APBSMENR2 | TIM14SMEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_TIM14SMEN_Msk |
| APBSMENR2 | TIM15SMEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_TIM15SMEN_Msk |
| APBSMENR2 | TIM16SMEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_TIM16SMEN_Msk |
| APBSMENR2 | TIM17SMEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_TIM17SMEN_Msk |
| APBSMENR2 | ADCSMEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APBSMENR2_ADCSMEN_Msk |
| CCIPR | USART1SEL | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_USART1SEL_Msk |
| CCIPR | USART2SEL | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_USART2SEL_Msk |
| CCIPR | CECSEL | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_CECSEL_Msk |
| CCIPR | LPUART1SEL | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_LPUART1SEL_Msk |
| CCIPR | I2C1SEL | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_I2C1SEL_Msk |
| CCIPR | I2S1SEL | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_I2S1SEL_Msk |
| CCIPR | LPTIM1SEL | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_LPTIM1SEL_Msk |
| CCIPR | LPTIM2SEL | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_LPTIM2SEL_Msk |
| CCIPR | TIM1SEL | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_TIM1SEL_Msk |
| CCIPR | TIM15SEL | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_TIM15SEL_Msk |
| CCIPR | ADCSEL | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CCIPR_ADCSEL_Msk |
| BDCR | LSEON | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEON_Msk |
| BDCR | LSERDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSERDY_Msk |
| BDCR | LSEBYP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEBYP_Msk |
| BDCR | LSEDRV | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEDRV_Msk |
| BDCR | LSECSSON | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSECSSON_Msk |
| BDCR | LSECSSD | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSECSSD_Msk |
| BDCR | RTCSEL | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCSEL_Msk |
| BDCR | RTCEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCEN_Msk |
| BDCR | BDRST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_BDRST_Msk |
| BDCR | LSCOEN | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSCOEN_Msk |
| BDCR | LSCOSEL | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSCOSEL_Msk |
| CSR | LSION | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSION_Msk |
| CSR | LSIRDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSIRDY_Msk |
| CSR | RMVF | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_RMVF_Msk |
| CSR | OBLRSTF | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_OBLRSTF_Msk |
| CSR | PINRSTF | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PINRSTF_Msk |
| CSR | PWRRSTF | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PWRRSTF_Msk |
| CSR | SFTRSTF | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_SFTRSTF_Msk |
| CSR | IWDGRSTF | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_IWDGRSTF_Msk |
| CSR | WWDGRSTF | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_WWDGRSTF_Msk |
| CSR | LPWRRSTF | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LPWRRSTF_Msk |

## Operating semantics unavailable

**rcc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
