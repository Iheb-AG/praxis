# CRC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CRC | 0x58024C00 | Not asserted | Not asserted | header:CRC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.DR |
| IDR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.IDR |
| CR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.CR |
| INIT | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.INIT |
| POL | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CRC_TypeDef.POL |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DR | DR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:CRC_DR_DR_Msk |
| IDR | IDR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:CRC_IDR_IDR_Msk |
| CR | RESET | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CRC_CR_RESET_Msk |
| CR | POLYSIZE | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:CRC_CR_POLYSIZE_Msk |
| CR | REV_IN | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:CRC_CR_REV_IN_Msk |
| CR | REV_OUT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CRC_CR_REV_OUT_Msk |
| INIT | INIT | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:CRC_INIT_INIT_Msk |
| POL | POL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:CRC_POL_POL_Msk |

## Operating semantics unavailable

**crc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
