# PWR — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PWR | 0x40007000 | Not asserted | Not asserted | header:PWR_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR2 |
| CR3 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR3 |
| CR4 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.CR4 |
| SR1 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.SR1 |
| SR2 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.SR2 |
| SCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.SCR |
| PUCRA | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PUCRA |
| PDCRA | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PDCRA |
| PUCRB | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PUCRB |
| PDCRB | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PDCRB |
| PUCRC | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PUCRC |
| PDCRC | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PDCRC |
| PUCRD | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PUCRD |
| PDCRD | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PDCRD |
| PUCRF | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PUCRF |
| PDCRF | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:PWR_TypeDef.PDCRF |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | LPMS | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_LPMS_Msk |
| CR1 | FPD_STOP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_FPD_STOP_Msk |
| CR1 | FPD_LPRUN | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_FPD_LPRUN_Msk |
| CR1 | FPD_LPSLP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_FPD_LPSLP_Msk |
| CR1 | DBP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_DBP_Msk |
| CR1 | VOS | 10:9 | 0x600 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_VOS_Msk |
| CR1 | LPR | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR1_LPR_Msk |
| CR2 | PVDE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_PVDE_Msk |
| CR2 | PVDFT | 3:1 | 0xE | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_PVDFT_Msk |
| CR2 | PVDRT | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_PVDRT_Msk |
| CR2 | PVMEN_DAC | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR2_PVMEN_DAC_Msk |
| SR2 | FLASH_RDY | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_FLASH_RDY_Msk |
| SR2 | REGLPS | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_REGLPS_Msk |
| SR2 | REGLPF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_REGLPF_Msk |
| SR2 | VOSF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_VOSF_Msk |
| SR2 | PVDO | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_PVDO_Msk |
| SR2 | PVMO_DAC | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_SR2_PVMO_DAC_Msk |
| PUCRA | PU0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU0_Msk |
| PUCRA | PU1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU1_Msk |
| PUCRA | PU2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU2_Msk |
| PUCRA | PU3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU3_Msk |
| PUCRA | PU4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU4_Msk |
| PUCRA | PU5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU5_Msk |
| PUCRA | PU6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU6_Msk |
| PUCRA | PU7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU7_Msk |
| PUCRA | PU8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU8_Msk |
| PUCRA | PU9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU9_Msk |
| PUCRA | PU10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU10_Msk |
| PUCRA | PU11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU11_Msk |
| PUCRA | PU12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU12_Msk |
| PUCRA | PU13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU13_Msk |
| PUCRA | PU14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU14_Msk |
| PUCRA | PU15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRA_PU15_Msk |
| PDCRA | PD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD0_Msk |
| PDCRA | PD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD1_Msk |
| PDCRA | PD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD2_Msk |
| PDCRA | PD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD3_Msk |
| PDCRA | PD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD4_Msk |
| PDCRA | PD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD5_Msk |
| PDCRA | PD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD6_Msk |
| PDCRA | PD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD7_Msk |
| PDCRA | PD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD8_Msk |
| PDCRA | PD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD9_Msk |
| PDCRA | PD10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD10_Msk |
| PDCRA | PD11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD11_Msk |
| PDCRA | PD12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD12_Msk |
| PDCRA | PD13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD13_Msk |
| PDCRA | PD14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD14_Msk |
| PDCRA | PD15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRA_PD15_Msk |
| PUCRB | PU0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU0_Msk |
| PUCRB | PU1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU1_Msk |
| PUCRB | PU2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU2_Msk |
| PUCRB | PU3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU3_Msk |
| PUCRB | PU4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU4_Msk |
| PUCRB | PU5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU5_Msk |
| PUCRB | PU6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU6_Msk |
| PUCRB | PU7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU7_Msk |
| PUCRB | PU8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU8_Msk |
| PUCRB | PU9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU9_Msk |
| PUCRB | PU10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU10_Msk |
| PUCRB | PU11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU11_Msk |
| PUCRB | PU12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU12_Msk |
| PUCRB | PU13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU13_Msk |
| PUCRB | PU14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU14_Msk |
| PUCRB | PU15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRB_PU15_Msk |
| PDCRB | PD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD0_Msk |
| PDCRB | PD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD1_Msk |
| PDCRB | PD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD2_Msk |
| PDCRB | PD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD3_Msk |
| PDCRB | PD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD4_Msk |
| PDCRB | PD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD5_Msk |
| PDCRB | PD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD6_Msk |
| PDCRB | PD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD7_Msk |
| PDCRB | PD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD8_Msk |
| PDCRB | PD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD9_Msk |
| PDCRB | PD10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD10_Msk |
| PDCRB | PD11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD11_Msk |
| PDCRB | PD12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD12_Msk |
| PDCRB | PD13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD13_Msk |
| PDCRB | PD14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD14_Msk |
| PDCRB | PD15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRB_PD15_Msk |
| PUCRC | PU0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU0_Msk |
| PUCRC | PU1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU1_Msk |
| PUCRC | PU2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU2_Msk |
| PUCRC | PU3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU3_Msk |
| PUCRC | PU4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU4_Msk |
| PUCRC | PU5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU5_Msk |
| PUCRC | PU6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU6_Msk |
| PUCRC | PU7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU7_Msk |
| PUCRC | PU8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU8_Msk |
| PUCRC | PU9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU9_Msk |
| PUCRC | PU10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU10_Msk |
| PUCRC | PU11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU11_Msk |
| PUCRC | PU12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU12_Msk |
| PUCRC | PU13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU13_Msk |
| PUCRC | PU14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU14_Msk |
| PUCRC | PU15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRC_PU15_Msk |
| PDCRC | PD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD0_Msk |
| PDCRC | PD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD1_Msk |
| PDCRC | PD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD2_Msk |
| PDCRC | PD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD3_Msk |
| PDCRC | PD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD4_Msk |
| PDCRC | PD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD5_Msk |
| PDCRC | PD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD6_Msk |
| PDCRC | PD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD7_Msk |
| PDCRC | PD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD8_Msk |
| PDCRC | PD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD9_Msk |
| PDCRC | PD10 | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD10_Msk |
| PDCRC | PD11 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD11_Msk |
| PDCRC | PD12 | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD12_Msk |
| PDCRC | PD13 | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD13_Msk |
| PDCRC | PD14 | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD14_Msk |
| PDCRC | PD15 | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRC_PD15_Msk |
| PUCRD | PU0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU0_Msk |
| PUCRD | PU1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU1_Msk |
| PUCRD | PU2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU2_Msk |
| PUCRD | PU3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU3_Msk |
| PUCRD | PU4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU4_Msk |
| PUCRD | PU5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU5_Msk |
| PUCRD | PU6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU6_Msk |
| PUCRD | PU8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU8_Msk |
| PUCRD | PU9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRD_PU9_Msk |
| PDCRD | PD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD0_Msk |
| PDCRD | PD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD1_Msk |
| PDCRD | PD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD2_Msk |
| PDCRD | PD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD3_Msk |
| PDCRD | PD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD4_Msk |
| PDCRD | PD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD5_Msk |
| PDCRD | PD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD6_Msk |
| PDCRD | PD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD8_Msk |
| PDCRD | PD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRD_PD9_Msk |
| PUCRF | PU0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRF_PU0_Msk |
| PUCRF | PU1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRF_PU1_Msk |
| PUCRF | PU2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRF_PU2_Msk |
| PUCRF | PU3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRF_PU3_Msk |
| PUCRF | PU4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PUCRF_PU4_Msk |
| PDCRF | PD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRF_PD0_Msk |
| PDCRF | PD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRF_PD1_Msk |
| PDCRF | PD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRF_PD2_Msk |
| PDCRF | PD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRF_PD3_Msk |
| PDCRF | PD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_PDCRF_PD4_Msk |

## Operating semantics unavailable

**pwr: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- CR3: bit fields withheld: UNSUPPORTED_MASK: PWR_CR3_EWUP_Msk: non-contiguous bit field
- CR4: bit fields withheld: UNSUPPORTED_MASK: PWR_CR4_WP_Msk: non-contiguous bit field
- SR1: bit fields withheld: UNSUPPORTED_MASK: PWR_SR1_WUF_Msk: non-contiguous bit field
- SCR: bit fields withheld: UNSUPPORTED_MASK: PWR_SCR_CWUF_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
