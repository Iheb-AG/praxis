# RAMECC_MONITOR — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RAMECC1_Monitor1 | 0x52009020 | Not asserted | Not asserted | header:RAMECC1_Monitor1_BASE |
| RAMECC1_Monitor2 | 0x52009040 | Not asserted | Not asserted | header:RAMECC1_Monitor2_BASE |
| RAMECC1_Monitor3 | 0x52009060 | Not asserted | Not asserted | header:RAMECC1_Monitor3_BASE |
| RAMECC1_Monitor4 | 0x52009080 | Not asserted | Not asserted | header:RAMECC1_Monitor4_BASE |
| RAMECC1_Monitor5 | 0x520090A0 | Not asserted | Not asserted | header:RAMECC1_Monitor5_BASE |
| RAMECC2_Monitor1 | 0x48023020 | Not asserted | Not asserted | header:RAMECC2_Monitor1_BASE |
| RAMECC2_Monitor2 | 0x48023040 | Not asserted | Not asserted | header:RAMECC2_Monitor2_BASE |
| RAMECC2_Monitor3 | 0x48023060 | Not asserted | Not asserted | header:RAMECC2_Monitor3_BASE |
| RAMECC2_Monitor4 | 0x48023080 | Not asserted | Not asserted | header:RAMECC2_Monitor4_BASE |
| RAMECC2_Monitor5 | 0x480230A0 | Not asserted | Not asserted | header:RAMECC2_Monitor5_BASE |
| RAMECC3_Monitor1 | 0x58027020 | Not asserted | Not asserted | header:RAMECC3_Monitor1_BASE |
| RAMECC3_Monitor2 | 0x58027040 | Not asserted | Not asserted | header:RAMECC3_Monitor2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.CR |
| SR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.SR |
| FAR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.FAR |
| FDRL | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.FDRL |
| FDRH | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.FDRH |
| FECR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RAMECC_MonitorTypeDef.FECR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**ramecc_monitor: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
