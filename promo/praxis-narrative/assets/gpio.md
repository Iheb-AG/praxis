# GPIO: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| GPIOA | 0x40020000 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOA_BASE; gpio_review:instance:GPIOA |
| GPIOB | 0x40020400 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOB_BASE; gpio_review:instance:GPIOB |
| GPIOC | 0x40020800 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOC_BASE; gpio_review:instance:GPIOC |
| GPIOD | 0x40020C00 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOD_BASE; gpio_review:instance:GPIOD |
| GPIOE | 0x40021000 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOE_BASE; gpio_review:instance:GPIOE |
| GPIOF | 0x40021400 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOF_BASE; gpio_review:instance:GPIOF |
| GPIOG | 0x40021800 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOG_BASE; gpio_review:instance:GPIOG |
| GPIOH | 0x40021C00 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOH_BASE; gpio_review:instance:GPIOH |
| GPIOI | 0x40022000 | AHB1 | HCLK=168 MHz; instance gate required; package pins need review | header:GPIOI_BASE; gpio_review:instance:GPIOI |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MODER | 0x000 | 32 | — | RW | not asserted | Preserve SWD/debug pins. | header:GPIO_TypeDef.MODER; gpio_review:MODER; rm_can_rx_283:page:283; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:283 | 32 |
| OTYPER | 0x004 | 32 | — | RW | not asserted | Upper 16 bits reserved. | header:GPIO_TypeDef.OTYPER; gpio_review:OTYPER; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:283 | 32 |
| OSPEEDR | 0x008 | 32 | — | RW | not asserted | Choose slew rate for the board signal. | header:GPIO_TypeDef.OSPEEDR; gpio_review:OSPEEDR; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:284 | 32 |
| PUPDR | 0x00C | 32 | — | RW | not asserted | 11 encoding is reserved. | header:GPIO_TypeDef.PUPDR; gpio_review:PUPDR; rm_can_rx_285:page:285; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:285 | 32 |
| IDR | 0x010 | 32 | — | RO | not asserted | Sampled input; no read-to-clear. | header:GPIO_TypeDef.IDR; gpio_review:IDR; rm_can_rx_285:page:285 | 32 |
| ODR | 0x014 | 32 | — | RW | not asserted | Use BSRR for atomic pin changes. | header:GPIO_TypeDef.ODR; gpio_review:ODR | not asserted |
| BSRR | 0x018 | 32 | — | WO | not asserted | Write ones to set/reset; never read-modify-write. | header:GPIO_TypeDef.BSRR; gpio_review:BSRR; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:286 | 32 |
| LCKR | 0x01C | 32 | — | RW | not asserted | Lock sequence is deliberate; fixture leaves pins unlocked. | header:GPIO_TypeDef.LCKR; gpio_review:LCKR; rm_can_rx_287:page:287; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:287 | 32 |
| AFRL | 0x020 | 32 | — | RW | not asserted | Write selected four-bit field; preserve adjacent pins. | header:GPIO_TypeDef.AFR[0]; compilation_policy:member_views.gpio.AFR; gpio_review:AFRL; rm_can_rx_287:page:287; timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:288 | 32 |
| AFRH | 0x024 | 32 | — | RW | not asserted | Pins 8–15 use this register. | header:GPIO_TypeDef.AFR[1]; compilation_policy:member_views.gpio.AFR; gpio_review:AFRH | not asserted |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MODER | MODER0 | 1:0 | 0x3 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER0_Msk; gpio_review:MODER.MODER0 |
| MODER | MODER1 | 3:2 | 0xC | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER1_Msk; gpio_review:MODER.MODER1; timer_routes_evidence:rm0090/page:283 |
| MODER | MODER2 | 5:4 | 0x30 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER2_Msk; gpio_review:MODER.MODER2; timer_routes_evidence:rm0090/page:283 |
| MODER | MODER3 | 7:6 | 0xC0 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER3_Msk; gpio_review:MODER.MODER3 |
| MODER | MODER4 | 9:8 | 0x300 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER4_Msk; gpio_review:MODER.MODER4 |
| MODER | MODER5 | 11:10 | 0xC00 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER5_Msk; gpio_review:MODER.MODER5 |
| MODER | MODER6 | 13:12 | 0x3000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER6_Msk; gpio_review:MODER.MODER6 |
| MODER | MODER7 | 15:14 | 0xC000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER7_Msk; gpio_review:MODER.MODER7 |
| MODER | MODER8 | 17:16 | 0x30000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER8_Msk; gpio_review:MODER.MODER8 |
| MODER | MODER9 | 19:18 | 0xC0000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER9_Msk; gpio_review:MODER.MODER9 |
| MODER | MODER10 | 21:20 | 0x300000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER10_Msk; gpio_review:MODER.MODER10 |
| MODER | MODER11 | 23:22 | 0xC00000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER11_Msk; gpio_review:MODER.MODER11 |
| MODER | MODER12 | 25:24 | 0x3000000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER12_Msk; gpio_review:MODER.MODER12 |
| MODER | MODER13 | 27:26 | 0xC000000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER13_Msk; gpio_review:MODER.MODER13 |
| MODER | MODER14 | 29:28 | 0x30000000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER14_Msk; gpio_review:MODER.MODER14 |
| MODER | MODER15 | 31:30 | 0xC0000000 | 00 input; 01 output; 10 alternate function; 11 analog | header:GPIO_MODER_MODER15_Msk; gpio_review:MODER.MODER15 |
| OTYPER | OT0 | 0:0 | 0x1 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT0_Msk; gpio_review:OTYPER.OT0 |
| OTYPER | OT1 | 1:1 | 0x2 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT1_Msk; gpio_review:OTYPER.OT1; timer_routes_evidence:rm0090/page:283 |
| OTYPER | OT2 | 2:2 | 0x4 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT2_Msk; gpio_review:OTYPER.OT2; timer_routes_evidence:rm0090/page:283 |
| OTYPER | OT3 | 3:3 | 0x8 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT3_Msk; gpio_review:OTYPER.OT3 |
| OTYPER | OT4 | 4:4 | 0x10 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT4_Msk; gpio_review:OTYPER.OT4 |
| OTYPER | OT5 | 5:5 | 0x20 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT5_Msk; gpio_review:OTYPER.OT5 |
| OTYPER | OT6 | 6:6 | 0x40 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT6_Msk; gpio_review:OTYPER.OT6 |
| OTYPER | OT7 | 7:7 | 0x80 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT7_Msk; gpio_review:OTYPER.OT7 |
| OTYPER | OT8 | 8:8 | 0x100 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT8_Msk; gpio_review:OTYPER.OT8 |
| OTYPER | OT9 | 9:9 | 0x200 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT9_Msk; gpio_review:OTYPER.OT9 |
| OTYPER | OT10 | 10:10 | 0x400 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT10_Msk; gpio_review:OTYPER.OT10 |
| OTYPER | OT11 | 11:11 | 0x800 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT11_Msk; gpio_review:OTYPER.OT11 |
| OTYPER | OT12 | 12:12 | 0x1000 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT12_Msk; gpio_review:OTYPER.OT12 |
| OTYPER | OT13 | 13:13 | 0x2000 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT13_Msk; gpio_review:OTYPER.OT13 |
| OTYPER | OT14 | 14:14 | 0x4000 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT14_Msk; gpio_review:OTYPER.OT14 |
| OTYPER | OT15 | 15:15 | 0x8000 | 0 push-pull; 1 open-drain | header:GPIO_OTYPER_OT15_Msk; gpio_review:OTYPER.OT15 |
| OSPEEDR | OSPEED0 | 1:0 | 0x3 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED0_Msk; gpio_review:OSPEEDR.OSPEED0 |
| OSPEEDR | OSPEED1 | 3:2 | 0xC | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED1_Msk; gpio_review:OSPEEDR.OSPEED1; timer_routes_evidence:rm0090/page:284 |
| OSPEEDR | OSPEED2 | 5:4 | 0x30 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED2_Msk; gpio_review:OSPEEDR.OSPEED2; timer_routes_evidence:rm0090/page:284 |
| OSPEEDR | OSPEED3 | 7:6 | 0xC0 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED3_Msk; gpio_review:OSPEEDR.OSPEED3 |
| OSPEEDR | OSPEED4 | 9:8 | 0x300 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED4_Msk; gpio_review:OSPEEDR.OSPEED4 |
| OSPEEDR | OSPEED5 | 11:10 | 0xC00 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED5_Msk; gpio_review:OSPEEDR.OSPEED5 |
| OSPEEDR | OSPEED6 | 13:12 | 0x3000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED6_Msk; gpio_review:OSPEEDR.OSPEED6 |
| OSPEEDR | OSPEED7 | 15:14 | 0xC000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED7_Msk; gpio_review:OSPEEDR.OSPEED7 |
| OSPEEDR | OSPEED8 | 17:16 | 0x30000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED8_Msk; gpio_review:OSPEEDR.OSPEED8 |
| OSPEEDR | OSPEED9 | 19:18 | 0xC0000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED9_Msk; gpio_review:OSPEEDR.OSPEED9 |
| OSPEEDR | OSPEED10 | 21:20 | 0x300000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED10_Msk; gpio_review:OSPEEDR.OSPEED10 |
| OSPEEDR | OSPEED11 | 23:22 | 0xC00000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED11_Msk; gpio_review:OSPEEDR.OSPEED11 |
| OSPEEDR | OSPEED12 | 25:24 | 0x3000000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED12_Msk; gpio_review:OSPEEDR.OSPEED12 |
| OSPEEDR | OSPEED13 | 27:26 | 0xC000000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED13_Msk; gpio_review:OSPEEDR.OSPEED13 |
| OSPEEDR | OSPEED14 | 29:28 | 0x30000000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED14_Msk; gpio_review:OSPEEDR.OSPEED14 |
| OSPEEDR | OSPEED15 | 31:30 | 0xC0000000 | 00 low; 01 medium; 10 fast; 11 high | header:GPIO_OSPEEDR_OSPEED15_Msk; gpio_review:OSPEEDR.OSPEED15 |
| PUPDR | PUPD0 | 1:0 | 0x3 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD0_Msk; gpio_review:PUPDR.PUPD0 |
| PUPDR | PUPD1 | 3:2 | 0xC | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD1_Msk; gpio_review:PUPDR.PUPD1; timer_routes_evidence:rm0090/page:285 |
| PUPDR | PUPD2 | 5:4 | 0x30 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD2_Msk; gpio_review:PUPDR.PUPD2; timer_routes_evidence:rm0090/page:285 |
| PUPDR | PUPD3 | 7:6 | 0xC0 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD3_Msk; gpio_review:PUPDR.PUPD3 |
| PUPDR | PUPD4 | 9:8 | 0x300 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD4_Msk; gpio_review:PUPDR.PUPD4 |
| PUPDR | PUPD5 | 11:10 | 0xC00 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD5_Msk; gpio_review:PUPDR.PUPD5 |
| PUPDR | PUPD6 | 13:12 | 0x3000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD6_Msk; gpio_review:PUPDR.PUPD6 |
| PUPDR | PUPD7 | 15:14 | 0xC000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD7_Msk; gpio_review:PUPDR.PUPD7 |
| PUPDR | PUPD8 | 17:16 | 0x30000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD8_Msk; gpio_review:PUPDR.PUPD8 |
| PUPDR | PUPD9 | 19:18 | 0xC0000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD9_Msk; gpio_review:PUPDR.PUPD9 |
| PUPDR | PUPD10 | 21:20 | 0x300000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD10_Msk; gpio_review:PUPDR.PUPD10 |
| PUPDR | PUPD11 | 23:22 | 0xC00000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD11_Msk; gpio_review:PUPDR.PUPD11 |
| PUPDR | PUPD12 | 25:24 | 0x3000000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD12_Msk; gpio_review:PUPDR.PUPD12 |
| PUPDR | PUPD13 | 27:26 | 0xC000000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD13_Msk; gpio_review:PUPDR.PUPD13 |
| PUPDR | PUPD14 | 29:28 | 0x30000000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD14_Msk; gpio_review:PUPDR.PUPD14 |
| PUPDR | PUPD15 | 31:30 | 0xC0000000 | 00 none; 01 pull-up; 10 pull-down | header:GPIO_PUPDR_PUPD15_Msk; gpio_review:PUPDR.PUPD15 |
| IDR | ID0 | 0:0 | 0x1 | Input sample | header:GPIO_IDR_ID0_Msk; gpio_review:IDR.ID0 |
| IDR | ID1 | 1:1 | 0x2 | Input sample | header:GPIO_IDR_ID1_Msk; gpio_review:IDR.ID1 |
| IDR | ID2 | 2:2 | 0x4 | Input sample | header:GPIO_IDR_ID2_Msk; gpio_review:IDR.ID2 |
| IDR | ID3 | 3:3 | 0x8 | Input sample | header:GPIO_IDR_ID3_Msk; gpio_review:IDR.ID3 |
| IDR | ID4 | 4:4 | 0x10 | Input sample | header:GPIO_IDR_ID4_Msk; gpio_review:IDR.ID4 |
| IDR | ID5 | 5:5 | 0x20 | Input sample | header:GPIO_IDR_ID5_Msk; gpio_review:IDR.ID5 |
| IDR | ID6 | 6:6 | 0x40 | Input sample | header:GPIO_IDR_ID6_Msk; gpio_review:IDR.ID6 |
| IDR | ID7 | 7:7 | 0x80 | Input sample | header:GPIO_IDR_ID7_Msk; gpio_review:IDR.ID7 |
| IDR | ID8 | 8:8 | 0x100 | Input sample | header:GPIO_IDR_ID8_Msk; gpio_review:IDR.ID8 |
| IDR | ID9 | 9:9 | 0x200 | Input sample | header:GPIO_IDR_ID9_Msk; gpio_review:IDR.ID9 |
| IDR | ID10 | 10:10 | 0x400 | Input sample | header:GPIO_IDR_ID10_Msk; gpio_review:IDR.ID10 |
| IDR | ID11 | 11:11 | 0x800 | Input sample | header:GPIO_IDR_ID11_Msk; gpio_review:IDR.ID11 |
| IDR | ID12 | 12:12 | 0x1000 | Input sample | header:GPIO_IDR_ID12_Msk; gpio_review:IDR.ID12 |
| IDR | ID13 | 13:13 | 0x2000 | Input sample | header:GPIO_IDR_ID13_Msk; gpio_review:IDR.ID13 |
| IDR | ID14 | 14:14 | 0x4000 | Input sample | header:GPIO_IDR_ID14_Msk; gpio_review:IDR.ID14 |
| IDR | ID15 | 15:15 | 0x8000 | Input sample | header:GPIO_IDR_ID15_Msk; gpio_review:IDR.ID15 |
| ODR | OD0 | 0:0 | 0x1 | Output latch | header:GPIO_ODR_OD0_Msk; gpio_review:ODR.OD0 |
| ODR | OD1 | 1:1 | 0x2 | Output latch | header:GPIO_ODR_OD1_Msk; gpio_review:ODR.OD1 |
| ODR | OD2 | 2:2 | 0x4 | Output latch | header:GPIO_ODR_OD2_Msk; gpio_review:ODR.OD2 |
| ODR | OD3 | 3:3 | 0x8 | Output latch | header:GPIO_ODR_OD3_Msk; gpio_review:ODR.OD3 |
| ODR | OD4 | 4:4 | 0x10 | Output latch | header:GPIO_ODR_OD4_Msk; gpio_review:ODR.OD4 |
| ODR | OD5 | 5:5 | 0x20 | Output latch | header:GPIO_ODR_OD5_Msk; gpio_review:ODR.OD5 |
| ODR | OD6 | 6:6 | 0x40 | Output latch | header:GPIO_ODR_OD6_Msk; gpio_review:ODR.OD6 |
| ODR | OD7 | 7:7 | 0x80 | Output latch | header:GPIO_ODR_OD7_Msk; gpio_review:ODR.OD7 |
| ODR | OD8 | 8:8 | 0x100 | Output latch | header:GPIO_ODR_OD8_Msk; gpio_review:ODR.OD8 |
| ODR | OD9 | 9:9 | 0x200 | Output latch | header:GPIO_ODR_OD9_Msk; gpio_review:ODR.OD9 |
| ODR | OD10 | 10:10 | 0x400 | Output latch | header:GPIO_ODR_OD10_Msk; gpio_review:ODR.OD10 |
| ODR | OD11 | 11:11 | 0x800 | Output latch | header:GPIO_ODR_OD11_Msk; gpio_review:ODR.OD11 |
| ODR | OD12 | 12:12 | 0x1000 | Output latch | header:GPIO_ODR_OD12_Msk; gpio_review:ODR.OD12 |
| ODR | OD13 | 13:13 | 0x2000 | Output latch | header:GPIO_ODR_OD13_Msk; gpio_review:ODR.OD13 |
| ODR | OD14 | 14:14 | 0x4000 | Output latch | header:GPIO_ODR_OD14_Msk; gpio_review:ODR.OD14 |
| ODR | OD15 | 15:15 | 0x8000 | Output latch | header:GPIO_ODR_OD15_Msk; gpio_review:ODR.OD15 |
| BSRR | BS0 | 0:0 | 0x1 | Write 1 sets output | header:GPIO_BSRR_BS0_Msk; gpio_review:BSRR.BS0 |
| BSRR | BS1 | 1:1 | 0x2 | Write 1 sets output | header:GPIO_BSRR_BS1_Msk; gpio_review:BSRR.BS1 |
| BSRR | BS2 | 2:2 | 0x4 | Write 1 sets output | header:GPIO_BSRR_BS2_Msk; gpio_review:BSRR.BS2 |
| BSRR | BS3 | 3:3 | 0x8 | Write 1 sets output | header:GPIO_BSRR_BS3_Msk; gpio_review:BSRR.BS3 |
| BSRR | BS4 | 4:4 | 0x10 | Write 1 sets output | header:GPIO_BSRR_BS4_Msk; gpio_review:BSRR.BS4 |
| BSRR | BS5 | 5:5 | 0x20 | Write 1 sets output | header:GPIO_BSRR_BS5_Msk; gpio_review:BSRR.BS5 |
| BSRR | BS6 | 6:6 | 0x40 | Write 1 sets output | header:GPIO_BSRR_BS6_Msk; gpio_review:BSRR.BS6 |
| BSRR | BS7 | 7:7 | 0x80 | Write 1 sets output | header:GPIO_BSRR_BS7_Msk; gpio_review:BSRR.BS7 |
| BSRR | BS8 | 8:8 | 0x100 | Write 1 sets output | header:GPIO_BSRR_BS8_Msk; gpio_review:BSRR.BS8 |
| BSRR | BS9 | 9:9 | 0x200 | Write 1 sets output | header:GPIO_BSRR_BS9_Msk; gpio_review:BSRR.BS9 |
| BSRR | BS10 | 10:10 | 0x400 | Write 1 sets output | header:GPIO_BSRR_BS10_Msk; gpio_review:BSRR.BS10 |
| BSRR | BS11 | 11:11 | 0x800 | Write 1 sets output | header:GPIO_BSRR_BS11_Msk; gpio_review:BSRR.BS11 |
| BSRR | BS12 | 12:12 | 0x1000 | Write 1 sets output | header:GPIO_BSRR_BS12_Msk; gpio_review:BSRR.BS12 |
| BSRR | BS13 | 13:13 | 0x2000 | Write 1 sets output | header:GPIO_BSRR_BS13_Msk; gpio_review:BSRR.BS13 |
| BSRR | BS14 | 14:14 | 0x4000 | Write 1 sets output | header:GPIO_BSRR_BS14_Msk; gpio_review:BSRR.BS14 |
| BSRR | BS15 | 15:15 | 0x8000 | Write 1 sets output | header:GPIO_BSRR_BS15_Msk; gpio_review:BSRR.BS15 |
| BSRR | BR0 | 16:16 | 0x10000 | Write 1 resets output | header:GPIO_BSRR_BR0_Msk; gpio_review:BSRR.BR0 |
| BSRR | BR1 | 17:17 | 0x20000 | Write 1 resets output | header:GPIO_BSRR_BR1_Msk; gpio_review:BSRR.BR1; timer_routes_evidence:rm0090/page:286 |
| BSRR | BR2 | 18:18 | 0x40000 | Write 1 resets output | header:GPIO_BSRR_BR2_Msk; gpio_review:BSRR.BR2 |
| BSRR | BR3 | 19:19 | 0x80000 | Write 1 resets output | header:GPIO_BSRR_BR3_Msk; gpio_review:BSRR.BR3 |
| BSRR | BR4 | 20:20 | 0x100000 | Write 1 resets output | header:GPIO_BSRR_BR4_Msk; gpio_review:BSRR.BR4 |
| BSRR | BR5 | 21:21 | 0x200000 | Write 1 resets output | header:GPIO_BSRR_BR5_Msk; gpio_review:BSRR.BR5 |
| BSRR | BR6 | 22:22 | 0x400000 | Write 1 resets output | header:GPIO_BSRR_BR6_Msk; gpio_review:BSRR.BR6 |
| BSRR | BR7 | 23:23 | 0x800000 | Write 1 resets output | header:GPIO_BSRR_BR7_Msk; gpio_review:BSRR.BR7 |
| BSRR | BR8 | 24:24 | 0x1000000 | Write 1 resets output | header:GPIO_BSRR_BR8_Msk; gpio_review:BSRR.BR8 |
| BSRR | BR9 | 25:25 | 0x2000000 | Write 1 resets output | header:GPIO_BSRR_BR9_Msk; gpio_review:BSRR.BR9 |
| BSRR | BR10 | 26:26 | 0x4000000 | Write 1 resets output | header:GPIO_BSRR_BR10_Msk; gpio_review:BSRR.BR10 |
| BSRR | BR11 | 27:27 | 0x8000000 | Write 1 resets output | header:GPIO_BSRR_BR11_Msk; gpio_review:BSRR.BR11 |
| BSRR | BR12 | 28:28 | 0x10000000 | Write 1 resets output | header:GPIO_BSRR_BR12_Msk; gpio_review:BSRR.BR12 |
| BSRR | BR13 | 29:29 | 0x20000000 | Write 1 resets output | header:GPIO_BSRR_BR13_Msk; gpio_review:BSRR.BR13 |
| BSRR | BR14 | 30:30 | 0x40000000 | Write 1 resets output | header:GPIO_BSRR_BR14_Msk; gpio_review:BSRR.BR14 |
| BSRR | BR15 | 31:31 | 0x80000000 | Write 1 resets output | header:GPIO_BSRR_BR15_Msk; gpio_review:BSRR.BR15 |
| LCKR | LCK0 | 0:0 | 0x1 | Pin configuration lock | header:GPIO_LCKR_LCK0_Msk; gpio_review:LCKR.LCK0 |
| LCKR | LCK1 | 1:1 | 0x2 | Pin configuration lock | header:GPIO_LCKR_LCK1_Msk; gpio_review:LCKR.LCK1; timer_routes_evidence:rm0090/page:287 |
| LCKR | LCK2 | 2:2 | 0x4 | Pin configuration lock | header:GPIO_LCKR_LCK2_Msk; gpio_review:LCKR.LCK2; timer_routes_evidence:rm0090/page:287 |
| LCKR | LCK3 | 3:3 | 0x8 | Pin configuration lock | header:GPIO_LCKR_LCK3_Msk; gpio_review:LCKR.LCK3 |
| LCKR | LCK4 | 4:4 | 0x10 | Pin configuration lock | header:GPIO_LCKR_LCK4_Msk; gpio_review:LCKR.LCK4 |
| LCKR | LCK5 | 5:5 | 0x20 | Pin configuration lock | header:GPIO_LCKR_LCK5_Msk; gpio_review:LCKR.LCK5 |
| LCKR | LCK6 | 6:6 | 0x40 | Pin configuration lock | header:GPIO_LCKR_LCK6_Msk; gpio_review:LCKR.LCK6 |
| LCKR | LCK7 | 7:7 | 0x80 | Pin configuration lock | header:GPIO_LCKR_LCK7_Msk; gpio_review:LCKR.LCK7 |
| LCKR | LCK8 | 8:8 | 0x100 | Pin configuration lock | header:GPIO_LCKR_LCK8_Msk; gpio_review:LCKR.LCK8 |
| LCKR | LCK9 | 9:9 | 0x200 | Pin configuration lock | header:GPIO_LCKR_LCK9_Msk; gpio_review:LCKR.LCK9 |
| LCKR | LCK10 | 10:10 | 0x400 | Pin configuration lock | header:GPIO_LCKR_LCK10_Msk; gpio_review:LCKR.LCK10 |
| LCKR | LCK11 | 11:11 | 0x800 | Pin configuration lock | header:GPIO_LCKR_LCK11_Msk; gpio_review:LCKR.LCK11 |
| LCKR | LCK12 | 12:12 | 0x1000 | Pin configuration lock | header:GPIO_LCKR_LCK12_Msk; gpio_review:LCKR.LCK12 |
| LCKR | LCK13 | 13:13 | 0x2000 | Pin configuration lock | header:GPIO_LCKR_LCK13_Msk; gpio_review:LCKR.LCK13 |
| LCKR | LCK14 | 14:14 | 0x4000 | Pin configuration lock | header:GPIO_LCKR_LCK14_Msk; gpio_review:LCKR.LCK14 |
| LCKR | LCK15 | 15:15 | 0x8000 | Pin configuration lock | header:GPIO_LCKR_LCK15_Msk; gpio_review:LCKR.LCK15 |
| LCKR | LCKK | 16:16 | 0x10000 | Lock sequence key | header:GPIO_LCKR_LCKK_Msk; gpio_review:LCKR.LCKK; timer_routes_evidence:rm0090/page:287 |
| AFRL | AFSEL0 | 3:0 | 0xF | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL0_Msk; gpio_review:AFRL.AFSEL0 |
| AFRL | AFSEL1 | 7:4 | 0xF0 | PA1: AF1 TIM2_CH2 output in this route; alternate owners such as USART2 excluded. | header:GPIO_AFRL_AFSEL1_Msk; gpio_review:AFRL.AFSEL1; timer_routes_evidence:rm0090/page:288; timer_routes_pin_evidence:ds8626/page:64 |
| AFRL | AFSEL2 | 11:8 | 0xF00 | PA2: AF2 TIM5_CH3 direct input in this route; alternate owners such as USART2 excluded. | header:GPIO_AFRL_AFSEL2_Msk; gpio_review:AFRL.AFSEL2; timer_routes_evidence:rm0090/page:288; timer_routes_pin_evidence:ds8626/page:64 |
| AFRL | AFSEL3 | 15:12 | 0xF000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL3_Msk; gpio_review:AFRL.AFSEL3 |
| AFRL | AFSEL4 | 19:16 | 0xF0000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL4_Msk; gpio_review:AFRL.AFSEL4 |
| AFRL | AFSEL5 | 23:20 | 0xF00000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL5_Msk; gpio_review:AFRL.AFSEL5 |
| AFRL | AFSEL6 | 27:24 | 0xF000000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL6_Msk; gpio_review:AFRL.AFSEL6 |
| AFRL | AFSEL7 | 31:28 | 0xF0000000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRL_AFSEL7_Msk; gpio_review:AFRL.AFSEL7 |
| AFRH | AFSEL8 | 3:0 | 0xF | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL8_Msk; gpio_review:AFRH.AFSEL8 |
| AFRH | AFSEL9 | 7:4 | 0xF0 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL9_Msk; gpio_review:AFRH.AFSEL9 |
| AFRH | AFSEL10 | 11:8 | 0xF00 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL10_Msk; gpio_review:AFRH.AFSEL10 |
| AFRH | AFSEL11 | 15:12 | 0xF000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL11_Msk; gpio_review:AFRH.AFSEL11 |
| AFRH | AFSEL12 | 19:16 | 0xF0000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL12_Msk; gpio_review:AFRH.AFSEL12 |
| AFRH | AFSEL13 | 23:20 | 0xF00000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL13_Msk; gpio_review:AFRH.AFSEL13 |
| AFRH | AFSEL14 | 27:24 | 0xF000000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL14_Msk; gpio_review:AFRH.AFSEL14 |
| AFRH | AFSEL15 | 31:28 | 0xF0000000 | AF0–AF15; only datasheet-listed mappings are valid | header:GPIO_AFRH_AFSEL15_Msk; gpio_review:AFRH.AFSEL15 |

## Reviewed operating semantics

Applicability: STM32F407VGT6, **LQFP100**, with the following reviewed AF subset.

| MCU pin | Physical LQFP100 pin | Signal | AF | AFRL bits | MODER bits | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PA2 | 25 | USART2_TX | 7 | 11:8 | 5:4 | gpio_review:DS8626 tables 7/9 |
| PA3 | 26 | USART2_RX | 7 | 15:12 | 7:6 | gpio_review:DS8626 tables 7/9 |

After [[peripherals/rcc]], replace only the PA2/PA3 fields: MODER=10, AFRL=7,
OTYPER=0 (push-pull), PUPDR=00, and OSPEEDR=01 as an example medium-speed choice.
Preserve all other pins, especially SWD PA13/PA14. The external interface must
provide an appropriate idle level. Validate routing in [[schemas/custom_pcb_netlist]]
before [[peripherals/usart]]. A schematic signal label does not configure AF7.

The complete GPIO register map is shared by GPIO instances; reset values for
MODER, OSPEEDR, and PUPDR depend on the port and remain unasserted in this common
table. BSRR is a write-one set/reset action. LCKR has a prescribed lock sequence;
do not use generic read-modify-write to lock configuration.

Header-declared GPIOF/G/I bases do not establish that those ports are bonded in
LQFP100. Only the package-specific reviewed pin map establishes physical pins.
This AF subset does not establish another pin's capabilities.

Evidence: `gpio_review` (DS8626 Rev 12 package pin table 7 and AF table 9),
`header` (GPIO layout/masks), and `profile:pin_map` (reviewed package map).
See [[sources]] and [[index]].


## Loopback and status pins

The loopback wire is an external test connection between PA2/P1-14 and PA3/P1-13; it is not a fixed board net. Both pins use AF7, push-pull, medium speed, no internal pull for the fitted-wire test. With the wire absent RX may float; a negative test can fail with a UART error rather than precisely at the timeout. PD12/13/14/15 drive the four active-high board LEDs; preload all off with BSRR before output mode. PA0 is input with the existing external pull-down and no internal pull. Preserve SWD PA13/14. Sources: schematic_uart:page:2; schematic_mcu:page:7; uart_connector:page:18; rm_gpio_speed:page:284; board signal definitions. See [[peripherals/syscfg]] and [[peripherals/exti]].

## CAN1 RX candidate route

PD0 (U4:81, P2:34), AF9, weak pull-up; see the can1_rx_pd0 operating contract. This is a scoped candidate, not a physical qualification. No CAN_TX output or transceiver is configured.

## Routed timer pins — reference MB997-E-01

| Role | MCU/package pin | Fixed connector endpoint | AF | Evidence |
| --- | --- | --- | --- | --- |
| TIM2_CH2 PWM output | PA1 / U4:24 | P1:11 | AF1 | timer_routes_pin_evidence ds8626/pages51,64; timer_routes_connectivity_evidence mb997/pages2,7 |
| TIM5_CH3 direct input | PA2 / U4:25 | P1:14 | AF2 | timer_routes_pin_evidence ds8626/pages51,64; timer_routes_connectivity_evidence mb997/pages2,7 |

The PA1 and PA2 nets remain separate. A passive external jumper between these
header endpoints is required only for the paired example, never inferred fitted.
Verify actual PCB revision and connector orientation. Disconnect every power source
before wiring; remove any prior PA2-to-PA3 jumper and other attachments first.
PA2 cannot simultaneously be USART2_TX; the UART and timer examples are mutually
exclusive owners. No active ADC/Ethernet/GPIO owner or external driver may share pins.
ST-LINK U2 PA1/PA2 labels denote local NC pins, not target VCP wiring.

Reject locked/already configured owned pins. Preserve SWD PA13/PA14, USER PA0
and all other pin fields with masks; never reset GPIOA. Before MODER=10, configure
PA1 low-speed push-pull/no pull and PA2 pull-down; set AFRL1=1 and AFRL2=2.
Keep channels/output disabled until route readback and capture setup pass. On
shutdown release only PA1/PA2 to input. This is an authored scoped subset, not a
complete board netlist or physical qualification. GPIO semantics: RM0090 pages282–288.
See [[peripherals/rcc]], [[peripherals/tim]], [[schemas/custom_pcb_netlist]].

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| can1_rx_pd0 | GPIOD | MODER, PUPDR, AFRL, IDR, LCKR | AFRL: AFSEL0; IDR: ID0; LCKR: LCK0, LCKK; MODER: MODER0; PUPDR: PUPD0 | STM32F407VGT6 LQFP100 only: PD0=U4:81, AF9 CAN1_RX; reference MB997-E-01 net PD0 reaches P2:34. Physical revision and external attachments remain unconfirmed.<br>Candidate-specific owned-startup policy, not a vendor mandate: leave P2:34 externally unconnected; enable/read back GPIODEN before GPIO accesses; preserve unrelated gates and fields.<br>Require PD0 MODER0=0, PUPD0=0, AFSEL0=0 and no active port lock before changing configuration; reject an existing owner. Use aligned32-bit accesses and no lock write sequence.<br>Set/read back PUPD0=1 (weak pull-up), AFSEL0=9, then MODER0=2 (AF input). Do not drive PD0 as a GPIO output. Leave CAN_TX and all unrelated pins unchanged.<br>Bound the IDR.ID0 high wait, then check CAN_MSR.RX before requesting initialization exit. A high GPIO sample does not prove 11 consecutive recessive bits or valid CAN timing; INAK/SLAK acknowledgements remain mandatory.<br>This is a software/model-checked hypothesis candidate. It does not establish electrical timing, fix causality, physical loopback success, transceiver support or external CAN readiness. | rm_can_rx_283:page:283; rm_can_rx_285:page:285; rm_can_rx_287:page:287; ds_can_rx_58:page:58; ds_can_rx_67:page:67; can_rx_gpio_review:CAN1 RX candidate route | [[peripherals/rcc]] / can1_rx_gpio_gate: RCC |
| pa1_tim2_ch2_pa2_tim5_ch3 | GPIOA | MODER, OTYPER, OSPEEDR, PUPDR, AFRL, BSRR, LCKR | AFRL: AFSEL1, AFSEL2; BSRR: BR1; LCKR: LCK1, LCK2, LCKK; MODER: MODER1, MODER2; OSPEEDR: OSPEED1, OSPEED2; OTYPER: OT1, OT2; PUPDR: PUPD1, PUPD2 | Exact STM32F407VGT6 LQFP100 and reference MB997-E-01; PA1/U4:24/P1:11 is AF1 TIM2_CH2, PA2/U4:25/P1:14 is AF2 TIM5_CH3.<br>Verify physical revision/orientation and sole passive PA1-to-PA2 test jumper, with all power disconnected before wiring; no other external drivers or active USART2/ADC/Ethernet/GPIO owners.<br>Reject already configured or locked PA1/PA2; preserve USER PA0, SWD PA13/PA14 and all unowned GPIO bits. Never reset GPIOA.<br>Keep timer output/channel disabled while routing; set PA1 latch low by BSRR action write, push-pull/low-speed, PA1 no pull and PA2 pull-down.<br>Program/read back AFRL and electrical fields before setting both MODER fields to alternate function (10); verify before enabling output.<br>On owned shutdown release only PA1/PA2 to input; do not claim safe shutdown if pin write/readback or GPIO clock access fails. | timer_routes_evidence:rm0090/page:282; timer_routes_evidence:rm0090/page:283; timer_routes_evidence:rm0090/page:284; timer_routes_evidence:rm0090/page:285; timer_routes_evidence:rm0090/page:286; timer_routes_evidence:rm0090/page:287; timer_routes_evidence:rm0090/page:288 | [[peripherals/rcc]] / timer_pair_gates: RCC |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: Exact MCP source parts and schematic images reviewed; implementing-author review only. Independent signoff and new physical qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
