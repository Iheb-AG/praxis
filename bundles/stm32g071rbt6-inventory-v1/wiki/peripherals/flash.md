# FLASH — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

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
| KEYR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR |
| OPTKEYR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTKEYR |
| SR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR |
| CR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR |
| ECCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ECCR |
| OPTR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTR |
| PCROP1ASR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PCROP1ASR |
| PCROP1AER | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PCROP1AER |
| WRP1AR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WRP1AR |
| WRP1BR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WRP1BR |
| PCROP1BSR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PCROP1BSR |
| PCROP1BER | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PCROP1BER |
| SECR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SECR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ACR | LATENCY | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_LATENCY_Msk |
| ACR | PRFTEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_PRFTEN_Msk |
| ACR | ICEN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_ICEN_Msk |
| ACR | ICRST | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_ICRST_Msk |
| ACR | PROGEMPTY | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_PROGEMPTY_Msk |
| ACR | DBG_SWEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_DBG_SWEN_Msk |
| SR | EOP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_EOP_Msk |
| SR | OPERR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_OPERR_Msk |
| SR | PROGERR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PROGERR_Msk |
| SR | WRPERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_WRPERR_Msk |
| SR | PGAERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGAERR_Msk |
| SR | SIZERR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_SIZERR_Msk |
| SR | PGSERR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGSERR_Msk |
| SR | MISERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_MISERR_Msk |
| SR | FASTERR | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_FASTERR_Msk |
| SR | RDERR | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_RDERR_Msk |
| SR | OPTVERR | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_OPTVERR_Msk |
| SR | BSY1 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_BSY1_Msk |
| SR | CFGBSY | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_CFGBSY_Msk |
| CR | PG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PG_Msk |
| CR | PER | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PER_Msk |
| CR | MER1 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_MER1_Msk |
| CR | PNB | 12:3 | 0x1FF8 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PNB_Msk |
| CR | STRT | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_STRT_Msk |
| CR | OPTSTRT | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OPTSTRT_Msk |
| CR | FSTPG | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_FSTPG_Msk |
| CR | EOPIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_EOPIE_Msk |
| CR | ERRIE | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_ERRIE_Msk |
| CR | RDERRIE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_RDERRIE_Msk |
| CR | OBL_LAUNCH | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OBL_LAUNCH_Msk |
| CR | SEC_PROT | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_SEC_PROT_Msk |
| CR | OPTLOCK | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_OPTLOCK_Msk |
| CR | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_LOCK_Msk |
| ECCR | ADDR_ECC | 13:0 | 0x3FFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_ECCR_ADDR_ECC_Msk |
| ECCR | SYSF_ECC | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ECCR_SYSF_ECC_Msk |
| ECCR | ECCCIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ECCR_ECCCIE_Msk |
| ECCR | ECCC | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ECCR_ECCC_Msk |
| ECCR | ECCD | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ECCR_ECCD_Msk |
| OPTR | RDP | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_RDP_Msk |
| OPTR | BOR_EN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_BOR_EN_Msk |
| OPTR | BORR_LEV | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_BORR_LEV_Msk |
| OPTR | BORF_LEV | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_BORF_LEV_Msk |
| OPTR | nRST_STOP | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nRST_STOP_Msk |
| OPTR | nRST_STDBY | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nRST_STDBY_Msk |
| OPTR | nRST_SHDW | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nRST_SHDW_Msk |
| OPTR | IWDG_SW | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_IWDG_SW_Msk |
| OPTR | IWDG_STOP | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_IWDG_STOP_Msk |
| OPTR | IWDG_STDBY | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_IWDG_STDBY_Msk |
| OPTR | WWDG_SW | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_WWDG_SW_Msk |
| OPTR | RAM_PARITY_CHECK | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_RAM_PARITY_CHECK_Msk |
| OPTR | nBOOT_SEL | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nBOOT_SEL_Msk |
| OPTR | nBOOT1 | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nBOOT1_Msk |
| OPTR | nBOOT0 | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_nBOOT0_Msk |
| OPTR | NRST_MODE | 28:27 | 0x18000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_NRST_MODE_Msk |
| OPTR | IRHEN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTR_IRHEN_Msk |
| PCROP1ASR | PCROP1A_STRT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_PCROP1ASR_PCROP1A_STRT_Msk |
| PCROP1AER | PCROP1A_END | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_PCROP1AER_PCROP1A_END_Msk |
| PCROP1AER | PCROP_RDP | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_PCROP1AER_PCROP_RDP_Msk |
| WRP1AR | WRP1A_STRT | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:FLASH_WRP1AR_WRP1A_STRT_Msk |
| WRP1AR | WRP1A_END | 21:16 | 0x3F0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_WRP1AR_WRP1A_END_Msk |
| WRP1BR | WRP1B_STRT | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:FLASH_WRP1BR_WRP1B_STRT_Msk |
| WRP1BR | WRP1B_END | 21:16 | 0x3F0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_WRP1BR_WRP1B_END_Msk |
| PCROP1BSR | PCROP1B_STRT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_PCROP1BSR_PCROP1B_STRT_Msk |
| PCROP1BER | PCROP1B_END | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_PCROP1BER_PCROP1B_END_Msk |
| SECR | SEC_SIZE | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:FLASH_SECR_SEC_SIZE_Msk |
| SECR | BOOT_LOCK | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SECR_BOOT_LOCK_Msk |

## Operating semantics unavailable

**flash: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
