# ADC common — independent internal-reference subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC123_COMMON | 0x40012300 | APB2 shared | ADCCLK common to all ADCs | header:ADC123_COMMON_BASE; rm_adc_392:page:392; rm_adc_429:page:429 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CSR | not asserted |
| CCR | 0x004 | 32 | — | RW | 0x0 | Shared across all ADCs. Configure only with all ADCs disabled and exclusive ownership. Independent mode, no multi-ADC DMA, VBAT disabled; TSVREFE starts the reference and requires settling. | header:ADC_Common_TypeDef.CCR; header:ADC_Common_TypeDef.CCR; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 | 32 |
| CDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CDR | not asserted |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CSR | AWD1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD1_Msk |
| CSR | EOC1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC1_Msk |
| CSR | JEOC1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC1_Msk |
| CSR | JSTRT1 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT1_Msk |
| CSR | STRT1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT1_Msk |
| CSR | OVR1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR1_Msk |
| CSR | AWD2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD2_Msk |
| CSR | EOC2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC2_Msk |
| CSR | JEOC2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC2_Msk |
| CSR | JSTRT2 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT2_Msk |
| CSR | STRT2 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT2_Msk |
| CSR | OVR2 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR2_Msk |
| CSR | AWD3 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD3_Msk |
| CSR | EOC3 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC3_Msk |
| CSR | JEOC3 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC3_Msk |
| CSR | JSTRT3 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT3_Msk |
| CSR | STRT3 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT3_Msk |
| CSR | OVR3 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR3_Msk |
| CCR | MULTI | 4:0 | 0x1F | 00000 selects independent ADCs. | header:ADC_CCR_MULTI_Msk; header:ADC_CCR_MULTI_Msk; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 |
| CCR | DELAY | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_DELAY_Msk |
| CCR | DDS | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_DDS_Msk |
| CCR | DMA | 15:14 | 0xC000 | 00 disables multi-ADC DMA. | header:ADC_CCR_DMA_Msk; header:ADC_CCR_DMA_Msk; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 |
| CCR | ADCPRE | 17:16 | 0x30000 | 01 selects PCLK2/4. | header:ADC_CCR_ADCPRE_Msk; header:ADC_CCR_ADCPRE_Msk; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 |
| CCR | VBATE | 22:22 | 0x400000 | 0 disables VBAT path. | header:ADC_CCR_VBATE_Msk; header:ADC_CCR_VBATE_Msk; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 |
| CCR | TSVREFE | 23:23 | 0x800000 | 1 enables temperature-sensor/VREFINT circuit; this mode samples only VREFINT. | header:ADC_CCR_TSVREFE_Msk; header:ADC_CCR_TSVREFE_Msk; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431 |
| CDR | DATA1 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_CDR_DATA1_Msk |
| CDR | DATA2 | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CDR_DATA2_Msk |

## Reviewed operating semantics

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

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| internal_reference_prescale4 | ADC123_COMMON | CCR | CCR: MULTI, ADCPRE, DMA, VBATE, TSVREFE | Requires the declared HSE8/168 MHz system profile, PCLK2=84 MHz and assumed VDDA/VREF+ in 2.7–3.6 V; ADCCLK=21 MHz remains below the 36 MHz datasheet ceiling in this range.<br>All ADCs must be disabled and unshared before CCR changes. Select MULTI=0, ADCPRE=1, DMA=0, VBATE=0 and TSVREFE=1; keep reserved bits zero.<br>Allow at least 10 us reference startup and select at least 10 us ADC acquisition; this workflow uses 480 cycles at 21 MHz and a separately implemented 1 ms settling delay.<br>No multi-ADC, external analog, battery, temperature or precision/entropy qualification. | rm_adc_392:page:392; rm_adc_429:page:429; rm_adc_430:page:430; rm_adc_431:page:431; ds_adc_135:page:135; ds_adc_reference:page:141 | [[peripherals/rcc]] / pll_hse8_168mhz: RCC; [[peripherals/rcc]] / adc_timer_gates: RCC |

## Review

Reviewer: Codex scoped source-backed editorial review via ingestion MCP. Basis: Header declarations checked against complete RM0090/DS8626 parts; ST RCC implementation resolves the ADC1 enable-table typo. No independent sign-off or physical qualification..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
