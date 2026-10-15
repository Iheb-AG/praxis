# SPI — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SPI1 | 0x40013000 | Not asserted | Not asserted | header:SPI1_BASE |
| SPI2 | 0x40003800 | Not asserted | Not asserted | header:SPI2_BASE |
| SPI3 | 0x40003C00 | Not asserted | Not asserted | header:SPI3_BASE |
| SPI4 | 0x40013400 | Not asserted | Not asserted | header:SPI4_BASE |
| SPI5 | 0x40015000 | Not asserted | Not asserted | header:SPI5_BASE |
| SPI6 | 0x58001400 | Not asserted | Not asserted | header:SPI6_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CR2 |
| CFG1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CFG1 |
| CFG2 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CFG2 |
| IER | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.IER |
| SR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.SR |
| IFCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.IFCR |
| TXDR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.TXDR |
| RXDR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.RXDR |
| CRCPOLY | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.CRCPOLY |
| TXCRC | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.TXCRC |
| RXCRC | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.RXCRC |
| UDRDR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.UDRDR |
| I2SCFGR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SPI_TypeDef.I2SCFGR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | SPE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_SPE_Msk |
| CR1 | MASRX | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_MASRX_Msk |
| CR1 | CSTART | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CSTART_Msk |
| CR1 | CSUSP | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CSUSP_Msk |
| CR1 | HDDIR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_HDDIR_Msk |
| CR1 | SSI | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_SSI_Msk |
| CR1 | CRC33_17 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CRC33_17_Msk |
| CR1 | RCRCINI | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_RCRCINI_Msk |
| CR1 | TCRCINI | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_TCRCINI_Msk |
| CR1 | IOLOCK | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_IOLOCK_Msk |
| CR2 | TSIZE | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_TSIZE_Msk |
| CR2 | TSER | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_TSER_Msk |
| CFG1 | DSIZE | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_DSIZE_Msk |
| CFG1 | FTHLV | 8:5 | 0x1E0 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_FTHLV_Msk |
| CFG1 | UDRCFG | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_UDRCFG_Msk |
| CFG1 | UDRDET | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_UDRDET_Msk |
| CFG1 | RXDMAEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_RXDMAEN_Msk |
| CFG1 | TXDMAEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_TXDMAEN_Msk |
| CFG1 | CRCSIZE | 20:16 | 0x1F0000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_CRCSIZE_Msk |
| CFG1 | CRCEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_CRCEN_Msk |
| CFG1 | MBR | 30:28 | 0x70000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG1_MBR_Msk |
| CFG2 | MSSI | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_MSSI_Msk |
| CFG2 | MIDI | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_MIDI_Msk |
| CFG2 | IOSWP | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_IOSWP_Msk |
| CFG2 | COMM | 18:17 | 0x60000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_COMM_Msk |
| CFG2 | SP | 21:19 | 0x380000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_SP_Msk |
| CFG2 | MASTER | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_MASTER_Msk |
| CFG2 | LSBFRST | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_LSBFRST_Msk |
| CFG2 | CPHA | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_CPHA_Msk |
| CFG2 | CPOL | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_CPOL_Msk |
| CFG2 | SSM | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_SSM_Msk |
| CFG2 | SSIOP | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_SSIOP_Msk |
| CFG2 | SSOE | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_SSOE_Msk |
| CFG2 | SSOM | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_SSOM_Msk |
| CFG2 | AFCNTR | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CFG2_AFCNTR_Msk |
| IER | RXPIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_RXPIE_Msk |
| IER | TXPIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_TXPIE_Msk |
| IER | DXPIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_DXPIE_Msk |
| IER | EOTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_EOTIE_Msk |
| IER | TXTFIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_TXTFIE_Msk |
| IER | UDRIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_UDRIE_Msk |
| IER | OVRIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_OVRIE_Msk |
| IER | CRCEIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_CRCEIE_Msk |
| IER | TIFREIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_TIFREIE_Msk |
| IER | MODFIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_MODFIE_Msk |
| IER | TSERFIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_IER_TSERFIE_Msk |
| SR | RXP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_RXP_Msk |
| SR | TXP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TXP_Msk |
| SR | DXP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_DXP_Msk |
| SR | EOT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_EOT_Msk |
| SR | TXTF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TXTF_Msk |
| SR | UDR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_UDR_Msk |
| SR | OVR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_OVR_Msk |
| SR | CRCE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_CRCE_Msk |
| SR | TIFRE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TIFRE_Msk |
| SR | MODF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_MODF_Msk |
| SR | TSERF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TSERF_Msk |
| SR | SUSP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_SUSP_Msk |
| SR | TXC | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_TXC_Msk |
| SR | RXPLVL | 14:13 | 0x6000 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_RXPLVL_Msk |
| SR | RXWNE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_RXWNE_Msk |
| SR | CTSIZE | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_CTSIZE_Msk |
| IFCR | EOTC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_EOTC_Msk |
| IFCR | TXTFC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_TXTFC_Msk |
| IFCR | UDRC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_UDRC_Msk |
| IFCR | OVRC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_OVRC_Msk |
| IFCR | CRCEC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_CRCEC_Msk |
| IFCR | TIFREC | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_TIFREC_Msk |
| IFCR | MODFC | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_MODFC_Msk |
| IFCR | TSERFC | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_TSERFC_Msk |
| IFCR | SUSPC | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_IFCR_SUSPC_Msk |
| TXDR | TXDR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_TXDR_TXDR_Msk |
| RXDR | RXDR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_RXDR_RXDR_Msk |
| CRCPOLY | CRCPOLY | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_CRCPOLY_CRCPOLY_Msk |
| TXCRC | TXCRC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_TXCRC_TXCRC_Msk |
| RXCRC | RXCRC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_RXCRC_RXCRC_Msk |
| UDRDR | UDRDR | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_UDRDR_UDRDR_Msk |
| I2SCFGR | I2SMOD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SMOD_Msk |
| I2SCFGR | I2SCFG | 3:1 | 0xE | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SCFG_Msk |
| I2SCFGR | I2SSTD | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SSTD_Msk |
| I2SCFGR | PCMSYNC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_PCMSYNC_Msk |
| I2SCFGR | DATLEN | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_DATLEN_Msk |
| I2SCFGR | CHLEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CHLEN_Msk |
| I2SCFGR | CKPOL | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CKPOL_Msk |
| I2SCFGR | FIXCH | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_FIXCH_Msk |
| I2SCFGR | WSINV | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_WSINV_Msk |
| I2SCFGR | DATFMT | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_DATFMT_Msk |
| I2SCFGR | I2SDIV | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SDIV_Msk |
| I2SCFGR | ODD | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_ODD_Msk |
| I2SCFGR | MCKOE | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_MCKOE_Msk |

## Operating semantics unavailable

**spi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
