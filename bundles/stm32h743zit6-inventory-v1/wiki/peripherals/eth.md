# ETH — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ETH | 0x40028000 | Not asserted | Not asserted | header:ETH_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MACCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACCR |
| MACECR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACECR |
| MACPFR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPFR |
| MACWTR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACWTR |
| MACHT0R | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHT0R |
| MACHT1R | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHT1R |
| MACVTR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACVTR |
| MACVHTR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACVHTR |
| MACVIR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACVIR |
| MACIVIR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACIVIR |
| MACTFCR | 0x070 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTFCR |
| MACRFCR | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACRFCR |
| MACISR | 0x0B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACISR |
| MACIER | 0x0B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACIER |
| MACRXTXSR | 0x0B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACRXTXSR |
| MACPCSR | 0x0C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPCSR |
| MACRWKPFR | 0x0C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACRWKPFR |
| MACLCSR | 0x0D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACLCSR |
| MACLTCR | 0x0D4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACLTCR |
| MACLETR | 0x0D8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACLETR |
| MAC1USTCR | 0x0DC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MAC1USTCR |
| MACVR | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACVR |
| MACDR | 0x114 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACDR |
| MACHWF0R | 0x11C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHWF0R |
| MACHWF1R | 0x120 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHWF1R |
| MACHWF2R | 0x124 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHWF2R |
| MACMDIOAR | 0x200 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACMDIOAR |
| MACMDIODR | 0x204 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACMDIODR |
| MACARPAR | 0x210 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACARPAR |
| MACA0HR | 0x300 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA0HR |
| MACA0LR | 0x304 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA0LR |
| MACA1HR | 0x308 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA1HR |
| MACA1LR | 0x30C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA1LR |
| MACA2HR | 0x310 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA2HR |
| MACA2LR | 0x314 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA2LR |
| MACA3HR | 0x318 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA3HR |
| MACA3LR | 0x31C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA3LR |
| MMCCR | 0x700 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCCR |
| MMCRIR | 0x704 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRIR |
| MMCTIR | 0x708 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTIR |
| MMCRIMR | 0x70C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRIMR |
| MMCTIMR | 0x710 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTIMR |
| MMCTSCGPR | 0x74C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTSCGPR |
| MMCTMCGPR | 0x750 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTMCGPR |
| MMCTPCGR | 0x768 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTPCGR |
| MMCRCRCEPR | 0x794 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRCRCEPR |
| MMCRAEPR | 0x798 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRAEPR |
| MMCRUPGR | 0x7C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRUPGR |
| MMCTLPIMSTR | 0x7EC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTLPIMSTR |
| MMCTLPITCR | 0x7F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTLPITCR |
| MMCRLPIMSTR | 0x7F4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRLPIMSTR |
| MMCRLPITCR | 0x7F8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRLPITCR |
| MACL3L4C0R | 0x900 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3L4C0R |
| MACL4A0R | 0x904 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL4A0R |
| MACL3A0R0R | 0x910 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A0R0R |
| MACL3A1R0R | 0x914 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A1R0R |
| MACL3A2R0R | 0x918 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A2R0R |
| MACL3A3R0R | 0x91C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A3R0R |
| MACL3L4C1R | 0x930 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3L4C1R |
| MACL4A1R | 0x934 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL4A1R |
| MACL3A0R1R | 0x940 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A0R1R |
| MACL3A1R1R | 0x944 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A1R1R |
| MACL3A2R1R | 0x948 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A2R1R |
| MACL3A3R1R | 0x94C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACL3A3R1R |
| MACTSCR | 0xB00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSCR |
| MACSSIR | 0xB04 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSSIR |
| MACSTSR | 0xB08 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSTSR |
| MACSTNR | 0xB0C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSTNR |
| MACSTSUR | 0xB10 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSTSUR |
| MACSTNUR | 0xB14 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSTNUR |
| MACTSAR | 0xB18 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSAR |
| MACTSSR | 0xB20 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSSR |
| MACTTSSNR | 0xB30 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTTSSNR |
| MACTTSSSR | 0xB34 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTTSSSR |
| MACACR | 0xB40 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACACR |
| MACATSNR | 0xB48 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACATSNR |
| MACATSSR | 0xB4C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACATSSR |
| MACTSIACR | 0xB50 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSIACR |
| MACTSEACR | 0xB54 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSEACR |
| MACTSICNR | 0xB58 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSICNR |
| MACTSECNR | 0xB5C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACTSECNR |
| MACPPSCR | 0xB70 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPPSCR |
| MACPPSTTSR | 0xB80 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPPSTTSR |
| MACPPSTTNR | 0xB84 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPPSTTNR |
| MACPPSIR | 0xB88 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPPSIR |
| MACPPSWR | 0xB8C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPPSWR |
| MACPOCR | 0xBC0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPOCR |
| MACSPI0R | 0xBC4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSPI0R |
| MACSPI1R | 0xBC8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSPI1R |
| MACSPI2R | 0xBCC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSPI2R |
| MACLMIR | 0xBD0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACLMIR |
| MTLOMR | 0xC00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLOMR |
| MTLISR | 0xC20 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLISR |
| MTLTQOMR | 0xD00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLTQOMR |
| MTLTQUR | 0xD04 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLTQUR |
| MTLTQDR | 0xD08 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLTQDR |
| MTLQICSR | 0xD2C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLQICSR |
| MTLRQOMR | 0xD30 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLRQOMR |
| MTLRQMPOCR | 0xD34 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLRQMPOCR |
| MTLRQDR | 0xD38 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MTLRQDR |
| DMAMR | 0x1000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMAMR |
| DMASBMR | 0x1004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMASBMR |
| DMAISR | 0x1008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMAISR |
| DMADSR | 0x100C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMADSR |
| DMACCR | 0x1100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACCR |
| DMACTCR | 0x1104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACTCR |
| DMACRCR | 0x1108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACRCR |
| DMACTDLAR | 0x1114 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACTDLAR |
| DMACRDLAR | 0x111C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACRDLAR |
| DMACTDTPR | 0x1120 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACTDTPR |
| DMACRDTPR | 0x1128 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACRDTPR |
| DMACTDRLR | 0x112C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACTDRLR |
| DMACRDRLR | 0x1130 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACRDRLR |
| DMACIER | 0x1134 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACIER |
| DMACRIWTR | 0x1138 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACRIWTR |
| DMACSFCSR | 0x113C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACSFCSR |
| DMACCATDR | 0x1144 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACCATDR |
| DMACCARDR | 0x114C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACCARDR |
| DMACCATBR | 0x1154 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACCATBR |
| DMACCARBR | 0x115C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACCARBR |
| DMACSR | 0x1160 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACSR |
| DMACMFCR | 0x116C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACMFCR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MACCR | RE | 0:0 | 0x1 | meaning_001 | header:ETH_MACCR_RE_Msk |
| MACCR | TE | 1:1 | 0x2 | meaning_001 | header:ETH_MACCR_TE_Msk |
| MACCR | PRELEN | 3:2 | 0xC | meaning_001 | header:ETH_MACCR_PRELEN_Msk |
| MACCR | DC | 4:4 | 0x10 | meaning_001 | header:ETH_MACCR_DC_Msk |
| MACCR | BL | 6:5 | 0x60 | meaning_001 | header:ETH_MACCR_BL_Msk |
| MACCR | DR | 8:8 | 0x100 | meaning_001 | header:ETH_MACCR_DR_Msk |
| MACCR | DCRS | 9:9 | 0x200 | meaning_001 | header:ETH_MACCR_DCRS_Msk |
| MACCR | DO | 10:10 | 0x400 | meaning_001 | header:ETH_MACCR_DO_Msk |
| MACCR | ECRSFD | 11:11 | 0x800 | meaning_001 | header:ETH_MACCR_ECRSFD_Msk |
| MACCR | LM | 12:12 | 0x1000 | meaning_001 | header:ETH_MACCR_LM_Msk |
| MACCR | DM | 13:13 | 0x2000 | meaning_001 | header:ETH_MACCR_DM_Msk |
| MACCR | FES | 14:14 | 0x4000 | meaning_001 | header:ETH_MACCR_FES_Msk |
| MACCR | JE | 16:16 | 0x10000 | meaning_001 | header:ETH_MACCR_JE_Msk |
| MACCR | JD | 17:17 | 0x20000 | meaning_001 | header:ETH_MACCR_JD_Msk |
| MACCR | WD | 19:19 | 0x80000 | meaning_001 | header:ETH_MACCR_WD_Msk |
| MACCR | ACS | 20:20 | 0x100000 | meaning_001 | header:ETH_MACCR_ACS_Msk |
| MACCR | CST | 21:21 | 0x200000 | meaning_001 | header:ETH_MACCR_CST_Msk |
| MACCR | S2KP | 22:22 | 0x400000 | meaning_001 | header:ETH_MACCR_S2KP_Msk |
| MACCR | GPSLCE | 23:23 | 0x800000 | meaning_001 | header:ETH_MACCR_GPSLCE_Msk |
| MACCR | IPG | 26:24 | 0x7000000 | meaning_001 | header:ETH_MACCR_IPG_Msk |
| MACCR | IPC | 27:27 | 0x8000000 | meaning_001 | header:ETH_MACCR_IPC_Msk |
| MACCR | SARC | 30:28 | 0x70000000 | meaning_001 | header:ETH_MACCR_SARC_Msk |
| MACCR | ARP | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACCR_ARP_Msk |
| MACECR | GPSL | 13:0 | 0x3FFF | meaning_001 | header:ETH_MACECR_GPSL_Msk |
| MACECR | DCRCC | 16:16 | 0x10000 | meaning_001 | header:ETH_MACECR_DCRCC_Msk |
| MACECR | SPEN | 17:17 | 0x20000 | meaning_001 | header:ETH_MACECR_SPEN_Msk |
| MACECR | USP | 18:18 | 0x40000 | meaning_001 | header:ETH_MACECR_USP_Msk |
| MACECR | EIPGEN | 24:24 | 0x1000000 | meaning_001 | header:ETH_MACECR_EIPGEN_Msk |
| MACECR | EIPG | 29:25 | 0x3E000000 | meaning_001 | header:ETH_MACECR_EIPG_Msk |
| MACPFR | PR | 0:0 | 0x1 | meaning_001 | header:ETH_MACPFR_PR_Msk |
| MACPFR | HUC | 1:1 | 0x2 | meaning_001 | header:ETH_MACPFR_HUC_Msk |
| MACPFR | HMC | 2:2 | 0x4 | meaning_001 | header:ETH_MACPFR_HMC_Msk |
| MACPFR | DAIF | 3:3 | 0x8 | meaning_001 | header:ETH_MACPFR_DAIF_Msk |
| MACPFR | PM | 4:4 | 0x10 | meaning_001 | header:ETH_MACPFR_PM_Msk |
| MACPFR | DBF | 5:5 | 0x20 | meaning_001 | header:ETH_MACPFR_DBF_Msk |
| MACPFR | PCF | 7:6 | 0xC0 | meaning_001 | header:ETH_MACPFR_PCF_Msk |
| MACPFR | SAIF | 8:8 | 0x100 | meaning_001 | header:ETH_MACPFR_SAIF_Msk |
| MACPFR | SAF | 9:9 | 0x200 | meaning_001 | header:ETH_MACPFR_SAF_Msk |
| MACPFR | HPF | 10:10 | 0x400 | meaning_001 | header:ETH_MACPFR_HPF_Msk |
| MACPFR | VTFE | 16:16 | 0x10000 | meaning_001 | header:ETH_MACPFR_VTFE_Msk |
| MACPFR | IPFE | 20:20 | 0x100000 | meaning_001 | header:ETH_MACPFR_IPFE_Msk |
| MACPFR | DNTU | 21:21 | 0x200000 | meaning_001 | header:ETH_MACPFR_DNTU_Msk |
| MACPFR | RA | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACPFR_RA_Msk |
| MACWTR | WTO | 3:0 | 0xF | meaning_001 | header:ETH_MACWTR_WTO_Msk |
| MACWTR | PWE | 8:8 | 0x100 | meaning_001 | header:ETH_MACWTR_PWE_Msk |
| MACVTR | VL | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACVTR_VL_Msk |
| MACVTR | ETV | 16:16 | 0x10000 | meaning_001 | header:ETH_MACVTR_ETV_Msk |
| MACVTR | VTIM | 17:17 | 0x20000 | meaning_001 | header:ETH_MACVTR_VTIM_Msk |
| MACVTR | ESVL | 18:18 | 0x40000 | meaning_001 | header:ETH_MACVTR_ESVL_Msk |
| MACVTR | ERSVLM | 19:19 | 0x80000 | meaning_001 | header:ETH_MACVTR_ERSVLM_Msk |
| MACVTR | DOVLTC | 20:20 | 0x100000 | meaning_001 | header:ETH_MACVTR_DOVLTC_Msk |
| MACVTR | EVLS | 22:21 | 0x600000 | meaning_001 | header:ETH_MACVTR_EVLS_Msk |
| MACVTR | EVLRXS | 24:24 | 0x1000000 | meaning_001 | header:ETH_MACVTR_EVLRXS_Msk |
| MACVTR | VTHM | 25:25 | 0x2000000 | meaning_001 | header:ETH_MACVTR_VTHM_Msk |
| MACVTR | EDVLP | 26:26 | 0x4000000 | meaning_001 | header:ETH_MACVTR_EDVLP_Msk |
| MACVTR | ERIVLT | 27:27 | 0x8000000 | meaning_001 | header:ETH_MACVTR_ERIVLT_Msk |
| MACVTR | EIVLS | 29:28 | 0x30000000 | meaning_001 | header:ETH_MACVTR_EIVLS_Msk |
| MACVTR | EIVLRXS | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACVTR_EIVLRXS_Msk |
| MACVHTR | VLHT | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACVHTR_VLHT_Msk |
| MACVIR | VLT | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACVIR_VLT_Msk |
| MACVIR | VLC | 17:16 | 0x30000 | meaning_001 | header:ETH_MACVIR_VLC_Msk |
| MACVIR | VLP | 18:18 | 0x40000 | meaning_001 | header:ETH_MACVIR_VLP_Msk |
| MACVIR | CSVL | 19:19 | 0x80000 | meaning_001 | header:ETH_MACVIR_CSVL_Msk |
| MACVIR | VLTI | 20:20 | 0x100000 | meaning_001 | header:ETH_MACVIR_VLTI_Msk |
| MACIVIR | VLT | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACIVIR_VLT_Msk |
| MACIVIR | VLC | 17:16 | 0x30000 | meaning_001 | header:ETH_MACIVIR_VLC_Msk |
| MACIVIR | VLP | 18:18 | 0x40000 | meaning_001 | header:ETH_MACIVIR_VLP_Msk |
| MACIVIR | CSVL | 19:19 | 0x80000 | meaning_001 | header:ETH_MACIVIR_CSVL_Msk |
| MACIVIR | VLTI | 20:20 | 0x100000 | meaning_001 | header:ETH_MACIVIR_VLTI_Msk |
| MACTFCR | FCB | 0:0 | 0x1 | meaning_001 | header:ETH_MACTFCR_FCB_Msk |
| MACTFCR | TFE | 1:1 | 0x2 | meaning_001 | header:ETH_MACTFCR_TFE_Msk |
| MACTFCR | PLT | 6:4 | 0x70 | meaning_001 | header:ETH_MACTFCR_PLT_Msk |
| MACTFCR | DZPQ | 7:7 | 0x80 | meaning_001 | header:ETH_MACTFCR_DZPQ_Msk |
| MACTFCR | PT | 31:16 | 0xFFFF0000 | meaning_001 | header:ETH_MACTFCR_PT_Msk |
| MACRFCR | RFE | 0:0 | 0x1 | meaning_001 | header:ETH_MACRFCR_RFE_Msk |
| MACRFCR | UP | 1:1 | 0x2 | meaning_001 | header:ETH_MACRFCR_UP_Msk |
| MACISR | PHYIS | 3:3 | 0x8 | meaning_001 | header:ETH_MACISR_PHYIS_Msk |
| MACISR | PMTIS | 4:4 | 0x10 | meaning_001 | header:ETH_MACISR_PMTIS_Msk |
| MACISR | LPIIS | 5:5 | 0x20 | meaning_001 | header:ETH_MACISR_LPIIS_Msk |
| MACISR | MMCIS | 8:8 | 0x100 | meaning_001 | header:ETH_MACISR_MMCIS_Msk |
| MACISR | MMCRXIS | 9:9 | 0x200 | meaning_001 | header:ETH_MACISR_MMCRXIS_Msk |
| MACISR | MMCTXIS | 10:10 | 0x400 | meaning_001 | header:ETH_MACISR_MMCTXIS_Msk |
| MACISR | TSIS | 12:12 | 0x1000 | meaning_001 | header:ETH_MACISR_TSIS_Msk |
| MACISR | TXSTSIS | 13:13 | 0x2000 | meaning_001 | header:ETH_MACISR_TXSTSIS_Msk |
| MACISR | RXSTSIS | 14:14 | 0x4000 | meaning_001 | header:ETH_MACISR_RXSTSIS_Msk |
| MACIER | PHYIE | 3:3 | 0x8 | meaning_001 | header:ETH_MACIER_PHYIE_Msk |
| MACIER | PMTIE | 4:4 | 0x10 | meaning_001 | header:ETH_MACIER_PMTIE_Msk |
| MACIER | LPIIE | 5:5 | 0x20 | meaning_001 | header:ETH_MACIER_LPIIE_Msk |
| MACIER | TSIE | 12:12 | 0x1000 | meaning_001 | header:ETH_MACIER_TSIE_Msk |
| MACIER | TXSTSIE | 13:13 | 0x2000 | meaning_001 | header:ETH_MACIER_TXSTSIE_Msk |
| MACIER | RXSTSIE | 14:14 | 0x4000 | meaning_001 | header:ETH_MACIER_RXSTSIE_Msk |
| MACRXTXSR | TJT | 0:0 | 0x1 | meaning_001 | header:ETH_MACRXTXSR_TJT_Msk |
| MACRXTXSR | NCARR | 1:1 | 0x2 | meaning_001 | header:ETH_MACRXTXSR_NCARR_Msk |
| MACRXTXSR | LCARR | 2:2 | 0x4 | meaning_001 | header:ETH_MACRXTXSR_LCARR_Msk |
| MACRXTXSR | EXDEF | 3:3 | 0x8 | meaning_001 | header:ETH_MACRXTXSR_EXDEF_Msk |
| MACRXTXSR | LCOL | 4:4 | 0x10 | meaning_001 | header:ETH_MACRXTXSR_LCOL_Msk |
| MACRXTXSR | EXCOL | 5:5 | 0x20 | meaning_001 | header:ETH_MACRXTXSR_EXCOL_Msk |
| MACRXTXSR | RWT | 8:8 | 0x100 | meaning_001 | header:ETH_MACRXTXSR_RWT_Msk |
| MACPCSR | PWRDWN | 0:0 | 0x1 | meaning_001 | header:ETH_MACPCSR_PWRDWN_Msk |
| MACPCSR | MGKPKTEN | 1:1 | 0x2 | meaning_001 | header:ETH_MACPCSR_MGKPKTEN_Msk |
| MACPCSR | RWKPKTEN | 2:2 | 0x4 | meaning_001 | header:ETH_MACPCSR_RWKPKTEN_Msk |
| MACPCSR | MGKPRCVD | 5:5 | 0x20 | meaning_001 | header:ETH_MACPCSR_MGKPRCVD_Msk |
| MACPCSR | RWKPRCVD | 6:6 | 0x40 | meaning_001 | header:ETH_MACPCSR_RWKPRCVD_Msk |
| MACPCSR | GLBLUCAST | 9:9 | 0x200 | meaning_001 | header:ETH_MACPCSR_GLBLUCAST_Msk |
| MACPCSR | RWKPFE | 10:10 | 0x400 | meaning_001 | header:ETH_MACPCSR_RWKPFE_Msk |
| MACPCSR | RWKPTR | 28:24 | 0x1F000000 | meaning_001 | header:ETH_MACPCSR_RWKPTR_Msk |
| MACPCSR | RWKFILTRST | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACPCSR_RWKFILTRST_Msk |
| MACLCSR | TLPIEN | 0:0 | 0x1 | meaning_001 | header:ETH_MACLCSR_TLPIEN_Msk |
| MACLCSR | TLPIEX | 1:1 | 0x2 | meaning_001 | header:ETH_MACLCSR_TLPIEX_Msk |
| MACLCSR | RLPIEN | 2:2 | 0x4 | meaning_001 | header:ETH_MACLCSR_RLPIEN_Msk |
| MACLCSR | RLPIEX | 3:3 | 0x8 | meaning_001 | header:ETH_MACLCSR_RLPIEX_Msk |
| MACLCSR | TLPIST | 8:8 | 0x100 | meaning_001 | header:ETH_MACLCSR_TLPIST_Msk |
| MACLCSR | RLPIST | 9:9 | 0x200 | meaning_001 | header:ETH_MACLCSR_RLPIST_Msk |
| MACLCSR | LPIEN | 16:16 | 0x10000 | meaning_001 | header:ETH_MACLCSR_LPIEN_Msk |
| MACLCSR | PLS | 17:17 | 0x20000 | meaning_001 | header:ETH_MACLCSR_PLS_Msk |
| MACLCSR | LPITXA | 19:19 | 0x80000 | meaning_001 | header:ETH_MACLCSR_LPITXA_Msk |
| MACLCSR | LPITE | 20:20 | 0x100000 | meaning_001 | header:ETH_MACLCSR_LPITE_Msk |
| MACLCSR | LPITCSE | 21:21 | 0x200000 | meaning_001 | header:ETH_MACLCSR_LPITCSE_Msk |
| MACLTCR | TWT | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACLTCR_TWT_Msk |
| MACLTCR | LST | 25:16 | 0x3FF0000 | meaning_001 | header:ETH_MACLTCR_LST_Msk |
| MACLETR | LPIET | 19:0 | 0xFFFFF | meaning_001 | header:ETH_MACLETR_LPIET_Msk |
| MAC1USTCR | TIC1USCNTR | 11:0 | 0xFFF | meaning_001 | header:ETH_MAC1USTCR_TIC1USCNTR_Msk |
| MACVR | SNPSVER | 7:0 | 0xFF | meaning_001 | header:ETH_MACVR_SNPSVER_Msk |
| MACVR | USERVER | 15:8 | 0xFF00 | meaning_001 | header:ETH_MACVR_USERVER_Msk |
| MACDR | RPESTS | 0:0 | 0x1 | meaning_001 | header:ETH_MACDR_RPESTS_Msk |
| MACDR | RFCFCSTS | 2:1 | 0x6 | meaning_001 | header:ETH_MACDR_RFCFCSTS_Msk |
| MACDR | TPESTS | 16:16 | 0x10000 | meaning_001 | header:ETH_MACDR_TPESTS_Msk |
| MACDR | TFCSTS | 18:17 | 0x60000 | meaning_001 | header:ETH_MACDR_TFCSTS_Msk |
| MACHWF0R | MIISEL | 0:0 | 0x1 | meaning_001 | header:ETH_MACHWF0R_MIISEL_Msk |
| MACHWF0R | GMIISEL | 1:1 | 0x2 | meaning_001 | header:ETH_MACHWF0R_GMIISEL_Msk |
| MACHWF0R | HDSEL | 2:2 | 0x4 | meaning_001 | header:ETH_MACHWF0R_HDSEL_Msk |
| MACHWF0R | PCSSEL | 3:3 | 0x8 | meaning_001 | header:ETH_MACHWF0R_PCSSEL_Msk |
| MACHWF0R | VLHASH | 4:4 | 0x10 | meaning_001 | header:ETH_MACHWF0R_VLHASH_Msk |
| MACHWF0R | SMASEL | 5:5 | 0x20 | meaning_001 | header:ETH_MACHWF0R_SMASEL_Msk |
| MACHWF0R | RWKSEL | 6:6 | 0x40 | meaning_001 | header:ETH_MACHWF0R_RWKSEL_Msk |
| MACHWF0R | MGKSEL | 7:7 | 0x80 | meaning_001 | header:ETH_MACHWF0R_MGKSEL_Msk |
| MACHWF0R | MMCSEL | 8:8 | 0x100 | meaning_001 | header:ETH_MACHWF0R_MMCSEL_Msk |
| MACHWF0R | ARPOFFSEL | 9:9 | 0x200 | meaning_001 | header:ETH_MACHWF0R_ARPOFFSEL_Msk |
| MACHWF0R | TSSEL | 12:12 | 0x1000 | meaning_001 | header:ETH_MACHWF0R_TSSEL_Msk |
| MACHWF0R | EEESEL | 13:13 | 0x2000 | meaning_001 | header:ETH_MACHWF0R_EEESEL_Msk |
| MACHWF0R | TXCOESEL | 14:14 | 0x4000 | meaning_001 | header:ETH_MACHWF0R_TXCOESEL_Msk |
| MACHWF0R | RXCOESEL | 16:16 | 0x10000 | meaning_001 | header:ETH_MACHWF0R_RXCOESEL_Msk |
| MACHWF0R | ADDMACADRSEL | 22:18 | 0x7C0000 | meaning_001 | header:ETH_MACHWF0R_ADDMACADRSEL_Msk |
| MACHWF0R | MACADR32SEL | 23:23 | 0x800000 | meaning_001 | header:ETH_MACHWF0R_MACADR32SEL_Msk |
| MACHWF0R | MACADR64SEL | 24:24 | 0x1000000 | meaning_001 | header:ETH_MACHWF0R_MACADR64SEL_Msk |
| MACHWF0R | TSSTSSEL | 26:25 | 0x6000000 | meaning_001 | header:ETH_MACHWF0R_TSSTSSEL_Msk |
| MACHWF0R | SAVLANINS | 27:27 | 0x8000000 | meaning_001 | header:ETH_MACHWF0R_SAVLANINS_Msk |
| MACHWF0R | ACTPHYSEL | 30:28 | 0x70000000 | meaning_001 | header:ETH_MACHWF0R_ACTPHYSEL_Msk |
| MACHWF1R | RXFIFOSIZE | 4:0 | 0x1F | meaning_001 | header:ETH_MACHWF1R_RXFIFOSIZE_Msk |
| MACHWF1R | TXFIFOSIZE | 10:6 | 0x7C0 | meaning_001 | header:ETH_MACHWF1R_TXFIFOSIZE_Msk |
| MACHWF1R | OSTEN | 11:11 | 0x800 | meaning_001 | header:ETH_MACHWF1R_OSTEN_Msk |
| MACHWF1R | PTOEN | 12:12 | 0x1000 | meaning_001 | header:ETH_MACHWF1R_PTOEN_Msk |
| MACHWF1R | ADVTHWORD | 13:13 | 0x2000 | meaning_001 | header:ETH_MACHWF1R_ADVTHWORD_Msk |
| MACHWF1R | ADDR64 | 15:14 | 0xC000 | meaning_001 | header:ETH_MACHWF1R_ADDR64_Msk |
| MACHWF1R | DCBEN | 16:16 | 0x10000 | meaning_001 | header:ETH_MACHWF1R_DCBEN_Msk |
| MACHWF1R | SPHEN | 17:17 | 0x20000 | meaning_001 | header:ETH_MACHWF1R_SPHEN_Msk |
| MACHWF1R | TSOEN | 18:18 | 0x40000 | meaning_001 | header:ETH_MACHWF1R_TSOEN_Msk |
| MACHWF1R | DBGMEMA | 19:19 | 0x80000 | meaning_001 | header:ETH_MACHWF1R_DBGMEMA_Msk |
| MACHWF1R | AVSEL | 20:20 | 0x100000 | meaning_001 | header:ETH_MACHWF1R_AVSEL_Msk |
| MACHWF1R | HASHTBLSZ | 25:24 | 0x3000000 | meaning_001 | header:ETH_MACHWF1R_HASHTBLSZ_Msk |
| MACHWF1R | L3L4FNUM | 30:27 | 0x78000000 | meaning_001 | header:ETH_MACHWF1R_L3L4FNUM_Msk |
| MACHWF2R | RXQCNT | 3:0 | 0xF | meaning_001 | header:ETH_MACHWF2R_RXQCNT_Msk |
| MACHWF2R | TXQCNT | 9:6 | 0x3C0 | meaning_001 | header:ETH_MACHWF2R_TXQCNT_Msk |
| MACHWF2R | RXCHCNT | 15:13 | 0xE000 | meaning_001 | header:ETH_MACHWF2R_RXCHCNT_Msk |
| MACHWF2R | TXCHCNT | 21:18 | 0x3C0000 | meaning_001 | header:ETH_MACHWF2R_TXCHCNT_Msk |
| MACHWF2R | PPSOUTNUM | 26:24 | 0x7000000 | meaning_001 | header:ETH_MACHWF2R_PPSOUTNUM_Msk |
| MACHWF2R | AUXSNAPNUM | 30:28 | 0x70000000 | meaning_001 | header:ETH_MACHWF2R_AUXSNAPNUM_Msk |
| MACMDIOAR | MB | 0:0 | 0x1 | meaning_001 | header:ETH_MACMDIOAR_MB_Msk |
| MACMDIOAR | C45E | 1:1 | 0x2 | meaning_001 | header:ETH_MACMDIOAR_C45E_Msk |
| MACMDIOAR | MOC | 3:2 | 0xC | meaning_001 | header:ETH_MACMDIOAR_MOC_Msk |
| MACMDIOAR | SKAP | 4:4 | 0x10 | meaning_001 | header:ETH_MACMDIOAR_SKAP_Msk |
| MACMDIOAR | CR | 11:8 | 0xF00 | meaning_001 | header:ETH_MACMDIOAR_CR_Msk |
| MACMDIOAR | NTC | 14:12 | 0x7000 | meaning_001 | header:ETH_MACMDIOAR_NTC_Msk |
| MACMDIOAR | RDA | 20:16 | 0x1F0000 | meaning_001 | header:ETH_MACMDIOAR_RDA_Msk |
| MACMDIOAR | PA | 25:21 | 0x3E00000 | meaning_001 | header:ETH_MACMDIOAR_PA_Msk |
| MACMDIOAR | BTB | 26:26 | 0x4000000 | meaning_001 | header:ETH_MACMDIOAR_BTB_Msk |
| MACMDIOAR | PSE | 27:27 | 0x8000000 | meaning_001 | header:ETH_MACMDIOAR_PSE_Msk |
| MACMDIODR | MD | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACMDIODR_MD_Msk |
| MACMDIODR | RA | 31:16 | 0xFFFF0000 | meaning_001 | header:ETH_MACMDIODR_RA_Msk |
| MACARPAR | ARPPA | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACARPAR_ARPPA_Msk |
| MACA0HR | ADDRHI | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACA0HR_ADDRHI_Msk |
| MACA0HR | AE | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACA0HR_AE_Msk |
| MACA0LR | ADDRLO | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACA0LR_ADDRLO_Msk |
| MACA1HR | ADDRHI | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACA1HR_ADDRHI_Msk |
| MACA1HR | MBC | 29:24 | 0x3F000000 | meaning_001 | header:ETH_MACA1HR_MBC_Msk |
| MACA1HR | SA | 30:30 | 0x40000000 | meaning_001 | header:ETH_MACA1HR_SA_Msk |
| MACA1HR | AE | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACA1HR_AE_Msk |
| MACA1LR | ADDRLO | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACA1LR_ADDRLO_Msk |
| MACA2HR | ADDRHI | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACA2HR_ADDRHI_Msk |
| MACA2HR | MBC | 29:24 | 0x3F000000 | meaning_001 | header:ETH_MACA2HR_MBC_Msk |
| MACA2HR | SA | 30:30 | 0x40000000 | meaning_001 | header:ETH_MACA2HR_SA_Msk |
| MACA2HR | AE | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACA2HR_AE_Msk |
| MACA2LR | ADDRLO | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACA2LR_ADDRLO_Msk |
| MACA3HR | ADDRHI | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACA3HR_ADDRHI_Msk |
| MACA3HR | MBC | 29:24 | 0x3F000000 | meaning_001 | header:ETH_MACA3HR_MBC_Msk |
| MACA3HR | SA | 30:30 | 0x40000000 | meaning_001 | header:ETH_MACA3HR_SA_Msk |
| MACA3HR | AE | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACA3HR_AE_Msk |
| MACA3LR | ADDRLO | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACA3LR_ADDRLO_Msk |
| MMCCR | CNTRST | 0:0 | 0x1 | meaning_001 | header:ETH_MMCCR_CNTRST_Msk |
| MMCCR | CNTSTOPRO | 1:1 | 0x2 | meaning_001 | header:ETH_MMCCR_CNTSTOPRO_Msk |
| MMCCR | RSTONRD | 2:2 | 0x4 | meaning_001 | header:ETH_MMCCR_RSTONRD_Msk |
| MMCCR | CNTFREEZ | 3:3 | 0x8 | meaning_001 | header:ETH_MMCCR_CNTFREEZ_Msk |
| MMCCR | CNTPRST | 4:4 | 0x10 | meaning_001 | header:ETH_MMCCR_CNTPRST_Msk |
| MMCCR | CNTPRSTLVL | 5:5 | 0x20 | meaning_001 | header:ETH_MMCCR_CNTPRSTLVL_Msk |
| MMCCR | UCDBC | 8:8 | 0x100 | meaning_001 | header:ETH_MMCCR_UCDBC_Msk |
| MMCRIR | RXCRCERPIS | 5:5 | 0x20 | meaning_001 | header:ETH_MMCRIR_RXCRCERPIS_Msk |
| MMCRIR | RXALGNERPIS | 6:6 | 0x40 | meaning_001 | header:ETH_MMCRIR_RXALGNERPIS_Msk |
| MMCRIR | RXUCGPIS | 17:17 | 0x20000 | meaning_001 | header:ETH_MMCRIR_RXUCGPIS_Msk |
| MMCRIR | RXLPIUSCIS | 26:26 | 0x4000000 | meaning_001 | header:ETH_MMCRIR_RXLPIUSCIS_Msk |
| MMCRIR | RXLPITRCIS | 27:27 | 0x8000000 | meaning_001 | header:ETH_MMCRIR_RXLPITRCIS_Msk |
| MMCTIR | TXSCOLGPIS | 14:14 | 0x4000 | meaning_001 | header:ETH_MMCTIR_TXSCOLGPIS_Msk |
| MMCTIR | TXMCOLGPIS | 15:15 | 0x8000 | meaning_001 | header:ETH_MMCTIR_TXMCOLGPIS_Msk |
| MMCTIR | TXGPKTIS | 21:21 | 0x200000 | meaning_001 | header:ETH_MMCTIR_TXGPKTIS_Msk |
| MMCTIR | TXLPIUSCIS | 26:26 | 0x4000000 | meaning_001 | header:ETH_MMCTIR_TXLPIUSCIS_Msk |
| MMCTIR | TXLPITRCIS | 27:27 | 0x8000000 | meaning_001 | header:ETH_MMCTIR_TXLPITRCIS_Msk |
| MMCRIMR | RXCRCERPIM | 5:5 | 0x20 | meaning_001 | header:ETH_MMCRIMR_RXCRCERPIM_Msk |
| MMCRIMR | RXALGNERPIM | 6:6 | 0x40 | meaning_001 | header:ETH_MMCRIMR_RXALGNERPIM_Msk |
| MMCRIMR | RXUCGPIM | 17:17 | 0x20000 | meaning_001 | header:ETH_MMCRIMR_RXUCGPIM_Msk |
| MMCRIMR | RXLPIUSCIM | 26:26 | 0x4000000 | meaning_001 | header:ETH_MMCRIMR_RXLPIUSCIM_Msk |
| MMCRIMR | RXLPITRCIM | 27:27 | 0x8000000 | meaning_001 | header:ETH_MMCRIMR_RXLPITRCIM_Msk |
| MMCTIMR | TXSCOLGPIM | 14:14 | 0x4000 | meaning_001 | header:ETH_MMCTIMR_TXSCOLGPIM_Msk |
| MMCTIMR | TXMCOLGPIM | 15:15 | 0x8000 | meaning_001 | header:ETH_MMCTIMR_TXMCOLGPIM_Msk |
| MMCTIMR | TXGPKTIM | 21:21 | 0x200000 | meaning_001 | header:ETH_MMCTIMR_TXGPKTIM_Msk |
| MMCTIMR | TXLPIUSCIM | 26:26 | 0x4000000 | meaning_001 | header:ETH_MMCTIMR_TXLPIUSCIM_Msk |
| MMCTIMR | TXLPITRCIM | 27:27 | 0x8000000 | meaning_001 | header:ETH_MMCTIMR_TXLPITRCIM_Msk |
| MACTSCR | TSENA | 0:0 | 0x1 | meaning_001 | header:ETH_MACTSCR_TSENA_Msk |
| MACTSCR | TSCFUPDT | 1:1 | 0x2 | meaning_001 | header:ETH_MACTSCR_TSCFUPDT_Msk |
| MACTSCR | TSINIT | 2:2 | 0x4 | meaning_001 | header:ETH_MACTSCR_TSINIT_Msk |
| MACTSCR | TSUPDT | 3:3 | 0x8 | meaning_001 | header:ETH_MACTSCR_TSUPDT_Msk |
| MACTSCR | TSADDREG | 5:5 | 0x20 | meaning_001 | header:ETH_MACTSCR_TSADDREG_Msk |
| MACTSCR | TSENALL | 8:8 | 0x100 | meaning_001 | header:ETH_MACTSCR_TSENALL_Msk |
| MACTSCR | TSCTRLSSR | 9:9 | 0x200 | meaning_001 | header:ETH_MACTSCR_TSCTRLSSR_Msk |
| MACTSCR | TSVER2ENA | 10:10 | 0x400 | meaning_001 | header:ETH_MACTSCR_TSVER2ENA_Msk |
| MACTSCR | TSIPENA | 11:11 | 0x800 | meaning_001 | header:ETH_MACTSCR_TSIPENA_Msk |
| MACTSCR | TSIPV6ENA | 12:12 | 0x1000 | meaning_001 | header:ETH_MACTSCR_TSIPV6ENA_Msk |
| MACTSCR | TSIPV4ENA | 13:13 | 0x2000 | meaning_001 | header:ETH_MACTSCR_TSIPV4ENA_Msk |
| MACTSCR | TSEVNTENA | 14:14 | 0x4000 | meaning_001 | header:ETH_MACTSCR_TSEVNTENA_Msk |
| MACTSCR | TSMSTRENA | 15:15 | 0x8000 | meaning_001 | header:ETH_MACTSCR_TSMSTRENA_Msk |
| MACTSCR | SNAPTYPSEL | 17:16 | 0x30000 | meaning_001 | header:ETH_MACTSCR_SNAPTYPSEL_Msk |
| MACTSCR | TSENMACADDR | 18:18 | 0x40000 | meaning_001 | header:ETH_MACTSCR_TSENMACADDR_Msk |
| MACTSCR | CSC | 19:19 | 0x80000 | meaning_001 | header:ETH_MACTSCR_CSC_Msk |
| MACTSCR | TXTSSTSM | 24:24 | 0x1000000 | meaning_001 | header:ETH_MACTSCR_TXTSSTSM_Msk |
| MACSTSR | TSS | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACSTSR_TSS_Msk |
| MACSTNR | TSSS | 30:0 | 0x7FFFFFFF | meaning_001 | header:ETH_MACSTNR_TSSS_Msk |
| MACSTSUR | TSS | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACSTSUR_TSS_Msk |
| MACSTNUR | TSSS | 30:0 | 0x7FFFFFFF | meaning_001 | header:ETH_MACSTNUR_TSSS_Msk |
| MACSTNUR | ADDSUB | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACSTNUR_ADDSUB_Msk |
| MACTSAR | TSAR | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTSAR_TSAR_Msk |
| MACTSSR | TSSOVF | 0:0 | 0x1 | meaning_001 | header:ETH_MACTSSR_TSSOVF_Msk |
| MACTSSR | TSTARGT0 | 1:1 | 0x2 | meaning_001 | header:ETH_MACTSSR_TSTARGT0_Msk |
| MACTSSR | AUXTSTRIG | 2:2 | 0x4 | meaning_001 | header:ETH_MACTSSR_AUXTSTRIG_Msk |
| MACTSSR | TSTRGTERR0 | 3:3 | 0x8 | meaning_001 | header:ETH_MACTSSR_TSTRGTERR0_Msk |
| MACTSSR | TXTSSIS | 15:15 | 0x8000 | meaning_001 | header:ETH_MACTSSR_TXTSSIS_Msk |
| MACTSSR | ATSSTN | 19:16 | 0xF0000 | meaning_001 | header:ETH_MACTSSR_ATSSTN_Msk |
| MACTSSR | ATSSTM | 24:24 | 0x1000000 | meaning_001 | header:ETH_MACTSSR_ATSSTM_Msk |
| MACTSSR | ATSNS | 29:25 | 0x3E000000 | meaning_001 | header:ETH_MACTSSR_ATSNS_Msk |
| MACTTSSNR | TXTSSLO | 30:0 | 0x7FFFFFFF | meaning_001 | header:ETH_MACTTSSNR_TXTSSLO_Msk |
| MACTTSSNR | TXTSSMIS | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACTTSSNR_TXTSSMIS_Msk |
| MACTTSSSR | TXTSSHI | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTTSSSR_TXTSSHI_Msk |
| MACACR | ATSFC | 0:0 | 0x1 | meaning_001 | header:ETH_MACACR_ATSFC_Msk |
| MACACR | ATSEN0 | 4:4 | 0x10 | meaning_001 | header:ETH_MACACR_ATSEN0_Msk |
| MACACR | ATSEN1 | 5:5 | 0x20 | meaning_001 | header:ETH_MACACR_ATSEN1_Msk |
| MACACR | ATSEN2 | 6:6 | 0x40 | meaning_001 | header:ETH_MACACR_ATSEN2_Msk |
| MACACR | ATSEN3 | 7:7 | 0x80 | meaning_001 | header:ETH_MACACR_ATSEN3_Msk |
| MACATSNR | AUXTSLO | 30:0 | 0x7FFFFFFF | meaning_001 | header:ETH_MACATSNR_AUXTSLO_Msk |
| MACATSSR | AUXTSHI | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACATSSR_AUXTSHI_Msk |
| MACTSIACR | OSTIAC | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTSIACR_OSTIAC_Msk |
| MACTSEACR | OSTEAC | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTSEACR_OSTEAC_Msk |
| MACTSICNR | TSIC | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTSICNR_TSIC_Msk |
| MACTSECNR | TSEC | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACTSECNR_TSEC_Msk |
| MACPPSCR | PPSCTRL | 3:0 | 0xF | meaning_001 | header:ETH_MACPPSCR_PPSCTRL_Msk |
| MACPPSCR | PPSEN0 | 4:4 | 0x10 | meaning_001 | header:ETH_MACPPSCR_PPSEN0_Msk |
| MACPPSCR | TRGTMODSEL0 | 6:5 | 0x60 | meaning_001 | header:ETH_MACPPSCR_TRGTMODSEL0_Msk |
| MACPPSTTSR | TSTRH0 | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACPPSTTSR_TSTRH0_Msk |
| MACPPSTTNR | TTSL0 | 30:0 | 0x7FFFFFFF | meaning_001 | header:ETH_MACPPSTTNR_TTSL0_Msk |
| MACPPSTTNR | TRGTBUSY0 | 31:31 | 0x80000000 | meaning_001 | header:ETH_MACPPSTTNR_TRGTBUSY0_Msk |
| MACPPSIR | PPSINT0 | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACPPSIR_PPSINT0_Msk |
| MACPPSWR | PPSWIDTH0 | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACPPSWR_PPSWIDTH0_Msk |
| MACPOCR | PTOEN | 0:0 | 0x1 | meaning_001 | header:ETH_MACPOCR_PTOEN_Msk |
| MACPOCR | ASYNCEN | 1:1 | 0x2 | meaning_001 | header:ETH_MACPOCR_ASYNCEN_Msk |
| MACPOCR | APDREQEN | 2:2 | 0x4 | meaning_001 | header:ETH_MACPOCR_APDREQEN_Msk |
| MACPOCR | ASYNCTRIG | 4:4 | 0x10 | meaning_001 | header:ETH_MACPOCR_ASYNCTRIG_Msk |
| MACPOCR | APDREQTRIG | 5:5 | 0x20 | meaning_001 | header:ETH_MACPOCR_APDREQTRIG_Msk |
| MACPOCR | DRRDIS | 6:6 | 0x40 | meaning_001 | header:ETH_MACPOCR_DRRDIS_Msk |
| MACPOCR | DN | 15:8 | 0xFF00 | meaning_001 | header:ETH_MACPOCR_DN_Msk |
| MACSPI0R | SPI0 | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACSPI0R_SPI0_Msk |
| MACSPI1R | SPI1 | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_MACSPI1R_SPI1_Msk |
| MACSPI2R | SPI2 | 15:0 | 0xFFFF | meaning_001 | header:ETH_MACSPI2R_SPI2_Msk |
| MACLMIR | LSI | 7:0 | 0xFF | meaning_001 | header:ETH_MACLMIR_LSI_Msk |
| MACLMIR | DRSYNCR | 10:8 | 0x700 | meaning_001 | header:ETH_MACLMIR_DRSYNCR_Msk |
| MACLMIR | LMPDRI | 31:24 | 0xFF000000 | meaning_001 | header:ETH_MACLMIR_LMPDRI_Msk |
| MTLOMR | DTXSTS | 1:1 | 0x2 | meaning_001 | header:ETH_MTLOMR_DTXSTS_Msk |
| MTLOMR | CNTPRST | 8:8 | 0x100 | meaning_001 | header:ETH_MTLOMR_CNTPRST_Msk |
| MTLOMR | CNTCLR | 9:9 | 0x200 | meaning_001 | header:ETH_MTLOMR_CNTCLR_Msk |
| MTLISR | QIS | 0:0 | 0x1 | meaning_001 | header:ETH_MTLISR_QIS_Msk |
| MTLISR | MACIS | 16:16 | 0x10000 | meaning_001 | header:ETH_MTLISR_MACIS_Msk |
| MTLTQOMR | FTQ | 0:0 | 0x1 | meaning_001 | header:ETH_MTLTQOMR_FTQ_Msk |
| MTLTQOMR | TSF | 1:1 | 0x2 | meaning_001 | header:ETH_MTLTQOMR_TSF_Msk |
| MTLTQOMR | TTC | 6:4 | 0x70 | meaning_001 | header:ETH_MTLTQOMR_TTC_Msk |
| MTLTQUR | UFPKTCNT | 10:0 | 0x7FF | meaning_001 | header:ETH_MTLTQUR_UFPKTCNT_Msk |
| MTLTQUR | UFCNTOVF | 11:11 | 0x800 | meaning_001 | header:ETH_MTLTQUR_UFCNTOVF_Msk |
| MTLTQDR | TXQPAUSED | 0:0 | 0x1 | meaning_001 | header:ETH_MTLTQDR_TXQPAUSED_Msk |
| MTLTQDR | TRCSTS | 2:1 | 0x6 | meaning_001 | header:ETH_MTLTQDR_TRCSTS_Msk |
| MTLTQDR | TWCSTS | 3:3 | 0x8 | meaning_001 | header:ETH_MTLTQDR_TWCSTS_Msk |
| MTLTQDR | TXQSTS | 4:4 | 0x10 | meaning_001 | header:ETH_MTLTQDR_TXQSTS_Msk |
| MTLTQDR | TXSTSFSTS | 5:5 | 0x20 | meaning_001 | header:ETH_MTLTQDR_TXSTSFSTS_Msk |
| MTLTQDR | PTXQ | 18:16 | 0x70000 | meaning_001 | header:ETH_MTLTQDR_PTXQ_Msk |
| MTLTQDR | STXSTSF | 22:20 | 0x700000 | meaning_001 | header:ETH_MTLTQDR_STXSTSF_Msk |
| MTLQICSR | TXUNFIS | 0:0 | 0x1 | meaning_001 | header:ETH_MTLQICSR_TXUNFIS_Msk |
| MTLQICSR | TXUIE | 8:8 | 0x100 | meaning_001 | header:ETH_MTLQICSR_TXUIE_Msk |
| MTLQICSR | RXOVFIS | 16:16 | 0x10000 | meaning_001 | header:ETH_MTLQICSR_RXOVFIS_Msk |
| MTLQICSR | RXOIE | 24:24 | 0x1000000 | meaning_001 | header:ETH_MTLQICSR_RXOIE_Msk |
| MTLRQOMR | RTC | 1:0 | 0x3 | meaning_001 | header:ETH_MTLRQOMR_RTC_Msk |
| MTLRQOMR | FUP | 3:3 | 0x8 | meaning_001 | header:ETH_MTLRQOMR_FUP_Msk |
| MTLRQOMR | FEP | 4:4 | 0x10 | meaning_001 | header:ETH_MTLRQOMR_FEP_Msk |
| MTLRQOMR | RSF | 5:5 | 0x20 | meaning_001 | header:ETH_MTLRQOMR_RSF_Msk |
| MTLRQOMR | DISTCPEF | 6:6 | 0x40 | meaning_001 | header:ETH_MTLRQOMR_DISTCPEF_Msk |
| MTLRQOMR | EHFC | 7:7 | 0x80 | meaning_001 | header:ETH_MTLRQOMR_EHFC_Msk |
| MTLRQOMR | RFA | 10:8 | 0x700 | meaning_001 | header:ETH_MTLRQOMR_RFA_Msk |
| MTLRQOMR | RFD | 16:14 | 0x1C000 | meaning_001 | header:ETH_MTLRQOMR_RFD_Msk |
| MTLRQOMR | RQS | 22:20 | 0x700000 | meaning_001 | header:ETH_MTLRQOMR_RQS_Msk |
| MTLRQMPOCR | OVFPKTCNT | 10:0 | 0x7FF | meaning_001 | header:ETH_MTLRQMPOCR_OVFPKTCNT_Msk |
| MTLRQMPOCR | OVFCNTOVF | 11:11 | 0x800 | meaning_001 | header:ETH_MTLRQMPOCR_OVFCNTOVF_Msk |
| MTLRQMPOCR | MISPKTCNT | 26:16 | 0x7FF0000 | meaning_001 | header:ETH_MTLRQMPOCR_MISPKTCNT_Msk |
| MTLRQMPOCR | MISCNTOVF | 27:27 | 0x8000000 | meaning_001 | header:ETH_MTLRQMPOCR_MISCNTOVF_Msk |
| MTLRQDR | RWCSTS | 0:0 | 0x1 | meaning_001 | header:ETH_MTLRQDR_RWCSTS_Msk |
| MTLRQDR | RRCSTS | 2:1 | 0x6 | meaning_001 | header:ETH_MTLRQDR_RRCSTS_Msk |
| MTLRQDR | RXQSTS | 5:4 | 0x30 | meaning_001 | header:ETH_MTLRQDR_RXQSTS_Msk |
| MTLRQDR | PRXQ | 29:16 | 0x3FFF0000 | meaning_001 | header:ETH_MTLRQDR_PRXQ_Msk |
| DMAMR | SWR | 0:0 | 0x1 | meaning_001 | header:ETH_DMAMR_SWR_Msk |
| DMAMR | DA | 1:1 | 0x2 | meaning_001 | header:ETH_DMAMR_DA_Msk |
| DMAMR | TXPR | 11:11 | 0x800 | meaning_001 | header:ETH_DMAMR_TXPR_Msk |
| DMAMR | PR | 14:12 | 0x7000 | meaning_001 | header:ETH_DMAMR_PR_Msk |
| DMAMR | INTM | 17:16 | 0x30000 | meaning_001 | header:ETH_DMAMR_INTM_Msk |
| DMASBMR | FB | 0:0 | 0x1 | meaning_001 | header:ETH_DMASBMR_FB_Msk |
| DMASBMR | AAL | 12:12 | 0x1000 | meaning_001 | header:ETH_DMASBMR_AAL_Msk |
| DMASBMR | MB | 14:14 | 0x4000 | meaning_001 | header:ETH_DMASBMR_MB_Msk |
| DMASBMR | RB | 15:15 | 0x8000 | meaning_001 | header:ETH_DMASBMR_RB_Msk |
| DMAISR | DMACIS | 0:0 | 0x1 | meaning_001 | header:ETH_DMAISR_DMACIS_Msk |
| DMAISR | MTLIS | 16:16 | 0x10000 | meaning_001 | header:ETH_DMAISR_MTLIS_Msk |
| DMAISR | MACIS | 17:17 | 0x20000 | meaning_001 | header:ETH_DMAISR_MACIS_Msk |
| DMACCR | MSS | 13:0 | 0x3FFF | meaning_001 | header:ETH_DMACCR_MSS_Msk |
| DMACCR | DSL | 20:18 | 0x1C0000 | meaning_001 | header:ETH_DMACCR_DSL_Msk |
| DMACTCR | ST | 0:0 | 0x1 | meaning_001 | header:ETH_DMACTCR_ST_Msk |
| DMACTCR | OSP | 4:4 | 0x10 | meaning_001 | header:ETH_DMACTCR_OSP_Msk |
| DMACTCR | TSE | 12:12 | 0x1000 | meaning_001 | header:ETH_DMACTCR_TSE_Msk |
| DMACTCR | TPBL | 21:16 | 0x3F0000 | meaning_001 | header:ETH_DMACTCR_TPBL_Msk |
| DMACRCR | SR | 0:0 | 0x1 | meaning_001 | header:ETH_DMACRCR_SR_Msk |
| DMACRCR | RBSZ | 14:1 | 0x7FFE | meaning_001 | header:ETH_DMACRCR_RBSZ_Msk |
| DMACRCR | RPBL | 21:16 | 0x3F0000 | meaning_001 | header:ETH_DMACRCR_RPBL_Msk |
| DMACRCR | RPF | 31:31 | 0x80000000 | meaning_001 | header:ETH_DMACRCR_RPF_Msk |
| DMACTDLAR | TDESLA | 31:2 | 0xFFFFFFFC | meaning_001 | header:ETH_DMACTDLAR_TDESLA_Msk |
| DMACRDLAR | RDESLA | 31:2 | 0xFFFFFFFC | meaning_001 | header:ETH_DMACRDLAR_RDESLA_Msk |
| DMACTDTPR | TDT | 31:2 | 0xFFFFFFFC | meaning_001 | header:ETH_DMACTDTPR_TDT_Msk |
| DMACRDTPR | RDT | 31:2 | 0xFFFFFFFC | meaning_001 | header:ETH_DMACRDTPR_RDT_Msk |
| DMACTDRLR | TDRL | 9:0 | 0x3FF | meaning_001 | header:ETH_DMACTDRLR_TDRL_Msk |
| DMACRDRLR | RDRL | 9:0 | 0x3FF | meaning_001 | header:ETH_DMACRDRLR_RDRL_Msk |
| DMACIER | TIE | 0:0 | 0x1 | meaning_001 | header:ETH_DMACIER_TIE_Msk |
| DMACIER | TXSE | 1:1 | 0x2 | meaning_001 | header:ETH_DMACIER_TXSE_Msk |
| DMACIER | TBUE | 2:2 | 0x4 | meaning_001 | header:ETH_DMACIER_TBUE_Msk |
| DMACIER | RIE | 6:6 | 0x40 | meaning_001 | header:ETH_DMACIER_RIE_Msk |
| DMACIER | RBUE | 7:7 | 0x80 | meaning_001 | header:ETH_DMACIER_RBUE_Msk |
| DMACIER | RSE | 8:8 | 0x100 | meaning_001 | header:ETH_DMACIER_RSE_Msk |
| DMACIER | RWTE | 9:9 | 0x200 | meaning_001 | header:ETH_DMACIER_RWTE_Msk |
| DMACIER | ETIE | 10:10 | 0x400 | meaning_001 | header:ETH_DMACIER_ETIE_Msk |
| DMACIER | ERIE | 11:11 | 0x800 | meaning_001 | header:ETH_DMACIER_ERIE_Msk |
| DMACIER | FBEE | 12:12 | 0x1000 | meaning_001 | header:ETH_DMACIER_FBEE_Msk |
| DMACIER | CDEE | 13:13 | 0x2000 | meaning_001 | header:ETH_DMACIER_CDEE_Msk |
| DMACIER | AIE | 14:14 | 0x4000 | meaning_001 | header:ETH_DMACIER_AIE_Msk |
| DMACIER | NIE | 15:15 | 0x8000 | meaning_001 | header:ETH_DMACIER_NIE_Msk |
| DMACRIWTR | RWT | 7:0 | 0xFF | meaning_001 | header:ETH_DMACRIWTR_RWT_Msk |
| DMACCATDR | CURTDESAPTR | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_DMACCATDR_CURTDESAPTR_Msk |
| DMACCARDR | CURRDESAPTR | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_DMACCARDR_CURRDESAPTR_Msk |
| DMACCATBR | CURTBUFAPTR | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_DMACCATBR_CURTBUFAPTR_Msk |
| DMACCARBR | CURRBUFAPTR | 31:0 | 0xFFFFFFFF | meaning_001 | header:ETH_DMACCARBR_CURRBUFAPTR_Msk |
| DMACSR | TI | 0:0 | 0x1 | meaning_001 | header:ETH_DMACSR_TI_Msk |
| DMACSR | TPS | 1:1 | 0x2 | meaning_001 | header:ETH_DMACSR_TPS_Msk |
| DMACSR | TBU | 2:2 | 0x4 | meaning_001 | header:ETH_DMACSR_TBU_Msk |
| DMACSR | RI | 6:6 | 0x40 | meaning_001 | header:ETH_DMACSR_RI_Msk |
| DMACSR | RBU | 7:7 | 0x80 | meaning_001 | header:ETH_DMACSR_RBU_Msk |
| DMACSR | RPS | 8:8 | 0x100 | meaning_001 | header:ETH_DMACSR_RPS_Msk |
| DMACSR | RWT | 9:9 | 0x200 | meaning_001 | header:ETH_DMACSR_RWT_Msk |
| DMACSR | ETI | 10:10 | 0x400 | meaning_001 | header:ETH_DMACSR_ETI_Msk |
| DMACSR | ERI | 11:11 | 0x800 | meaning_001 | header:ETH_DMACSR_ERI_Msk |
| DMACSR | FBE | 12:12 | 0x1000 | meaning_001 | header:ETH_DMACSR_FBE_Msk |
| DMACSR | CDE | 13:13 | 0x2000 | meaning_001 | header:ETH_DMACSR_CDE_Msk |
| DMACSR | AIS | 14:14 | 0x4000 | meaning_001 | header:ETH_DMACSR_AIS_Msk |
| DMACSR | NIS | 15:15 | 0x8000 | meaning_001 | header:ETH_DMACSR_NIS_Msk |
| DMACSR | TEB | 18:16 | 0x70000 | meaning_001 | header:ETH_DMACSR_TEB_Msk |
| DMACSR | REB | 21:19 | 0x380000 | meaning_001 | header:ETH_DMACSR_REB_Msk |
| DMACMFCR | MFC | 10:0 | 0x7FF | meaning_001 | header:ETH_DMACMFCR_MFC_Msk |
| DMACMFCR | MFCO | 15:15 | 0x8000 | meaning_001 | header:ETH_DMACMFCR_MFCO_Msk |

### Meaning references

Each Meaning identifier resolves to its complete text below; no fields or operating facts were omitted.

| Identifier | Complete meaning |
| --- | --- |
| meaning_001 | Declaration only; encoding requires reviewed semantics. |

## Operating semantics unavailable

**eth: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- DMADSR: bit fields withheld: UNSUPPORTED_MASK: ETH_DMADSR_RPS_CLOSING_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
