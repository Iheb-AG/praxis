# SYSCFG: reviewed GPIO-to-EXTI routing

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SYSCFG | 0x40013800 | APB2 | Explicitly selected HSI scenario; see RCC and reviewed notes | header:SYSCFG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MEMRMP | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.MEMRMP |
| PMC | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.PMC |
| EXTICR0 | 0x008 | 32 | — | RW | 0x0 | GPIO-to-EXTI routing; replace only the selected nibble, preserve upper reserved bits. | header:SYSCFG_TypeDef.EXTICR[0]; header:SYSCFG_TypeDef.EXTICR; rm_syscfg1:page:293 |
| EXTICR1 | 0x00C | 32 | — | RW | 0x0 | GPIO-to-EXTI routing; replace only the selected nibble, preserve upper reserved bits. | header:SYSCFG_TypeDef.EXTICR[1]; header:SYSCFG_TypeDef.EXTICR; rm_syscfg1:page:293 |
| EXTICR2 | 0x010 | 32 | — | RW | 0x0 | GPIO-to-EXTI routing; replace only the selected nibble, preserve upper reserved bits. | header:SYSCFG_TypeDef.EXTICR[2]; header:SYSCFG_TypeDef.EXTICR; rm_syscfg2:page:294 |
| EXTICR3 | 0x014 | 32 | — | RW | 0x0 | GPIO-to-EXTI routing; replace only the selected nibble, preserve upper reserved bits. | header:SYSCFG_TypeDef.EXTICR[3]; header:SYSCFG_TypeDef.EXTICR; rm_syscfg3:page:295 |
| CMPCR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CMPCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MEMRMP | MEM_MODE | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_MEMRMP_MEM_MODE_Msk |
| PMC | MII_RMII_SEL | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMC_MII_RMII_SEL_Msk |
| EXTICR0 | EXTI0 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR1_EXTI0_Msk |
| EXTICR0 | EXTI1 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR1_EXTI1_Msk |
| EXTICR0 | EXTI2 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR1_EXTI2_Msk |
| EXTICR0 | EXTI3 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR1_EXTI3_Msk |
| EXTICR1 | EXTI4 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR2_EXTI4_Msk |
| EXTICR1 | EXTI5 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR2_EXTI5_Msk |
| EXTICR1 | EXTI6 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR2_EXTI6_Msk |
| EXTICR1 | EXTI7 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR2_EXTI7_Msk |
| EXTICR2 | EXTI8 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR3_EXTI8_Msk |
| EXTICR2 | EXTI9 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR3_EXTI9_Msk |
| EXTICR2 | EXTI10 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR3_EXTI10_Msk |
| EXTICR2 | EXTI11 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR3_EXTI11_Msk |
| EXTICR3 | EXTI12 | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR4_EXTI12_Msk |
| EXTICR3 | EXTI13 | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR4_EXTI13_Msk |
| EXTICR3 | EXTI14 | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR4_EXTI14_Msk |
| EXTICR3 | EXTI15 | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_EXTICR4_EXTI15_Msk |
| CMPCR | CMP_PD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CMPCR_CMP_PD_Msk |
| CMPCR | READY | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CMPCR_READY_Msk |

## Reviewed operating semantics

Supported operating subset: route **PA0 to EXTI0** through SYSCFG_EXTICR1.
Evidence: `rm_syscfg1:page:293`, RM0090 Rev22 section 9.2.3 (F405/407 section).

Enable RCC_APB2ENR.SYSCFGEN and read back the gate before accessing SYSCFG. The clock
and its enable bit are documented by `rm_apb2_gate:page:250`. SYSCFG is on APB2.
Keep EXTI0 masked and global interrupts disabled during routing. Replace only
SYSCFG->EXTICR[0] bits 3:0 with zero: 0000 selects PA0; 0001 would select PB0.
Preserve all other line-selection fields and reserved upper bits.

The declaration adapter explicitly expands EXTICR[4] into EXTICR0..EXTICR3, preserving
the C members EXTICR[0]..EXTICR[3] and offsets 0x08/0x0C/0x10/0x14. In this catalog,
EXTICR0 corresponds to the manual's **EXTICR1**, not a different silicon register.
The corresponding vendor macro prefixes are SYSCFG_EXTICR1..SYSCFG_EXTICR4.
All four route-register reset values are zero; other SYSCFG functions remain unreviewed.
Evidence: `rm_syscfg1:page:293`, `rm_syscfg2:page:294`, `rm_syscfg3:page:295`.

Do not reset SYSCFG wholesale to change one route. Board wiring and GPIO input setup
are separate prerequisites. See [[peripherals/gpio]], [[peripherals/exti]],
[[peripherals/rcc]], [[schemas/custom_pcb_netlist]] and [[sources]].

## Review

Reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
