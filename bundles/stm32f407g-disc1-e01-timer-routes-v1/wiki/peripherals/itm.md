# ITM — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| ITM | 0xE0000000 | Not asserted | Not asserted | cmsis_core:ITM_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PORT | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PORT | 32 | 4 |
| TER | 0xE00 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.TER | 1 | 4 |
| TPR | 0xE40 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.TPR | 1 | 4 |
| TCR | 0xE80 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.TCR | 1 | 4 |
| LAR | 0xFB0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.LAR | 1 | 4 |
| LSR | 0xFB4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.LSR | 1 | 4 |
| PID4 | 0xFD0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID4 | 1 | 4 |
| PID5 | 0xFD4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID5 | 1 | 4 |
| PID6 | 0xFD8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID6 | 1 | 4 |
| PID7 | 0xFDC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID7 | 1 | 4 |
| PID0 | 0xFE0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID0 | 1 | 4 |
| PID1 | 0xFE4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID1 | 1 | 4 |
| PID2 | 0xFE8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID2 | 1 | 4 |
| PID3 | 0xFEC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.PID3 | 1 | 4 |
| CID0 | 0xFF0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.CID0 | 1 | 4 |
| CID1 | 0xFF4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.CID1 | 1 | 4 |
| CID2 | 0xFF8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.CID2 | 1 | 4 |
| CID3 | 0xFFC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:ITM_Type.CID3 | 1 | 4 |

## Declared C storage views

These union members share storage; the register map records its ABI size and array stride. Declared C widths do not establish legal hardware access widths, permissions, reset values or operating semantics. Those require separate reviewed evidence.

| Register | Union member | Declared C type | Width bits | Sources |
| --- | --- | --- | --- | --- |
| PORT | u8 | volatile uint8_t | 8 | cmsis_core:ITM_Type.PORT.u8 |
| PORT | u16 | volatile uint16_t | 16 | cmsis_core:ITM_Type.PORT.u16 |
| PORT | u32 | volatile uint32_t | 32 | cmsis_core:ITM_Type.PORT.u32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| TPR | PRIVMASK | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TPR_PRIVMASK_Msk |
| TCR | ITMENA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_ITMENA_Msk |
| TCR | TSENA | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_TSENA_Msk |
| TCR | SYNCENA | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_SYNCENA_Msk |
| TCR | DWTENA | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_DWTENA_Msk |
| TCR | SWOENA | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_SWOENA_Msk |
| TCR | TSPrescale | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_TSPrescale_Msk |
| TCR | GTSFREQ | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_GTSFREQ_Msk |
| TCR | TraceBusID | 22:16 | 0x7F0000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_TraceBusID_Msk |
| TCR | BUSY | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_TCR_BUSY_Msk |
| LSR | Present | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_LSR_Present_Msk |
| LSR | Access | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_LSR_Access_Msk |
| LSR | ByteAcc | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | cmsis_core:ITM_LSR_ByteAcc_Msk |

## Operating semantics unavailable

**itm: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
