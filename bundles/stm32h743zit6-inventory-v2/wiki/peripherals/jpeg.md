# JPEG — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| JPEG | 0x52003000 | Not asserted | Not asserted | header:JPGDEC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CONFR0 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR0 | 1 | 4 |
| CONFR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR1 | 1 | 4 |
| CONFR2 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR2 | 1 | 4 |
| CONFR3 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR3 | 1 | 4 |
| CONFR4 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR4 | 1 | 4 |
| CONFR5 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR5 | 1 | 4 |
| CONFR6 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR6 | 1 | 4 |
| CONFR7 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CONFR7 | 1 | 4 |
| CR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CR | 1 | 4 |
| SR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.SR | 1 | 4 |
| CFR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.CFR | 1 | 4 |
| DIR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.DIR | 1 | 4 |
| DOR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.DOR | 1 | 4 |
| QMEM0 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.QMEM0 | 16 | 4 |
| QMEM1 | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.QMEM1 | 16 | 4 |
| QMEM2 | 0x0D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.QMEM2 | 16 | 4 |
| QMEM3 | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.QMEM3 | 16 | 4 |
| HUFFMIN | 0x150 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFMIN | 16 | 4 |
| HUFFBASE | 0x190 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFBASE | 32 | 4 |
| HUFFSYMB | 0x210 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFSYMB | 84 | 4 |
| DHTMEM | 0x360 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.DHTMEM | 103 | 4 |
| HUFFENC_AC0 | 0x500 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFENC_AC0 | 88 | 4 |
| HUFFENC_AC1 | 0x660 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFENC_AC1 | 88 | 4 |
| HUFFENC_DC0 | 0x7C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFENC_DC0 | 8 | 4 |
| HUFFENC_DC1 | 0x7E0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:JPEG_TypeDef.HUFFENC_DC1 | 8 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CONFR0 | START | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR0_START_Msk |
| CONFR1 | NF | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_NF_Msk |
| CONFR1 | DE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_DE_Msk |
| CONFR1 | COLORSPACE | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_COLORSPACE_Msk |
| CONFR1 | NS | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_NS_Msk |
| CONFR1 | HDR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_HDR_Msk |
| CONFR1 | YSIZE | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR1_YSIZE_Msk |
| CONFR2 | NMCU | 25:0 | 0x3FFFFFF | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR2_NMCU_Msk |
| CONFR3 | XSIZE | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR3_XSIZE_Msk |
| CONFR4 | HD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_HD_Msk |
| CONFR4 | HA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_HA_Msk |
| CONFR4 | QT | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_QT_Msk |
| CONFR4 | NB | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_NB_Msk |
| CONFR4 | VSF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_VSF_Msk |
| CONFR4 | HSF | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR4_HSF_Msk |
| CONFR5 | HD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_HD_Msk |
| CONFR5 | HA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_HA_Msk |
| CONFR5 | QT | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_QT_Msk |
| CONFR5 | NB | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_NB_Msk |
| CONFR5 | VSF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_VSF_Msk |
| CONFR5 | HSF | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR5_HSF_Msk |
| CONFR6 | HD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_HD_Msk |
| CONFR6 | HA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_HA_Msk |
| CONFR6 | QT | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_QT_Msk |
| CONFR6 | NB | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_NB_Msk |
| CONFR6 | VSF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_VSF_Msk |
| CONFR6 | HSF | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR6_HSF_Msk |
| CONFR7 | HD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_HD_Msk |
| CONFR7 | HA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_HA_Msk |
| CONFR7 | QT | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_QT_Msk |
| CONFR7 | NB | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_NB_Msk |
| CONFR7 | VSF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_VSF_Msk |
| CONFR7 | HSF | 15:12 | 0xF000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CONFR7_HSF_Msk |
| CR | JCEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_JCEN_Msk |
| CR | IFTIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_IFTIE_Msk |
| CR | IFNFIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_IFNFIE_Msk |
| CR | OFTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_OFTIE_Msk |
| CR | OFNEIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_OFNEIE_Msk |
| CR | EOCIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_EOCIE_Msk |
| CR | HPDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_HPDIE_Msk |
| CR | IFF | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_IFF_Msk |
| CR | OFF | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CR_OFF_Msk |
| SR | IFTF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_IFTF_Msk |
| SR | IFNFF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_IFNFF_Msk |
| SR | OFTF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_OFTF_Msk |
| SR | OFNEF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_OFNEF_Msk |
| SR | EOCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_EOCF_Msk |
| SR | HPDF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_HPDF_Msk |
| SR | COF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:JPEG_SR_COF_Msk |
| CFR | CEOCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CFR_CEOCF_Msk |
| CFR | CHPDF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:JPEG_CFR_CHPDF_Msk |
| DIR | DATAIN | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:JPEG_DIR_DATAIN_Msk |
| DOR | DATAOUT | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:JPEG_DOR_DATAOUT_Msk |

## Operating semantics unavailable

**jpeg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
