# SysTick — checked HSI16 periodic polling and system exception

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]], [[peripherals/scb]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SysTick | 0xE000E010 | Core system timer | CLKSOURCE=1 selects processor/AHB; example checks nominal HSI16 before starting | cmsis_core:SysTick_BASE; pm_core_246:page:246; pm_core_247:page:247 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths | Reviewed write-value mask |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CTRL | 0x000 | 32 | — | mixed | not asserted | Reading consumes COUNTFLAG. Reviewed writes only ENABLE/TICKINT/CLKSOURCE; initialize explicitly, reset conflict left unasserted. | cmsis_core:SysTick_Type.CTRL; cmsis_core:SysTick_Type.CTRL; pm_core_246:page:246; pm_core_247:page:247; pm_core_250:page:250; pm_core_251:page:251; arm_core_resolution:SysTick_reset_conflicts | 32 | 0x7 |
| LOAD | 0x004 | 32 | — | RW | not asserted | 24-bit periodic reload; use cycles-1 with cycles2..16777216. Reject zero-effective reload/fractional periods. Reset unasserted. | cmsis_core:SysTick_Type.LOAD; cmsis_core:SysTick_Type.LOAD; pm_core_246:page:246; pm_core_248:page:248; pm_core_250:page:250; arm_core_resolution:SysTick_reset_conflicts | 32 | 0xFFFFFF |
| VAL | 0x008 | 32 | — | mixed | not asserted | Read current value; any write clears current and COUNTFLAG. Reviewed writes only zero; pending SysTick is cleared separately in SCB. | cmsis_core:SysTick_Type.VAL; cmsis_core:SysTick_Type.VAL; pm_core_246:page:246; pm_core_249:page:249; pm_core_250:page:250; arm_core_resolution:SysTick_reset_conflicts | 32 | 0x0 |
| CALIB | 0x00C | 32 | — | RO | not asserted | Read only. Contradictory reset/calibration descriptions are not resolved to a value; this subset never derives timing from CALIB. | cmsis_core:SysTick_Type.CALIB; cmsis_core:SysTick_Type.CALIB; pm_core_246:page:246; pm_core_250:page:250; pm_core_251:page:251; arm_core_resolution:SysTick_reset_conflicts | 32 | 0x0 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CTRL | ENABLE | 0:0 | 0x1 | 1 enables the counter;0 disables. | cmsis_core:SysTick_CTRL_ENABLE_Msk; cmsis_core:SysTick_CTRL_ENABLE_Msk; pm_core_247:page:247 |
| CTRL | TICKINT | 1:1 | 0x2 | 1 requests the SysTick exception on a1-to0 event; enable only after handler preparation. | cmsis_core:SysTick_CTRL_TICKINT_Msk; cmsis_core:SysTick_CTRL_TICKINT_Msk; pm_core_247:page:247 |
| CTRL | CLKSOURCE | 2:2 | 0x4 | Reviewed value1 selects the processor/AHB clock. External calibration/reference selection is outside this subset. | cmsis_core:SysTick_CTRL_CLKSOURCE_Msk; cmsis_core:SysTick_CTRL_CLKSOURCE_Msk; pm_core_247:page:247 |
| CTRL | COUNTFLAG | 16:16 | 0x10000 | Status since previous CTRL read; a read consumes the flag. Multiple wraps coalesce; not a wrap count. | cmsis_core:SysTick_CTRL_COUNTFLAG_Msk; cmsis_core:SysTick_CTRL_COUNTFLAG_Msk; pm_core_247:page:247 |
| LOAD | RELOAD | 23:0 | 0xFFFFFF | Periodic reload=cycles-1; effective supported values1..0xFFFFFF. | cmsis_core:SysTick_LOAD_RELOAD_Msk; cmsis_core:SysTick_LOAD_RELOAD_Msk; pm_core_248:page:248 |
| VAL | CURRENT | 23:0 | 0xFFFFFF | Read current count; writes clear it and COUNTFLAG, not pending exception. | cmsis_core:SysTick_VAL_CURRENT_Msk; cmsis_core:SysTick_VAL_CURRENT_Msk; pm_core_249:page:249 |
| CALIB | TENMS | 23:0 | 0xFFFFFF | Calibration declaration only; no reset/calibration operating value asserted. | cmsis_core:SysTick_CALIB_TENMS_Msk; cmsis_core:SysTick_CALIB_TENMS_Msk; pm_core_250:page:250 |
| CALIB | SKEW | 30:30 | 0x40000000 | Calibration declaration only; no reset/calibration operating value asserted. | cmsis_core:SysTick_CALIB_SKEW_Msk; cmsis_core:SysTick_CALIB_SKEW_Msk; pm_core_250:page:250 |
| CALIB | NOREF | 31:31 | 0x80000000 | Calibration declaration only; no reset/calibration operating value asserted. | cmsis_core:SysTick_CALIB_NOREF_Msk; cmsis_core:SysTick_CALIB_NOREF_Msk; pm_core_250:page:250 |

## Reviewed operating semantics

Supported subset: **owned SysTick periodic core-clock operation at checked nominal HSI16**,
either bounded COUNTFLAG polling or a1kHz system-exception example. It requires no APB
gate and no external NVIC ISER line. It does not provide an RTOS tick, measured wall time,
low-power timing, an external calibration clock or automatic live clock reconfiguration.

1. Establish exclusive ownership before inspection: reading CTRL consumes COUNTFLAG,
   even when a busy check subsequently rejects the operation. Run in privileged Thread
   mode with PRIMASK=1. Do not take over another owner's active counter.
2. Retrieve [[peripherals/rcc]] and validate HSION=HSIRDY=1, SW=SWS=HSI,
   AHB/APB divisors1, and an updated SystemCoreClock=16000000. The reference bundle's
   168MHz PLL recipe is a different mode, not a claim about the running clock.
3. Calculate cycles=HCLK/tick_hz with exact integer division. Require cycles2..16777216;
   write LOAD=cycles-1 within24 bits. For the example,16000000/1000 gives LOAD15999.
   LOAD0 cannot produce the1-to0 event; fractional divisors are rejected, not rounded.
4. Keep ENABLE and TICKINT zero. Write LOAD, then VAL=0. Any VAL write clears the
   current count and COUNTFLAG; this is an action, not a writable stored count or RMW target.
5. For interrupts, first complete [[peripherals/scb]]'s vector/priority/pending mode and
   clear stale pending SysTick separately. VAL=0 is not a substitute for PENDSTCLR.
   The handler/software state must be ready before the source is enabled.
6. Write CTRL=CLKSOURCE|ENABLE for polling, or additionally TICKINT for IRQ operation.
   Keep all reserved/write-excluded bits zero; check the control bits on readback.
   The caller restores global interrupt masking only after successful preparation.

CTRL reads report and consume COUNTFLAG. Polling first discards an old flag, then waits
for a later event within a finite iteration budget. A flag records at least one wrap, not
how many wraps occurred; observing a new flag is not proof of a full interval since the call.
Debug halts stop counting. With processor-clock selection, stopping HCLK also stops SysTick.
On timeout/state failure, disable the owned source, report readback and require a new startup
context rather than retrying automatically. Never silently clear another owner's state.

The1kHz ISR increments an aligned uint32 software counter and returns; it performs no delays
or peripheral polling. Masked or delayed exceptions can coalesce, so the software count is
not a certified elapsed-time measurement. Use unsigned subtraction for counter wrap.

## Conflicting source descriptions

PM0214's summary, individual reset lines, hints and rotated register-map table disagree
about CTRL/LOAD/VAL and CALIB reset/calibration values. The rendered p251 table was reviewed,
not reconstructed from rotated extracted text alone. **All four reset values remain unasserted.**
The modes program LOAD, VAL and CTRL explicitly and never depend on CALIB/TENMS/NOREF/SKEW.
No unknown reset or calibration value is promoted to a supported workflow fact. The side effects
and supported clock/reload sequence are separately reviewed from pp247-250.

Sources: pm_core_24:page:24; pm_core_39:page:39; pm_core_246:page:246;
pm_core_247:page:247; pm_core_248:page:248; pm_core_249:page:249;
pm_core_250:page:250; pm_core_251:page:251; cmsis_core:SysTick_Type;
cmsis_core:SysTick_Config; header:SysTick_IRQn; arm_core_resolution:source_review.
Independent review and physical timing qualification remain pending.
See [[index]], [[peripherals/scb]], [[peripherals/rcc]] and [[sources]].

## Review

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| core_clock_interrupt | SysTick | CTRL, LOAD, VAL | CTRL: ENABLE, TICKINT, CLKSOURCE; LOAD: RELOAD; VAL: CURRENT | Complete the checked HSI16 and SCB vector/priority/pending contracts before enabling TICKINT.<br>The1kHz example uses LOAD15999 and SysTick_Handler slot15; never use a negative IRQn to index external NVIC banks.<br>Program LOAD, clear VAL, clear stale pending through SCB and enable CTRL last while global masking remains set.<br>Restore global masking only after success. A bounded ISR increments software state and returns without delays.<br>Masked/delayed exceptions can coalesce. Clock arithmetic and IRQ counts are not physical timing qualification. | pm_core_24:page:24; pm_core_39:page:39; pm_core_247:page:247; pm_core_248:page:248; pm_core_249:page:249; pm_core_250:page:250 | [[peripherals/rcc]] / hsi16_core_checked: RCC; [[peripherals/scb]] / systick_exception_setup: SCB |
| core_clock_polling | SysTick | CTRL, LOAD, VAL | CTRL: ENABLE, CLKSOURCE, COUNTFLAG; LOAD: RELOAD; VAL: CURRENT | Exclusive disabled counter, privileged Thread mode and PRIMASK=1; no RTOS ownership.<br>Use checked nominal HSI16 and exact integer division; cycles2..16777216, LOAD=cycles-1.<br>Write LOAD then VAL=0 then CTRL=CLKSOURCE&#124;ENABLE; keep TICKINT0 and reserved bits zero.<br>Drain stale COUNTFLAG, then wait for a later event within a finite iteration budget; events coalesce and do not certify elapsed time.<br>Debug halt/HCLK stop pauses counting. On failure disable the owned source and require a new startup context. | pm_core_24:page:24; pm_core_246:page:246; pm_core_247:page:247; pm_core_248:page:248; pm_core_249:page:249; pm_core_250:page:250 | [[peripherals/rcc]] / hsi16_core_checked: RCC |
| quiescent_owned | SysTick | CTRL | CTRL: ENABLE, TICKINT, COUNTFLAG | Caller establishes privileged startup ownership before inspection; CTRL reads consume COUNTFLAG even on a rejected busy check.<br>Require PRIMASK=1, Thread mode and ENABLE=TICKINT=0; do not overwrite another owner. | pm_core_22:page:22; pm_core_24:page:24; pm_core_247:page:247 |  |

Reviewer: Codex implementing-author source review through Praxis ingestion MCP; independent review pending. Basis: ST PM0214 Rev10 complete pages and rendered register diagrams, exact F407 CMSIS declarations, existing RM0090 HSI facts and pinned build profile. See arm_core_resolution; no physical core-timing qualification..

Reviewed write-value masks constrain values used by this operating subset: do not set bits outside the mask. A zero mask permits only a zero write to writable registers; RO registers remain non-writable. This is not a complete hardware writable-bit claim or permission for RMW: obey access, action and side-effect rules.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
