# USB — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USB | 0x40005C00 | Not asserted | Not asserted | header:USB_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EP0R | 0x000 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP0R |
| EP1R | 0x004 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP1R |
| EP2R | 0x008 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP2R |
| EP3R | 0x00C | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP3R |
| EP4R | 0x010 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP4R |
| EP5R | 0x014 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP5R |
| EP6R | 0x018 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP6R |
| EP7R | 0x01C | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.EP7R |
| CNTR | 0x040 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.CNTR |
| ISTR | 0x044 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.ISTR |
| FNR | 0x048 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.FNR |
| DADDR | 0x04C | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.DADDR |
| BTABLE | 0x050 | 16 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_TypeDef.BTABLE |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| EP0R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_EA_Msk |
| EP0R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_STAT_TX_Msk |
| EP0R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_DTOG_TX_Msk |
| EP0R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_CTR_TX_Msk |
| EP0R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_EP_KIND_Msk |
| EP0R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_EP_TYPE_Msk |
| EP0R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_SETUP_Msk |
| EP0R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_STAT_RX_Msk |
| EP0R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_DTOG_RX_Msk |
| EP0R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP0R_CTR_RX_Msk |
| EP1R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_EA_Msk |
| EP1R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_STAT_TX_Msk |
| EP1R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_DTOG_TX_Msk |
| EP1R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_CTR_TX_Msk |
| EP1R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_EP_KIND_Msk |
| EP1R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_EP_TYPE_Msk |
| EP1R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_SETUP_Msk |
| EP1R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_STAT_RX_Msk |
| EP1R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_DTOG_RX_Msk |
| EP1R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP1R_CTR_RX_Msk |
| EP2R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_EA_Msk |
| EP2R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_STAT_TX_Msk |
| EP2R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_DTOG_TX_Msk |
| EP2R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_CTR_TX_Msk |
| EP2R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_EP_KIND_Msk |
| EP2R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_EP_TYPE_Msk |
| EP2R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_SETUP_Msk |
| EP2R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_STAT_RX_Msk |
| EP2R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_DTOG_RX_Msk |
| EP2R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP2R_CTR_RX_Msk |
| EP3R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_EA_Msk |
| EP3R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_STAT_TX_Msk |
| EP3R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_DTOG_TX_Msk |
| EP3R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_CTR_TX_Msk |
| EP3R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_EP_KIND_Msk |
| EP3R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_EP_TYPE_Msk |
| EP3R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_SETUP_Msk |
| EP3R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_STAT_RX_Msk |
| EP3R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_DTOG_RX_Msk |
| EP3R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP3R_CTR_RX_Msk |
| EP4R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_EA_Msk |
| EP4R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_STAT_TX_Msk |
| EP4R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_DTOG_TX_Msk |
| EP4R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_CTR_TX_Msk |
| EP4R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_EP_KIND_Msk |
| EP4R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_EP_TYPE_Msk |
| EP4R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_SETUP_Msk |
| EP4R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_STAT_RX_Msk |
| EP4R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_DTOG_RX_Msk |
| EP4R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP4R_CTR_RX_Msk |
| EP5R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_EA_Msk |
| EP5R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_STAT_TX_Msk |
| EP5R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_DTOG_TX_Msk |
| EP5R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_CTR_TX_Msk |
| EP5R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_EP_KIND_Msk |
| EP5R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_EP_TYPE_Msk |
| EP5R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_SETUP_Msk |
| EP5R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_STAT_RX_Msk |
| EP5R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_DTOG_RX_Msk |
| EP5R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP5R_CTR_RX_Msk |
| EP6R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_EA_Msk |
| EP6R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_STAT_TX_Msk |
| EP6R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_DTOG_TX_Msk |
| EP6R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_CTR_TX_Msk |
| EP6R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_EP_KIND_Msk |
| EP6R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_EP_TYPE_Msk |
| EP6R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_SETUP_Msk |
| EP6R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_STAT_RX_Msk |
| EP6R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_DTOG_RX_Msk |
| EP6R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP6R_CTR_RX_Msk |
| EP7R | EA | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_EA_Msk |
| EP7R | STAT_TX | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_STAT_TX_Msk |
| EP7R | DTOG_TX | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_DTOG_TX_Msk |
| EP7R | CTR_TX | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_CTR_TX_Msk |
| EP7R | EP_KIND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_EP_KIND_Msk |
| EP7R | EP_TYPE | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_EP_TYPE_Msk |
| EP7R | SETUP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_SETUP_Msk |
| EP7R | STAT_RX | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_STAT_RX_Msk |
| EP7R | DTOG_RX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_DTOG_RX_Msk |
| EP7R | CTR_RX | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_EP7R_CTR_RX_Msk |
| CNTR | FRES | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_FRES_Msk |
| CNTR | PDWN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_PDWN_Msk |
| CNTR | LP_MODE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_LP_MODE_Msk |
| CNTR | FSUSP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_FSUSP_Msk |
| CNTR | RESUME | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_RESUME_Msk |
| CNTR | ESOFM | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_ESOFM_Msk |
| CNTR | SOFM | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_SOFM_Msk |
| CNTR | RESETM | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_RESETM_Msk |
| CNTR | SUSPM | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_SUSPM_Msk |
| CNTR | WKUPM | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_WKUPM_Msk |
| CNTR | ERRM | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_ERRM_Msk |
| CNTR | PMAOVRM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_PMAOVRM_Msk |
| CNTR | CTRM | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_CNTR_CTRM_Msk |
| ISTR | EP_ID | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_EP_ID_Msk |
| ISTR | DIR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_DIR_Msk |
| ISTR | ESOF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_ESOF_Msk |
| ISTR | SOF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_SOF_Msk |
| ISTR | RESET | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_RESET_Msk |
| ISTR | SUSP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_SUSP_Msk |
| ISTR | WKUP | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_WKUP_Msk |
| ISTR | ERR | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_ERR_Msk |
| ISTR | PMAOVR | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_PMAOVR_Msk |
| ISTR | CTR | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_ISTR_CTR_Msk |
| FNR | FN | 10:0 | 0x7FF | Declaration only; encoding requires reviewed semantics. | header:USB_FNR_FN_Msk |
| FNR | LSOF | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:USB_FNR_LSOF_Msk |
| FNR | LCK | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_FNR_LCK_Msk |
| FNR | RXDM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_FNR_RXDM_Msk |
| FNR | RXDP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_FNR_RXDP_Msk |
| DADDR | ADD | 6:0 | 0x7F | Declaration only; encoding requires reviewed semantics. | header:USB_DADDR_ADD_Msk |
| DADDR | EF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_DADDR_EF_Msk |
| BTABLE | BTABLE | 15:3 | 0xFFF8 | Declaration only; encoding requires reviewed semantics. | header:USB_BTABLE_BTABLE_Msk |

## Operating semantics unavailable

**usb: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
