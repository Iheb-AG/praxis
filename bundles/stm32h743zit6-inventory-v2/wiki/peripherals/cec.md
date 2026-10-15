# CEC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CEC | 0x40006C00 | Not asserted | Not asserted | header:CEC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.CR |
| CFGR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.CFGR |
| TXDR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.TXDR |
| RXDR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.RXDR |
| ISR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.ISR |
| IER | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CEC_TypeDef.IER |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | CECEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CEC_CR_CECEN_Msk |
| CR | TXSOM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CEC_CR_TXSOM_Msk |
| CR | TXEOM | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CEC_CR_TXEOM_Msk |
| CFGR | SFT | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_SFT_Msk |
| CFGR | RXTOL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_RXTOL_Msk |
| CFGR | BRESTP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_BRESTP_Msk |
| CFGR | BREGEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_BREGEN_Msk |
| CFGR | LBPEGEN | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_LBPEGEN_Msk |
| CFGR | BRDNOGEN | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_BRDNOGEN_Msk |
| CFGR | SFTOPT | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_SFTOPT_Msk |
| CFGR | OAR | 30:16 | 0x7FFF0000 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_OAR_Msk |
| CFGR | LSTN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:CEC_CFGR_LSTN_Msk |
| TXDR | TXD | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:CEC_TXDR_TXD_Msk |
| RXDR | RXD | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:CEC_RXDR_RXD_Msk |
| ISR | RXBR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_RXBR_Msk |
| ISR | RXEND | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_RXEND_Msk |
| ISR | RXOVR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_RXOVR_Msk |
| ISR | BRE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_BRE_Msk |
| ISR | SBPE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_SBPE_Msk |
| ISR | LBPE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_LBPE_Msk |
| ISR | RXACKE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_RXACKE_Msk |
| ISR | ARBLST | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_ARBLST_Msk |
| ISR | TXBR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_TXBR_Msk |
| ISR | TXEND | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_TXEND_Msk |
| ISR | TXUDR | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_TXUDR_Msk |
| ISR | TXERR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_TXERR_Msk |
| ISR | TXACKE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:CEC_ISR_TXACKE_Msk |
| IER | RXBRIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_RXBRIE_Msk |
| IER | RXENDIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_RXENDIE_Msk |
| IER | RXOVRIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_RXOVRIE_Msk |
| IER | BREIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_BREIE_Msk |
| IER | SBPEIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_SBPEIE_Msk |
| IER | LBPEIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_LBPEIE_Msk |
| IER | RXACKEIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_RXACKEIE_Msk |
| IER | ARBLSTIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_ARBLSTIE_Msk |
| IER | TXBRIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_TXBRIE_Msk |
| IER | TXENDIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_TXENDIE_Msk |
| IER | TXUDRIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_TXUDRIE_Msk |
| IER | TXERRIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_TXERRIE_Msk |
| IER | TXACKEIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:CEC_IER_TXACKEIE_Msk |

## Operating semantics unavailable

**cec: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
