# GPIO — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| GPIOA | 0x58020000 | Not asserted | Not asserted | header:GPIOA_BASE |
| GPIOB | 0x58020400 | Not asserted | Not asserted | header:GPIOB_BASE |
| GPIOC | 0x58020800 | Not asserted | Not asserted | header:GPIOC_BASE |
| GPIOD | 0x58020C00 | Not asserted | Not asserted | header:GPIOD_BASE |
| GPIOE | 0x58021000 | Not asserted | Not asserted | header:GPIOE_BASE |
| GPIOF | 0x58021400 | Not asserted | Not asserted | header:GPIOF_BASE |
| GPIOG | 0x58021800 | Not asserted | Not asserted | header:GPIOG_BASE |
| GPIOH | 0x58021C00 | Not asserted | Not asserted | header:GPIOH_BASE |
| GPIOI | 0x58022000 | Not asserted | Not asserted | header:GPIOI_BASE |
| GPIOJ | 0x58022400 | Not asserted | Not asserted | header:GPIOJ_BASE |
| GPIOK | 0x58022800 | Not asserted | Not asserted | header:GPIOK_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MODER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.MODER |
| OTYPER | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.OTYPER |
| OSPEEDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.OSPEEDR |
| PUPDR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.PUPDR |
| IDR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.IDR |
| ODR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.ODR |
| BSRR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.BSRR |
| LCKR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.LCKR |
| AFRL | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.AFR[0] |
| AFRH | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.AFR[1] |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MODER | MODER0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER0_Msk |
| MODER | MODER1 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER1_Msk |
| MODER | MODER2 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER2_Msk |
| MODER | MODER3 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER3_Msk |
| MODER | MODER4 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER4_Msk |
| MODER | MODER5 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER5_Msk |
| MODER | MODER6 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER6_Msk |
| MODER | MODER7 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER7_Msk |
| MODER | MODER8 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER8_Msk |
| MODER | MODER9 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER9_Msk |
| MODER | MODER10 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER10_Msk |
| MODER | MODER11 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER11_Msk |
| MODER | MODER12 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER12_Msk |
| MODER | MODER13 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER13_Msk |
| MODER | MODER14 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER14_Msk |
| MODER | MODER15 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_MODER_MODER15_Msk |
| OTYPER | OT0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT0_Msk |
| OTYPER | OT1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT1_Msk |
| OTYPER | OT2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT2_Msk |
| OTYPER | OT3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT3_Msk |
| OTYPER | OT4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT4_Msk |
| OTYPER | OT5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT5_Msk |
| OTYPER | OT6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT6_Msk |
| OTYPER | OT7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT7_Msk |
| OTYPER | OT8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT8_Msk |
| OTYPER | OT9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT9_Msk |
| OTYPER | OT10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT10_Msk |
| OTYPER | OT11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT11_Msk |
| OTYPER | OT12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT12_Msk |
| OTYPER | OT13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT13_Msk |
| OTYPER | OT14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT14_Msk |
| OTYPER | OT15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OTYPER_OT15_Msk |
| OSPEEDR | OSPEED0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED0_Msk |
| OSPEEDR | OSPEED1 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED1_Msk |
| OSPEEDR | OSPEED2 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED2_Msk |
| OSPEEDR | OSPEED3 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED3_Msk |
| OSPEEDR | OSPEED4 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED4_Msk |
| OSPEEDR | OSPEED5 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED5_Msk |
| OSPEEDR | OSPEED6 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED6_Msk |
| OSPEEDR | OSPEED7 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED7_Msk |
| OSPEEDR | OSPEED8 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED8_Msk |
| OSPEEDR | OSPEED9 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED9_Msk |
| OSPEEDR | OSPEED10 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED10_Msk |
| OSPEEDR | OSPEED11 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED11_Msk |
| OSPEEDR | OSPEED12 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED12_Msk |
| OSPEEDR | OSPEED13 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED13_Msk |
| OSPEEDR | OSPEED14 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED14_Msk |
| OSPEEDR | OSPEED15 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_OSPEEDR_OSPEED15_Msk |
| PUPDR | PUPD0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD0_Msk |
| PUPDR | PUPD1 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD1_Msk |
| PUPDR | PUPD2 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD2_Msk |
| PUPDR | PUPD3 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD3_Msk |
| PUPDR | PUPD4 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD4_Msk |
| PUPDR | PUPD5 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD5_Msk |
| PUPDR | PUPD6 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD6_Msk |
| PUPDR | PUPD7 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD7_Msk |
| PUPDR | PUPD8 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD8_Msk |
| PUPDR | PUPD9 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD9_Msk |
| PUPDR | PUPD10 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD10_Msk |
| PUPDR | PUPD11 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD11_Msk |
| PUPDR | PUPD12 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD12_Msk |
| PUPDR | PUPD13 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD13_Msk |
| PUPDR | PUPD14 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD14_Msk |
| PUPDR | PUPD15 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_PUPDR_PUPD15_Msk |
| IDR | ID0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID0_Msk |
| IDR | ID1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID1_Msk |
| IDR | ID2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID2_Msk |
| IDR | ID3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID3_Msk |
| IDR | ID4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID4_Msk |
| IDR | ID5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID5_Msk |
| IDR | ID6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID6_Msk |
| IDR | ID7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID7_Msk |
| IDR | ID8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID8_Msk |
| IDR | ID9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID9_Msk |
| IDR | ID10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID10_Msk |
| IDR | ID11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID11_Msk |
| IDR | ID12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID12_Msk |
| IDR | ID13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID13_Msk |
| IDR | ID14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID14_Msk |
| IDR | ID15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_ID15_Msk |
| ODR | OD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD0_Msk |
| ODR | OD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD1_Msk |
| ODR | OD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD2_Msk |
| ODR | OD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD3_Msk |
| ODR | OD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD4_Msk |
| ODR | OD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD5_Msk |
| ODR | OD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD6_Msk |
| ODR | OD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD7_Msk |
| ODR | OD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD8_Msk |
| ODR | OD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD9_Msk |
| ODR | OD10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD10_Msk |
| ODR | OD11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD11_Msk |
| ODR | OD12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD12_Msk |
| ODR | OD13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD13_Msk |
| ODR | OD14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD14_Msk |
| ODR | OD15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_OD15_Msk |
| BSRR | BS0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS0_Msk |
| BSRR | BS1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS1_Msk |
| BSRR | BS2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS2_Msk |
| BSRR | BS3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS3_Msk |
| BSRR | BS4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS4_Msk |
| BSRR | BS5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS5_Msk |
| BSRR | BS6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS6_Msk |
| BSRR | BS7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS7_Msk |
| BSRR | BS8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS8_Msk |
| BSRR | BS9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS9_Msk |
| BSRR | BS10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS10_Msk |
| BSRR | BS11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS11_Msk |
| BSRR | BS12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS12_Msk |
| BSRR | BS13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS13_Msk |
| BSRR | BS14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS14_Msk |
| BSRR | BS15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BS15_Msk |
| BSRR | BR0 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR0_Msk |
| BSRR | BR1 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR1_Msk |
| BSRR | BR2 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR2_Msk |
| BSRR | BR3 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR3_Msk |
| BSRR | BR4 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR4_Msk |
| BSRR | BR5 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR5_Msk |
| BSRR | BR6 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR6_Msk |
| BSRR | BR7 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR7_Msk |
| BSRR | BR8 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR8_Msk |
| BSRR | BR9 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR9_Msk |
| BSRR | BR10 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR10_Msk |
| BSRR | BR11 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR11_Msk |
| BSRR | BR12 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR12_Msk |
| BSRR | BR13 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR13_Msk |
| BSRR | BR14 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR14_Msk |
| BSRR | BR15 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BSRR_BR15_Msk |
| LCKR | LCK0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK0_Msk |
| LCKR | LCK1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK1_Msk |
| LCKR | LCK2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK2_Msk |
| LCKR | LCK3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK3_Msk |
| LCKR | LCK4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK4_Msk |
| LCKR | LCK5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK5_Msk |
| LCKR | LCK6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK6_Msk |
| LCKR | LCK7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK7_Msk |
| LCKR | LCK8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK8_Msk |
| LCKR | LCK9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK9_Msk |
| LCKR | LCK10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK10_Msk |
| LCKR | LCK11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK11_Msk |
| LCKR | LCK12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK12_Msk |
| LCKR | LCK13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK13_Msk |
| LCKR | LCK14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK14_Msk |
| LCKR | LCK15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCK15_Msk |
| LCKR | LCKK | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_LCKR_LCKK_Msk |
| AFRL | AFSEL0 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL0_Msk |
| AFRL | AFSEL1 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL1_Msk |
| AFRL | AFSEL2 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL2_Msk |
| AFRL | AFSEL3 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL3_Msk |
| AFRL | AFSEL4 | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL4_Msk |
| AFRL | AFSEL5 | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL5_Msk |
| AFRL | AFSEL6 | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL6_Msk |
| AFRL | AFSEL7 | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRL_AFSEL7_Msk |
| AFRH | AFSEL8 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL8_Msk |
| AFRH | AFSEL9 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL9_Msk |
| AFRH | AFSEL10 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL10_Msk |
| AFRH | AFSEL11 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL11_Msk |
| AFRH | AFSEL12 | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL12_Msk |
| AFRH | AFSEL13 | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL13_Msk |
| AFRH | AFSEL14 | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL14_Msk |
| AFRH | AFSEL15 | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_AFRH_AFSEL15_Msk |

## Operating semantics unavailable

**gpio: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
