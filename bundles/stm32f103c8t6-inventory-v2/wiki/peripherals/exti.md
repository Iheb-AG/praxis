# EXTI — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| EXTI | 0x40010400 | Not asserted | Not asserted | header:EXTI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR |
| EMR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR |
| RTSR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RTSR |
| FTSR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FTSR |
| SWIER | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.SWIER |
| PR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.PR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| IMR | MR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR0_Msk |
| IMR | MR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR1_Msk |
| IMR | MR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR2_Msk |
| IMR | MR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR3_Msk |
| IMR | MR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR4_Msk |
| IMR | MR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR5_Msk |
| IMR | MR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR6_Msk |
| IMR | MR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR7_Msk |
| IMR | MR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR8_Msk |
| IMR | MR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR9_Msk |
| IMR | MR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR10_Msk |
| IMR | MR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR11_Msk |
| IMR | MR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR12_Msk |
| IMR | MR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR13_Msk |
| IMR | MR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR14_Msk |
| IMR | MR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR15_Msk |
| IMR | MR16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR16_Msk |
| IMR | MR17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR17_Msk |
| IMR | MR18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR18_Msk |
| EMR | MR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR0_Msk |
| EMR | MR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR1_Msk |
| EMR | MR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR2_Msk |
| EMR | MR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR3_Msk |
| EMR | MR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR4_Msk |
| EMR | MR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR5_Msk |
| EMR | MR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR6_Msk |
| EMR | MR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR7_Msk |
| EMR | MR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR8_Msk |
| EMR | MR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR9_Msk |
| EMR | MR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR10_Msk |
| EMR | MR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR11_Msk |
| EMR | MR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR12_Msk |
| EMR | MR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR13_Msk |
| EMR | MR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR14_Msk |
| EMR | MR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR15_Msk |
| EMR | MR16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR16_Msk |
| EMR | MR17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR17_Msk |
| EMR | MR18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR18_Msk |
| RTSR | TR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR0_Msk |
| RTSR | TR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR1_Msk |
| RTSR | TR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR2_Msk |
| RTSR | TR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR3_Msk |
| RTSR | TR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR4_Msk |
| RTSR | TR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR5_Msk |
| RTSR | TR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR6_Msk |
| RTSR | TR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR7_Msk |
| RTSR | TR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR8_Msk |
| RTSR | TR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR9_Msk |
| RTSR | TR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR10_Msk |
| RTSR | TR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR11_Msk |
| RTSR | TR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR12_Msk |
| RTSR | TR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR13_Msk |
| RTSR | TR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR14_Msk |
| RTSR | TR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR15_Msk |
| RTSR | TR16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR16_Msk |
| RTSR | TR17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR17_Msk |
| RTSR | TR18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR18_Msk |
| FTSR | TR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR0_Msk |
| FTSR | TR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR1_Msk |
| FTSR | TR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR2_Msk |
| FTSR | TR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR3_Msk |
| FTSR | TR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR4_Msk |
| FTSR | TR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR5_Msk |
| FTSR | TR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR6_Msk |
| FTSR | TR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR7_Msk |
| FTSR | TR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR8_Msk |
| FTSR | TR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR9_Msk |
| FTSR | TR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR10_Msk |
| FTSR | TR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR11_Msk |
| FTSR | TR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR12_Msk |
| FTSR | TR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR13_Msk |
| FTSR | TR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR14_Msk |
| FTSR | TR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR15_Msk |
| FTSR | TR16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR16_Msk |
| FTSR | TR17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR17_Msk |
| FTSR | TR18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR18_Msk |
| SWIER | SWIER0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER0_Msk |
| SWIER | SWIER1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER1_Msk |
| SWIER | SWIER2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER2_Msk |
| SWIER | SWIER3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER3_Msk |
| SWIER | SWIER4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER4_Msk |
| SWIER | SWIER5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER5_Msk |
| SWIER | SWIER6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER6_Msk |
| SWIER | SWIER7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER7_Msk |
| SWIER | SWIER8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER8_Msk |
| SWIER | SWIER9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER9_Msk |
| SWIER | SWIER10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER10_Msk |
| SWIER | SWIER11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER11_Msk |
| SWIER | SWIER12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER12_Msk |
| SWIER | SWIER13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER13_Msk |
| SWIER | SWIER14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER14_Msk |
| SWIER | SWIER15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER15_Msk |
| SWIER | SWIER16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER16_Msk |
| SWIER | SWIER17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER17_Msk |
| SWIER | SWIER18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER18_Msk |
| PR | PR0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR0_Msk |
| PR | PR1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR1_Msk |
| PR | PR2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR2_Msk |
| PR | PR3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR3_Msk |
| PR | PR4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR4_Msk |
| PR | PR5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR5_Msk |
| PR | PR6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR6_Msk |
| PR | PR7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR7_Msk |
| PR | PR8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR8_Msk |
| PR | PR9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR9_Msk |
| PR | PR10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR10_Msk |
| PR | PR11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR11_Msk |
| PR | PR12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR12_Msk |
| PR | PR13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR13_Msk |
| PR | PR14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR14_Msk |
| PR | PR15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR15_Msk |
| PR | PR16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR16_Msk |
| PR | PR17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR17_Msk |
| PR | PR18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR18_Msk |

## Operating semantics unavailable

**exti: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
