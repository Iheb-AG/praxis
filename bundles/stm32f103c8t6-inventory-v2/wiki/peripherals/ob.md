# OB — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| OB | 0x1FFFF800 | Not asserted | Not asserted | header:OB_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RDP | 0x000 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.RDP |
| USER | 0x002 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.USER |
| Data0 | 0x004 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.Data0 |
| Data1 | 0x006 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.Data1 |
| WRP0 | 0x008 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.WRP0 |
| WRP1 | 0x00A | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.WRP1 |
| WRP2 | 0x00C | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.WRP2 |
| WRP3 | 0x00E | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OB_TypeDef.WRP3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**ob: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
