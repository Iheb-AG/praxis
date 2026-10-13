# STM32F407 SPI — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]], [[peripherals/gpio]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| I2S2ext | 0x40003400 | Instance-specific APB1/APB2; I2S extension applicability not reviewed | SPI1: RCC_APB2ENR.SPI1EN; SPI2/3: RCC_APB1ENR.SPI2EN/SPI3EN; extension clocks not asserted | header:I2S2ext_BASE; rm_features_248:page:248; rm_features_250:page:250 |
| I2S3ext | 0x40004000 | Instance-specific APB1/APB2; I2S extension applicability not reviewed | SPI1: RCC_APB2ENR.SPI1EN; SPI2/3: RCC_APB1ENR.SPI2EN/SPI3EN; extension clocks not asserted | header:I2S3ext_BASE; rm_features_248:page:248; rm_features_250:page:250 |
| SPI1 | 0x40013000 | Instance-specific APB1/APB2; I2S extension applicability not reviewed | SPI1: RCC_APB2ENR.SPI1EN; SPI2/3: RCC_APB1ENR.SPI2EN/SPI3EN; extension clocks not asserted | header:SPI1_BASE; rm_features_248:page:248; rm_features_250:page:250 |
| SPI2 | 0x40003800 | Instance-specific APB1/APB2; I2S extension applicability not reviewed | SPI1: RCC_APB2ENR.SPI1EN; SPI2/3: RCC_APB1ENR.SPI2EN/SPI3EN; extension clocks not asserted | header:SPI2_BASE; rm_features_248:page:248; rm_features_250:page:250 |
| SPI3 | 0x40003C00 | Instance-specific APB1/APB2; I2S extension applicability not reviewed | SPI1: RCC_APB2ENR.SPI1EN; SPI2/3: RCC_APB1ENR.SPI2EN/SPI3EN; extension clocks not asserted | header:SPI3_BASE; rm_features_248:page:248; rm_features_250:page:250 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | RW | 0x0 | Set DFF/CRCEN while disabled. Master/NSS policy must be coherent; MODF can clear SPE and MSTR. | header:SPI_TypeDef.CR1; header:SPI_TypeDef.CR1; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 | 16, 32 |
| CR2 | 0x004 | 32 | — | RW | 0x0 | RX/TX DMA request and interrupt enables; the reviewed mode keeps them disabled. | header:SPI_TypeDef.CR2; header:SPI_TypeDef.CR2; rm_features_913:page:913; rm_features_914:page:914 | 16, 32 |
| SR | 0x008 | 32 | — | mixed | 0x2 | OVR: read DR then SR. MODF: access SR then write CR1, with NSS safe before restore. CRCERR clears by writing 0. FRE clears on reading SR; status reads have side effects. | header:SPI_TypeDef.SR; header:SPI_TypeDef.SR; rm_features_914:page:914; rm_features_915:page:915; rm_features_891:page:891; rm_features_892:page:892 | 16, 32 |
| DR | 0x00C | 32 | — | RW | 0x0 | Writes fill TX buffer; reads drain RX buffer. Read every received frame to avoid overrun. | header:SPI_TypeDef.DR; header:SPI_TypeDef.DR; rm_features_915:page:915 | 16, 32 |
| CRCPR | 0x010 | 32 | — | RW | 0x7 | CRC polynomial configuration; the reviewed SPI polling mode leaves hardware CRC disabled. | header:SPI_TypeDef.CRCPR; header:SPI_TypeDef.CRCPR; rm_features_916:page:916 | 16, 32 |
| RXCRCR | 0x014 | 32 | — | RO | 0x0 | Receive CRC result; reset when CRCEN is enabled. CRC transfer procedure is outside this mode. | header:SPI_TypeDef.RXCRCR; header:SPI_TypeDef.RXCRCR; rm_features_916:page:916 | 16, 32 |
| TXCRCR | 0x018 | 32 | — | RO | 0x0 | Transmit CRC result; reset when CRCEN is enabled. CRC transfer procedure is outside this mode. | header:SPI_TypeDef.TXCRCR; header:SPI_TypeDef.TXCRCR; rm_features_916:page:916; rm_features_917:page:917 | 16, 32 |
| I2SCFGR | 0x01C | 32 | — | RW | 0x0 | Configure mode only while SPI/I2S disabled; I2SMOD=0 selects SPI. I2S operation is not qualified. | header:SPI_TypeDef.I2SCFGR; header:SPI_TypeDef.I2SCFGR; rm_features_917:page:917; rm_features_918:page:918 | 16, 32 |
| I2SPR | 0x020 | 32 | — | RW | 0x2 | I2S prescaler configuration while disabled; no I2S clock/board route is qualified. | header:SPI_TypeDef.I2SPR; header:SPI_TypeDef.I2SPR; rm_features_918:page:918; rm_features_919:page:919 | 16, 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | CPHA | 0:0 | 0x1 | 0 first clock transition, 1 second clock transition. | header:SPI_CR1_CPHA_Msk; header:SPI_CR1_CPHA_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | CPOL | 1:1 | 0x2 | 0 clock idle low, 1 idle high. | header:SPI_CR1_CPOL_Msk; header:SPI_CR1_CPOL_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | MSTR | 2:2 | 0x4 | 1 master, 0 slave; set while SPI is disabled. | header:SPI_CR1_MSTR_Msk; header:SPI_CR1_MSTR_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | BR | 5:3 | 0x38 | Baud-rate divider code 0..7 selects peripheral clock /2,/4,/8,/16,/32,/64,/128,/256. | header:SPI_CR1_BR_Msk; header:SPI_CR1_BR_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | SPE | 6:6 | 0x40 | SPI peripheral enable. | header:SPI_CR1_SPE_Msk; header:SPI_CR1_SPE_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | LSBFIRST | 7:7 | 0x80 | 0 MSB first, 1 LSB first; configure before transfer. | header:SPI_CR1_LSBFIRST_Msk; header:SPI_CR1_LSBFIRST_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | SSI | 8:8 | 0x100 | Internal NSS level when SSM=1; keep high for the supported software-NSS master mode. | header:SPI_CR1_SSI_Msk; header:SPI_CR1_SSI_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | SSM | 9:9 | 0x200 | 1 enables software NSS management. | header:SPI_CR1_SSM_Msk; header:SPI_CR1_SSM_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | RXONLY | 10:10 | 0x400 | 0 selects full-duplex with BIDIMODE=0. | header:SPI_CR1_RXONLY_Msk; header:SPI_CR1_RXONLY_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | DFF | 11:11 | 0x800 | 0 eight-bit, 1 sixteen-bit frames; configure only with SPE=0. | header:SPI_CR1_DFF_Msk; header:SPI_CR1_DFF_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | CRCNEXT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_CRCNEXT_Msk; header:SPI_CR1_CRCNEXT_Msk |
| CR1 | CRCEN | 13:13 | 0x2000 | CRC enable; change only when disabled. The reviewed polling mode sets this to zero. | header:SPI_CR1_CRCEN_Msk; header:SPI_CR1_CRCEN_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR1 | BIDIOE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR1_BIDIOE_Msk; header:SPI_CR1_BIDIOE_Msk |
| CR1 | BIDIMODE | 15:15 | 0x8000 | 0 two-line unidirectional data mode (full duplex when RXONLY=0). | header:SPI_CR1_BIDIMODE_Msk; header:SPI_CR1_BIDIMODE_Msk; rm_features_877:page:877; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913 |
| CR2 | RXDMAEN | 0:0 | 0x1 | RX DMA request enable; zero in polling mode. | header:SPI_CR2_RXDMAEN_Msk; header:SPI_CR2_RXDMAEN_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| CR2 | TXDMAEN | 1:1 | 0x2 | TX DMA request enable; zero in polling mode. | header:SPI_CR2_TXDMAEN_Msk; header:SPI_CR2_TXDMAEN_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| CR2 | SSOE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_CR2_SSOE_Msk; header:SPI_CR2_SSOE_Msk |
| CR2 | FRF | 4:4 | 0x10 | 0 Motorola SPI frame format; 1 TI frame format. | header:SPI_CR2_FRF_Msk; header:SPI_CR2_FRF_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| CR2 | ERRIE | 5:5 | 0x20 | Error interrupt enable; zero in polling mode. | header:SPI_CR2_ERRIE_Msk; header:SPI_CR2_ERRIE_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| CR2 | RXNEIE | 6:6 | 0x40 | RXNE interrupt enable; zero in polling mode. | header:SPI_CR2_RXNEIE_Msk; header:SPI_CR2_RXNEIE_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| CR2 | TXEIE | 7:7 | 0x80 | TXE interrupt enable; zero in polling mode. | header:SPI_CR2_TXEIE_Msk; header:SPI_CR2_TXEIE_Msk; rm_features_913:page:913; rm_features_914:page:914 |
| SR | RXNE | 0:0 | 0x1 | Receive buffer not empty; read DR when set. | header:SPI_SR_RXNE_Msk; header:SPI_SR_RXNE_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | TXE | 1:1 | 0x2 | Transmit buffer empty; write DR when set. | header:SPI_SR_TXE_Msk; header:SPI_SR_TXE_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | CHSIDE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_CHSIDE_Msk; header:SPI_SR_CHSIDE_Msk |
| SR | UDR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_SR_UDR_Msk; header:SPI_SR_UDR_Msk |
| SR | CRCERR | 4:4 | 0x10 | CRC mismatch; clear by writing zero. | header:SPI_SR_CRCERR_Msk; header:SPI_SR_CRCERR_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | MODF | 5:5 | 0x20 | Mode fault; hardware clears SPE/MSTR; clear via SR access then CR1 write. | header:SPI_SR_MODF_Msk; header:SPI_SR_MODF_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | OVR | 6:6 | 0x40 | Overrun: clear by DR read followed by SR read. | header:SPI_SR_OVR_Msk; header:SPI_SR_OVR_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | BSY | 7:7 | 0x80 | Busy status; require zero before disabling after full-duplex completion. | header:SPI_SR_BSY_Msk; header:SPI_SR_BSY_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| SR | FRE | 8:8 | 0x100 | Frame-format error; reading SR clears it. | header:SPI_SR_FRE_Msk; header:SPI_SR_FRE_Msk; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_914:page:914; rm_features_915:page:915 |
| DR | DR | 15:0 | 0xFFFF | Low eight/sixteen bits selected by DFF; TX on write, RX on read. | header:SPI_DR_DR_Msk; header:SPI_DR_DR_Msk; rm_features_915:page:915 |
| CRCPR | CRCPOLY | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_CRCPR_CRCPOLY_Msk; header:SPI_CRCPR_CRCPOLY_Msk |
| RXCRCR | RXCRC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_RXCRCR_RXCRC_Msk; header:SPI_RXCRCR_RXCRC_Msk |
| TXCRCR | TXCRC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SPI_TXCRCR_TXCRC_Msk; header:SPI_TXCRCR_TXCRC_Msk |
| I2SCFGR | CHLEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CHLEN_Msk; header:SPI_I2SCFGR_CHLEN_Msk |
| I2SCFGR | DATLEN | 2:1 | 0x6 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_DATLEN_Msk; header:SPI_I2SCFGR_DATLEN_Msk |
| I2SCFGR | CKPOL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_CKPOL_Msk; header:SPI_I2SCFGR_CKPOL_Msk |
| I2SCFGR | I2SSTD | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SSTD_Msk; header:SPI_I2SCFGR_I2SSTD_Msk |
| I2SCFGR | PCMSYNC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_PCMSYNC_Msk; header:SPI_I2SCFGR_PCMSYNC_Msk |
| I2SCFGR | I2SCFG | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SCFG_Msk; header:SPI_I2SCFGR_I2SCFG_Msk |
| I2SCFGR | I2SE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SCFGR_I2SE_Msk; header:SPI_I2SCFGR_I2SE_Msk |
| I2SCFGR | I2SMOD | 11:11 | 0x800 | 0 selects SPI; 1 I2S. Configure while disabled. | header:SPI_I2SCFGR_I2SMOD_Msk; header:SPI_I2SCFGR_I2SMOD_Msk; rm_features_917:page:917 |
| I2SPR | I2SDIV | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_I2SDIV_Msk; header:SPI_I2SPR_I2SDIV_Msk |
| I2SPR | ODD | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_ODD_Msk; header:SPI_I2SPR_ODD_Msk |
| I2SPR | MCKOE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SPI_I2SPR_MCKOE_Msk; header:SPI_I2SPR_MCKOE_Msk |

## Reviewed operating semantics

This review establishes controller semantics for SPI1/SPI2/SPI3 master full-duplex polling. The I2S extension instances share a C layout but are excluded from this SPI mode. SPI CRC, TI framing, slave operation, I2S audio and DMA/interrupt transfers need their own reviewed contracts.

Select CPOL/CPHA and bit order from the peer, compute BR from the actual instance peripheral clock, configure with SPE=0 and select I2SMOD=0. Software NSS uses SSM=SSI=1; peer chip select requires separately supported GPIO connectivity. Use Motorola FRF=0 and read every received frame. Finish RX, then wait TXE=1 and BSY=0 before clearing SPE.

SR reads can clear FRE. OVR clears by DR read then SR read. MODF requires SR access then CR1 write and a safe NSS level before restoration. All waits are bounded.

**Board readiness is blocked:** no SPI1_SCK/MOSI/MISO mapping is asserted in the current schematic subset. Never fall back to a remembered evaluation-board pinout. Resolve [[schemas/custom_pcb_netlist]] and reviewed AF availability before generating wired firmware. Prerequisites: [[peripherals/rcc]], [[peripherals/gpio]]. See [[features]] and [[coverage]].

Evidence: rm_features_877:page:877, rm_features_880:page:880, rm_features_881:page:881, rm_features_882:page:882, rm_features_883:page:883, rm_features_887:page:887, rm_features_888:page:888, rm_features_889:page:889, rm_features_891:page:891, rm_features_892:page:892, rm_features_911:page:911, rm_features_912:page:912, rm_features_913:page:913, rm_features_914:page:914, rm_features_915:page:915, rm_features_917:page:917. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| master_full_duplex_polling | SPI1, SPI2, SPI3 | CR1, CR2, SR, DR, I2SCFGR | CR1: CPHA, CPOL, MSTR, BR, SPE, LSBFIRST, SSM, SSI, DFF, RXONLY, BIDIMODE, CRCEN; CR2: FRF, RXDMAEN, TXDMAEN, RXNEIE, TXEIE, ERRIE; DR: DR; I2SCFGR: I2SMOD; SR: RXNE, TXE, BSY, OVR, MODF, FRE | Requires separately reviewed package AF mapping, board pins, electrical levels and peer timing; this mode establishes controller semantics only.<br>Enable the instance APB clock, select SPI mode and configure pins from actual board evidence.<br>With SPE=0 select master, full-duplex, Motorola format, frame width, peer CPOL/CPHA and peripheral-clock baud divider.<br>Set SSM=SSI=1 for software NSS; manage any peer chip select through a separately validated output.<br>Enable SPE after configuration; bound TXE/RXNE waits and drain RX on every transmitted frame.<br>Check error flags and follow the documented clearing sequences.<br>For full-duplex shutdown finish RXNE/read, wait TXE=1 then BSY=0, then clear SPE. | rm_features_877:page:877; rm_features_880:page:880; rm_features_881:page:881; rm_features_882:page:882; rm_features_883:page:883; rm_features_887:page:887; rm_features_888:page:888; rm_features_889:page:889; rm_features_891:page:891; rm_features_892:page:892; rm_features_911:page:911; rm_features_912:page:912; rm_features_913:page:913; rm_features_914:page:914; rm_features_915:page:915; rm_features_917:page:917 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
