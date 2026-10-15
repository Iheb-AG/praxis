# SCB — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SCB | 0xE000ED00 | Not asserted | Not asserted | core_cm0plus_h:SCB_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPUID | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.CPUID | 1 | 4 |
| ICSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.ICSR | 1 | 4 |
| VTOR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.VTOR | 1 | 4 |
| AIRCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.AIRCR | 1 | 4 |
| SCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.SCR | 1 | 4 |
| CCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.CCR | 1 | 4 |
| SHP | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.SHP | 2 | 4 |
| SHCSR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm0plus_h:SCB_Type.SHCSR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CPUID | REVISION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CPUID_REVISION_Msk |
| CPUID | PARTNO | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CPUID_PARTNO_Msk |
| CPUID | ARCHITECTURE | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CPUID_ARCHITECTURE_Msk |
| CPUID | VARIANT | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CPUID_VARIANT_Msk |
| CPUID | IMPLEMENTER | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CPUID_IMPLEMENTER_Msk |
| ICSR | VECTACTIVE | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_VECTACTIVE_Msk |
| ICSR | VECTPENDING | 20:12 | 0x1FF000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_VECTPENDING_Msk |
| ICSR | ISRPENDING | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_ISRPENDING_Msk |
| ICSR | ISRPREEMPT | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_ISRPREEMPT_Msk |
| ICSR | PENDSTCLR | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_PENDSTCLR_Msk |
| ICSR | PENDSTSET | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_PENDSTSET_Msk |
| ICSR | PENDSVCLR | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_PENDSVCLR_Msk |
| ICSR | PENDSVSET | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_PENDSVSET_Msk |
| ICSR | NMIPENDSET | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_ICSR_NMIPENDSET_Msk |
| VTOR | TBLOFF | 31:8 | 0xFFFFFF00 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_VTOR_TBLOFF_Msk |
| AIRCR | VECTCLRACTIVE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_AIRCR_VECTCLRACTIVE_Msk |
| AIRCR | SYSRESETREQ | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_AIRCR_SYSRESETREQ_Msk |
| AIRCR | ENDIANESS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_AIRCR_ENDIANESS_Msk |
| AIRCR | VECTKEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_AIRCR_VECTKEY_Msk |
| SCR | SLEEPONEXIT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_SCR_SLEEPONEXIT_Msk |
| SCR | SLEEPDEEP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_SCR_SLEEPDEEP_Msk |
| SCR | SEVONPEND | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_SCR_SEVONPEND_Msk |
| CCR | UNALIGN_TRP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CCR_UNALIGN_TRP_Msk |
| CCR | STKALIGN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_CCR_STKALIGN_Msk |
| SHCSR | SVCALLPENDED | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | core_cm0plus_h:SCB_SHCSR_SVCALLPENDED_Msk |

## Operating semantics unavailable

**scb: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
