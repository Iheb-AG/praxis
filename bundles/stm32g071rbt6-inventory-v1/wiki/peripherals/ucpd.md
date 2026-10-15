# UCPD — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| UCPD1 | 0x4000A000 | Not asserted | Not asserted | header:UCPD1_BASE |
| UCPD2 | 0x4000A400 | Not asserted | Not asserted | header:UCPD2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CFG1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.CFG1 |
| CFG2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.CFG2 |
| CR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.CR |
| IMR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.IMR |
| SR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.SR |
| ICR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.ICR |
| TX_ORDSET | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.TX_ORDSET |
| TX_PAYSZ | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.TX_PAYSZ |
| TXDR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.TXDR |
| RX_ORDSET | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.RX_ORDSET |
| RX_PAYSZ | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.RX_PAYSZ |
| RXDR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.RXDR |
| RX_ORDEXT1 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.RX_ORDEXT1 |
| RX_ORDEXT2 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:UCPD_TypeDef.RX_ORDEXT2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CFG1 | HBITCLKDIV | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_HBITCLKDIV_Msk |
| CFG1 | IFRGAP | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_IFRGAP_Msk |
| CFG1 | TRANSWIN | 15:11 | 0xF800 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_TRANSWIN_Msk |
| CFG1 | PSC_UCPDCLK | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_PSC_UCPDCLK_Msk |
| CFG1 | RXORDSETEN | 28:20 | 0x1FF00000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_RXORDSETEN_Msk |
| CFG1 | TXDMAEN | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_TXDMAEN_Msk |
| CFG1 | RXDMAEN | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_RXDMAEN_Msk |
| CFG1 | UCPDEN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG1_UCPDEN_Msk |
| CFG2 | RXFILTDIS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG2_RXFILTDIS_Msk |
| CFG2 | RXFILT2N3 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG2_RXFILT2N3_Msk |
| CFG2 | FORCECLK | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG2_FORCECLK_Msk |
| CFG2 | WUPEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CFG2_WUPEN_Msk |
| CR | TXMODE | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_TXMODE_Msk |
| CR | TXSEND | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_TXSEND_Msk |
| CR | TXHRST | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_TXHRST_Msk |
| CR | RXMODE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_RXMODE_Msk |
| CR | PHYRXEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_PHYRXEN_Msk |
| CR | PHYCCSEL | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_PHYCCSEL_Msk |
| CR | ANASUBMODE | 8:7 | 0x180 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_ANASUBMODE_Msk |
| CR | ANAMODE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_ANAMODE_Msk |
| CR | CCENABLE | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_CCENABLE_Msk |
| CR | FRSRXEN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_FRSRXEN_Msk |
| CR | FRSTX | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_FRSTX_Msk |
| CR | RDCH | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_RDCH_Msk |
| CR | CC1TCDIS | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_CC1TCDIS_Msk |
| CR | CC2TCDIS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_CR_CC2TCDIS_Msk |
| IMR | TXISIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TXISIE_Msk |
| IMR | TXMSGDISCIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TXMSGDISCIE_Msk |
| IMR | TXMSGSENTIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TXMSGSENTIE_Msk |
| IMR | TXMSGABTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TXMSGABTIE_Msk |
| IMR | HRSTDISCIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_HRSTDISCIE_Msk |
| IMR | HRSTSENTIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_HRSTSENTIE_Msk |
| IMR | TXUNDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TXUNDIE_Msk |
| IMR | RXNEIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_RXNEIE_Msk |
| IMR | RXORDDETIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_RXORDDETIE_Msk |
| IMR | RXHRSTDETIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_RXHRSTDETIE_Msk |
| IMR | RXOVRIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_RXOVRIE_Msk |
| IMR | RXMSGENDIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_RXMSGENDIE_Msk |
| IMR | TYPECEVT1IE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TYPECEVT1IE_Msk |
| IMR | TYPECEVT2IE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_TYPECEVT2IE_Msk |
| IMR | FRSEVTIE | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_IMR_FRSEVTIE_Msk |
| SR | TXIS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TXIS_Msk |
| SR | TXMSGDISC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TXMSGDISC_Msk |
| SR | TXMSGSENT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TXMSGSENT_Msk |
| SR | TXMSGABT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TXMSGABT_Msk |
| SR | HRSTDISC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_HRSTDISC_Msk |
| SR | HRSTSENT | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_HRSTSENT_Msk |
| SR | TXUND | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TXUND_Msk |
| SR | RXNE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXNE_Msk |
| SR | RXORDDET | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXORDDET_Msk |
| SR | RXHRSTDET | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXHRSTDET_Msk |
| SR | RXOVR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXOVR_Msk |
| SR | RXMSGEND | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXMSGEND_Msk |
| SR | RXERR | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_RXERR_Msk |
| SR | TYPECEVT1 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TYPECEVT1_Msk |
| SR | TYPECEVT2 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TYPECEVT2_Msk |
| SR | TYPEC_VSTATE_CC1 | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TYPEC_VSTATE_CC1_Msk |
| SR | TYPEC_VSTATE_CC2 | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_TYPEC_VSTATE_CC2_Msk |
| SR | FRSEVT | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_SR_FRSEVT_Msk |
| ICR | TXMSGDISCCF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TXMSGDISCCF_Msk |
| ICR | TXMSGSENTCF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TXMSGSENTCF_Msk |
| ICR | TXMSGABTCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TXMSGABTCF_Msk |
| ICR | HRSTDISCCF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_HRSTDISCCF_Msk |
| ICR | HRSTSENTCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_HRSTSENTCF_Msk |
| ICR | TXUNDCF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TXUNDCF_Msk |
| ICR | RXORDDETCF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_RXORDDETCF_Msk |
| ICR | RXHRSTDETCF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_RXHRSTDETCF_Msk |
| ICR | RXOVRCF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_RXOVRCF_Msk |
| ICR | RXMSGENDCF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_RXMSGENDCF_Msk |
| ICR | TYPECEVT1CF | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TYPECEVT1CF_Msk |
| ICR | TYPECEVT2CF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_TYPECEVT2CF_Msk |
| ICR | FRSEVTCF | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:UCPD_ICR_FRSEVTCF_Msk |
| TX_ORDSET | TXORDSET | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:UCPD_TX_ORDSET_TXORDSET_Msk |
| TX_PAYSZ | TXPAYSZ | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:UCPD_TX_PAYSZ_TXPAYSZ_Msk |
| TXDR | TXDATA | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:UCPD_TXDR_TXDATA_Msk |
| RX_ORDSET | RXORDSET | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_ORDSET_RXORDSET_Msk |
| RX_ORDSET | RXSOP3OF4 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_ORDSET_RXSOP3OF4_Msk |
| RX_ORDSET | RXSOPKINVALID | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_ORDSET_RXSOPKINVALID_Msk |
| RX_PAYSZ | RXPAYSZ | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_PAYSZ_RXPAYSZ_Msk |
| RXDR | RXDATA | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:UCPD_RXDR_RXDATA_Msk |
| RX_ORDEXT1 | RXSOPX1 | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_ORDEXT1_RXSOPX1_Msk |
| RX_ORDEXT2 | RXSOPX2 | 19:0 | 0xFFFFF | Declaration only; encoding requires reviewed semantics. | header:UCPD_RX_ORDEXT2_RXSOPX2_Msk |

## Operating semantics unavailable

**ucpd: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
