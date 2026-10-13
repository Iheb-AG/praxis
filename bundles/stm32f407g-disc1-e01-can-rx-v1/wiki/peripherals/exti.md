# EXTI: reviewed PA0 interrupt subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/syscfg]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| EXTI | 0x40013C00 | APB2 | Explicitly selected HSI scenario; see RCC and reviewed notes | header:EXTI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMR | 0x000 | 32 | — | RW | 0x0 | Interrupt mask; bit=1 unmasks. | header:EXTI_TypeDef.IMR; header:EXTI_TypeDef.IMR; rm_exti_mask:page:386 |
| EMR | 0x004 | 32 | — | RW | 0x0 | Event mask; unused in interrupt-only workflow. | header:EXTI_TypeDef.EMR; header:EXTI_TypeDef.EMR; rm_exti_mask:page:386 |
| RTSR | 0x008 | 32 | — | RW | 0x0 | Rising-edge trigger; preserve unrelated lines. | header:EXTI_TypeDef.RTSR; header:EXTI_TypeDef.RTSR; rm_exti_edges:page:387 |
| FTSR | 0x00C | 32 | — | RW | 0x0 | Falling-edge trigger; preserve unrelated lines. | header:EXTI_TypeDef.FTSR; header:EXTI_TypeDef.FTSR; rm_exti_edges:page:387 |
| SWIER | 0x010 | 32 | — | mixed | 0x0 | Software request action; cleared through PR; unused. | header:EXTI_TypeDef.SWIER; header:EXTI_TypeDef.SWIER; rm_exti_pending:page:388 |
| PR | 0x014 | 32 | — | mixed | 0x0 | rc_w1: write-one-to-clear selected pending bits. Never generic read-modify-write. | header:EXTI_TypeDef.PR; header:EXTI_TypeDef.PR; rm_exti_pending:page:388 |

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
| IMR | MR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR19_Msk |
| IMR | MR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR20_Msk |
| IMR | MR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR21_Msk |
| IMR | MR22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_IMR_MR22_Msk |
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
| EMR | MR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR19_Msk |
| EMR | MR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR20_Msk |
| EMR | MR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR21_Msk |
| EMR | MR22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_EMR_MR22_Msk |
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
| RTSR | TR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR19_Msk |
| RTSR | TR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR20_Msk |
| RTSR | TR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR21_Msk |
| RTSR | TR22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_RTSR_TR22_Msk |
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
| FTSR | TR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR19_Msk |
| FTSR | TR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR20_Msk |
| FTSR | TR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR21_Msk |
| FTSR | TR22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_FTSR_TR22_Msk |
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
| SWIER | SWIER19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER19_Msk |
| SWIER | SWIER20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER20_Msk |
| SWIER | SWIER21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER21_Msk |
| SWIER | SWIER22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_SWIER_SWIER22_Msk |
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
| PR | PR19 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR19_Msk |
| PR | PR20 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR20_Msk |
| PR | PR21 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR21_Msk |
| PR | PR22 | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:EXTI_PR_PR22_Msk |

## Reviewed operating semantics

Supported operating subset: **EXTI line 0 on PA0**, both-edge USER button notification.
The board signal is active high with an external pull-down; GPIO must select input with
no internal pull. Check the board's SB20 path separately. Route PA0 through
[[peripherals/syscfg]] before unmasking line 0.

| Register | Line-zero behavior | Source |
| --- | --- | --- |
| IMR | bit0=0 masks interrupt request; bit0=1 unmasks | rm_exti_mask:page:386 |
| EMR | bit0 controls events; leave zero for interrupt-only use | rm_exti_mask:page:386 |
| RTSR | bit0=1 enables rising-edge detection | rm_exti_edges:page:387 |
| FTSR | bit0=1 enables falling-edge detection | rm_exti_edges:page:387 |
| SWIER | software event/request action; unused | rm_exti_pending:page:388 |
| PR | bit0 is **write-one-to-clear**; write PR=1, never PR|=1 | rm_exti_pending:page:388 |

Keep line 0 masked while configuring both edge selectors and handler state. Clear the
peripheral pending bit first, then NVIC pending, then configure priority/enable the line.
Restore global interrupts only after all sources are ready. Preserve other lines and
reserved bits. The ISR writes PR=1 and records a timestamp/generation counter; debounce
and press/release policy run outside the ISR. A single edge is not a debounced press.
Require a stable input for nominal 50 ms and a release before another press.

EXTI0_IRQn=6, vector slot 22, handler EXTI0_IRQHandler: `header:EXTI0_IRQn` and the
pinned startup vector. Header MR/IM aliases are explicitly selected as individual MR
bits in this profile; they do not become overlapping independent fields.
See [[peripherals/nvic]], [[peripherals/gpio]], [[schemas/board]] and [[sources]].

## Review

Reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
