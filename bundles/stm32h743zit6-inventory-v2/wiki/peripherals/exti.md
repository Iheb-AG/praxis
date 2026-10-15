# EXTI — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| EXTI | 0x58000000 | Not asserted | Not asserted | header:EXTI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RTSR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RTSR1 |
| FTSR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FTSR1 |
| SWIER1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.SWIER1 |
| D3PMR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PMR1 |
| D3PCR1L | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR1L |
| D3PCR1H | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR1H |
| RTSR2 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RTSR2 |
| FTSR2 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FTSR2 |
| SWIER2 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.SWIER2 |
| D3PMR2 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PMR2 |
| D3PCR2L | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR2L |
| D3PCR2H | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR2H |
| RTSR3 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RTSR3 |
| FTSR3 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FTSR3 |
| SWIER3 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.SWIER3 |
| D3PMR3 | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PMR3 |
| D3PCR3L | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR3L |
| D3PCR3H | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.D3PCR3H |
| IMR1 | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR1 |
| EMR1 | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR1 |
| PR1 | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.PR1 |
| IMR2 | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR2 |
| EMR2 | 0x094 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR2 |
| PR2 | 0x098 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.PR2 |
| IMR3 | 0x0A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR3 |
| EMR3 | 0x0A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR3 |
| PR3 | 0x0A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.PR3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| RTSR1 | TR | 21:0 | 0x3FFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_TR_Msk |
| FTSR1 | TR | 21:0 | 0x3FFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_TR_Msk |
| SWIER1 | SWIER0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER0_Msk |
| SWIER1 | SWIER1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER1_Msk |
| SWIER1 | SWIER2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER2_Msk |
| SWIER1 | SWIER3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER3_Msk |
| SWIER1 | SWIER4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER4_Msk |
| SWIER1 | SWIER5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER5_Msk |
| SWIER1 | SWIER6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER6_Msk |
| SWIER1 | SWIER7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER7_Msk |
| SWIER1 | SWIER8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER8_Msk |
| SWIER1 | SWIER9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER9_Msk |
| SWIER1 | SWIER10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER10_Msk |
| SWIER1 | SWIER11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER11_Msk |
| SWIER1 | SWIER12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER12_Msk |
| SWIER1 | SWIER13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER13_Msk |
| SWIER1 | SWIER14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER14_Msk |
| SWIER1 | SWIER15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER15_Msk |
| SWIER1 | SWIER16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER16_Msk |
| SWIER1 | SWIER17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER17_Msk |
| SWIER1 | SWIER18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER18_Msk |
| SWIER1 | SWIER19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER19_Msk |
| SWIER1 | SWIER20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER20_Msk |
| SWIER1 | SWIER21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWIER21_Msk |
| D3PMR1 | MR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR0_Msk |
| D3PMR1 | MR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR1_Msk |
| D3PMR1 | MR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR2_Msk |
| D3PMR1 | MR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR3_Msk |
| D3PMR1 | MR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR4_Msk |
| D3PMR1 | MR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR5_Msk |
| D3PMR1 | MR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR6_Msk |
| D3PMR1 | MR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR7_Msk |
| D3PMR1 | MR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR8_Msk |
| D3PMR1 | MR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR9_Msk |
| D3PMR1 | MR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR10_Msk |
| D3PMR1 | MR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR11_Msk |
| D3PMR1 | MR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR12_Msk |
| D3PMR1 | MR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR13_Msk |
| D3PMR1 | MR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR14_Msk |
| D3PMR1 | MR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR15_Msk |
| D3PMR1 | MR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR19_Msk |
| D3PMR1 | MR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR20_Msk |
| D3PMR1 | MR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR21_Msk |
| D3PMR1 | MR25 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR1_MR25_Msk |
| D3PCR1L | PCS0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS0_Msk |
| D3PCR1L | PCS1 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS1_Msk |
| D3PCR1L | PCS2 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS2_Msk |
| D3PCR1L | PCS3 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS3_Msk |
| D3PCR1L | PCS4 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS4_Msk |
| D3PCR1L | PCS5 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS5_Msk |
| D3PCR1L | PCS6 | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS6_Msk |
| D3PCR1L | PCS7 | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS7_Msk |
| D3PCR1L | PCS8 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS8_Msk |
| D3PCR1L | PCS9 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS9_Msk |
| D3PCR1L | PCS10 | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS10_Msk |
| D3PCR1L | PCS11 | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS11_Msk |
| D3PCR1L | PCS12 | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS12_Msk |
| D3PCR1L | PCS13 | 27:26 | 0xC000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS13_Msk |
| D3PCR1L | PCS14 | 29:28 | 0x30000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS14_Msk |
| D3PCR1L | PCS15 | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1L_PCS15_Msk |
| D3PCR1H | PCS19 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1H_PCS19_Msk |
| D3PCR1H | PCS20 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1H_PCS20_Msk |
| D3PCR1H | PCS21 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1H_PCS21_Msk |
| D3PCR1H | PCS25 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR1H_PCS25_Msk |
| RTSR2 | TR49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR2_TR49_Msk |
| RTSR2 | TR51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR2_TR51_Msk |
| FTSR2 | TR49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR2_TR49_Msk |
| FTSR2 | TR51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR2_TR51_Msk |
| SWIER2 | SWIER49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER2_SWIER49_Msk |
| SWIER2 | SWIER51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER2_SWIER51_Msk |
| D3PMR2 | MR34 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR34_Msk |
| D3PMR2 | MR35 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR35_Msk |
| D3PMR2 | MR41 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR41_Msk |
| D3PMR2 | MR48 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR48_Msk |
| D3PMR2 | MR49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR49_Msk |
| D3PMR2 | MR50 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR50_Msk |
| D3PMR2 | MR51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR51_Msk |
| D3PMR2 | MR52 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR52_Msk |
| D3PMR2 | MR53 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PMR2_MR53_Msk |
| D3PCR2L | PCS34 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2L_PCS34_Msk |
| D3PCR2L | PCS35 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2L_PCS35_Msk |
| D3PCR2L | PCS41 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2L_PCS41_Msk |
| D3PCR2H | PCS48 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS48_Msk |
| D3PCR2H | PCS49 | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS49_Msk |
| D3PCR2H | PCS50 | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS50_Msk |
| D3PCR2H | PCS51 | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS51_Msk |
| D3PCR2H | PCS52 | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS52_Msk |
| D3PCR2H | PCS53 | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:EXTI_D3PCR2H_PCS53_Msk |
| RTSR3 | TR82 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR3_TR82_Msk |
| RTSR3 | TR84 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR3_TR84_Msk |
| RTSR3 | TR85 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR3_TR85_Msk |
| RTSR3 | TR86 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR3_TR86_Msk |
| FTSR3 | TR82 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR3_TR82_Msk |
| FTSR3 | TR84 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR3_TR84_Msk |
| FTSR3 | TR85 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR3_TR85_Msk |
| FTSR3 | TR86 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR3_TR86_Msk |
| IMR1 | IM | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR1_IM_Msk |
| EMR1 | EM | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM_Msk |
| PR1 | PR | 21:0 | 0x3FFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR1_PR_Msk |
| IMR2 | IM32 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM32_Msk |
| IMR2 | IM33 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM33_Msk |
| IMR2 | IM34 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM34_Msk |
| IMR2 | IM35 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM35_Msk |
| IMR2 | IM36 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM36_Msk |
| IMR2 | IM37 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM37_Msk |
| IMR2 | IM38 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM38_Msk |
| IMR2 | IM39 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM39_Msk |
| IMR2 | IM40 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM40_Msk |
| IMR2 | IM41 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM41_Msk |
| IMR2 | IM42 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM42_Msk |
| IMR2 | IM43 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM43_Msk |
| IMR2 | IM44 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM44_Msk |
| IMR2 | IM46 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM46_Msk |
| IMR2 | IM47 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM47_Msk |
| IMR2 | IM48 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM48_Msk |
| IMR2 | IM49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM49_Msk |
| IMR2 | IM50 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM50_Msk |
| IMR2 | IM51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM51_Msk |
| IMR2 | IM52 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM52_Msk |
| IMR2 | IM53 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM53_Msk |
| IMR2 | IM54 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM54_Msk |
| IMR2 | IM55 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM55_Msk |
| IMR2 | IM56 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM56_Msk |
| IMR2 | IM57 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM57_Msk |
| IMR2 | IM58 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM58_Msk |
| IMR2 | IM59 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM59_Msk |
| IMR2 | IM60 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM60_Msk |
| IMR2 | IM61 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM61_Msk |
| IMR2 | IM62 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM62_Msk |
| IMR2 | IM63 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM63_Msk |
| EMR2 | EM32 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM32_Msk |
| EMR2 | EM33 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM33_Msk |
| EMR2 | EM34 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM34_Msk |
| EMR2 | EM35 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM35_Msk |
| EMR2 | EM36 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM36_Msk |
| EMR2 | EM37 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM37_Msk |
| EMR2 | EM38 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM38_Msk |
| EMR2 | EM39 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM39_Msk |
| EMR2 | EM40 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM40_Msk |
| EMR2 | EM41 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM41_Msk |
| EMR2 | EM42 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM42_Msk |
| EMR2 | EM43 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM43_Msk |
| EMR2 | EM44 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM44_Msk |
| EMR2 | EM46 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM46_Msk |
| EMR2 | EM47 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM47_Msk |
| EMR2 | EM48 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM48_Msk |
| EMR2 | EM49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM49_Msk |
| EMR2 | EM50 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM50_Msk |
| EMR2 | EM51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM51_Msk |
| EMR2 | EM52 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM52_Msk |
| EMR2 | EM53 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM53_Msk |
| EMR2 | EM54 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM54_Msk |
| EMR2 | EM55 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM55_Msk |
| EMR2 | EM56 | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM56_Msk |
| EMR2 | EM57 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM57_Msk |
| EMR2 | EM58 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM58_Msk |
| EMR2 | EM59 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM59_Msk |
| EMR2 | EM60 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM60_Msk |
| EMR2 | EM61 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM61_Msk |
| EMR2 | EM62 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM62_Msk |
| EMR2 | EM63 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM63_Msk |
| PR2 | PR49 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR2_PR49_Msk |
| PR2 | PR51 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR2_PR51_Msk |
| IMR3 | IM64 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM64_Msk |
| IMR3 | IM65 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM65_Msk |
| IMR3 | IM66 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM66_Msk |
| IMR3 | IM67 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM67_Msk |
| IMR3 | IM68 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM68_Msk |
| IMR3 | IM69 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM69_Msk |
| IMR3 | IM70 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM70_Msk |
| IMR3 | IM71 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM71_Msk |
| IMR3 | IM72 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM72_Msk |
| IMR3 | IM73 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM73_Msk |
| IMR3 | IM74 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM74_Msk |
| IMR3 | IM75 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM75_Msk |
| IMR3 | IM76 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM76_Msk |
| IMR3 | IM77 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM77_Msk |
| IMR3 | IM78 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM78_Msk |
| IMR3 | IM79 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM79_Msk |
| IMR3 | IM80 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM80_Msk |
| IMR3 | IM82 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM82_Msk |
| IMR3 | IM84 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM84_Msk |
| IMR3 | IM85 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM85_Msk |
| IMR3 | IM86 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM86_Msk |
| IMR3 | IM87 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR3_IM87_Msk |
| PR3 | PR82 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR3_PR82_Msk |
| PR3 | PR84 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR3_PR84_Msk |
| PR3 | PR85 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR3_PR85_Msk |
| PR3 | PR86 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR3_PR86_Msk |

## Operating semantics unavailable

**exti: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps (the affected register's entire bit-field set is withheld):

- SWIER3: bit fields withheld: UNSUPPORTED_MASK: EXTI_SWIER3_SWI_Msk: non-contiguous bit field without an exact declared component partition
- EMR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_EMR3_EM_Msk: non-contiguous bit field without an exact declared component partition

Compound declaration masks:

- Compound mask EXTI_RTSR2_TR_Msk=0xA0000 (header:EXTI_RTSR2_TR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_RTSR2_TR49_Msk=0x20000 (header:EXTI_RTSR2_TR49_Msk); EXTI_RTSR2_TR51_Msk=0x80000 (header:EXTI_RTSR2_TR51_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_FTSR2_TR_Msk=0xA0000 (header:EXTI_FTSR2_TR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_FTSR2_TR49_Msk=0x20000 (header:EXTI_FTSR2_TR49_Msk); EXTI_FTSR2_TR51_Msk=0x80000 (header:EXTI_FTSR2_TR51_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_RTSR3_TR_Msk=0x740000 (header:EXTI_RTSR3_TR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_RTSR3_TR82_Msk=0x40000 (header:EXTI_RTSR3_TR82_Msk); EXTI_RTSR3_TR84_Msk=0x100000 (header:EXTI_RTSR3_TR84_Msk); EXTI_RTSR3_TR85_Msk=0x200000 (header:EXTI_RTSR3_TR85_Msk); EXTI_RTSR3_TR86_Msk=0x400000 (header:EXTI_RTSR3_TR86_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_FTSR3_TR_Msk=0x740000 (header:EXTI_FTSR3_TR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_FTSR3_TR82_Msk=0x40000 (header:EXTI_FTSR3_TR82_Msk); EXTI_FTSR3_TR84_Msk=0x100000 (header:EXTI_FTSR3_TR84_Msk); EXTI_FTSR3_TR85_Msk=0x200000 (header:EXTI_FTSR3_TR85_Msk); EXTI_FTSR3_TR86_Msk=0x400000 (header:EXTI_FTSR3_TR86_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_IMR2_IM_Msk=0xFFFFDFFF (header:EXTI_IMR2_IM_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_IMR2_IM32_Msk=0x1 (header:EXTI_IMR2_IM32_Msk); EXTI_IMR2_IM33_Msk=0x2 (header:EXTI_IMR2_IM33_Msk); EXTI_IMR2_IM34_Msk=0x4 (header:EXTI_IMR2_IM34_Msk); EXTI_IMR2_IM35_Msk=0x8 (header:EXTI_IMR2_IM35_Msk); EXTI_IMR2_IM36_Msk=0x10 (header:EXTI_IMR2_IM36_Msk); EXTI_IMR2_IM37_Msk=0x20 (header:EXTI_IMR2_IM37_Msk); EXTI_IMR2_IM38_Msk=0x40 (header:EXTI_IMR2_IM38_Msk); EXTI_IMR2_IM39_Msk=0x80 (header:EXTI_IMR2_IM39_Msk); EXTI_IMR2_IM40_Msk=0x100 (header:EXTI_IMR2_IM40_Msk); EXTI_IMR2_IM41_Msk=0x200 (header:EXTI_IMR2_IM41_Msk); EXTI_IMR2_IM42_Msk=0x400 (header:EXTI_IMR2_IM42_Msk); EXTI_IMR2_IM43_Msk=0x800 (header:EXTI_IMR2_IM43_Msk); EXTI_IMR2_IM44_Msk=0x1000 (header:EXTI_IMR2_IM44_Msk); EXTI_IMR2_IM46_Msk=0x4000 (header:EXTI_IMR2_IM46_Msk); EXTI_IMR2_IM47_Msk=0x8000 (header:EXTI_IMR2_IM47_Msk); EXTI_IMR2_IM48_Msk=0x10000 (header:EXTI_IMR2_IM48_Msk); EXTI_IMR2_IM49_Msk=0x20000 (header:EXTI_IMR2_IM49_Msk); EXTI_IMR2_IM50_Msk=0x40000 (header:EXTI_IMR2_IM50_Msk); EXTI_IMR2_IM51_Msk=0x80000 (header:EXTI_IMR2_IM51_Msk); EXTI_IMR2_IM52_Msk=0x100000 (header:EXTI_IMR2_IM52_Msk); EXTI_IMR2_IM53_Msk=0x200000 (header:EXTI_IMR2_IM53_Msk); EXTI_IMR2_IM54_Msk=0x400000 (header:EXTI_IMR2_IM54_Msk); EXTI_IMR2_IM55_Msk=0x800000 (header:EXTI_IMR2_IM55_Msk); EXTI_IMR2_IM56_Msk=0x1000000 (header:EXTI_IMR2_IM56_Msk); EXTI_IMR2_IM57_Msk=0x2000000 (header:EXTI_IMR2_IM57_Msk); EXTI_IMR2_IM58_Msk=0x4000000 (header:EXTI_IMR2_IM58_Msk); EXTI_IMR2_IM59_Msk=0x8000000 (header:EXTI_IMR2_IM59_Msk); EXTI_IMR2_IM60_Msk=0x10000000 (header:EXTI_IMR2_IM60_Msk); EXTI_IMR2_IM61_Msk=0x20000000 (header:EXTI_IMR2_IM61_Msk); EXTI_IMR2_IM62_Msk=0x40000000 (header:EXTI_IMR2_IM62_Msk); EXTI_IMR2_IM63_Msk=0x80000000 (header:EXTI_IMR2_IM63_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_EMR2_EM_Msk=0xFFFFDFFF (header:EXTI_EMR2_EM_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_EMR2_EM32_Msk=0x1 (header:EXTI_EMR2_EM32_Msk); EXTI_EMR2_EM33_Msk=0x2 (header:EXTI_EMR2_EM33_Msk); EXTI_EMR2_EM34_Msk=0x4 (header:EXTI_EMR2_EM34_Msk); EXTI_EMR2_EM35_Msk=0x8 (header:EXTI_EMR2_EM35_Msk); EXTI_EMR2_EM36_Msk=0x10 (header:EXTI_EMR2_EM36_Msk); EXTI_EMR2_EM37_Msk=0x20 (header:EXTI_EMR2_EM37_Msk); EXTI_EMR2_EM38_Msk=0x40 (header:EXTI_EMR2_EM38_Msk); EXTI_EMR2_EM39_Msk=0x80 (header:EXTI_EMR2_EM39_Msk); EXTI_EMR2_EM40_Msk=0x100 (header:EXTI_EMR2_EM40_Msk); EXTI_EMR2_EM41_Msk=0x200 (header:EXTI_EMR2_EM41_Msk); EXTI_EMR2_EM42_Msk=0x400 (header:EXTI_EMR2_EM42_Msk); EXTI_EMR2_EM43_Msk=0x800 (header:EXTI_EMR2_EM43_Msk); EXTI_EMR2_EM44_Msk=0x1000 (header:EXTI_EMR2_EM44_Msk); EXTI_EMR2_EM46_Msk=0x4000 (header:EXTI_EMR2_EM46_Msk); EXTI_EMR2_EM47_Msk=0x8000 (header:EXTI_EMR2_EM47_Msk); EXTI_EMR2_EM48_Msk=0x10000 (header:EXTI_EMR2_EM48_Msk); EXTI_EMR2_EM49_Msk=0x20000 (header:EXTI_EMR2_EM49_Msk); EXTI_EMR2_EM50_Msk=0x40000 (header:EXTI_EMR2_EM50_Msk); EXTI_EMR2_EM51_Msk=0x80000 (header:EXTI_EMR2_EM51_Msk); EXTI_EMR2_EM52_Msk=0x100000 (header:EXTI_EMR2_EM52_Msk); EXTI_EMR2_EM53_Msk=0x200000 (header:EXTI_EMR2_EM53_Msk); EXTI_EMR2_EM54_Msk=0x400000 (header:EXTI_EMR2_EM54_Msk); EXTI_EMR2_EM55_Msk=0x800000 (header:EXTI_EMR2_EM55_Msk); EXTI_EMR2_EM56_Msk=0x1000000 (header:EXTI_EMR2_EM56_Msk); EXTI_EMR2_EM57_Msk=0x2000000 (header:EXTI_EMR2_EM57_Msk); EXTI_EMR2_EM58_Msk=0x4000000 (header:EXTI_EMR2_EM58_Msk); EXTI_EMR2_EM59_Msk=0x8000000 (header:EXTI_EMR2_EM59_Msk); EXTI_EMR2_EM60_Msk=0x10000000 (header:EXTI_EMR2_EM60_Msk); EXTI_EMR2_EM61_Msk=0x20000000 (header:EXTI_EMR2_EM61_Msk); EXTI_EMR2_EM62_Msk=0x40000000 (header:EXTI_EMR2_EM62_Msk); EXTI_EMR2_EM63_Msk=0x80000000 (header:EXTI_EMR2_EM63_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_PR2_PR_Msk=0xA0000 (header:EXTI_PR2_PR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_PR2_PR49_Msk=0x20000 (header:EXTI_PR2_PR49_Msk); EXTI_PR2_PR51_Msk=0x80000 (header:EXTI_PR2_PR51_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_IMR3_IM_Msk=0xF5FFFF (header:EXTI_IMR3_IM_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_IMR3_IM64_Msk=0x1 (header:EXTI_IMR3_IM64_Msk); EXTI_IMR3_IM65_Msk=0x2 (header:EXTI_IMR3_IM65_Msk); EXTI_IMR3_IM66_Msk=0x4 (header:EXTI_IMR3_IM66_Msk); EXTI_IMR3_IM67_Msk=0x8 (header:EXTI_IMR3_IM67_Msk); EXTI_IMR3_IM68_Msk=0x10 (header:EXTI_IMR3_IM68_Msk); EXTI_IMR3_IM69_Msk=0x20 (header:EXTI_IMR3_IM69_Msk); EXTI_IMR3_IM70_Msk=0x40 (header:EXTI_IMR3_IM70_Msk); EXTI_IMR3_IM71_Msk=0x80 (header:EXTI_IMR3_IM71_Msk); EXTI_IMR3_IM72_Msk=0x100 (header:EXTI_IMR3_IM72_Msk); EXTI_IMR3_IM73_Msk=0x200 (header:EXTI_IMR3_IM73_Msk); EXTI_IMR3_IM74_Msk=0x400 (header:EXTI_IMR3_IM74_Msk); EXTI_IMR3_IM75_Msk=0x800 (header:EXTI_IMR3_IM75_Msk); EXTI_IMR3_IM76_Msk=0x1000 (header:EXTI_IMR3_IM76_Msk); EXTI_IMR3_IM77_Msk=0x2000 (header:EXTI_IMR3_IM77_Msk); EXTI_IMR3_IM78_Msk=0x4000 (header:EXTI_IMR3_IM78_Msk); EXTI_IMR3_IM79_Msk=0x8000 (header:EXTI_IMR3_IM79_Msk); EXTI_IMR3_IM80_Msk=0x10000 (header:EXTI_IMR3_IM80_Msk); EXTI_IMR3_IM82_Msk=0x40000 (header:EXTI_IMR3_IM82_Msk); EXTI_IMR3_IM84_Msk=0x100000 (header:EXTI_IMR3_IM84_Msk); EXTI_IMR3_IM85_Msk=0x200000 (header:EXTI_IMR3_IM85_Msk); EXTI_IMR3_IM86_Msk=0x400000 (header:EXTI_IMR3_IM86_Msk); EXTI_IMR3_IM87_Msk=0x800000 (header:EXTI_IMR3_IM87_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.
- Compound mask EXTI_PR3_PR_Msk=0x740000 (header:EXTI_PR3_PR_Msk) is represented by its separately declared, disjoint contiguous components: EXTI_PR3_PR82_Msk=0x40000 (header:EXTI_PR3_PR82_Msk); EXTI_PR3_PR84_Msk=0x100000 (header:EXTI_PR3_PR84_Msk); EXTI_PR3_PR85_Msk=0x200000 (header:EXTI_PR3_PR85_Msk); EXTI_PR3_PR86_Msk=0x400000 (header:EXTI_PR3_PR86_Msk). Their bitwise union exactly equals the compound mask; encodings remain unreviewed.

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
