# FPU — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FPU | 0xE000EF30 | Not asserted | Not asserted | cmsis_core:FPU_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FPCCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.FPCCR |
| FPCAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.FPCAR |
| FPDSCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.FPDSCR |
| MVFR0 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.MVFR0 |
| MVFR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.MVFR1 |
| MVFR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:FPU_Type.MVFR2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| FPCCR | LSPACT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_LSPACT_Msk |
| FPCCR | USER | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_USER_Msk |
| FPCCR | THREAD | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_THREAD_Msk |
| FPCCR | HFRDY | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_HFRDY_Msk |
| FPCCR | MMRDY | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_MMRDY_Msk |
| FPCCR | BFRDY | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_BFRDY_Msk |
| FPCCR | MONRDY | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_MONRDY_Msk |
| FPCCR | LSPEN | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_LSPEN_Msk |
| FPCCR | ASPEN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCCR_ASPEN_Msk |
| FPCAR | ADDRESS | 31:3 | 0xFFFFFFF8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPCAR_ADDRESS_Msk |
| FPDSCR | RMode | 23:22 | 0xC00000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPDSCR_RMode_Msk |
| FPDSCR | FZ | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPDSCR_FZ_Msk |
| FPDSCR | DN | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPDSCR_DN_Msk |
| FPDSCR | AHP | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_FPDSCR_AHP_Msk |
| MVFR0 | A_SIMD_registers | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_A_SIMD_registers_Msk |
| MVFR0 | Single_precision | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_Single_precision_Msk |
| MVFR0 | Double_precision | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_Double_precision_Msk |
| MVFR0 | FP_excep_trapping | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_FP_excep_trapping_Msk |
| MVFR0 | Divide | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_Divide_Msk |
| MVFR0 | Square_root | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_Square_root_Msk |
| MVFR0 | Short_vectors | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_Short_vectors_Msk |
| MVFR0 | FP_rounding_modes | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR0_FP_rounding_modes_Msk |
| MVFR1 | FtZ_mode | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR1_FtZ_mode_Msk |
| MVFR1 | D_NaN_mode | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR1_D_NaN_mode_Msk |
| MVFR1 | FP_HPFP | 27:24 | 0xF000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR1_FP_HPFP_Msk |
| MVFR1 | FP_fused_MAC | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR1_FP_fused_MAC_Msk |
| MVFR2 | VFP_Misc | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:FPU_MVFR2_VFP_Misc_Msk |

## Operating semantics unavailable

**fpu: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
