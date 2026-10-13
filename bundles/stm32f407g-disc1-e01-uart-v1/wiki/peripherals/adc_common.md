# ADC_COMMON — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ADC123_COMMON | 0x40012300 | Not asserted | Not asserted | header:ADC123_COMMON_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CSR; header:ADC_Common_TypeDef.CSR |
| CCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CCR; header:ADC_Common_TypeDef.CCR |
| CDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ADC_Common_TypeDef.CDR; header:ADC_Common_TypeDef.CDR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CSR | AWD1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD1_Msk; header:ADC_CSR_AWD1_Msk |
| CSR | EOC1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC1_Msk; header:ADC_CSR_EOC1_Msk |
| CSR | JEOC1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC1_Msk; header:ADC_CSR_JEOC1_Msk |
| CSR | JSTRT1 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT1_Msk; header:ADC_CSR_JSTRT1_Msk |
| CSR | STRT1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT1_Msk; header:ADC_CSR_STRT1_Msk |
| CSR | OVR1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR1_Msk; header:ADC_CSR_OVR1_Msk |
| CSR | AWD2 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD2_Msk; header:ADC_CSR_AWD2_Msk |
| CSR | EOC2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC2_Msk; header:ADC_CSR_EOC2_Msk |
| CSR | JEOC2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC2_Msk; header:ADC_CSR_JEOC2_Msk |
| CSR | JSTRT2 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT2_Msk; header:ADC_CSR_JSTRT2_Msk |
| CSR | STRT2 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT2_Msk; header:ADC_CSR_STRT2_Msk |
| CSR | OVR2 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR2_Msk; header:ADC_CSR_OVR2_Msk |
| CSR | AWD3 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_AWD3_Msk; header:ADC_CSR_AWD3_Msk |
| CSR | EOC3 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_EOC3_Msk; header:ADC_CSR_EOC3_Msk |
| CSR | JEOC3 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JEOC3_Msk; header:ADC_CSR_JEOC3_Msk |
| CSR | JSTRT3 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_JSTRT3_Msk; header:ADC_CSR_JSTRT3_Msk |
| CSR | STRT3 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_STRT3_Msk; header:ADC_CSR_STRT3_Msk |
| CSR | OVR3 | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CSR_OVR3_Msk; header:ADC_CSR_OVR3_Msk |
| CCR | MULTI | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_MULTI_Msk; header:ADC_CCR_MULTI_Msk |
| CCR | DELAY | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_DELAY_Msk; header:ADC_CCR_DELAY_Msk |
| CCR | DDS | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_DDS_Msk; header:ADC_CCR_DDS_Msk |
| CCR | DMA | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_DMA_Msk; header:ADC_CCR_DMA_Msk |
| CCR | ADCPRE | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_ADCPRE_Msk; header:ADC_CCR_ADCPRE_Msk |
| CCR | VBATE | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_VBATE_Msk; header:ADC_CCR_VBATE_Msk |
| CCR | TSVREFE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CCR_TSVREFE_Msk; header:ADC_CCR_TSVREFE_Msk |
| CDR | DATA1 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ADC_CDR_DATA1_Msk; header:ADC_CDR_DATA1_Msk |
| CDR | DATA2 | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ADC_CDR_DATA2_Msk; header:ADC_CDR_DATA2_Msk |

## Operating semantics unavailable

**adc_common: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
