# AFIO — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| AFIO | 0x40010000 | Not asserted | Not asserted | header:AFIO_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EVCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:AFIO_TypeDef.EVCR | 1 | 4 |
| MAPR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:AFIO_TypeDef.MAPR | 1 | 4 |
| EXTICR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:AFIO_TypeDef.EXTICR | 4 | 4 |
| MAPR2 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:AFIO_TypeDef.MAPR2 | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| EVCR | PIN | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:AFIO_EVCR_PIN_Msk |
| EVCR | PORT | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:AFIO_EVCR_PORT_Msk |
| EVCR | EVOE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:AFIO_EVCR_EVOE_Msk |
| MAPR | SPI1_REMAP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_SPI1_REMAP_Msk |
| MAPR | I2C1_REMAP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_I2C1_REMAP_Msk |
| MAPR | USART1_REMAP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_USART1_REMAP_Msk |
| MAPR | USART2_REMAP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_USART2_REMAP_Msk |
| MAPR | USART3_REMAP | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_USART3_REMAP_Msk |
| MAPR | TIM1_REMAP | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_TIM1_REMAP_Msk |
| MAPR | TIM2_REMAP | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_TIM2_REMAP_Msk |
| MAPR | TIM3_REMAP | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_TIM3_REMAP_Msk |
| MAPR | TIM4_REMAP | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_TIM4_REMAP_Msk |
| MAPR | CAN_REMAP | 14:13 | 0x6000 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_CAN_REMAP_Msk |
| MAPR | PD01_REMAP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_PD01_REMAP_Msk |
| MAPR | SWJ_CFG | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:AFIO_MAPR_SWJ_CFG_Msk |

## Operating semantics unavailable

**afio: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
