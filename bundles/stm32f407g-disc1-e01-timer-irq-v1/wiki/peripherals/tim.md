# TIM2: reviewed update interrupt subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TIM1 | 0x40010000 | Not asserted | Not asserted outside reviewed workflow | header:TIM1_BASE |
| TIM10 | 0x40014400 | Not asserted | Not asserted outside reviewed workflow | header:TIM10_BASE |
| TIM11 | 0x40014800 | Not asserted | Not asserted outside reviewed workflow | header:TIM11_BASE |
| TIM12 | 0x40001800 | Not asserted | Not asserted outside reviewed workflow | header:TIM12_BASE |
| TIM13 | 0x40001C00 | Not asserted | Not asserted outside reviewed workflow | header:TIM13_BASE |
| TIM14 | 0x40002000 | Not asserted | Not asserted outside reviewed workflow | header:TIM14_BASE |
| TIM2 | 0x40000000 | APB1 | Explicitly selected HSI scenario; see RCC and reviewed notes | header:TIM2_BASE |
| TIM3 | 0x40000400 | Not asserted | Not asserted outside reviewed workflow | header:TIM3_BASE |
| TIM4 | 0x40000800 | Not asserted | Not asserted outside reviewed workflow | header:TIM4_BASE |
| TIM5 | 0x40000C00 | APB1 | Nominal HSI16 with PPRE1=/1 for this reviewed route | header:TIM5_BASE; timer_routes_evidence:rm0090/page:604; timer_routes_evidence:rm0090/page:638 |
| TIM6 | 0x40001000 | Not asserted | Not asserted outside reviewed workflow | header:TIM6_BASE |
| TIM7 | 0x40001400 | Not asserted | Not asserted outside reviewed workflow | header:TIM7_BASE |
| TIM8 | 0x40010400 | Not asserted | Not asserted outside reviewed workflow | header:TIM8_BASE |
| TIM9 | 0x40014000 | Not asserted | Not asserted outside reviewed workflow | header:TIM9_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.CR1; header:TIM_TypeDef.CR1; rm_tim_cr1:page:624; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 | 32 |
| CR2 | 0x004 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.CR2; header:TIM_TypeDef.CR2; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:625; timer_routes_evidence:rm0090/page:624 | 32 |
| SMCR | 0x008 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.SMCR; header:TIM_TypeDef.SMCR; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:626; timer_routes_evidence:rm0090/page:624 | 32 |
| DIER | 0x00C | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.DIER; header:TIM_TypeDef.DIER; rm_tim_dier:page:629; rm_tim_dier:page:629; rm_tim_sr:page:630; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:629; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:628; timer_irq_evidence:rm0090/page:629 | 32 |
| SR | 0x010 | 32 | — | RW | 0x0 | Flags rc_w0. SR=0 discards all flags only under exclusive timer ownership. Input CCR1 read also clears CC1IF. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.SR; header:TIM_TypeDef.SR; rm_tim_sr:page:630; rm_tim_sr:page:630; rm_tim_status:page:631; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:630; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:629; timer_irq_evidence:rm0090/page:630; timer_irq_evidence:rm0090/page:631 | 32 |
| EGR | 0x014 | 32 | — | WO | 0x0 | Write-only actions; UG reinitializes/transfers preloads and may set UIF/TRGO; CC1G generates software capture. Never RMW. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.EGR; header:TIM_TypeDef.EGR; rm_tim_egr:page:632; rm_tim_status:page:631; rm_tim_egr:page:632; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:631; timer_routes_evidence:rm0090/page:624 | 32 |
| CCMR1 | 0x018 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. | header:TIM_TypeDef.CCMR1; header:TIM_TypeDef.CCMR1; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:632 | 32 |
| CCMR2 | 0x01C | 32 | — | RW | 0x0 | Write CCxS only while channel disabled; each selected field view is distinct. Reviewed TIM5 direct TI3 capture only. | header:TIM_TypeDef.CCMR2; header:TIM_TypeDef.CCMR2; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:634; timer_irq_evidence:rm0090/page:634; timer_irq_evidence:rm0090/page:635 | 32 |
| CCER | 0x020 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.CCER; header:TIM_TypeDef.CCER; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:636; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:635 | 32 |
| CNT | 0x024 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.CNT; header:TIM_TypeDef.CNT; rm_tim_values:page:638; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:624 | 32 |
| PSC | 0x028 | 32 | — | RW | 0x0 | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.PSC; header:TIM_TypeDef.PSC; rm_tim_values:page:638; rm_tim_values:page:638; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:624 | 32 |
| ARR | 0x02C | 32 | — | RW | 0xFFFFFFFF | TIM2 reviewed subset only; preserve reserved bits and obey mode requirements. Writes/readback use words. Additional TIM5 application is limited to capture_ch3_pa2; other timer applicability is not inferred. | header:TIM_TypeDef.ARR; header:TIM_TypeDef.ARR; rm_tim_arr:page:639; rm_tim_values:page:638; rm_tim_arr:page:639; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:624 | 32 |
| RCR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.RCR | not asserted |
| CCR1 | 0x034 | 32 | — | mixed | 0x0 | Output-mode preload; read-only in input mode, where reads clear CC1IF. No input-mode write is permitted. | header:TIM_TypeDef.CCR1; header:TIM_TypeDef.CCR1; timer_modes_evidence:rm0090/page:624; timer_modes_evidence:rm0090/page:639 | 32 |
| CCR2 | 0x038 | 32 | — | mixed | 0x0 | TIM2/TIM5 registers are 32-bit: output compare is preload-capable, input capture is read-only and reading clears the corresponding CCxIF. Never write an input CCR. Header field mask documents low16 bits, not the complete hardware value. | header:TIM_TypeDef.CCR2; header:TIM_TypeDef.CCR2; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:640 | 32 |
| CCR3 | 0x03C | 32 | — | mixed | 0x0 | TIM2/TIM5 registers are 32-bit: output compare is preload-capable, input capture is read-only and reading clears the corresponding CCxIF. Never write an input CCR. Header field mask documents low16 bits, not the complete hardware value. | header:TIM_TypeDef.CCR3; header:TIM_TypeDef.CCR3; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:640 | 32 |
| CCR4 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.CCR4 | not asserted |
| BDTR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.BDTR | not asserted |
| DCR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.DCR | not asserted |
| DMAR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.DMAR | not asserted |
| OR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TIM_TypeDef.OR | not asserted |

## Alternative register field views

Each table is a separate interpretation of the same register. Select exactly one view per register as required by a reviewed operating contract. Fields in different views must never be combined into one write. Declaration sets alone do not establish selection conditions, instance availability, pin routing or operating support.

### CCMR1: input_input

Selection: Configured declaration set only; selection conditions require reviewed semantics.

Sources: header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2F_Msk; header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2F_Msk

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR1 | CC1S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_CC1S_Msk |
| CCMR1 | IC1PSC | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1PSC_Msk |
| CCMR1 | IC1F | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_IC1F_Msk |
| CCMR1 | CC2S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_CC2S_Msk |
| CCMR1 | IC2PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2PSC_Msk |
| CCMR1 | IC2F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2F_Msk; header:TIM_CCMR1_IC2F_Msk |

### CCMR1: input_output

Selection: TIM2 subset: CC1S=nonzero and CC2S=00; change selection only with CC1E/CC2E=0.

Sources: header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2CE_Msk; header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2CE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR1 | CC1S | 1:0 | 0x3 | Channel selection:00 output;11 internal TRC only with an internal TS selection. Change only while corresponding CCxE=0. | header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_CC1S_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | IC1PSC | 3:2 | 0xC | 00 captures every event without input prescaling. | header:TIM_CCMR1_IC1PSC_Msk; header:TIM_CCMR1_IC1PSC_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | IC1F | 7:4 | 0xF0 | 0000 leaves input filter disabled; software capture makes no external filtering claim. | header:TIM_CCMR1_IC1F_Msk; header:TIM_CCMR1_IC1F_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | CC2S | 9:8 | 0x300 | Channel selection:00 output;11 internal TRC only with an internal TS selection. Change only while corresponding CCxE=0. | header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_CC2S_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC2FE | 10:10 | 0x400 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2FE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC2PE | 11:11 | 0x800 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2PE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC2M | 14:12 | 0x7000 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2M_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC2CE | 15:15 | 0x8000 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC2CE_Msk; header:TIM_CCMR1_OC2CE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |

### CCMR1: output_input

Selection: Configured declaration set only; selection conditions require reviewed semantics.

Sources: header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2F_Msk; header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2F_Msk

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR1 | CC1S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_CC1S_Msk |
| CCMR1 | OC1FE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1FE_Msk |
| CCMR1 | OC1PE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1PE_Msk |
| CCMR1 | OC1M | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1M_Msk |
| CCMR1 | OC1CE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_OC1CE_Msk |
| CCMR1 | CC2S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_CC2S_Msk |
| CCMR1 | IC2PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2PSC_Msk; header:TIM_CCMR1_IC2PSC_Msk |
| CCMR1 | IC2F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR1_IC2F_Msk; header:TIM_CCMR1_IC2F_Msk |

### CCMR1: output_output

Selection: TIM2 subset: CC1S=00 and CC2S=00; change selection only with CC1E/CC2E=0.

Sources: header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2CE_Msk; header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2CE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR1 | CC1S | 1:0 | 0x3 | Channel selection:00 output;11 internal TRC only with an internal TS selection. Change only while corresponding CCxE=0. | header:TIM_CCMR1_CC1S_Msk; header:TIM_CCMR1_CC1S_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC1FE | 2:2 | 0x4 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC1FE_Msk; header:TIM_CCMR1_OC1FE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC1PE | 3:3 | 0x8 | 1 buffers CCR1; update events transfer its preload to active compare state. | header:TIM_CCMR1_OC1PE_Msk; header:TIM_CCMR1_OC1PE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC1M | 6:4 | 0x70 | 110 PWM1: in upcounting OC1REF is high while CNT&lt;CCR1. | header:TIM_CCMR1_OC1M_Msk; header:TIM_CCMR1_OC1M_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | OC1CE | 7:7 | 0x80 | Keep0 in this subset: fast/clear behavior and channel2 waveform generation are unused. | header:TIM_CCMR1_OC1CE_Msk; header:TIM_CCMR1_OC1CE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634 |
| CCMR1 | CC2S | 9:8 | 0x300 | 00 selects channel2 output; change only with CC2E=0. | header:TIM_CCMR1_CC2S_Msk; header:TIM_CCMR1_CC2S_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:632 |
| CCMR1 | OC2FE | 10:10 | 0x400 | 0 disables fast mode. | header:TIM_CCMR1_OC2FE_Msk; header:TIM_CCMR1_OC2FE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:632 |
| CCMR1 | OC2PE | 11:11 | 0x800 | 1 enables CCR2 preload in pwm_ch2_pa1; 0 disables preload on inactive channel2. | header:TIM_CCMR1_OC2PE_Msk; header:TIM_CCMR1_OC2PE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:632 |
| CCMR1 | OC2M | 14:12 | 0x7000 | 110 PWM1: active while CNT&lt;CCR2 for upcounting; 000 frozen for inactive channel2 in the earlier channel1 mode. | header:TIM_CCMR1_OC2M_Msk; header:TIM_CCMR1_OC2M_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:632 |
| CCMR1 | OC2CE | 15:15 | 0x8000 | 0 disables external clear. | header:TIM_CCMR1_OC2CE_Msk; header:TIM_CCMR1_OC2CE_Msk; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:rm0090/page:633; timer_modes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:632 |

### CCMR2: input_input

Selection: Configured declaration set only; selection conditions require reviewed semantics.

Sources: header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4F_Msk; header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4F_Msk

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR2 | CC3S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_CC3S_Msk |
| CCMR2 | IC3PSC | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3PSC_Msk |
| CCMR2 | IC3F | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_IC3F_Msk |
| CCMR2 | CC4S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_CC4S_Msk |
| CCMR2 | IC4PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4PSC_Msk |
| CCMR2 | IC4F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4F_Msk; header:TIM_CCMR2_IC4F_Msk |

### CCMR2: input_output

Selection: CC3S=01 direct TI3 input; CC4S=00 inactive output. Write selection only with CC3E/CC4E clear.

Sources: header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4CE_Msk; header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4CE_Msk; timer_routes_evidence:rm0090/page:634

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR2 | CC3S | 1:0 | 0x3 | 01 maps IC3 to TI3; change only when CC3E=0. | header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_CC3S_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | IC3PSC | 3:2 | 0xC | 00 capture every detected edge. | header:TIM_CCMR2_IC3PSC_Msk; header:TIM_CCMR2_IC3PSC_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | IC3F | 7:4 | 0xF0 | 0000 no digital filter, sampling at fDTS. | header:TIM_CCMR2_IC3F_Msk; header:TIM_CCMR2_IC3F_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | CC4S | 9:8 | 0x300 | 00 inactive output, CC4E remains0. | header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_CC4S_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | OC4FE | 10:10 | 0x400 | 0 fast mode disabled. | header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4FE_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | OC4PE | 11:11 | 0x800 | 0 preload disabled for inactive channel. | header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4PE_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | OC4M | 14:12 | 0x7000 | 000 frozen inactive output. | header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4M_Msk; timer_routes_evidence:rm0090/page:634 |
| CCMR2 | OC4CE | 15:15 | 0x8000 | 0 external clear disabled. | header:TIM_CCMR2_OC4CE_Msk; header:TIM_CCMR2_OC4CE_Msk; timer_routes_evidence:rm0090/page:634 |

### CCMR2: output_input

Selection: Configured declaration set only; selection conditions require reviewed semantics.

Sources: header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4F_Msk; header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4F_Msk

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR2 | CC3S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_CC3S_Msk |
| CCMR2 | OC3FE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3FE_Msk |
| CCMR2 | OC3PE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3PE_Msk |
| CCMR2 | OC3M | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3M_Msk |
| CCMR2 | OC3CE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_OC3CE_Msk |
| CCMR2 | CC4S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_CC4S_Msk |
| CCMR2 | IC4PSC | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4PSC_Msk; header:TIM_CCMR2_IC4PSC_Msk |
| CCMR2 | IC4F | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_IC4F_Msk; header:TIM_CCMR2_IC4F_Msk |

### CCMR2: output_output

Selection: Configured declaration set only; selection conditions require reviewed semantics.

Sources: header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4CE_Msk; header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4CE_Msk

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CCMR2 | CC3S | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC3S_Msk; header:TIM_CCMR2_CC3S_Msk |
| CCMR2 | OC3FE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3FE_Msk; header:TIM_CCMR2_OC3FE_Msk |
| CCMR2 | OC3PE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3PE_Msk; header:TIM_CCMR2_OC3PE_Msk |
| CCMR2 | OC3M | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3M_Msk; header:TIM_CCMR2_OC3M_Msk |
| CCMR2 | OC3CE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC3CE_Msk; header:TIM_CCMR2_OC3CE_Msk |
| CCMR2 | CC4S | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_CC4S_Msk; header:TIM_CCMR2_CC4S_Msk |
| CCMR2 | OC4FE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4FE_Msk; header:TIM_CCMR2_OC4FE_Msk |
| CCMR2 | OC4PE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4PE_Msk; header:TIM_CCMR2_OC4PE_Msk |
| CCMR2 | OC4M | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4M_Msk; header:TIM_CCMR2_OC4M_Msk |
| CCMR2 | OC4CE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCMR2_OC4CE_Msk; header:TIM_CCMR2_OC4CE_Msk |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | CEN | 0:0 | 0x1 | Enable counter last; keep zero for stopped software capture. | header:TIM_CR1_CEN_Msk; header:TIM_CR1_CEN_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | UDIS | 1:1 | 0x2 | 0 permits update events/preload transfer. | header:TIM_CR1_UDIS_Msk; header:TIM_CR1_UDIS_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | URS | 2:2 | 0x4 | 0 allows UG to set UIF; discard that stale flag. | header:TIM_CR1_URS_Msk; header:TIM_CR1_URS_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | OPM | 3:3 | 0x8 | 0 leaves PWM continuous. | header:TIM_CR1_OPM_Msk; header:TIM_CR1_OPM_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | DIR | 4:4 | 0x10 | 0 selects upcounting. | header:TIM_CR1_DIR_Msk; header:TIM_CR1_DIR_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | CMS | 6:5 | 0x60 | 00 selects edge-aligned mode. | header:TIM_CR1_CMS_Msk; header:TIM_CR1_CMS_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | ARPE | 7:7 | 0x80 | 1 buffers ARR; UG and later update events transfer its preload. | header:TIM_CR1_ARPE_Msk; header:TIM_CR1_ARPE_Msk; rm_tim_cr1:page:624; rm_tim_control:page:625; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR1 | CKD | 9:8 | 0x300 | 00 selects undivided digital-filter sampling basis. | header:TIM_CR1_CKD_Msk; header:TIM_CR1_CKD_Msk; timer_modes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:624 |
| CR2 | CCPC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_CCPC_Msk; header:TIM_CR2_CCPC_Msk |
| CR2 | CCUS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_CCUS_Msk; header:TIM_CR2_CCUS_Msk |
| CR2 | CCDS | 3:3 | 0x8 | 0; DMA requests remain disabled. | header:TIM_CR2_CCDS_Msk; header:TIM_CR2_CCDS_Msk; timer_modes_evidence:rm0090/page:626; timer_routes_evidence:rm0090/page:624 |
| CR2 | MMS | 6:4 | 0x70 | 000 exposes UG on TRGO; require no downstream consumers. | header:TIM_CR2_MMS_Msk; header:TIM_CR2_MMS_Msk; timer_modes_evidence:rm0090/page:626; timer_routes_evidence:rm0090/page:624 |
| CR2 | TI1S | 7:7 | 0x80 | 0 excludes the XOR input combination. | header:TIM_CR2_TI1S_Msk; header:TIM_CR2_TI1S_Msk; timer_modes_evidence:rm0090/page:625; timer_routes_evidence:rm0090/page:624 |
| CR2 | OIS1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS1_Msk; header:TIM_CR2_OIS1_Msk |
| CR2 | OIS1N | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS1N_Msk; header:TIM_CR2_OIS1N_Msk |
| CR2 | OIS2 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS2_Msk; header:TIM_CR2_OIS2_Msk |
| CR2 | OIS2N | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS2N_Msk; header:TIM_CR2_OIS2N_Msk |
| CR2 | OIS3 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS3_Msk; header:TIM_CR2_OIS3_Msk |
| CR2 | OIS3N | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS3N_Msk; header:TIM_CR2_OIS3N_Msk |
| CR2 | OIS4 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CR2_OIS4_Msk; header:TIM_CR2_OIS4_Msk |
| SMCR | SMS | 2:0 | 0x7 | 000 disables slave mode. | header:TIM_SMCR_SMS_Msk; header:TIM_SMCR_SMS_Msk; timer_modes_evidence:rm0090/page:628; timer_routes_evidence:rm0090/page:624 |
| SMCR | TS | 6:4 | 0x70 | 000 selects TIM2 ITR0 from TIM1_TRGO; keep TIM1 gated. | header:TIM_SMCR_TS_Msk; header:TIM_SMCR_TS_Msk; timer_modes_evidence:rm0090/page:628; timer_routes_evidence:rm0090/page:624 |
| SMCR | MSM | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_MSM_Msk; header:TIM_SMCR_MSM_Msk |
| SMCR | ETF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETF_Msk; header:TIM_SMCR_ETF_Msk |
| SMCR | ETPS | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETPS_Msk; header:TIM_SMCR_ETPS_Msk |
| SMCR | ECE | 14:14 | 0x4000 | 0 disables external clock mode2. | header:TIM_SMCR_ECE_Msk; header:TIM_SMCR_ECE_Msk; timer_modes_evidence:rm0090/page:627; timer_routes_evidence:rm0090/page:624 |
| SMCR | ETP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SMCR_ETP_Msk; header:TIM_SMCR_ETP_Msk |
| DIER | UIE | 0:0 | 0x1 | 0 keeps update interrupts disabled. | header:TIM_DIER_UIE_Msk; header:TIM_DIER_UIE_Msk; rm_tim_dier:page:629; rm_tim_sr:page:630; timer_modes_evidence:rm0090/page:630; timer_routes_evidence:rm0090/page:628; timer_routes_evidence:rm0090/page:624 |
| DIER | CC1IE | 1:1 | 0x2 | 0 keeps capture/compare interrupts disabled. | header:TIM_DIER_CC1IE_Msk; header:TIM_DIER_CC1IE_Msk; timer_modes_evidence:rm0090/page:629 |
| DIER | CC2IE | 2:2 | 0x4 | Inactive channel2 request/flag except CC2E output enable; obey pwm_ch2_pa1 explicit sequence. | header:TIM_DIER_CC2IE_Msk; header:TIM_DIER_CC2IE_Msk; timer_routes_evidence:rm0090/page:628 |
| DIER | CC3IE | 3:3 | 0x8 | 0 disables and1 enables capture3 interrupt requests; enable only after handler/vector/line setup and source-cause clearing. | header:TIM_DIER_CC3IE_Msk; header:TIM_DIER_CC3IE_Msk; timer_irq_evidence:rm0090/page:629 |
| DIER | CC4IE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC4IE_Msk |
| DIER | COMIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_COMIE_Msk |
| DIER | TIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_TIE_Msk |
| DIER | BIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_BIE_Msk |
| DIER | UDE | 8:8 | 0x100 | 0 keeps update DMA disabled. | header:TIM_DIER_UDE_Msk; header:TIM_DIER_UDE_Msk; rm_tim_dier:page:629; rm_tim_sr:page:630; timer_modes_evidence:rm0090/page:629; timer_routes_evidence:rm0090/page:628; timer_routes_evidence:rm0090/page:624 |
| DIER | CC1DE | 9:9 | 0x200 | 0 keeps capture/compare DMA disabled. | header:TIM_DIER_CC1DE_Msk; header:TIM_DIER_CC1DE_Msk; timer_modes_evidence:rm0090/page:629 |
| DIER | CC2DE | 10:10 | 0x400 | Inactive channel2 request/flag except CC2E output enable; obey pwm_ch2_pa1 explicit sequence. | header:TIM_DIER_CC2DE_Msk; header:TIM_DIER_CC2DE_Msk; timer_routes_evidence:rm0090/page:628 |
| DIER | CC3DE | 11:11 | 0x800 | 0 keeps capture3 DMA disabled in these polling/IRQ scopes; DMA routing is not supported here. | header:TIM_DIER_CC3DE_Msk; header:TIM_DIER_CC3DE_Msk; timer_irq_evidence:rm0090/page:629 |
| DIER | CC4DE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_CC4DE_Msk |
| DIER | COMDE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_COMDE_Msk |
| DIER | TDE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_DIER_TDE_Msk |
| SR | UIF | 0:0 | 0x1 | rc_w0; UG and natural updates set UIF; discard stale UIF before waiting. | header:TIM_SR_UIF_Msk; header:TIM_SR_UIF_Msk; rm_tim_sr:page:630; rm_tim_status:page:631; timer_modes_evidence:rm0090/page:631; timer_routes_evidence:rm0090/page:629; timer_routes_evidence:rm0090/page:624 |
| SR | CC1IF | 1:1 | 0x2 | rc_w0; input capture sets this flag and reading CCR1 clears it. | header:TIM_SR_CC1IF_Msk; header:TIM_SR_CC1IF_Msk; timer_modes_evidence:rm0090/page:631 |
| SR | CC2IF | 2:2 | 0x4 | Inactive channel2 request/flag except CC2E output enable; obey pwm_ch2_pa1 explicit sequence. | header:TIM_SR_CC2IF_Msk; header:TIM_SR_CC2IF_Msk; timer_routes_evidence:rm0090/page:629 |
| SR | CC3IF | 3:3 | 0x8 | Input capture sets flag; full CCR3 read clears it. Reject a new flag after the data read. | header:TIM_SR_CC3IF_Msk; header:TIM_SR_CC3IF_Msk; timer_irq_evidence:rm0090/page:630; timer_irq_evidence:rm0090/page:631 |
| SR | CC4IF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC4IF_Msk |
| SR | COMIF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_COMIF_Msk |
| SR | TIF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_TIF_Msk |
| SR | BIF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_BIF_Msk |
| SR | CC1OF | 9:9 | 0x200 | rc_w0; another capture while CC1IF is set indicates lost/ambiguous data. | header:TIM_SR_CC1OF_Msk; header:TIM_SR_CC1OF_Msk; timer_modes_evidence:rm0090/page:630 |
| SR | CC2OF | 10:10 | 0x400 | Inactive channel2 request/flag except CC2E output enable; obey pwm_ch2_pa1 explicit sequence. | header:TIM_SR_CC2OF_Msk; header:TIM_SR_CC2OF_Msk; timer_routes_evidence:rm0090/page:629 |
| SR | CC3OF | 11:11 | 0x800 | Set when capture occurs with CC3IF already pending; rc_w0, not cleared by CCR3 read. Reject before/after data read. | header:TIM_SR_CC3OF_Msk; header:TIM_SR_CC3OF_Msk; timer_irq_evidence:rm0090/page:630; timer_irq_evidence:rm0090/page:631 |
| SR | CC4OF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_SR_CC4OF_Msk |
| EGR | UG | 0:0 | 0x1 | Write1 generates update/reinitialization and transfers preloads; never RMW. | header:TIM_EGR_UG_Msk; header:TIM_EGR_UG_Msk; rm_tim_status:page:631; rm_tim_egr:page:632; timer_modes_evidence:rm0090/page:632; timer_routes_evidence:rm0090/page:624 |
| EGR | CC1G | 1:1 | 0x2 | Write1 in input mode captures CNT into CCR1 and sets capture/overcapture status. | header:TIM_EGR_CC1G_Msk; header:TIM_EGR_CC1G_Msk; timer_modes_evidence:rm0090/page:632 |
| EGR | CC2G | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC2G_Msk |
| EGR | CC3G | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC3G_Msk |
| EGR | CC4G | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_CC4G_Msk |
| EGR | COMG | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_COMG_Msk |
| EGR | TG | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_TG_Msk |
| EGR | BG | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TIM_EGR_BG_Msk |
| CCER | CC1E | 0:0 | 0x1 | PWM reference leaves0; input capture enables1 only after setup. | header:TIM_CCER_CC1E_Msk; header:TIM_CCER_CC1E_Msk; timer_modes_evidence:rm0090/page:637 |
| CCER | CC1P | 1:1 | 0x2 | 0 selects noninverted/rising polarity with CC1NP=0. | header:TIM_CCER_CC1P_Msk; header:TIM_CCER_CC1P_Msk; timer_modes_evidence:rm0090/page:637 |
| CCER | CC1NE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC1NE_Msk; header:TIM_CCER_CC1NE_Msk |
| CCER | CC1NP | 3:3 | 0x8 | 0; output mode requires it cleared; input pair00 selects rising. | header:TIM_CCER_CC1NP_Msk; header:TIM_CCER_CC1NP_Msk; timer_modes_evidence:rm0090/page:637 |
| CCER | CC2E | 4:4 | 0x10 | 1 enables TIM2 channel2 physical output only after PA1 route and independent TIM5 capture are ready. | header:TIM_CCER_CC2E_Msk; header:TIM_CCER_CC2E_Msk; timer_routes_evidence:rm0090/page:635 |
| CCER | CC2P | 5:5 | 0x20 | 0 selects active-high PWM output; unsupported polarity modes excluded. | header:TIM_CCER_CC2P_Msk; header:TIM_CCER_CC2P_Msk; timer_routes_evidence:rm0090/page:635 |
| CCER | CC2NE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC2NE_Msk; header:TIM_CCER_CC2NE_Msk |
| CCER | CC2NP | 7:7 | 0x80 | 0 selects active-high PWM output; unsupported polarity modes excluded. | header:TIM_CCER_CC2NP_Msk; header:TIM_CCER_CC2NP_Msk; timer_routes_evidence:rm0090/page:635 |
| CCER | CC3E | 8:8 | 0x100 | 1 enables IC3 capture; enable only after route/timebase setup; 0 disables capture. | header:TIM_CCER_CC3E_Msk; header:TIM_CCER_CC3E_Msk; timer_routes_evidence:rm0090/page:635; timer_routes_evidence:rm0090/page:624 |
| CCER | CC3P | 9:9 | 0x200 | 0 with CC3NP=0 selects rising-edge capture. | header:TIM_CCER_CC3P_Msk; header:TIM_CCER_CC3P_Msk; timer_routes_evidence:rm0090/page:635; timer_routes_evidence:rm0090/page:624 |
| CCER | CC3NE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC3NE_Msk; header:TIM_CCER_CC3NE_Msk |
| CCER | CC3NP | 11:11 | 0x800 | 0 with CC3P=0 selects rising edge; unsupported edge modes not implied. | header:TIM_CCER_CC3NP_Msk; header:TIM_CCER_CC3NP_Msk; timer_routes_evidence:rm0090/page:635; timer_routes_evidence:rm0090/page:624 |
| CCER | CC4E | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4E_Msk; header:TIM_CCER_CC4E_Msk |
| CCER | CC4P | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4P_Msk; header:TIM_CCER_CC4P_Msk |
| CCER | CC4NP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_CCER_CC4NP_Msk; header:TIM_CCER_CC4NP_Msk |
| CNT | CNT | 31:0 | 0xFFFFFFFF | 32-bit TIM2/TIM5 counter; stopped writes/readback precede software capture. | header:TIM_CNT_CNT_Msk; header:TIM_CNT_CNT_Msk; timer_modes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:639; timer_routes_evidence:rm0090/page:624 |
| PSC | PSC | 15:0 | 0xFFFF | 16-bit divider minus1, buffered until update. HSI16/1MHz gives15. | header:TIM_PSC_PSC_Msk; header:TIM_PSC_PSC_Msk; rm_tim_values:page:638; timer_modes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:624 |
| ARR | ARR | 31:0 | 0xFFFFFFFF | 32-bit TIM2/TIM5 reload; zero blocks counting. PWM uses period-1. | header:TIM_ARR_ARR_Msk; header:TIM_ARR_ARR_Msk; rm_tim_values:page:638; rm_tim_arr:page:639; timer_modes_evidence:rm0090/page:639; timer_routes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:639; timer_routes_evidence:rm0090/page:624 |
| RCR | REP | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:TIM_RCR_REP_Msk |
| CCR1 | CCR1 | 15:0 | 0xFFFF | 32-bit TIM2 value: output preload when OC1PE=1; read-only capture data when CC1S!=0; reading clears input CC1IF. | header:TIM_CCR1_CCR1_Msk; header:TIM_CCR1_CCR1_Msk; timer_modes_evidence:rm0090/page:639 |
| CCR2 | CCR2 | 15:0 | 0xFFFF | Declared low16 mask; TIM2/TIM5 full32-bit register transfers are required by the reviewed manual. Do not mask a captured word to this field. | header:TIM_CCR2_CCR2_Msk; header:TIM_CCR2_CCR2_Msk; timer_routes_evidence:rm0090/page:640; timer_routes_evidence:rm0090/page:624 |
| CCR3 | CCR3 | 15:0 | 0xFFFF | Declared low16 mask; TIM2/TIM5 full32-bit register transfers are required by the reviewed manual. Do not mask a captured word to this field. | header:TIM_CCR3_CCR3_Msk; header:TIM_CCR3_CCR3_Msk; timer_routes_evidence:rm0090/page:640; timer_routes_evidence:rm0090/page:624 |
| CCR4 | CCR4 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_CCR4_CCR4_Msk |
| BDTR | DTG | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_DTG_Msk |
| BDTR | LOCK | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_LOCK_Msk |
| BDTR | OSSI | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_OSSI_Msk |
| BDTR | OSSR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_OSSR_Msk |
| BDTR | BKE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BKE_Msk |
| BDTR | BKP | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_BKP_Msk |
| BDTR | AOE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_AOE_Msk |
| BDTR | MOE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:TIM_BDTR_MOE_Msk |
| DCR | DBA | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBA_Msk |
| DCR | DBL | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:TIM_DCR_DBL_Msk |
| DMAR | DMAB | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:TIM_DMAR_DMAB_Msk |
| OR | TI1_RMP | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_TI1_RMP_Msk |
| OR | TI4_RMP | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_TI4_RMP_Msk |
| OR | ITR1_RMP | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:TIM_OR_ITR1_RMP_Msk |

## Reviewed operating semantics

Supported operating subset: **TIM2 internal-clock, edge-aligned upcounter, update interrupt**.
The shared vendor structure also describes other timers; its full declaration map does not
establish that all members exist on TIM2 or that other timer modes are reviewed. RCR and BDTR
are not TIM2 operating registers. CCMR tables retain separate input/output interpretations, including mixed channel directions.
These configured declaration views do not extend this reviewed operating subset: PWM,
input capture, pin routing and their execution requirements remain outside this workflow.

TIM2 is on APB1. If the APB1 prescaler is one, TIM2CLK=PCLK1; otherwise TIM2CLK=2×PCLK1.
For this scenario explicitly establish HSI nominal 16 MHz, AHB /1, APB1 /1 and APB2 /1.
TIM2CLK is then nominal 16 MHz. PSC=15 and ARR=999 give
16,000,000 / ((15+1)×(999+1)) = 1,000 updates/second. This is a design calculation,
not a timing measurement. PSC is 16 bits; TIM2 CNT and ARR are 32 bits.
Evidence: `rm_clock:page:218`, `rm_tim_values:page:638`, `rm_tim_arr:page:639`.

1. Mask interrupts; enable TIM2EN and read back the gate. Reset only owned TIM2 through
   TIM2RST and release reset. Keep CEN and UIE zero while initializing software state.
2. Use CR1=0 (upcounter, edge-aligned, continuous, UDIS=0, URS=0), PSC=15, ARR=999, CNT=0.
3. Write EGR.UG to load the buffered prescaler and reinitialize the counter. This is an
   action register; do not use a read-modify-write. UG can set UIF with this configuration.
4. Clear stale flags with **SR=0** while all channel/trigger uses are disabled. SR flags
   are **rc_w0**, not W1C. In this update-only ISR, SR=0 deliberately clears all timer flags;
   this is inappropriate if unrelated capture/compare owners share the timer.
5. Clear NVIC pending, set priority and enable the TIM2 line only after its handler/state
   are ready; enable UIE and CEN, restore global interrupts last. The bounded ISR checks
   UIF, writes SR=0, increments the millisecond counter and returns. It does not delay.

TIM2_IRQn=28, external vector slot 44, handler TIM2_IRQHandler, from `header:TIM2_IRQn`;
the pinned startup supplies the vector slot. All startup/ELF assets remain separately pinned.
Use unsigned subtraction for millisecond wrap; do not assume SysTick is the time source here.

Source-backed editorial subset: RM0090 Rev22 sections 7.2, 18.4.1/4/5/6/10/11/12,
read through the ingestion MCP. Header masks for shared advanced-timer fields do not change
reserved-bit rules for TIM2. See [[peripherals/rcc]], [[peripherals/nvic]] and [[sources]].

## Separate PLL-clock polling delay

The polling_update_delay contract uses TIM2CLK=84MHz under the explicit
HSE8 PLL mode (APB1/4, PCLK1=42MHz, timer multiplier2). It does not use the
16MHz interrupt example above. Fresh owned TIM2 is required, with no
slave/channel/interrupt/DMA users. Keep CR1=0 and DIER=0 while setting PSC=8399
and ARR=9. Write EGR=UG to load the buffered prescaler and reinitialize CNT.
Then write SR=0 to discard the UIF generated by UG; accepting it as elapsed
time would violate settling. Start CR1=OPM|CEN, poll UIF with a finite iteration
budget and verify CEN cleared. Stop on failure. The calculated interval is
8400*10/84MHz=1ms, not measured timing. No timer pin or NVIC setup is required.

Sources: rm_clock:page:218; rm_tim_cr1:page:624; rm_tim_control:page:625;
rm_tim_dier:page:629; rm_tim_sr:page:630; rm_tim_status:page:631;
rm_tim_egr:page:632; rm_tim_values:page:638; rm_tim_arr:page:639.
See [[peripherals/adc]], [[peripherals/rcc]] and [[features]].

## Preserved timing workflows

Existing TIM2 update-interrupt and PLL-clock polling-delay contracts remain available.
Their source references and mode requirements are preserved in the normalized definitions.
They require their own reviewed clock basis; the new modes below use checked nominal HSI16.
This shared CMSIS layout is not evidence that every register or mode exists on every timer.
RCR/BDTR and advanced-timer fields are outside the TIM2 operating scope.

## Owned TIM2 mode boundary

These two new modes require privileged Thread mode, PRIMASK=1, exclusive fresh-startup
ownership of TIM2 and every downstream consumer of its TRGO signal. No active timer/ADC
consumer may receive its initialization UG pulse. HSI must be on and ready, SW/SWS=HSI,
AHB/APB1/APB2 divisors1 and synchronized SystemCoreClock=16000000. Frequency is nominal.
TIM1 must stay clock-gated: TIM2 ITR0 selects TIM1_TRGO, which must supply no events.
Changing clocks, ownership or register configuration while a mode is active is unsupported.
Use the separate RCC tim2_owned_gate_reset and hsi16_core_checked contracts first.

All writes in these examples are 32-bit words. Keep reserved bits zero. PSC values fit16 bits;
TIM2 CNT/ARR/CCR1 are32 bits. Set CEN=0, DIER=0, CCER=0 before changing channel selection.
Write CR2=0 and SMCR=0, keeping external clock, slave mode and master forwarding disabled.
CR2.MMS=0 still exposes UG as TRGO: it does not suppress initialization trigger pulses.
Verify CCMR1 readback before writing CCR1, because capture configuration makes CCR1 read-only.
Use EGR action writes, never read-modify-write. Clear SR with0 only under exclusive ownership:
flags are rc_w0, not W1C. This discards all timer flags, including UG's stale UIF.

## pwm_ch1_reference — internal PWM1 reference only

This is **not a pin waveform** contract. No GPIO is configured; all CCER channel enables
stay zero, including CC1E. It establishes the timer's OC1REF compare configuration only.
Select the CCMR1 output_output view with CC1S=CC2S=0, OC1M=110 (PWM1), OC1PE=1,
OC1FE=0, OC1CE=0 and inactive channel2 controls. Use CR1.ARPE=1, DIR=0, CMS=0,
UDIS=0, URS=0, OPM=0. Set PSC, ARR, CCR1, CNT=0; then write EGR.UG to transfer
prescaler/ARR/CCR1 preloads. Clear SR, verify configuration, and enable CEN last.
Keep interrupts and DMA requests disabled throughout. No NVIC programming is required.

At nominal16MHz, PSC=15 gives a nominal1MHz counter. ARR=999 produces1000 counts/period:
the nominal reference frequency is1kHz. CCR1=250 gives250 high counts (25%); CCR1=750
gives750 (75%). In upcounting PWM1 OC1REF is high while CNT<CCR1. CCR1=0 is always
inactive; CCR1=ARR+1 is always active. The example API restricts periods to2..UINT32_MAX
counts and high counts to0..period; ARR=0 is excluded because it blocks the counter.

CCR1 writes/readback access the preload while OC1PE=1, not the active comparison value.
A new value takes effect at an update event. Do not generate UG while running to prove a
smooth update: it resets the counter. A bounded UIF wait first clears stale SR, then accepts
only a new update event; timeout latches failure and quiesces the timer. Iteration budgets
are not elapsed-time measurements. No compare-event delivery guarantee is claimed.

## software_capture_ch1 — software event, stopped counter, internal TRC

Select CCMR1 input_output: CC1S=11 maps IC1 to TRC; SMCR.TS=000 selects ITR0/TIM1_TRGO.
TIM1 stays gated and no other owner may generate a trigger. SMS=000 and ECE=0, so the
timer is not externally clocked or slaved. IC1PSC=00, IC1F=0000, CC1P=CC1NP=0.
Keep channel2 and all interrupt/DMA requests disabled. Keep CEN=0 and ARR=0xFFFFFFFF.
Enable CC1E only after configuration, UG, stale-flag clearing and readback succeed.
This uses capture semantics without a GPIO pin or an incoming signal measurement.

Require CC1IF and CC1OF clear before each software event; a stale sample fails the operation.
Write/read back the desired stopped CNT value, then write only EGR.CC1G. In input mode this
captures CNT into CCR1, sets CC1IF, and sets CC1OF if CC1IF was already set.
Poll with a finite iteration budget. Read CCR1 (clears CC1IF) before checking SR again for
overcapture/new pending data. Reject CC1OF, a newly pending CC1IF or a mismatching sample;
publish the sample only after all checks. **Never write CCR1 in capture mode.**
The examples test full-word values0x12345678 and0xFFFFFFFE; they do not measure time,
input filtering, edge polarity or external frequency. Those need separate routed-input modes.

## Failure, shutdown and errata boundary

Configuration/readback/timeout/data failures latch an error. Disable DIER, CCER and CEN and
verify quiescence; retain the error even if cleanup succeeds. Gate loss or held reset prevents
unsafe cleanup accesses and cannot establish quiescence. Failed shutdown remains a failure.
No automatic retry or in-place switch between these modes is supported. Fresh reset/ownership
is needed to reuse the timer. Startup/context/parameter errors before ownership cause no writes.

ES0182 Rev19 sections2.7.1–2.7.4 were read through MCP, including the continuation on page19.
These subsets exclude advanced break/AOE behavior, toggle/center-aligned compare-event
guarantees, OCREF clearing and external/slave reset. They prohibit active TRGO consumers
during initialization and live clock changes, addressing the documented trigger clock-order
restriction. Silicon revision is unconfirmed; this is implementing-author editorial scope,
not independent errata sign-off or hardware qualification.

Sources: timer_modes_evidence:rm0090/pages604,607–608,624–639; timer_modes_evidence:es0182/pages17–19.
The evidence file retains original PDF hashes, source part hashes and editorial fact locators.
See [[peripherals/rcc]], [[features]], [[coverage]], [[index]] and [[sources]].

## External routed PWM and independent capture

The paired workflow tim2_tim5_pwm_capture_loopback assigns pwm_ch2_pa1 only
to TIM2 and capture_ch3_pa2 only to TIM5. It does not qualify the previously
blocked channel1 external workflows, every timer instance, IRQ/DMA or other modes.

Under checked nominal HSI16 and divisors1, TIM2 PSC15/ARR999/CCR2=250 with
CCMR1.output_output (OC2M=110, OC2PE=1) produces nominal1kHz/25% PWM on PA1 AF1.
TIM5 PSC15/ARR0xFFFFFFFF, CCMR2.input_output (CC3S=01 direct TI3, IC3PSC=IC3F=0),
CC3P=CC3NP=0 captures rising edges on PA2 AF2. Set DIR=CMS=SMS=ECE=0.
TIM5 uses an independent free-running32-bit counter, so a wrong TIM2 period cannot
be hidden by measuring against that same wrapping PWM counter. Both clocks still
share HSI: measured ticks do not calibrate physical frequency or duty cycle.

Configure with CEN/channels/requests disabled. Verify output direction before CCR2
write; no input CCR3 write is permitted. UG transfers preloads and can emit TRGO
with MMS=0: no downstream consumers during setup. Clear stale flags while disabled.
Verify pins and configuration, enable/read back TIM5 CC3E then CEN, then TIM2 CC2E
and finally CEN, checking each transition. Discard the enable edge, prime a natural
edge, then validate8 subsequent unsigned32-bit periods of1000+/-2 local ticks.

Poll with a finite budget. Read full32-bit CCR3 (read clears CC3IF), then recheck SR;
reject CC3OF before/after or new CC3IF after the read. Header CCRx field masks cover
low16 bits; RM0090 pages639–640 establish full32-bit TIM2/TIM5 registers. Never mask
capture words to0xFFFF. No calibrated real-time, duty measurement or physical pass
is claimed. Missing wire/changed clock/overcapture/wrong period all latch failure.
Stop both owned timers and release the two pin MODER fields on shutdown; lost
gates or failed writes cannot prove quiet. No automatic retry.

ES0182 Rev19 timer sections2.7.1–2.7.4 remain scoped: no advanced AOE, no active TRGO
consumers during UG or clock changes, no toggle/center compare-event guarantee,
and OC2CE=SMS=0. Independent review, actual PCB verification and the new wired
physical test remain pending. See [[peripherals/rcc]], [[peripherals/gpio]],
[[schemas/custom_pcb_netlist]]. Sources: timer_routes_evidence RM0090 pages604,
624,628–640 and parent timer_modes_evidence ES0182 pages17–19.

## Paired interrupt capture — TIM2 output / TIM5 IRQ50

New modes pwm_ch2_irq_pair (TIM2 only) and capture_ch3_pa2_irq (TIM5 only) use the
reviewed PA1/P1-11 to PA2/P1-14 passive jumper. The older polling modes stay unchanged.
Prepare/read back the pair and GPIO route with channels/counters/requests disabled.
Prepare vector/priority/line; arm capture channel/counter then NVIC line, set onlyCC3IE,
then enable PWM output/CEN and unmask globally. TIM2 DIER stays0. Only ISR reads live CCR3.
Require IPSR66; check live clocks/gates/modes and exact capture cause. Read SR, full32-bit
CCR3, then SR; reject pre/post overcapture, spurious/new events and clock/configuration loss.
Discard enable edge, capture9 natural timestamps, validate8 periods1000+/-2 local ticks,
and require10 IRQ receipts/data reads. Bound Thread wait; pending capture without ISR
delivery is not a no-edge success/failure diagnosis. Disable request before line/pending,
mask globally in Thread, verify inactive/disabled/clear, then stop timers and release pins.
No automatic retry, DMA, other instances/modes or new physical IRQ qualification.

Literal source reconciliation: RM0090 Rev22 DIER=page629, SR=pages630–631. Selected
CC3IE/CC3DE/CC3IF/CC3OF semantic references in this new replacement use those exact parts.
Historical bundles stay immutable; earlier broad context locators are not operating authority
for this new IRQ contract. See [[peripherals/nvic]], [[peripherals/scb]], [[peripherals/gpio]].

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes | Selected register field views |
| --- | --- | --- | --- | --- | --- | --- | --- |
| capture_ch3_pa2 | TIM5 | ARR, CNT, CR1, CR2, PSC, SMCR, CCMR2, CCER, DIER, SR, EGR, CCR3 | ARR: ARR; CCER: CC3E, CC3P, CC3NP; CCMR2: CC3S, IC3PSC, IC3F, CC4S, OC4FE, OC4PE, OC4M, OC4CE; CCR3: CCR3; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC3IE, CC3DE, UDE; EGR: UG; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC3IF, CC3OF | Fresh privileged Thread startup, PRIMASK=1, exclusive ownership of TIM2/TIM5 and GPIOA pins1/2; no downstream TRGO consumers during UG and no live clock/configuration changes.<br>Actual ready HSI selected, nominal16MHz, AHB/APB1/APB2 all divisor1 and SystemCoreClock synchronized; PSC=15 produces nominal1MHz ticks.<br>Configure/read back with channels and CEN disabled; UG transfers preloads and can emit TRGO even when MMS=0; clear stale status only during owned disabled setup.<br>No IRQ/DMA, slave/encoder/external-reset, center-aligned, advanced-timer or other instance support implied. All accesses are full32-bit words; failure latches and never automatically retries.<br>CC3S=01 direct TI3; IC3PSC=IC3F=0, CC3P=CC3NP=0, ARR=0xFFFFFFFF, ARPE=0, SMS=ECE=0, DIER=0; enable/read back capture before PWM output.<br>The counter free-runs independently of TIM2 ARR; read the entire32-bit CCR3 word, never write it. CCR3 input read clears CC3IF.<br>Bound polling; reject CC3OF both before and after data read, or a new CC3IF after read; never publish ambiguous data.<br>Discard enable edge and prime a natural PWM edge, then accept8 successive unsigned32-bit periods1000+/-2 local ticks; this is not independent oscillator calibration.<br>Missing jumper, wrong period, ownership/configuration/clock changes, overflow races or failed shutdown latch failure; restart requires explicit reset. | timer_routes_evidence:rm0090/page:604; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:629; timer_routes_evidence:rm0090/page:634; timer_routes_evidence:rm0090/page:635; timer_routes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:639; timer_routes_evidence:rm0090/page:640 | [[peripherals/gpio]] / pa1_tim2_ch2_pa2_tim5_ch3: GPIOA | CCMR2: input_output |
| capture_ch3_pa2_irq | TIM5 | ARR, CNT, CR1, CR2, PSC, SMCR, CCMR2, CCER, DIER, SR, EGR, CCR3 | ARR: ARR; CCER: CC3E, CC3P, CC3NP; CCMR2: CC3S, IC3PSC, IC3F, CC4S, OC4FE, OC4PE, OC4M, OC4CE; CCR3: CCR3; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC3IE, CC3DE, UDE; EGR: UG; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC3IF, CC3OF | Fresh privileged Thread/MSP startup with PRIMASK1, BASEPRI=FAULTMASK0; only exact paired TIM2/TIM5 route, no downstream UG/TRGO consumers or live owner/clock changes.<br>Prepare/read back complete counters/fields with CEN, channels and DIER disabled; full32-bit capture words, read-only CCR3. Never poll/drain CCR3 in Thread after arming IRQ.<br>Start capture channel/counter first, prepare/read back NVIC line/priority, set DIER=CC3IE only, enable PWM output/counter last, unmask globally after state/vector are ready.<br>ISR must see IPSR66 and expected live clock/pin/register state. Read SR then CCR3 once then SR; reject absent cause, overcapture or a new capture flag after the data read.<br>Discard initial output-enable edge, store9 natural timestamps and validate8 unsigned32-bit intervals1000+/-2 ticks. Success needs10 exception receipts and10 data reads.<br>Terminal ISR disables request before line/pending clear; Thread masks globally and verifies pending/active/enabled zero, then stops owned timers/releases pins. Failure latches, no retry.<br>Bound Thread waiting by iterations. Distinguish a no-stored-edge timeout from pending captures without ISR delivery. No DMA, nesting, other timer modes or physical IRQ acceptance. | timer_irq_evidence:rm0090/page:624; timer_irq_evidence:rm0090/page:629; timer_irq_evidence:rm0090/page:630; timer_irq_evidence:rm0090/page:631; timer_irq_evidence:rm0090/page:634; timer_irq_evidence:rm0090/page:635; timer_irq_evidence:rm0090/page:636; timer_irq_evidence:rm0090/page:638; timer_irq_evidence:rm0090/page:639; timer_irq_evidence:rm0090/page:640 | [[peripherals/gpio]] / pa1_tim2_ch2_pa2_tim5_ch3: GPIOA; [[peripherals/nvic]] / tim5_capture_prepare: NVIC | CCMR2: input_output |
| polling_update_delay | TIM2 | CR1, DIER, SR, EGR, PSC, ARR | ARR: ARR; CR1: CEN, UDIS, URS, OPM, DIR, CMS, ARPE; DIER: UIE, UDE; EGR: UG; PSC: PSC; SR: UIF | Exclusive fresh TIM2, no channel/slave/interrupt/DMA owners, declared HSE8 PLL mode and APB1/4; TIM2CLK=2*PCLK1=84 MHz.<br>Keep CEN=0 and DIER=0 while setting PSC=8399, ARR=9. Write EGR=UG to load PSC/reinitialize counter; write SR=0 afterward to discard the UG-created UIF.<br>Set CR1=OPM&#124;CEN with UDIS/URS/DIR/CMS/ARPE zero. Poll UIF with a finite budget and verify CEN cleared. This is 1 ms nominal under the declared clock assumptions, not measured timing.<br>Do not accept the stale UG flag as elapsed time. Stop the owned timer on failure. This operation uses no timer output pin or NVIC interrupt. | rm_tim_cr1:page:624; rm_tim_control:page:625; rm_tim_status:page:631; rm_tim_egr:page:632; rm_tim_values:page:638; rm_tim_arr:page:639; rm_clock:page:218 | [[peripherals/rcc]] / pll_hse8_168mhz: RCC; [[peripherals/rcc]] / adc_timer_gates: RCC |  |
| pwm_ch1_reference | TIM2 | CR1, CR2, SMCR, DIER, SR, EGR, CCMR1, CCER, CNT, PSC, ARR, CCR1 | ARR: ARR; CCER: CC1E, CC1P, CC1NP; CCMR1: CC1S, OC1FE, OC1PE, OC1M, OC1CE, CC2S, OC2FE, OC2PE, OC2M, OC2CE; CCR1: CCR1; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC1IE, CC1DE, UDE; EGR: UG, CC1G; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC1IF, CC1OF | Fresh privileged owned startup, PRIMASK=1, no downstream TRGO consumers; TIM1 stays gated.<br>Checked nominal HSI16/APB1 divisor1; PSC&lt;=65535, period2..UINT32_MAX counts, high0..period.<br>CC1S=CC2S=0, OC1M=110, OC1PE=1, ARPE=1; all CCER enables and DIER requests remain0.<br>Configure while CEN=0; verify CCMR1 direction before CCR1 write; UG transfers preloads, clear stale SR, verify, enable CEN last.<br>CCR1 readback is preload only; wait for a fresh bounded UIF event for update evidence; no compare-event guarantee.<br>No GPIO/pin waveform, advanced/center/toggle modes, DMA or IRQ support is implied; failure/cleanup never permits automatic retry. | timer_modes_evidence:rm0090/page:604; timer_modes_evidence:rm0090/page:607; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:es0182/page:17; timer_modes_evidence:es0182/page:18; timer_modes_evidence:es0182/page:19 | [[peripherals/rcc]] / tim2_owned_gate_reset: RCC | CCMR1: output_output |
| pwm_ch2_irq_pair | TIM2 | ARR, CNT, CR1, CR2, PSC, SMCR, CCMR1, CCER, DIER, SR, EGR, CCR2 | ARR: ARR; CCER: CC2E, CC2P, CC2NP; CCMR1: CC1S, OC1FE, OC1PE, OC1M, OC1CE, CC2S, OC2FE, OC2PE, OC2M, OC2CE; CCR2: CCR2; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC2IE, CC2DE, UDE; EGR: UG; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC2IF, CC2OF | Fresh checked HSI16/divisors1, exclusive TIM2/TIM5/pin ownership, no downstream UG/TRGO consumers. Configure under global mask; only the final interrupt-ready paired step may unmask.<br>TIM2 PSC15/ARR999/CCR2=250, PWM1/OC2PE/ARPE, direction up/edge-aligned. TIM2 DIER remains0, all other channels disabled; TIM5 alone requests IRQ50.<br>Use complete GPIO AF1 PA1/AF2 PA2 route and verify output direction before CCR2 write. Prepare counters/preloads/stale flags before IRQ arming; capture/line/request ready before final output and CEN.<br>Only the paired capture_irq contract supplies exception receipts and cleanup. On failure mask requests/line, quiesce owned timers/pins and report incomplete shutdown explicitly. No DMA or other timer instance support. | timer_irq_evidence:rm0090/page:624; timer_irq_evidence:rm0090/page:629; timer_irq_evidence:rm0090/page:632; timer_irq_evidence:rm0090/page:638; timer_irq_evidence:rm0090/page:639; timer_irq_evidence:rm0090/page:640 | [[peripherals/gpio]] / pa1_tim2_ch2_pa2_tim5_ch3: GPIOA; [[peripherals/nvic]] / tim5_capture_prepare: NVIC | CCMR1: output_output |
| pwm_ch2_pa1 | TIM2 | ARR, CNT, CR1, CR2, PSC, SMCR, CCMR1, CCER, DIER, SR, EGR, CCR2 | ARR: ARR; CCER: CC2E, CC2P, CC2NP; CCMR1: CC1S, OC1FE, OC1PE, OC1M, OC1CE, CC2S, OC2FE, OC2PE, OC2M, OC2CE; CCR2: CCR2; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC2IE, CC2DE, UDE; EGR: UG; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC2IF, CC2OF | Fresh privileged Thread startup, PRIMASK=1, exclusive ownership of TIM2/TIM5 and GPIOA pins1/2; no downstream TRGO consumers during UG and no live clock/configuration changes.<br>Actual ready HSI selected, nominal16MHz, AHB/APB1/APB2 all divisor1 and SystemCoreClock synchronized; PSC=15 produces nominal1MHz ticks.<br>Configure/read back with channels and CEN disabled; UG transfers preloads and can emit TRGO even when MMS=0; clear stale status only during owned disabled setup.<br>No IRQ/DMA, slave/encoder/external-reset, center-aligned, advanced-timer or other instance support implied. All accesses are full32-bit words; failure latches and never automatically retries.<br>CC2S=CC1S=0, OC2M=110 PWM1, OC2PE=1, ARPE=1, DIR=CMS=0; PSC15/ARR999/CCR2=250 gives nominal1kHz/25% output.<br>Verify CCMR1 output direction before CCR2 write; keep all other channels disabled and DIER=0.<br>Start TIM5 capture timer/channel and verify first, then enable/read back CC2E and enable/read back TIM2 CEN last. Discard the initial output-enable edge.<br>On failure stop owned output/counters and release only the two GPIO pins; inaccessible clocks or failed readback cannot claim quiet shutdown. | timer_routes_evidence:rm0090/page:604; timer_routes_evidence:rm0090/page:624; timer_routes_evidence:rm0090/page:632; timer_routes_evidence:rm0090/page:635; timer_routes_evidence:rm0090/page:638; timer_routes_evidence:rm0090/page:639; timer_routes_evidence:rm0090/page:640 | [[peripherals/gpio]] / pa1_tim2_ch2_pa2_tim5_ch3: GPIOA | CCMR1: output_output |
| software_capture_ch1 | TIM2 | CR1, CR2, SMCR, DIER, SR, EGR, CCMR1, CCER, CNT, PSC, ARR, CCR1 | ARR: ARR; CCER: CC1E, CC1P, CC1NP; CCMR1: CC1S, IC1PSC, IC1F, CC2S, OC2FE, OC2PE, OC2M, OC2CE; CCR1: CCR1; CNT: CNT; CR1: CEN, ARPE, DIR, CMS, UDIS, URS, OPM, CKD; CR2: MMS, TI1S, CCDS; DIER: UIE, CC1IE, CC1DE, UDE; EGR: UG, CC1G; PSC: PSC; SMCR: SMS, TS, ECE; SR: UIF, CC1IF, CC1OF | Fresh privileged owned startup, PRIMASK=1, no downstream TRGO consumers; TIM1 gate remains0.<br>CC1S=11, TS=000 selects TIM1_TRGO/ITR0; SMS=0/ECE=0; IC1PSC=0, IC1F=0, CC1P=CC1NP=0.<br>Keep CEN=0, ARR=0xFFFFFFFF, DIER=0; enable CC1E only after UG, stale clearing and validated setup.<br>Refuse pending CC1IF/CC1OF before issuing an event; write/read back stopped CNT, then action-write EGR.CC1G.<br>Bound polling; read CCR1 before final SR overcapture/new-event check; reject stale, missing, overcaptured or mismatching data.<br>Never write CCR1 in input mode. No external pin, elapsed-time, filter or edge measurement is qualified. | timer_modes_evidence:rm0090/page:604; timer_modes_evidence:rm0090/page:607; timer_modes_evidence:rm0090/page:632; timer_modes_evidence:es0182/page:17; timer_modes_evidence:es0182/page:18; timer_modes_evidence:es0182/page:19 | [[peripherals/rcc]] / tim2_owned_gate_reset: RCC | CCMR1: input_output |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: Complete RM0090 Rev22 and PM0214 Rev10 source parts plus exact pinned IRQ/priority declarations. Implementing-author review only; independent signoff and new physical IRQ qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
