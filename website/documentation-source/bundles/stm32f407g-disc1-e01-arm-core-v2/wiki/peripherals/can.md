# CAN — CAN1 silent loopback and FIFO0 interrupt subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]], [[peripherals/nvic]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CAN1 | 0x40006400 | APB1 | PCLK1=42MHz under reviewed owned-startup recipe | header:CAN1_BASE; rm_can_1087:page:1087 |
| CAN2 | 0x40006800 | Not asserted | Not asserted outside reviewed workflow | header:CAN2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MCR | 0x000 | 32 | — | mixed | 0x10002 | Request initialization with INRQ=1 and SLEEP=0; wait INAK. Bounded INAK/SLAK checks required. NART=1 prevents automatic retransmission; RFLM=1 locks FIFO on overrun. Preserve DBF reset setting. RESET command is outside this mode. | header:CAN_TypeDef.MCR; header:CAN_TypeDef.MCR; rm_can_1090:page:1090 | 32 |
| MSR | 0x004 | 32 | — | mixed | 0xC02 | INAK/SLAK and mode signals are RO; ERRI/WKUI/SLAKI are W1C. Poll acknowledgements without clearing diagnostics. RX/SAMP may reflect pin state and cannot be compared to a whole-register reset literal. | header:CAN_TypeDef.MSR; header:CAN_TypeDef.MSR; rm_can_1092:page:1092 | 32 |
| TSR | 0x008 | 32 | — | mixed | 0x1C000000 | Mixed RO state, W1C completion and abort commands. Literal RQCP0 clears TXOK0/ALST0/TERR0 together. Preserve failures; acknowledge only validated success. Never RMW status or abort another mailbox. | header:CAN_TypeDef.TSR; header:CAN_TypeDef.TSR; rm_can_1093:page:1093 | 32 |
| RF0R | 0x00C | 32 | — | mixed | 0x0 | FMP0 is RO count; FULL0/FOVR0 are W1C; RFOM0 releases oldest message and clears in hardware. Read all four mailbox words before literal RFOM0; never RMW (would clear diagnostics). Bounded release acknowledgement. | header:CAN_TypeDef.RF0R; header:CAN_TypeDef.RF0R; rm_can_1095:page:1095 | 32 |
| RF1R | 0x010 | 32 | — | mixed | 0x0 | FIFO1 unused and must stay empty; flag semantics match FIFO0. This mode never releases or clears FIFO1. | header:CAN_TypeDef.RF1R; header:CAN_TypeDef.RF1R; rm_can_1096:page:1096 | 32 |
| IER | 0x014 | 32 | — | RW | 0x0 | Keep0 throughout initialization. Only FMPIE0 is enabled after handler/state/source preparation; disable source before owned NVIC cleanup. | header:CAN_TypeDef.IER; header:CAN_TypeDef.IER; rm_can_1096:page:1096 | 32 |
| ESR | 0x018 | 32 | — | mixed | 0x0 | Flags/counters RO; LEC software-writable (111 software marker). This mode reads only and preserves diagnostics. Any error/count fails; no automatic bus-off recovery. | header:CAN_TypeDef.ESR; header:CAN_TypeDef.ESR; rm_can_1098:page:1098 | 32 |
| BTR | 0x01C | 32 | — | RW | 0x1230000 | Read/write only in acknowledged initialization mode. SILM=LBKM=1 disconnects CANRX internally and holds CANTX recessive. BRP=5,TS1=10,TS2=1,SJW=0 gives nominal500kbit/s at42MHz PCLK1. | header:CAN_TypeDef.BTR; header:CAN_TypeDef.BTR; rm_can_1099:page:1099 | 32 |
| sTxMailBox_0__TIR | 0x180 | 32 | — | RW | not asserted | Only write mailbox0 while TME0=1. All reset data unspecified, except TXRQ=0. Program identifier/DLC/data fully, then set TXRQ last. Never modify a pending mailbox. | header:CAN_TypeDef.sTxMailBox[0].TIR; header:CAN_TypeDef.sTxMailBox[0].TIR; rm_can_1100:page:1100 | 32 |
| sTxMailBox_0__TDTR | 0x184 | 32 | — | RW | not asserted | Only write mailbox0 while TME0=1. All reset data unspecified, except TXRQ=0. Program identifier/DLC/data fully, then set TXRQ last. Never modify a pending mailbox. | header:CAN_TypeDef.sTxMailBox[0].TDTR; header:CAN_TypeDef.sTxMailBox[0].TDTR; rm_can_1101:page:1101 | 32 |
| sTxMailBox_0__TDLR | 0x188 | 32 | — | RW | not asserted | Only write mailbox0 while TME0=1. All reset data unspecified, except TXRQ=0. Program identifier/DLC/data fully, then set TXRQ last. Never modify a pending mailbox. | header:CAN_TypeDef.sTxMailBox[0].TDLR; header:CAN_TypeDef.sTxMailBox[0].TDLR; rm_can_1101:page:1101 | 32 |
| sTxMailBox_0__TDHR | 0x18C | 32 | — | RW | not asserted | Only write mailbox0 while TME0=1. All reset data unspecified, except TXRQ=0. Program identifier/DLC/data fully, then set TXRQ last. Never modify a pending mailbox. | header:CAN_TypeDef.sTxMailBox[0].TDHR; header:CAN_TypeDef.sTxMailBox[0].TDHR; rm_can_1102:page:1102 | 32 |
| sTxMailBox_1__TIR | 0x190 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TIR | not asserted |
| sTxMailBox_1__TDTR | 0x194 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDTR | not asserted |
| sTxMailBox_1__TDLR | 0x198 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDLR | not asserted |
| sTxMailBox_1__TDHR | 0x19C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[1].TDHR | not asserted |
| sTxMailBox_2__TIR | 0x1A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TIR | not asserted |
| sTxMailBox_2__TDTR | 0x1A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDTR | not asserted |
| sTxMailBox_2__TDLR | 0x1A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDLR | not asserted |
| sTxMailBox_2__TDHR | 0x1AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sTxMailBox[2].TDHR | not asserted |
| sFIFOMailBox_0__RIR | 0x1B0 | 32 | — | RO | not asserted | Read-only FIFO0 output view, meaningful only with FMP0&gt;0. Reset unspecified; read identifier,length and both data words before releasing the oldest frame. | header:CAN_TypeDef.sFIFOMailBox[0].RIR; header:CAN_TypeDef.sFIFOMailBox[0].RIR; rm_can_1102:page:1102 | 32 |
| sFIFOMailBox_0__RDTR | 0x1B4 | 32 | — | RO | not asserted | Read-only FIFO0 output view, meaningful only with FMP0&gt;0. Reset unspecified; read identifier,length and both data words before releasing the oldest frame. | header:CAN_TypeDef.sFIFOMailBox[0].RDTR; header:CAN_TypeDef.sFIFOMailBox[0].RDTR; rm_can_1103:page:1103 | 32 |
| sFIFOMailBox_0__RDLR | 0x1B8 | 32 | — | RO | not asserted | Read-only FIFO0 output view, meaningful only with FMP0&gt;0. Reset unspecified; read identifier,length and both data words before releasing the oldest frame. | header:CAN_TypeDef.sFIFOMailBox[0].RDLR; header:CAN_TypeDef.sFIFOMailBox[0].RDLR; rm_can_1103:page:1103 | 32 |
| sFIFOMailBox_0__RDHR | 0x1BC | 32 | — | RO | not asserted | Read-only FIFO0 output view, meaningful only with FMP0&gt;0. Reset unspecified; read identifier,length and both data words before releasing the oldest frame. | header:CAN_TypeDef.sFIFOMailBox[0].RDHR; header:CAN_TypeDef.sFIFOMailBox[0].RDHR; rm_can_1104:page:1104 | 32 |
| sFIFOMailBox_1__RIR | 0x1C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RIR | not asserted |
| sFIFOMailBox_1__RDTR | 0x1C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDTR | not asserted |
| sFIFOMailBox_1__RDLR | 0x1C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDLR | not asserted |
| sFIFOMailBox_1__RDHR | 0x1CC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFIFOMailBox[1].RDHR | not asserted |
| FMR | 0x200 | 32 | — | RW | not asserted | Filter registers exist only in CAN1. FINIT gates filter configuration and suppresses reception. Keep CAN2SB=14 and preserve all other bits read from hardware. p1104 printed full reset includes reserved values omitted by p1111: whole reset remains unasserted. | header:CAN_TypeDef.FMR; header:CAN_TypeDef.FMR; rm_can_1104:page:1104 | 32 |
| FM1R | 0x204 | 32 | — | RW | 0x0 | Write only with FINIT=1; bank0 identifier-list mode, all other banks disabled. Preserve reserved reset bits. | header:CAN_TypeDef.FM1R; header:CAN_TypeDef.FM1R; rm_can_1105:page:1105 | 32 |
| FS1R | 0x20C | 32 | — | RW | 0x0 | Write only with FINIT=1; bank0 single32-bit scale. Other banks unused. | header:CAN_TypeDef.FS1R; header:CAN_TypeDef.FS1R; rm_can_1106:page:1106 | 32 |
| FFA1R | 0x214 | 32 | — | RW | 0x0 | Write only with FINIT=1; bank0 assigned FIFO0. No FIFO1 traffic. | header:CAN_TypeDef.FFA1R; header:CAN_TypeDef.FFA1R; rm_can_1106:page:1106 | 32 |
| FA1R | 0x21C | 32 | — | RW | 0x0 | Activate only bank0 after scale/mode/ID programming. Filter-value writes require inactive bank or FINIT=1. | header:CAN_TypeDef.FA1R; header:CAN_TypeDef.FA1R; rm_can_1107:page:1107 | 32 |
| sFilterRegister_0__FR1 | 0x240 | 32 | — | RW | not asserted | Filter bank0 identifier-list entry: standard ID occupies31:21, IDE/RTR and remaining bits zero. Write only with bank inactive or FINIT=1; reset data unspecified. | header:CAN_TypeDef.sFilterRegister[0].FR1; header:CAN_TypeDef.sFilterRegister[0].FR1; rm_can_1107:page:1107 | 32 |
| sFilterRegister_0__FR2 | 0x244 | 32 | — | RW | not asserted | Filter bank0 identifier-list entry: standard ID occupies31:21, IDE/RTR and remaining bits zero. Write only with bank inactive or FINIT=1; reset data unspecified. | header:CAN_TypeDef.sFilterRegister[0].FR2; header:CAN_TypeDef.sFilterRegister[0].FR2; rm_can_1107:page:1107 | 32 |
| sFilterRegister_1__FR1 | 0x248 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[1].FR1 | not asserted |
| sFilterRegister_1__FR2 | 0x24C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[1].FR2 | not asserted |
| sFilterRegister_2__FR1 | 0x250 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[2].FR1 | not asserted |
| sFilterRegister_2__FR2 | 0x254 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[2].FR2 | not asserted |
| sFilterRegister_3__FR1 | 0x258 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[3].FR1 | not asserted |
| sFilterRegister_3__FR2 | 0x25C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[3].FR2 | not asserted |
| sFilterRegister_4__FR1 | 0x260 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[4].FR1 | not asserted |
| sFilterRegister_4__FR2 | 0x264 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[4].FR2 | not asserted |
| sFilterRegister_5__FR1 | 0x268 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[5].FR1 | not asserted |
| sFilterRegister_5__FR2 | 0x26C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[5].FR2 | not asserted |
| sFilterRegister_6__FR1 | 0x270 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[6].FR1 | not asserted |
| sFilterRegister_6__FR2 | 0x274 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[6].FR2 | not asserted |
| sFilterRegister_7__FR1 | 0x278 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[7].FR1 | not asserted |
| sFilterRegister_7__FR2 | 0x27C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[7].FR2 | not asserted |
| sFilterRegister_8__FR1 | 0x280 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[8].FR1 | not asserted |
| sFilterRegister_8__FR2 | 0x284 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[8].FR2 | not asserted |
| sFilterRegister_9__FR1 | 0x288 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[9].FR1 | not asserted |
| sFilterRegister_9__FR2 | 0x28C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[9].FR2 | not asserted |
| sFilterRegister_10__FR1 | 0x290 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[10].FR1 | not asserted |
| sFilterRegister_10__FR2 | 0x294 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[10].FR2 | not asserted |
| sFilterRegister_11__FR1 | 0x298 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[11].FR1 | not asserted |
| sFilterRegister_11__FR2 | 0x29C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[11].FR2 | not asserted |
| sFilterRegister_12__FR1 | 0x2A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[12].FR1 | not asserted |
| sFilterRegister_12__FR2 | 0x2A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[12].FR2 | not asserted |
| sFilterRegister_13__FR1 | 0x2A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[13].FR1 | not asserted |
| sFilterRegister_13__FR2 | 0x2AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[13].FR2 | not asserted |
| sFilterRegister_14__FR1 | 0x2B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[14].FR1 | not asserted |
| sFilterRegister_14__FR2 | 0x2B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[14].FR2 | not asserted |
| sFilterRegister_15__FR1 | 0x2B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[15].FR1 | not asserted |
| sFilterRegister_15__FR2 | 0x2BC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[15].FR2 | not asserted |
| sFilterRegister_16__FR1 | 0x2C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[16].FR1 | not asserted |
| sFilterRegister_16__FR2 | 0x2C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[16].FR2 | not asserted |
| sFilterRegister_17__FR1 | 0x2C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[17].FR1 | not asserted |
| sFilterRegister_17__FR2 | 0x2CC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[17].FR2 | not asserted |
| sFilterRegister_18__FR1 | 0x2D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[18].FR1 | not asserted |
| sFilterRegister_18__FR2 | 0x2D4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[18].FR2 | not asserted |
| sFilterRegister_19__FR1 | 0x2D8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[19].FR1 | not asserted |
| sFilterRegister_19__FR2 | 0x2DC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[19].FR2 | not asserted |
| sFilterRegister_20__FR1 | 0x2E0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[20].FR1 | not asserted |
| sFilterRegister_20__FR2 | 0x2E4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[20].FR2 | not asserted |
| sFilterRegister_21__FR1 | 0x2E8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[21].FR1 | not asserted |
| sFilterRegister_21__FR2 | 0x2EC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[21].FR2 | not asserted |
| sFilterRegister_22__FR1 | 0x2F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[22].FR1 | not asserted |
| sFilterRegister_22__FR2 | 0x2F4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[22].FR2 | not asserted |
| sFilterRegister_23__FR1 | 0x2F8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[23].FR1 | not asserted |
| sFilterRegister_23__FR2 | 0x2FC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[23].FR2 | not asserted |
| sFilterRegister_24__FR1 | 0x300 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[24].FR1 | not asserted |
| sFilterRegister_24__FR2 | 0x304 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[24].FR2 | not asserted |
| sFilterRegister_25__FR1 | 0x308 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[25].FR1 | not asserted |
| sFilterRegister_25__FR2 | 0x30C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[25].FR2 | not asserted |
| sFilterRegister_26__FR1 | 0x310 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[26].FR1 | not asserted |
| sFilterRegister_26__FR2 | 0x314 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[26].FR2 | not asserted |
| sFilterRegister_27__FR1 | 0x318 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[27].FR1 | not asserted |
| sFilterRegister_27__FR2 | 0x31C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:CAN_TypeDef.sFilterRegister[27].FR2 | not asserted |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| MCR | INRQ | 0:0 | 0x1 | 1 requests init; wait INAK before BTR/filter setup; clear then wait INAK/SLAK0 before requests. | header:CAN_MCR_INRQ_Msk; header:CAN_MCR_INRQ_Msk; rm_can_1092:page:1092 |
| MCR | SLEEP | 1:1 | 0x2 | Reset1; clear when requesting initialization from sleep. | header:CAN_MCR_SLEEP_Msk; header:CAN_MCR_SLEEP_Msk; rm_can_1091:page:1091 |
| MCR | TXFP | 2:2 | 0x4 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_MCR_TXFP_Msk; header:CAN_MCR_TXFP_Msk; rm_can_1091:page:1091 |
| MCR | RFLM | 3:3 | 0x8 | 1 locks FIFO on overrun; additional frame discarded. | header:CAN_MCR_RFLM_Msk; header:CAN_MCR_RFLM_Msk; rm_can_1091:page:1091 |
| MCR | NART | 4:4 | 0x10 | 1 disables automatic retransmission; one attempt per request. | header:CAN_MCR_NART_Msk; header:CAN_MCR_NART_Msk; rm_can_1091:page:1091 |
| MCR | AWUM | 5:5 | 0x20 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_MCR_AWUM_Msk; header:CAN_MCR_AWUM_Msk; rm_can_1091:page:1091 |
| MCR | ABOM | 6:6 | 0x40 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_MCR_ABOM_Msk; header:CAN_MCR_ABOM_Msk; rm_can_1091:page:1091 |
| MCR | TTCM | 7:7 | 0x80 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_MCR_TTCM_Msk; header:CAN_MCR_TTCM_Msk; rm_can_1091:page:1091 |
| MCR | RESET | 15:15 | 0x8000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_MCR_RESET_Msk; header:CAN_MCR_RESET_Msk; rm_can_1090:page:1090 |
| MCR | DBF | 16:16 | 0x10000 | Reset1 freezes CAN reception/transmission during debug; no debug timing claim. | header:CAN_MCR_DBF_Msk; header:CAN_MCR_DBF_Msk; rm_can_1090:page:1090 |
| MSR | INAK | 0:0 | 0x1 | Read-only mode/line state. | header:CAN_MSR_INAK_Msk; header:CAN_MSR_INAK_Msk; rm_can_1092:page:1092 |
| MSR | SLAK | 1:1 | 0x2 | Read-only mode/line state. | header:CAN_MSR_SLAK_Msk; header:CAN_MSR_SLAK_Msk; rm_can_1092:page:1092 |
| MSR | ERRI | 2:2 | 0x4 | W1C interrupt diagnostic; this contract does not clear it. | header:CAN_MSR_ERRI_Msk; header:CAN_MSR_ERRI_Msk; rm_can_1092:page:1092 |
| MSR | WKUI | 3:3 | 0x8 | W1C interrupt diagnostic; this contract does not clear it. | header:CAN_MSR_WKUI_Msk; header:CAN_MSR_WKUI_Msk; rm_can_1092:page:1092 |
| MSR | SLAKI | 4:4 | 0x10 | W1C interrupt diagnostic; this contract does not clear it. | header:CAN_MSR_SLAKI_Msk; header:CAN_MSR_SLAKI_Msk; rm_can_1092:page:1092 |
| MSR | TXM | 8:8 | 0x100 | Read-only mode/line state. | header:CAN_MSR_TXM_Msk; header:CAN_MSR_TXM_Msk; rm_can_1092:page:1092 |
| MSR | RXM | 9:9 | 0x200 | Read-only mode/line state. | header:CAN_MSR_RXM_Msk; header:CAN_MSR_RXM_Msk; rm_can_1092:page:1092 |
| MSR | SAMP | 10:10 | 0x400 | Read-only mode/line state. | header:CAN_MSR_SAMP_Msk; header:CAN_MSR_SAMP_Msk; rm_can_1092:page:1092 |
| MSR | RX | 11:11 | 0x800 | Read-only mode/line state. | header:CAN_MSR_RX_Msk; header:CAN_MSR_RX_Msk; rm_can_1092:page:1092 |
| TSR | RQCP0 | 0:0 | 0x1 | W1C request-complete: writing1 clears TXOK0/ALST0/TERR0 together. | header:CAN_TSR_RQCP0_Msk; header:CAN_TSR_RQCP0_Msk; rm_can_1095:page:1095 |
| TSR | TXOK0 | 1:1 | 0x2 | Successful previous mailbox0 attempt; require RQCP0 and TME0 too. | header:CAN_TSR_TXOK0_Msk; header:CAN_TSR_TXOK0_Msk; rm_can_1095:page:1095 |
| TSR | ALST0 | 2:2 | 0x4 | Previous mailbox0 arbitration loss; failure takes priority over success. | header:CAN_TSR_ALST0_Msk; header:CAN_TSR_ALST0_Msk; rm_can_1095:page:1095 |
| TSR | TERR0 | 3:3 | 0x8 | Previous mailbox0 transmission error; preserve on failure. | header:CAN_TSR_TERR0_Msk; header:CAN_TSR_TERR0_Msk; rm_can_1095:page:1095 |
| TSR | ABRQ0 | 7:7 | 0x80 | Write1 abort request; hardware clears when empty. Recovery beyond this contract. | header:CAN_TSR_ABRQ0_Msk; header:CAN_TSR_ABRQ0_Msk; rm_can_1095:page:1095 |
| TSR | RQCP1 | 8:8 | 0x100 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_RQCP1_Msk; header:CAN_TSR_RQCP1_Msk; rm_can_1093:page:1093 |
| TSR | TXOK1 | 9:9 | 0x200 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_TXOK1_Msk; header:CAN_TSR_TXOK1_Msk; rm_can_1093:page:1093 |
| TSR | ALST1 | 10:10 | 0x400 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_ALST1_Msk; header:CAN_TSR_ALST1_Msk; rm_can_1093:page:1093 |
| TSR | TERR1 | 11:11 | 0x800 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_TERR1_Msk; header:CAN_TSR_TERR1_Msk; rm_can_1093:page:1093 |
| TSR | ABRQ1 | 15:15 | 0x8000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_ABRQ1_Msk; header:CAN_TSR_ABRQ1_Msk; rm_can_1093:page:1093 |
| TSR | RQCP2 | 16:16 | 0x10000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_RQCP2_Msk; header:CAN_TSR_RQCP2_Msk; rm_can_1093:page:1093 |
| TSR | TXOK2 | 17:17 | 0x20000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_TXOK2_Msk; header:CAN_TSR_TXOK2_Msk; rm_can_1093:page:1093 |
| TSR | ALST2 | 18:18 | 0x40000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_ALST2_Msk; header:CAN_TSR_ALST2_Msk; rm_can_1093:page:1093 |
| TSR | TERR2 | 19:19 | 0x80000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_TERR2_Msk; header:CAN_TSR_TERR2_Msk; rm_can_1093:page:1093 |
| TSR | ABRQ2 | 23:23 | 0x800000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_ABRQ2_Msk; header:CAN_TSR_ABRQ2_Msk; rm_can_1093:page:1093 |
| TSR | CODE | 25:24 | 0x3000000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_CODE_Msk; header:CAN_TSR_CODE_Msk; rm_can_1093:page:1093 |
| TSR | TME | 28:26 | 0x1C000000 | Three RO empty bits at28:26. All must be1 before exclusive mailbox0 staging. | header:CAN_TSR_TME_Msk; header:CAN_TSR_TME_Msk; rm_can_1093:page:1093 |
| TSR | LOW | 31:29 | 0xE0000000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_TSR_LOW_Msk; header:CAN_TSR_LOW_Msk; rm_can_1093:page:1093 |
| RF0R | FMP0 | 1:0 | 0x3 | RO pending count0..3; this one-shot expects exactly1 before reading. | header:CAN_RF0R_FMP0_Msk; header:CAN_RF0R_FMP0_Msk; rm_can_1095:page:1095 |
| RF0R | FULL0 | 3:3 | 0x8 | W1C FIFO-full flag; treated as failure, retained. | header:CAN_RF0R_FULL0_Msk; header:CAN_RF0R_FULL0_Msk; rm_can_1095:page:1095 |
| RF0R | FOVR0 | 4:4 | 0x10 | W1C overrun diagnostic; retained on failure. | header:CAN_RF0R_FOVR0_Msk; header:CAN_RF0R_FOVR0_Msk; rm_can_1095:page:1095 |
| RF0R | RFOM0 | 5:5 | 0x20 | Write1 releases oldest mailbox, auto-cleared. Literal write only after complete read. | header:CAN_RF0R_RFOM0_Msk; header:CAN_RF0R_RFOM0_Msk; rm_can_1095:page:1095 |
| RF1R | FMP1 | 1:0 | 0x3 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_RF1R_FMP1_Msk; header:CAN_RF1R_FMP1_Msk; rm_can_1096:page:1096 |
| RF1R | FULL1 | 3:3 | 0x8 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_RF1R_FULL1_Msk; header:CAN_RF1R_FULL1_Msk; rm_can_1096:page:1096 |
| RF1R | FOVR1 | 4:4 | 0x10 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_RF1R_FOVR1_Msk; header:CAN_RF1R_FOVR1_Msk; rm_can_1096:page:1096 |
| RF1R | RFOM1 | 5:5 | 0x20 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_RF1R_RFOM1_Msk; header:CAN_RF1R_RFOM1_Msk; rm_can_1096:page:1096 |
| IER | TMEIE | 0:0 | 0x1 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_TMEIE_Msk; header:CAN_IER_TMEIE_Msk; rm_can_1098:page:1098 |
| IER | FMPIE0 | 1:1 | 0x2 | Enable FIFO0 interrupt whenever FMP0 is nonzero. Keep other sources0. | header:CAN_IER_FMPIE0_Msk; header:CAN_IER_FMPIE0_Msk; rm_can_1097:page:1097 |
| IER | FFIE0 | 2:2 | 0x4 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_FFIE0_Msk; header:CAN_IER_FFIE0_Msk; rm_can_1097:page:1097 |
| IER | FOVIE0 | 3:3 | 0x8 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_FOVIE0_Msk; header:CAN_IER_FOVIE0_Msk; rm_can_1097:page:1097 |
| IER | FMPIE1 | 4:4 | 0x10 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_FMPIE1_Msk; header:CAN_IER_FMPIE1_Msk; rm_can_1097:page:1097 |
| IER | FFIE1 | 5:5 | 0x20 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_FFIE1_Msk; header:CAN_IER_FFIE1_Msk; rm_can_1097:page:1097 |
| IER | FOVIE1 | 6:6 | 0x40 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_FOVIE1_Msk; header:CAN_IER_FOVIE1_Msk; rm_can_1097:page:1097 |
| IER | EWGIE | 8:8 | 0x100 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_EWGIE_Msk; header:CAN_IER_EWGIE_Msk; rm_can_1097:page:1097 |
| IER | EPVIE | 9:9 | 0x200 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_EPVIE_Msk; header:CAN_IER_EPVIE_Msk; rm_can_1097:page:1097 |
| IER | BOFIE | 10:10 | 0x400 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_BOFIE_Msk; header:CAN_IER_BOFIE_Msk; rm_can_1097:page:1097 |
| IER | LECIE | 11:11 | 0x800 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_LECIE_Msk; header:CAN_IER_LECIE_Msk; rm_can_1097:page:1097 |
| IER | ERRIE | 15:15 | 0x8000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_ERRIE_Msk; header:CAN_IER_ERRIE_Msk; rm_can_1097:page:1097 |
| IER | WKUIE | 16:16 | 0x10000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_WKUIE_Msk; header:CAN_IER_WKUIE_Msk; rm_can_1097:page:1097 |
| IER | SLKIE | 17:17 | 0x20000 | Outside selected operating fields; consult the complete manual before using this field. | header:CAN_IER_SLKIE_Msk; header:CAN_IER_SLKIE_Msk; rm_can_1097:page:1097 |
| ESR | EWGF | 0:0 | 0x1 | Hardware error state/counter; nonzero fails this fresh-reset one-shot. | header:CAN_ESR_EWGF_Msk; header:CAN_ESR_EWGF_Msk; rm_can_1098:page:1098 |
| ESR | EPVF | 1:1 | 0x2 | Hardware error state/counter; nonzero fails this fresh-reset one-shot. | header:CAN_ESR_EPVF_Msk; header:CAN_ESR_EPVF_Msk; rm_can_1098:page:1098 |
| ESR | BOFF | 2:2 | 0x4 | Hardware error state/counter; nonzero fails this fresh-reset one-shot. | header:CAN_ESR_BOFF_Msk; header:CAN_ESR_BOFF_Msk; rm_can_1098:page:1098 |
| ESR | LEC | 6:4 | 0x70 | Last-error code0:none,1:stuff,2:form,3:ack,4:recessive,5:dominant,6:CRC,7:software marker; read-only use here. | header:CAN_ESR_LEC_Msk; header:CAN_ESR_LEC_Msk; rm_can_1098:page:1098 |
| ESR | TEC | 23:16 | 0xFF0000 | Hardware error state/counter; nonzero fails this fresh-reset one-shot. | header:CAN_ESR_TEC_Msk; header:CAN_ESR_TEC_Msk; rm_can_1098:page:1098 |
| ESR | REC | 31:24 | 0xFF000000 | Hardware error state/counter; nonzero fails this fresh-reset one-shot. | header:CAN_ESR_REC_Msk; header:CAN_ESR_REC_Msk; rm_can_1098:page:1098 |
| BTR | BRP | 9:0 | 0x3FF | Prescaler encoding divisor-1;5 gives divide6. | header:CAN_BTR_BRP_Msk; header:CAN_BTR_BRP_Msk; rm_can_1099:page:1099 |
| BTR | TS1 | 19:16 | 0xF0000 | Segment1 encoding quanta-1;10 gives11. | header:CAN_BTR_TS1_Msk; header:CAN_BTR_TS1_Msk; rm_can_1099:page:1099 |
| BTR | TS2 | 22:20 | 0x700000 | Segment2 encoding quanta-1;1 gives2. | header:CAN_BTR_TS2_Msk; header:CAN_BTR_TS2_Msk; rm_can_1099:page:1099 |
| BTR | SJW | 25:24 | 0x3000000 | Resynchronization jump encoding quanta-1;0 gives1. | header:CAN_BTR_SJW_Msk; header:CAN_BTR_SJW_Msk; rm_can_1099:page:1099 |
| BTR | LBKM | 30:30 | 0x40000000 | 1 enables internal TX-to-RX feedback; acceptance filters still apply. | header:CAN_BTR_LBKM_Msk; header:CAN_BTR_LBKM_Msk; rm_can_1099:page:1099 |
| BTR | SILM | 31:31 | 0x80000000 | Combine with LBKM=1 to disconnect CANRX and hold CANTX recessive. | header:CAN_BTR_SILM_Msk; header:CAN_BTR_SILM_Msk; rm_can_1099:page:1099 |
| sTxMailBox_0__TIR | TXRQ | 0:0 | 0x1 | Write1 last to request transmission; hardware clears on empty. | header:CAN_TI0R_TXRQ_Msk; header:CAN_TI0R_TXRQ_Msk; rm_can_1100:page:1100 |
| sTxMailBox_0__TIR | RTR | 1:1 | 0x2 | 0 data frame;1 remote (unsupported here). | header:CAN_TI0R_RTR_Msk; header:CAN_TI0R_RTR_Msk; rm_can_1100:page:1100 |
| sTxMailBox_0__TIR | IDE | 2:2 | 0x4 | 0 standard identifier;1 extended (unsupported here). | header:CAN_TI0R_IDE_Msk; header:CAN_TI0R_IDE_Msk; rm_can_1100:page:1100 |
| sTxMailBox_0__TIR | EXID | 20:3 | 0x1FFFF8 | Extended identifier lower18 bits; kept0 in this standard-ID mode. | header:CAN_TI0R_EXID_Msk; header:CAN_TI0R_EXID_Msk; rm_can_1100:page:1100 |
| sTxMailBox_0__TIR | STID | 31:21 | 0xFFE00000 | 11-bit standard identifier in31:21; EXID overlap convention only when IDE=1, outside this mode. | header:CAN_TI0R_STID_Msk; header:CAN_TI0R_STID_Msk; rm_can_1100:page:1100 |
| sTxMailBox_0__TDTR | DLC | 3:0 | 0xF | Data length0..8; this mode uses exactly8. | header:CAN_TDT0R_DLC_Msk; header:CAN_TDT0R_DLC_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDTR | TGT | 8:8 | 0x100 | Timestamp/global-time metadata unused; TTCM/TGT disabled. | header:CAN_TDT0R_TGT_Msk; header:CAN_TDT0R_TGT_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDTR | TIME | 31:16 | 0xFFFF0000 | Timestamp/global-time metadata unused; TTCM/TGT disabled. | header:CAN_TDT0R_TIME_Msk; header:CAN_TDT0R_TIME_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDLR | DATA0 | 7:0 | 0xFF | Payload byte0 in bits7:0; mode packs data byte0 first. | header:CAN_TDL0R_DATA0_Msk; header:CAN_TDL0R_DATA0_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDLR | DATA1 | 15:8 | 0xFF00 | Payload byte1 in bits15:8; mode packs data byte0 first. | header:CAN_TDL0R_DATA1_Msk; header:CAN_TDL0R_DATA1_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDLR | DATA2 | 23:16 | 0xFF0000 | Payload byte2 in bits23:16; mode packs data byte0 first. | header:CAN_TDL0R_DATA2_Msk; header:CAN_TDL0R_DATA2_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDLR | DATA3 | 31:24 | 0xFF000000 | Payload byte3 in bits31:24; mode packs data byte0 first. | header:CAN_TDL0R_DATA3_Msk; header:CAN_TDL0R_DATA3_Msk; rm_can_1101:page:1101 |
| sTxMailBox_0__TDHR | DATA4 | 7:0 | 0xFF | Payload byte4 in bits7:0; mode packs data byte0 first. | header:CAN_TDH0R_DATA4_Msk; header:CAN_TDH0R_DATA4_Msk; rm_can_1102:page:1102 |
| sTxMailBox_0__TDHR | DATA5 | 15:8 | 0xFF00 | Payload byte5 in bits15:8; mode packs data byte0 first. | header:CAN_TDH0R_DATA5_Msk; header:CAN_TDH0R_DATA5_Msk; rm_can_1102:page:1102 |
| sTxMailBox_0__TDHR | DATA6 | 23:16 | 0xFF0000 | Payload byte6 in bits23:16; mode packs data byte0 first. | header:CAN_TDH0R_DATA6_Msk; header:CAN_TDH0R_DATA6_Msk; rm_can_1102:page:1102 |
| sTxMailBox_0__TDHR | DATA7 | 31:24 | 0xFF000000 | Payload byte7 in bits31:24; mode packs data byte0 first. | header:CAN_TDH0R_DATA7_Msk; header:CAN_TDH0R_DATA7_Msk; rm_can_1102:page:1102 |
| sFIFOMailBox_0__RIR | RTR | 1:1 | 0x2 | 0 data frame;1 remote (unsupported here). | header:CAN_RI0R_RTR_Msk; header:CAN_RI0R_RTR_Msk; rm_can_1102:page:1102 |
| sFIFOMailBox_0__RIR | IDE | 2:2 | 0x4 | 0 standard identifier;1 extended (unsupported here). | header:CAN_RI0R_IDE_Msk; header:CAN_RI0R_IDE_Msk; rm_can_1102:page:1102 |
| sFIFOMailBox_0__RIR | EXID | 20:3 | 0x1FFFF8 | Extended identifier lower18 bits; kept0 in this standard-ID mode. | header:CAN_RI0R_EXID_Msk; header:CAN_RI0R_EXID_Msk; rm_can_1102:page:1102 |
| sFIFOMailBox_0__RIR | STID | 31:21 | 0xFFE00000 | 11-bit standard identifier in31:21; EXID overlap convention only when IDE=1, outside this mode. | header:CAN_RI0R_STID_Msk; header:CAN_RI0R_STID_Msk; rm_can_1102:page:1102 |
| sFIFOMailBox_0__RDTR | DLC | 3:0 | 0xF | Data length0..8; this mode uses exactly8. | header:CAN_RDT0R_DLC_Msk; header:CAN_RDT0R_DLC_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDTR | FMI | 15:8 | 0xFF00 | Filter match index; duplicated bank0 list entries permit indexes0 or1. | header:CAN_RDT0R_FMI_Msk; header:CAN_RDT0R_FMI_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDTR | TIME | 31:16 | 0xFFFF0000 | Timestamp/global-time metadata unused; TTCM/TGT disabled. | header:CAN_RDT0R_TIME_Msk; header:CAN_RDT0R_TIME_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDLR | DATA0 | 7:0 | 0xFF | Payload byte0 in bits7:0; mode packs data byte0 first. | header:CAN_RDL0R_DATA0_Msk; header:CAN_RDL0R_DATA0_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDLR | DATA1 | 15:8 | 0xFF00 | Payload byte1 in bits15:8; mode packs data byte0 first. | header:CAN_RDL0R_DATA1_Msk; header:CAN_RDL0R_DATA1_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDLR | DATA2 | 23:16 | 0xFF0000 | Payload byte2 in bits23:16; mode packs data byte0 first. | header:CAN_RDL0R_DATA2_Msk; header:CAN_RDL0R_DATA2_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDLR | DATA3 | 31:24 | 0xFF000000 | Payload byte3 in bits31:24; mode packs data byte0 first. | header:CAN_RDL0R_DATA3_Msk; header:CAN_RDL0R_DATA3_Msk; rm_can_1103:page:1103 |
| sFIFOMailBox_0__RDHR | DATA4 | 7:0 | 0xFF | Payload byte4 in bits7:0; mode packs data byte0 first. | header:CAN_RDH0R_DATA4_Msk; header:CAN_RDH0R_DATA4_Msk; rm_can_1104:page:1104 |
| sFIFOMailBox_0__RDHR | DATA5 | 15:8 | 0xFF00 | Payload byte5 in bits15:8; mode packs data byte0 first. | header:CAN_RDH0R_DATA5_Msk; header:CAN_RDH0R_DATA5_Msk; rm_can_1104:page:1104 |
| sFIFOMailBox_0__RDHR | DATA6 | 23:16 | 0xFF0000 | Payload byte6 in bits23:16; mode packs data byte0 first. | header:CAN_RDH0R_DATA6_Msk; header:CAN_RDH0R_DATA6_Msk; rm_can_1104:page:1104 |
| sFIFOMailBox_0__RDHR | DATA7 | 31:24 | 0xFF000000 | Payload byte7 in bits31:24; mode packs data byte0 first. | header:CAN_RDH0R_DATA7_Msk; header:CAN_RDH0R_DATA7_Msk; rm_can_1104:page:1104 |
| FMR | FINIT | 0:0 | 0x1 | 1 filter init/reception disabled;0 active. | header:CAN_FMR_FINIT_Msk; header:CAN_FMR_FINIT_Msk; rm_can_1105:page:1105 |
| FMR | CAN2SB | 13:8 | 0x3F00 | First CAN2 filter bank; this mode retains14 and uses only CAN1 bank0. | header:CAN_FMR_CAN2SB_Msk; header:CAN_FMR_CAN2SB_Msk; rm_can_1105:page:1105 |
| FM1R | FBM | 27:0 | 0xFFFFFFF | Bitmap of28 filter banks, bit0 selects bank0; only the documented bank0 list/scale/FIFO0/activation policy is supported. | header:CAN_FM1R_FBM_Msk; header:CAN_FM1R_FBM_Msk; rm_can_1105:page:1105 |
| FS1R | FSC | 27:0 | 0xFFFFFFF | Bitmap of28 filter banks, bit0 selects bank0; only the documented bank0 list/scale/FIFO0/activation policy is supported. | header:CAN_FS1R_FSC_Msk; header:CAN_FS1R_FSC_Msk; rm_can_1106:page:1106 |
| FFA1R | FFA | 27:0 | 0xFFFFFFF | Bitmap of28 filter banks, bit0 selects bank0; only the documented bank0 list/scale/FIFO0/activation policy is supported. | header:CAN_FFA1R_FFA_Msk; header:CAN_FFA1R_FFA_Msk; rm_can_1106:page:1106 |
| FA1R | FACT | 27:0 | 0xFFFFFFF | Bitmap of28 filter banks, bit0 selects bank0; only the documented bank0 list/scale/FIFO0/activation policy is supported. | header:CAN_FA1R_FACT_Msk; header:CAN_FA1R_FACT_Msk; rm_can_1107:page:1107 |

## Reviewed operating semantics

Applicability: **STM32F407VGT6, CAN1 only**, standard identifier `0x123`, eight data bytes, mailbox0, filter bank0/FIFO0, combined silent internal loopback. The mode assumes the reviewed owned-startup 42MHz PCLK1 recipe and exclusive ownership of CAN1/CAN2/shared filters. CAN2, normal external-bus, extended/remote/time-trigger frames, general bus-off recovery and CAN FD are outside this contract. Editorial review is not independent engineering approval or silicon-errata qualification.

Retrieve [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]] and [[peripherals/nvic]]. The shared NVIC document retains UART/TIM/EXTI retrieval prerequisites; those document reads do not require starting UART/TIM/EXTI hardware for CAN. No board CAN signal, transceiver or connector mapping is added to [[schemas/custom_pcb_netlist]]. Source: rm_can_1070:page:1070; rm_can_1075:page:1075; exact header and inherited NVIC review.

## Owned startup and test configuration

1. Keep global interrupts masked, install the exact startup vector/handler state and require CAN1_RX0_IRQn=20 (vector slot36, CAN1_RX0_IRQHandler). Reject an already enabled/active line. Own both controllers/shared filters and start with both clock gates disabled. Enable/read back CAN1EN; assert/release only CAN1RST, preserving unrelated APB1 bits and leaving CAN2EN disabled. Sources: rm_dac_239:page:239; rm_dac_247:page:247; rm_can_1070:page:1070; header:CAN1_RX0_IRQn.
2. CAN resets in sleep. Require the fresh-reset control/empty/disabled state, clear SLEEP while requesting INRQ, and bound the wait for INAK=1/SLAK=0. Preserve the DBF reset bit, set NART=1 (no automatic retry) and RFLM=1 (locked FIFO), leave automatic wake/bus-off/time-trigger modes off. BTR accesses occur **only while initialization is acknowledged**. Sources: rm_can_1073:page:1073; rm_can_1090 through rm_can_1093.
3. Configure **SILM=LBKM=1**. Combined mode disconnects external CANRX internally and holds CANTX recessive; plain LBKM alone can expose transmissions on CANTX and is not this contract. No external wiring is required by this internal test. Every CAN register access is an aligned32-bit word. Sources: rm_can_1075:page:1075; rm_can_1090:page:1090; rm_can_1099:page:1099.
4. Use BRP=5, TS1=10, TS2=1, SJW=0. Derived values: prescaler6, segment1=11tq, segment2=2tq, SJW=1tq; nominal bit rate42MHz/(6*(1+11+2))=500kbit/s and sample point12/14. These are calculations at the declared clock, not measured timing. Sources: rm_can_1086:page:1086; rm_can_1087:page:1087; rm_can_1099:page:1099.
5. Require unused filters inactive. Preserve all unmodeled FMR bits from a read; retain CAN2SB=14 and FINIT=1 while configuring. Deactivate bank0, choose 32-bit identifier-list mode and FIFO0, set both list entries to `0x123<<21` (standard/data, remaining bits zero), then activate only bank0 and clear FINIT. Other banks stay inactive. Source: visually reviewed Figure342, rm_can_1081:page:1081; rm_can_1104 through rm_can_1107; rm_can_1111:page:1111.
6. Leave initialization and bound INAK/SLAK becoming0. Keep IER=0 and NVIC disabled until handler/state and source conditions are ready. Do not access BTR after leaving initialization. Source: rm_can_1073:page:1073; rm_can_1092 through rm_can_1093; rm_can_1099:page:1099.

## One-shot request and FIFO0 interrupt

Require all transmit mailboxes empty, both receive FIFOs empty and no stale completion/error. Mailbox contents at reset are **unspecified**: program identifier, DLC=8 and both payload words explicitly. Pack byte0 into data-low bits7:0. A pending mailbox is write-protected and must never be rewritten. Set TXRQ only after all other data is staged/read back and software expectations are published. Sources: rm_can_1076:page:1076; rm_can_1077:page:1077; rm_can_1100 through rm_can_1104.

With global interrupts still masked and a prepared handler, clear the empty/disabled source's NVIC pending state, set priority5 (IP[20]=0x50; software policy), enable only FMPIE0, then NVIC line20 through literal action writes. The RX pending count generates FIFO0 IRQ while nonzero; clearing NVIC pending alone cannot remove that cause. Restore the intended global state only after setup/request publication. Source: rm_can_1088:page:1088; visually reviewed Figure348, rm_can_1089:page:1089; rm_can_1097:page:1097; nvic_review:ISER/ICER/ICPR/IP/IABR; header:CAN1_RX0_IRQn.

The handler must reject errors/overrun, require one pending frame and read **RIR, RDTR, RDLR, RDHR before RFOM0**. Validate standard ID, IDE/RTR, length, accepted filter index and all8bytes. Recheck errors after reads; simultaneous progress never hides a failure. Write literal RFOM0 to release, bound acknowledgement and disable the owned source/line after the cause is removed. Never write an RX mailbox. A spurious IRQ or FIFO pending observation alone does not establish an interrupt-delivered frame. Sources: rm_can_1079:page:1079; rm_can_1084:page:1084; rm_can_1095:page:1095; rm_can_1102 through rm_can_1104.

Foreground completion requires a validated ISR receipt **and** RQCP0/TXOK0/TME0. TXOK or TME alone is insufficient. Only after success may a literal RQCP0 clear that mailbox's completion group. Acknowledge no other mailbox; never read-modify-write TSR or RF0R. Failures retain diagnostics, invalidate configuration and require an owned reset before retry. Cleanup disables only the owned interrupt source/line; it does not promise abort, drain, bus recovery or restored hardware state. All foreground waits and release checks have finite iteration limits, not calibrated millisecond guarantees. Sources: rm_can_1093 through rm_can_1098; inherited NVIC action semantics.

## Reviewed ambiguities and limits

The printed FMR reset on page1104 is `0x2A1C0E01`, while page1111 leaves reserved reset bits unenumerated. This contract asserts only the defined CAN2SB/FINIT fields, preserves other read bits and **does not publish a full-register reset literal**. TX/RX data/filter reset values with `X` remain unknown. Page1104's DATA4..7 prose has copied low-byte descriptions; the explicit bit labels, exact header masks and register layout govern byte numbering. Source: rm_can_1104:page:1104; rm_can_1111:page:1111; exact header DATA4..7 masks.

Offsets0x200..0x31C are present **only in CAN1**, even though vendor CAN_TypeDef is reused for CAN2. The complete declaration table is retained; instance-scoped modes prevent applying this filter contract to CAN2. Source: rm_can_1109:page:1109.

A host effect model and target build do not prove real exception delivery, physical timing, external-bus interoperability or arbitrary generated code correctness. No CAN firmware has been flashed or physically qualified in this increment. Independent embedded review and errata qualification remain pending. See [[sources]] and [[index]].

## Initialization RX follow-up

The original hardware run timed out with INRQ=0, INAK=1 and RX=0. This revision keeps bounded acknowledgement waits and explicitly requires [[peripherals/gpio]] can1_rx_pd0 before CAN initialization. Combined-mode RX isolation does not prove that initialization can ignore synchronization. See the complete operating requirements; physical success and causal diagnosis remain pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| silent_loopback | CAN1 | MCR, MSR, TSR, RF0R, RF1R, IER, ESR, BTR, FMR, FM1R, FS1R, FFA1R, FA1R, sTxMailBox_0__TIR, sTxMailBox_0__TDTR, sTxMailBox_0__TDLR, sTxMailBox_0__TDHR, sFIFOMailBox_0__RIR, sFIFOMailBox_0__RDTR, sFIFOMailBox_0__RDLR, sFIFOMailBox_0__RDHR, sFilterRegister_0__FR1, sFilterRegister_0__FR2 | BTR: BRP, TS1, TS2, SJW, LBKM, SILM; ESR: EWGF, EPVF, BOFF, LEC, TEC, REC; FA1R: FACT; FFA1R: FFA; FM1R: FBM; FMR: FINIT, CAN2SB; FS1R: FSC; IER: FMPIE0; MCR: INRQ, SLEEP, NART, RFLM, DBF; MSR: INAK, SLAK, RX; RF0R: FMP0, FULL0, FOVR0, RFOM0; RF1R: FMP1, FULL1, FOVR1, RFOM1; TSR: RQCP0, TXOK0, ALST0, TERR0, TME; sFIFOMailBox_0__RDHR: DATA4, DATA5, DATA6, DATA7; sFIFOMailBox_0__RDLR: DATA0, DATA1, DATA2, DATA3; sFIFOMailBox_0__RDTR: DLC, FMI, TIME; sFIFOMailBox_0__RIR: RTR, IDE, EXID, STID; sTxMailBox_0__TDHR: DATA4, DATA5, DATA6, DATA7; sTxMailBox_0__TDLR: DATA0, DATA1, DATA2, DATA3; sTxMailBox_0__TDTR: DLC, TGT, TIME; sTxMailBox_0__TIR: TXRQ, RTR, IDE, EXID, STID | STM32F407VGT6 CAN1 only, owned fresh reset, exclusive CAN1/CAN2 shared filters, PCLK1=42MHz. Registers0x200..0x31C belong only to CAN1, despite shared header structure.<br>Aligned32-bit accesses. From reset sleep set INRQ and clear SLEEP; bound INAK/SLAK acknowledgements. Program BTR only while INAK=1. Preserve DBF and use NART/RFLM=1.<br>Combined SILM/LBKM=1 provides internal loopback with CANRX disconnected and CANTX recessive; external CAN wiring/transceiver is not established.<br>BRP5,TS1=10,TS2=1,SJW0 gives42MHz/(6*(1+11+2))=500kbit/s nominal; sample point12/14. This is calculated, not physically measured.<br>FINIT=1 during filter configuration, bank0 inactive before writes, single32-bit identifier list, FIFO0, FR1=FR2=0x123&lt;&lt;21, only bank0 active. Retain CAN2SB14 and preserve FMR reserved bits read from hardware. Full reset word remains unasserted due to source table presentation differences.<br>Mailbox reset data and filter values are unspecified. Require empty TX mailboxes and FIFOs with no stale completion/error; explicitly write all four TX mailbox0 registers, TXRQ last. Never write pending TX or any RX mailbox.<br>One standard data frame,ID0x123,DLC8, no extended/remote/time-trigger traffic. Require request-complete,TXOK0,TME0 and full matching received identifier,length,payload. Errors have precedence over simultaneous progress.<br>Read all four FIFO words before literal RFOM0; never RMW mixed W1C/release status. Bound release acknowledgement. Preserve underrun/overrun/bus-off/transmit diagnostics on failure; require owned reset before retry.<br>Interrupt delivery uses the separate FIFO0 IRQ contract; polling completion alone cannot prove exception delivery. No normal external-bus,CAN2,FD,DMA or broad recovery support.<br>This revised candidate requires the explicit GPIO can1_rx_pd0 route before CAN configuration; no claim is made that every silent-loopback implementation requires this pin choice.<br>Require CAN_MSR.RX high while INAK=1 before clearing INRQ. A low snapshot rejects the attempt without enabling IRQ or TX. After clearing INRQ retain a finite wait for INAK/SLAK=0; hardware synchronization still needs 11 consecutive recessive bits.<br>RM0090 describes actual CANRX disregard in established combined silent/loopback operation; do not use that wording to erase initialization synchronization prerequisites. The prior physical failure is preserved and the proposed fix is not yet physically tested. | rm_can_1070:page:1070; rm_can_1073:page:1073; rm_can_1075:page:1075; rm_can_1076:page:1076; rm_can_1077:page:1077; rm_can_1079:page:1079; rm_can_1081:page:1081; rm_can_1084:page:1084; rm_can_1086:page:1086; rm_can_1087:page:1087; rm_can_1090:page:1090; rm_can_1095:page:1095; rm_can_1099:page:1099; rm_can_1100:page:1100; rm_can_1101:page:1101; rm_can_1104:page:1104; rm_can_1105:page:1105; rm_can_1107:page:1107; rm_can_1109:page:1109; rm_can_1111:page:1111; rm_can_1073:page:1073; rm_can_rx_1074:page:1074; rm_can_1075:page:1075; rm_can_1092:page:1092 | [[peripherals/rcc]] / can1_gate_reset: RCC; [[peripherals/gpio]] / can1_rx_pd0: GPIOD |
| silent_loopback_fifo0_irq | CAN1 | IER, RF0R, ESR, TSR, sFIFOMailBox_0__RIR, sFIFOMailBox_0__RDTR, sFIFOMailBox_0__RDLR, sFIFOMailBox_0__RDHR, MSR | IER: FMPIE0; MSR: RX; RF0R: FMP0, FOVR0, FULL0, RFOM0 | Keep global interrupts masked during handler/state/configuration and arming. IRQ20/vector36 must resolve CAN1_RX0_IRQHandler in the pinned startup asset.<br>Clear source cause before NVIC pending, program implemented priority5, enable only FMPIE0, then NVIC line20. Restore intended global interrupt state last, after staging the owned request.<br>Handler validates error/state and all four receive words, releases FIFO with literal RFOM0, then disables source and owned line. Spurious interrupts cannot establish success.<br>A bounded foreground wait requires both valid interrupt-delivered receive and TX completion; polling/FMP or TXOK alone cannot pass. Failure cleanup disables only owned source/line without erasing diagnostics. Reset before retry.<br>This revised candidate requires the explicit GPIO can1_rx_pd0 route before CAN configuration; no claim is made that every silent-loopback implementation requires this pin choice.<br>Require CAN_MSR.RX high while INAK=1 before clearing INRQ. A low snapshot rejects the attempt without enabling IRQ or TX. After clearing INRQ retain a finite wait for INAK/SLAK=0; hardware synchronization still needs 11 consecutive recessive bits.<br>RM0090 describes actual CANRX disregard in established combined silent/loopback operation; do not use that wording to erase initialization synchronization prerequisites. The prior physical failure is preserved and the proposed fix is not yet physically tested. | rm_can_1088:page:1088; rm_can_1089:page:1089; rm_can_1095:page:1095; rm_can_1097:page:1097; can_nvic_review:CAN1_RX0_IRQn binding to exact header:20; nvic_review:ISER/ICER/ICPR/IP; rm_can_1073:page:1073; rm_can_rx_1074:page:1074; rm_can_1075:page:1075; rm_can_1092:page:1092 | [[peripherals/can]] / silent_loopback: CAN1; [[peripherals/nvic]] / can1_rx0_prepare: NVIC; [[peripherals/gpio]] / can1_rx_pd0: GPIOD |

## Review

Reviewer: Codex implementing-author editorial review; independent review pending. Basis: Complete MCP-returned RM0090 Rev22 pp1069-1112, exact header mapping, selected source images and inherited NVIC semantics. Scope/conflicts explicit; no physical CAN qualification..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
