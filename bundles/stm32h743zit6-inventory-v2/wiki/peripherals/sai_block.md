# SAI_BLOCK — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SAI1_Block_A | 0x40015804 | Not asserted | Not asserted | header:SAI1_Block_A_BASE |
| SAI1_Block_B | 0x40015824 | Not asserted | Not asserted | header:SAI1_Block_B_BASE |
| SAI2_Block_A | 0x40015C04 | Not asserted | Not asserted | header:SAI2_Block_A_BASE |
| SAI2_Block_B | 0x40015C24 | Not asserted | Not asserted | header:SAI2_Block_B_BASE |
| SAI3_Block_A | 0x40016004 | Not asserted | Not asserted | header:SAI3_Block_A_BASE |
| SAI3_Block_B | 0x40016024 | Not asserted | Not asserted | header:SAI3_Block_B_BASE |
| SAI4_Block_A | 0x58005404 | Not asserted | Not asserted | header:SAI4_Block_A_BASE |
| SAI4_Block_B | 0x58005424 | Not asserted | Not asserted | header:SAI4_Block_B_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.CR2 |
| FRCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.FRCR |
| SLOTR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.SLOTR |
| IMR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.IMR |
| SR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.SR |
| CLRFR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.CLRFR |
| DR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SAI_Block_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**sai_block: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
