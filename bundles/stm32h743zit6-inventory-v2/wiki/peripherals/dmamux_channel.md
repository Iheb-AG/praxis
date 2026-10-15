# DMAMUX_CHANNEL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMAMUX1 | 0x40020800 | Not asserted | Not asserted | header:DMAMUX1_BASE |
| DMAMUX1_Channel0 | 0x40020800 | Not asserted | Not asserted | header:DMAMUX1_Channel0_BASE |
| DMAMUX1_Channel1 | 0x40020804 | Not asserted | Not asserted | header:DMAMUX1_Channel1_BASE |
| DMAMUX1_Channel10 | 0x40020828 | Not asserted | Not asserted | header:DMAMUX1_Channel10_BASE |
| DMAMUX1_Channel11 | 0x4002082C | Not asserted | Not asserted | header:DMAMUX1_Channel11_BASE |
| DMAMUX1_Channel12 | 0x40020830 | Not asserted | Not asserted | header:DMAMUX1_Channel12_BASE |
| DMAMUX1_Channel13 | 0x40020834 | Not asserted | Not asserted | header:DMAMUX1_Channel13_BASE |
| DMAMUX1_Channel14 | 0x40020838 | Not asserted | Not asserted | header:DMAMUX1_Channel14_BASE |
| DMAMUX1_Channel15 | 0x4002083C | Not asserted | Not asserted | header:DMAMUX1_Channel15_BASE |
| DMAMUX1_Channel2 | 0x40020808 | Not asserted | Not asserted | header:DMAMUX1_Channel2_BASE |
| DMAMUX1_Channel3 | 0x4002080C | Not asserted | Not asserted | header:DMAMUX1_Channel3_BASE |
| DMAMUX1_Channel4 | 0x40020810 | Not asserted | Not asserted | header:DMAMUX1_Channel4_BASE |
| DMAMUX1_Channel5 | 0x40020814 | Not asserted | Not asserted | header:DMAMUX1_Channel5_BASE |
| DMAMUX1_Channel6 | 0x40020818 | Not asserted | Not asserted | header:DMAMUX1_Channel6_BASE |
| DMAMUX1_Channel7 | 0x4002081C | Not asserted | Not asserted | header:DMAMUX1_Channel7_BASE |
| DMAMUX1_Channel8 | 0x40020820 | Not asserted | Not asserted | header:DMAMUX1_Channel8_BASE |
| DMAMUX1_Channel9 | 0x40020824 | Not asserted | Not asserted | header:DMAMUX1_Channel9_BASE |
| DMAMUX2 | 0x58025800 | Not asserted | Not asserted | header:DMAMUX2_BASE |
| DMAMUX2_Channel0 | 0x58025800 | Not asserted | Not asserted | header:DMAMUX2_Channel0_BASE |
| DMAMUX2_Channel1 | 0x58025804 | Not asserted | Not asserted | header:DMAMUX2_Channel1_BASE |
| DMAMUX2_Channel2 | 0x58025808 | Not asserted | Not asserted | header:DMAMUX2_Channel2_BASE |
| DMAMUX2_Channel3 | 0x5802580C | Not asserted | Not asserted | header:DMAMUX2_Channel3_BASE |
| DMAMUX2_Channel4 | 0x58025810 | Not asserted | Not asserted | header:DMAMUX2_Channel4_BASE |
| DMAMUX2_Channel5 | 0x58025814 | Not asserted | Not asserted | header:DMAMUX2_Channel5_BASE |
| DMAMUX2_Channel6 | 0x58025818 | Not asserted | Not asserted | header:DMAMUX2_Channel6_BASE |
| DMAMUX2_Channel7 | 0x5802581C | Not asserted | Not asserted | header:DMAMUX2_Channel7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMAMUX_Channel_TypeDef.CCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dmamux_channel: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
