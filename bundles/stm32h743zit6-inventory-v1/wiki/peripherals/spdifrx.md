# SPDIFRX — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SPDIFRX | 0x40004000 | Not asserted | Not asserted | header:SPDIFRX_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.CR |
| IMR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.IMR |
| SR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.SR |
| IFCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.IFCR |
| DR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.DR |
| CSR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.CSR |
| DIR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPDIFRX_TypeDef.DIR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | SPDIFEN | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_SPDIFEN_Msk |
| CR | RXDMAEN | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_RXDMAEN_Msk |
| CR | RXSTEO | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_RXSTEO_Msk |
| CR | DRFMT | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_DRFMT_Msk |
| CR | PMSK | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_PMSK_Msk |
| CR | VMSK | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_VMSK_Msk |
| CR | CUMSK | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_CUMSK_Msk |
| CR | PTMSK | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_PTMSK_Msk |
| CR | CBDMAEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_CBDMAEN_Msk |
| CR | CHSEL | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_CHSEL_Msk |
| CR | NBTR | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_NBTR_Msk |
| CR | WFA | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_WFA_Msk |
| CR | INSEL | 18:16 | 0x70000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_INSEL_Msk |
| CR | CKSEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_CKSEN_Msk |
| CR | CKSBKPEN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CR_CKSBKPEN_Msk |
| IMR | RXNEIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_RXNEIE_Msk |
| IMR | CSRNEIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_CSRNEIE_Msk |
| IMR | PERRIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_PERRIE_Msk |
| IMR | OVRIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_OVRIE_Msk |
| IMR | SBLKIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_SBLKIE_Msk |
| IMR | SYNCDIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_SYNCDIE_Msk |
| IMR | IFEIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IMR_IFEIE_Msk |
| SR | RXNE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_RXNE_Msk |
| SR | CSRNE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_CSRNE_Msk |
| SR | PERR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_PERR_Msk |
| SR | OVR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_OVR_Msk |
| SR | SBD | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_SBD_Msk |
| SR | SYNCD | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_SYNCD_Msk |
| SR | FERR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_FERR_Msk |
| SR | SERR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_SERR_Msk |
| SR | TERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_TERR_Msk |
| SR | WIDTH5 | 30:16 | 0x7FFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_SR_WIDTH5_Msk |
| IFCR | PERRCF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IFCR_PERRCF_Msk |
| IFCR | OVRCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IFCR_OVRCF_Msk |
| IFCR | SBDCF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IFCR_SBDCF_Msk |
| IFCR | SYNCDCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_IFCR_SYNCDCF_Msk |
| CSR | USR | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CSR_USR_Msk |
| CSR | CS | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CSR_CS_Msk |
| CSR | SOB | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_CSR_SOB_Msk |
| DIR | THI | 12:0 | 0x1FFF | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_DIR_THI_Msk |
| DIR | TLO | 28:16 | 0x1FFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPDIFRX_DIR_TLO_Msk |

## Operating semantics unavailable

**spdifrx: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
