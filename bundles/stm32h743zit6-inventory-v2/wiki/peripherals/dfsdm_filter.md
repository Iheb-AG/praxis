# DFSDM_FILTER — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DFSDM1_Filter0 | 0x40017100 | Not asserted | Not asserted | header:DFSDM1_Filter0_BASE |
| DFSDM1_Filter1 | 0x40017180 | Not asserted | Not asserted | header:DFSDM1_Filter1_BASE |
| DFSDM1_Filter2 | 0x40017200 | Not asserted | Not asserted | header:DFSDM1_Filter2_BASE |
| DFSDM1_Filter3 | 0x40017280 | Not asserted | Not asserted | header:DFSDM1_Filter3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FLTCR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTCR1 |
| FLTCR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTCR2 |
| FLTISR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTISR |
| FLTICR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTICR |
| FLTJCHGR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTJCHGR |
| FLTFCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTFCR |
| FLTJDATAR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTJDATAR |
| FLTRDATAR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTRDATAR |
| FLTAWHTR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTAWHTR |
| FLTAWLTR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTAWLTR |
| FLTAWSR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTAWSR |
| FLTAWCFR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTAWCFR |
| FLTEXMAX | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTEXMAX |
| FLTEXMIN | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTEXMIN |
| FLTCNVTIMR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DFSDM_Filter_TypeDef.FLTCNVTIMR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**dfsdm_filter: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
