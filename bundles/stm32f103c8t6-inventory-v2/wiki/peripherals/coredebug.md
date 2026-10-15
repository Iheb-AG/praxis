# COREDEBUG — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CoreDebug | 0xE000EDF0 | Not asserted | Not asserted | core_cm3_h:CoreDebug_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DHCSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm3_h:CoreDebug_Type.DHCSR |
| DCRSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm3_h:CoreDebug_Type.DCRSR |
| DCRDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm3_h:CoreDebug_Type.DCRDR |
| DEMCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | core_cm3_h:CoreDebug_Type.DEMCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**coredebug: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
