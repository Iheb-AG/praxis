# RCC: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RCC | 0x40023800 | AHB1 | HSE8/PLL; see reviewed clock plan | header:RCC_BASE; rcc_review:instance:RCC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | mixed | not asserted | Ready flags are read-only; preserve calibration/reserved bits. | header:RCC_TypeDef.CR; rcc_review:CR |
| PLLCFGR | 0x004 | 32 | — | RW | not asserted | Change PLL parameters only with PLL disabled and PLLRDY=0. | header:RCC_TypeDef.PLLCFGR; rcc_review:PLLCFGR |
| CFGR | 0x008 | 32 | — | mixed | 0x0 | SWS reflects selected source; wait after changing SW. | header:RCC_TypeDef.CFGR; rcc_review:CFGR |
| CIR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIR |
| AHB1RSTR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1RSTR |
| AHB2RSTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2RSTR |
| AHB3RSTR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3RSTR |
| APB1RSTR | 0x020 | 32 | — | RW | 0x0 | Pulse only the required reset bit; clear it before use. | header:RCC_TypeDef.APB1RSTR; rcc_review:APB1RSTR |
| APB2RSTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2RSTR |
| AHB1ENR | 0x030 | 32 | — | RW | not asserted | Read back after enabling a clock before peripheral access. | header:RCC_TypeDef.AHB1ENR; rcc_review:AHB1ENR |
| AHB2ENR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2ENR |
| AHB3ENR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3ENR |
| APB1ENR | 0x040 | 32 | — | RW | 0x0 | Read back before accessing the newly enabled peripheral. | header:RCC_TypeDef.APB1ENR; rcc_review:APB1ENR |
| APB2ENR | 0x044 | 32 | — | RW | 0x0 | SYSCFGEN gate only reviewed here; preserve unrelated/reserved bits and read back before access. | header:RCC_TypeDef.APB2ENR; rm_apb2_gate:page:250 |
| AHB1LPENR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1LPENR |
| AHB2LPENR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2LPENR |
| AHB3LPENR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3LPENR |
| APB1LPENR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1LPENR |
| APB2LPENR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2LPENR |
| BDCR | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.BDCR |
| CSR | 0x074 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSR |
| SSCGR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.SSCGR |
| PLLI2SCFGR | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLLI2SCFGR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 0:0 | 0x1 | 1 enables HSI16 | header:RCC_CR_HSION_Msk; rcc_review:CR.HSION |
| CR | HSIRDY | 1:1 | 0x2 | Wait until 1 with timeout | header:RCC_CR_HSIRDY_Msk; rcc_review:CR.HSIRDY |
| CR | HSITRIM | 7:3 | 0xF8 | Factory default trim 16 | header:RCC_CR_HSITRIM_Msk; rcc_review:CR.HSITRIM |
| CR | HSICAL | 15:8 | 0xFF00 | Read-only factory calibration | header:RCC_CR_HSICAL_Msk; rcc_review:CR.HSICAL |
| CR | HSEON | 16:16 | 0x10000 | Enable assumed 8 MHz external crystal. | header:RCC_CR_HSEON_Msk; rcc_review:CR.HSEON |
| CR | HSERDY | 17:17 | 0x20000 | HSE ready | header:RCC_CR_HSERDY_Msk; rcc_review:CR.HSERDY |
| CR | HSEBYP | 18:18 | 0x40000 | 0 for crystal; bypass needs a different board assumption. | header:RCC_CR_HSEBYP_Msk; rcc_review:CR.HSEBYP |
| CR | CSSON | 19:19 | 0x80000 | Clock security | header:RCC_CR_CSSON_Msk; rcc_review:CR.CSSON |
| CR | PLLON | 24:24 | 0x1000000 | PLL enable | header:RCC_CR_PLLON_Msk; rcc_review:CR.PLLON |
| CR | PLLRDY | 25:25 | 0x2000000 | PLL ready | header:RCC_CR_PLLRDY_Msk; rcc_review:CR.PLLRDY |
| CR | PLLI2SON | 26:26 | 0x4000000 | PLLI2S enable | header:RCC_CR_PLLI2SON_Msk; rcc_review:CR.PLLI2SON |
| CR | PLLI2SRDY | 27:27 | 0x8000000 | PLLI2S ready | header:RCC_CR_PLLI2SRDY_Msk; rcc_review:CR.PLLI2SRDY |
| PLLCFGR | PLLM | 5:0 | 0x3F | 8: HSE divider. | header:RCC_PLLCFGR_PLLM_Msk; rcc_review:PLLCFGR; clock_review:SystemClock_Config |
| PLLCFGR | PLLN | 14:6 | 0x7FC0 | 336: VCO multiplier. | header:RCC_PLLCFGR_PLLN_Msk; rcc_review:PLLCFGR; clock_review:SystemClock_Config |
| PLLCFGR | PLLP | 17:16 | 0x30000 | Encoding 0: SYSCLK divider 2. | header:RCC_PLLCFGR_PLLP_Msk; rcc_review:PLLCFGR; clock_review:SystemClock_Config |
| PLLCFGR | PLLSRC | 22:22 | 0x400000 | 1: HSE source. | header:RCC_PLLCFGR_PLLSRC_Msk; rcc_review:PLLCFGR; clock_review:SystemClock_Config |
| PLLCFGR | PLLQ | 27:24 | 0xF000000 | 7: 48 MHz divider. | header:RCC_PLLCFGR_PLLQ_Msk; rcc_review:PLLCFGR; clock_review:SystemClock_Config |
| CFGR | SW | 1:0 | 0x3 | Encoding 2: PLL selected after readiness checks. | header:RCC_CFGR_SW_Msk; rcc_review:CFGR.SW; clock_review:SystemClock_Config |
| CFGR | SWS | 3:2 | 0xC | Encoding 2 confirms PLL SYSCLK. | header:RCC_CFGR_SWS_Msk; rcc_review:CFGR.SWS; clock_review:SystemClock_Config |
| CFGR | HPRE | 7:4 | 0xF0 | Encoding 0: AHB /1. | header:RCC_CFGR_HPRE_Msk; rcc_review:CFGR.HPRE; clock_review:SystemClock_Config |
| CFGR | PPRE1 | 12:10 | 0x1C00 | Encoding 5: APB1 /4 = 42 MHz. | header:RCC_CFGR_PPRE1_Msk; rcc_review:CFGR.PPRE1; clock_review:SystemClock_Config |
| CFGR | PPRE2 | 15:13 | 0xE000 | Encoding 4: APB2 /2 = 84 MHz. | header:RCC_CFGR_PPRE2_Msk; rcc_review:CFGR.PPRE2; clock_review:SystemClock_Config |
| CFGR | RTCPRE | 20:16 | 0x1F0000 | RTC HSE division | header:RCC_CFGR_RTCPRE_Msk; rcc_review:CFGR.RTCPRE |
| CFGR | MCO1 | 22:21 | 0x600000 | Clock output source | header:RCC_CFGR_MCO1_Msk; rcc_review:CFGR.MCO1 |
| CFGR | I2SSRC | 23:23 | 0x800000 | I2S source | header:RCC_CFGR_I2SSRC_Msk; rcc_review:CFGR.I2SSRC |
| CFGR | MCO1PRE | 26:24 | 0x7000000 | MCO1 division | header:RCC_CFGR_MCO1PRE_Msk; rcc_review:CFGR.MCO1PRE |
| CFGR | MCO2PRE | 29:27 | 0x38000000 | MCO2 division | header:RCC_CFGR_MCO2PRE_Msk; rcc_review:CFGR.MCO2PRE |
| CFGR | MCO2 | 31:30 | 0xC0000000 | MCO2 source | header:RCC_CFGR_MCO2_Msk; rcc_review:CFGR.MCO2 |
| CIR | LSIRDYF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYF_Msk |
| CIR | LSERDYF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYF_Msk |
| CIR | HSIRDYF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYF_Msk |
| CIR | HSERDYF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYF_Msk |
| CIR | PLLRDYF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYF_Msk |
| CIR | PLLI2SRDYF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLI2SRDYF_Msk |
| CIR | CSSF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_CSSF_Msk |
| CIR | LSIRDYIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYIE_Msk |
| CIR | LSERDYIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYIE_Msk |
| CIR | HSIRDYIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYIE_Msk |
| CIR | HSERDYIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYIE_Msk |
| CIR | PLLRDYIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYIE_Msk |
| CIR | PLLI2SRDYIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLI2SRDYIE_Msk |
| CIR | LSIRDYC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSIRDYC_Msk |
| CIR | LSERDYC | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_LSERDYC_Msk |
| CIR | HSIRDYC | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSIRDYC_Msk |
| CIR | HSERDYC | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_HSERDYC_Msk |
| CIR | PLLRDYC | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLRDYC_Msk |
| CIR | PLLI2SRDYC | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_PLLI2SRDYC_Msk |
| CIR | CSSC | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CIR_CSSC_Msk |
| AHB1RSTR | GPIOARST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOARST_Msk |
| AHB1RSTR | GPIOBRST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOBRST_Msk |
| AHB1RSTR | GPIOCRST | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOCRST_Msk |
| AHB1RSTR | GPIODRST | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIODRST_Msk |
| AHB1RSTR | GPIOERST | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOERST_Msk |
| AHB1RSTR | GPIOFRST | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOFRST_Msk |
| AHB1RSTR | GPIOGRST | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOGRST_Msk |
| AHB1RSTR | GPIOHRST | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOHRST_Msk |
| AHB1RSTR | GPIOIRST | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_GPIOIRST_Msk |
| AHB1RSTR | CRCRST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_CRCRST_Msk |
| AHB1RSTR | DMA1RST | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_DMA1RST_Msk |
| AHB1RSTR | DMA2RST | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_DMA2RST_Msk |
| AHB1RSTR | ETHMACRST | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_ETHMACRST_Msk |
| AHB1RSTR | OTGHRST | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1RSTR_OTGHRST_Msk |
| AHB2RSTR | DCMIRST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2RSTR_DCMIRST_Msk |
| AHB2RSTR | RNGRST | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2RSTR_RNGRST_Msk |
| AHB2RSTR | OTGFSRST | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2RSTR_OTGFSRST_Msk |
| AHB3RSTR | FSMCRST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB3RSTR_FSMCRST_Msk |
| APB1RSTR | TIM2RST | 0:0 | 0x1 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM2RST_Msk; header:RCC_APB1RSTR_TIM2RST_Msk |
| APB1RSTR | TIM3RST | 1:1 | 0x2 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM3RST_Msk; header:RCC_APB1RSTR_TIM3RST_Msk |
| APB1RSTR | TIM4RST | 2:2 | 0x4 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM4RST_Msk; header:RCC_APB1RSTR_TIM4RST_Msk |
| APB1RSTR | TIM5RST | 3:3 | 0x8 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM5RST_Msk; header:RCC_APB1RSTR_TIM5RST_Msk |
| APB1RSTR | TIM6RST | 4:4 | 0x10 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM6RST_Msk; header:RCC_APB1RSTR_TIM6RST_Msk |
| APB1RSTR | TIM7RST | 5:5 | 0x20 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM7RST_Msk; header:RCC_APB1RSTR_TIM7RST_Msk |
| APB1RSTR | TIM12RST | 6:6 | 0x40 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM12RST_Msk; header:RCC_APB1RSTR_TIM12RST_Msk |
| APB1RSTR | TIM13RST | 7:7 | 0x80 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM13RST_Msk; header:RCC_APB1RSTR_TIM13RST_Msk |
| APB1RSTR | TIM14RST | 8:8 | 0x100 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM14RST_Msk; header:RCC_APB1RSTR_TIM14RST_Msk |
| APB1RSTR | WWDGRST | 11:11 | 0x800 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_WWDGRST_Msk; header:RCC_APB1RSTR_WWDGRST_Msk |
| APB1RSTR | SPI2RST | 14:14 | 0x4000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_SPI2RST_Msk; header:RCC_APB1RSTR_SPI2RST_Msk |
| APB1RSTR | SPI3RST | 15:15 | 0x8000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_SPI3RST_Msk; header:RCC_APB1RSTR_SPI3RST_Msk |
| APB1RSTR | USART2RST | 17:17 | 0x20000 | 1 holds USART2 in reset | header:RCC_APB1RSTR_USART2RST_Msk; rcc_review:APB1RSTR.USART2RST |
| APB1RSTR | USART3RST | 18:18 | 0x40000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_USART3RST_Msk; header:RCC_APB1RSTR_USART3RST_Msk |
| APB1RSTR | UART4RST | 19:19 | 0x80000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_UART4RST_Msk; header:RCC_APB1RSTR_UART4RST_Msk |
| APB1RSTR | UART5RST | 20:20 | 0x100000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_UART5RST_Msk; header:RCC_APB1RSTR_UART5RST_Msk |
| APB1RSTR | I2C1RST | 21:21 | 0x200000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_I2C1RST_Msk; header:RCC_APB1RSTR_I2C1RST_Msk |
| APB1RSTR | I2C2RST | 22:22 | 0x400000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_I2C2RST_Msk; header:RCC_APB1RSTR_I2C2RST_Msk |
| APB1RSTR | I2C3RST | 23:23 | 0x800000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_I2C3RST_Msk; header:RCC_APB1RSTR_I2C3RST_Msk |
| APB1RSTR | CAN1RST | 25:25 | 0x2000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_CAN1RST_Msk; header:RCC_APB1RSTR_CAN1RST_Msk |
| APB1RSTR | CAN2RST | 26:26 | 0x4000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_CAN2RST_Msk; header:RCC_APB1RSTR_CAN2RST_Msk |
| APB1RSTR | PWRRST | 28:28 | 0x10000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_PWRRST_Msk; header:RCC_APB1RSTR_PWRRST_Msk |
| APB1RSTR | DACRST | 29:29 | 0x20000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_DACRST_Msk; header:RCC_APB1RSTR_DACRST_Msk |
| APB2RSTR | TIM1RST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM1RST_Msk |
| APB2RSTR | TIM8RST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM8RST_Msk |
| APB2RSTR | USART1RST | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_USART1RST_Msk |
| APB2RSTR | USART6RST | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_USART6RST_Msk |
| APB2RSTR | ADCRST | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_ADCRST_Msk |
| APB2RSTR | SDIORST | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_SDIORST_Msk |
| APB2RSTR | SPI1RST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_SPI1RST_Msk |
| APB2RSTR | SYSCFGRST | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_SYSCFGRST_Msk |
| APB2RSTR | TIM9RST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM9RST_Msk |
| APB2RSTR | TIM10RST | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM10RST_Msk |
| APB2RSTR | TIM11RST | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2RSTR_TIM11RST_Msk |
| AHB1ENR | GPIOAEN | 0:0 | 0x1 | 1 enables port clock | header:RCC_AHB1ENR_GPIOAEN_Msk; rcc_review:AHB1ENR.GPIOAEN |
| AHB1ENR | GPIOBEN | 1:1 | 0x2 | 1 enables port clock | header:RCC_AHB1ENR_GPIOBEN_Msk; rcc_review:AHB1ENR.GPIOBEN |
| AHB1ENR | GPIOCEN | 2:2 | 0x4 | 1 enables port clock | header:RCC_AHB1ENR_GPIOCEN_Msk; rcc_review:AHB1ENR.GPIOCEN |
| AHB1ENR | GPIODEN | 3:3 | 0x8 | 1 enables port clock | header:RCC_AHB1ENR_GPIODEN_Msk; rcc_review:AHB1ENR.GPIODEN |
| AHB1ENR | GPIOEEN | 4:4 | 0x10 | 1 enables port clock | header:RCC_AHB1ENR_GPIOEEN_Msk; rcc_review:AHB1ENR.GPIOEEN |
| AHB1ENR | GPIOFEN | 5:5 | 0x20 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOFEN_Msk; header:RCC_AHB1ENR_GPIOFEN_Msk |
| AHB1ENR | GPIOGEN | 6:6 | 0x40 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOGEN_Msk; header:RCC_AHB1ENR_GPIOGEN_Msk |
| AHB1ENR | GPIOHEN | 7:7 | 0x80 | GPIOH gate | header:RCC_AHB1ENR_GPIOHEN_Msk; rcc_review:AHB1ENR.GPIOHEN |
| AHB1ENR | GPIOIEN | 8:8 | 0x100 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOIEN_Msk; header:RCC_AHB1ENR_GPIOIEN_Msk |
| AHB1ENR | CRCEN | 12:12 | 0x1000 | CRC gate | header:RCC_AHB1ENR_CRCEN_Msk; rcc_review:AHB1ENR.CRCEN |
| AHB1ENR | BKPSRAMEN | 18:18 | 0x40000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_BKPSRAMEN_Msk; header:RCC_AHB1ENR_BKPSRAMEN_Msk |
| AHB1ENR | CCMDATARAMEN | 20:20 | 0x100000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_CCMDATARAMEN_Msk; header:RCC_AHB1ENR_CCMDATARAMEN_Msk |
| AHB1ENR | DMA1EN | 21:21 | 0x200000 | DMA1 gate | header:RCC_AHB1ENR_DMA1EN_Msk; rcc_review:AHB1ENR.DMA1EN |
| AHB1ENR | DMA2EN | 22:22 | 0x400000 | DMA2 gate | header:RCC_AHB1ENR_DMA2EN_Msk; rcc_review:AHB1ENR.DMA2EN |
| AHB1ENR | ETHMACEN | 25:25 | 0x2000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACEN_Msk; header:RCC_AHB1ENR_ETHMACEN_Msk |
| AHB1ENR | ETHMACTXEN | 26:26 | 0x4000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACTXEN_Msk; header:RCC_AHB1ENR_ETHMACTXEN_Msk |
| AHB1ENR | ETHMACRXEN | 27:27 | 0x8000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACRXEN_Msk; header:RCC_AHB1ENR_ETHMACRXEN_Msk |
| AHB1ENR | ETHMACPTPEN | 28:28 | 0x10000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACPTPEN_Msk; header:RCC_AHB1ENR_ETHMACPTPEN_Msk |
| AHB1ENR | OTGHSEN | 29:29 | 0x20000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_OTGHSEN_Msk; header:RCC_AHB1ENR_OTGHSEN_Msk |
| AHB1ENR | OTGHSULPIEN | 30:30 | 0x40000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_OTGHSULPIEN_Msk; header:RCC_AHB1ENR_OTGHSULPIEN_Msk |
| AHB2ENR | DCMIEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2ENR_DCMIEN_Msk |
| AHB2ENR | RNGEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2ENR_RNGEN_Msk |
| AHB2ENR | OTGFSEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2ENR_OTGFSEN_Msk |
| AHB3ENR | FSMCEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB3ENR_FSMCEN_Msk |
| APB1ENR | TIM2EN | 0:0 | 0x1 | Timer gate | header:RCC_APB1ENR_TIM2EN_Msk; rcc_review:APB1ENR.TIM2EN |
| APB1ENR | TIM3EN | 1:1 | 0x2 | Timer gate | header:RCC_APB1ENR_TIM3EN_Msk; rcc_review:APB1ENR.TIM3EN |
| APB1ENR | TIM4EN | 2:2 | 0x4 | Timer gate | header:RCC_APB1ENR_TIM4EN_Msk; rcc_review:APB1ENR.TIM4EN |
| APB1ENR | TIM5EN | 3:3 | 0x8 | Timer gate | header:RCC_APB1ENR_TIM5EN_Msk; rcc_review:APB1ENR.TIM5EN |
| APB1ENR | TIM6EN | 4:4 | 0x10 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM6EN_Msk; header:RCC_APB1ENR_TIM6EN_Msk |
| APB1ENR | TIM7EN | 5:5 | 0x20 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM7EN_Msk; header:RCC_APB1ENR_TIM7EN_Msk |
| APB1ENR | TIM12EN | 6:6 | 0x40 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM12EN_Msk; header:RCC_APB1ENR_TIM12EN_Msk |
| APB1ENR | TIM13EN | 7:7 | 0x80 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM13EN_Msk; header:RCC_APB1ENR_TIM13EN_Msk |
| APB1ENR | TIM14EN | 8:8 | 0x100 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM14EN_Msk; header:RCC_APB1ENR_TIM14EN_Msk |
| APB1ENR | WWDGEN | 11:11 | 0x800 | Window watchdog gate | header:RCC_APB1ENR_WWDGEN_Msk; rcc_review:APB1ENR.WWDGEN |
| APB1ENR | SPI2EN | 14:14 | 0x4000 | SPI2 gate | header:RCC_APB1ENR_SPI2EN_Msk; rcc_review:APB1ENR.SPI2EN |
| APB1ENR | SPI3EN | 15:15 | 0x8000 | SPI3 gate | header:RCC_APB1ENR_SPI3EN_Msk; rcc_review:APB1ENR.SPI3EN |
| APB1ENR | USART2EN | 17:17 | 0x20000 | USART2 PCLK1 gate | header:RCC_APB1ENR_USART2EN_Msk; rcc_review:APB1ENR.USART2EN |
| APB1ENR | USART3EN | 18:18 | 0x40000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_USART3EN_Msk; header:RCC_APB1ENR_USART3EN_Msk |
| APB1ENR | UART4EN | 19:19 | 0x80000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_UART4EN_Msk; header:RCC_APB1ENR_UART4EN_Msk |
| APB1ENR | UART5EN | 20:20 | 0x100000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_UART5EN_Msk; header:RCC_APB1ENR_UART5EN_Msk |
| APB1ENR | I2C1EN | 21:21 | 0x200000 | I2C1 gate | header:RCC_APB1ENR_I2C1EN_Msk; rcc_review:APB1ENR.I2C1EN |
| APB1ENR | I2C2EN | 22:22 | 0x400000 | I2C2 gate | header:RCC_APB1ENR_I2C2EN_Msk; rcc_review:APB1ENR.I2C2EN |
| APB1ENR | I2C3EN | 23:23 | 0x800000 | I2C3 gate | header:RCC_APB1ENR_I2C3EN_Msk; rcc_review:APB1ENR.I2C3EN |
| APB1ENR | CAN1EN | 25:25 | 0x2000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_CAN1EN_Msk; header:RCC_APB1ENR_CAN1EN_Msk |
| APB1ENR | CAN2EN | 26:26 | 0x4000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_CAN2EN_Msk; header:RCC_APB1ENR_CAN2EN_Msk |
| APB1ENR | PWREN | 28:28 | 0x10000000 | Power control gate | header:RCC_APB1ENR_PWREN_Msk; rcc_review:APB1ENR.PWREN |
| APB1ENR | DACEN | 29:29 | 0x20000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_DACEN_Msk; header:RCC_APB1ENR_DACEN_Msk |
| APB2ENR | TIM1EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM1EN_Msk |
| APB2ENR | TIM8EN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM8EN_Msk |
| APB2ENR | USART1EN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_USART1EN_Msk |
| APB2ENR | USART6EN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_USART6EN_Msk |
| APB2ENR | ADC1EN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_ADC1EN_Msk |
| APB2ENR | ADC2EN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_ADC2EN_Msk |
| APB2ENR | ADC3EN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_ADC3EN_Msk |
| APB2ENR | SDIOEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_SDIOEN_Msk |
| APB2ENR | SPI1EN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_SPI1EN_Msk |
| APB2ENR | SYSCFGEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_SYSCFGEN_Msk |
| APB2ENR | TIM9EN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM9EN_Msk |
| APB2ENR | TIM10EN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM10EN_Msk |
| APB2ENR | TIM11EN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM11EN_Msk |
| AHB1LPENR | GPIOALPEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOALPEN_Msk |
| AHB1LPENR | GPIOBLPEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOBLPEN_Msk |
| AHB1LPENR | GPIOCLPEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOCLPEN_Msk |
| AHB1LPENR | GPIODLPEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIODLPEN_Msk |
| AHB1LPENR | GPIOELPEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOELPEN_Msk |
| AHB1LPENR | GPIOFLPEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOFLPEN_Msk |
| AHB1LPENR | GPIOGLPEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOGLPEN_Msk |
| AHB1LPENR | GPIOHLPEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOHLPEN_Msk |
| AHB1LPENR | GPIOILPEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_GPIOILPEN_Msk |
| AHB1LPENR | CRCLPEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_CRCLPEN_Msk |
| AHB1LPENR | FLITFLPEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_FLITFLPEN_Msk |
| AHB1LPENR | SRAM1LPEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_SRAM1LPEN_Msk |
| AHB1LPENR | SRAM2LPEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_SRAM2LPEN_Msk |
| AHB1LPENR | BKPSRAMLPEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_BKPSRAMLPEN_Msk |
| AHB1LPENR | DMA1LPEN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_DMA1LPEN_Msk |
| AHB1LPENR | DMA2LPEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_DMA2LPEN_Msk |
| AHB1LPENR | ETHMACLPEN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_ETHMACLPEN_Msk |
| AHB1LPENR | ETHMACTXLPEN | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_ETHMACTXLPEN_Msk |
| AHB1LPENR | ETHMACRXLPEN | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_ETHMACRXLPEN_Msk |
| AHB1LPENR | ETHMACPTPLPEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_ETHMACPTPLPEN_Msk |
| AHB1LPENR | OTGHSLPEN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_OTGHSLPEN_Msk |
| AHB1LPENR | OTGHSULPILPEN | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB1LPENR_OTGHSULPILPEN_Msk |
| AHB2LPENR | DCMILPEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2LPENR_DCMILPEN_Msk |
| AHB2LPENR | RNGLPEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2LPENR_RNGLPEN_Msk |
| AHB2LPENR | OTGFSLPEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2LPENR_OTGFSLPEN_Msk |
| AHB3LPENR | FSMCLPEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB3LPENR_FSMCLPEN_Msk |
| APB1LPENR | TIM2LPEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM2LPEN_Msk |
| APB1LPENR | TIM3LPEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM3LPEN_Msk |
| APB1LPENR | TIM4LPEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM4LPEN_Msk |
| APB1LPENR | TIM5LPEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM5LPEN_Msk |
| APB1LPENR | TIM6LPEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM6LPEN_Msk |
| APB1LPENR | TIM7LPEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM7LPEN_Msk |
| APB1LPENR | TIM12LPEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM12LPEN_Msk |
| APB1LPENR | TIM13LPEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM13LPEN_Msk |
| APB1LPENR | TIM14LPEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_TIM14LPEN_Msk |
| APB1LPENR | WWDGLPEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_WWDGLPEN_Msk |
| APB1LPENR | SPI2LPEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_SPI2LPEN_Msk |
| APB1LPENR | SPI3LPEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_SPI3LPEN_Msk |
| APB1LPENR | USART2LPEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_USART2LPEN_Msk |
| APB1LPENR | USART3LPEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_USART3LPEN_Msk |
| APB1LPENR | UART4LPEN | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_UART4LPEN_Msk |
| APB1LPENR | UART5LPEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_UART5LPEN_Msk |
| APB1LPENR | I2C1LPEN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_I2C1LPEN_Msk |
| APB1LPENR | I2C2LPEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_I2C2LPEN_Msk |
| APB1LPENR | I2C3LPEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_I2C3LPEN_Msk |
| APB1LPENR | CAN1LPEN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_CAN1LPEN_Msk |
| APB1LPENR | CAN2LPEN | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_CAN2LPEN_Msk |
| APB1LPENR | PWRLPEN | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_PWRLPEN_Msk |
| APB1LPENR | DACLPEN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB1LPENR_DACLPEN_Msk |
| APB2LPENR | TIM1LPEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_TIM1LPEN_Msk |
| APB2LPENR | TIM8LPEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_TIM8LPEN_Msk |
| APB2LPENR | USART1LPEN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_USART1LPEN_Msk |
| APB2LPENR | USART6LPEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_USART6LPEN_Msk |
| APB2LPENR | ADC1LPEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_ADC1LPEN_Msk |
| APB2LPENR | ADC2LPEN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_ADC2LPEN_Msk |
| APB2LPENR | ADC3LPEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_ADC3LPEN_Msk |
| APB2LPENR | SDIOLPEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_SDIOLPEN_Msk |
| APB2LPENR | SPI1LPEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_SPI1LPEN_Msk |
| APB2LPENR | SYSCFGLPEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_SYSCFGLPEN_Msk |
| APB2LPENR | TIM9LPEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_TIM9LPEN_Msk |
| APB2LPENR | TIM10LPEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_TIM10LPEN_Msk |
| APB2LPENR | TIM11LPEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2LPENR_TIM11LPEN_Msk |
| BDCR | LSEON | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEON_Msk |
| BDCR | LSERDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSERDY_Msk |
| BDCR | LSEBYP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_LSEBYP_Msk |
| BDCR | RTCSEL | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCSEL_Msk |
| BDCR | RTCEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_RTCEN_Msk |
| BDCR | BDRST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:RCC_BDCR_BDRST_Msk |
| CSR | LSION | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSION_Msk |
| CSR | LSIRDY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LSIRDY_Msk |
| CSR | RMVF | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_RMVF_Msk |
| CSR | BORRSTF | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_BORRSTF_Msk |
| CSR | PINRSTF | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PINRSTF_Msk |
| CSR | PORRSTF | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_PORRSTF_Msk |
| CSR | SFTRSTF | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_SFTRSTF_Msk |
| CSR | IWDGRSTF | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_IWDGRSTF_Msk |
| CSR | WWDGRSTF | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_WWDGRSTF_Msk |
| CSR | LPWRRSTF | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_CSR_LPWRRSTF_Msk |
| SSCGR | MODPER | 12:0 | 0x1FFF | Declaration only; encoding requires reviewed semantics. | header:RCC_SSCGR_MODPER_Msk |
| SSCGR | INCSTEP | 27:13 | 0xFFFE000 | Declaration only; encoding requires reviewed semantics. | header:RCC_SSCGR_INCSTEP_Msk |
| SSCGR | SPREADSEL | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_SSCGR_SPREADSEL_Msk |
| SSCGR | SSCGEN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_SSCGR_SSCGEN_Msk |
| PLLI2SCFGR | PLLI2SN | 14:6 | 0x7FC0 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLI2SCFGR_PLLI2SN_Msk |
| PLLI2SCFGR | PLLI2SR | 30:28 | 0x70000000 | Declaration only; encoding requires reviewed semantics. | header:RCC_PLLI2SCFGR_PLLI2SR_Msk |

## Reviewed operating semantics

Supported workflow: USART2 bring-up under an explicitly assumed 8 MHz HSE crystal,
3.3 V VDD, internal regulator in Scale 1, and the PLL configuration below. This
is an example operating point, not a measurement of the user's board.

| Quantity | Value | Evidence |
| --- | --- | --- |
| HSE | 8,000,000 Hz; crystal mode, HSEBYP=0 | profile:clock_plan; clock_review:SystemClock_Config |
| PLLM / PLLN / PLLP / PLLQ | 8 / 336 / 2 / 7 | profile:clock_plan; header:RCC_PLLCFGR_* |
| VCO input / output | 1 MHz / 336 MHz | profile:clock_plan; arithmetic |
| SYSCLK / HCLK | 168 MHz / 168 MHz (AHB /1) | profile:clock_plan; arithmetic |
| PCLK1 / PCLK2 | 42 MHz / 84 MHz (APB1 /4, APB2 /2) | profile:clock_plan; arithmetic |
| PLL48CLK | 48 MHz | profile:clock_plan; arithmetic; no USB accuracy certification |
| FLASH latency | 5 wait states at the assumed supply | clock_review:SystemClock_Config |

Keep interrupts masked and quiesce peripherals before changing clocks. First
enable HSI and wait for HSIRDY with a finite timeout; select HSI and confirm SWS
before disabling the PLL. Enable the PWR bus clock, read it back, and select
Scale 1. Program and read back five FLASH wait states before increasing HCLK.
Do not infer prefetch availability without checking the silicon revision.

Enable HSE in the board's documented crystal/bypass mode and wait for HSERDY.
Wait for PLLRDY=0 before replacing PLLM/N/P/Q and PLLSRC. Program AHB /1, APB1 /4,
and APB2 /2 before the 168 MHz switch. Enable the PLL, wait for PLLRDY=1, select
PLL as SYSCLK and confirm SWS=PLL. Every readiness wait needs a finite deadline
and an error path that prevents further peripheral initialization.

Enable GPIOAEN and USART2EN, then read back the enable registers before peripheral
access. USART2 baud generation uses PCLK1=42 MHz, not the doubled APB timer clock.
Reserved fields must retain their documented values; ready/status bits are not
ordinary writable controls. Resetting USART2 is an explicit operation on an idle
peripheral, never a blanket write to the entire reset register.

PWR and FLASH are prerequisites inside this clock stage. Their full peripheral
catalogs, electrical design, startup, and errata review remain outside this
UART fixture. Header-only entries marked unknown are declarations, not permission
to operate other clock domains. Unknown facts required by a new workflow need a
reviewed import before use.

Sources: `rcc_review` (RM0090 RCC/PWR/FLASH operating semantics), `clock_review`
(ST's UART example SystemClock_Config), and `profile:clock_plan` (local declared
assumptions). See [[peripherals/gpio]], [[peripherals/usart]], and [[sources]].


## UART/timer scenario: explicitly selected HSI operating point

Use HSI nominal 16 MHz, AHB /1, APB1 /1, APB2 /1 for this application. Enable HSI and bound the HSIRDY wait; select HSI and bound the SWS confirmation before changing divisors or disabling PLL. Keep FLASH latency conservatively unchanged while lowering frequency. Synchronize SystemCoreClock and verify the selected RCC bits. Enable/read back GPIOA/GPIOD, USART2/TIM2 on APB1 and SYSCFG on APB2. Reset only owned USART2 and TIM2. The 168 MHz recipe above is optional and is not used here. Sources: rm_clock:page:218; rm_hsi:page:219; rm_apb2_gate:page:250. See [[peripherals/tim]], [[peripherals/syscfg]] and [[peripherals/exti]].

## Review

Reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
