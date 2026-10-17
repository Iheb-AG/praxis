# RCC: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RCC | 0x40023800 | AHB1 | HSE8/PLL; see reviewed clock plan | header:RCC_BASE; rcc_review:instance:RCC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | mixed | not asserted | Mixed RW controls and read-only readiness/calibration. Reset 0x0000XX83 has undefined calibration bits; preserve unrelated fields and reserved values. | header:RCC_TypeDef.CR; rcc_review:CR; rm_clock_v1_221:page:221; rm_clock_v1_225:page:225; rm_clock_v1_226:page:226; rm_clock_v1_227:page:227; rm_clock_v1_228:page:228 | 8, 16, 32 |
| PLLCFGR | 0x004 | 32 | — | RW | not asserted | Change PLL parameters only with PLL disabled and PLLRDY=0. | header:RCC_TypeDef.PLLCFGR; rcc_review:PLLCFGR; rm_clock_v1_227:page:227; rm_clock_v1_228:page:228 | 32 |
| CFGR | 0x008 | 32 | — | mixed | 0x0 | SWS reflects selected source; wait after changing SW. | header:RCC_TypeDef.CFGR; rcc_review:CFGR; rm_clock_v1_230:page:230; rm_clock_v1_231:page:231 | 8, 16, 32 |
| CIR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIR | not asserted |
| AHB1RSTR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1RSTR | not asserted |
| AHB2RSTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2RSTR | not asserted |
| AHB3RSTR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3RSTR | not asserted |
| APB1RSTR | 0x020 | 32 | — | RW | 0x0 | Owned-startup reset control: setting I2C1RST resets I2C1; clear to release. Preserve unrelated/reserved bits. Never pulse while another client owns an active bus. | header:RCC_TypeDef.APB1RSTR; rcc_review:APB1RSTR; rm_i2c_238:page:238; rm_i2c_239:page:239; rm_dac_238:page:238; rm_dac_239:page:239; rm_dac_239:page:239; timer_modes_evidence:rm0090/page:240; timer_routes_evidence:rm0090/page:240 | 32 |
| APB2RSTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2RSTR | not asserted |
| AHB1ENR | 0x030 | 32 | — | RW | 0x100000 | Read back after enabling a clock before peripheral access. Preserve reserved bits at their reset values. Gate enable does not establish source clock frequency or readiness. | header:RCC_TypeDef.AHB1ENR; rcc_review:AHB1ENR; rm_features_243:page:243; rm_features_244:page:244; timer_routes_evidence:rm0090/page:245 | 8, 16, 32 |
| AHB2ENR | 0x034 | 32 | — | RW | 0x0 | Not asserted; consult reviewed operating semantics. Preserve reserved bits at their reset values. Gate enable does not establish source clock frequency or readiness. | header:RCC_TypeDef.AHB2ENR; header:RCC_TypeDef.AHB2ENR; rm_features_245:page:245 | 8, 16, 32 |
| AHB3ENR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3ENR | not asserted |
| APB1ENR | 0x040 | 32 | — | RW | 0x0 | Read back before accessing the newly enabled peripheral. Preserve reserved bits at their reset values. Gate enable does not establish source clock frequency or readiness. | header:RCC_TypeDef.APB1ENR; rcc_review:APB1ENR; rm_features_248:page:248; rm_clock_v1_247:page:247; rm_i2c_247:page:247; rm_dac_247:page:247; rm_dac_247:page:247; rm_dac_247:page:247; timer_modes_evidence:rm0090/page:249; timer_routes_evidence:rm0090/page:248 | 32 |
| APB2ENR | 0x044 | 32 | — | RW | 0x0 | SYSCFGEN gate only reviewed here; preserve unrelated/reserved bits and read back before access. Preserve reserved bits at their reset values. Gate enable does not establish source clock frequency or readiness. | header:RCC_TypeDef.APB2ENR; rm_apb2_gate:page:250; rm_features_250:page:250; timer_modes_evidence:rm0090/page:250 | 32 |
| AHB1LPENR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1LPENR | not asserted |
| AHB2LPENR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2LPENR | not asserted |
| AHB3LPENR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3LPENR | not asserted |
| APB1LPENR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1LPENR | not asserted |
| APB2LPENR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2LPENR | not asserted |
| BDCR | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.BDCR | not asserted |
| CSR | 0x074 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSR | not asserted |
| SSCGR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.SSCGR | not asserted |
| PLLI2SCFGR | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLLI2SCFGR | not asserted |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 0:0 | 0x1 | Enable HSI before selecting it. | header:RCC_CR_HSION_Msk; header:RCC_CR_HSION_Msk; rm_clock_v1_226:page:226 |
| CR | HSIRDY | 1:1 | 0x2 | Read-only HSI readiness. | header:RCC_CR_HSIRDY_Msk; header:RCC_CR_HSIRDY_Msk; rm_clock_v1_226:page:226 |
| CR | HSITRIM | 7:3 | 0xF8 | Factory default trim 16 | header:RCC_CR_HSITRIM_Msk; rcc_review:CR.HSITRIM |
| CR | HSICAL | 15:8 | 0xFF00 | Read-only factory calibration | header:RCC_CR_HSICAL_Msk; rcc_review:CR.HSICAL |
| CR | HSEON | 16:16 | 0x10000 | Enable HSE; do not disable while it clocks SYSCLK directly or indirectly. | header:RCC_CR_HSEON_Msk; header:RCC_CR_HSEON_Msk; rm_clock_v1_226:page:226 |
| CR | HSERDY | 17:17 | 0x20000 | Read-only HSE readiness; confirm deasserted before changing bypass. | header:RCC_CR_HSERDY_Msk; header:RCC_CR_HSERDY_Msk; rm_clock_v1_226:page:226 |
| CR | HSEBYP | 18:18 | 0x40000 | Crystal/bypass selection writable only while HSE disabled; crystal recipe clears it. | header:RCC_CR_HSEBYP_Msk; header:RCC_CR_HSEBYP_Msk; rm_clock_v1_226:page:226 |
| CR | CSSON | 19:19 | 0x80000 | Clock security setup and NMI recovery are outside this startup mode. | header:RCC_CR_CSSON_Msk; header:RCC_CR_CSSON_Msk; rm_clock_v1_225:page:225; rm_clock_v1_221:page:221 |
| CR | PLLON | 24:24 | 0x1000000 | Enable PLL only after configuration; cannot disable while PLL is SYSCLK. | header:RCC_CR_PLLON_Msk; header:RCC_CR_PLLON_Msk; rm_clock_v1_225:page:225 |
| CR | PLLRDY | 25:25 | 0x2000000 | Read-only main PLL lock status. | header:RCC_CR_PLLRDY_Msk; header:RCC_CR_PLLRDY_Msk; rm_clock_v1_225:page:225 |
| CR | PLLI2SON | 26:26 | 0x4000000 | Shared PLLM/PLLSRC require PLLI2S disabled before reconfiguration. | header:RCC_CR_PLLI2SON_Msk; header:RCC_CR_PLLI2SON_Msk; rm_clock_v1_225:page:225; rm_clock_v1_227:page:227; rm_clock_v1_228:page:228 |
| CR | PLLI2SRDY | 27:27 | 0x8000000 | PLLI2S ready | header:RCC_CR_PLLI2SRDY_Msk; rcc_review:CR.PLLI2SRDY |
| PLLCFGR | PLLM | 5:0 | 0x3F | Shared input divisor, written only with PLL and PLLI2S disabled; declared divisor8. | header:RCC_PLLCFGR_PLLM_Msk; header:RCC_PLLCFGR_PLLM_Msk; rm_clock_v1_228:page:228 |
| PLLCFGR | PLLN | 14:6 | 0x7FC0 | Main VCO multiplier, PLL disabled for writes; declared multiplier336; halfword/word writes. | header:RCC_PLLCFGR_PLLN_Msk; header:RCC_PLLCFGR_PLLN_Msk; rm_clock_v1_228:page:228 |
| PLLCFGR | PLLP | 17:16 | 0x30000 | Main output divisor; encoded0 means /2 for declared operating point. | header:RCC_PLLCFGR_PLLP_Msk; header:RCC_PLLCFGR_PLLP_Msk; rm_clock_v1_228:page:228 |
| PLLCFGR | PLLSRC | 22:22 | 0x400000 | Shared source select;1=HSE; both PLLs must be disabled to write. | header:RCC_PLLCFGR_PLLSRC_Msk; header:RCC_PLLCFGR_PLLSRC_Msk; rm_clock_v1_227:page:227 |
| PLLCFGR | PLLQ | 27:24 | 0xF000000 | PLL48 divisor; declared7 yields48MHz from336MHz VCO; PLL must be disabled to write. | header:RCC_PLLCFGR_PLLQ_Msk; header:RCC_PLLCFGR_PLLQ_Msk; rm_clock_v1_227:page:227 |
| CFGR | SW | 1:0 | 0x3 | Software source select:0=HSI,2=PLL; selection is not proof of switch completion. | header:RCC_CFGR_SW_Msk; header:RCC_CFGR_SW_Msk; rm_clock_v1_231:page:231 |
| CFGR | SWS | 3:2 | 0xC | Read-only current source:0=HSI,2=PLL; confirm each transition with finite polling. | header:RCC_CFGR_SWS_Msk; header:RCC_CFGR_SWS_Msk; rm_clock_v1_231:page:231 |
| CFGR | HPRE | 7:4 | 0xF0 | AHB prescaler; encoded0=/1 in this profile. | header:RCC_CFGR_HPRE_Msk; header:RCC_CFGR_HPRE_Msk; rm_clock_v1_231:page:231 |
| CFGR | PPRE1 | 12:10 | 0x1C00 | APB1 prescaler;encoded5=/4,42MHz at168MHz HCLK. | header:RCC_CFGR_PPRE1_Msk; header:RCC_CFGR_PPRE1_Msk; rm_clock_v1_230:page:230 |
| CFGR | PPRE2 | 15:13 | 0xE000 | APB2 prescaler;encoded4=/2,84MHz at168MHz HCLK. | header:RCC_CFGR_PPRE2_Msk; header:RCC_CFGR_PPRE2_Msk; rm_clock_v1_230:page:230 |
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
| APB1RSTR | TIM2RST | 0:0 | 0x1 | 0 releases/1 asserts named timer reset; preserve unrelated bits, read back both transitions. | header:RCC_APB1RSTR_TIM2RST_Msk; header:RCC_APB1RSTR_TIM2RST_Msk; timer_modes_evidence:rm0090/page:240; timer_routes_evidence:rm0090/page:240 |
| APB1RSTR | TIM3RST | 1:1 | 0x2 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM3RST_Msk; header:RCC_APB1RSTR_TIM3RST_Msk |
| APB1RSTR | TIM4RST | 2:2 | 0x4 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_TIM4RST_Msk; header:RCC_APB1RSTR_TIM4RST_Msk |
| APB1RSTR | TIM5RST | 3:3 | 0x8 | 0 releases/1 asserts named timer reset; preserve unrelated bits, read back both transitions. | header:RCC_APB1RSTR_TIM5RST_Msk; header:RCC_APB1RSTR_TIM5RST_Msk; timer_routes_evidence:rm0090/page:240 |
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
| APB1RSTR | I2C1RST | 21:21 | 0x200000 | 1 resets I2C1;0 releases. Pulse only under exclusive ownership and idle/released bus. | header:RCC_APB1RSTR_I2C1RST_Msk; header:RCC_APB1RSTR_I2C1RST_Msk; rm_i2c_239:page:239 |
| APB1RSTR | I2C2RST | 22:22 | 0x400000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_I2C2RST_Msk; header:RCC_APB1RSTR_I2C2RST_Msk |
| APB1RSTR | I2C3RST | 23:23 | 0x800000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_I2C3RST_Msk; header:RCC_APB1RSTR_I2C3RST_Msk |
| APB1RSTR | CAN1RST | 25:25 | 0x2000000 | 1 asserts,0 releases CAN1 reset. This contract resets only CAN1 under exclusive ownership with CAN2 disabled. | header:RCC_APB1RSTR_CAN1RST_Msk; header:RCC_APB1RSTR_CAN1RST_Msk; rm_dac_239:page:239 |
| APB1RSTR | CAN2RST | 26:26 | 0x4000000 | 1 asserts,0 releases CAN2 reset. This contract resets only CAN1 under exclusive ownership with CAN2 disabled. | header:RCC_APB1RSTR_CAN2RST_Msk; header:RCC_APB1RSTR_CAN2RST_Msk; rm_dac_239:page:239 |
| APB1RSTR | PWRRST | 28:28 | 0x10000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1RSTR_PWRRST_Msk; header:RCC_APB1RSTR_PWRRST_Msk |
| APB1RSTR | DACRST | 29:29 | 0x20000000 | Set1 asserts reset of the DAC interface (both channels); clear0 releases reset under exclusive ownership. | header:RCC_APB1RSTR_DACRST_Msk; header:RCC_APB1RSTR_DACRST_Msk; rm_dac_238:page:238 |
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
| AHB1ENR | GPIOAEN | 0:0 | 0x1 | 0 disables/1 enables the named peripheral clock; read back before accessing it. | header:RCC_AHB1ENR_GPIOAEN_Msk; rcc_review:AHB1ENR.GPIOAEN; timer_routes_evidence:rm0090/page:245 |
| AHB1ENR | GPIOBEN | 1:1 | 0x2 | 1 enables port clock | header:RCC_AHB1ENR_GPIOBEN_Msk; rcc_review:AHB1ENR.GPIOBEN |
| AHB1ENR | GPIOCEN | 2:2 | 0x4 | 1 enables port clock | header:RCC_AHB1ENR_GPIOCEN_Msk; rcc_review:AHB1ENR.GPIOCEN |
| AHB1ENR | GPIODEN | 3:3 | 0x8 | 1 enables port clock | header:RCC_AHB1ENR_GPIODEN_Msk; rcc_review:AHB1ENR.GPIODEN |
| AHB1ENR | GPIOEEN | 4:4 | 0x10 | 1 enables port clock | header:RCC_AHB1ENR_GPIOEEN_Msk; rcc_review:AHB1ENR.GPIOEEN |
| AHB1ENR | GPIOFEN | 5:5 | 0x20 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOFEN_Msk; header:RCC_AHB1ENR_GPIOFEN_Msk |
| AHB1ENR | GPIOGEN | 6:6 | 0x40 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOGEN_Msk; header:RCC_AHB1ENR_GPIOGEN_Msk |
| AHB1ENR | GPIOHEN | 7:7 | 0x80 | GPIOH gate | header:RCC_AHB1ENR_GPIOHEN_Msk; rcc_review:AHB1ENR.GPIOHEN |
| AHB1ENR | GPIOIEN | 8:8 | 0x100 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_GPIOIEN_Msk; header:RCC_AHB1ENR_GPIOIEN_Msk |
| AHB1ENR | CRCEN | 12:12 | 0x1000 | 1 enables CRC clock; 0 disables it. | header:RCC_AHB1ENR_CRCEN_Msk; rcc_review:AHB1ENR.CRCEN; rm_features_243:page:243; rm_features_244:page:244 |
| AHB1ENR | BKPSRAMEN | 18:18 | 0x40000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_BKPSRAMEN_Msk; header:RCC_AHB1ENR_BKPSRAMEN_Msk |
| AHB1ENR | CCMDATARAMEN | 20:20 | 0x100000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_CCMDATARAMEN_Msk; header:RCC_AHB1ENR_CCMDATARAMEN_Msk |
| AHB1ENR | DMA1EN | 21:21 | 0x200000 | 1 enables DMA1 clock; 0 disables it. | header:RCC_AHB1ENR_DMA1EN_Msk; rcc_review:AHB1ENR.DMA1EN; rm_features_243:page:243; rm_features_244:page:244 |
| AHB1ENR | DMA2EN | 22:22 | 0x400000 | 1 enables DMA2 clock; 0 disables it. | header:RCC_AHB1ENR_DMA2EN_Msk; rcc_review:AHB1ENR.DMA2EN; rm_features_243:page:243; rm_features_244:page:244 |
| AHB1ENR | ETHMACEN | 25:25 | 0x2000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACEN_Msk; header:RCC_AHB1ENR_ETHMACEN_Msk |
| AHB1ENR | ETHMACTXEN | 26:26 | 0x4000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACTXEN_Msk; header:RCC_AHB1ENR_ETHMACTXEN_Msk |
| AHB1ENR | ETHMACRXEN | 27:27 | 0x8000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACRXEN_Msk; header:RCC_AHB1ENR_ETHMACRXEN_Msk |
| AHB1ENR | ETHMACPTPEN | 28:28 | 0x10000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_ETHMACPTPEN_Msk; header:RCC_AHB1ENR_ETHMACPTPEN_Msk |
| AHB1ENR | OTGHSEN | 29:29 | 0x20000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_OTGHSEN_Msk; header:RCC_AHB1ENR_OTGHSEN_Msk |
| AHB1ENR | OTGHSULPIEN | 30:30 | 0x40000000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_AHB1ENR_OTGHSULPIEN_Msk; header:RCC_AHB1ENR_OTGHSULPIEN_Msk |
| AHB2ENR | DCMIEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2ENR_DCMIEN_Msk; header:RCC_AHB2ENR_DCMIEN_Msk |
| AHB2ENR | RNGEN | 6:6 | 0x40 | 1 enables RNG clock; the separate RNG clock source must also be valid. | header:RCC_AHB2ENR_RNGEN_Msk; header:RCC_AHB2ENR_RNGEN_Msk; rm_features_245:page:245 |
| AHB2ENR | OTGFSEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB2ENR_OTGFSEN_Msk; header:RCC_AHB2ENR_OTGFSEN_Msk |
| AHB3ENR | FSMCEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RCC_AHB3ENR_FSMCEN_Msk |
| APB1ENR | TIM2EN | 0:0 | 0x1 | 0 disables/1 enables the named peripheral clock; read back before accessing it. | header:RCC_APB1ENR_TIM2EN_Msk; rcc_review:APB1ENR.TIM2EN; timer_modes_evidence:rm0090/page:249; timer_routes_evidence:rm0090/page:248 |
| APB1ENR | TIM3EN | 1:1 | 0x2 | Timer gate | header:RCC_APB1ENR_TIM3EN_Msk; rcc_review:APB1ENR.TIM3EN |
| APB1ENR | TIM4EN | 2:2 | 0x4 | Timer gate | header:RCC_APB1ENR_TIM4EN_Msk; rcc_review:APB1ENR.TIM4EN |
| APB1ENR | TIM5EN | 3:3 | 0x8 | 0 disables/1 enables the named peripheral clock; read back before accessing it. | header:RCC_APB1ENR_TIM5EN_Msk; rcc_review:APB1ENR.TIM5EN; timer_routes_evidence:rm0090/page:248 |
| APB1ENR | TIM6EN | 4:4 | 0x10 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM6EN_Msk; header:RCC_APB1ENR_TIM6EN_Msk |
| APB1ENR | TIM7EN | 5:5 | 0x20 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM7EN_Msk; header:RCC_APB1ENR_TIM7EN_Msk |
| APB1ENR | TIM12EN | 6:6 | 0x40 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM12EN_Msk; header:RCC_APB1ENR_TIM12EN_Msk |
| APB1ENR | TIM13EN | 7:7 | 0x80 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM13EN_Msk; header:RCC_APB1ENR_TIM13EN_Msk |
| APB1ENR | TIM14EN | 8:8 | 0x100 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_TIM14EN_Msk; header:RCC_APB1ENR_TIM14EN_Msk |
| APB1ENR | WWDGEN | 11:11 | 0x800 | Window watchdog gate | header:RCC_APB1ENR_WWDGEN_Msk; rcc_review:APB1ENR.WWDGEN |
| APB1ENR | SPI2EN | 14:14 | 0x4000 | 1 enables SPI2 clock. | header:RCC_APB1ENR_SPI2EN_Msk; rcc_review:APB1ENR.SPI2EN; rm_features_248:page:248 |
| APB1ENR | SPI3EN | 15:15 | 0x8000 | 1 enables SPI3 clock. | header:RCC_APB1ENR_SPI3EN_Msk; rcc_review:APB1ENR.SPI3EN; rm_features_248:page:248 |
| APB1ENR | USART2EN | 17:17 | 0x20000 | USART2 PCLK1 gate | header:RCC_APB1ENR_USART2EN_Msk; rcc_review:APB1ENR.USART2EN |
| APB1ENR | USART3EN | 18:18 | 0x40000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_USART3EN_Msk; header:RCC_APB1ENR_USART3EN_Msk |
| APB1ENR | UART4EN | 19:19 | 0x80000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_UART4EN_Msk; header:RCC_APB1ENR_UART4EN_Msk |
| APB1ENR | UART5EN | 20:20 | 0x100000 | Declared mask; operating encoding outside this reviewed workflow. | header:RCC_APB1ENR_UART5EN_Msk; header:RCC_APB1ENR_UART5EN_Msk |
| APB1ENR | I2C1EN | 21:21 | 0x200000 | 1 enables I2C1 APB1 clock; read back before peripheral access. | header:RCC_APB1ENR_I2C1EN_Msk; rcc_review:APB1ENR.I2C1EN; rm_i2c_247:page:247 |
| APB1ENR | I2C2EN | 22:22 | 0x400000 | I2C2 gate | header:RCC_APB1ENR_I2C2EN_Msk; rcc_review:APB1ENR.I2C2EN |
| APB1ENR | I2C3EN | 23:23 | 0x800000 | I2C3 gate | header:RCC_APB1ENR_I2C3EN_Msk; rcc_review:APB1ENR.I2C3EN |
| APB1ENR | CAN1EN | 25:25 | 0x2000000 | 1 enables,0 disables CAN1 interface clock; require both CAN gates initially disabled for exclusive shared-filter ownership. | header:RCC_APB1ENR_CAN1EN_Msk; header:RCC_APB1ENR_CAN1EN_Msk; rm_dac_247:page:247 |
| APB1ENR | CAN2EN | 26:26 | 0x4000000 | 1 enables,0 disables CAN2 interface clock; require both CAN gates initially disabled for exclusive shared-filter ownership. | header:RCC_APB1ENR_CAN2EN_Msk; header:RCC_APB1ENR_CAN2EN_Msk; rm_dac_247:page:247 |
| APB1ENR | PWREN | 28:28 | 0x10000000 | Power interface clock enable; set and read back before PWR access. | header:RCC_APB1ENR_PWREN_Msk; header:RCC_APB1ENR_PWREN_Msk; rm_clock_v1_247:page:247 |
| APB1ENR | DACEN | 29:29 | 0x20000000 | DAC interface clock:0 disabled,1 enabled. | header:RCC_APB1ENR_DACEN_Msk; header:RCC_APB1ENR_DACEN_Msk; rm_dac_247:page:247 |
| APB2ENR | TIM1EN | 0:0 | 0x1 | TIM1 gate bit0 must remain disabled for the internal TRC software-capture fixture. | header:RCC_APB2ENR_TIM1EN_Msk; header:RCC_APB2ENR_TIM1EN_Msk; timer_modes_evidence:rm0090/page:250 |
| APB2ENR | TIM8EN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_TIM8EN_Msk |
| APB2ENR | USART1EN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_USART1EN_Msk |
| APB2ENR | USART6EN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_USART6EN_Msk |
| APB2ENR | ADC1EN | 8:8 | 0x100 | 0 disables, 1 enables ADC1 clock; the duplicated disabled entry in RM0090 p250 is resolved by ST HAL SET_BIT enable / clear-bit disable macros. | header:RCC_APB2ENR_ADC1EN_Msk; header:RCC_APB2ENR_ADC1EN_Msk; rm_apb2_gate:page:250; st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE |
| APB2ENR | ADC2EN | 9:9 | 0x200 | Require zero (documented disabled state) for exclusive ADC common configuration; this mode does not enable this ADC. | header:RCC_APB2ENR_ADC2EN_Msk; header:RCC_APB2ENR_ADC2EN_Msk; rm_apb2_gate:page:250; st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE |
| APB2ENR | ADC3EN | 10:10 | 0x400 | Require zero (documented disabled state) for exclusive ADC common configuration; this mode does not enable this ADC. | header:RCC_APB2ENR_ADC3EN_Msk; header:RCC_APB2ENR_ADC3EN_Msk; rm_apb2_gate:page:250; st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE |
| APB2ENR | SDIOEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:RCC_APB2ENR_SDIOEN_Msk |
| APB2ENR | SPI1EN | 12:12 | 0x1000 | 1 enables SPI1 clock. | header:RCC_APB2ENR_SPI1EN_Msk; header:RCC_APB2ENR_SPI1EN_Msk; rm_features_250:page:250 |
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

## Explicit clock-mode publication

The new pll_hse8_168mhz mode requires exact FLASH latency_168mhz and PWR voltage_scale modes. The latter requires RCC power_interface_gate. These form a separate acyclic mode graph; retrieving RCC bus-gate information does not require changing any clock. Retrieve [[peripherals/flash]] and [[peripherals/pwr]] before implementing the PLL recipe. PLLM/PLLSRC are shared with PLLI2S; do not change them while either PLL is enabled. HSEBYP can change only after HSE is disabled and no longer ready. This startup subset rejects active PLLI2S/CSS ownership instead of altering their state. Preserve calibration/reserved bits; RCC_CR reset has undefined HSICAL bits and is not asserted as a complete number. All waits need a bounded failure exit. Failed switching does not permit dependent peripheral initialization.

Evidence: rm_clock_v1_80/81/82,218/219/220/221,225/226/227/228/229/230/231/247, with page locators matching each suffix. These complete pages and declarations were read through ingestion MCP. Editorial synthesis only; no physical clock/supply/errata qualification. See [[features]] and [[coverage]].

## ADC1 / TIM2 exclusive startup gates

The adc_timer_gates contract requires the three ADC gate bits and TIM2EN initially
zero. An existing owner blocks this operation. Enable only ADC1EN and TIM2EN,
preserve unrelated bus gates, and read back each enable before accessing the
peripheral. ADC2/3 remain gated off. Configure shared ADC state only while all
ADCs are disabled. This contract accompanies the declared PLL clock mode.

Explicit source conflict: RM0090 Rev22 page250 prints “disabled” for both
ADC1EN encodings. ST's acquired RCC implementation sets ADC1EN to enable and
clears it to disable, with readback after enable. That resolves ADC1EN=1 for this
subset. It does not extend review to ADC2/3 operation. Evidence: rm_apb2_gate:page:250;
st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE, source SHA-256
eb6911d964b1cf8a83993b19c8feb9845e8793d7c0e5d643390b53207c8b078e.
See [[peripherals/adc_common]], [[peripherals/adc]] and [[peripherals/tim]].

## I2C1 owned-startup gate and reset

I2C1EN is APB1ENR bit21; I2C1RST is APB1RSTR bit21. Enable/read back, pulse reset and release under exclusive ownership; preserve other bits. PCLK1=42 MHz comes from the required PLL recipe. Gate enable establishes no board wiring. Sources: rm_i2c_238:page:238; rm_i2c_239:page:239; rm_i2c_247:page:247. See [[peripherals/i2c]].


DAC amendment: at the declared42 MHz PCLK1 point, exclusive ownership of both DAC channels is required before enabling/readback DACEN (APB1ENR bit29) and asserting/releasing DACRST (APB1RSTR bit29). Preserve unrelated fields. This shared reset must not disturb a live channel owner. The channel1 contract additionally needs GPIO/electrical review and the reviewed TIM2 bounded wait. See [[peripherals/dac]] and [[peripherals/tim]]. Sources: rm_dac_238:page:238; rm_dac_247:page:247; exact header macros.


## CAN1 silent-loopback gate/reset amendment

Require both CAN gates initially disabled and exclusive ownership of CAN1/CAN2 shared filters. Enable and read back CAN1EN, assert/release CAN1RST, preserve unrelated APB1 bits, and leave CAN2EN disabled. Use the reviewed PCLK1=42MHz recipe. Sources: rm_dac_239:page:239; rm_dac_247:page:247; rm_can_1070:page:1070. See [[peripherals/can]] and [[peripherals/nvic]].

## Separate checked HSI16 core context

The hsi16_core_checked mode validates HSION/HSIRDY, SW/SWS=HSI, AHB/APB divisors1 and an updated SystemCoreClock=16000000. It does not switch live clocks or change FLASH/PWR. This owned-startup context is separate from the reference HSE/PLL recipe. SysTick uses the processor clock directly and requires no APB gate. HSI frequency is nominal, not measured. Reject mismatches before starting the core timer. Sources: rm_hsi:page:219; rm_clock_v1_226:page:226; rm_clock_v1_230:page:230; rm_clock_v1_231:page:231. See [[peripherals/systick]] and [[peripherals/scb]].

## Additional owned TIM2 gate/reset contract

Preserve all previously reviewed RCC operating contracts and their individual clock bases.
The new tim2_owned_gate_reset mode requires hsi16_core_checked: nominal16MHz HSI,
HSION/HSIRDY, SW/SWS=HSI, AHB/APB divisors1 and synchronized SystemCoreClock.
It does not switch live clocks or activate the optional168MHz recipe.

Require fresh exclusive TIM2 startup ownership, no downstream TRGO consumers and TIM1EN=0.
TIM2EN (APB1ENR bit0) and TIM2RST (APB1RSTR bit0) must initially be zero. Refuse an existing
owner instead of resetting its timer. Preserve unrelated APB1 enable/reset bits. Set TIM2EN,
read back the gate before timer access, assert/read back TIM2RST, then release/read back reset.
A held reset or failed gate readback blocks dependent setup. All accesses here are words.

With APB1 divisor1, TIM2CLK=PCLK1=nominal16MHz. The multiplier2 rule under divided APB1
is preserved in earlier contracts but not used here. TIM1EN is APB2ENR bit0; keeping it gated
prevents new TIM1_TRGO events on TIM2 ITR0. The application additionally owns all consumers
of TIM2's own UG/TRGO pulse, per ES0182 section2.7.2. No GPIO/board wiring is implied.

Sources: timer_modes_evidence:rm0090/pages238–240,247–250,628;
timer_modes_evidence:es0182/pages17–19; existing checked HSI16 source records.
See [[peripherals/tim]], [[index]] and [[sources]].

## TIM2/TIM5 routed pair

Use timer_pair_gates after hsi16_core_checked. Both TIM2/TIM5 gates and resets
must initially be clear under exclusive startup ownership. Enable/read back GPIOA,
then TIM2/TIM5 gates; assert/read back/release/read back their resets. Preserve every
unrelated RCC bit. Never reset GPIOA. No downstream TRGO consumers may be active
during initialization UG, even with MMS=0. Source: timer_routes_evidence,
RM0090 pages240,243,245,248,249. See [[peripherals/gpio]] and [[peripherals/tim]].

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| adc_timer_gates | RCC | APB1ENR, APB2ENR | APB1ENR: TIM2EN; APB2ENR: ADC1EN, ADC2EN, ADC3EN | Fresh exclusive startup: require all three ADC gate bits and TIM2 gate initially zero; reject an existing owner instead of resetting it.<br>Enable ADC1EN and TIM2EN preserving unrelated gates; read back each gate before peripheral accesses. Keep ADC2/ADC3 gates zero.<br>RM0090 Rev22 p250 repeats disabled for ADC1EN=0 and =1. Resolve the typo using the acquired exact-hash ST HAL enable macro SET_BIT and disable macro bit-clear; retain both sources as an explicit reviewed resolution. | rm_apb2_gate:page:250; st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE; rcc_review:APB1ENR.TIM2EN |  |
| can1_gate_reset | RCC | APB1ENR, APB1RSTR | APB1ENR: CAN1EN, CAN2EN; APB1RSTR: CAN1RST | Start with CAN1 and CAN2 clocks disabled and exclusive ownership of both controllers/shared filters. Do not reset another owner.<br>Enable/read back CAN1EN, assert/release CAN1RST, preserve unrelated bits and leave CAN2EN disabled.<br>Use the declared reviewed PCLK1=42MHz recipe. Clock Boolean and source retrieval do not prove hardware state. | rm_dac_239:page:239; rm_dac_247:page:247; rm_can_1070:page:1070 | [[peripherals/rcc]] / pll_hse8_168mhz: RCC |
| can1_rx_gpio_gate | RCC | AHB1ENR | AHB1ENR: GPIODEN | Enable GPIODEN and read it back before GPIO accesses; preserve every unrelated AHB1 gate. This route changes no peripheral reset or CAN2 state. | rcc_review:AHB1ENR.GPIODEN |  |
| dac_gate_reset | RCC | APB1ENR, APB1RSTR | APB1ENR: DACEN; APB1RSTR: DACRST | Own both DAC channels before asserting reset; no live reconfiguration or reset of an existing owner.<br>Enable DACEN and read it back, assert then release DACRST, preserving unrelated APB1 bits.<br>Use the reviewed HSE8/SYSCLK168/PCLK1=42MHz clock recipe; a software Boolean alone does not prove ownership, reset or electrical readiness. | rm_dac_238:page:238; rm_dac_247:page:247 | [[peripherals/rcc]] / pll_hse8_168mhz: RCC |
| hsi16_core_checked | RCC | CR, CFGR | CFGR: SW, SWS, HPRE, PPRE1, PPRE2; CR: HSION, HSIRDY | Owned cold startup: require HSION=HSIRDY=1, SW=SWS=HSI, AHB/APB divisors1, and SystemCoreClock updated to16000000.<br>This mode checks existing state; it does not switch a running clock or rewrite FLASH/PWR. Reject mismatches before starting SysTick.<br>HSI16 is nominal RC timing, not a physical measurement. SysTick uses HCLK directly and needs no APB peripheral gate. | rm_hsi:page:219; rm_clock_v1_226:page:226; rm_clock_v1_230:page:230; rm_clock_v1_231:page:231; arm_rcc_review:hsi16_core_checked |  |
| i2c1_gate_reset | RCC | APB1ENR, APB1RSTR | APB1ENR: I2C1EN; APB1RSTR: I2C1RST | Exclusive I2C1 owner at owned startup; establish the required PLL clock recipe before access.<br>Enable I2C1EN, read back, pulse I2C1RST then release; preserve all unrelated/reserved RCC bits. Never reset an active bus owner.<br>No GPIO routing, pull-up or external target qualification is asserted by gate/reset. | rm_i2c_238:page:238; rm_i2c_239:page:239; rm_i2c_247:page:247 | [[peripherals/rcc]] / pll_hse8_168mhz: RCC |
| peripheral_clock_gates | RCC | AHB1ENR, AHB2ENR, APB1ENR, APB2ENR | AHB1ENR: CRCEN, DMA1EN, DMA2EN; AHB2ENR: RNGEN; APB1ENR: SPI2EN, SPI3EN; APB2ENR: SPI1EN | Enable the target peripheral clock before accessing its registers.<br>Preserve unrelated and reserved bits.<br>A bus gate is distinct from a valid source clock; the reference PLL plan is not proof of a running clock configuration. | rm_features_243:page:243; rm_features_244:page:244; rm_features_245:page:245; rm_features_248:page:248; rm_features_250:page:250 |  |
| pll_hse8_168mhz | RCC | CR, PLLCFGR, CFGR, APB1ENR | APB1ENR: PWREN; CFGR: SW, SWS, HPRE, PPRE1, PPRE2; CR: HSION, HSIRDY, HSEON, HSERDY, HSEBYP, PLLON, PLLRDY, PLLI2SON, CSSON; PLLCFGR: PLLM, PLLN, PLLP, PLLSRC, PLLQ | Assume HSE8 crystal, internal regulator,2.7-3.6V and exclusive startup ownership; no measured clock or errata certification.<br>Do not reconfigure an active PLLI2S/CSS or live peripheral owner. Enable/wait HSI, select it and confirm SWS before disabling main PLL.<br>Install safe APB1/4 and APB2/2 divisors; disable PLL and wait unlocked; disable HSE and confirm not ready before clearing HSEBYP.<br>Enable/read back PWR gate, establish Scale1/VOSRDY and set/read back FLASH LATENCY5 before increasing HCLK.<br>Enable/wait HSE; with both PLLs disabled program M8/N336/P2/Q7,HSE source while preserving reserved fields; enable PLL and wait lock.<br>Select PLL, confirm SWS and divisors, then synchronize SystemCoreClock. Every wait finite; failure stops dependent initialization without claiming a successful clock switch. | rm_clock_v1_80:page:80; rm_clock_v1_81:page:81; rm_clock_v1_82:page:82; rm_clock_v1_218:page:218; rm_clock_v1_219:page:219; rm_clock_v1_220:page:220; rm_clock_v1_221:page:221; rm_clock_v1_225:page:225; rm_clock_v1_226:page:226; rm_clock_v1_227:page:227; rm_clock_v1_228:page:228; rm_clock_v1_229:page:229; rm_clock_v1_230:page:230; rm_clock_v1_231:page:231; rm_clock_v1_247:page:247 | [[peripherals/flash]] / latency_168mhz: FLASH; [[peripherals/pwr]] / voltage_scale: PWR |
| power_interface_gate | RCC | APB1ENR | APB1ENR: PWREN | Set PWREN, preserving other gate configuration, then read the enable register before PWR access. | rm_clock_v1_247:page:247 |  |
| tim2_owned_gate_reset | RCC | APB1ENR, APB1RSTR, APB2ENR | APB1ENR: TIM2EN; APB1RSTR: TIM2RST; APB2ENR: TIM1EN | Privileged exclusive startup, no TIM2 owner or downstream TRGO consumers; keep TIM1EN=0.<br>Require TIM2EN=0/TIM2RST=0 initially; enable/read back gate, assert/read back reset, release/read back; preserve unrelated bits.<br>No live clock changes; failures block timer setup. | timer_modes_evidence:rm0090/page:240; timer_modes_evidence:rm0090/page:249; timer_modes_evidence:rm0090/page:250; timer_modes_evidence:es0182/page:17 | [[peripherals/rcc]] / hsi16_core_checked: RCC |
| timer_pair_gates | RCC | AHB1ENR, APB1ENR, APB1RSTR | AHB1ENR: GPIOAEN; APB1ENR: TIM2EN, TIM5EN; APB1RSTR: TIM2RST, TIM5RST | Fresh exclusive privileged startup, Thread mode and PRIMASK=1; both timer gates/resets initially clear.<br>Enable/read back GPIOA gate before pin access, then both timer gates; assert/read back/release/read back both resets.<br>Never reset GPIOA or overwrite unrelated gates/resets. No other pin/timer owners, downstream TRGO consumers or live clock changes.<br>Keep IRQ/DMA requests disabled; failure blocks setup and cannot imply hardware is quiet if a clock gate/reset is inaccessible. | timer_routes_evidence:rm0090/page:240; timer_routes_evidence:rm0090/page:243; timer_routes_evidence:rm0090/page:245; timer_routes_evidence:rm0090/page:248; timer_routes_evidence:rm0090/page:249 | [[peripherals/rcc]] / hsi16_core_checked: RCC |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: Exact MCP source parts and schematic images reviewed; implementing-author review only. Independent signoff and new physical qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
