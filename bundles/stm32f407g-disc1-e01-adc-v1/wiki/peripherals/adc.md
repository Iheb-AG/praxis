# ADC — ADC1 internal-reference single-conversion subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/adc_common]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC1 | 0x40012000 | APB2 | PCLK2/4 = 21 MHz under the declared PLL operating point | header:ADC1_BASE; rm_adc_392:page:392 |
| ADC2 | 0x40012100 | Not asserted | Not asserted outside reviewed workflow | header:ADC2_BASE |
| ADC3 | 0x40012200 | Not asserted | Not asserted outside reviewed workflow | header:ADC3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SR | 0x000 | 32 | — | mixed | 0x0 | Status flags clear by writing zero. Reading DR clears EOC. OVR detection requires EOCS=1 or DMA=1; this mode uses EOCS=1. Clear owned stale flags with SR=0, never W1C. | header:ADC_TypeDef.SR; header:ADC_TypeDef.SR; rm_adc_417:page:417 | 32 |
| CR1 | 0x004 | 32 | — | RW | 0x0 | Configure only while ADC1 disabled. This mode writes zero: 12-bit resolution, no scan/injected/watchdog/interrupt operation. Reserved bits remain zero. | header:ADC_TypeDef.CR1; header:ADC_TypeDef.CR1; rm_adc_418:page:418; rm_adc_419:page:419 | 32 |
| CR2 | 0x008 | 32 | — | RW | 0x0 | ADON powers the ADC. SWSTART is a self-clearing command and requires ADON=1. Disable ADC on completion or failure; no trigger/DMA/continuous requests. | header:ADC_TypeDef.CR2; header:ADC_TypeDef.CR2; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 | 32 |
| SMPR1 | 0x00C | 32 | — | RW | 0x0 | Sampling selection cannot change during conversion. SMP17=111 chooses 480 ADC cycles; at 21 MHz this is about 22.86 us, above the declared 10 us VREFINT minimum. | header:ADC_TypeDef.SMPR1; header:ADC_TypeDef.SMPR1; rm_adc_422:page:422 | 32 |
| SMPR2 | 0x010 | 32 | — | RW | 0x0 | Channel 0–9 sampling configuration; leave zero in this internal-channel mode. Do not change during conversion. | header:ADC_TypeDef.SMPR2; header:ADC_TypeDef.SMPR2; rm_adc_422:page:422; rm_adc_423:page:423 | 32 |
| JOFR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR1 | not asserted |
| JOFR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR2 | not asserted |
| JOFR3 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR3 | not asserted |
| JOFR4 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JOFR4 | not asserted |
| HTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.HTR | not asserted |
| LTR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.LTR | not asserted |
| SQR1 | 0x02C | 32 | — | RW | 0x0 | Do not modify sequence while conversion is active; changing it can restart conversion. | header:ADC_TypeDef.SQR1; header:ADC_TypeDef.SQR1; rm_adc_424:page:424 | 32 |
| SQR2 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.SQR2 | not asserted |
| SQR3 | 0x034 | 32 | — | RW | 0x0 | Do not modify sequence while conversion is active. | header:ADC_TypeDef.SQR3; header:ADC_TypeDef.SQR3; rm_adc_425:page:425; rm_adc_426:page:426 | 32 |
| JSQR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JSQR | not asserted |
| JDR1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR1 | not asserted |
| JDR2 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR2 | not asserted |
| JDR3 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR3 | not asserted |
| JDR4 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_TypeDef.JDR4 | not asserted |
| DR | 0x04C | 32 | — | RO | 0x0 | Read once after EOC; reading clears EOC. RO: never write. DATA is a 16-bit container; the reviewed right-aligned 12-bit mode returns 0–4095. | header:ADC_TypeDef.DR; header:ADC_TypeDef.DR; rm_adc_417:page:417; rm_adc_427:page:427 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | AWD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_AWD_Msk |
| SR | EOC | 1:1 | 0x2 | End of conversion; read DR clears this flag. | header:ADC_SR_EOC_Msk; header:ADC_SR_EOC_Msk; rm_adc_417:page:417 |
| SR | JEOC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JEOC_Msk |
| SR | JSTRT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_SR_JSTRT_Msk |
| SR | STRT | 4:4 | 0x10 | Regular conversion start flag; clear by writing zero. | header:ADC_SR_STRT_Msk; header:ADC_SR_STRT_Msk; rm_adc_417:page:417 |
| SR | OVR | 5:5 | 0x20 | Lost conversion data; abort this operation if set. | header:ADC_SR_OVR_Msk; header:ADC_SR_OVR_Msk; rm_adc_417:page:417 |
| CR1 | AWDCH | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDCH_Msk |
| CR1 | EOCIE | 5:5 | 0x20 | 0 disables EOC interrupt. | header:ADC_CR1_EOCIE_Msk; header:ADC_CR1_EOCIE_Msk; rm_adc_418:page:418; rm_adc_419:page:419 |
| CR1 | AWDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDIE_Msk |
| CR1 | JEOCIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JEOCIE_Msk |
| CR1 | SCAN | 8:8 | 0x100 | 0 disables scan. | header:ADC_CR1_SCAN_Msk; header:ADC_CR1_SCAN_Msk; rm_adc_418:page:418; rm_adc_419:page:419 |
| CR1 | AWDSGL | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDSGL_Msk |
| CR1 | JAUTO | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAUTO_Msk |
| CR1 | DISCEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCEN_Msk |
| CR1 | JDISCEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JDISCEN_Msk |
| CR1 | DISCNUM | 15:13 | 0xE000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_DISCNUM_Msk |
| CR1 | JAWDEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_JAWDEN_Msk |
| CR1 | AWDEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR1_AWDEN_Msk |
| CR1 | RES | 25:24 | 0x3000000 | 00 selects 12-bit conversion. | header:ADC_CR1_RES_Msk; header:ADC_CR1_RES_Msk; rm_adc_418:page:418; rm_adc_419:page:419 |
| CR1 | OVRIE | 26:26 | 0x4000000 | 0 disables overrun interrupt. | header:ADC_CR1_OVRIE_Msk; header:ADC_CR1_OVRIE_Msk; rm_adc_418:page:418; rm_adc_419:page:419 |
| CR2 | ADON | 0:0 | 0x1 | 1 enables ADC; 0 powers down. | header:ADC_CR2_ADON_Msk; header:ADC_CR2_ADON_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | CONT | 1:1 | 0x2 | 0 selects single conversion. | header:ADC_CR2_CONT_Msk; header:ADC_CR2_CONT_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | DMA | 8:8 | 0x100 | 0 disables DMA. | header:ADC_CR2_DMA_Msk; header:ADC_CR2_DMA_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | DDS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_DDS_Msk |
| CR2 | EOCS | 10:10 | 0x400 | 1 sets EOC per conversion and enables overrun detection. | header:ADC_CR2_EOCS_Msk; header:ADC_CR2_EOCS_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | ALIGN | 11:11 | 0x800 | 0 selects right alignment. | header:ADC_CR2_ALIGN_Msk; header:ADC_CR2_ALIGN_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | JEXTSEL | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTSEL_Msk |
| CR2 | JEXTEN | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JEXTEN_Msk |
| CR2 | JSWSTART | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_JSWSTART_Msk |
| CR2 | EXTSEL | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CR2_EXTSEL_Msk |
| CR2 | EXTEN | 29:28 | 0x30000000 | 00 disables external triggering. | header:ADC_CR2_EXTEN_Msk; header:ADC_CR2_EXTEN_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| CR2 | SWSTART | 30:30 | 0x40000000 | Software regular-conversion command; hardware clears when conversion starts. | header:ADC_CR2_SWSTART_Msk; header:ADC_CR2_SWSTART_Msk; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422 |
| SMPR1 | SMP10 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP10_Msk |
| SMPR1 | SMP11 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP11_Msk |
| SMPR1 | SMP12 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP12_Msk |
| SMPR1 | SMP13 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP13_Msk |
| SMPR1 | SMP14 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP14_Msk |
| SMPR1 | SMP15 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP15_Msk |
| SMPR1 | SMP16 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP16_Msk |
| SMPR1 | SMP17 | 23:21 | 0xE00000 | 111 selects 480 cycles for channel 17. | header:ADC_SMPR1_SMP17_Msk; header:ADC_SMPR1_SMP17_Msk; rm_adc_422:page:422 |
| SMPR1 | SMP18 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR1_SMP18_Msk |
| SMPR2 | SMP0 | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP0_Msk |
| SMPR2 | SMP1 | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP1_Msk |
| SMPR2 | SMP2 | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP2_Msk |
| SMPR2 | SMP3 | 11:9 | 0xE00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP3_Msk |
| SMPR2 | SMP4 | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP4_Msk |
| SMPR2 | SMP5 | 17:15 | 0x38000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP5_Msk |
| SMPR2 | SMP6 | 20:18 | 0x1C0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP6_Msk |
| SMPR2 | SMP7 | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP7_Msk |
| SMPR2 | SMP8 | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP8_Msk |
| SMPR2 | SMP9 | 29:27 | 0x38000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SMPR2_SMP9_Msk |
| JOFR1 | JOFFSET1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR1_JOFFSET1_Msk |
| JOFR2 | JOFFSET2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR2_JOFFSET2_Msk |
| JOFR3 | JOFFSET3 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR3_JOFFSET3_Msk |
| JOFR4 | JOFFSET4 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JOFR4_JOFFSET4_Msk |
| HTR | HT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_HTR_HT_Msk |
| LTR | LT | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_LTR_LT_Msk |
| SQR1 | SQ13 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ13_Msk |
| SQR1 | SQ14 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ14_Msk |
| SQR1 | SQ15 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ15_Msk |
| SQR1 | SQ16 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR1_SQ16_Msk |
| SQR1 | L | 23:20 | 0xF00000 | 0000 selects one regular conversion. | header:ADC_SQR1_L_Msk; header:ADC_SQR1_L_Msk; rm_adc_424:page:424 |
| SQR2 | SQ7 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ7_Msk |
| SQR2 | SQ8 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ8_Msk |
| SQR2 | SQ9 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ9_Msk |
| SQR2 | SQ10 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ10_Msk |
| SQR2 | SQ11 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ11_Msk |
| SQR2 | SQ12 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR2_SQ12_Msk |
| SQR3 | SQ1 | 4:0 | 0x1F | 10001 selects ADC1 internal reference channel 17 for the first conversion. | header:ADC_SQR3_SQ1_Msk; header:ADC_SQR3_SQ1_Msk; rm_adc_425:page:425; rm_adc_426:page:426 |
| SQR3 | SQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ2_Msk |
| SQR3 | SQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ3_Msk |
| SQR3 | SQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ4_Msk |
| SQR3 | SQ5 | 24:20 | 0x1F00000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ5_Msk |
| SQR3 | SQ6 | 29:25 | 0x3E000000 | Declaration only; encoding requires reviewed semantics. | header:ADC_SQR3_SQ6_Msk |
| JSQR | JSQ1 | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ1_Msk |
| JSQR | JSQ2 | 9:5 | 0x3E0 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ2_Msk |
| JSQR | JSQ3 | 14:10 | 0x7C00 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ3_Msk |
| JSQR | JSQ4 | 19:15 | 0xF8000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JSQ4_Msk |
| JSQR | JL | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ADC_JSQR_JL_Msk |
| JDR1 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR1_JDATA_Msk |
| JDR2 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR2_JDATA_Msk |
| JDR3 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR3_JDATA_Msk |
| JDR4 | JDATA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_JDR4_JDATA_Msk |
| DR | DATA | 15:0 | 0xFFFF | Regular conversion data; interpreted as right-aligned 12-bit in this mode. | header:ADC_DR_DATA_Msk; header:ADC_DR_DATA_Msk; rm_adc_417:page:417; rm_adc_427:page:427 |
| DR | ADC2DATA | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_DR_ADC2DATA_Msk |

## Reviewed operating semantics

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

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| single_conversion | ADC1 | SR, CR1, CR2, SMPR1, SQR1, SQR3, DR | CR1: RES, SCAN, EOCIE, OVRIE; CR2: ADON, SWSTART, CONT, EOCS, ALIGN, DMA, EXTEN; DR: DATA; SMPR1: SMP17; SQR1: L; SQR3: SQ1; SR: EOC, OVR, STRT | ADC1 only: internal VREFINT is not available through ADC2/ADC3; no GPIO pin or external connection is selected.<br>Fresh owned startup: ADC1/ADC2/ADC3 initially disabled and no other ADC, timer, DMA or interrupt owner. VDDA/VREF+ supply must satisfy the declared datasheet operating range.<br>Set CR1=0, CR2=0, SQR1=0 and SQR3.SQ1=17 while disabled; SMP17=7 means 480 ADC clocks. Keep reserved bits zero.<br>Enable reference/common configuration and ADON&#124;EOCS, then provide at least 10 us reference startup and 3 us ADC power-up settling before SWSTART; the example uses the separate 1 ms TIM2 contract.<br>Clear stale SR flags with SR=0, issue SWSTART only after settling, bound EOC polling, reject OVR and out-of-range raw values, read DR once, then disable ADC/reference and stop the owned timer.<br>No scan, external analog input, injected conversion, ADC2/ADC3, DMA, interrupts, calibration, temperature or precision voltage measurement is supported by this contract. | rm_adc_392:page:392; rm_adc_393:page:393; rm_adc_417:page:417; rm_adc_418:page:418; rm_adc_420:page:420; rm_adc_421:page:421; rm_adc_422:page:422; rm_adc_424:page:424; rm_adc_426:page:426; rm_adc_427:page:427; ds_adc_reference:page:141; ds_adc_136:page:136 | [[peripherals/adc_common]] / internal_reference_prescale4: ADC123_COMMON |

## Review

Reviewer: Codex scoped source-backed editorial review via ingestion MCP. Basis: Header declarations checked against complete RM0090/DS8626 parts; ST RCC implementation resolves the ADC1 enable-table typo. No independent sign-off or physical qualification..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
