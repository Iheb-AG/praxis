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
| IMR1 | IM | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR1_IM_Msk |
| EMR1 | EM | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM_Msk |
| PR1 | PR | 21:0 | 0x3FFFFF | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR1_PR_Msk |

## Operating semantics unavailable

**exti: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- RTSR2: bit fields withheld: UNSUPPORTED_MASK: EXTI_RTSR2_TR_Msk: non-contiguous bit field
- FTSR2: bit fields withheld: UNSUPPORTED_MASK: EXTI_FTSR2_TR_Msk: non-contiguous bit field
- RTSR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_RTSR3_TR_Msk: non-contiguous bit field
- FTSR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_FTSR3_TR_Msk: non-contiguous bit field
- SWIER3: bit fields withheld: UNSUPPORTED_MASK: EXTI_SWIER3_SWI_Msk: non-contiguous bit field
- IMR2: bit fields withheld: UNSUPPORTED_MASK: EXTI_IMR2_IM_Msk: non-contiguous bit field
- EMR2: bit fields withheld: UNSUPPORTED_MASK: EXTI_EMR2_EM_Msk: non-contiguous bit field
- PR2: bit fields withheld: UNSUPPORTED_MASK: EXTI_PR2_PR_Msk: non-contiguous bit field
- IMR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_IMR3_IM_Msk: non-contiguous bit field
- EMR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_EMR3_EM_Msk: non-contiguous bit field
- PR3: bit fields withheld: UNSUPPORTED_MASK: EXTI_PR3_PR_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
