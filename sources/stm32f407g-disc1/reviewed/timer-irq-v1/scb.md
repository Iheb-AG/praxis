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
