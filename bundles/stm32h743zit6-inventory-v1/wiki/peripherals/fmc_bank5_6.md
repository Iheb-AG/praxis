# FMC_BANK5_6 — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FMC_Bank5_6_R | 0x52004140 | Not asserted | Not asserted | header:FMC_Bank5_6_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SDCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FMC_Bank5_6_TypeDef.SDCR | 2 | 4 |
| SDTR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FMC_Bank5_6_TypeDef.SDTR | 2 | 4 |
| SDCMR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FMC_Bank5_6_TypeDef.SDCMR | 1 | 4 |
| SDRTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FMC_Bank5_6_TypeDef.SDRTR | 1 | 4 |
| SDSR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FMC_Bank5_6_TypeDef.SDSR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**fmc_bank5_6: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
