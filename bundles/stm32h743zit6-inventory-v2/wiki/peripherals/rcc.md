# RCC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RCC | 0x58024400 | Not asserted | Not asserted | header:RCC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CR |
| HSICFGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.HSICFGR |
| CRRCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CRRCR |
| CSICFGR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSICFGR |
| CFGR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CFGR |
| D1CFGR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D1CFGR |
| D2CFGR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D2CFGR |
| D3CFGR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D3CFGR |
| PLLCKSELR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLLCKSELR |
| PLLCFGR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLLCFGR |
| PLL1DIVR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL1DIVR |
| PLL1FRACR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL1FRACR |
| PLL2DIVR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL2DIVR |
| PLL2FRACR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL2FRACR |
| PLL3DIVR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL3DIVR |
| PLL3FRACR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.PLL3FRACR |
| D1CCIPR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D1CCIPR |
| D2CCIP1R | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D2CCIP1R |
| D2CCIP2R | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D2CCIP2R |
| D3CCIPR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D3CCIPR |
| CIER | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIER |
| CIFR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CIFR |
| CICR | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CICR |
| BDCR | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.BDCR |
| CSR | 0x074 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.CSR |
| AHB3RSTR | 0x07C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3RSTR |
| AHB1RSTR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1RSTR |
| AHB2RSTR | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2RSTR |
| AHB4RSTR | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB4RSTR |
| APB3RSTR | 0x08C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB3RSTR |
| APB1LRSTR | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1LRSTR |
| APB1HRSTR | 0x094 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1HRSTR |
| APB2RSTR | 0x098 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2RSTR |
| APB4RSTR | 0x09C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB4RSTR |
| GCR | 0x0A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.GCR |
| D3AMR | 0x0A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.D3AMR |
| RSR | 0x0D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.RSR |
| AHB3ENR | 0x0D4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3ENR |
| AHB1ENR | 0x0D8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1ENR |
| AHB2ENR | 0x0DC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2ENR |
| AHB4ENR | 0x0E0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB4ENR |
| APB3ENR | 0x0E4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB3ENR |
| APB1LENR | 0x0E8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1LENR |
| APB1HENR | 0x0EC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1HENR |
| APB2ENR | 0x0F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2ENR |
| APB4ENR | 0x0F4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB4ENR |
| AHB3LPENR | 0x0FC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB3LPENR |
| AHB1LPENR | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB1LPENR |
| AHB2LPENR | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB2LPENR |
| AHB4LPENR | 0x108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.AHB4LPENR |
| APB3LPENR | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB3LPENR |
| APB1LLPENR | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1LLPENR |
| APB1HLPENR | 0x114 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB1HLPENR |
| APB2LPENR | 0x118 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB2LPENR |
| APB4LPENR | 0x11C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RCC_TypeDef.APB4LPENR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 0:0 | 0x1 | meaning_001 | header:RCC_CR_HSION_Msk |
| CR | HSIKERON | 1:1 | 0x2 | meaning_001 | header:RCC_CR_HSIKERON_Msk |
| CR | HSIRDY | 2:2 | 0x4 | meaning_001 | header:RCC_CR_HSIRDY_Msk |
| CR | HSIDIV | 4:3 | 0x18 | meaning_001 | header:RCC_CR_HSIDIV_Msk |
| CR | HSIDIVF | 5:5 | 0x20 | meaning_001 | header:RCC_CR_HSIDIVF_Msk |
| CR | CSION | 7:7 | 0x80 | meaning_001 | header:RCC_CR_CSION_Msk |
| CR | CSIRDY | 8:8 | 0x100 | meaning_001 | header:RCC_CR_CSIRDY_Msk |
| CR | CSIKERON | 9:9 | 0x200 | meaning_001 | header:RCC_CR_CSIKERON_Msk |
| CR | HSI48ON | 12:12 | 0x1000 | meaning_001 | header:RCC_CR_HSI48ON_Msk |
| CR | HSI48RDY | 13:13 | 0x2000 | meaning_001 | header:RCC_CR_HSI48RDY_Msk |
| CR | D1CKRDY | 14:14 | 0x4000 | meaning_001 | header:RCC_CR_D1CKRDY_Msk |
| CR | D2CKRDY | 15:15 | 0x8000 | meaning_001 | header:RCC_CR_D2CKRDY_Msk |
| CR | HSEON | 16:16 | 0x10000 | meaning_001 | header:RCC_CR_HSEON_Msk |
| CR | HSERDY | 17:17 | 0x20000 | meaning_001 | header:RCC_CR_HSERDY_Msk |
| CR | HSEBYP | 18:18 | 0x40000 | meaning_001 | header:RCC_CR_HSEBYP_Msk |
| CR | CSSHSEON | 19:19 | 0x80000 | meaning_001 | header:RCC_CR_CSSHSEON_Msk |
| CR | PLLON | 24:24 | 0x1000000 | meaning_001 | header:RCC_CR_PLLON_Msk |
| CR | PLLRDY | 25:25 | 0x2000000 | meaning_001 | header:RCC_CR_PLLRDY_Msk |
| CR | PLL2ON | 26:26 | 0x4000000 | meaning_001 | header:RCC_CR_PLL2ON_Msk |
| CR | PLL2RDY | 27:27 | 0x8000000 | meaning_001 | header:RCC_CR_PLL2RDY_Msk |
| CR | PLL3ON | 28:28 | 0x10000000 | meaning_001 | header:RCC_CR_PLL3ON_Msk |
| CR | PLL3RDY | 29:29 | 0x20000000 | meaning_001 | header:RCC_CR_PLL3RDY_Msk |
| HSICFGR | HSICAL | 11:0 | 0xFFF | meaning_001 | header:RCC_HSICFGR_HSICAL_Msk |
| HSICFGR | HSITRIM | 30:24 | 0x7F000000 | meaning_001 | header:RCC_HSICFGR_HSITRIM_Msk |
| CRRCR | HSI48CAL | 9:0 | 0x3FF | meaning_001 | header:RCC_CRRCR_HSI48CAL_Msk |
| CSICFGR | CSICAL | 7:0 | 0xFF | meaning_001 | header:RCC_CSICFGR_CSICAL_Msk |
| CSICFGR | CSITRIM | 29:24 | 0x3F000000 | meaning_001 | header:RCC_CSICFGR_CSITRIM_Msk |
| CFGR | SW | 2:0 | 0x7 | meaning_001 | header:RCC_CFGR_SW_Msk |
| CFGR | SWS | 5:3 | 0x38 | meaning_001 | header:RCC_CFGR_SWS_Msk |
| CFGR | STOPWUCK | 6:6 | 0x40 | meaning_001 | header:RCC_CFGR_STOPWUCK_Msk |
| CFGR | STOPKERWUCK | 7:7 | 0x80 | meaning_001 | header:RCC_CFGR_STOPKERWUCK_Msk |
| CFGR | RTCPRE | 13:8 | 0x3F00 | meaning_001 | header:RCC_CFGR_RTCPRE_Msk |
| CFGR | HRTIMSEL | 14:14 | 0x4000 | meaning_001 | header:RCC_CFGR_HRTIMSEL_Msk |
| CFGR | TIMPRE | 15:15 | 0x8000 | meaning_001 | header:RCC_CFGR_TIMPRE_Msk |
| CFGR | MCO1PRE | 21:18 | 0x3C0000 | meaning_001 | header:RCC_CFGR_MCO1PRE_Msk |
| CFGR | MCO1 | 24:22 | 0x1C00000 | meaning_001 | header:RCC_CFGR_MCO1_Msk |
| CFGR | MCO2PRE | 28:25 | 0x1E000000 | meaning_001 | header:RCC_CFGR_MCO2PRE_Msk |
| CFGR | MCO2 | 31:29 | 0xE0000000 | meaning_001 | header:RCC_CFGR_MCO2_Msk |
| D1CFGR | HPRE | 3:0 | 0xF | meaning_001 | header:RCC_D1CFGR_HPRE_Msk |
| D1CFGR | D1PPRE | 6:4 | 0x70 | meaning_001 | header:RCC_D1CFGR_D1PPRE_Msk |
| D1CFGR | D1CPRE | 11:8 | 0xF00 | meaning_001 | header:RCC_D1CFGR_D1CPRE_Msk |
| D2CFGR | D2PPRE1 | 6:4 | 0x70 | meaning_001 | header:RCC_D2CFGR_D2PPRE1_Msk |
| D2CFGR | D2PPRE2 | 10:8 | 0x700 | meaning_001 | header:RCC_D2CFGR_D2PPRE2_Msk |
| D3CFGR | D3PPRE | 6:4 | 0x70 | meaning_001 | header:RCC_D3CFGR_D3PPRE_Msk |
| PLLCKSELR | PLLSRC | 1:0 | 0x3 | meaning_001 | header:RCC_PLLCKSELR_PLLSRC_Msk |
| PLLCKSELR | DIVM1 | 9:4 | 0x3F0 | meaning_001 | header:RCC_PLLCKSELR_DIVM1_Msk |
| PLLCKSELR | DIVM2 | 17:12 | 0x3F000 | meaning_001 | header:RCC_PLLCKSELR_DIVM2_Msk |
| PLLCKSELR | DIVM3 | 25:20 | 0x3F00000 | meaning_001 | header:RCC_PLLCKSELR_DIVM3_Msk |
| PLLCFGR | PLL1FRACEN | 0:0 | 0x1 | meaning_001 | header:RCC_PLLCFGR_PLL1FRACEN_Msk |
| PLLCFGR | PLL1VCOSEL | 1:1 | 0x2 | meaning_001 | header:RCC_PLLCFGR_PLL1VCOSEL_Msk |
| PLLCFGR | PLL1RGE | 3:2 | 0xC | meaning_001 | header:RCC_PLLCFGR_PLL1RGE_Msk |
| PLLCFGR | PLL2FRACEN | 4:4 | 0x10 | meaning_001 | header:RCC_PLLCFGR_PLL2FRACEN_Msk |
| PLLCFGR | PLL2VCOSEL | 5:5 | 0x20 | meaning_001 | header:RCC_PLLCFGR_PLL2VCOSEL_Msk |
| PLLCFGR | PLL2RGE | 7:6 | 0xC0 | meaning_001 | header:RCC_PLLCFGR_PLL2RGE_Msk |
| PLLCFGR | PLL3FRACEN | 8:8 | 0x100 | meaning_001 | header:RCC_PLLCFGR_PLL3FRACEN_Msk |
| PLLCFGR | PLL3VCOSEL | 9:9 | 0x200 | meaning_001 | header:RCC_PLLCFGR_PLL3VCOSEL_Msk |
| PLLCFGR | PLL3RGE | 11:10 | 0xC00 | meaning_001 | header:RCC_PLLCFGR_PLL3RGE_Msk |
| PLLCFGR | DIVP1EN | 16:16 | 0x10000 | meaning_001 | header:RCC_PLLCFGR_DIVP1EN_Msk |
| PLLCFGR | DIVQ1EN | 17:17 | 0x20000 | meaning_001 | header:RCC_PLLCFGR_DIVQ1EN_Msk |
| PLLCFGR | DIVR1EN | 18:18 | 0x40000 | meaning_001 | header:RCC_PLLCFGR_DIVR1EN_Msk |
| PLLCFGR | DIVP2EN | 19:19 | 0x80000 | meaning_001 | header:RCC_PLLCFGR_DIVP2EN_Msk |
| PLLCFGR | DIVQ2EN | 20:20 | 0x100000 | meaning_001 | header:RCC_PLLCFGR_DIVQ2EN_Msk |
| PLLCFGR | DIVR2EN | 21:21 | 0x200000 | meaning_001 | header:RCC_PLLCFGR_DIVR2EN_Msk |
| PLLCFGR | DIVP3EN | 22:22 | 0x400000 | meaning_001 | header:RCC_PLLCFGR_DIVP3EN_Msk |
| PLLCFGR | DIVQ3EN | 23:23 | 0x800000 | meaning_001 | header:RCC_PLLCFGR_DIVQ3EN_Msk |
| PLLCFGR | DIVR3EN | 24:24 | 0x1000000 | meaning_001 | header:RCC_PLLCFGR_DIVR3EN_Msk |
| PLL1DIVR | N1 | 8:0 | 0x1FF | meaning_001 | header:RCC_PLL1DIVR_N1_Msk |
| PLL1DIVR | P1 | 15:9 | 0xFE00 | meaning_001 | header:RCC_PLL1DIVR_P1_Msk |
| PLL1DIVR | Q1 | 22:16 | 0x7F0000 | meaning_001 | header:RCC_PLL1DIVR_Q1_Msk |
| PLL1DIVR | R1 | 30:24 | 0x7F000000 | meaning_001 | header:RCC_PLL1DIVR_R1_Msk |
| PLL1FRACR | FRACN1 | 15:3 | 0xFFF8 | meaning_001 | header:RCC_PLL1FRACR_FRACN1_Msk |
| PLL2DIVR | N2 | 8:0 | 0x1FF | meaning_001 | header:RCC_PLL2DIVR_N2_Msk |
| PLL2DIVR | P2 | 15:9 | 0xFE00 | meaning_001 | header:RCC_PLL2DIVR_P2_Msk |
| PLL2DIVR | Q2 | 22:16 | 0x7F0000 | meaning_001 | header:RCC_PLL2DIVR_Q2_Msk |
| PLL2DIVR | R2 | 30:24 | 0x7F000000 | meaning_001 | header:RCC_PLL2DIVR_R2_Msk |
| PLL2FRACR | FRACN2 | 15:3 | 0xFFF8 | meaning_001 | header:RCC_PLL2FRACR_FRACN2_Msk |
| PLL3DIVR | N3 | 8:0 | 0x1FF | meaning_001 | header:RCC_PLL3DIVR_N3_Msk |
| PLL3DIVR | P3 | 15:9 | 0xFE00 | meaning_001 | header:RCC_PLL3DIVR_P3_Msk |
| PLL3DIVR | Q3 | 22:16 | 0x7F0000 | meaning_001 | header:RCC_PLL3DIVR_Q3_Msk |
| PLL3DIVR | R3 | 30:24 | 0x7F000000 | meaning_001 | header:RCC_PLL3DIVR_R3_Msk |
| PLL3FRACR | FRACN3 | 15:3 | 0xFFF8 | meaning_001 | header:RCC_PLL3FRACR_FRACN3_Msk |
| D1CCIPR | FMCSEL | 1:0 | 0x3 | meaning_001 | header:RCC_D1CCIPR_FMCSEL_Msk |
| D1CCIPR | QSPISEL | 5:4 | 0x30 | meaning_001 | header:RCC_D1CCIPR_QSPISEL_Msk |
| D1CCIPR | SDMMCSEL | 16:16 | 0x10000 | meaning_001 | header:RCC_D1CCIPR_SDMMCSEL_Msk |
| D1CCIPR | CKPERSEL | 29:28 | 0x30000000 | meaning_001 | header:RCC_D1CCIPR_CKPERSEL_Msk |
| D2CCIP1R | SAI1SEL | 2:0 | 0x7 | meaning_001 | header:RCC_D2CCIP1R_SAI1SEL_Msk |
| D2CCIP1R | SAI23SEL | 8:6 | 0x1C0 | meaning_001 | header:RCC_D2CCIP1R_SAI23SEL_Msk |
| D2CCIP1R | SPI123SEL | 14:12 | 0x7000 | meaning_001 | header:RCC_D2CCIP1R_SPI123SEL_Msk |
| D2CCIP1R | SPI45SEL | 18:16 | 0x70000 | meaning_001 | header:RCC_D2CCIP1R_SPI45SEL_Msk |
| D2CCIP1R | SPDIFSEL | 21:20 | 0x300000 | meaning_001 | header:RCC_D2CCIP1R_SPDIFSEL_Msk |
| D2CCIP1R | DFSDM1SEL | 24:24 | 0x1000000 | meaning_001 | header:RCC_D2CCIP1R_DFSDM1SEL_Msk |
| D2CCIP1R | FDCANSEL | 29:28 | 0x30000000 | meaning_001 | header:RCC_D2CCIP1R_FDCANSEL_Msk |
| D2CCIP1R | SWPSEL | 31:31 | 0x80000000 | meaning_001 | header:RCC_D2CCIP1R_SWPSEL_Msk |
| D2CCIP2R | USART28SEL | 2:0 | 0x7 | meaning_001 | header:RCC_D2CCIP2R_USART28SEL_Msk |
| D2CCIP2R | USART16SEL | 5:3 | 0x38 | meaning_001 | header:RCC_D2CCIP2R_USART16SEL_Msk |
| D2CCIP2R | RNGSEL | 9:8 | 0x300 | meaning_001 | header:RCC_D2CCIP2R_RNGSEL_Msk |
| D2CCIP2R | I2C123SEL | 13:12 | 0x3000 | meaning_001 | header:RCC_D2CCIP2R_I2C123SEL_Msk |
| D2CCIP2R | USBSEL | 21:20 | 0x300000 | meaning_001 | header:RCC_D2CCIP2R_USBSEL_Msk |
| D2CCIP2R | CECSEL | 23:22 | 0xC00000 | meaning_001 | header:RCC_D2CCIP2R_CECSEL_Msk |
| D2CCIP2R | LPTIM1SEL | 30:28 | 0x70000000 | meaning_001 | header:RCC_D2CCIP2R_LPTIM1SEL_Msk |
| D3CCIPR | LPUART1SEL | 2:0 | 0x7 | meaning_001 | header:RCC_D3CCIPR_LPUART1SEL_Msk |
| D3CCIPR | I2C4SEL | 9:8 | 0x300 | meaning_001 | header:RCC_D3CCIPR_I2C4SEL_Msk |
| D3CCIPR | LPTIM2SEL | 12:10 | 0x1C00 | meaning_001 | header:RCC_D3CCIPR_LPTIM2SEL_Msk |
| D3CCIPR | LPTIM345SEL | 15:13 | 0xE000 | meaning_001 | header:RCC_D3CCIPR_LPTIM345SEL_Msk |
| D3CCIPR | ADCSEL | 17:16 | 0x30000 | meaning_001 | header:RCC_D3CCIPR_ADCSEL_Msk |
| D3CCIPR | SAI4ASEL | 23:21 | 0xE00000 | meaning_001 | header:RCC_D3CCIPR_SAI4ASEL_Msk |
| D3CCIPR | SAI4BSEL | 26:24 | 0x7000000 | meaning_001 | header:RCC_D3CCIPR_SAI4BSEL_Msk |
| D3CCIPR | SPI6SEL | 30:28 | 0x70000000 | meaning_001 | header:RCC_D3CCIPR_SPI6SEL_Msk |
| CIER | LSIRDYIE | 0:0 | 0x1 | meaning_001 | header:RCC_CIER_LSIRDYIE_Msk |
| CIER | LSERDYIE | 1:1 | 0x2 | meaning_001 | header:RCC_CIER_LSERDYIE_Msk |
| CIER | HSIRDYIE | 2:2 | 0x4 | meaning_001 | header:RCC_CIER_HSIRDYIE_Msk |
| CIER | HSERDYIE | 3:3 | 0x8 | meaning_001 | header:RCC_CIER_HSERDYIE_Msk |
| CIER | CSIRDYIE | 4:4 | 0x10 | meaning_001 | header:RCC_CIER_CSIRDYIE_Msk |
| CIER | HSI48RDYIE | 5:5 | 0x20 | meaning_001 | header:RCC_CIER_HSI48RDYIE_Msk |
| CIER | PLL1RDYIE | 6:6 | 0x40 | meaning_001 | header:RCC_CIER_PLL1RDYIE_Msk |
| CIER | PLL2RDYIE | 7:7 | 0x80 | meaning_001 | header:RCC_CIER_PLL2RDYIE_Msk |
| CIER | PLL3RDYIE | 8:8 | 0x100 | meaning_001 | header:RCC_CIER_PLL3RDYIE_Msk |
| CIER | LSECSSIE | 9:9 | 0x200 | meaning_001 | header:RCC_CIER_LSECSSIE_Msk |
| CIFR | LSIRDYF | 0:0 | 0x1 | meaning_001 | header:RCC_CIFR_LSIRDYF_Msk |
| CIFR | LSERDYF | 1:1 | 0x2 | meaning_001 | header:RCC_CIFR_LSERDYF_Msk |
| CIFR | HSIRDYF | 2:2 | 0x4 | meaning_001 | header:RCC_CIFR_HSIRDYF_Msk |
| CIFR | HSERDYF | 3:3 | 0x8 | meaning_001 | header:RCC_CIFR_HSERDYF_Msk |
| CIFR | CSIRDYF | 4:4 | 0x10 | meaning_001 | header:RCC_CIFR_CSIRDYF_Msk |
| CIFR | HSI48RDYF | 5:5 | 0x20 | meaning_001 | header:RCC_CIFR_HSI48RDYF_Msk |
| CIFR | PLLRDYF | 6:6 | 0x40 | meaning_001 | header:RCC_CIFR_PLLRDYF_Msk |
| CIFR | PLL2RDYF | 7:7 | 0x80 | meaning_001 | header:RCC_CIFR_PLL2RDYF_Msk |
| CIFR | PLL3RDYF | 8:8 | 0x100 | meaning_001 | header:RCC_CIFR_PLL3RDYF_Msk |
| CIFR | LSECSSF | 9:9 | 0x200 | meaning_001 | header:RCC_CIFR_LSECSSF_Msk |
| CIFR | HSECSSF | 10:10 | 0x400 | meaning_001 | header:RCC_CIFR_HSECSSF_Msk |
| CICR | LSIRDYC | 0:0 | 0x1 | meaning_001 | header:RCC_CICR_LSIRDYC_Msk |
| CICR | LSERDYC | 1:1 | 0x2 | meaning_001 | header:RCC_CICR_LSERDYC_Msk |
| CICR | HSIRDYC | 2:2 | 0x4 | meaning_001 | header:RCC_CICR_HSIRDYC_Msk |
| CICR | HSERDYC | 3:3 | 0x8 | meaning_001 | header:RCC_CICR_HSERDYC_Msk |
| CICR | CSIRDYC | 4:4 | 0x10 | meaning_001 | header:RCC_CICR_CSIRDYC_Msk |
| CICR | HSI48RDYC | 5:5 | 0x20 | meaning_001 | header:RCC_CICR_HSI48RDYC_Msk |
| CICR | PLLRDYC | 6:6 | 0x40 | meaning_001 | header:RCC_CICR_PLLRDYC_Msk |
| CICR | PLL2RDYC | 7:7 | 0x80 | meaning_001 | header:RCC_CICR_PLL2RDYC_Msk |
| CICR | PLL3RDYC | 8:8 | 0x100 | meaning_001 | header:RCC_CICR_PLL3RDYC_Msk |
| CICR | LSECSSC | 9:9 | 0x200 | meaning_001 | header:RCC_CICR_LSECSSC_Msk |
| CICR | HSECSSC | 10:10 | 0x400 | meaning_001 | header:RCC_CICR_HSECSSC_Msk |
| BDCR | LSEON | 0:0 | 0x1 | meaning_001 | header:RCC_BDCR_LSEON_Msk |
| BDCR | LSERDY | 1:1 | 0x2 | meaning_001 | header:RCC_BDCR_LSERDY_Msk |
| BDCR | LSEBYP | 2:2 | 0x4 | meaning_001 | header:RCC_BDCR_LSEBYP_Msk |
| BDCR | LSEDRV | 4:3 | 0x18 | meaning_001 | header:RCC_BDCR_LSEDRV_Msk |
| BDCR | LSECSSON | 5:5 | 0x20 | meaning_001 | header:RCC_BDCR_LSECSSON_Msk |
| BDCR | LSECSSD | 6:6 | 0x40 | meaning_001 | header:RCC_BDCR_LSECSSD_Msk |
| BDCR | RTCSEL | 9:8 | 0x300 | meaning_001 | header:RCC_BDCR_RTCSEL_Msk |
| BDCR | RTCEN | 15:15 | 0x8000 | meaning_001 | header:RCC_BDCR_RTCEN_Msk |
| BDCR | BDRST | 16:16 | 0x10000 | meaning_001 | header:RCC_BDCR_BDRST_Msk |
| CSR | LSION | 0:0 | 0x1 | meaning_001 | header:RCC_CSR_LSION_Msk |
| CSR | LSIRDY | 1:1 | 0x2 | meaning_001 | header:RCC_CSR_LSIRDY_Msk |
| AHB3RSTR | MDMARST | 0:0 | 0x1 | meaning_001 | header:RCC_AHB3RSTR_MDMARST_Msk |
| AHB3RSTR | DMA2DRST | 4:4 | 0x10 | meaning_001 | header:RCC_AHB3RSTR_DMA2DRST_Msk |
| AHB3RSTR | JPGDECRST | 5:5 | 0x20 | meaning_001 | header:RCC_AHB3RSTR_JPGDECRST_Msk |
| AHB3RSTR | FMCRST | 12:12 | 0x1000 | meaning_001 | header:RCC_AHB3RSTR_FMCRST_Msk |
| AHB3RSTR | QSPIRST | 14:14 | 0x4000 | meaning_001 | header:RCC_AHB3RSTR_QSPIRST_Msk |
| AHB3RSTR | SDMMC1RST | 16:16 | 0x10000 | meaning_001 | header:RCC_AHB3RSTR_SDMMC1RST_Msk |
| AHB1RSTR | DMA1RST | 0:0 | 0x1 | meaning_001 | header:RCC_AHB1RSTR_DMA1RST_Msk |
| AHB1RSTR | DMA2RST | 1:1 | 0x2 | meaning_001 | header:RCC_AHB1RSTR_DMA2RST_Msk |
| AHB1RSTR | ADC12RST | 5:5 | 0x20 | meaning_001 | header:RCC_AHB1RSTR_ADC12RST_Msk |
| AHB1RSTR | ETH1MACRST | 15:15 | 0x8000 | meaning_001 | header:RCC_AHB1RSTR_ETH1MACRST_Msk |
| AHB1RSTR | USB1OTGHSRST | 25:25 | 0x2000000 | meaning_001 | header:RCC_AHB1RSTR_USB1OTGHSRST_Msk |
| AHB1RSTR | USB2OTGFSRST | 27:27 | 0x8000000 | meaning_001 | header:RCC_AHB1RSTR_USB2OTGFSRST_Msk |
| AHB2RSTR | DCMIRST | 0:0 | 0x1 | meaning_001 | header:RCC_AHB2RSTR_DCMIRST_Msk |
| AHB2RSTR | RNGRST | 6:6 | 0x40 | meaning_001 | header:RCC_AHB2RSTR_RNGRST_Msk |
| AHB2RSTR | SDMMC2RST | 9:9 | 0x200 | meaning_001 | header:RCC_AHB2RSTR_SDMMC2RST_Msk |
| AHB4RSTR | GPIOARST | 0:0 | 0x1 | meaning_001 | header:RCC_AHB4RSTR_GPIOARST_Msk |
| AHB4RSTR | GPIOBRST | 1:1 | 0x2 | meaning_001 | header:RCC_AHB4RSTR_GPIOBRST_Msk |
| AHB4RSTR | GPIOCRST | 2:2 | 0x4 | meaning_001 | header:RCC_AHB4RSTR_GPIOCRST_Msk |
| AHB4RSTR | GPIODRST | 3:3 | 0x8 | meaning_001 | header:RCC_AHB4RSTR_GPIODRST_Msk |
| AHB4RSTR | GPIOERST | 4:4 | 0x10 | meaning_001 | header:RCC_AHB4RSTR_GPIOERST_Msk |
| AHB4RSTR | GPIOFRST | 5:5 | 0x20 | meaning_001 | header:RCC_AHB4RSTR_GPIOFRST_Msk |
| AHB4RSTR | GPIOGRST | 6:6 | 0x40 | meaning_001 | header:RCC_AHB4RSTR_GPIOGRST_Msk |
| AHB4RSTR | GPIOHRST | 7:7 | 0x80 | meaning_001 | header:RCC_AHB4RSTR_GPIOHRST_Msk |
| AHB4RSTR | GPIOIRST | 8:8 | 0x100 | meaning_001 | header:RCC_AHB4RSTR_GPIOIRST_Msk |
| AHB4RSTR | GPIOJRST | 9:9 | 0x200 | meaning_001 | header:RCC_AHB4RSTR_GPIOJRST_Msk |
| AHB4RSTR | GPIOKRST | 10:10 | 0x400 | meaning_001 | header:RCC_AHB4RSTR_GPIOKRST_Msk |
| AHB4RSTR | CRCRST | 19:19 | 0x80000 | meaning_001 | header:RCC_AHB4RSTR_CRCRST_Msk |
| AHB4RSTR | BDMARST | 21:21 | 0x200000 | meaning_001 | header:RCC_AHB4RSTR_BDMARST_Msk |
| AHB4RSTR | ADC3RST | 24:24 | 0x1000000 | meaning_001 | header:RCC_AHB4RSTR_ADC3RST_Msk |
| AHB4RSTR | HSEMRST | 25:25 | 0x2000000 | meaning_001 | header:RCC_AHB4RSTR_HSEMRST_Msk |
| APB3RSTR | LTDCRST | 3:3 | 0x8 | meaning_001 | header:RCC_APB3RSTR_LTDCRST_Msk |
| APB1LRSTR | TIM2RST | 0:0 | 0x1 | meaning_001 | header:RCC_APB1LRSTR_TIM2RST_Msk |
| APB1LRSTR | TIM3RST | 1:1 | 0x2 | meaning_001 | header:RCC_APB1LRSTR_TIM3RST_Msk |
| APB1LRSTR | TIM4RST | 2:2 | 0x4 | meaning_001 | header:RCC_APB1LRSTR_TIM4RST_Msk |
| APB1LRSTR | TIM5RST | 3:3 | 0x8 | meaning_001 | header:RCC_APB1LRSTR_TIM5RST_Msk |
| APB1LRSTR | TIM6RST | 4:4 | 0x10 | meaning_001 | header:RCC_APB1LRSTR_TIM6RST_Msk |
| APB1LRSTR | TIM7RST | 5:5 | 0x20 | meaning_001 | header:RCC_APB1LRSTR_TIM7RST_Msk |
| APB1LRSTR | TIM12RST | 6:6 | 0x40 | meaning_001 | header:RCC_APB1LRSTR_TIM12RST_Msk |
| APB1LRSTR | TIM13RST | 7:7 | 0x80 | meaning_001 | header:RCC_APB1LRSTR_TIM13RST_Msk |
| APB1LRSTR | TIM14RST | 8:8 | 0x100 | meaning_001 | header:RCC_APB1LRSTR_TIM14RST_Msk |
| APB1LRSTR | LPTIM1RST | 9:9 | 0x200 | meaning_001 | header:RCC_APB1LRSTR_LPTIM1RST_Msk |
| APB1LRSTR | SPI2RST | 14:14 | 0x4000 | meaning_001 | header:RCC_APB1LRSTR_SPI2RST_Msk |
| APB1LRSTR | SPI3RST | 15:15 | 0x8000 | meaning_001 | header:RCC_APB1LRSTR_SPI3RST_Msk |
| APB1LRSTR | SPDIFRXRST | 16:16 | 0x10000 | meaning_001 | header:RCC_APB1LRSTR_SPDIFRXRST_Msk |
| APB1LRSTR | USART2RST | 17:17 | 0x20000 | meaning_001 | header:RCC_APB1LRSTR_USART2RST_Msk |
| APB1LRSTR | USART3RST | 18:18 | 0x40000 | meaning_001 | header:RCC_APB1LRSTR_USART3RST_Msk |
| APB1LRSTR | UART4RST | 19:19 | 0x80000 | meaning_001 | header:RCC_APB1LRSTR_UART4RST_Msk |
| APB1LRSTR | UART5RST | 20:20 | 0x100000 | meaning_001 | header:RCC_APB1LRSTR_UART5RST_Msk |
| APB1LRSTR | I2C1RST | 21:21 | 0x200000 | meaning_001 | header:RCC_APB1LRSTR_I2C1RST_Msk |
| APB1LRSTR | I2C2RST | 22:22 | 0x400000 | meaning_001 | header:RCC_APB1LRSTR_I2C2RST_Msk |
| APB1LRSTR | I2C3RST | 23:23 | 0x800000 | meaning_001 | header:RCC_APB1LRSTR_I2C3RST_Msk |
| APB1LRSTR | CECRST | 27:27 | 0x8000000 | meaning_001 | header:RCC_APB1LRSTR_CECRST_Msk |
| APB1LRSTR | DAC12RST | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB1LRSTR_DAC12RST_Msk |
| APB1LRSTR | UART7RST | 30:30 | 0x40000000 | meaning_001 | header:RCC_APB1LRSTR_UART7RST_Msk |
| APB1LRSTR | UART8RST | 31:31 | 0x80000000 | meaning_001 | header:RCC_APB1LRSTR_UART8RST_Msk |
| APB1HRSTR | CRSRST | 1:1 | 0x2 | meaning_001 | header:RCC_APB1HRSTR_CRSRST_Msk |
| APB1HRSTR | SWPMIRST | 2:2 | 0x4 | meaning_001 | header:RCC_APB1HRSTR_SWPMIRST_Msk |
| APB1HRSTR | OPAMPRST | 4:4 | 0x10 | meaning_001 | header:RCC_APB1HRSTR_OPAMPRST_Msk |
| APB1HRSTR | MDIOSRST | 5:5 | 0x20 | meaning_001 | header:RCC_APB1HRSTR_MDIOSRST_Msk |
| APB1HRSTR | FDCANRST | 8:8 | 0x100 | meaning_001 | header:RCC_APB1HRSTR_FDCANRST_Msk |
| APB2RSTR | TIM1RST | 0:0 | 0x1 | meaning_001 | header:RCC_APB2RSTR_TIM1RST_Msk |
| APB2RSTR | TIM8RST | 1:1 | 0x2 | meaning_001 | header:RCC_APB2RSTR_TIM8RST_Msk |
| APB2RSTR | USART1RST | 4:4 | 0x10 | meaning_001 | header:RCC_APB2RSTR_USART1RST_Msk |
| APB2RSTR | USART6RST | 5:5 | 0x20 | meaning_001 | header:RCC_APB2RSTR_USART6RST_Msk |
| APB2RSTR | SPI1RST | 12:12 | 0x1000 | meaning_001 | header:RCC_APB2RSTR_SPI1RST_Msk |
| APB2RSTR | SPI4RST | 13:13 | 0x2000 | meaning_001 | header:RCC_APB2RSTR_SPI4RST_Msk |
| APB2RSTR | TIM15RST | 16:16 | 0x10000 | meaning_001 | header:RCC_APB2RSTR_TIM15RST_Msk |
| APB2RSTR | TIM16RST | 17:17 | 0x20000 | meaning_001 | header:RCC_APB2RSTR_TIM16RST_Msk |
| APB2RSTR | TIM17RST | 18:18 | 0x40000 | meaning_001 | header:RCC_APB2RSTR_TIM17RST_Msk |
| APB2RSTR | SPI5RST | 20:20 | 0x100000 | meaning_001 | header:RCC_APB2RSTR_SPI5RST_Msk |
| APB2RSTR | SAI1RST | 22:22 | 0x400000 | meaning_001 | header:RCC_APB2RSTR_SAI1RST_Msk |
| APB2RSTR | SAI2RST | 23:23 | 0x800000 | meaning_001 | header:RCC_APB2RSTR_SAI2RST_Msk |
| APB2RSTR | SAI3RST | 24:24 | 0x1000000 | meaning_001 | header:RCC_APB2RSTR_SAI3RST_Msk |
| APB2RSTR | DFSDM1RST | 28:28 | 0x10000000 | meaning_001 | header:RCC_APB2RSTR_DFSDM1RST_Msk |
| APB2RSTR | HRTIMRST | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB2RSTR_HRTIMRST_Msk |
| APB4RSTR | SYSCFGRST | 1:1 | 0x2 | meaning_001 | header:RCC_APB4RSTR_SYSCFGRST_Msk |
| APB4RSTR | LPUART1RST | 3:3 | 0x8 | meaning_001 | header:RCC_APB4RSTR_LPUART1RST_Msk |
| APB4RSTR | SPI6RST | 5:5 | 0x20 | meaning_001 | header:RCC_APB4RSTR_SPI6RST_Msk |
| APB4RSTR | I2C4RST | 7:7 | 0x80 | meaning_001 | header:RCC_APB4RSTR_I2C4RST_Msk |
| APB4RSTR | LPTIM2RST | 9:9 | 0x200 | meaning_001 | header:RCC_APB4RSTR_LPTIM2RST_Msk |
| APB4RSTR | LPTIM3RST | 10:10 | 0x400 | meaning_001 | header:RCC_APB4RSTR_LPTIM3RST_Msk |
| APB4RSTR | LPTIM4RST | 11:11 | 0x800 | meaning_001 | header:RCC_APB4RSTR_LPTIM4RST_Msk |
| APB4RSTR | LPTIM5RST | 12:12 | 0x1000 | meaning_001 | header:RCC_APB4RSTR_LPTIM5RST_Msk |
| APB4RSTR | COMP12RST | 14:14 | 0x4000 | meaning_001 | header:RCC_APB4RSTR_COMP12RST_Msk |
| APB4RSTR | VREFRST | 15:15 | 0x8000 | meaning_001 | header:RCC_APB4RSTR_VREFRST_Msk |
| APB4RSTR | SAI4RST | 21:21 | 0x200000 | meaning_001 | header:RCC_APB4RSTR_SAI4RST_Msk |
| GCR | WW1RSC | 0:0 | 0x1 | meaning_001 | header:RCC_GCR_WW1RSC_Msk |
| D3AMR | BDMAAMEN | 0:0 | 0x1 | meaning_001 | header:RCC_D3AMR_BDMAAMEN_Msk |
| D3AMR | LPUART1AMEN | 3:3 | 0x8 | meaning_001 | header:RCC_D3AMR_LPUART1AMEN_Msk |
| D3AMR | SPI6AMEN | 5:5 | 0x20 | meaning_001 | header:RCC_D3AMR_SPI6AMEN_Msk |
| D3AMR | I2C4AMEN | 7:7 | 0x80 | meaning_001 | header:RCC_D3AMR_I2C4AMEN_Msk |
| D3AMR | LPTIM2AMEN | 9:9 | 0x200 | meaning_001 | header:RCC_D3AMR_LPTIM2AMEN_Msk |
| D3AMR | LPTIM3AMEN | 10:10 | 0x400 | meaning_001 | header:RCC_D3AMR_LPTIM3AMEN_Msk |
| D3AMR | LPTIM4AMEN | 11:11 | 0x800 | meaning_001 | header:RCC_D3AMR_LPTIM4AMEN_Msk |
| D3AMR | LPTIM5AMEN | 12:12 | 0x1000 | meaning_001 | header:RCC_D3AMR_LPTIM5AMEN_Msk |
| D3AMR | COMP12AMEN | 14:14 | 0x4000 | meaning_001 | header:RCC_D3AMR_COMP12AMEN_Msk |
| D3AMR | VREFAMEN | 15:15 | 0x8000 | meaning_001 | header:RCC_D3AMR_VREFAMEN_Msk |
| D3AMR | RTCAMEN | 16:16 | 0x10000 | meaning_001 | header:RCC_D3AMR_RTCAMEN_Msk |
| D3AMR | CRCAMEN | 19:19 | 0x80000 | meaning_001 | header:RCC_D3AMR_CRCAMEN_Msk |
| D3AMR | SAI4AMEN | 21:21 | 0x200000 | meaning_001 | header:RCC_D3AMR_SAI4AMEN_Msk |
| D3AMR | ADC3AMEN | 24:24 | 0x1000000 | meaning_001 | header:RCC_D3AMR_ADC3AMEN_Msk |
| D3AMR | BKPRAMAMEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_D3AMR_BKPRAMAMEN_Msk |
| D3AMR | SRAM4AMEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_D3AMR_SRAM4AMEN_Msk |
| RSR | RMVF | 16:16 | 0x10000 | meaning_001 | header:RCC_RSR_RMVF_Msk |
| RSR | CPURSTF | 17:17 | 0x20000 | meaning_001 | header:RCC_RSR_CPURSTF_Msk |
| RSR | D1RSTF | 19:19 | 0x80000 | meaning_001 | header:RCC_RSR_D1RSTF_Msk |
| RSR | D2RSTF | 20:20 | 0x100000 | meaning_001 | header:RCC_RSR_D2RSTF_Msk |
| RSR | BORRSTF | 21:21 | 0x200000 | meaning_001 | header:RCC_RSR_BORRSTF_Msk |
| RSR | PINRSTF | 22:22 | 0x400000 | meaning_001 | header:RCC_RSR_PINRSTF_Msk |
| RSR | PORRSTF | 23:23 | 0x800000 | meaning_001 | header:RCC_RSR_PORRSTF_Msk |
| RSR | SFTRSTF | 24:24 | 0x1000000 | meaning_001 | header:RCC_RSR_SFTRSTF_Msk |
| RSR | IWDG1RSTF | 26:26 | 0x4000000 | meaning_001 | header:RCC_RSR_IWDG1RSTF_Msk |
| RSR | WWDG1RSTF | 28:28 | 0x10000000 | meaning_001 | header:RCC_RSR_WWDG1RSTF_Msk |
| RSR | LPWRRSTF | 30:30 | 0x40000000 | meaning_001 | header:RCC_RSR_LPWRRSTF_Msk |
| AHB3ENR | MDMAEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB3ENR_MDMAEN_Msk |
| AHB3ENR | DMA2DEN | 4:4 | 0x10 | meaning_001 | header:RCC_AHB3ENR_DMA2DEN_Msk |
| AHB3ENR | JPGDECEN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB3ENR_JPGDECEN_Msk |
| AHB3ENR | FMCEN | 12:12 | 0x1000 | meaning_001 | header:RCC_AHB3ENR_FMCEN_Msk |
| AHB3ENR | QSPIEN | 14:14 | 0x4000 | meaning_001 | header:RCC_AHB3ENR_QSPIEN_Msk |
| AHB3ENR | SDMMC1EN | 16:16 | 0x10000 | meaning_001 | header:RCC_AHB3ENR_SDMMC1EN_Msk |
| AHB1ENR | DMA1EN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB1ENR_DMA1EN_Msk |
| AHB1ENR | DMA2EN | 1:1 | 0x2 | meaning_001 | header:RCC_AHB1ENR_DMA2EN_Msk |
| AHB1ENR | ADC12EN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB1ENR_ADC12EN_Msk |
| AHB1ENR | ETH1MACEN | 15:15 | 0x8000 | meaning_001 | header:RCC_AHB1ENR_ETH1MACEN_Msk |
| AHB1ENR | ETH1TXEN | 16:16 | 0x10000 | meaning_001 | header:RCC_AHB1ENR_ETH1TXEN_Msk |
| AHB1ENR | ETH1RXEN | 17:17 | 0x20000 | meaning_001 | header:RCC_AHB1ENR_ETH1RXEN_Msk |
| AHB1ENR | USB1OTGHSEN | 25:25 | 0x2000000 | meaning_001 | header:RCC_AHB1ENR_USB1OTGHSEN_Msk |
| AHB1ENR | USB1OTGHSULPIEN | 26:26 | 0x4000000 | meaning_001 | header:RCC_AHB1ENR_USB1OTGHSULPIEN_Msk |
| AHB1ENR | USB2OTGFSEN | 27:27 | 0x8000000 | meaning_001 | header:RCC_AHB1ENR_USB2OTGFSEN_Msk |
| AHB1ENR | USB2OTGFSULPIEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_AHB1ENR_USB2OTGFSULPIEN_Msk |
| AHB2ENR | DCMIEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB2ENR_DCMIEN_Msk |
| AHB2ENR | RNGEN | 6:6 | 0x40 | meaning_001 | header:RCC_AHB2ENR_RNGEN_Msk |
| AHB2ENR | SDMMC2EN | 9:9 | 0x200 | meaning_001 | header:RCC_AHB2ENR_SDMMC2EN_Msk |
| AHB2ENR | SRAM1EN | 29:29 | 0x20000000 | meaning_001 | header:RCC_AHB2ENR_SRAM1EN_Msk |
| AHB2ENR | SRAM2EN | 30:30 | 0x40000000 | meaning_001 | header:RCC_AHB2ENR_SRAM2EN_Msk |
| AHB2ENR | SRAM3EN | 31:31 | 0x80000000 | meaning_001 | header:RCC_AHB2ENR_SRAM3EN_Msk |
| AHB4ENR | GPIOAEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB4ENR_GPIOAEN_Msk |
| AHB4ENR | GPIOBEN | 1:1 | 0x2 | meaning_001 | header:RCC_AHB4ENR_GPIOBEN_Msk |
| AHB4ENR | GPIOCEN | 2:2 | 0x4 | meaning_001 | header:RCC_AHB4ENR_GPIOCEN_Msk |
| AHB4ENR | GPIODEN | 3:3 | 0x8 | meaning_001 | header:RCC_AHB4ENR_GPIODEN_Msk |
| AHB4ENR | GPIOEEN | 4:4 | 0x10 | meaning_001 | header:RCC_AHB4ENR_GPIOEEN_Msk |
| AHB4ENR | GPIOFEN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB4ENR_GPIOFEN_Msk |
| AHB4ENR | GPIOGEN | 6:6 | 0x40 | meaning_001 | header:RCC_AHB4ENR_GPIOGEN_Msk |
| AHB4ENR | GPIOHEN | 7:7 | 0x80 | meaning_001 | header:RCC_AHB4ENR_GPIOHEN_Msk |
| AHB4ENR | GPIOIEN | 8:8 | 0x100 | meaning_001 | header:RCC_AHB4ENR_GPIOIEN_Msk |
| AHB4ENR | GPIOJEN | 9:9 | 0x200 | meaning_001 | header:RCC_AHB4ENR_GPIOJEN_Msk |
| AHB4ENR | GPIOKEN | 10:10 | 0x400 | meaning_001 | header:RCC_AHB4ENR_GPIOKEN_Msk |
| AHB4ENR | CRCEN | 19:19 | 0x80000 | meaning_001 | header:RCC_AHB4ENR_CRCEN_Msk |
| AHB4ENR | BDMAEN | 21:21 | 0x200000 | meaning_001 | header:RCC_AHB4ENR_BDMAEN_Msk |
| AHB4ENR | ADC3EN | 24:24 | 0x1000000 | meaning_001 | header:RCC_AHB4ENR_ADC3EN_Msk |
| AHB4ENR | HSEMEN | 25:25 | 0x2000000 | meaning_001 | header:RCC_AHB4ENR_HSEMEN_Msk |
| AHB4ENR | BKPRAMEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_AHB4ENR_BKPRAMEN_Msk |
| APB3ENR | LTDCEN | 3:3 | 0x8 | meaning_001 | header:RCC_APB3ENR_LTDCEN_Msk |
| APB3ENR | WWDG1EN | 6:6 | 0x40 | meaning_001 | header:RCC_APB3ENR_WWDG1EN_Msk |
| APB1LENR | TIM2EN | 0:0 | 0x1 | meaning_001 | header:RCC_APB1LENR_TIM2EN_Msk |
| APB1LENR | TIM3EN | 1:1 | 0x2 | meaning_001 | header:RCC_APB1LENR_TIM3EN_Msk |
| APB1LENR | TIM4EN | 2:2 | 0x4 | meaning_001 | header:RCC_APB1LENR_TIM4EN_Msk |
| APB1LENR | TIM5EN | 3:3 | 0x8 | meaning_001 | header:RCC_APB1LENR_TIM5EN_Msk |
| APB1LENR | TIM6EN | 4:4 | 0x10 | meaning_001 | header:RCC_APB1LENR_TIM6EN_Msk |
| APB1LENR | TIM7EN | 5:5 | 0x20 | meaning_001 | header:RCC_APB1LENR_TIM7EN_Msk |
| APB1LENR | TIM12EN | 6:6 | 0x40 | meaning_001 | header:RCC_APB1LENR_TIM12EN_Msk |
| APB1LENR | TIM13EN | 7:7 | 0x80 | meaning_001 | header:RCC_APB1LENR_TIM13EN_Msk |
| APB1LENR | TIM14EN | 8:8 | 0x100 | meaning_001 | header:RCC_APB1LENR_TIM14EN_Msk |
| APB1LENR | LPTIM1EN | 9:9 | 0x200 | meaning_001 | header:RCC_APB1LENR_LPTIM1EN_Msk |
| APB1LENR | SPI2EN | 14:14 | 0x4000 | meaning_001 | header:RCC_APB1LENR_SPI2EN_Msk |
| APB1LENR | SPI3EN | 15:15 | 0x8000 | meaning_001 | header:RCC_APB1LENR_SPI3EN_Msk |
| APB1LENR | SPDIFRXEN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB1LENR_SPDIFRXEN_Msk |
| APB1LENR | USART2EN | 17:17 | 0x20000 | meaning_001 | header:RCC_APB1LENR_USART2EN_Msk |
| APB1LENR | USART3EN | 18:18 | 0x40000 | meaning_001 | header:RCC_APB1LENR_USART3EN_Msk |
| APB1LENR | UART4EN | 19:19 | 0x80000 | meaning_001 | header:RCC_APB1LENR_UART4EN_Msk |
| APB1LENR | UART5EN | 20:20 | 0x100000 | meaning_001 | header:RCC_APB1LENR_UART5EN_Msk |
| APB1LENR | I2C1EN | 21:21 | 0x200000 | meaning_001 | header:RCC_APB1LENR_I2C1EN_Msk |
| APB1LENR | I2C2EN | 22:22 | 0x400000 | meaning_001 | header:RCC_APB1LENR_I2C2EN_Msk |
| APB1LENR | I2C3EN | 23:23 | 0x800000 | meaning_001 | header:RCC_APB1LENR_I2C3EN_Msk |
| APB1LENR | CECEN | 27:27 | 0x8000000 | meaning_001 | header:RCC_APB1LENR_CECEN_Msk |
| APB1LENR | DAC12EN | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB1LENR_DAC12EN_Msk |
| APB1LENR | UART7EN | 30:30 | 0x40000000 | meaning_001 | header:RCC_APB1LENR_UART7EN_Msk |
| APB1LENR | UART8EN | 31:31 | 0x80000000 | meaning_001 | header:RCC_APB1LENR_UART8EN_Msk |
| APB1HENR | CRSEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB1HENR_CRSEN_Msk |
| APB1HENR | SWPMIEN | 2:2 | 0x4 | meaning_001 | header:RCC_APB1HENR_SWPMIEN_Msk |
| APB1HENR | OPAMPEN | 4:4 | 0x10 | meaning_001 | header:RCC_APB1HENR_OPAMPEN_Msk |
| APB1HENR | MDIOSEN | 5:5 | 0x20 | meaning_001 | header:RCC_APB1HENR_MDIOSEN_Msk |
| APB1HENR | FDCANEN | 8:8 | 0x100 | meaning_001 | header:RCC_APB1HENR_FDCANEN_Msk |
| APB2ENR | TIM1EN | 0:0 | 0x1 | meaning_001 | header:RCC_APB2ENR_TIM1EN_Msk |
| APB2ENR | TIM8EN | 1:1 | 0x2 | meaning_001 | header:RCC_APB2ENR_TIM8EN_Msk |
| APB2ENR | USART1EN | 4:4 | 0x10 | meaning_001 | header:RCC_APB2ENR_USART1EN_Msk |
| APB2ENR | USART6EN | 5:5 | 0x20 | meaning_001 | header:RCC_APB2ENR_USART6EN_Msk |
| APB2ENR | SPI1EN | 12:12 | 0x1000 | meaning_001 | header:RCC_APB2ENR_SPI1EN_Msk |
| APB2ENR | SPI4EN | 13:13 | 0x2000 | meaning_001 | header:RCC_APB2ENR_SPI4EN_Msk |
| APB2ENR | TIM15EN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB2ENR_TIM15EN_Msk |
| APB2ENR | TIM16EN | 17:17 | 0x20000 | meaning_001 | header:RCC_APB2ENR_TIM16EN_Msk |
| APB2ENR | TIM17EN | 18:18 | 0x40000 | meaning_001 | header:RCC_APB2ENR_TIM17EN_Msk |
| APB2ENR | SPI5EN | 20:20 | 0x100000 | meaning_001 | header:RCC_APB2ENR_SPI5EN_Msk |
| APB2ENR | SAI1EN | 22:22 | 0x400000 | meaning_001 | header:RCC_APB2ENR_SAI1EN_Msk |
| APB2ENR | SAI2EN | 23:23 | 0x800000 | meaning_001 | header:RCC_APB2ENR_SAI2EN_Msk |
| APB2ENR | SAI3EN | 24:24 | 0x1000000 | meaning_001 | header:RCC_APB2ENR_SAI3EN_Msk |
| APB2ENR | DFSDM1EN | 28:28 | 0x10000000 | meaning_001 | header:RCC_APB2ENR_DFSDM1EN_Msk |
| APB2ENR | HRTIMEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB2ENR_HRTIMEN_Msk |
| APB4ENR | SYSCFGEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB4ENR_SYSCFGEN_Msk |
| APB4ENR | LPUART1EN | 3:3 | 0x8 | meaning_001 | header:RCC_APB4ENR_LPUART1EN_Msk |
| APB4ENR | SPI6EN | 5:5 | 0x20 | meaning_001 | header:RCC_APB4ENR_SPI6EN_Msk |
| APB4ENR | I2C4EN | 7:7 | 0x80 | meaning_001 | header:RCC_APB4ENR_I2C4EN_Msk |
| APB4ENR | LPTIM2EN | 9:9 | 0x200 | meaning_001 | header:RCC_APB4ENR_LPTIM2EN_Msk |
| APB4ENR | LPTIM3EN | 10:10 | 0x400 | meaning_001 | header:RCC_APB4ENR_LPTIM3EN_Msk |
| APB4ENR | LPTIM4EN | 11:11 | 0x800 | meaning_001 | header:RCC_APB4ENR_LPTIM4EN_Msk |
| APB4ENR | LPTIM5EN | 12:12 | 0x1000 | meaning_001 | header:RCC_APB4ENR_LPTIM5EN_Msk |
| APB4ENR | COMP12EN | 14:14 | 0x4000 | meaning_001 | header:RCC_APB4ENR_COMP12EN_Msk |
| APB4ENR | VREFEN | 15:15 | 0x8000 | meaning_001 | header:RCC_APB4ENR_VREFEN_Msk |
| APB4ENR | RTCAPBEN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB4ENR_RTCAPBEN_Msk |
| APB4ENR | SAI4EN | 21:21 | 0x200000 | meaning_001 | header:RCC_APB4ENR_SAI4EN_Msk |
| AHB3LPENR | MDMALPEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB3LPENR_MDMALPEN_Msk |
| AHB3LPENR | DMA2DLPEN | 4:4 | 0x10 | meaning_001 | header:RCC_AHB3LPENR_DMA2DLPEN_Msk |
| AHB3LPENR | JPGDECLPEN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB3LPENR_JPGDECLPEN_Msk |
| AHB3LPENR | FLASHLPEN | 8:8 | 0x100 | meaning_001 | header:RCC_AHB3LPENR_FLASHLPEN_Msk |
| AHB3LPENR | FMCLPEN | 12:12 | 0x1000 | meaning_001 | header:RCC_AHB3LPENR_FMCLPEN_Msk |
| AHB3LPENR | QSPILPEN | 14:14 | 0x4000 | meaning_001 | header:RCC_AHB3LPENR_QSPILPEN_Msk |
| AHB3LPENR | SDMMC1LPEN | 16:16 | 0x10000 | meaning_001 | header:RCC_AHB3LPENR_SDMMC1LPEN_Msk |
| AHB3LPENR | DTCM1LPEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_AHB3LPENR_DTCM1LPEN_Msk |
| AHB3LPENR | DTCM2LPEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_AHB3LPENR_DTCM2LPEN_Msk |
| AHB3LPENR | ITCMLPEN | 30:30 | 0x40000000 | meaning_001 | header:RCC_AHB3LPENR_ITCMLPEN_Msk |
| AHB3LPENR | AXISRAMLPEN | 31:31 | 0x80000000 | meaning_001 | header:RCC_AHB3LPENR_AXISRAMLPEN_Msk |
| AHB1LPENR | DMA1LPEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB1LPENR_DMA1LPEN_Msk |
| AHB1LPENR | DMA2LPEN | 1:1 | 0x2 | meaning_001 | header:RCC_AHB1LPENR_DMA2LPEN_Msk |
| AHB1LPENR | ADC12LPEN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB1LPENR_ADC12LPEN_Msk |
| AHB1LPENR | ETH1MACLPEN | 15:15 | 0x8000 | meaning_001 | header:RCC_AHB1LPENR_ETH1MACLPEN_Msk |
| AHB1LPENR | ETH1TXLPEN | 16:16 | 0x10000 | meaning_001 | header:RCC_AHB1LPENR_ETH1TXLPEN_Msk |
| AHB1LPENR | ETH1RXLPEN | 17:17 | 0x20000 | meaning_001 | header:RCC_AHB1LPENR_ETH1RXLPEN_Msk |
| AHB1LPENR | USB1OTGHSLPEN | 25:25 | 0x2000000 | meaning_001 | header:RCC_AHB1LPENR_USB1OTGHSLPEN_Msk |
| AHB1LPENR | USB1OTGHSULPILPEN | 26:26 | 0x4000000 | meaning_001 | header:RCC_AHB1LPENR_USB1OTGHSULPILPEN_Msk |
| AHB1LPENR | USB2OTGFSLPEN | 27:27 | 0x8000000 | meaning_001 | header:RCC_AHB1LPENR_USB2OTGFSLPEN_Msk |
| AHB1LPENR | USB2OTGFSULPILPEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_AHB1LPENR_USB2OTGFSULPILPEN_Msk |
| AHB2LPENR | DCMILPEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB2LPENR_DCMILPEN_Msk |
| AHB2LPENR | RNGLPEN | 6:6 | 0x40 | meaning_001 | header:RCC_AHB2LPENR_RNGLPEN_Msk |
| AHB2LPENR | SDMMC2LPEN | 9:9 | 0x200 | meaning_001 | header:RCC_AHB2LPENR_SDMMC2LPEN_Msk |
| AHB2LPENR | SRAM1LPEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_AHB2LPENR_SRAM1LPEN_Msk |
| AHB2LPENR | SRAM2LPEN | 30:30 | 0x40000000 | meaning_001 | header:RCC_AHB2LPENR_SRAM2LPEN_Msk |
| AHB2LPENR | SRAM3LPEN | 31:31 | 0x80000000 | meaning_001 | header:RCC_AHB2LPENR_SRAM3LPEN_Msk |
| AHB4LPENR | GPIOALPEN | 0:0 | 0x1 | meaning_001 | header:RCC_AHB4LPENR_GPIOALPEN_Msk |
| AHB4LPENR | GPIOBLPEN | 1:1 | 0x2 | meaning_001 | header:RCC_AHB4LPENR_GPIOBLPEN_Msk |
| AHB4LPENR | GPIOCLPEN | 2:2 | 0x4 | meaning_001 | header:RCC_AHB4LPENR_GPIOCLPEN_Msk |
| AHB4LPENR | GPIODLPEN | 3:3 | 0x8 | meaning_001 | header:RCC_AHB4LPENR_GPIODLPEN_Msk |
| AHB4LPENR | GPIOELPEN | 4:4 | 0x10 | meaning_001 | header:RCC_AHB4LPENR_GPIOELPEN_Msk |
| AHB4LPENR | GPIOFLPEN | 5:5 | 0x20 | meaning_001 | header:RCC_AHB4LPENR_GPIOFLPEN_Msk |
| AHB4LPENR | GPIOGLPEN | 6:6 | 0x40 | meaning_001 | header:RCC_AHB4LPENR_GPIOGLPEN_Msk |
| AHB4LPENR | GPIOHLPEN | 7:7 | 0x80 | meaning_001 | header:RCC_AHB4LPENR_GPIOHLPEN_Msk |
| AHB4LPENR | GPIOILPEN | 8:8 | 0x100 | meaning_001 | header:RCC_AHB4LPENR_GPIOILPEN_Msk |
| AHB4LPENR | GPIOJLPEN | 9:9 | 0x200 | meaning_001 | header:RCC_AHB4LPENR_GPIOJLPEN_Msk |
| AHB4LPENR | GPIOKLPEN | 10:10 | 0x400 | meaning_001 | header:RCC_AHB4LPENR_GPIOKLPEN_Msk |
| AHB4LPENR | CRCLPEN | 19:19 | 0x80000 | meaning_001 | header:RCC_AHB4LPENR_CRCLPEN_Msk |
| AHB4LPENR | BDMALPEN | 21:21 | 0x200000 | meaning_001 | header:RCC_AHB4LPENR_BDMALPEN_Msk |
| AHB4LPENR | ADC3LPEN | 24:24 | 0x1000000 | meaning_001 | header:RCC_AHB4LPENR_ADC3LPEN_Msk |
| AHB4LPENR | BKPRAMLPEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_AHB4LPENR_BKPRAMLPEN_Msk |
| AHB4LPENR | SRAM4LPEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_AHB4LPENR_SRAM4LPEN_Msk |
| APB3LPENR | LTDCLPEN | 3:3 | 0x8 | meaning_001 | header:RCC_APB3LPENR_LTDCLPEN_Msk |
| APB3LPENR | WWDG1LPEN | 6:6 | 0x40 | meaning_001 | header:RCC_APB3LPENR_WWDG1LPEN_Msk |
| APB1LLPENR | TIM2LPEN | 0:0 | 0x1 | meaning_001 | header:RCC_APB1LLPENR_TIM2LPEN_Msk |
| APB1LLPENR | TIM3LPEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB1LLPENR_TIM3LPEN_Msk |
| APB1LLPENR | TIM4LPEN | 2:2 | 0x4 | meaning_001 | header:RCC_APB1LLPENR_TIM4LPEN_Msk |
| APB1LLPENR | TIM5LPEN | 3:3 | 0x8 | meaning_001 | header:RCC_APB1LLPENR_TIM5LPEN_Msk |
| APB1LLPENR | TIM6LPEN | 4:4 | 0x10 | meaning_001 | header:RCC_APB1LLPENR_TIM6LPEN_Msk |
| APB1LLPENR | TIM7LPEN | 5:5 | 0x20 | meaning_001 | header:RCC_APB1LLPENR_TIM7LPEN_Msk |
| APB1LLPENR | TIM12LPEN | 6:6 | 0x40 | meaning_001 | header:RCC_APB1LLPENR_TIM12LPEN_Msk |
| APB1LLPENR | TIM13LPEN | 7:7 | 0x80 | meaning_001 | header:RCC_APB1LLPENR_TIM13LPEN_Msk |
| APB1LLPENR | TIM14LPEN | 8:8 | 0x100 | meaning_001 | header:RCC_APB1LLPENR_TIM14LPEN_Msk |
| APB1LLPENR | LPTIM1LPEN | 9:9 | 0x200 | meaning_001 | header:RCC_APB1LLPENR_LPTIM1LPEN_Msk |
| APB1LLPENR | SPI2LPEN | 14:14 | 0x4000 | meaning_001 | header:RCC_APB1LLPENR_SPI2LPEN_Msk |
| APB1LLPENR | SPI3LPEN | 15:15 | 0x8000 | meaning_001 | header:RCC_APB1LLPENR_SPI3LPEN_Msk |
| APB1LLPENR | SPDIFRXLPEN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB1LLPENR_SPDIFRXLPEN_Msk |
| APB1LLPENR | USART2LPEN | 17:17 | 0x20000 | meaning_001 | header:RCC_APB1LLPENR_USART2LPEN_Msk |
| APB1LLPENR | USART3LPEN | 18:18 | 0x40000 | meaning_001 | header:RCC_APB1LLPENR_USART3LPEN_Msk |
| APB1LLPENR | UART4LPEN | 19:19 | 0x80000 | meaning_001 | header:RCC_APB1LLPENR_UART4LPEN_Msk |
| APB1LLPENR | UART5LPEN | 20:20 | 0x100000 | meaning_001 | header:RCC_APB1LLPENR_UART5LPEN_Msk |
| APB1LLPENR | I2C1LPEN | 21:21 | 0x200000 | meaning_001 | header:RCC_APB1LLPENR_I2C1LPEN_Msk |
| APB1LLPENR | I2C2LPEN | 22:22 | 0x400000 | meaning_001 | header:RCC_APB1LLPENR_I2C2LPEN_Msk |
| APB1LLPENR | I2C3LPEN | 23:23 | 0x800000 | meaning_001 | header:RCC_APB1LLPENR_I2C3LPEN_Msk |
| APB1LLPENR | CECLPEN | 27:27 | 0x8000000 | meaning_001 | header:RCC_APB1LLPENR_CECLPEN_Msk |
| APB1LLPENR | DAC12LPEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB1LLPENR_DAC12LPEN_Msk |
| APB1LLPENR | UART7LPEN | 30:30 | 0x40000000 | meaning_001 | header:RCC_APB1LLPENR_UART7LPEN_Msk |
| APB1LLPENR | UART8LPEN | 31:31 | 0x80000000 | meaning_001 | header:RCC_APB1LLPENR_UART8LPEN_Msk |
| APB1HLPENR | CRSLPEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB1HLPENR_CRSLPEN_Msk |
| APB1HLPENR | SWPMILPEN | 2:2 | 0x4 | meaning_001 | header:RCC_APB1HLPENR_SWPMILPEN_Msk |
| APB1HLPENR | OPAMPLPEN | 4:4 | 0x10 | meaning_001 | header:RCC_APB1HLPENR_OPAMPLPEN_Msk |
| APB1HLPENR | MDIOSLPEN | 5:5 | 0x20 | meaning_001 | header:RCC_APB1HLPENR_MDIOSLPEN_Msk |
| APB1HLPENR | FDCANLPEN | 8:8 | 0x100 | meaning_001 | header:RCC_APB1HLPENR_FDCANLPEN_Msk |
| APB2LPENR | TIM1LPEN | 0:0 | 0x1 | meaning_001 | header:RCC_APB2LPENR_TIM1LPEN_Msk |
| APB2LPENR | TIM8LPEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB2LPENR_TIM8LPEN_Msk |
| APB2LPENR | USART1LPEN | 4:4 | 0x10 | meaning_001 | header:RCC_APB2LPENR_USART1LPEN_Msk |
| APB2LPENR | USART6LPEN | 5:5 | 0x20 | meaning_001 | header:RCC_APB2LPENR_USART6LPEN_Msk |
| APB2LPENR | SPI1LPEN | 12:12 | 0x1000 | meaning_001 | header:RCC_APB2LPENR_SPI1LPEN_Msk |
| APB2LPENR | SPI4LPEN | 13:13 | 0x2000 | meaning_001 | header:RCC_APB2LPENR_SPI4LPEN_Msk |
| APB2LPENR | TIM15LPEN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB2LPENR_TIM15LPEN_Msk |
| APB2LPENR | TIM16LPEN | 17:17 | 0x20000 | meaning_001 | header:RCC_APB2LPENR_TIM16LPEN_Msk |
| APB2LPENR | TIM17LPEN | 18:18 | 0x40000 | meaning_001 | header:RCC_APB2LPENR_TIM17LPEN_Msk |
| APB2LPENR | SPI5LPEN | 20:20 | 0x100000 | meaning_001 | header:RCC_APB2LPENR_SPI5LPEN_Msk |
| APB2LPENR | SAI1LPEN | 22:22 | 0x400000 | meaning_001 | header:RCC_APB2LPENR_SAI1LPEN_Msk |
| APB2LPENR | SAI2LPEN | 23:23 | 0x800000 | meaning_001 | header:RCC_APB2LPENR_SAI2LPEN_Msk |
| APB2LPENR | SAI3LPEN | 24:24 | 0x1000000 | meaning_001 | header:RCC_APB2LPENR_SAI3LPEN_Msk |
| APB2LPENR | DFSDM1LPEN | 28:28 | 0x10000000 | meaning_001 | header:RCC_APB2LPENR_DFSDM1LPEN_Msk |
| APB2LPENR | HRTIMLPEN | 29:29 | 0x20000000 | meaning_001 | header:RCC_APB2LPENR_HRTIMLPEN_Msk |
| APB4LPENR | SYSCFGLPEN | 1:1 | 0x2 | meaning_001 | header:RCC_APB4LPENR_SYSCFGLPEN_Msk |
| APB4LPENR | LPUART1LPEN | 3:3 | 0x8 | meaning_001 | header:RCC_APB4LPENR_LPUART1LPEN_Msk |
| APB4LPENR | SPI6LPEN | 5:5 | 0x20 | meaning_001 | header:RCC_APB4LPENR_SPI6LPEN_Msk |
| APB4LPENR | I2C4LPEN | 7:7 | 0x80 | meaning_001 | header:RCC_APB4LPENR_I2C4LPEN_Msk |
| APB4LPENR | LPTIM2LPEN | 9:9 | 0x200 | meaning_001 | header:RCC_APB4LPENR_LPTIM2LPEN_Msk |
| APB4LPENR | LPTIM3LPEN | 10:10 | 0x400 | meaning_001 | header:RCC_APB4LPENR_LPTIM3LPEN_Msk |
| APB4LPENR | LPTIM4LPEN | 11:11 | 0x800 | meaning_001 | header:RCC_APB4LPENR_LPTIM4LPEN_Msk |
| APB4LPENR | LPTIM5LPEN | 12:12 | 0x1000 | meaning_001 | header:RCC_APB4LPENR_LPTIM5LPEN_Msk |
| APB4LPENR | COMP12LPEN | 14:14 | 0x4000 | meaning_001 | header:RCC_APB4LPENR_COMP12LPEN_Msk |
| APB4LPENR | VREFLPEN | 15:15 | 0x8000 | meaning_001 | header:RCC_APB4LPENR_VREFLPEN_Msk |
| APB4LPENR | RTCAPBLPEN | 16:16 | 0x10000 | meaning_001 | header:RCC_APB4LPENR_RTCAPBLPEN_Msk |
| APB4LPENR | SAI4LPEN | 21:21 | 0x200000 | meaning_001 | header:RCC_APB4LPENR_SAI4LPEN_Msk |

### Meaning references

Each Meaning identifier resolves to its complete text below; no fields or operating facts were omitted.

| Identifier | Complete meaning |
| --- | --- |
| meaning_001 | Declaration only; encoding requires reviewed semantics. |

## Operating semantics unavailable

**rcc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
