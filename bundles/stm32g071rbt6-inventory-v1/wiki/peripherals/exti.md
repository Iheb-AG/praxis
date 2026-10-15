# EXTI — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| EXTI | 0x40021800 | Not asserted | Not asserted | header:EXTI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RTSR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RTSR1 | 1 | 4 |
| FTSR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FTSR1 | 1 | 4 |
| SWIER1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.SWIER1 | 1 | 4 |
| RPR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.RPR1 | 1 | 4 |
| FPR1 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.FPR1 | 1 | 4 |
| EXTICR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EXTICR | 4 | 4 |
| IMR1 | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR1 | 1 | 4 |
| EMR1 | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR1 | 1 | 4 |
| IMR2 | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.IMR2 | 1 | 4 |
| EMR2 | 0x094 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:EXTI_TypeDef.EMR2 | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| RTSR1 | RT0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT0_Msk |
| RTSR1 | RT1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT1_Msk |
| RTSR1 | RT2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT2_Msk |
| RTSR1 | RT3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT3_Msk |
| RTSR1 | RT4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT4_Msk |
| RTSR1 | RT5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT5_Msk |
| RTSR1 | RT6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT6_Msk |
| RTSR1 | RT7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT7_Msk |
| RTSR1 | RT8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT8_Msk |
| RTSR1 | RT9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT9_Msk |
| RTSR1 | RT10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT10_Msk |
| RTSR1 | RT11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT11_Msk |
| RTSR1 | RT12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT12_Msk |
| RTSR1 | RT13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT13_Msk |
| RTSR1 | RT14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT14_Msk |
| RTSR1 | RT15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT15_Msk |
| RTSR1 | RT16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT16_Msk |
| RTSR1 | RT17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT17_Msk |
| RTSR1 | RT18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR1_RT18_Msk |
| FTSR1 | FT0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT0_Msk |
| FTSR1 | FT1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT1_Msk |
| FTSR1 | FT2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT2_Msk |
| FTSR1 | FT3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT3_Msk |
| FTSR1 | FT4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT4_Msk |
| FTSR1 | FT5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT5_Msk |
| FTSR1 | FT6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT6_Msk |
| FTSR1 | FT7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT7_Msk |
| FTSR1 | FT8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT8_Msk |
| FTSR1 | FT9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT9_Msk |
| FTSR1 | FT10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT10_Msk |
| FTSR1 | FT11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT11_Msk |
| FTSR1 | FT12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT12_Msk |
| FTSR1 | FT13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT13_Msk |
| FTSR1 | FT14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT14_Msk |
| FTSR1 | FT15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT15_Msk |
| FTSR1 | FT16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT16_Msk |
| FTSR1 | FT17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT17_Msk |
| FTSR1 | FT18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR1_FT18_Msk |
| SWIER1 | SWI0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI0_Msk |
| SWIER1 | SWI1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI1_Msk |
| SWIER1 | SWI2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI2_Msk |
| SWIER1 | SWI3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI3_Msk |
| SWIER1 | SWI4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI4_Msk |
| SWIER1 | SWI5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI5_Msk |
| SWIER1 | SWI6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI6_Msk |
| SWIER1 | SWI7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI7_Msk |
| SWIER1 | SWI8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI8_Msk |
| SWIER1 | SWI9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI9_Msk |
| SWIER1 | SWI10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI10_Msk |
| SWIER1 | SWI11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI11_Msk |
| SWIER1 | SWI12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI12_Msk |
| SWIER1 | SWI13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI13_Msk |
| SWIER1 | SWI14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI14_Msk |
| SWIER1 | SWI15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI15_Msk |
| SWIER1 | SWI16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI16_Msk |
| SWIER1 | SWI17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI17_Msk |
| SWIER1 | SWI18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER1_SWI18_Msk |
| RPR1 | RPIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF0_Msk |
| RPR1 | RPIF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF1_Msk |
| RPR1 | RPIF2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF2_Msk |
| RPR1 | RPIF3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF3_Msk |
| RPR1 | RPIF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF4_Msk |
| RPR1 | RPIF5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF5_Msk |
| RPR1 | RPIF6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF6_Msk |
| RPR1 | RPIF7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF7_Msk |
| RPR1 | RPIF8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF8_Msk |
| RPR1 | RPIF9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF9_Msk |
| RPR1 | RPIF10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF10_Msk |
| RPR1 | RPIF11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF11_Msk |
| RPR1 | RPIF12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF12_Msk |
| RPR1 | RPIF13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF13_Msk |
| RPR1 | RPIF14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF14_Msk |
| RPR1 | RPIF15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF15_Msk |
| RPR1 | RPIF16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF16_Msk |
| RPR1 | RPIF17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF17_Msk |
| RPR1 | RPIF18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RPR1_RPIF18_Msk |
| FPR1 | FPIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF0_Msk |
| FPR1 | FPIF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF1_Msk |
| FPR1 | FPIF2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF2_Msk |
| FPR1 | FPIF3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF3_Msk |
| FPR1 | FPIF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF4_Msk |
| FPR1 | FPIF5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF5_Msk |
| FPR1 | FPIF6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF6_Msk |
| FPR1 | FPIF7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF7_Msk |
| FPR1 | FPIF8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF8_Msk |
| FPR1 | FPIF9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF9_Msk |
| FPR1 | FPIF10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF10_Msk |
| FPR1 | FPIF11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF11_Msk |
| FPR1 | FPIF12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF12_Msk |
| FPR1 | FPIF13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF13_Msk |
| FPR1 | FPIF14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF14_Msk |
| FPR1 | FPIF15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF15_Msk |
| FPR1 | FPIF16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF16_Msk |
| FPR1 | FPIF17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF17_Msk |
| FPR1 | FPIF18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FPR1_FPIF18_Msk |
| EMR1 | EM0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM0_Msk |
| EMR1 | EM1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM1_Msk |
| EMR1 | EM2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM2_Msk |
| EMR1 | EM3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM3_Msk |
| EMR1 | EM4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM4_Msk |
| EMR1 | EM5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM5_Msk |
| EMR1 | EM6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM6_Msk |
| EMR1 | EM7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM7_Msk |
| EMR1 | EM8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM8_Msk |
| EMR1 | EM9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM9_Msk |
| EMR1 | EM10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM10_Msk |
| EMR1 | EM11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM11_Msk |
| EMR1 | EM12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM12_Msk |
| EMR1 | EM13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM13_Msk |
| EMR1 | EM14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM14_Msk |
| EMR1 | EM15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM15_Msk |
| EMR1 | EM16 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM16_Msk |
| EMR1 | EM17 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM17_Msk |
| EMR1 | EM18 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM18_Msk |
| EMR1 | EM19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM19_Msk |
| EMR1 | EM21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM21_Msk |
| EMR1 | EM23 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM23_Msk |
| EMR1 | EM25 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM25_Msk |
| EMR1 | EM26 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM26_Msk |
| EMR1 | EM27 | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM27_Msk |
| EMR1 | EM28 | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM28_Msk |
| EMR1 | EM29 | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM29_Msk |
| EMR1 | EM30 | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM30_Msk |
| EMR1 | EM31 | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR1_EM31_Msk |
| IMR2 | IM | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR2_IM_Msk |
| EMR2 | EM32 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM32_Msk |
| EMR2 | EM33 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR2_EM33_Msk |

## Operating semantics unavailable

**exti: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- IMR1: bit fields withheld: UNSUPPORTED_MASK: EXTI_IMR1_IM_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
