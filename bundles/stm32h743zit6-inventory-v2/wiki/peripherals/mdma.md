# MDMA — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| MDMA | 0x52000000 | Not asserted | Not asserted | header:MDMA_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GISR0 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:MDMA_TypeDef.GISR0 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| GISR0 | GIF0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF0_Msk |
| GISR0 | GIF1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF1_Msk |
| GISR0 | GIF2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF2_Msk |
| GISR0 | GIF3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF3_Msk |
| GISR0 | GIF4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF4_Msk |
| GISR0 | GIF5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF5_Msk |
| GISR0 | GIF6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF6_Msk |
| GISR0 | GIF7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF7_Msk |
| GISR0 | GIF8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF8_Msk |
| GISR0 | GIF9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF9_Msk |
| GISR0 | GIF10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF10_Msk |
| GISR0 | GIF11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF11_Msk |
| GISR0 | GIF12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF12_Msk |
| GISR0 | GIF13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF13_Msk |
| GISR0 | GIF14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF14_Msk |
| GISR0 | GIF15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:MDMA_GISR0_GIF15_Msk |

## Operating semantics unavailable

**mdma: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
