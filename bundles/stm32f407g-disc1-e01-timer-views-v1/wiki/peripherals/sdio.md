# SDIO — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SDIO | 0x40012C00 | Not asserted | Not asserted | header:SDIO_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POWER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.POWER |
| CLKCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.CLKCR |
| ARG | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.ARG |
| CMD | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.CMD |
| RESPCMD | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.RESPCMD |
| RESP1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.RESP1 |
| RESP2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.RESP2 |
| RESP3 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.RESP3 |
| RESP4 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.RESP4 |
| DTIMER | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.DTIMER |
| DLEN | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.DLEN |
| DCTRL | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.DCTRL |
| DCOUNT | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.DCOUNT |
| STA | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.STA |
| ICR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.ICR |
| MASK | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.MASK |
| FIFOCNT | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.FIFOCNT |
| FIFO | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDIO_TypeDef.FIFO |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| POWER | PWRCTRL | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SDIO_POWER_PWRCTRL_Msk |
| CLKCR | CLKDIV | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_CLKDIV_Msk |
| CLKCR | CLKEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_CLKEN_Msk |
| CLKCR | PWRSAV | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_PWRSAV_Msk |
| CLKCR | BYPASS | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_BYPASS_Msk |
| CLKCR | WIDBUS | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_WIDBUS_Msk |
| CLKCR | NEGEDGE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_NEGEDGE_Msk |
| CLKCR | HWFC_EN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CLKCR_HWFC_EN_Msk |
| ARG | CMDARG | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_ARG_CMDARG_Msk |
| CMD | CMDINDEX | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_CMDINDEX_Msk |
| CMD | WAITRESP | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_WAITRESP_Msk |
| CMD | WAITINT | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_WAITINT_Msk |
| CMD | WAITPEND | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_WAITPEND_Msk |
| CMD | CPSMEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_CPSMEN_Msk |
| CMD | SDIOSUSPEND | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_SDIOSUSPEND_Msk |
| CMD | ENCMDCOMPL | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_ENCMDCOMPL_Msk |
| CMD | NIEN | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_NIEN_Msk |
| CMD | CEATACMD | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_CMD_CEATACMD_Msk |
| RESPCMD | RESPCMD | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:SDIO_RESPCMD_RESPCMD_Msk |
| RESP1 | CARDSTATUS1 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_RESP1_CARDSTATUS1_Msk |
| RESP2 | CARDSTATUS2 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_RESP2_CARDSTATUS2_Msk |
| RESP3 | CARDSTATUS3 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_RESP3_CARDSTATUS3_Msk |
| RESP4 | CARDSTATUS4 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_RESP4_CARDSTATUS4_Msk |
| DTIMER | DATATIME | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_DTIMER_DATATIME_Msk |
| DLEN | DATALENGTH | 24:0 | 0x1FFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_DLEN_DATALENGTH_Msk |
| DCTRL | DTEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_DTEN_Msk |
| DCTRL | DTDIR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_DTDIR_Msk |
| DCTRL | DTMODE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_DTMODE_Msk |
| DCTRL | DMAEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_DMAEN_Msk |
| DCTRL | DBLOCKSIZE | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_DBLOCKSIZE_Msk |
| DCTRL | RWSTART | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_RWSTART_Msk |
| DCTRL | RWSTOP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_RWSTOP_Msk |
| DCTRL | RWMOD | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_RWMOD_Msk |
| DCTRL | SDIOEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCTRL_SDIOEN_Msk |
| DCOUNT | DATACOUNT | 24:0 | 0x1FFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_DCOUNT_DATACOUNT_Msk |
| STA | CCRCFAIL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CCRCFAIL_Msk |
| STA | DCRCFAIL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_DCRCFAIL_Msk |
| STA | CTIMEOUT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CTIMEOUT_Msk |
| STA | DTIMEOUT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_DTIMEOUT_Msk |
| STA | TXUNDERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXUNDERR_Msk |
| STA | RXOVERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXOVERR_Msk |
| STA | CMDREND | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CMDREND_Msk |
| STA | CMDSENT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CMDSENT_Msk |
| STA | DATAEND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_DATAEND_Msk |
| STA | STBITERR | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_STBITERR_Msk |
| STA | DBCKEND | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_DBCKEND_Msk |
| STA | CMDACT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CMDACT_Msk |
| STA | TXACT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXACT_Msk |
| STA | RXACT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXACT_Msk |
| STA | TXFIFOHE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXFIFOHE_Msk |
| STA | RXFIFOHF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXFIFOHF_Msk |
| STA | TXFIFOF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXFIFOF_Msk |
| STA | RXFIFOF | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXFIFOF_Msk |
| STA | TXFIFOE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXFIFOE_Msk |
| STA | RXFIFOE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXFIFOE_Msk |
| STA | TXDAVL | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_TXDAVL_Msk |
| STA | RXDAVL | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_RXDAVL_Msk |
| STA | SDIOIT | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_SDIOIT_Msk |
| STA | CEATAEND | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_STA_CEATAEND_Msk |
| ICR | CCRCFAILC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_CCRCFAILC_Msk |
| ICR | DCRCFAILC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_DCRCFAILC_Msk |
| ICR | CTIMEOUTC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_CTIMEOUTC_Msk |
| ICR | DTIMEOUTC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_DTIMEOUTC_Msk |
| ICR | TXUNDERRC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_TXUNDERRC_Msk |
| ICR | RXOVERRC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_RXOVERRC_Msk |
| ICR | CMDRENDC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_CMDRENDC_Msk |
| ICR | CMDSENTC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_CMDSENTC_Msk |
| ICR | DATAENDC | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_DATAENDC_Msk |
| ICR | STBITERRC | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_STBITERRC_Msk |
| ICR | DBCKENDC | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_DBCKENDC_Msk |
| ICR | SDIOITC | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_SDIOITC_Msk |
| ICR | CEATAENDC | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_ICR_CEATAENDC_Msk |
| MASK | CCRCFAILIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CCRCFAILIE_Msk |
| MASK | DCRCFAILIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_DCRCFAILIE_Msk |
| MASK | CTIMEOUTIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CTIMEOUTIE_Msk |
| MASK | DTIMEOUTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_DTIMEOUTIE_Msk |
| MASK | TXUNDERRIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXUNDERRIE_Msk |
| MASK | RXOVERRIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXOVERRIE_Msk |
| MASK | CMDRENDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CMDRENDIE_Msk |
| MASK | CMDSENTIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CMDSENTIE_Msk |
| MASK | DATAENDIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_DATAENDIE_Msk |
| MASK | STBITERRIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_STBITERRIE_Msk |
| MASK | DBCKENDIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_DBCKENDIE_Msk |
| MASK | CMDACTIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CMDACTIE_Msk |
| MASK | TXACTIE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXACTIE_Msk |
| MASK | RXACTIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXACTIE_Msk |
| MASK | TXFIFOHEIE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXFIFOHEIE_Msk |
| MASK | RXFIFOHFIE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXFIFOHFIE_Msk |
| MASK | TXFIFOFIE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXFIFOFIE_Msk |
| MASK | RXFIFOFIE | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXFIFOFIE_Msk |
| MASK | TXFIFOEIE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXFIFOEIE_Msk |
| MASK | RXFIFOEIE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXFIFOEIE_Msk |
| MASK | TXDAVLIE | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_TXDAVLIE_Msk |
| MASK | RXDAVLIE | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_RXDAVLIE_Msk |
| MASK | SDIOITIE | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_SDIOITIE_Msk |
| MASK | CEATAENDIE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDIO_MASK_CEATAENDIE_Msk |
| FIFOCNT | FIFOCOUNT | 23:0 | 0xFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_FIFOCNT_FIFOCOUNT_Msk |
| FIFO | FIFODATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDIO_FIFO_FIFODATA_Msk |

## Operating semantics unavailable

**sdio: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
