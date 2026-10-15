# DMAMUX_REQUESTGEN — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMAMUX1_RequestGenerator0 | 0x40020900 | Not asserted | Not asserted | header:DMAMUX1_RequestGenerator0_BASE |
| DMAMUX1_RequestGenerator1 | 0x40020904 | Not asserted | Not asserted | header:DMAMUX1_RequestGenerator1_BASE |
| DMAMUX1_RequestGenerator2 | 0x40020908 | Not asserted | Not asserted | header:DMAMUX1_RequestGenerator2_BASE |
| DMAMUX1_RequestGenerator3 | 0x4002090C | Not asserted | Not asserted | header:DMAMUX1_RequestGenerator3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RGCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMAMUX_RequestGen_TypeDef.RGCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dmamux_requestgen: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
