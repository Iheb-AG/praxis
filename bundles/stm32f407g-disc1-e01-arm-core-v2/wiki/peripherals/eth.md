# ETH — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ETH | 0x40028000 | Not asserted | Not asserted | header:ETH_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MACCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACCR; header:ETH_TypeDef.MACCR |
| MACFFR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACFFR; header:ETH_TypeDef.MACFFR |
| MACHTHR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHTHR; header:ETH_TypeDef.MACHTHR |
| MACHTLR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACHTLR; header:ETH_TypeDef.MACHTLR |
| MACMIIAR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACMIIAR; header:ETH_TypeDef.MACMIIAR |
| MACMIIDR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACMIIDR; header:ETH_TypeDef.MACMIIDR |
| MACFCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACFCR; header:ETH_TypeDef.MACFCR |
| MACVLANTR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACVLANTR; header:ETH_TypeDef.MACVLANTR |
| MACRWUFFR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACRWUFFR; header:ETH_TypeDef.MACRWUFFR |
| MACPMTCSR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACPMTCSR; header:ETH_TypeDef.MACPMTCSR |
| MACDBGR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACDBGR; header:ETH_TypeDef.MACDBGR |
| MACSR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACSR; header:ETH_TypeDef.MACSR |
| MACIMR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACIMR; header:ETH_TypeDef.MACIMR |
| MACA0HR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA0HR; header:ETH_TypeDef.MACA0HR |
| MACA0LR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA0LR; header:ETH_TypeDef.MACA0LR |
| MACA1HR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA1HR; header:ETH_TypeDef.MACA1HR |
| MACA1LR | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA1LR; header:ETH_TypeDef.MACA1LR |
| MACA2HR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA2HR; header:ETH_TypeDef.MACA2HR |
| MACA2LR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA2LR; header:ETH_TypeDef.MACA2LR |
| MACA3HR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA3HR; header:ETH_TypeDef.MACA3HR |
| MACA3LR | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MACA3LR; header:ETH_TypeDef.MACA3LR |
| MMCCR | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCCR; header:ETH_TypeDef.MMCCR |
| MMCRIR | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRIR; header:ETH_TypeDef.MMCRIR |
| MMCTIR | 0x108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTIR; header:ETH_TypeDef.MMCTIR |
| MMCRIMR | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRIMR; header:ETH_TypeDef.MMCRIMR |
| MMCTIMR | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTIMR; header:ETH_TypeDef.MMCTIMR |
| MMCTGFSCCR | 0x14C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTGFSCCR; header:ETH_TypeDef.MMCTGFSCCR |
| MMCTGFMSCCR | 0x150 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTGFMSCCR; header:ETH_TypeDef.MMCTGFMSCCR |
| MMCTGFCR | 0x168 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCTGFCR; header:ETH_TypeDef.MMCTGFCR |
| MMCRFCECR | 0x194 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRFCECR; header:ETH_TypeDef.MMCRFCECR |
| MMCRFAECR | 0x198 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRFAECR; header:ETH_TypeDef.MMCRFAECR |
| MMCRGUFCR | 0x1C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.MMCRGUFCR; header:ETH_TypeDef.MMCRGUFCR |
| PTPTSCR | 0x700 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSCR; header:ETH_TypeDef.PTPTSCR |
| PTPSSIR | 0x704 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPSSIR; header:ETH_TypeDef.PTPSSIR |
| PTPTSHR | 0x708 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSHR; header:ETH_TypeDef.PTPTSHR |
| PTPTSLR | 0x70C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSLR; header:ETH_TypeDef.PTPTSLR |
| PTPTSHUR | 0x710 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSHUR; header:ETH_TypeDef.PTPTSHUR |
| PTPTSLUR | 0x714 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSLUR; header:ETH_TypeDef.PTPTSLUR |
| PTPTSAR | 0x718 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSAR; header:ETH_TypeDef.PTPTSAR |
| PTPTTHR | 0x71C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTTHR; header:ETH_TypeDef.PTPTTHR |
| PTPTTLR | 0x720 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTTLR; header:ETH_TypeDef.PTPTTLR |
| PTPTSSR | 0x728 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.PTPTSSR; header:ETH_TypeDef.PTPTSSR |
| DMABMR | 0x1000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMABMR; header:ETH_TypeDef.DMABMR |
| DMATPDR | 0x1004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMATPDR; header:ETH_TypeDef.DMATPDR |
| DMARPDR | 0x1008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMARPDR; header:ETH_TypeDef.DMARPDR |
| DMARDLAR | 0x100C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMARDLAR; header:ETH_TypeDef.DMARDLAR |
| DMATDLAR | 0x1010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMATDLAR; header:ETH_TypeDef.DMATDLAR |
| DMASR | 0x1014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMASR; header:ETH_TypeDef.DMASR |
| DMAOMR | 0x1018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMAOMR; header:ETH_TypeDef.DMAOMR |
| DMAIER | 0x101C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMAIER; header:ETH_TypeDef.DMAIER |
| DMAMFBOCR | 0x1020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMAMFBOCR; header:ETH_TypeDef.DMAMFBOCR |
| DMARSWTR | 0x1024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMARSWTR; header:ETH_TypeDef.DMARSWTR |
| DMACHTDR | 0x1048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACHTDR; header:ETH_TypeDef.DMACHTDR |
| DMACHRDR | 0x104C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACHRDR; header:ETH_TypeDef.DMACHRDR |
| DMACHTBAR | 0x1050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACHTBAR; header:ETH_TypeDef.DMACHTBAR |
| DMACHRBAR | 0x1054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:ETH_TypeDef.DMACHRBAR; header:ETH_TypeDef.DMACHRBAR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MACCR | RE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_RE_Msk; header:ETH_MACCR_RE_Msk |
| MACCR | TE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_TE_Msk; header:ETH_MACCR_TE_Msk |
| MACCR | DC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_DC_Msk; header:ETH_MACCR_DC_Msk |
| MACCR | BL | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_BL_Msk; header:ETH_MACCR_BL_Msk |
| MACCR | APCS | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_APCS_Msk; header:ETH_MACCR_APCS_Msk |
| MACCR | RD | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_RD_Msk; header:ETH_MACCR_RD_Msk |
| MACCR | IPCO | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_IPCO_Msk; header:ETH_MACCR_IPCO_Msk |
| MACCR | DM | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_DM_Msk; header:ETH_MACCR_DM_Msk |
| MACCR | LM | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_LM_Msk; header:ETH_MACCR_LM_Msk |
| MACCR | ROD | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_ROD_Msk; header:ETH_MACCR_ROD_Msk |
| MACCR | FES | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_FES_Msk; header:ETH_MACCR_FES_Msk |
| MACCR | CSD | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_CSD_Msk; header:ETH_MACCR_CSD_Msk |
| MACCR | IFG | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_IFG_Msk; header:ETH_MACCR_IFG_Msk |
| MACCR | JD | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_JD_Msk; header:ETH_MACCR_JD_Msk |
| MACCR | WD | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_WD_Msk; header:ETH_MACCR_WD_Msk |
| MACCR | CSTF | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACCR_CSTF_Msk; header:ETH_MACCR_CSTF_Msk |
| MACFFR | PM | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_PM_Msk; header:ETH_MACFFR_PM_Msk |
| MACFFR | HU | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_HU_Msk; header:ETH_MACFFR_HU_Msk |
| MACFFR | HM | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_HM_Msk; header:ETH_MACFFR_HM_Msk |
| MACFFR | DAIF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_DAIF_Msk; header:ETH_MACFFR_DAIF_Msk |
| MACFFR | PAM | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_PAM_Msk; header:ETH_MACFFR_PAM_Msk |
| MACFFR | BFD | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_BFD_Msk; header:ETH_MACFFR_BFD_Msk |
| MACFFR | PCF | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_PCF_Msk; header:ETH_MACFFR_PCF_Msk |
| MACFFR | SAIF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_SAIF_Msk; header:ETH_MACFFR_SAIF_Msk |
| MACFFR | SAF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_SAF_Msk; header:ETH_MACFFR_SAF_Msk |
| MACFFR | HPF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_HPF_Msk; header:ETH_MACFFR_HPF_Msk |
| MACFFR | RA | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFFR_RA_Msk; header:ETH_MACFFR_RA_Msk |
| MACHTHR | HTH | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACHTHR_HTH_Msk; header:ETH_MACHTHR_HTH_Msk |
| MACHTLR | HTL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACHTLR_HTL_Msk; header:ETH_MACHTLR_HTL_Msk |
| MACMIIAR | MB | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIAR_MB_Msk; header:ETH_MACMIIAR_MB_Msk |
| MACMIIAR | MW | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIAR_MW_Msk; header:ETH_MACMIIAR_MW_Msk |
| MACMIIAR | CR | 4:2 | 0x1C | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIAR_CR_Msk; header:ETH_MACMIIAR_CR_Msk |
| MACMIIAR | MR | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIAR_MR_Msk; header:ETH_MACMIIAR_MR_Msk |
| MACMIIAR | PA | 15:11 | 0xF800 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIAR_PA_Msk; header:ETH_MACMIIAR_PA_Msk |
| MACMIIDR | MD | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACMIIDR_MD_Msk; header:ETH_MACMIIDR_MD_Msk |
| MACFCR | FCBBPA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_FCBBPA_Msk; header:ETH_MACFCR_FCBBPA_Msk |
| MACFCR | TFCE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_TFCE_Msk; header:ETH_MACFCR_TFCE_Msk |
| MACFCR | RFCE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_RFCE_Msk; header:ETH_MACFCR_RFCE_Msk |
| MACFCR | UPFD | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_UPFD_Msk; header:ETH_MACFCR_UPFD_Msk |
| MACFCR | PLT | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_PLT_Msk; header:ETH_MACFCR_PLT_Msk |
| MACFCR | ZQPD | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_ZQPD_Msk; header:ETH_MACFCR_ZQPD_Msk |
| MACFCR | PT | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACFCR_PT_Msk; header:ETH_MACFCR_PT_Msk |
| MACVLANTR | VLANTI | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACVLANTR_VLANTI_Msk; header:ETH_MACVLANTR_VLANTI_Msk |
| MACVLANTR | VLANTC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACVLANTR_VLANTC_Msk; header:ETH_MACVLANTR_VLANTC_Msk |
| MACRWUFFR | D | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACRWUFFR_D_Msk; header:ETH_MACRWUFFR_D_Msk |
| MACPMTCSR | PD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_PD_Msk; header:ETH_MACPMTCSR_PD_Msk |
| MACPMTCSR | MPE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_MPE_Msk; header:ETH_MACPMTCSR_MPE_Msk |
| MACPMTCSR | WFE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_WFE_Msk; header:ETH_MACPMTCSR_WFE_Msk |
| MACPMTCSR | MPR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_MPR_Msk; header:ETH_MACPMTCSR_MPR_Msk |
| MACPMTCSR | WFR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_WFR_Msk; header:ETH_MACPMTCSR_WFR_Msk |
| MACPMTCSR | GU | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_GU_Msk; header:ETH_MACPMTCSR_GU_Msk |
| MACPMTCSR | WFFRPR | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACPMTCSR_WFFRPR_Msk; header:ETH_MACPMTCSR_WFFRPR_Msk |
| MACDBGR | MMRPEA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_MMRPEA_Msk; header:ETH_MACDBGR_MMRPEA_Msk |
| MACDBGR | MSFRWCS | 2:1 | 0x6 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_MSFRWCS_Msk; header:ETH_MACDBGR_MSFRWCS_Msk |
| MACDBGR | RFWRA | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_RFWRA_Msk; header:ETH_MACDBGR_RFWRA_Msk |
| MACDBGR | RFRCS | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_RFRCS_Msk; header:ETH_MACDBGR_RFRCS_Msk |
| MACDBGR | RFFL | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_RFFL_Msk; header:ETH_MACDBGR_RFFL_Msk |
| MACDBGR | MMTEA | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_MMTEA_Msk; header:ETH_MACDBGR_MMTEA_Msk |
| MACDBGR | MTFCS | 18:17 | 0x60000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_MTFCS_Msk; header:ETH_MACDBGR_MTFCS_Msk |
| MACDBGR | MTP | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_MTP_Msk; header:ETH_MACDBGR_MTP_Msk |
| MACDBGR | TFRS | 21:20 | 0x300000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_TFRS_Msk; header:ETH_MACDBGR_TFRS_Msk |
| MACDBGR | TFWA | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_TFWA_Msk; header:ETH_MACDBGR_TFWA_Msk |
| MACDBGR | TFNE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_TFNE_Msk; header:ETH_MACDBGR_TFNE_Msk |
| MACDBGR | TFF | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACDBGR_TFF_Msk; header:ETH_MACDBGR_TFF_Msk |
| MACSR | PMTS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACSR_PMTS_Msk; header:ETH_MACSR_PMTS_Msk |
| MACSR | MMCS | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACSR_MMCS_Msk; header:ETH_MACSR_MMCS_Msk |
| MACSR | MMMCRS | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACSR_MMMCRS_Msk; header:ETH_MACSR_MMMCRS_Msk |
| MACSR | MMCTS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACSR_MMCTS_Msk; header:ETH_MACSR_MMCTS_Msk |
| MACSR | TSTS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACSR_TSTS_Msk; header:ETH_MACSR_TSTS_Msk |
| MACIMR | PMTIM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACIMR_PMTIM_Msk; header:ETH_MACIMR_PMTIM_Msk |
| MACIMR | TSTIM | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACIMR_TSTIM_Msk; header:ETH_MACIMR_TSTIM_Msk |
| MACA0HR | MACA0H | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA0HR_MACA0H_Msk; header:ETH_MACA0HR_MACA0H_Msk |
| MACA0LR | MACA0L | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA0LR_MACA0L_Msk; header:ETH_MACA0LR_MACA0L_Msk |
| MACA1HR | MACA1H | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA1HR_MACA1H_Msk; header:ETH_MACA1HR_MACA1H_Msk |
| MACA1HR | MBC | 29:24 | 0x3F000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA1HR_MBC_Msk; header:ETH_MACA1HR_MBC_Msk |
| MACA1HR | SA | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA1HR_SA_Msk; header:ETH_MACA1HR_SA_Msk |
| MACA1HR | AE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA1HR_AE_Msk; header:ETH_MACA1HR_AE_Msk |
| MACA1LR | MACA1L | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA1LR_MACA1L_Msk; header:ETH_MACA1LR_MACA1L_Msk |
| MACA2HR | MACA2H | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA2HR_MACA2H_Msk; header:ETH_MACA2HR_MACA2H_Msk |
| MACA2HR | MBC | 29:24 | 0x3F000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA2HR_MBC_Msk; header:ETH_MACA2HR_MBC_Msk |
| MACA2HR | SA | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA2HR_SA_Msk; header:ETH_MACA2HR_SA_Msk |
| MACA2HR | AE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA2HR_AE_Msk; header:ETH_MACA2HR_AE_Msk |
| MACA2LR | MACA2L | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA2LR_MACA2L_Msk; header:ETH_MACA2LR_MACA2L_Msk |
| MACA3HR | MACA3H | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA3HR_MACA3H_Msk; header:ETH_MACA3HR_MACA3H_Msk |
| MACA3HR | MBC | 29:24 | 0x3F000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA3HR_MBC_Msk; header:ETH_MACA3HR_MBC_Msk |
| MACA3HR | SA | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA3HR_SA_Msk; header:ETH_MACA3HR_SA_Msk |
| MACA3HR | AE | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA3HR_AE_Msk; header:ETH_MACA3HR_AE_Msk |
| MACA3LR | MACA3L | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MACA3LR_MACA3L_Msk; header:ETH_MACA3LR_MACA3L_Msk |
| MMCCR | CR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_CR_Msk; header:ETH_MMCCR_CR_Msk |
| MMCCR | CSR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_CSR_Msk; header:ETH_MMCCR_CSR_Msk |
| MMCCR | ROR | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_ROR_Msk; header:ETH_MMCCR_ROR_Msk |
| MMCCR | MCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_MCF_Msk; header:ETH_MMCCR_MCF_Msk |
| MMCCR | MCP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_MCP_Msk; header:ETH_MMCCR_MCP_Msk |
| MMCCR | MCFHP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCCR_MCFHP_Msk; header:ETH_MMCCR_MCFHP_Msk |
| MMCRIR | RFCES | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIR_RFCES_Msk; header:ETH_MMCRIR_RFCES_Msk |
| MMCRIR | RFAES | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIR_RFAES_Msk; header:ETH_MMCRIR_RFAES_Msk |
| MMCRIR | RGUFS | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIR_RGUFS_Msk; header:ETH_MMCRIR_RGUFS_Msk |
| MMCTIR | TGFSCS | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIR_TGFSCS_Msk; header:ETH_MMCTIR_TGFSCS_Msk |
| MMCTIR | TGFMSCS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIR_TGFMSCS_Msk; header:ETH_MMCTIR_TGFMSCS_Msk |
| MMCTIR | TGFS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIR_TGFS_Msk; header:ETH_MMCTIR_TGFS_Msk |
| MMCRIMR | RFCEM | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIMR_RFCEM_Msk; header:ETH_MMCRIMR_RFCEM_Msk |
| MMCRIMR | RFAEM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIMR_RFAEM_Msk; header:ETH_MMCRIMR_RFAEM_Msk |
| MMCRIMR | RGUFM | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRIMR_RGUFM_Msk; header:ETH_MMCRIMR_RGUFM_Msk |
| MMCTIMR | TGFSCM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIMR_TGFSCM_Msk; header:ETH_MMCTIMR_TGFSCM_Msk |
| MMCTIMR | TGFMSCM | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIMR_TGFMSCM_Msk; header:ETH_MMCTIMR_TGFMSCM_Msk |
| MMCTIMR | TGFM | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTIMR_TGFM_Msk; header:ETH_MMCTIMR_TGFM_Msk |
| MMCTGFSCCR | TGFSCC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTGFSCCR_TGFSCC_Msk; header:ETH_MMCTGFSCCR_TGFSCC_Msk |
| MMCTGFMSCCR | TGFMSCC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTGFMSCCR_TGFMSCC_Msk; header:ETH_MMCTGFMSCCR_TGFMSCC_Msk |
| MMCTGFCR | TGFC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCTGFCR_TGFC_Msk; header:ETH_MMCTGFCR_TGFC_Msk |
| MMCRFCECR | RFCEC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRFCECR_RFCEC_Msk; header:ETH_MMCRFCECR_RFCEC_Msk |
| MMCRFAECR | RFAEC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRFAECR_RFAEC_Msk; header:ETH_MMCRFAECR_RFAEC_Msk |
| MMCRGUFCR | RGUFC | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_MMCRGUFCR_RGUFC_Msk; header:ETH_MMCRGUFCR_RGUFC_Msk |
| PTPTSCR | TSE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSE_Msk; header:ETH_PTPTSCR_TSE_Msk |
| PTPTSCR | TSFCU | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSFCU_Msk; header:ETH_PTPTSCR_TSFCU_Msk |
| PTPTSCR | TSSTI | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSTI_Msk; header:ETH_PTPTSCR_TSSTI_Msk |
| PTPTSCR | TSSTU | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSTU_Msk; header:ETH_PTPTSCR_TSSTU_Msk |
| PTPTSCR | TSITE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSITE_Msk; header:ETH_PTPTSCR_TSITE_Msk |
| PTPTSCR | TSARU | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSARU_Msk; header:ETH_PTPTSCR_TSARU_Msk |
| PTPTSCR | TSSARFE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSARFE_Msk; header:ETH_PTPTSCR_TSSARFE_Msk |
| PTPTSCR | TSSSR | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSSR_Msk; header:ETH_PTPTSCR_TSSSR_Msk |
| PTPTSCR | TSPTPPSV2E | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSPTPPSV2E_Msk; header:ETH_PTPTSCR_TSPTPPSV2E_Msk |
| PTPTSCR | TSSPTPOEFE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSPTPOEFE_Msk; header:ETH_PTPTSCR_TSSPTPOEFE_Msk |
| PTPTSCR | TSSIPV6FE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSIPV6FE_Msk; header:ETH_PTPTSCR_TSSIPV6FE_Msk |
| PTPTSCR | TSSIPV4FE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSIPV4FE_Msk; header:ETH_PTPTSCR_TSSIPV4FE_Msk |
| PTPTSCR | TSSEME | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSEME_Msk; header:ETH_PTPTSCR_TSSEME_Msk |
| PTPTSCR | TSSMRME | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSSMRME_Msk; header:ETH_PTPTSCR_TSSMRME_Msk |
| PTPTSCR | TSCNT | 17:16 | 0x30000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSCNT_Msk; header:ETH_PTPTSCR_TSCNT_Msk |
| PTPTSCR | TSPFFMAE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSCR_TSPFFMAE_Msk; header:ETH_PTPTSCR_TSPFFMAE_Msk |
| PTPSSIR | STSSI | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPSSIR_STSSI_Msk; header:ETH_PTPSSIR_STSSI_Msk |
| PTPTSHR | STS | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSHR_STS_Msk; header:ETH_PTPTSHR_STS_Msk |
| PTPTSLR | STSS | 30:0 | 0x7FFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSLR_STSS_Msk; header:ETH_PTPTSLR_STSS_Msk |
| PTPTSLR | STPNS | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSLR_STPNS_Msk; header:ETH_PTPTSLR_STPNS_Msk |
| PTPTSHUR | TSUS | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSHUR_TSUS_Msk; header:ETH_PTPTSHUR_TSUS_Msk |
| PTPTSLUR | TSUSS | 30:0 | 0x7FFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSLUR_TSUSS_Msk; header:ETH_PTPTSLUR_TSUSS_Msk |
| PTPTSLUR | TSUPNS | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSLUR_TSUPNS_Msk; header:ETH_PTPTSLUR_TSUPNS_Msk |
| PTPTSAR | TSA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSAR_TSA_Msk; header:ETH_PTPTSAR_TSA_Msk |
| PTPTTHR | TTSH | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTTHR_TTSH_Msk; header:ETH_PTPTTHR_TTSH_Msk |
| PTPTTLR | TTSL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTTLR_TTSL_Msk; header:ETH_PTPTTLR_TTSL_Msk |
| PTPTSSR | TSSO | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSSR_TSSO_Msk; header:ETH_PTPTSSR_TSSO_Msk |
| PTPTSSR | TSTTR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_PTPTSSR_TSTTR_Msk; header:ETH_PTPTSSR_TSTTR_Msk |
| DMABMR | SR | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_SR_Msk; header:ETH_DMABMR_SR_Msk |
| DMABMR | DA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_DA_Msk; header:ETH_DMABMR_DA_Msk |
| DMABMR | DSL | 6:2 | 0x7C | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_DSL_Msk; header:ETH_DMABMR_DSL_Msk |
| DMABMR | EDE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_EDE_Msk; header:ETH_DMABMR_EDE_Msk |
| DMABMR | PBL | 13:8 | 0x3F00 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_PBL_Msk; header:ETH_DMABMR_PBL_Msk |
| DMABMR | RTPR | 15:14 | 0xC000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_RTPR_Msk; header:ETH_DMABMR_RTPR_Msk |
| DMABMR | FB | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_FB_Msk; header:ETH_DMABMR_FB_Msk |
| DMABMR | RDP | 22:17 | 0x7E0000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_RDP_Msk; header:ETH_DMABMR_RDP_Msk |
| DMABMR | USP | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_USP_Msk; header:ETH_DMABMR_USP_Msk |
| DMABMR | FPM | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_FPM_Msk; header:ETH_DMABMR_FPM_Msk |
| DMABMR | AAB | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_AAB_Msk; header:ETH_DMABMR_AAB_Msk |
| DMABMR | MB | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMABMR_MB_Msk; header:ETH_DMABMR_MB_Msk |
| DMATPDR | TPD | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMATPDR_TPD_Msk; header:ETH_DMATPDR_TPD_Msk |
| DMARPDR | RPD | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMARPDR_RPD_Msk; header:ETH_DMARPDR_RPD_Msk |
| DMARDLAR | SRL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMARDLAR_SRL_Msk; header:ETH_DMARDLAR_SRL_Msk |
| DMATDLAR | STL | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMATDLAR_STL_Msk; header:ETH_DMATDLAR_STL_Msk |
| DMASR | TS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TS_Msk; header:ETH_DMASR_TS_Msk |
| DMASR | TPSS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TPSS_Msk; header:ETH_DMASR_TPSS_Msk |
| DMASR | TBUS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TBUS_Msk; header:ETH_DMASR_TBUS_Msk |
| DMASR | TJTS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TJTS_Msk; header:ETH_DMASR_TJTS_Msk |
| DMASR | ROS | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_ROS_Msk; header:ETH_DMASR_ROS_Msk |
| DMASR | TUS | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TUS_Msk; header:ETH_DMASR_TUS_Msk |
| DMASR | RS | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_RS_Msk; header:ETH_DMASR_RS_Msk |
| DMASR | RBUS | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_RBUS_Msk; header:ETH_DMASR_RBUS_Msk |
| DMASR | RPSS | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_RPSS_Msk; header:ETH_DMASR_RPSS_Msk |
| DMASR | RWTS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_RWTS_Msk; header:ETH_DMASR_RWTS_Msk |
| DMASR | ETS | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_ETS_Msk; header:ETH_DMASR_ETS_Msk |
| DMASR | FBES | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_FBES_Msk; header:ETH_DMASR_FBES_Msk |
| DMASR | ERS | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_ERS_Msk; header:ETH_DMASR_ERS_Msk |
| DMASR | AIS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_AIS_Msk; header:ETH_DMASR_AIS_Msk |
| DMASR | NIS | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_NIS_Msk; header:ETH_DMASR_NIS_Msk |
| DMASR | RPS | 19:17 | 0xE0000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_RPS_Msk; header:ETH_DMASR_RPS_Msk |
| DMASR | TPS | 22:20 | 0x700000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TPS_Msk; header:ETH_DMASR_TPS_Msk |
| DMASR | EBS | 25:23 | 0x3800000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_EBS_Msk; header:ETH_DMASR_EBS_Msk |
| DMASR | MMCS | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_MMCS_Msk; header:ETH_DMASR_MMCS_Msk |
| DMASR | PMTS | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_PMTS_Msk; header:ETH_DMASR_PMTS_Msk |
| DMASR | TSTS | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMASR_TSTS_Msk; header:ETH_DMASR_TSTS_Msk |
| DMAOMR | SR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_SR_Msk; header:ETH_DMAOMR_SR_Msk |
| DMAOMR | OSF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_OSF_Msk; header:ETH_DMAOMR_OSF_Msk |
| DMAOMR | RTC | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_RTC_Msk; header:ETH_DMAOMR_RTC_Msk |
| DMAOMR | FUGF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_FUGF_Msk; header:ETH_DMAOMR_FUGF_Msk |
| DMAOMR | FEF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_FEF_Msk; header:ETH_DMAOMR_FEF_Msk |
| DMAOMR | ST | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_ST_Msk; header:ETH_DMAOMR_ST_Msk |
| DMAOMR | TTC | 16:14 | 0x1C000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_TTC_Msk; header:ETH_DMAOMR_TTC_Msk |
| DMAOMR | FTF | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_FTF_Msk; header:ETH_DMAOMR_FTF_Msk |
| DMAOMR | TSF | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_TSF_Msk; header:ETH_DMAOMR_TSF_Msk |
| DMAOMR | DFRF | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_DFRF_Msk; header:ETH_DMAOMR_DFRF_Msk |
| DMAOMR | RSF | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_RSF_Msk; header:ETH_DMAOMR_RSF_Msk |
| DMAOMR | DTCEFD | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAOMR_DTCEFD_Msk; header:ETH_DMAOMR_DTCEFD_Msk |
| DMAIER | TIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_TIE_Msk; header:ETH_DMAIER_TIE_Msk |
| DMAIER | TPSIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_TPSIE_Msk; header:ETH_DMAIER_TPSIE_Msk |
| DMAIER | TBUIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_TBUIE_Msk; header:ETH_DMAIER_TBUIE_Msk |
| DMAIER | TJTIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_TJTIE_Msk; header:ETH_DMAIER_TJTIE_Msk |
| DMAIER | ROIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_ROIE_Msk; header:ETH_DMAIER_ROIE_Msk |
| DMAIER | TUIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_TUIE_Msk; header:ETH_DMAIER_TUIE_Msk |
| DMAIER | RIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_RIE_Msk; header:ETH_DMAIER_RIE_Msk |
| DMAIER | RBUIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_RBUIE_Msk; header:ETH_DMAIER_RBUIE_Msk |
| DMAIER | RPSIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_RPSIE_Msk; header:ETH_DMAIER_RPSIE_Msk |
| DMAIER | RWTIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_RWTIE_Msk; header:ETH_DMAIER_RWTIE_Msk |
| DMAIER | ETIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_ETIE_Msk; header:ETH_DMAIER_ETIE_Msk |
| DMAIER | FBEIE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_FBEIE_Msk; header:ETH_DMAIER_FBEIE_Msk |
| DMAIER | ERIE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_ERIE_Msk; header:ETH_DMAIER_ERIE_Msk |
| DMAIER | AISE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_AISE_Msk; header:ETH_DMAIER_AISE_Msk |
| DMAIER | NISE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAIER_NISE_Msk; header:ETH_DMAIER_NISE_Msk |
| DMAMFBOCR | MFC | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAMFBOCR_MFC_Msk; header:ETH_DMAMFBOCR_MFC_Msk |
| DMAMFBOCR | OMFC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAMFBOCR_OMFC_Msk; header:ETH_DMAMFBOCR_OMFC_Msk |
| DMAMFBOCR | MFA | 27:17 | 0xFFE0000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAMFBOCR_MFA_Msk; header:ETH_DMAMFBOCR_MFA_Msk |
| DMAMFBOCR | OFOC | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:ETH_DMAMFBOCR_OFOC_Msk; header:ETH_DMAMFBOCR_OFOC_Msk |
| DMACHTDR | HTDAP | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMACHTDR_HTDAP_Msk; header:ETH_DMACHTDR_HTDAP_Msk |
| DMACHRDR | HRDAP | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMACHRDR_HRDAP_Msk; header:ETH_DMACHRDR_HRDAP_Msk |
| DMACHTBAR | HTBAP | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMACHTBAR_HTBAP_Msk; header:ETH_DMACHTBAR_HTBAP_Msk |
| DMACHRBAR | HRBAP | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:ETH_DMACHRBAR_HRBAP_Msk; header:ETH_DMACHRBAR_HRBAP_Msk |

## Operating semantics unavailable

**eth: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
