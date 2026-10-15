# FLASH — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FLASH | 0x40022000 | Not asserted | Not asserted | header:FLASH_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ACR |
| KEYR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR |
| OPTKEYR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTKEYR |
| SR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR |
| CR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR |
| AR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.AR |
| OBR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OBR |
| WRPR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WRPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ACR | LATENCY | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_LATENCY_Msk |
| ACR | HLFCYA | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_HLFCYA_Msk |
| ACR | PRFTBE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_PRFTBE_Msk |
| ACR | PRFTBS | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_PRFTBS_Msk |
| KEYR | FKEYR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_KEYR_FKEYR_Msk |
| OPTKEYR | OPTKEYR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTKEYR_OPTKEYR_Msk |
| SR | BSY | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_BSY_Msk |
| SR | PGERR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGERR_Msk |
| SR | WRPRTERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_WRPRTERR_Msk |
| SR | EOP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_EOP_Msk |
| CR | PG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PG_Msk |
| CR | PER | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PER_Msk |
| CR | MER | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_MER_Msk |
| CR | OPTPG | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OPTPG_Msk |
| CR | OPTER | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OPTER_Msk |
| CR | STRT | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_STRT_Msk |
| CR | LOCK | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_LOCK_Msk |
| CR | OPTWRE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OPTWRE_Msk |
| CR | ERRIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_ERRIE_Msk |
| CR | EOPIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_EOPIE_Msk |
| AR | FAR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_AR_FAR_Msk |
| OBR | OPTERR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OBR_OPTERR_Msk |
| OBR | RDPRT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OBR_RDPRT_Msk |
| OBR | USER | 4:2 | 0x1C | Declaration only; encoding requires reviewed semantics. | header:FLASH_OBR_USER_Msk |
| OBR | DATA0 | 17:10 | 0x3FC00 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OBR_DATA0_Msk |
| OBR | DATA1 | 25:18 | 0x3FC0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OBR_DATA1_Msk |
| WRPR | WRP | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_WRPR_WRP_Msk |

## Operating semantics unavailable

**flash: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
