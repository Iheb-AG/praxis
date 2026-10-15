# VREFBUF — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| VREFBUF | 0x40010030 | Not asserted | Not asserted | header:VREFBUF_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:VREFBUF_TypeDef.CSR |
| CCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:VREFBUF_TypeDef.CCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CSR | ENVR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:VREFBUF_CSR_ENVR_Msk |
| CSR | HIZ | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:VREFBUF_CSR_HIZ_Msk |
| CSR | VRS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:VREFBUF_CSR_VRS_Msk |
| CSR | VRR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:VREFBUF_CSR_VRR_Msk |
| CCR | TRIM | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:VREFBUF_CCR_TRIM_Msk |

## Operating semantics unavailable

**vrefbuf: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
