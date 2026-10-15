# SCB — F407 fixed vectors and SysTick exception preparation

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SCB | 0xE000ED00 | Core system registers | Core interface; no peripheral bus gate for this subset | cmsis_core:SCB_BASE; pm_core_225:page:225 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths | Reviewed write-value mask | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CPUID | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CPUID | not asserted | not asserted | 1 | 4 |
| ICSR | 0x004 | 32 | — | mixed | not asserted | Mixed status and write-one actions. Reviewed writes only PENDSTCLR; its read value is unknown. No RMW, no SET+CLR, no NMI/PendSV action writes. | cmsis_core:SCB_Type.ICSR; cmsis_core:SCB_Type.ICSR; pm_core_225:page:225; pm_core_226:page:226; timer_irq_evidence:pm0214/page:225; timer_irq_evidence:pm0214/page:226 | 32 | 0x2000000 | 1 | 4 |
| VTOR | 0x008 | 32 | — | RW | not asserted | F407 reviewed table-base writes keep bits31:30 and8:0 zero. Fixed table0x08000000,512-byte alignment, DSB/ISB and readback; no handoff. | cmsis_core:SCB_Type.VTOR; cmsis_core:SCB_Type.VTOR; pm_core_227:page:227 | 32 | 0x3FFFFE00 | 1 | 4 |
| AIRCR | 0x00C | 32 | — | mixed | 0xFA050000 | Reviewed subset reads PRIGROUP only. Writes need VECTKEY and may request reset; no AIRCR write is supported by this mode. | cmsis_core:SCB_Type.AIRCR; cmsis_core:SCB_Type.AIRCR; timer_irq_evidence:pm0214/page:228; timer_irq_evidence:pm0214/page:229 | 32 | not asserted | 1 | 4 |
| SCR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.SCR | not asserted | not asserted | 1 | 4 |
| CCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CCR | not asserted | not asserted | 1 | 4 |
| SHP | 0x018 | 8 | — | mixed | not asserted | Byte-accessible priority array with reserved slots. This subset writes only SHP[11], high four priority bits; preserve PendSV and other bytes. | cmsis_core:SCB_Type.SHP; cmsis_core:SCB_Type.SHP; pm_core_233:page:233; pm_core_234:page:234 | 8 | 0xF0 | 12 | 1 |
| SHCSR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.SHCSR | not asserted | not asserted | 1 | 4 |
| CFSR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CFSR | not asserted | not asserted | 1 | 4 |
| HFSR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.HFSR | not asserted | not asserted | 1 | 4 |
| DFSR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.DFSR | not asserted | not asserted | 1 | 4 |
| MMFAR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.MMFAR | not asserted | not asserted | 1 | 4 |
| BFAR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.BFAR | not asserted | not asserted | 1 | 4 |
| AFSR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.AFSR | not asserted | not asserted | 1 | 4 |
| PFR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.PFR | not asserted | not asserted | 2 | 4 |
| DFR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.DFR | not asserted | not asserted | 1 | 4 |
| ADR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.ADR | not asserted | not asserted | 1 | 4 |
| MMFR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.MMFR | not asserted | not asserted | 4 | 4 |
| ISAR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.ISAR | not asserted | not asserted | 5 | 4 |
| CPACR | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:SCB_Type.CPACR | not asserted | not asserted | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CPUID | REVISION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_REVISION_Msk |
| CPUID | PARTNO | 15:4 | 0xFFF0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_PARTNO_Msk |
| CPUID | ARCHITECTURE | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_ARCHITECTURE_Msk |
| CPUID | VARIANT | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_VARIANT_Msk |
| CPUID | IMPLEMENTER | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CPUID_IMPLEMENTER_Msk |
| ICSR | VECTACTIVE | 8:0 | 0x1FF | Read current exception number; zero means Thread mode. | cmsis_core:SCB_ICSR_VECTACTIVE_Msk; cmsis_core:SCB_ICSR_VECTACTIVE_Msk; pm_core_226:page:226 |
| ICSR | RETTOBASE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_RETTOBASE_Msk; cmsis_core:SCB_ICSR_RETTOBASE_Msk |
| ICSR | VECTPENDING | 20:12 | 0x1FF000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_VECTPENDING_Msk; cmsis_core:SCB_ICSR_VECTPENDING_Msk |
| ICSR | ISRPENDING | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_ISRPENDING_Msk; cmsis_core:SCB_ICSR_ISRPENDING_Msk |
| ICSR | ISRPREEMPT | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_ISRPREEMPT_Msk; cmsis_core:SCB_ICSR_ISRPREEMPT_Msk |
| ICSR | PENDSTCLR | 25:25 | 0x2000000 | Write one clears pending SysTick. Read is unknown; only exact action writes are supported. | cmsis_core:SCB_ICSR_PENDSTCLR_Msk; cmsis_core:SCB_ICSR_PENDSTCLR_Msk; pm_core_226:page:226 |
| ICSR | PENDSTSET | 26:26 | 0x4000000 | Read0 requires this system exception not pending before global unmask. No ICSR write is supported by the TIM5 fresh-startup contract. | cmsis_core:SCB_ICSR_PENDSTSET_Msk; cmsis_core:SCB_ICSR_PENDSTSET_Msk; pm_core_226:page:226; timer_irq_evidence:pm0214/page:226 |
| ICSR | PENDSVCLR | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_ICSR_PENDSVCLR_Msk; cmsis_core:SCB_ICSR_PENDSVCLR_Msk |
| ICSR | PENDSVSET | 28:28 | 0x10000000 | Read0 requires this system exception not pending before global unmask. No ICSR write is supported by the TIM5 fresh-startup contract. | cmsis_core:SCB_ICSR_PENDSVSET_Msk; cmsis_core:SCB_ICSR_PENDSVSET_Msk; timer_irq_evidence:pm0214/page:226 |
| ICSR | NMIPENDSET | 31:31 | 0x80000000 | Read0 requires this system exception not pending before global unmask. No ICSR write is supported by the TIM5 fresh-startup contract. | cmsis_core:SCB_ICSR_NMIPENDSET_Msk; cmsis_core:SCB_ICSR_NMIPENDSET_Msk; timer_irq_evidence:pm0214/page:225 |
| VTOR | TBLOFF | 31:7 | 0xFFFFFF80 | Shared CMSIS declaration envelope only. F407 supported writes also require0x3FFFFE00 and512-byte alignment; only the pinned Flash table is supported. | cmsis_core:SCB_VTOR_TBLOFF_Msk; cmsis_core:SCB_VTOR_TBLOFF_Msk; pm_core_227:page:227; arm_core_resolution:VTOR_device_rule |
| AIRCR | VECTRESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTRESET_Msk |
| AIRCR | VECTCLRACTIVE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTCLRACTIVE_Msk |
| AIRCR | SYSRESETREQ | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_SYSRESETREQ_Msk |
| AIRCR | PRIGROUP | 10:8 | 0x700 | Read field must equal0 for this fresh-startup IRQ example; all four implemented priority bits are preemption priority. Never write AIRCR in this scope. | cmsis_core:SCB_AIRCR_PRIGROUP_Msk; cmsis_core:SCB_AIRCR_PRIGROUP_Msk; timer_irq_evidence:pm0214/page:228; timer_irq_evidence:pm0214/page:229 |
| AIRCR | ENDIANESS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_ENDIANESS_Msk |
| AIRCR | VECTKEY | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_AIRCR_VECTKEY_Msk |
| SCR | SLEEPONEXIT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SLEEPONEXIT_Msk |
| SCR | SLEEPDEEP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SLEEPDEEP_Msk |
| SCR | SEVONPEND | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SCR_SEVONPEND_Msk |
| CCR | NONBASETHRDENA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_NONBASETHRDENA_Msk |
| CCR | USERSETMPEND | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_USERSETMPEND_Msk |
| CCR | UNALIGN_TRP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_UNALIGN_TRP_Msk |
| CCR | DIV_0_TRP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_DIV_0_TRP_Msk |
| CCR | BFHFNMIGN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_BFHFNMIGN_Msk |
| CCR | STKALIGN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CCR_STKALIGN_Msk |
| SHCSR | MEMFAULTACT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTACT_Msk |
| SHCSR | BUSFAULTACT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTACT_Msk |
| SHCSR | USGFAULTACT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTACT_Msk |
| SHCSR | SVCALLACT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SVCALLACT_Msk |
| SHCSR | MONITORACT | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MONITORACT_Msk |
| SHCSR | PENDSVACT | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_PENDSVACT_Msk |
| SHCSR | SYSTICKACT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SYSTICKACT_Msk |
| SHCSR | USGFAULTPENDED | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTPENDED_Msk |
| SHCSR | MEMFAULTPENDED | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTPENDED_Msk |
| SHCSR | BUSFAULTPENDED | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTPENDED_Msk |
| SHCSR | SVCALLPENDED | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_SVCALLPENDED_Msk |
| SHCSR | MEMFAULTENA | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_MEMFAULTENA_Msk |
| SHCSR | BUSFAULTENA | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_BUSFAULTENA_Msk |
| SHCSR | USGFAULTENA | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_SHCSR_USGFAULTENA_Msk |
| CFSR | MEMFAULTSR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_MEMFAULTSR_Msk |
| CFSR | BUSFAULTSR | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_BUSFAULTSR_Msk |
| CFSR | USGFAULTSR | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_CFSR_USGFAULTSR_Msk |
| HFSR | VECTTBL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_VECTTBL_Msk |
| HFSR | FORCED | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_FORCED_Msk |
| HFSR | DEBUGEVT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_HFSR_DEBUGEVT_Msk |
| DFSR | HALTED | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_HALTED_Msk |
| DFSR | BKPT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_BKPT_Msk |
| DFSR | DWTTRAP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_DWTTRAP_Msk |
| DFSR | VCATCH | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_VCATCH_Msk |
| DFSR | EXTERNAL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:SCB_DFSR_EXTERNAL_Msk |

## Reviewed operating semantics

Supported subset: **owned privileged startup, fixed F407 Flash vector table, SysTick priority
and pending-state preparation**. No image handoff, MSP change, RAM table relocation, fault
recovery, RTOS ownership transfer or arbitrary VTOR address is supported by these modes.

## Fixed vector table

The approved build assets provide 98 entries at Flash 0x08000000, initial MSP 0x20020000
in the 128 KiB contiguous main SRAM bank, and a SysTick entry in slot15/offset0x3C.
These are the pinned build profile's limits, not an assertion that every Cortex-M4 has
that memory map. Check the selected build profile and ELF separately.

Run only in privileged Thread mode, with PRIMASK=1, exclusive startup ownership and
SysTick ENABLE=TICKINT=0. Verify the pinned table's initial SP and its odd Thumb
SysTick handler address before selecting it. Write VTOR=0x08000000, execute DSB then
ISB, and check readback. Retain masking on failure; do not attempt an automatic handoff.

PM0214 p227 restricts the F407 table base to bits29:9, with bits31:30 and8:0 zero:
the reviewed write-value mask is **0x3FFFFE00** and minimum alignment is512 bytes.
The common CMSIS `SCB_VTOR_TBLOFF_Msk=0xFFFFFF80` is a declaration envelope; it does
**not** authorize the extra bits on this device. The narrower device rule takes precedence
for writes. The general discussion at p40 is also broader than this device register rule.

## SysTick exception setup

SysTick has exception number15/CMSIS IRQn=-1; it has no external NVIC ISER bit.
The priority byte is SCB.SHP[11], at SCB+0x23, the high byte of SHPR3. Access it as
one byte; never overwrite PendSV's adjacent byte. Four priority bits are implemented
(`header:__NVIC_PRIO_BITS`); accept priorities0..15 and encode them in bits7:4.
The example chooses15, a software policy. Priority grouping is retained, not rewritten.

Initialize the handler and software counter, select the approved vector table, set the
priority, and clear stale pending SysTick with the exact word write
`ICSR=PENDSTCLR` (bit25). Verify pending status through PENDSTSET (bit26), not the
write-only clear bit, whose read value is unknown. Never RMW ICSR: readback can contain
NMI/PendSV action bits and SET+CLR writes are unpredictable. Preserve unrelated pending
exceptions. Only after this preparation may [[peripherals/systick]] enable TICKINT.
Global configurable interrupts remain masked until the caller deliberately enables them.
PRIMASK does not mask NMI or HardFault and does not prove handler correctness.

ICSR's shared header VECTPENDING envelope is wider than PM0214's device field. This mode
does not use VECTPENDING or debug-only ISRPREEMPT; their complete declarations remain
unreviewed. The SHP array has twelve bytes; only the documented priority slots are implemented.
This mode writes only byte11 and preserves all others. Reset values are not relied upon.

Sources: pm_core_22:page:22; pm_core_24:page:24; pm_core_39:page:39;
pm_core_40:page:40; pm_core_41:page:41; pm_core_184:page:184;
pm_core_185:page:185; pm_core_225:page:225; pm_core_226:page:226;
pm_core_227:page:227; pm_core_233:page:233; pm_core_234:page:234;
cmsis_core:SCB_Type; cmsis_core:__NVIC_SetPriority;
header:SysTick_IRQn; header:__NVIC_PRIO_BITS; header:FLASH_BASE;
arm_asset_contract:source_profile. Independent engineering review remains pending.
See [[index]], [[peripherals/systick]], [[peripherals/rcc]] and [[sources]].

## TIM5 capture interrupt startup context

Use tim5_fixed_irq_context: privileged Thread/MSP, PRIMASK1 during setup, BASEPRI=FAULTMASK0,
checked VTOR0x08000000 and exact linked Thumb slot66. Read AIRCR.PRIGROUP and require0;
never write AIRCR or relocate the vector in this example. PM0214 pages22–26,40,227–229;
header TIM5_IRQn50 and four priority bits. See [[peripherals/nvic]] and [[peripherals/tim]].

## Review

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| flash_vector_table | SCB | VTOR | VTOR: TBLOFF | Privileged owned startup, Thread mode and PRIMASK=1; no RTOS/image handoff.<br>Only the pinned98-entry table at0x08000000; verify initial SP0x20020000 and a matching odd Flash SysTick handler.<br>Use device write-value mask0x3FFFFE00 and512-byte alignment; the wider CMSIS field is not write permission.<br>Write VTOR, execute DSB then ISB and check readback; retain masking on failure. | pm_core_39:page:39; pm_core_40:page:40; pm_core_184:page:184; pm_core_185:page:185; pm_core_227:page:227; arm_asset_contract:memory_and_vectors | [[peripherals/systick]] / quiescent_owned: SysTick |
| systick_exception_setup | SCB | ICSR, SHP | ICSR: PENDSTCLR, PENDSTSET, VECTACTIVE | SysTick exception15/IRQn-1 has no external NVIC ISER bit; keep PRIMASK=1 and source disabled.<br>Initialize handler/software state before source enable. Only write SHP[11] as a byte with priority0..15 encoded in high four bits.<br>Preserve PendSV and priority grouping. Clear pending with exact ICSR=PENDSTCLR; never RMW ICSR.<br>Check pending through PENDSTSET, not the write-only clear bit. Restore global interrupt state last. | pm_core_22:page:22; pm_core_24:page:24; pm_core_39:page:39; pm_core_41:page:41; pm_core_225:page:225; pm_core_226:page:226; pm_core_233:page:233; pm_core_234:page:234 | [[peripherals/scb]] / flash_vector_table: SCB |
| tim5_fixed_irq_context | SCB | VTOR, AIRCR, ICSR | AIRCR: PRIGROUP; ICSR: PENDSTSET, PENDSVSET, NMIPENDSET; VTOR: TBLOFF | Fresh privileged Thread/MSP startup: PRIMASK1, BASEPRI0, FAULTMASK0, CONTROL.nPRIV=CONTROL.SPSEL=0.<br>VTOR must equal pinned Flash0x08000000, aligned512 bytes; initial SP must equal pinned main-SRAM top0x20020000 and slot16+TIM5_IRQn66 must equal the linked Thumb TIM5_IRQHandler.<br>Require exclusively owned SysTick disabled (ENABLE/TICKINT0); CTRL inspection consumes COUNTFLAG. Require no pending SysTick, PendSV or NMI from read-only ICSR. No system-exception configuration writes.<br>Read AIRCR.PRIGROUP and require0; logical priority2 is software policy using four high implemented priority bits. No AIRCR/reset/vector-table write or live priority-group changes. | timer_irq_evidence:pm0214/page:22; timer_irq_evidence:pm0214/page:24; timer_irq_evidence:pm0214/page:25; timer_irq_evidence:pm0214/page:26; timer_irq_evidence:pm0214/page:40; timer_irq_evidence:pm0214/page:225; timer_irq_evidence:pm0214/page:226; timer_irq_evidence:pm0214/page:227; timer_irq_evidence:pm0214/page:228; timer_irq_evidence:pm0214/page:229; timer_irq_evidence:pm0214/page:247; arm_asset_contract:memory_and_vectors | [[peripherals/systick]] / quiescent_owned: SysTick |

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: Complete RM0090 Rev22 and PM0214 Rev10 source parts plus exact pinned IRQ/priority declarations. Implementing-author review only; independent signoff and new physical IRQ qualification pending..

Reviewed write-value masks constrain values used by this operating subset: do not set bits outside the mask. A zero mask permits only a zero write to writable registers; RO registers remain non-writable. This is not a complete hardware writable-bit claim or permission for RMW: obey access, action and side-effect rules.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
