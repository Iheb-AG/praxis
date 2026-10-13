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

## Polling pending-state guard

Before any timer write, require SCB.ICSR.PENDSTSET=0. Polling does not install a SysTick handler or clear an old pending exception. Refuse already pending SysTick; neither TICKINT=0 nor a VAL write proves the exception is no longer pending. Keep the bounded polling operation globally masked, stop the source before changing its ownership, and do not infer safe global unmasking from COUNTFLAG or source-disable state alone. Source: pm_core_226:page:226.
