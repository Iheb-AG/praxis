# SAI — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SAI1 | 0x40015800 | Not asserted | Not asserted | header:SAI1_BASE |
| SAI2 | 0x40015C00 | Not asserted | Not asserted | header:SAI2_BASE |
| SAI3 | 0x40016000 | Not asserted | Not asserted | header:SAI3_BASE |
| SAI4 | 0x58005400 | Not asserted | Not asserted | header:SAI4_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_TypeDef.GCR |
| PDMCR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_TypeDef.PDMCR |
| PDMDLY | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_TypeDef.PDMDLY |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| GCR | SYNCIN | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SAI_GCR_SYNCIN_Msk |
| GCR | SYNCOUT | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SAI_GCR_SYNCOUT_Msk |
| PDMCR | PDMEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_PDMEN_Msk |
| PDMCR | MICNBR | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_MICNBR_Msk |
| PDMCR | CKEN1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_CKEN1_Msk |
| PDMCR | CKEN2 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_CKEN2_Msk |
| PDMCR | CKEN3 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_CKEN3_Msk |
| PDMCR | CKEN4 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMCR_CKEN4_Msk |
| PDMDLY | DLYM1L | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM1L_Msk |
| PDMDLY | DLYM1R | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM1R_Msk |
| PDMDLY | DLYM2L | 10:8 | 0x700 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM2L_Msk |
| PDMDLY | DLYM2R | 14:12 | 0x7000 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM2R_Msk |
| PDMDLY | DLYM3L | 18:16 | 0x70000 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM3L_Msk |
| PDMDLY | DLYM3R | 22:20 | 0x700000 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM3R_Msk |
| PDMDLY | DLYM4L | 26:24 | 0x7000000 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM4L_Msk |
| PDMDLY | DLYM4R | 30:28 | 0x70000000 | Declaration only; encoding requires reviewed semantics. | header:SAI_PDMDLY_DLYM4R_Msk |

## Operating semantics unavailable

**sai: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
