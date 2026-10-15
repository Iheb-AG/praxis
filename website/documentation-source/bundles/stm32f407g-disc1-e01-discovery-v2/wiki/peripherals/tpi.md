# TPI — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TPI | 0xE0040000 | Not asserted | Not asserted | cmsis_core:TPI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SSPSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.SSPSR; cmsis_core:TPI_Type.SSPSR |
| CSPSR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.CSPSR; cmsis_core:TPI_Type.CSPSR |
| ACPR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.ACPR; cmsis_core:TPI_Type.ACPR |
| SPPR | 0x0F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.SPPR; cmsis_core:TPI_Type.SPPR |
| FFSR | 0x300 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.FFSR; cmsis_core:TPI_Type.FFSR |
| FFCR | 0x304 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.FFCR; cmsis_core:TPI_Type.FFCR |
| FSCR | 0x308 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.FSCR; cmsis_core:TPI_Type.FSCR |
| TRIGGER | 0xEE8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.TRIGGER; cmsis_core:TPI_Type.TRIGGER |
| FIFO0 | 0xEEC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.FIFO0; cmsis_core:TPI_Type.FIFO0 |
| ITATBCTR2 | 0xEF0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.ITATBCTR2; cmsis_core:TPI_Type.ITATBCTR2 |
| ITATBCTR0 | 0xEF8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.ITATBCTR0; cmsis_core:TPI_Type.ITATBCTR0 |
| FIFO1 | 0xEFC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.FIFO1; cmsis_core:TPI_Type.FIFO1 |
| ITCTRL | 0xF00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.ITCTRL; cmsis_core:TPI_Type.ITCTRL |
| CLAIMSET | 0xFA0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.CLAIMSET; cmsis_core:TPI_Type.CLAIMSET |
| CLAIMCLR | 0xFA4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.CLAIMCLR; cmsis_core:TPI_Type.CLAIMCLR |
| DEVID | 0xFC8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.DEVID; cmsis_core:TPI_Type.DEVID |
| DEVTYPE | 0xFCC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:TPI_Type.DEVTYPE; cmsis_core:TPI_Type.DEVTYPE |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ACPR | PRESCALER | 12:0 | 0x1FFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_ACPR_PRESCALER_Msk; cmsis_core:TPI_ACPR_PRESCALER_Msk |
| SPPR | TXMODE | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_SPPR_TXMODE_Msk; cmsis_core:TPI_SPPR_TXMODE_Msk |
| FFSR | FlInProg | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFSR_FlInProg_Msk; cmsis_core:TPI_FFSR_FlInProg_Msk |
| FFSR | FtStopped | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFSR_FtStopped_Msk; cmsis_core:TPI_FFSR_FtStopped_Msk |
| FFSR | TCPresent | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFSR_TCPresent_Msk; cmsis_core:TPI_FFSR_TCPresent_Msk |
| FFSR | FtNonStop | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFSR_FtNonStop_Msk; cmsis_core:TPI_FFSR_FtNonStop_Msk |
| FFCR | EnFCont | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFCR_EnFCont_Msk; cmsis_core:TPI_FFCR_EnFCont_Msk |
| FFCR | TrigIn | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FFCR_TrigIn_Msk; cmsis_core:TPI_FFCR_TrigIn_Msk |
| TRIGGER | TRIGGER | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_TRIGGER_TRIGGER_Msk; cmsis_core:TPI_TRIGGER_TRIGGER_Msk |
| FIFO0 | ETM0 | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ETM0_Msk; cmsis_core:TPI_FIFO0_ETM0_Msk |
| FIFO0 | ETM1 | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ETM1_Msk; cmsis_core:TPI_FIFO0_ETM1_Msk |
| FIFO0 | ETM2 | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ETM2_Msk; cmsis_core:TPI_FIFO0_ETM2_Msk |
| FIFO0 | ETM_bytecount | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ETM_bytecount_Msk; cmsis_core:TPI_FIFO0_ETM_bytecount_Msk |
| FIFO0 | ETM_ATVALID | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ETM_ATVALID_Msk; cmsis_core:TPI_FIFO0_ETM_ATVALID_Msk |
| FIFO0 | ITM_bytecount | 28:27 | 0x18000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ITM_bytecount_Msk; cmsis_core:TPI_FIFO0_ITM_bytecount_Msk |
| FIFO0 | ITM_ATVALID | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO0_ITM_ATVALID_Msk; cmsis_core:TPI_FIFO0_ITM_ATVALID_Msk |
| ITATBCTR2 | ATREADY1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_ITATBCTR2_ATREADY1_Msk; cmsis_core:TPI_ITATBCTR2_ATREADY1_Msk |
| ITATBCTR0 | ATREADY1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_ITATBCTR0_ATREADY1_Msk; cmsis_core:TPI_ITATBCTR0_ATREADY1_Msk |
| FIFO1 | ITM0 | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ITM0_Msk; cmsis_core:TPI_FIFO1_ITM0_Msk |
| FIFO1 | ITM1 | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ITM1_Msk; cmsis_core:TPI_FIFO1_ITM1_Msk |
| FIFO1 | ITM2 | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ITM2_Msk; cmsis_core:TPI_FIFO1_ITM2_Msk |
| FIFO1 | ETM_bytecount | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ETM_bytecount_Msk; cmsis_core:TPI_FIFO1_ETM_bytecount_Msk |
| FIFO1 | ETM_ATVALID | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ETM_ATVALID_Msk; cmsis_core:TPI_FIFO1_ETM_ATVALID_Msk |
| FIFO1 | ITM_bytecount | 28:27 | 0x18000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ITM_bytecount_Msk; cmsis_core:TPI_FIFO1_ITM_bytecount_Msk |
| FIFO1 | ITM_ATVALID | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_FIFO1_ITM_ATVALID_Msk; cmsis_core:TPI_FIFO1_ITM_ATVALID_Msk |
| ITCTRL | Mode | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_ITCTRL_Mode_Msk; cmsis_core:TPI_ITCTRL_Mode_Msk |
| DEVID | NrTraceInput | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_NrTraceInput_Msk; cmsis_core:TPI_DEVID_NrTraceInput_Msk |
| DEVID | AsynClkIn | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_AsynClkIn_Msk; cmsis_core:TPI_DEVID_AsynClkIn_Msk |
| DEVID | MinBufSz | 8:6 | 0x1C0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_MinBufSz_Msk; cmsis_core:TPI_DEVID_MinBufSz_Msk |
| DEVID | PTINVALID | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_PTINVALID_Msk; cmsis_core:TPI_DEVID_PTINVALID_Msk |
| DEVID | MANCVALID | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_MANCVALID_Msk; cmsis_core:TPI_DEVID_MANCVALID_Msk |
| DEVID | NRZVALID | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | cmsis_core:TPI_DEVID_NRZVALID_Msk; cmsis_core:TPI_DEVID_NRZVALID_Msk |

## Operating semantics unavailable

**tpi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- DEVTYPE: bit fields withheld: DECLARATION_CONFLICT: TPI_DEVTYPE_SubType_Msk: position and mask disagree

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
