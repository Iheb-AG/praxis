Supported subset: ADC1 VREFINT channel17, 12-bit right-aligned single regular
conversion started by software and read by polling. No external wire or GPIO
pin is involved. ADC2/3 lack these internal channels; their declaration tables
do not permit substituting them. The returned value is a raw code, not a
calibrated voltage or a source of verified entropy.

1. Retrieve [[peripherals/adc_common]] and its clock/voltage prerequisites.
   Reject existing ADC or TIM2 owners; this example requires fresh startup.
2. Enable/read back ADC1 and TIM2 clocks through RCC, leaving ADC2/3 disabled.
   Use 32-bit writes. Set CR2=0 while configuring CR1=0, SQR1.L=0 (one result),
   SQR3.SQ1=17, and SMPR1.SMP17=111 (480cycles). No scan, injected, watchdog,
   interrupt, external trigger, DMA or continuous conversion is enabled.
3. Select the shared independent-reference configuration; set CR2=ADON|EOCS.
   EOCS enables per-conversion EOC and overrun detection even without DMA.
   Use [[peripherals/tim]] polling_update_delay to settle for nominal1ms,
   exceeding reference startup10us and ADC startup3us under stated assumptions.
4. Clear stale SR with zero (rc_w0, not W1C), then issue SWSTART with ADON set.
   Hardware clears SWSTART at conversion start. Do not change sequence/sample
   settings during conversion. Poll with a finite iteration budget; stop on
   OVR or timeout. These budgets bound work, not wall-clock time.
5. Read DR once after EOC; the read clears EOC. DATA is a 16-bit container;
   only raw0–4095 is valid for this right-aligned12-bit contract. Power down
   ADC1, remove the owned TSVREFE enable, and stop TIM2 on completion/failure.
   Never write DR. Do not clear unrelated owners' flags.

Full header register/field tables are retained, including unreviewed rows.
Only the named single_conversion mode and its exact field requirements are
operating knowledge. External analog inputs, ADC2/3, scanning, injected
channels, DMA and ADC interrupts remain outside this supported mode.

Sources: rm_adc_392/393:page:392/393; rm_adc_417 through rm_adc_427 at
matching page locators; ds_adc_reference:page:141; ds_adc_135:page:135;
ds_adc_136:page:136. See [[index]], [[features]] and [[sources]].
