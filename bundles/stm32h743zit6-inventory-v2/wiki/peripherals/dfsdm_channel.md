# DFSDM_CHANNEL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DFSDM1_Channel0 | 0x40017000 | Not asserted | Not asserted | header:DFSDM1_Channel0_BASE |
| DFSDM1_Channel1 | 0x40017020 | Not asserted | Not asserted | header:DFSDM1_Channel1_BASE |
| DFSDM1_Channel2 | 0x40017040 | Not asserted | Not asserted | header:DFSDM1_Channel2_BASE |
| DFSDM1_Channel3 | 0x40017060 | Not asserted | Not asserted | header:DFSDM1_Channel3_BASE |
| DFSDM1_Channel4 | 0x40017080 | Not asserted | Not asserted | header:DFSDM1_Channel4_BASE |
| DFSDM1_Channel5 | 0x400170A0 | Not asserted | Not asserted | header:DFSDM1_Channel5_BASE |
| DFSDM1_Channel6 | 0x400170C0 | Not asserted | Not asserted | header:DFSDM1_Channel6_BASE |
| DFSDM1_Channel7 | 0x400170E0 | Not asserted | Not asserted | header:DFSDM1_Channel7_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CHCFGR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Channel_TypeDef.CHCFGR1 |
| CHCFGR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Channel_TypeDef.CHCFGR2 |
| CHAWSCDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Channel_TypeDef.CHAWSCDR |
| CHWDATAR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Channel_TypeDef.CHWDATAR |
| CHDATINR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Channel_TypeDef.CHDATINR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dfsdm_channel: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
