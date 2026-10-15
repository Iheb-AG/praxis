# DMA2D — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DMA2D | 0x52001000 | Not asserted | Not asserted | header:DMA2D_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.CR | 1 | 4 |
| ISR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.ISR | 1 | 4 |
| IFCR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.IFCR | 1 | 4 |
| FGMAR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGMAR | 1 | 4 |
| FGOR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGOR | 1 | 4 |
| BGMAR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGMAR | 1 | 4 |
| BGOR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGOR | 1 | 4 |
| FGPFCCR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGPFCCR | 1 | 4 |
| FGCOLR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGCOLR | 1 | 4 |
| BGPFCCR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGPFCCR | 1 | 4 |
| BGCOLR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGCOLR | 1 | 4 |
| FGCMAR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGCMAR | 1 | 4 |
| BGCMAR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGCMAR | 1 | 4 |
| OPFCCR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.OPFCCR | 1 | 4 |
| OCOLR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.OCOLR | 1 | 4 |
| OMAR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.OMAR | 1 | 4 |
| OOR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.OOR | 1 | 4 |
| NLR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.NLR | 1 | 4 |
| LWR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.LWR | 1 | 4 |
| AMTCR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.AMTCR | 1 | 4 |
| FGCLUT | 0x400 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.FGCLUT | 256 | 4 |
| BGCLUT | 0x800 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DMA2D_TypeDef.BGCLUT | 256 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | START | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_START_Msk |
| CR | SUSP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_SUSP_Msk |
| CR | ABORT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_ABORT_Msk |
| CR | LOM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_LOM_Msk |
| CR | TEIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_TEIE_Msk |
| CR | TCIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_TCIE_Msk |
| CR | TWIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_TWIE_Msk |
| CR | CAEIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_CAEIE_Msk |
| CR | CTCIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_CTCIE_Msk |
| CR | CEIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_CEIE_Msk |
| CR | MODE | 18:16 | 0x70000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_CR_MODE_Msk |
| ISR | TEIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_TEIF_Msk |
| ISR | TCIF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_TCIF_Msk |
| ISR | TWIF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_TWIF_Msk |
| ISR | CAEIF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_CAEIF_Msk |
| ISR | CTCIF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_CTCIF_Msk |
| ISR | CEIF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_ISR_CEIF_Msk |
| IFCR | CTEIF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CTEIF_Msk |
| IFCR | CTCIF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CTCIF_Msk |
| IFCR | CTWIF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CTWIF_Msk |
| IFCR | CAECIF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CAECIF_Msk |
| IFCR | CCTCIF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CCTCIF_Msk |
| IFCR | CCEIF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_IFCR_CCEIF_Msk |
| FGMAR | MA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGMAR_MA_Msk |
| FGOR | LO | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGOR_LO_Msk |
| BGMAR | MA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGMAR_MA_Msk |
| BGOR | LO | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGOR_LO_Msk |
| FGPFCCR | CM | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_CM_Msk |
| FGPFCCR | CCM | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_CCM_Msk |
| FGPFCCR | START | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_START_Msk |
| FGPFCCR | CS | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_CS_Msk |
| FGPFCCR | AM | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_AM_Msk |
| FGPFCCR | CSS | 19:18 | 0xC0000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_CSS_Msk |
| FGPFCCR | AI | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_AI_Msk |
| FGPFCCR | RBS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_RBS_Msk |
| FGPFCCR | ALPHA | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGPFCCR_ALPHA_Msk |
| FGCOLR | BLUE | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGCOLR_BLUE_Msk |
| FGCOLR | GREEN | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGCOLR_GREEN_Msk |
| FGCOLR | RED | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGCOLR_RED_Msk |
| BGPFCCR | CM | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_CM_Msk |
| BGPFCCR | CCM | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_CCM_Msk |
| BGPFCCR | START | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_START_Msk |
| BGPFCCR | CS | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_CS_Msk |
| BGPFCCR | AM | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_AM_Msk |
| BGPFCCR | AI | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_AI_Msk |
| BGPFCCR | RBS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_RBS_Msk |
| BGPFCCR | ALPHA | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGPFCCR_ALPHA_Msk |
| BGCOLR | BLUE | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGCOLR_BLUE_Msk |
| BGCOLR | GREEN | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGCOLR_GREEN_Msk |
| BGCOLR | RED | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGCOLR_RED_Msk |
| FGCMAR | MA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_FGCMAR_MA_Msk |
| BGCMAR | MA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_BGCMAR_MA_Msk |
| OPFCCR | CM | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OPFCCR_CM_Msk |
| OPFCCR | SB | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OPFCCR_SB_Msk |
| OPFCCR | AI | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OPFCCR_AI_Msk |
| OPFCCR | RBS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OPFCCR_RBS_Msk |
| OMAR | MA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OMAR_MA_Msk |
| OOR | LO | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_OOR_LO_Msk |
| NLR | NL | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_NLR_NL_Msk |
| NLR | PL | 29:16 | 0x3FFF0000 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_NLR_PL_Msk |
| LWR | LW | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:DMA2D_LWR_LW_Msk |
| AMTCR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_AMTCR_EN_Msk |
| AMTCR | DT | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DMA2D_AMTCR_DT_Msk |

## Operating semantics unavailable

**dma2d: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps (the affected register's entire bit-field set is withheld):

- OCOLR: bit fields withheld: DECLARATION_CONFLICT: DMA2D_OCOLR_GREEN_2_Msk: position and mask disagree

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
