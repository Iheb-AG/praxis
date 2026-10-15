# GPIOA: multiplexing and USART2 pins

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| GPIOA | 0x40020000 | AHB1 | RCC_AHB1ENR.GPIOAEN | header:instance:GPIOA; gpio_review:clock:GPIOA |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MODER | 0x000 | 32 | — | RW | 0xA8000000 | Preserve SWD/debug pins. | header:register:MODER; gpio_review:register:MODER |
| OTYPER | 0x004 | 32 | — | RW | 0x0 | Upper 16 bits reserved. | header:register:OTYPER; gpio_review:register:OTYPER |
| OSPEEDR | 0x008 | 32 | — | RW | not asserted | Choose slew rate for the board signal. | header:register:OSPEEDR; gpio_review:register:OSPEEDR |
| PUPDR | 0x00C | 32 | — | RW | not asserted | 11 encoding is reserved. | header:register:PUPDR; gpio_review:register:PUPDR |
| IDR | 0x010 | 32 | — | RO | not asserted | Sampled input; no read-to-clear. | header:register:IDR; gpio_review:register:IDR |
| ODR | 0x014 | 32 | — | RW | 0x0 | Use BSRR for atomic pin changes. | header:register:ODR; gpio_review:register:ODR |
| BSRR | 0x018 | 32 | — | WO | 0x0 | Write ones to set/reset; never read-modify-write. | header:register:BSRR; gpio_review:register:BSRR |
| LCKR | 0x01C | 32 | — | RW | 0x0 | Lock sequence is deliberate; fixture leaves pins unlocked. | header:register:LCKR; gpio_review:register:LCKR |
| AFRL | 0x020 | 32 | — | RW | 0x0 | Write selected four-bit field; preserve adjacent pins. | header:register:AFRL; gpio_review:register:AFRL |
| AFRH | 0x024 | 32 | — | RW | 0x0 | Pins 8–15 use this register. | header:register:AFRH; gpio_review:register:AFRH |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MODER | MODER0 | 1:0 | 0x3 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER0 |
| MODER | MODER1 | 3:2 | 0xC | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER1 |
| MODER | MODER2 | 5:4 | 0x30 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER2 |
| MODER | MODER3 | 7:6 | 0xC0 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER3 |
| MODER | MODER4 | 9:8 | 0x300 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER4 |
| MODER | MODER5 | 11:10 | 0xC00 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER5 |
| MODER | MODER6 | 13:12 | 0x3000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER6 |
| MODER | MODER7 | 15:14 | 0xC000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER7 |
| MODER | MODER8 | 17:16 | 0x30000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER8 |
| MODER | MODER9 | 19:18 | 0xC0000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER9 |
| MODER | MODER10 | 21:20 | 0x300000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER10 |
| MODER | MODER11 | 23:22 | 0xC00000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER11 |
| MODER | MODER12 | 25:24 | 0x3000000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER12 |
| MODER | MODER13 | 27:26 | 0xC000000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER13 |
| MODER | MODER14 | 29:28 | 0x30000000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER14 |
| MODER | MODER15 | 31:30 | 0xC0000000 | 00 input; 01 output; 10 alternate function; 11 analog | gpio_review:field:MODER15 |
| OTYPER | OT0 | 0:0 | 0x1 | 0 push-pull; 1 open-drain | gpio_review:field:OT0 |
| OTYPER | OT1 | 1:1 | 0x2 | 0 push-pull; 1 open-drain | gpio_review:field:OT1 |
| OTYPER | OT2 | 2:2 | 0x4 | 0 push-pull; 1 open-drain | gpio_review:field:OT2 |
| OTYPER | OT3 | 3:3 | 0x8 | 0 push-pull; 1 open-drain | gpio_review:field:OT3 |
| OTYPER | OT4 | 4:4 | 0x10 | 0 push-pull; 1 open-drain | gpio_review:field:OT4 |
| OTYPER | OT5 | 5:5 | 0x20 | 0 push-pull; 1 open-drain | gpio_review:field:OT5 |
| OTYPER | OT6 | 6:6 | 0x40 | 0 push-pull; 1 open-drain | gpio_review:field:OT6 |
| OTYPER | OT7 | 7:7 | 0x80 | 0 push-pull; 1 open-drain | gpio_review:field:OT7 |
| OTYPER | OT8 | 8:8 | 0x100 | 0 push-pull; 1 open-drain | gpio_review:field:OT8 |
| OTYPER | OT9 | 9:9 | 0x200 | 0 push-pull; 1 open-drain | gpio_review:field:OT9 |
| OTYPER | OT10 | 10:10 | 0x400 | 0 push-pull; 1 open-drain | gpio_review:field:OT10 |
| OTYPER | OT11 | 11:11 | 0x800 | 0 push-pull; 1 open-drain | gpio_review:field:OT11 |
| OTYPER | OT12 | 12:12 | 0x1000 | 0 push-pull; 1 open-drain | gpio_review:field:OT12 |
| OTYPER | OT13 | 13:13 | 0x2000 | 0 push-pull; 1 open-drain | gpio_review:field:OT13 |
| OTYPER | OT14 | 14:14 | 0x4000 | 0 push-pull; 1 open-drain | gpio_review:field:OT14 |
| OTYPER | OT15 | 15:15 | 0x8000 | 0 push-pull; 1 open-drain | gpio_review:field:OT15 |
| OSPEEDR | OSPEED0 | 1:0 | 0x3 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED0 |
| OSPEEDR | OSPEED1 | 3:2 | 0xC | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED1 |
| OSPEEDR | OSPEED2 | 5:4 | 0x30 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED2 |
| OSPEEDR | OSPEED3 | 7:6 | 0xC0 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED3 |
| OSPEEDR | OSPEED4 | 9:8 | 0x300 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED4 |
| OSPEEDR | OSPEED5 | 11:10 | 0xC00 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED5 |
| OSPEEDR | OSPEED6 | 13:12 | 0x3000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED6 |
| OSPEEDR | OSPEED7 | 15:14 | 0xC000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED7 |
| OSPEEDR | OSPEED8 | 17:16 | 0x30000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED8 |
| OSPEEDR | OSPEED9 | 19:18 | 0xC0000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED9 |
| OSPEEDR | OSPEED10 | 21:20 | 0x300000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED10 |
| OSPEEDR | OSPEED11 | 23:22 | 0xC00000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED11 |
| OSPEEDR | OSPEED12 | 25:24 | 0x3000000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED12 |
| OSPEEDR | OSPEED13 | 27:26 | 0xC000000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED13 |
| OSPEEDR | OSPEED14 | 29:28 | 0x30000000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED14 |
| OSPEEDR | OSPEED15 | 31:30 | 0xC0000000 | 00 low; 01 medium; 10 fast; 11 high | gpio_review:field:OSPEED15 |
| PUPDR | PUPD0 | 1:0 | 0x3 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD0 |
| PUPDR | PUPD1 | 3:2 | 0xC | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD1 |
| PUPDR | PUPD2 | 5:4 | 0x30 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD2 |
| PUPDR | PUPD3 | 7:6 | 0xC0 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD3 |
| PUPDR | PUPD4 | 9:8 | 0x300 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD4 |
| PUPDR | PUPD5 | 11:10 | 0xC00 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD5 |
| PUPDR | PUPD6 | 13:12 | 0x3000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD6 |
| PUPDR | PUPD7 | 15:14 | 0xC000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD7 |
| PUPDR | PUPD8 | 17:16 | 0x30000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD8 |
| PUPDR | PUPD9 | 19:18 | 0xC0000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD9 |
| PUPDR | PUPD10 | 21:20 | 0x300000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD10 |
| PUPDR | PUPD11 | 23:22 | 0xC00000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD11 |
| PUPDR | PUPD12 | 25:24 | 0x3000000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD12 |
| PUPDR | PUPD13 | 27:26 | 0xC000000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD13 |
| PUPDR | PUPD14 | 29:28 | 0x30000000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD14 |
| PUPDR | PUPD15 | 31:30 | 0xC0000000 | 00 none; 01 pull-up; 10 pull-down | gpio_review:field:PUPD15 |
| IDR | IDR0 | 0:0 | 0x1 | Input sample | gpio_review:field:IDR0 |
| IDR | IDR1 | 1:1 | 0x2 | Input sample | gpio_review:field:IDR1 |
| IDR | IDR2 | 2:2 | 0x4 | Input sample | gpio_review:field:IDR2 |
| IDR | IDR3 | 3:3 | 0x8 | Input sample | gpio_review:field:IDR3 |
| IDR | IDR4 | 4:4 | 0x10 | Input sample | gpio_review:field:IDR4 |
| IDR | IDR5 | 5:5 | 0x20 | Input sample | gpio_review:field:IDR5 |
| IDR | IDR6 | 6:6 | 0x40 | Input sample | gpio_review:field:IDR6 |
| IDR | IDR7 | 7:7 | 0x80 | Input sample | gpio_review:field:IDR7 |
| IDR | IDR8 | 8:8 | 0x100 | Input sample | gpio_review:field:IDR8 |
| IDR | IDR9 | 9:9 | 0x200 | Input sample | gpio_review:field:IDR9 |
| IDR | IDR10 | 10:10 | 0x400 | Input sample | gpio_review:field:IDR10 |
| IDR | IDR11 | 11:11 | 0x800 | Input sample | gpio_review:field:IDR11 |
| IDR | IDR12 | 12:12 | 0x1000 | Input sample | gpio_review:field:IDR12 |
| IDR | IDR13 | 13:13 | 0x2000 | Input sample | gpio_review:field:IDR13 |
| IDR | IDR14 | 14:14 | 0x4000 | Input sample | gpio_review:field:IDR14 |
| IDR | IDR15 | 15:15 | 0x8000 | Input sample | gpio_review:field:IDR15 |
| ODR | ODR0 | 0:0 | 0x1 | Output latch | gpio_review:field:ODR0 |
| ODR | ODR1 | 1:1 | 0x2 | Output latch | gpio_review:field:ODR1 |
| ODR | ODR2 | 2:2 | 0x4 | Output latch | gpio_review:field:ODR2 |
| ODR | ODR3 | 3:3 | 0x8 | Output latch | gpio_review:field:ODR3 |
| ODR | ODR4 | 4:4 | 0x10 | Output latch | gpio_review:field:ODR4 |
| ODR | ODR5 | 5:5 | 0x20 | Output latch | gpio_review:field:ODR5 |
| ODR | ODR6 | 6:6 | 0x40 | Output latch | gpio_review:field:ODR6 |
| ODR | ODR7 | 7:7 | 0x80 | Output latch | gpio_review:field:ODR7 |
| ODR | ODR8 | 8:8 | 0x100 | Output latch | gpio_review:field:ODR8 |
| ODR | ODR9 | 9:9 | 0x200 | Output latch | gpio_review:field:ODR9 |
| ODR | ODR10 | 10:10 | 0x400 | Output latch | gpio_review:field:ODR10 |
| ODR | ODR11 | 11:11 | 0x800 | Output latch | gpio_review:field:ODR11 |
| ODR | ODR12 | 12:12 | 0x1000 | Output latch | gpio_review:field:ODR12 |
| ODR | ODR13 | 13:13 | 0x2000 | Output latch | gpio_review:field:ODR13 |
| ODR | ODR14 | 14:14 | 0x4000 | Output latch | gpio_review:field:ODR14 |
| ODR | ODR15 | 15:15 | 0x8000 | Output latch | gpio_review:field:ODR15 |
| BSRR | BS0 | 0:0 | 0x1 | Write 1 sets output | gpio_review:field:BS0 |
| BSRR | BS1 | 1:1 | 0x2 | Write 1 sets output | gpio_review:field:BS1 |
| BSRR | BS2 | 2:2 | 0x4 | Write 1 sets output | gpio_review:field:BS2 |
| BSRR | BS3 | 3:3 | 0x8 | Write 1 sets output | gpio_review:field:BS3 |
| BSRR | BS4 | 4:4 | 0x10 | Write 1 sets output | gpio_review:field:BS4 |
| BSRR | BS5 | 5:5 | 0x20 | Write 1 sets output | gpio_review:field:BS5 |
| BSRR | BS6 | 6:6 | 0x40 | Write 1 sets output | gpio_review:field:BS6 |
| BSRR | BS7 | 7:7 | 0x80 | Write 1 sets output | gpio_review:field:BS7 |
| BSRR | BS8 | 8:8 | 0x100 | Write 1 sets output | gpio_review:field:BS8 |
| BSRR | BS9 | 9:9 | 0x200 | Write 1 sets output | gpio_review:field:BS9 |
| BSRR | BS10 | 10:10 | 0x400 | Write 1 sets output | gpio_review:field:BS10 |
| BSRR | BS11 | 11:11 | 0x800 | Write 1 sets output | gpio_review:field:BS11 |
| BSRR | BS12 | 12:12 | 0x1000 | Write 1 sets output | gpio_review:field:BS12 |
| BSRR | BS13 | 13:13 | 0x2000 | Write 1 sets output | gpio_review:field:BS13 |
| BSRR | BS14 | 14:14 | 0x4000 | Write 1 sets output | gpio_review:field:BS14 |
| BSRR | BS15 | 15:15 | 0x8000 | Write 1 sets output | gpio_review:field:BS15 |
| BSRR | BR0 | 16:16 | 0x10000 | Write 1 resets output | gpio_review:field:BR0 |
| BSRR | BR1 | 17:17 | 0x20000 | Write 1 resets output | gpio_review:field:BR1 |
| BSRR | BR2 | 18:18 | 0x40000 | Write 1 resets output | gpio_review:field:BR2 |
| BSRR | BR3 | 19:19 | 0x80000 | Write 1 resets output | gpio_review:field:BR3 |
| BSRR | BR4 | 20:20 | 0x100000 | Write 1 resets output | gpio_review:field:BR4 |
| BSRR | BR5 | 21:21 | 0x200000 | Write 1 resets output | gpio_review:field:BR5 |
| BSRR | BR6 | 22:22 | 0x400000 | Write 1 resets output | gpio_review:field:BR6 |
| BSRR | BR7 | 23:23 | 0x800000 | Write 1 resets output | gpio_review:field:BR7 |
| BSRR | BR8 | 24:24 | 0x1000000 | Write 1 resets output | gpio_review:field:BR8 |
| BSRR | BR9 | 25:25 | 0x2000000 | Write 1 resets output | gpio_review:field:BR9 |
| BSRR | BR10 | 26:26 | 0x4000000 | Write 1 resets output | gpio_review:field:BR10 |
| BSRR | BR11 | 27:27 | 0x8000000 | Write 1 resets output | gpio_review:field:BR11 |
| BSRR | BR12 | 28:28 | 0x10000000 | Write 1 resets output | gpio_review:field:BR12 |
| BSRR | BR13 | 29:29 | 0x20000000 | Write 1 resets output | gpio_review:field:BR13 |
| BSRR | BR14 | 30:30 | 0x40000000 | Write 1 resets output | gpio_review:field:BR14 |
| BSRR | BR15 | 31:31 | 0x80000000 | Write 1 resets output | gpio_review:field:BR15 |
| LCKR | LCK0 | 0:0 | 0x1 | Pin configuration lock | gpio_review:field:LCK0 |
| LCKR | LCK1 | 1:1 | 0x2 | Pin configuration lock | gpio_review:field:LCK1 |
| LCKR | LCK2 | 2:2 | 0x4 | Pin configuration lock | gpio_review:field:LCK2 |
| LCKR | LCK3 | 3:3 | 0x8 | Pin configuration lock | gpio_review:field:LCK3 |
| LCKR | LCK4 | 4:4 | 0x10 | Pin configuration lock | gpio_review:field:LCK4 |
| LCKR | LCK5 | 5:5 | 0x20 | Pin configuration lock | gpio_review:field:LCK5 |
| LCKR | LCK6 | 6:6 | 0x40 | Pin configuration lock | gpio_review:field:LCK6 |
| LCKR | LCK7 | 7:7 | 0x80 | Pin configuration lock | gpio_review:field:LCK7 |
| LCKR | LCK8 | 8:8 | 0x100 | Pin configuration lock | gpio_review:field:LCK8 |
| LCKR | LCK9 | 9:9 | 0x200 | Pin configuration lock | gpio_review:field:LCK9 |
| LCKR | LCK10 | 10:10 | 0x400 | Pin configuration lock | gpio_review:field:LCK10 |
| LCKR | LCK11 | 11:11 | 0x800 | Pin configuration lock | gpio_review:field:LCK11 |
| LCKR | LCK12 | 12:12 | 0x1000 | Pin configuration lock | gpio_review:field:LCK12 |
| LCKR | LCK13 | 13:13 | 0x2000 | Pin configuration lock | gpio_review:field:LCK13 |
| LCKR | LCK14 | 14:14 | 0x4000 | Pin configuration lock | gpio_review:field:LCK14 |
| LCKR | LCK15 | 15:15 | 0x8000 | Pin configuration lock | gpio_review:field:LCK15 |
| LCKR | LCKK | 16:16 | 0x10000 | Lock sequence key | gpio_review:field:LCKK |
| AFRL | AFSEL0 | 3:0 | 0xF | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL0 |
| AFRL | AFSEL1 | 7:4 | 0xF0 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL1 |
| AFRL | AFSEL2 | 11:8 | 0xF00 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL2 |
| AFRL | AFSEL3 | 15:12 | 0xF000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL3 |
| AFRL | AFSEL4 | 19:16 | 0xF0000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL4 |
| AFRL | AFSEL5 | 23:20 | 0xF00000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL5 |
| AFRL | AFSEL6 | 27:24 | 0xF000000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL6 |
| AFRL | AFSEL7 | 31:28 | 0xF0000000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL7 |
| AFRH | AFSEL8 | 3:0 | 0xF | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL8 |
| AFRH | AFSEL9 | 7:4 | 0xF0 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL9 |
| AFRH | AFSEL10 | 11:8 | 0xF00 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL10 |
| AFRH | AFSEL11 | 15:12 | 0xF000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL11 |
| AFRH | AFSEL12 | 19:16 | 0xF0000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL12 |
| AFRH | AFSEL13 | 23:20 | 0xF00000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL13 |
| AFRH | AFSEL14 | 27:24 | 0xF000000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL14 |
| AFRH | AFSEL15 | 31:28 | 0xF0000000 | AF0–AF15; only datasheet-listed mappings are valid | gpio_review:field:AFSEL15 |

## Reviewed operating semantics

The fixture uses STM32F401RE in LQFP64. The supported AF table is deliberately limited to the routed USART2 pins; never extrapolate AF7 to another pin.

| MCU pin | Physical LQFP64 pin | Signal | AF | AFRL bits | MODER bits |
| --- | --- | --- | --- | --- | --- |
| PA2 | 16 | USART2_TX | 7 | 11:8 | 5:4 |
| PA3 | 17 | USART2_RX | 7 | 15:12 | 7:6 |

After [[peripherals/rcc]], clear and replace the relevant fields: MODER=10, AFRL=7, OTYPER=0 (push-pull), OSPEEDR=01 (medium fixture choice), PUPDR=00. Preserve every other pin, especially SWD PA13/PA14. Inputs must have a defined electrical idle level from the attached interface; the fixture does not guarantee external biasing.

The register field table is contiguous and covers every GPIO bit position. Package-specific alternate functions come from [DS10086 pin and AF tables](https://www.st.com/resource/en/datasheet/stm32f401re.pdf); register semantics come from [RM0368 GPIO](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf). Verify direct routing in [[schemas/custom_pcb_netlist]] before [[peripherals/usart]].

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
