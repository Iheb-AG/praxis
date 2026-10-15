# CAN — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CAN1 | 0x40006400 | Not asserted | Not asserted | header:CAN1_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.MCR |
| MSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.MSR |
| TSR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.TSR |
| RF0R | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.RF0R |
| RF1R | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.RF1R |
| IER | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.IER |
| ESR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.ESR |
| BTR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.BTR |
| sTxMailBox_0__TIR | 0x180 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[0].TIR |
| sTxMailBox_0__TDTR | 0x184 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[0].TDTR |
| sTxMailBox_0__TDLR | 0x188 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[0].TDLR |
| sTxMailBox_0__TDHR | 0x18C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[0].TDHR |
| sTxMailBox_1__TIR | 0x190 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TIR |
| sTxMailBox_1__TDTR | 0x194 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDTR |
| sTxMailBox_1__TDLR | 0x198 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDLR |
| sTxMailBox_1__TDHR | 0x19C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDHR |
| sTxMailBox_2__TIR | 0x1A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TIR |
| sTxMailBox_2__TDTR | 0x1A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDTR |
| sTxMailBox_2__TDLR | 0x1A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDLR |
| sTxMailBox_2__TDHR | 0x1AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDHR |
| sFIFOMailBox_0__RIR | 0x1B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[0].RIR |
| sFIFOMailBox_0__RDTR | 0x1B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[0].RDTR |
| sFIFOMailBox_0__RDLR | 0x1B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[0].RDLR |
| sFIFOMailBox_0__RDHR | 0x1BC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[0].RDHR |
| sFIFOMailBox_1__RIR | 0x1C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RIR |
| sFIFOMailBox_1__RDTR | 0x1C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDTR |
| sFIFOMailBox_1__RDLR | 0x1C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDLR |
| sFIFOMailBox_1__RDHR | 0x1CC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDHR |
| FMR | 0x200 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.FMR |
| FM1R | 0x204 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.FM1R |
| FS1R | 0x20C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.FS1R |
| FFA1R | 0x214 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.FFA1R |
| FA1R | 0x21C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.FA1R |
| sFilterRegister_0__FR1 | 0x240 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[0].FR1 |
| sFilterRegister_0__FR2 | 0x244 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[0].FR2 |
| sFilterRegister_1__FR1 | 0x248 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[1].FR1 |
| sFilterRegister_1__FR2 | 0x24C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[1].FR2 |
| sFilterRegister_2__FR1 | 0x250 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[2].FR1 |
| sFilterRegister_2__FR2 | 0x254 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[2].FR2 |
| sFilterRegister_3__FR1 | 0x258 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[3].FR1 |
| sFilterRegister_3__FR2 | 0x25C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[3].FR2 |
| sFilterRegister_4__FR1 | 0x260 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[4].FR1 |
| sFilterRegister_4__FR2 | 0x264 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[4].FR2 |
| sFilterRegister_5__FR1 | 0x268 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[5].FR1 |
| sFilterRegister_5__FR2 | 0x26C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[5].FR2 |
| sFilterRegister_6__FR1 | 0x270 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[6].FR1 |
| sFilterRegister_6__FR2 | 0x274 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[6].FR2 |
| sFilterRegister_7__FR1 | 0x278 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[7].FR1 |
| sFilterRegister_7__FR2 | 0x27C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[7].FR2 |
| sFilterRegister_8__FR1 | 0x280 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[8].FR1 |
| sFilterRegister_8__FR2 | 0x284 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[8].FR2 |
| sFilterRegister_9__FR1 | 0x288 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[9].FR1 |
| sFilterRegister_9__FR2 | 0x28C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[9].FR2 |
| sFilterRegister_10__FR1 | 0x290 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[10].FR1 |
| sFilterRegister_10__FR2 | 0x294 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[10].FR2 |
| sFilterRegister_11__FR1 | 0x298 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[11].FR1 |
| sFilterRegister_11__FR2 | 0x29C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[11].FR2 |
| sFilterRegister_12__FR1 | 0x2A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[12].FR1 |
| sFilterRegister_12__FR2 | 0x2A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[12].FR2 |
| sFilterRegister_13__FR1 | 0x2A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[13].FR1 |
| sFilterRegister_13__FR2 | 0x2AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[13].FR2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MCR | INRQ | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_INRQ_Msk |
| MCR | SLEEP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_SLEEP_Msk |
| MCR | TXFP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_TXFP_Msk |
| MCR | RFLM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_RFLM_Msk |
| MCR | NART | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_NART_Msk |
| MCR | AWUM | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_AWUM_Msk |
| MCR | ABOM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_ABOM_Msk |
| MCR | TTCM | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_TTCM_Msk |
| MCR | RESET | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_RESET_Msk |
| MCR | DBF | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:CAN_MCR_DBF_Msk |
| MSR | INAK | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_INAK_Msk |
| MSR | SLAK | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_SLAK_Msk |
| MSR | ERRI | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_ERRI_Msk |
| MSR | WKUI | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_WKUI_Msk |
| MSR | SLAKI | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_SLAKI_Msk |
| MSR | TXM | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_TXM_Msk |
| MSR | RXM | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_RXM_Msk |
| MSR | SAMP | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_SAMP_Msk |
| MSR | RX | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:CAN_MSR_RX_Msk |
| TSR | RQCP0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_RQCP0_Msk |
| TSR | TXOK0 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TXOK0_Msk |
| TSR | ALST0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ALST0_Msk |
| TSR | TERR0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TERR0_Msk |
| TSR | ABRQ0 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ABRQ0_Msk |
| TSR | RQCP1 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_RQCP1_Msk |
| TSR | TXOK1 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TXOK1_Msk |
| TSR | ALST1 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ALST1_Msk |
| TSR | TERR1 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TERR1_Msk |
| TSR | ABRQ1 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ABRQ1_Msk |
| TSR | RQCP2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_RQCP2_Msk |
| TSR | TXOK2 | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TXOK2_Msk |
| TSR | ALST2 | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ALST2_Msk |
| TSR | TERR2 | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TERR2_Msk |
| TSR | ABRQ2 | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_ABRQ2_Msk |
| TSR | CODE | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_CODE_Msk |
| TSR | TME | 28:26 | 0x1C000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_TME_Msk |
| TSR | LOW | 31:29 | 0xE0000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_TSR_LOW_Msk |
| RF0R | FMP0 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF0R_FMP0_Msk |
| RF0R | FULL0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF0R_FULL0_Msk |
| RF0R | FOVR0 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF0R_FOVR0_Msk |
| RF0R | RFOM0 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF0R_RFOM0_Msk |
| RF1R | FMP1 | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF1R_FMP1_Msk |
| RF1R | FULL1 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF1R_FULL1_Msk |
| RF1R | FOVR1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF1R_FOVR1_Msk |
| RF1R | RFOM1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CAN_RF1R_RFOM1_Msk |
| IER | TMEIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_TMEIE_Msk |
| IER | FMPIE0 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FMPIE0_Msk |
| IER | FFIE0 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FFIE0_Msk |
| IER | FOVIE0 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FOVIE0_Msk |
| IER | FMPIE1 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FMPIE1_Msk |
| IER | FFIE1 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FFIE1_Msk |
| IER | FOVIE1 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_FOVIE1_Msk |
| IER | EWGIE | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_EWGIE_Msk |
| IER | EPVIE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_EPVIE_Msk |
| IER | BOFIE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_BOFIE_Msk |
| IER | LECIE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_LECIE_Msk |
| IER | ERRIE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_ERRIE_Msk |
| IER | WKUIE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_WKUIE_Msk |
| IER | SLKIE | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:CAN_IER_SLKIE_Msk |
| ESR | EWGF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_EWGF_Msk |
| ESR | EPVF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_EPVF_Msk |
| ESR | BOFF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_BOFF_Msk |
| ESR | LEC | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_LEC_Msk |
| ESR | TEC | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_TEC_Msk |
| ESR | REC | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_ESR_REC_Msk |
| BTR | BRP | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_BRP_Msk |
| BTR | TS1 | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_TS1_Msk |
| BTR | TS2 | 22:20 | 0x700000 | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_TS2_Msk |
| BTR | SJW | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_SJW_Msk |
| BTR | LBKM | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_LBKM_Msk |
| BTR | SILM | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:CAN_BTR_SILM_Msk |
| FMR | FINIT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:CAN_FMR_FINIT_Msk |
| FMR | CAN2SB | 13:8 | 0x3F00 | Declaration only; encoding requires reviewed semantics. | header:CAN_FMR_CAN2SB_Msk |
| FM1R | FBM | 13:0 | 0x3FFF | Declaration only; encoding requires reviewed semantics. | header:CAN_FM1R_FBM_Msk |
| FS1R | FSC | 13:0 | 0x3FFF | Declaration only; encoding requires reviewed semantics. | header:CAN_FS1R_FSC_Msk |
| FFA1R | FFA | 13:0 | 0x3FFF | Declaration only; encoding requires reviewed semantics. | header:CAN_FFA1R_FFA_Msk |
| FA1R | FACT | 13:0 | 0x3FFF | Declaration only; encoding requires reviewed semantics. | header:CAN_FA1R_FACT_Msk |

## Operating semantics unavailable

**can: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
