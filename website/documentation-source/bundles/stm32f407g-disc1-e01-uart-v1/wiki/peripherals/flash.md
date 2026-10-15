# FLASH — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FLASH | 0x40023C00 | Not asserted | Not asserted | header:FLASH_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ACR; header:FLASH_TypeDef.ACR |
| KEYR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR; header:FLASH_TypeDef.KEYR |
| OPTKEYR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTKEYR; header:FLASH_TypeDef.OPTKEYR |
| SR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR; header:FLASH_TypeDef.SR |
| CR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR; header:FLASH_TypeDef.CR |
| OPTCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCR; header:FLASH_TypeDef.OPTCR |
| OPTCR1 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCR1; header:FLASH_TypeDef.OPTCR1 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| SR | EOP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_EOP_Msk; header:FLASH_SR_EOP_Msk |
| SR | OPERR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_OPERR_Msk; header:FLASH_SR_OPERR_Msk |
| SR | WRPERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_WRPERR_Msk; header:FLASH_SR_WRPERR_Msk |
| SR | PGAERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGAERR_Msk; header:FLASH_SR_PGAERR_Msk |
| SR | PGPERR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGPERR_Msk; header:FLASH_SR_PGPERR_Msk |
| SR | PGSERR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGSERR_Msk; header:FLASH_SR_PGSERR_Msk |
| SR | BSY | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_BSY_Msk; header:FLASH_SR_BSY_Msk |
| CR | PG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PG_Msk; header:FLASH_CR_PG_Msk |
| CR | SER | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_SER_Msk; header:FLASH_CR_SER_Msk |
| CR | MER | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_MER_Msk; header:FLASH_CR_MER_Msk |
| CR | SNB | 6:3 | 0x78 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_SNB_Msk; header:FLASH_CR_SNB_Msk |
| CR | PSIZE | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PSIZE_Msk; header:FLASH_CR_PSIZE_Msk |
| CR | STRT | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_STRT_Msk; header:FLASH_CR_STRT_Msk |
| CR | EOPIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_EOPIE_Msk; header:FLASH_CR_EOPIE_Msk |
| CR | ERRIE | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_ERRIE_Msk; header:FLASH_CR_ERRIE_Msk |
| CR | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_LOCK_Msk; header:FLASH_CR_LOCK_Msk |
| OPTCR | OPTLOCK | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTLOCK_Msk; header:FLASH_OPTCR_OPTLOCK_Msk |
| OPTCR | OPTSTRT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTSTRT_Msk; header:FLASH_OPTCR_OPTSTRT_Msk |
| OPTCR | BOR_LEV | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_BOR_LEV_Msk; header:FLASH_OPTCR_BOR_LEV_Msk |
| OPTCR | WDG_SW | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_WDG_SW_Msk; header:FLASH_OPTCR_WDG_SW_Msk |
| OPTCR | nRST_STOP | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nRST_STOP_Msk; header:FLASH_OPTCR_nRST_STOP_Msk |
| OPTCR | nRST_STDBY | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nRST_STDBY_Msk; header:FLASH_OPTCR_nRST_STDBY_Msk |
| OPTCR | RDP | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_RDP_Msk; header:FLASH_OPTCR_RDP_Msk |
| OPTCR | nWRP | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nWRP_Msk; header:FLASH_OPTCR_nWRP_Msk |
| OPTCR1 | nWRP | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR1_nWRP_Msk; header:FLASH_OPTCR1_nWRP_Msk |

## Operating semantics unavailable

**flash: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- ACR: bit fields withheld: UNSUPPORTED_MASK: FLASH_ACR_BYTE0_ADDRESS_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
