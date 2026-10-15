# SCB — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SCB | 0xE000ED00 | Not asserted | Not asserted | core_cm7_h:SCB_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPUID | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CPUID | 1 | 4 |
| ICSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ICSR | 1 | 4 |
| VTOR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.VTOR | 1 | 4 |
| AIRCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.AIRCR | 1 | 4 |
| SCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.SCR | 1 | 4 |
| CCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CCR | 1 | 4 |
| SHPR | 0x018 | 8 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.SHPR | 12 | 1 |
| SHCSR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.SHCSR | 1 | 4 |
| CFSR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CFSR | 1 | 4 |
| HFSR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.HFSR | 1 | 4 |
| DFSR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DFSR | 1 | 4 |
| MMFAR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.MMFAR | 1 | 4 |
| BFAR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.BFAR | 1 | 4 |
| AFSR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.AFSR | 1 | 4 |
| ID_PFR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ID_PFR | 2 | 4 |
| ID_DFR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ID_DFR | 1 | 4 |
| ID_AFR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ID_AFR | 1 | 4 |
| ID_MFR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ID_MFR | 4 | 4 |
| ID_ISAR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ID_ISAR | 5 | 4 |
| CLIDR | 0x078 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CLIDR | 1 | 4 |
| CTR | 0x07C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CTR | 1 | 4 |
| CCSIDR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CCSIDR | 1 | 4 |
| CSSELR | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CSSELR | 1 | 4 |
| CPACR | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CPACR | 1 | 4 |
| STIR | 0x200 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.STIR | 1 | 4 |
| MVFR0 | 0x240 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.MVFR0 | 1 | 4 |
| MVFR1 | 0x244 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.MVFR1 | 1 | 4 |
| MVFR2 | 0x248 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.MVFR2 | 1 | 4 |
| ICIALLU | 0x250 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ICIALLU | 1 | 4 |
| ICIMVAU | 0x258 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ICIMVAU | 1 | 4 |
| DCIMVAC | 0x25C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCIMVAC | 1 | 4 |
| DCISW | 0x260 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCISW | 1 | 4 |
| DCCMVAU | 0x264 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCCMVAU | 1 | 4 |
| DCCMVAC | 0x268 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCCMVAC | 1 | 4 |
| DCCSW | 0x26C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCCSW | 1 | 4 |
| DCCIMVAC | 0x270 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCCIMVAC | 1 | 4 |
| DCCISW | 0x274 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DCCISW | 1 | 4 |
| BPIALL | 0x278 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.BPIALL | 1 | 4 |
| ITCMCR | 0x290 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ITCMCR | 1 | 4 |
| DTCMCR | 0x294 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.DTCMCR | 1 | 4 |
| AHBPCR | 0x298 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.AHBPCR | 1 | 4 |
| CACR | 0x29C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.CACR | 1 | 4 |
| AHBSCR | 0x2A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.AHBSCR | 1 | 4 |
| ABFSR | 0x2A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm7_h:SCB_Type.ABFSR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CPUID | REVISION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CPUID_REVISION_Msk |
| CPUID | PARTNO | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CPUID_PARTNO_Msk |
| CPUID | ARCHITECTURE | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CPUID_ARCHITECTURE_Msk |
| CPUID | VARIANT | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CPUID_VARIANT_Msk |
| CPUID | IMPLEMENTER | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CPUID_IMPLEMENTER_Msk |
| ICSR | VECTACTIVE | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_VECTACTIVE_Msk |
| ICSR | RETTOBASE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_RETTOBASE_Msk |
| ICSR | VECTPENDING | 20:12 | 0x1FF000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_VECTPENDING_Msk |
| ICSR | ISRPENDING | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_ISRPENDING_Msk |
| ICSR | ISRPREEMPT | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_ISRPREEMPT_Msk |
| ICSR | PENDSTCLR | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_PENDSTCLR_Msk |
| ICSR | PENDSTSET | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_PENDSTSET_Msk |
| ICSR | PENDSVCLR | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_PENDSVCLR_Msk |
| ICSR | PENDSVSET | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_PENDSVSET_Msk |
| ICSR | NMIPENDSET | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ICSR_NMIPENDSET_Msk |
| VTOR | TBLOFF | 31:7 | 0xFFFFFF80 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_VTOR_TBLOFF_Msk |
| AIRCR | VECTRESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_VECTRESET_Msk |
| AIRCR | VECTCLRACTIVE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_VECTCLRACTIVE_Msk |
| AIRCR | SYSRESETREQ | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_SYSRESETREQ_Msk |
| AIRCR | PRIGROUP | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_PRIGROUP_Msk |
| AIRCR | ENDIANESS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_ENDIANESS_Msk |
| AIRCR | VECTKEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AIRCR_VECTKEY_Msk |
| SCR | SLEEPONEXIT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SCR_SLEEPONEXIT_Msk |
| SCR | SLEEPDEEP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SCR_SLEEPDEEP_Msk |
| SCR | SEVONPEND | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SCR_SEVONPEND_Msk |
| CCR | NONBASETHRDENA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_NONBASETHRDENA_Msk |
| CCR | USERSETMPEND | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_USERSETMPEND_Msk |
| CCR | UNALIGN_TRP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_UNALIGN_TRP_Msk |
| CCR | DIV_0_TRP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_DIV_0_TRP_Msk |
| CCR | BFHFNMIGN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_BFHFNMIGN_Msk |
| CCR | STKALIGN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_STKALIGN_Msk |
| CCR | DC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_DC_Msk |
| CCR | IC | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_IC_Msk |
| CCR | BP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCR_BP_Msk |
| SHCSR | MEMFAULTACT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_MEMFAULTACT_Msk |
| SHCSR | BUSFAULTACT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_BUSFAULTACT_Msk |
| SHCSR | USGFAULTACT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_USGFAULTACT_Msk |
| SHCSR | SVCALLACT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_SVCALLACT_Msk |
| SHCSR | MONITORACT | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_MONITORACT_Msk |
| SHCSR | PENDSVACT | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_PENDSVACT_Msk |
| SHCSR | SYSTICKACT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_SYSTICKACT_Msk |
| SHCSR | USGFAULTPENDED | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_USGFAULTPENDED_Msk |
| SHCSR | MEMFAULTPENDED | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_MEMFAULTPENDED_Msk |
| SHCSR | BUSFAULTPENDED | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_BUSFAULTPENDED_Msk |
| SHCSR | SVCALLPENDED | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_SVCALLPENDED_Msk |
| SHCSR | MEMFAULTENA | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_MEMFAULTENA_Msk |
| SHCSR | BUSFAULTENA | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_BUSFAULTENA_Msk |
| SHCSR | USGFAULTENA | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_SHCSR_USGFAULTENA_Msk |
| CFSR | MEMFAULTSR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CFSR_MEMFAULTSR_Msk |
| CFSR | BUSFAULTSR | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CFSR_BUSFAULTSR_Msk |
| CFSR | USGFAULTSR | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CFSR_USGFAULTSR_Msk |
| HFSR | VECTTBL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_HFSR_VECTTBL_Msk |
| HFSR | FORCED | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_HFSR_FORCED_Msk |
| HFSR | DEBUGEVT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_HFSR_DEBUGEVT_Msk |
| DFSR | HALTED | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DFSR_HALTED_Msk |
| DFSR | BKPT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DFSR_BKPT_Msk |
| DFSR | DWTTRAP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DFSR_DWTTRAP_Msk |
| DFSR | VCATCH | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DFSR_VCATCH_Msk |
| DFSR | EXTERNAL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DFSR_EXTERNAL_Msk |
| CLIDR | LOC | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CLIDR_LOC_Msk |
| CLIDR | LOUU | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CLIDR_LOUU_Msk |
| CTR | IMINLINE | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CTR_IMINLINE_Msk |
| CTR | DMINLINE | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CTR_DMINLINE_Msk |
| CTR | ERG | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CTR_ERG_Msk |
| CTR | CWG | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CTR_CWG_Msk |
| CTR | FORMAT | 31:29 | 0xE0000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CTR_FORMAT_Msk |
| CCSIDR | LINESIZE | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_LINESIZE_Msk |
| CCSIDR | ASSOCIATIVITY | 12:3 | 0x1FF8 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_ASSOCIATIVITY_Msk |
| CCSIDR | NUMSETS | 27:13 | 0xFFFE000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_NUMSETS_Msk |
| CCSIDR | WA | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_WA_Msk |
| CCSIDR | RA | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_RA_Msk |
| CCSIDR | WB | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_WB_Msk |
| CCSIDR | WT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CCSIDR_WT_Msk |
| CSSELR | IND | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CSSELR_IND_Msk |
| CSSELR | LEVEL | 3:1 | 0xE | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CSSELR_LEVEL_Msk |
| STIR | INTID | 8:0 | 0x1FF | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_STIR_INTID_Msk |
| DCISW | SET | 13:5 | 0x3FE0 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCISW_SET_Msk |
| DCISW | WAY | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCISW_WAY_Msk |
| DCCSW | SET | 13:5 | 0x3FE0 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCCSW_SET_Msk |
| DCCSW | WAY | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCCSW_WAY_Msk |
| DCCISW | SET | 13:5 | 0x3FE0 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCCISW_SET_Msk |
| DCCISW | WAY | 31:30 | 0xC0000000 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DCCISW_WAY_Msk |
| ITCMCR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ITCMCR_EN_Msk |
| ITCMCR | RMW | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ITCMCR_RMW_Msk |
| ITCMCR | RETEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ITCMCR_RETEN_Msk |
| ITCMCR | SZ | 6:3 | 0x78 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ITCMCR_SZ_Msk |
| DTCMCR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DTCMCR_EN_Msk |
| DTCMCR | RMW | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DTCMCR_RMW_Msk |
| DTCMCR | RETEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DTCMCR_RETEN_Msk |
| DTCMCR | SZ | 6:3 | 0x78 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_DTCMCR_SZ_Msk |
| AHBPCR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AHBPCR_EN_Msk |
| AHBPCR | SZ | 3:1 | 0xE | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AHBPCR_SZ_Msk |
| CACR | SIWT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CACR_SIWT_Msk |
| CACR | ECCEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CACR_ECCEN_Msk |
| CACR | FORCEWT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_CACR_FORCEWT_Msk |
| AHBSCR | CTL | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AHBSCR_CTL_Msk |
| AHBSCR | TPRI | 10:2 | 0x7FC | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AHBSCR_TPRI_Msk |
| AHBSCR | INITCOUNT | 15:11 | 0xF800 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_AHBSCR_INITCOUNT_Msk |
| ABFSR | ITCM | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_ITCM_Msk |
| ABFSR | DTCM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_DTCM_Msk |
| ABFSR | AHBP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_AHBP_Msk |
| ABFSR | AXIM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_AXIM_Msk |
| ABFSR | EPPB | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_EPPB_Msk |
| ABFSR | AXIMTYPE | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | core_cm7_h:SCB_ABFSR_AXIMTYPE_Msk |

## Operating semantics unavailable

**scb: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
