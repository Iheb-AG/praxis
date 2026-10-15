# SPI — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SPI1 | 0x40013000 | Not asserted | Not asserted | header:SPI1_BASE |
| SPI2 | 0x40003800 | Not asserted | Not asserted | header:SPI2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CR2 |
| SR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.SR |
| DR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.DR |
| CRCPR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CRCPR |
| RXCRCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.RXCRCR |
| TXCRCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.TXCRCR |
| I2SCFGR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.I2SCFGR |
| I2SPR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.I2SPR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | CPHA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CPHA_Msk |
| CR1 | CPOL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CPOL_Msk |
| CR1 | MSTR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_MSTR_Msk |
| CR1 | BR | 5:3 | 0x38 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_BR_Msk |
| CR1 | SPE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_SPE_Msk |
| CR1 | LSBFIRST | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_LSBFIRST_Msk |
| CR1 | SSI | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_SSI_Msk |
| CR1 | SSM | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_SSM_Msk |
| CR1 | RXONLY | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_RXONLY_Msk |
| CR1 | CRCL | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CRCL_Msk |
| CR1 | CRCNEXT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CRCNEXT_Msk |
| CR1 | CRCEN | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CRCEN_Msk |
| CR1 | BIDIOE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_BIDIOE_Msk |
| CR1 | BIDIMODE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_BIDIMODE_Msk |
| CR2 | RXDMAEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_RXDMAEN_Msk |
| CR2 | TXDMAEN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_TXDMAEN_Msk |
| CR2 | SSOE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_SSOE_Msk |
| CR2 | NSSP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_NSSP_Msk |
| CR2 | FRF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_FRF_Msk |
| CR2 | ERRIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_ERRIE_Msk |
| CR2 | RXNEIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_RXNEIE_Msk |
| CR2 | TXEIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_TXEIE_Msk |
| CR2 | DS | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_DS_Msk |
| CR2 | FRXTH | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_FRXTH_Msk |
| CR2 | LDMARX | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_LDMARX_Msk |
| CR2 | LDMATX | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_LDMATX_Msk |
| SR | RXNE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_RXNE_Msk |
| SR | TXE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TXE_Msk |
| SR | CHSIDE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_CHSIDE_Msk |
| SR | UDR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_UDR_Msk |
| SR | CRCERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_CRCERR_Msk |
| SR | MODF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_MODF_Msk |
| SR | OVR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_OVR_Msk |
| SR | BSY | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_BSY_Msk |
| SR | FRE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_FRE_Msk |
| SR | FRLVL | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_FRLVL_Msk |
| SR | FTLVL | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_FTLVL_Msk |
| DR | DR | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_DR_DR_Msk |
| CRCPR | CRCPOLY | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_CRCPR_CRCPOLY_Msk |
| RXCRCR | RXCRC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_RXCRCR_RXCRC_Msk |
| TXCRCR | TXCRC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_TXCRCR_TXCRC_Msk |
| I2SCFGR | CHLEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CHLEN_Msk |
| I2SCFGR | DATLEN | 2:1 | 0x6 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_DATLEN_Msk |
| I2SCFGR | CKPOL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CKPOL_Msk |
| I2SCFGR | I2SSTD | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SSTD_Msk |
| I2SCFGR | PCMSYNC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_PCMSYNC_Msk |
| I2SCFGR | I2SCFG | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SCFG_Msk |
| I2SCFGR | I2SE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SE_Msk |
| I2SCFGR | I2SMOD | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SMOD_Msk |
| I2SCFGR | ASTRTEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_ASTRTEN_Msk |
| I2SPR | I2SDIV | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_I2SDIV_Msk |
| I2SPR | ODD | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_ODD_Msk |
| I2SPR | MCKOE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_MCKOE_Msk |

## Operating semantics unavailable

**spi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
