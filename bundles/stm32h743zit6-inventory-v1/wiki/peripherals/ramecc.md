# RAMECC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RAMECC1 | 0x52009000 | Not asserted | Not asserted | header:RAMECC1_BASE |
| RAMECC2 | 0x48023000 | Not asserted | Not asserted | header:RAMECC2_BASE |
| RAMECC3 | 0x58027000 | Not asserted | Not asserted | header:RAMECC3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_TypeDef.IER |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| IER | GIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RAMECC_IER_GIE_Msk |
| IER | GECCSEIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RAMECC_IER_GECCSEIE_Msk |
| IER | GECCDEIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RAMECC_IER_GECCDEIE_Msk |
| IER | GECCDEBWIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RAMECC_IER_GECCDEBWIE_Msk |

## Operating semantics unavailable

**ramecc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
