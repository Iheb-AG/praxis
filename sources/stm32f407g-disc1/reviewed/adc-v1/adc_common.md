Supported subset: independent ADC1 internal-reference operation only.
Shared registers also declare multi-ADC modes; declarations do not establish
reviewed operating support. Configure CCR only while every ADC is disabled and
no other owner exists. The workflow requires ADC2/3 clock gates initially zero.

1. Follow [[peripherals/rcc]], [[peripherals/flash]] and [[peripherals/pwr]]
   operating contracts to establish the assumed HSE8/168MHz profile. PCLK2 is
   84MHz. Require VDDA/VREF+ in the declared 2.7–3.6V range; supply is not measured.
2. Set CCR.ADCPRE=01 (/4), MULTI=0 (independent), DMA=0, VBATE=0 and TSVREFE=1.
   Keep reserved bits zero. ADC clock is 21MHz, below the datasheet 36MHz ceiling
   for the declared supply range. This is shared state; do not change it live.
3. Allow at least 10us reference startup before conversion. ADC1 also requires
   up to 3us power-up settling. The separate TIM2 polling contract supplies a
   nominal 1ms after ADON and reference enable. Bound all readiness polling.
4. Select a sampling interval at least 10us. ADC1 SMP17=111 provides 480cycles,
   about 22.86us at21MHz. Turn ADC1 off before removing TSVREFE after this owned
   operation. This example does not claim calibrated voltage, temperature,
   entropy, continuous, multi-ADC or DMA support.

Sources: rm_adc_392:page:392; rm_adc_429:page:429; rm_adc_430:page:430;
rm_adc_431:page:431; ds_adc_135:page:135; ds_adc_136:page:136;
ds_adc_reference:page:141. See [[peripherals/adc]], [[peripherals/tim]], [[sources]].
