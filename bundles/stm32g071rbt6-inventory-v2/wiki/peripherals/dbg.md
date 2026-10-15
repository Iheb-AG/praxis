# DBG — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DBG | 0x40015800 | Not asserted | Not asserted | header:DBG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IDCODE | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBG_TypeDef.IDCODE |
| CR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBG_TypeDef.CR |
| APBFZ1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBG_TypeDef.APBFZ1 |
| APBFZ2 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DBG_TypeDef.APBFZ2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| IDCODE | DEV_ID | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:DBG_IDCODE_DEV_ID_Msk |
| IDCODE | REV_ID | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:DBG_IDCODE_REV_ID_Msk |
| CR | DBG_STOP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DBG_CR_DBG_STOP_Msk |
| CR | DBG_STANDBY | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DBG_CR_DBG_STANDBY_Msk |

## Operating semantics unavailable

**dbg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
