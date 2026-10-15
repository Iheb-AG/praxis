# HSEM — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| HSEM | 0x58026400 | Not asserted | Not asserted | header:HSEM_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.R | 32 | 4 |
| RLR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.RLR | 32 | 4 |
| C1IER | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.C1IER | 1 | 4 |
| C1ICR | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.C1ICR | 1 | 4 |
| C1ISR | 0x108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.C1ISR | 1 | 4 |
| C1MISR | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.C1MISR | 1 | 4 |
| CR | 0x140 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.CR | 1 | 4 |
| KEYR | 0x144 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HSEM_TypeDef.KEYR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| R | PROCID | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:HSEM_R_PROCID_Msk |
| R | COREID | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:HSEM_R_COREID_Msk |
| R | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_R_LOCK_Msk |
| RLR | PROCID | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:HSEM_RLR_PROCID_Msk |
| RLR | COREID | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:HSEM_RLR_COREID_Msk |
| RLR | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_RLR_LOCK_Msk |
| C1IER | ISE0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE0_Msk |
| C1IER | ISE1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE1_Msk |
| C1IER | ISE2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE2_Msk |
| C1IER | ISE3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE3_Msk |
| C1IER | ISE4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE4_Msk |
| C1IER | ISE5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE5_Msk |
| C1IER | ISE6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE6_Msk |
| C1IER | ISE7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE7_Msk |
| C1IER | ISE8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE8_Msk |
| C1IER | ISE9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE9_Msk |
| C1IER | ISE10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE10_Msk |
| C1IER | ISE11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE11_Msk |
| C1IER | ISE12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE12_Msk |
| C1IER | ISE13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE13_Msk |
| C1IER | ISE14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE14_Msk |
| C1IER | ISE15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE15_Msk |
| C1IER | ISE16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE16_Msk |
| C1IER | ISE17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE17_Msk |
| C1IER | ISE18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE18_Msk |
| C1IER | ISE19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE19_Msk |
| C1IER | ISE20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE20_Msk |
| C1IER | ISE21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE21_Msk |
| C1IER | ISE22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE22_Msk |
| C1IER | ISE23 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE23_Msk |
| C1IER | ISE24 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE24_Msk |
| C1IER | ISE25 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE25_Msk |
| C1IER | ISE26 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE26_Msk |
| C1IER | ISE27 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE27_Msk |
| C1IER | ISE28 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE28_Msk |
| C1IER | ISE29 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE29_Msk |
| C1IER | ISE30 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE30_Msk |
| C1IER | ISE31 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1IER_ISE31_Msk |
| C1ICR | ISC0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC0_Msk |
| C1ICR | ISC1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC1_Msk |
| C1ICR | ISC2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC2_Msk |
| C1ICR | ISC3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC3_Msk |
| C1ICR | ISC4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC4_Msk |
| C1ICR | ISC5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC5_Msk |
| C1ICR | ISC6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC6_Msk |
| C1ICR | ISC7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC7_Msk |
| C1ICR | ISC8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC8_Msk |
| C1ICR | ISC9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC9_Msk |
| C1ICR | ISC10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC10_Msk |
| C1ICR | ISC11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC11_Msk |
| C1ICR | ISC12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC12_Msk |
| C1ICR | ISC13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC13_Msk |
| C1ICR | ISC14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC14_Msk |
| C1ICR | ISC15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC15_Msk |
| C1ICR | ISC16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC16_Msk |
| C1ICR | ISC17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC17_Msk |
| C1ICR | ISC18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC18_Msk |
| C1ICR | ISC19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC19_Msk |
| C1ICR | ISC20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC20_Msk |
| C1ICR | ISC21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC21_Msk |
| C1ICR | ISC22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC22_Msk |
| C1ICR | ISC23 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC23_Msk |
| C1ICR | ISC24 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC24_Msk |
| C1ICR | ISC25 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC25_Msk |
| C1ICR | ISC26 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC26_Msk |
| C1ICR | ISC27 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC27_Msk |
| C1ICR | ISC28 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC28_Msk |
| C1ICR | ISC29 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC29_Msk |
| C1ICR | ISC30 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC30_Msk |
| C1ICR | ISC31 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ICR_ISC31_Msk |
| C1ISR | ISF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF0_Msk |
| C1ISR | ISF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF1_Msk |
| C1ISR | ISF2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF2_Msk |
| C1ISR | ISF3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF3_Msk |
| C1ISR | ISF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF4_Msk |
| C1ISR | ISF5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF5_Msk |
| C1ISR | ISF6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF6_Msk |
| C1ISR | ISF7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF7_Msk |
| C1ISR | ISF8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF8_Msk |
| C1ISR | ISF9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF9_Msk |
| C1ISR | ISF10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF10_Msk |
| C1ISR | ISF11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF11_Msk |
| C1ISR | ISF12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF12_Msk |
| C1ISR | ISF13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF13_Msk |
| C1ISR | ISF14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF14_Msk |
| C1ISR | ISF15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF15_Msk |
| C1ISR | ISF16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF16_Msk |
| C1ISR | ISF17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF17_Msk |
| C1ISR | ISF18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF18_Msk |
| C1ISR | ISF19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF19_Msk |
| C1ISR | ISF20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF20_Msk |
| C1ISR | ISF21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF21_Msk |
| C1ISR | ISF22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF22_Msk |
| C1ISR | ISF23 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF23_Msk |
| C1ISR | ISF24 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF24_Msk |
| C1ISR | ISF25 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF25_Msk |
| C1ISR | ISF26 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF26_Msk |
| C1ISR | ISF27 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF27_Msk |
| C1ISR | ISF28 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF28_Msk |
| C1ISR | ISF29 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF29_Msk |
| C1ISR | ISF30 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF30_Msk |
| C1ISR | ISF31 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1ISR_ISF31_Msk |
| C1MISR | MISF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF0_Msk |
| C1MISR | MISF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF1_Msk |
| C1MISR | MISF2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF2_Msk |
| C1MISR | MISF3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF3_Msk |
| C1MISR | MISF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF4_Msk |
| C1MISR | MISF5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF5_Msk |
| C1MISR | MISF6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF6_Msk |
| C1MISR | MISF7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF7_Msk |
| C1MISR | MISF8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF8_Msk |
| C1MISR | MISF9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF9_Msk |
| C1MISR | MISF10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF10_Msk |
| C1MISR | MISF11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF11_Msk |
| C1MISR | MISF12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF12_Msk |
| C1MISR | MISF13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF13_Msk |
| C1MISR | MISF14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF14_Msk |
| C1MISR | MISF15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF15_Msk |
| C1MISR | MISF16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF16_Msk |
| C1MISR | MISF17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF17_Msk |
| C1MISR | MISF18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF18_Msk |
| C1MISR | MISF19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF19_Msk |
| C1MISR | MISF20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF20_Msk |
| C1MISR | MISF21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF21_Msk |
| C1MISR | MISF22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF22_Msk |
| C1MISR | MISF23 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF23_Msk |
| C1MISR | MISF24 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF24_Msk |
| C1MISR | MISF25 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF25_Msk |
| C1MISR | MISF26 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF26_Msk |
| C1MISR | MISF27 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF27_Msk |
| C1MISR | MISF28 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF28_Msk |
| C1MISR | MISF29 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF29_Msk |
| C1MISR | MISF30 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF30_Msk |
| C1MISR | MISF31 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_C1MISR_MISF31_Msk |
| CR | COREID | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:HSEM_CR_COREID_Msk |
| CR | KEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_CR_KEY_Msk |
| KEYR | KEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:HSEM_KEYR_KEY_Msk |

## Operating semantics unavailable

**hsem: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
