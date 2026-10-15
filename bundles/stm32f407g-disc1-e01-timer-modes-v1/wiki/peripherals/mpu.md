# MPU — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| MPU | 0xE000ED90 | Not asserted | Not asserted | cmsis_core:MPU_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TYPE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.TYPE |
| CTRL | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.CTRL |
| RNR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RNR |
| RBAR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RBAR |
| RASR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RASR |
| RBAR_A1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RBAR_A1 |
| RASR_A1 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RASR_A1 |
| RBAR_A2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RBAR_A2 |
| RASR_A2 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RASR_A2 |
| RBAR_A3 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RBAR_A3 |
| RASR_A3 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:MPU_Type.RASR_A3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| TYPE | SEPARATE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_TYPE_SEPARATE_Msk |
| TYPE | DREGION | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_TYPE_DREGION_Msk |
| TYPE | IREGION | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_TYPE_IREGION_Msk |
| CTRL | ENABLE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_CTRL_ENABLE_Msk |
| CTRL | HFNMIENA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_CTRL_HFNMIENA_Msk |
| CTRL | PRIVDEFENA | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_CTRL_PRIVDEFENA_Msk |
| RNR | REGION | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RNR_REGION_Msk |
| RBAR | REGION | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RBAR_REGION_Msk |
| RBAR | VALID | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RBAR_VALID_Msk |
| RBAR | ADDR | 31:5 | 0xFFFFFFE0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RBAR_ADDR_Msk |
| RASR | ENABLE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RASR_ENABLE_Msk |
| RASR | SIZE | 5:1 | 0x3E | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RASR_SIZE_Msk |
| RASR | SRD | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RASR_SRD_Msk |
| RASR | ATTRS | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:MPU_RASR_ATTRS_Msk |

## Operating semantics unavailable

**mpu: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
