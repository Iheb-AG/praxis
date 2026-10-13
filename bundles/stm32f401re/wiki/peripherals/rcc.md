# RCC: HSI clock and bus gates

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RCC | 0x40023800 | AHB1 | HSI16 | header:instance:RCC; rcc_review:clock:RCC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | mixed | 0x83 | Ready flags are read-only; preserve calibration/reserved bits. | header:register:CR; rcc_review:register:CR |
| CFGR | 0x008 | 32 | — | mixed | 0x0 | SWS reflects selected source; wait after changing SW. | header:register:CFGR; rcc_review:register:CFGR |
| APB1RSTR | 0x020 | 32 | — | RW | 0x0 | Pulse only the required reset bit; clear it before use. | header:register:APB1RSTR; rcc_review:register:APB1RSTR |
| AHB1ENR | 0x030 | 32 | — | RW | 0x0 | Read back after enabling a clock before peripheral access. | header:register:AHB1ENR; rcc_review:register:AHB1ENR |
| APB1ENR | 0x040 | 32 | — | RW | 0x0 | Read back before accessing the newly enabled peripheral. | header:register:APB1ENR; rcc_review:register:APB1ENR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | HSION | 0:0 | 0x1 | 1 enables HSI16 | rcc_review:field:HSION |
| CR | HSIRDY | 1:1 | 0x2 | Wait until 1 with timeout | rcc_review:field:HSIRDY |
| CR | HSITRIM | 7:3 | 0xF8 | Factory default trim 16 | rcc_review:field:HSITRIM |
| CR | HSICAL | 15:8 | 0xFF00 | Read-only factory calibration | rcc_review:field:HSICAL |
| CR | HSEON | 16:16 | 0x10000 | External oscillator enable; not used by fixture | rcc_review:field:HSEON |
| CR | HSERDY | 17:17 | 0x20000 | HSE ready | rcc_review:field:HSERDY |
| CR | HSEBYP | 18:18 | 0x40000 | HSE bypass | rcc_review:field:HSEBYP |
| CR | CSSON | 19:19 | 0x80000 | Clock security | rcc_review:field:CSSON |
| CR | PLLON | 24:24 | 0x1000000 | PLL enable | rcc_review:field:PLLON |
| CR | PLLRDY | 25:25 | 0x2000000 | PLL ready | rcc_review:field:PLLRDY |
| CR | PLLI2SON | 26:26 | 0x4000000 | PLLI2S enable | rcc_review:field:PLLI2SON |
| CR | PLLI2SRDY | 27:27 | 0x8000000 | PLLI2S ready | rcc_review:field:PLLI2SRDY |
| CFGR | SW | 1:0 | 0x3 | 00 HSI; 01 HSE; 10 PLL | rcc_review:field:SW |
| CFGR | SWS | 3:2 | 0xC | Read-only active source | rcc_review:field:SWS |
| CFGR | HPRE | 7:4 | 0xF0 | 0xxx /1; 1000 /2; see manual for other divisors | rcc_review:field:HPRE |
| CFGR | PPRE1 | 12:10 | 0x1C00 | 0xx /1; 100 /2; 101 /4; 110 /8; 111 /16 | rcc_review:field:PPRE1 |
| CFGR | PPRE2 | 15:13 | 0xE000 | Same encoding as PPRE1 | rcc_review:field:PPRE2 |
| CFGR | RTCPRE | 20:16 | 0x1F0000 | RTC HSE division | rcc_review:field:RTCPRE |
| CFGR | MCO1 | 22:21 | 0x600000 | Clock output source | rcc_review:field:MCO1 |
| CFGR | I2SSRC | 23:23 | 0x800000 | I2S source | rcc_review:field:I2SSRC |
| CFGR | MCO1PRE | 26:24 | 0x7000000 | MCO1 division | rcc_review:field:MCO1PRE |
| CFGR | MCO2PRE | 29:27 | 0x38000000 | MCO2 division | rcc_review:field:MCO2PRE |
| CFGR | MCO2 | 31:30 | 0xC0000000 | MCO2 source | rcc_review:field:MCO2 |
| APB1RSTR | USART2RST | 17:17 | 0x20000 | 1 holds USART2 in reset | rcc_review:field:USART2RST |
| AHB1ENR | GPIOAEN | 0:0 | 0x1 | 1 enables port clock | rcc_review:field:GPIOAEN |
| AHB1ENR | GPIOBEN | 1:1 | 0x2 | 1 enables port clock | rcc_review:field:GPIOBEN |
| AHB1ENR | GPIOCEN | 2:2 | 0x4 | 1 enables port clock | rcc_review:field:GPIOCEN |
| AHB1ENR | GPIODEN | 3:3 | 0x8 | 1 enables port clock | rcc_review:field:GPIODEN |
| AHB1ENR | GPIOEEN | 4:4 | 0x10 | 1 enables port clock | rcc_review:field:GPIOEEN |
| AHB1ENR | GPIOHEN | 7:7 | 0x80 | GPIOH gate | rcc_review:field:GPIOHEN |
| AHB1ENR | CRCEN | 12:12 | 0x1000 | CRC gate | rcc_review:field:CRCEN |
| AHB1ENR | DMA1EN | 21:21 | 0x200000 | DMA1 gate | rcc_review:field:DMA1EN |
| AHB1ENR | DMA2EN | 22:22 | 0x400000 | DMA2 gate | rcc_review:field:DMA2EN |
| APB1ENR | TIM2EN | 0:0 | 0x1 | Timer gate | rcc_review:field:TIM2EN |
| APB1ENR | TIM3EN | 1:1 | 0x2 | Timer gate | rcc_review:field:TIM3EN |
| APB1ENR | TIM4EN | 2:2 | 0x4 | Timer gate | rcc_review:field:TIM4EN |
| APB1ENR | TIM5EN | 3:3 | 0x8 | Timer gate | rcc_review:field:TIM5EN |
| APB1ENR | WWDGEN | 11:11 | 0x800 | Window watchdog gate | rcc_review:field:WWDGEN |
| APB1ENR | SPI2EN | 14:14 | 0x4000 | SPI2 gate | rcc_review:field:SPI2EN |
| APB1ENR | SPI3EN | 15:15 | 0x8000 | SPI3 gate | rcc_review:field:SPI3EN |
| APB1ENR | USART2EN | 17:17 | 0x20000 | USART2 PCLK1 gate | rcc_review:field:USART2EN |
| APB1ENR | I2C1EN | 21:21 | 0x200000 | I2C1 gate | rcc_review:field:I2C1EN |
| APB1ENR | I2C2EN | 22:22 | 0x400000 | I2C2 gate | rcc_review:field:I2C2EN |
| APB1ENR | I2C3EN | 23:23 | 0x800000 | I2C3 gate | rcc_review:field:I2C3EN |
| APB1ENR | PWREN | 28:28 | 0x10000000 | Power control gate | rcc_review:field:PWREN |

## Reviewed operating semantics

Supported scope: HSI16-based USART2 bring-up; this is not a complete PLL/power-mode guide.

1. Keep interrupts masked; set HSION and wait for HSIRDY with a finite timeout.
2. Select SW=00, wait for SWS=00, and use HPRE=/1, PPRE1=/1, PPRE2=/1 only after active peripherals are quiescent.
3. The fixture assumes SYSCLK=HCLK=PCLK1=PCLK2=16,000,000 Hz. APB1 must never exceed 42 MHz; SYSCLK/HCLK max is 84 MHz.
4. Enable GPIOAEN and USART2EN and read back the enable registers before access. USART2 uses PCLK1; timer clock doubling does not apply to USART.
5. Pulse USART2RST only when resetting this peripheral is intended. Preserve other gates and reserved fields.

Physical supply stabilization, decoupling, FLASH latency, and voltage scaling are board/startup responsibilities. No PLL increase is performed here. DMA1EN is needed before any future DMA stream access.

Continue to [[peripherals/gpio]], then [[peripherals/usart]]. Source: [RM0368, RCC chapter](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf).

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
