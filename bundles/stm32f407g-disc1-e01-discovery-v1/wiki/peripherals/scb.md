# SCB — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SCB | 0xE000ED00 | Not asserted | Not asserted | cmsis_core:SCB_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPUID | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CPUID; cmsis_core:SCB_Type.CPUID | 1 | 4 |
| ICSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.ICSR; cmsis_core:SCB_Type.ICSR | 1 | 4 |
| VTOR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.VTOR; cmsis_core:SCB_Type.VTOR | 1 | 4 |
| AIRCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.AIRCR; cmsis_core:SCB_Type.AIRCR | 1 | 4 |
| SCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.SCR; cmsis_core:SCB_Type.SCR | 1 | 4 |
| CCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CCR; cmsis_core:SCB_Type.CCR | 1 | 4 |
| SHP | 0x018 | 8 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.SHP; cmsis_core:SCB_Type.SHP | 12 | 1 |
| SHCSR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.SHCSR; cmsis_core:SCB_Type.SHCSR | 1 | 4 |
| CFSR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CFSR; cmsis_core:SCB_Type.CFSR | 1 | 4 |
| HFSR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.HFSR; cmsis_core:SCB_Type.HFSR | 1 | 4 |
| DFSR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.DFSR; cmsis_core:SCB_Type.DFSR | 1 | 4 |
| MMFAR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.MMFAR; cmsis_core:SCB_Type.MMFAR | 1 | 4 |
| BFAR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.BFAR; cmsis_core:SCB_Type.BFAR | 1 | 4 |
| AFSR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.AFSR; cmsis_core:SCB_Type.AFSR | 1 | 4 |
| PFR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.PFR; cmsis_core:SCB_Type.PFR | 2 | 4 |
| DFR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.DFR; cmsis_core:SCB_Type.DFR | 1 | 4 |
| ADR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.ADR; cmsis_core:SCB_Type.ADR | 1 | 4 |
| MMFR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.MMFR; cmsis_core:SCB_Type.MMFR | 4 | 4 |
| ISAR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.ISAR; cmsis_core:SCB_Type.ISAR | 5 | 4 |
| CPACR | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CPACR; cmsis_core:SCB_Type.CPACR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CPUID | REVISION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_REVISION_Msk; cmsis_core:SCB_CPUID_REVISION_Msk |
| CPUID | PARTNO | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_PARTNO_Msk; cmsis_core:SCB_CPUID_PARTNO_Msk |
| CPUID | ARCHITECTURE | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_ARCHITECTURE_Msk; cmsis_core:SCB_CPUID_ARCHITECTURE_Msk |
| CPUID | VARIANT | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_VARIANT_Msk; cmsis_core:SCB_CPUID_VARIANT_Msk |
| CPUID | IMPLEMENTER | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_IMPLEMENTER_Msk; cmsis_core:SCB_CPUID_IMPLEMENTER_Msk |
| ICSR | VECTACTIVE | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_VECTACTIVE_Msk; cmsis_core:SCB_ICSR_VECTACTIVE_Msk |
| ICSR | RETTOBASE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_RETTOBASE_Msk; cmsis_core:SCB_ICSR_RETTOBASE_Msk |
| ICSR | VECTPENDING | 20:12 | 0x1FF000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_VECTPENDING_Msk; cmsis_core:SCB_ICSR_VECTPENDING_Msk |
| ICSR | ISRPENDING | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_ISRPENDING_Msk; cmsis_core:SCB_ICSR_ISRPENDING_Msk |
| ICSR | ISRPREEMPT | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_ISRPREEMPT_Msk; cmsis_core:SCB_ICSR_ISRPREEMPT_Msk |
| ICSR | PENDSTCLR | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_PENDSTCLR_Msk; cmsis_core:SCB_ICSR_PENDSTCLR_Msk |
| ICSR | PENDSTSET | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_PENDSTSET_Msk; cmsis_core:SCB_ICSR_PENDSTSET_Msk |
| ICSR | PENDSVCLR | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_PENDSVCLR_Msk; cmsis_core:SCB_ICSR_PENDSVCLR_Msk |
| ICSR | PENDSVSET | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_PENDSVSET_Msk; cmsis_core:SCB_ICSR_PENDSVSET_Msk |
| ICSR | NMIPENDSET | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_NMIPENDSET_Msk; cmsis_core:SCB_ICSR_NMIPENDSET_Msk |
| VTOR | TBLOFF | 31:7 | 0xFFFFFF80 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_VTOR_TBLOFF_Msk; cmsis_core:SCB_VTOR_TBLOFF_Msk |
| AIRCR | VECTRESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTRESET_Msk; cmsis_core:SCB_AIRCR_VECTRESET_Msk |
| AIRCR | VECTCLRACTIVE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTCLRACTIVE_Msk; cmsis_core:SCB_AIRCR_VECTCLRACTIVE_Msk |
| AIRCR | SYSRESETREQ | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_SYSRESETREQ_Msk; cmsis_core:SCB_AIRCR_SYSRESETREQ_Msk |
| AIRCR | PRIGROUP | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_PRIGROUP_Msk; cmsis_core:SCB_AIRCR_PRIGROUP_Msk |
| AIRCR | ENDIANESS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_ENDIANESS_Msk; cmsis_core:SCB_AIRCR_ENDIANESS_Msk |
| AIRCR | VECTKEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTKEY_Msk; cmsis_core:SCB_AIRCR_VECTKEY_Msk |
| SCR | SLEEPONEXIT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SLEEPONEXIT_Msk; cmsis_core:SCB_SCR_SLEEPONEXIT_Msk |
| SCR | SLEEPDEEP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SLEEPDEEP_Msk; cmsis_core:SCB_SCR_SLEEPDEEP_Msk |
| SCR | SEVONPEND | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SEVONPEND_Msk; cmsis_core:SCB_SCR_SEVONPEND_Msk |
| CCR | NONBASETHRDENA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_NONBASETHRDENA_Msk; cmsis_core:SCB_CCR_NONBASETHRDENA_Msk |
| CCR | USERSETMPEND | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_USERSETMPEND_Msk; cmsis_core:SCB_CCR_USERSETMPEND_Msk |
| CCR | UNALIGN_TRP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_UNALIGN_TRP_Msk; cmsis_core:SCB_CCR_UNALIGN_TRP_Msk |
| CCR | DIV_0_TRP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_DIV_0_TRP_Msk; cmsis_core:SCB_CCR_DIV_0_TRP_Msk |
| CCR | BFHFNMIGN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_BFHFNMIGN_Msk; cmsis_core:SCB_CCR_BFHFNMIGN_Msk |
| CCR | STKALIGN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_STKALIGN_Msk; cmsis_core:SCB_CCR_STKALIGN_Msk |
| SHCSR | MEMFAULTACT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTACT_Msk; cmsis_core:SCB_SHCSR_MEMFAULTACT_Msk |
| SHCSR | BUSFAULTACT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTACT_Msk; cmsis_core:SCB_SHCSR_BUSFAULTACT_Msk |
| SHCSR | USGFAULTACT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTACT_Msk; cmsis_core:SCB_SHCSR_USGFAULTACT_Msk |
| SHCSR | SVCALLACT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SVCALLACT_Msk; cmsis_core:SCB_SHCSR_SVCALLACT_Msk |
| SHCSR | MONITORACT | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MONITORACT_Msk; cmsis_core:SCB_SHCSR_MONITORACT_Msk |
| SHCSR | PENDSVACT | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_PENDSVACT_Msk; cmsis_core:SCB_SHCSR_PENDSVACT_Msk |
| SHCSR | SYSTICKACT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SYSTICKACT_Msk; cmsis_core:SCB_SHCSR_SYSTICKACT_Msk |
| SHCSR | USGFAULTPENDED | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTPENDED_Msk; cmsis_core:SCB_SHCSR_USGFAULTPENDED_Msk |
| SHCSR | MEMFAULTPENDED | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTPENDED_Msk; cmsis_core:SCB_SHCSR_MEMFAULTPENDED_Msk |
| SHCSR | BUSFAULTPENDED | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTPENDED_Msk; cmsis_core:SCB_SHCSR_BUSFAULTPENDED_Msk |
| SHCSR | SVCALLPENDED | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SVCALLPENDED_Msk; cmsis_core:SCB_SHCSR_SVCALLPENDED_Msk |
| SHCSR | MEMFAULTENA | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTENA_Msk; cmsis_core:SCB_SHCSR_MEMFAULTENA_Msk |
| SHCSR | BUSFAULTENA | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTENA_Msk; cmsis_core:SCB_SHCSR_BUSFAULTENA_Msk |
| SHCSR | USGFAULTENA | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTENA_Msk; cmsis_core:SCB_SHCSR_USGFAULTENA_Msk |
| CFSR | MEMFAULTSR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_MEMFAULTSR_Msk; cmsis_core:SCB_CFSR_MEMFAULTSR_Msk |
| CFSR | BUSFAULTSR | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_BUSFAULTSR_Msk; cmsis_core:SCB_CFSR_BUSFAULTSR_Msk |
| CFSR | USGFAULTSR | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_USGFAULTSR_Msk; cmsis_core:SCB_CFSR_USGFAULTSR_Msk |
| HFSR | VECTTBL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_VECTTBL_Msk; cmsis_core:SCB_HFSR_VECTTBL_Msk |
| HFSR | FORCED | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_FORCED_Msk; cmsis_core:SCB_HFSR_FORCED_Msk |
| HFSR | DEBUGEVT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_DEBUGEVT_Msk; cmsis_core:SCB_HFSR_DEBUGEVT_Msk |
| DFSR | HALTED | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_HALTED_Msk; cmsis_core:SCB_DFSR_HALTED_Msk |
| DFSR | BKPT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_BKPT_Msk; cmsis_core:SCB_DFSR_BKPT_Msk |
| DFSR | DWTTRAP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_DWTTRAP_Msk; cmsis_core:SCB_DFSR_DWTTRAP_Msk |
| DFSR | VCATCH | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_VCATCH_Msk; cmsis_core:SCB_DFSR_VCATCH_Msk |
| DFSR | EXTERNAL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_EXTERNAL_Msk; cmsis_core:SCB_DFSR_EXTERNAL_Msk |

## Operating semantics unavailable

**scb: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
