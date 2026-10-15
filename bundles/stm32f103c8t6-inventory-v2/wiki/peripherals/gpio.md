# GPIO — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| GPIOA | 0x40010800 | Not asserted | Not asserted | header:GPIOA_BASE |
| GPIOB | 0x40010C00 | Not asserted | Not asserted | header:GPIOB_BASE |
| GPIOC | 0x40011000 | Not asserted | Not asserted | header:GPIOC_BASE |
| GPIOD | 0x40011400 | Not asserted | Not asserted | header:GPIOD_BASE |
| GPIOE | 0x40011800 | Not asserted | Not asserted | header:GPIOE_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRL | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.CRL |
| CRH | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.CRH |
| IDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.IDR |
| ODR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.ODR |
| BSRR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.BSRR |
| BRR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.BRR |
| LCKR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:GPIO_TypeDef.LCKR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CRL | MODE0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE0_Msk |
| CRL | CNF0 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF0_Msk |
| CRL | MODE1 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE1_Msk |
| CRL | CNF1 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF1_Msk |
| CRL | MODE2 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE2_Msk |
| CRL | CNF2 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF2_Msk |
| CRL | MODE3 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE3_Msk |
| CRL | CNF3 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF3_Msk |
| CRL | MODE4 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE4_Msk |
| CRL | CNF4 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF4_Msk |
| CRL | MODE5 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE5_Msk |
| CRL | CNF5 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF5_Msk |
| CRL | MODE6 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE6_Msk |
| CRL | CNF6 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF6_Msk |
| CRL | MODE7 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_MODE7_Msk |
| CRL | CNF7 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRL_CNF7_Msk |
| CRH | MODE8 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE8_Msk |
| CRH | CNF8 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF8_Msk |
| CRH | MODE9 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE9_Msk |
| CRH | CNF9 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF9_Msk |
| CRH | MODE10 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE10_Msk |
| CRH | CNF10 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF10_Msk |
| CRH | MODE11 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE11_Msk |
| CRH | CNF11 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF11_Msk |
| CRH | MODE12 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE12_Msk |
| CRH | CNF12 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF12_Msk |
| CRH | MODE13 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE13_Msk |
| CRH | CNF13 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF13_Msk |
| CRH | MODE14 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE14_Msk |
| CRH | CNF14 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF14_Msk |
| CRH | MODE15 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_MODE15_Msk |
| CRH | CNF15 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_CRH_CNF15_Msk |
| IDR | IDR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR0_Msk |
| IDR | IDR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR1_Msk |
| IDR | IDR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR2_Msk |
| IDR | IDR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR3_Msk |
| IDR | IDR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR4_Msk |
| IDR | IDR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR5_Msk |
| IDR | IDR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR6_Msk |
| IDR | IDR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR7_Msk |
| IDR | IDR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR8_Msk |
| IDR | IDR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR9_Msk |
| IDR | IDR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR10_Msk |
| IDR | IDR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR11_Msk |
| IDR | IDR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR12_Msk |
| IDR | IDR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR13_Msk |
| IDR | IDR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR14_Msk |
| IDR | IDR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_IDR_IDR15_Msk |
| ODR | ODR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR0_Msk |
| ODR | ODR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR1_Msk |
| ODR | ODR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR2_Msk |
| ODR | ODR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR3_Msk |
| ODR | ODR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR4_Msk |
| ODR | ODR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR5_Msk |
| ODR | ODR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR6_Msk |
| ODR | ODR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR7_Msk |
| ODR | ODR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR8_Msk |
| ODR | ODR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR9_Msk |
| ODR | ODR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR10_Msk |
| ODR | ODR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR11_Msk |
| ODR | ODR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR12_Msk |
| ODR | ODR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR13_Msk |
| ODR | ODR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR14_Msk |
| ODR | ODR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_ODR_ODR15_Msk |
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
| BRR | BR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR0_Msk |
| BRR | BR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR1_Msk |
| BRR | BR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR2_Msk |
| BRR | BR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR3_Msk |
| BRR | BR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR4_Msk |
| BRR | BR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR5_Msk |
| BRR | BR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR6_Msk |
| BRR | BR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR7_Msk |
| BRR | BR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR8_Msk |
| BRR | BR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR9_Msk |
| BRR | BR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR10_Msk |
| BRR | BR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR11_Msk |
| BRR | BR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR12_Msk |
| BRR | BR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR13_Msk |
| BRR | BR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR14_Msk |
| BRR | BR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:GPIO_BRR_BR15_Msk |
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

## Operating semantics unavailable

**gpio: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Compound declaration masks:

- Compound mask GPIO_CRL_CNF_Msk=0xCCCCCCCC (header:GPIO_CRL_CNF_Msk) is represented by its separately declared, disjoint contiguous components: GPIO_CRL_CNF0_Msk=0xC (header:GPIO_CRL_CNF0_Msk); GPIO_CRL_CNF1_Msk=0xC0 (header:GPIO_CRL_CNF1_Msk); GPIO_CRL_CNF2_Msk=0xC00 (header:GPIO_CRL_CNF2_Msk); GPIO_CRL_CNF3_Msk=0xC000 (header:GPIO_CRL_CNF3_Msk); GPIO_CRL_CNF4_Msk=0xC0000 (header:GPIO_CRL_CNF4_Msk); GPIO_CRL_CNF5_Msk=0xC00000 (header:GPIO_CRL_CNF5_Msk); GPIO_CRL_CNF6_Msk=0xC000000 (header:GPIO_CRL_CNF6_Msk); GPIO_CRL_CNF7_Msk=0xC0000000 (header:GPIO_CRL_CNF7_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask GPIO_CRL_MODE_Msk=0x33333333 (header:GPIO_CRL_MODE_Msk) is represented by its separately declared, disjoint contiguous components: GPIO_CRL_MODE0_Msk=0x3 (header:GPIO_CRL_MODE0_Msk); GPIO_CRL_MODE1_Msk=0x30 (header:GPIO_CRL_MODE1_Msk); GPIO_CRL_MODE2_Msk=0x300 (header:GPIO_CRL_MODE2_Msk); GPIO_CRL_MODE3_Msk=0x3000 (header:GPIO_CRL_MODE3_Msk); GPIO_CRL_MODE4_Msk=0x30000 (header:GPIO_CRL_MODE4_Msk); GPIO_CRL_MODE5_Msk=0x300000 (header:GPIO_CRL_MODE5_Msk); GPIO_CRL_MODE6_Msk=0x3000000 (header:GPIO_CRL_MODE6_Msk); GPIO_CRL_MODE7_Msk=0x30000000 (header:GPIO_CRL_MODE7_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask GPIO_CRH_CNF_Msk=0xCCCCCCCC (header:GPIO_CRH_CNF_Msk) is represented by its separately declared, disjoint contiguous components: GPIO_CRH_CNF10_Msk=0xC00 (header:GPIO_CRH_CNF10_Msk); GPIO_CRH_CNF11_Msk=0xC000 (header:GPIO_CRH_CNF11_Msk); GPIO_CRH_CNF12_Msk=0xC0000 (header:GPIO_CRH_CNF12_Msk); GPIO_CRH_CNF13_Msk=0xC00000 (header:GPIO_CRH_CNF13_Msk); GPIO_CRH_CNF14_Msk=0xC000000 (header:GPIO_CRH_CNF14_Msk); GPIO_CRH_CNF15_Msk=0xC0000000 (header:GPIO_CRH_CNF15_Msk); GPIO_CRH_CNF8_Msk=0xC (header:GPIO_CRH_CNF8_Msk); GPIO_CRH_CNF9_Msk=0xC0 (header:GPIO_CRH_CNF9_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask GPIO_CRH_MODE_Msk=0x33333333 (header:GPIO_CRH_MODE_Msk) is represented by its separately declared, disjoint contiguous components: GPIO_CRH_MODE10_Msk=0x300 (header:GPIO_CRH_MODE10_Msk); GPIO_CRH_MODE11_Msk=0x3000 (header:GPIO_CRH_MODE11_Msk); GPIO_CRH_MODE12_Msk=0x30000 (header:GPIO_CRH_MODE12_Msk); GPIO_CRH_MODE13_Msk=0x300000 (header:GPIO_CRH_MODE13_Msk); GPIO_CRH_MODE14_Msk=0x3000000 (header:GPIO_CRH_MODE14_Msk); GPIO_CRH_MODE15_Msk=0x30000000 (header:GPIO_CRH_MODE15_Msk); GPIO_CRH_MODE8_Msk=0x3 (header:GPIO_CRH_MODE8_Msk); GPIO_CRH_MODE9_Msk=0x30 (header:GPIO_CRH_MODE9_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
