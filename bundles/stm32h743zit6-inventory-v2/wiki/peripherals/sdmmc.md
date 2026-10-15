# SDMMC — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SDMMC1 | 0x52007000 | Not asserted | Not asserted | header:SDMMC1_BASE |
| SDMMC2 | 0x48022400 | Not asserted | Not asserted | header:SDMMC2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| POWER | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.POWER |
| CLKCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.CLKCR |
| ARG | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.ARG |
| CMD | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.CMD |
| RESPCMD | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.RESPCMD |
| RESP1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.RESP1 |
| RESP2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.RESP2 |
| RESP3 | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.RESP3 |
| RESP4 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.RESP4 |
| DTIMER | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.DTIMER |
| DLEN | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.DLEN |
| DCTRL | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.DCTRL |
| DCOUNT | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.DCOUNT |
| STA | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.STA |
| ICR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.ICR |
| MASK | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.MASK |
| ACKTIME | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.ACKTIME |
| IDMACTRL | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.IDMACTRL |
| IDMABSIZE | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.IDMABSIZE |
| IDMABASE0 | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.IDMABASE0 |
| IDMABASE1 | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.IDMABASE1 |
| FIFO | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.FIFO |
| IPVR | 0x3FC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SDMMC_TypeDef.IPVR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| POWER | PWRCTRL | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_POWER_PWRCTRL_Msk |
| POWER | VSWITCH | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_POWER_VSWITCH_Msk |
| POWER | VSWITCHEN | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_POWER_VSWITCHEN_Msk |
| POWER | DIRPOL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_POWER_DIRPOL_Msk |
| CLKCR | CLKDIV | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_CLKDIV_Msk |
| CLKCR | PWRSAV | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_PWRSAV_Msk |
| CLKCR | WIDBUS | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_WIDBUS_Msk |
| CLKCR | NEGEDGE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_NEGEDGE_Msk |
| CLKCR | HWFC_EN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_HWFC_EN_Msk |
| CLKCR | DDR | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_DDR_Msk |
| CLKCR | BUSSPEED | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_BUSSPEED_Msk |
| CLKCR | SELCLKRX | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CLKCR_SELCLKRX_Msk |
| ARG | CMDARG | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ARG_CMDARG_Msk |
| CMD | CMDINDEX | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_CMDINDEX_Msk |
| CMD | CMDTRANS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_CMDTRANS_Msk |
| CMD | CMDSTOP | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_CMDSTOP_Msk |
| CMD | WAITRESP | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_WAITRESP_Msk |
| CMD | WAITINT | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_WAITINT_Msk |
| CMD | WAITPEND | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_WAITPEND_Msk |
| CMD | CPSMEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_CPSMEN_Msk |
| CMD | DTHOLD | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_DTHOLD_Msk |
| CMD | BOOTMODE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_BOOTMODE_Msk |
| CMD | BOOTEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_BOOTEN_Msk |
| CMD | CMDSUSPEND | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_CMD_CMDSUSPEND_Msk |
| RESPCMD | RESPCMD | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:SDMMC_RESPCMD_RESPCMD_Msk |
| RESP1 | CARDSTATUS1 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_RESP1_CARDSTATUS1_Msk |
| RESP2 | CARDSTATUS2 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_RESP2_CARDSTATUS2_Msk |
| RESP3 | CARDSTATUS3 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_RESP3_CARDSTATUS3_Msk |
| RESP4 | CARDSTATUS4 | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_RESP4_CARDSTATUS4_Msk |
| DTIMER | DATATIME | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DTIMER_DATATIME_Msk |
| DLEN | DATALENGTH | 24:0 | 0x1FFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DLEN_DATALENGTH_Msk |
| DCTRL | DTEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_DTEN_Msk |
| DCTRL | DTDIR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_DTDIR_Msk |
| DCTRL | DTMODE | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_DTMODE_Msk |
| DCTRL | DBLOCKSIZE | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_DBLOCKSIZE_Msk |
| DCTRL | RWSTART | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_RWSTART_Msk |
| DCTRL | RWSTOP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_RWSTOP_Msk |
| DCTRL | RWMOD | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_RWMOD_Msk |
| DCTRL | SDIOEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_SDIOEN_Msk |
| DCTRL | BOOTACKEN | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_BOOTACKEN_Msk |
| DCTRL | FIFORST | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCTRL_FIFORST_Msk |
| DCOUNT | DATACOUNT | 24:0 | 0x1FFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_DCOUNT_DATACOUNT_Msk |
| STA | CCRCFAIL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CCRCFAIL_Msk |
| STA | DCRCFAIL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DCRCFAIL_Msk |
| STA | CTIMEOUT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CTIMEOUT_Msk |
| STA | DTIMEOUT | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DTIMEOUT_Msk |
| STA | TXUNDERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_TXUNDERR_Msk |
| STA | RXOVERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_RXOVERR_Msk |
| STA | CMDREND | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CMDREND_Msk |
| STA | CMDSENT | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CMDSENT_Msk |
| STA | DATAEND | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DATAEND_Msk |
| STA | DHOLD | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DHOLD_Msk |
| STA | DBCKEND | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DBCKEND_Msk |
| STA | DABORT | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DABORT_Msk |
| STA | DPSMACT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_DPSMACT_Msk |
| STA | CPSMACT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CPSMACT_Msk |
| STA | TXFIFOHE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_TXFIFOHE_Msk |
| STA | RXFIFOHF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_RXFIFOHF_Msk |
| STA | TXFIFOF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_TXFIFOF_Msk |
| STA | RXFIFOF | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_RXFIFOF_Msk |
| STA | TXFIFOE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_TXFIFOE_Msk |
| STA | RXFIFOE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_RXFIFOE_Msk |
| STA | BUSYD0 | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_BUSYD0_Msk |
| STA | BUSYD0END | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_BUSYD0END_Msk |
| STA | SDIOIT | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_SDIOIT_Msk |
| STA | ACKFAIL | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_ACKFAIL_Msk |
| STA | ACKTIMEOUT | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_ACKTIMEOUT_Msk |
| STA | VSWEND | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_VSWEND_Msk |
| STA | CKSTOP | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_CKSTOP_Msk |
| STA | IDMATE | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_IDMATE_Msk |
| STA | IDMABTC | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_STA_IDMABTC_Msk |
| ICR | CCRCFAILC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_CCRCFAILC_Msk |
| ICR | DCRCFAILC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DCRCFAILC_Msk |
| ICR | CTIMEOUTC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_CTIMEOUTC_Msk |
| ICR | DTIMEOUTC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DTIMEOUTC_Msk |
| ICR | TXUNDERRC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_TXUNDERRC_Msk |
| ICR | RXOVERRC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_RXOVERRC_Msk |
| ICR | CMDRENDC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_CMDRENDC_Msk |
| ICR | CMDSENTC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_CMDSENTC_Msk |
| ICR | DATAENDC | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DATAENDC_Msk |
| ICR | DHOLDC | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DHOLDC_Msk |
| ICR | DBCKENDC | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DBCKENDC_Msk |
| ICR | DABORTC | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_DABORTC_Msk |
| ICR | BUSYD0ENDC | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_BUSYD0ENDC_Msk |
| ICR | SDIOITC | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_SDIOITC_Msk |
| ICR | ACKFAILC | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_ACKFAILC_Msk |
| ICR | ACKTIMEOUTC | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_ACKTIMEOUTC_Msk |
| ICR | VSWENDC | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_VSWENDC_Msk |
| ICR | CKSTOPC | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_CKSTOPC_Msk |
| ICR | IDMATEC | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_IDMATEC_Msk |
| ICR | IDMABTCC | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ICR_IDMABTCC_Msk |
| MASK | CCRCFAILIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_CCRCFAILIE_Msk |
| MASK | DCRCFAILIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DCRCFAILIE_Msk |
| MASK | CTIMEOUTIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_CTIMEOUTIE_Msk |
| MASK | DTIMEOUTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DTIMEOUTIE_Msk |
| MASK | TXUNDERRIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_TXUNDERRIE_Msk |
| MASK | RXOVERRIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_RXOVERRIE_Msk |
| MASK | CMDRENDIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_CMDRENDIE_Msk |
| MASK | CMDSENTIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_CMDSENTIE_Msk |
| MASK | DATAENDIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DATAENDIE_Msk |
| MASK | DHOLDIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DHOLDIE_Msk |
| MASK | DBCKENDIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DBCKENDIE_Msk |
| MASK | DABORTIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_DABORTIE_Msk |
| MASK | TXFIFOHEIE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_TXFIFOHEIE_Msk |
| MASK | RXFIFOHFIE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_RXFIFOHFIE_Msk |
| MASK | RXFIFOFIE | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_RXFIFOFIE_Msk |
| MASK | TXFIFOEIE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_TXFIFOEIE_Msk |
| MASK | BUSYD0ENDIE | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_BUSYD0ENDIE_Msk |
| MASK | SDIOITIE | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_SDIOITIE_Msk |
| MASK | ACKFAILIE | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_ACKFAILIE_Msk |
| MASK | ACKTIMEOUTIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_ACKTIMEOUTIE_Msk |
| MASK | VSWENDIE | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_VSWENDIE_Msk |
| MASK | CKSTOPIE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_CKSTOPIE_Msk |
| MASK | IDMABTCIE | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_MASK_IDMABTCIE_Msk |
| ACKTIME | ACKTIME | 24:0 | 0x1FFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_ACKTIME_ACKTIME_Msk |
| IDMABSIZE | IDMABNDT | 12:5 | 0x1FE0 | Declaration only; encoding requires reviewed semantics. | header:SDMMC_IDMABSIZE_IDMABNDT_Msk |
| FIFO | FIFODATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:SDMMC_FIFO_FIFODATA_Msk |

## Operating semantics unavailable

**sdmmc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
