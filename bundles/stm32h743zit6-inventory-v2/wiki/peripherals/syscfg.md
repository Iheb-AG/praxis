# SYSCFG — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SYSCFG | 0x58000400 | Not asserted | Not asserted | header:SYSCFG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PMCR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.PMCR | 1 | 4 |
| EXTICR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.EXTICR | 4 | 4 |
| CFGR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CFGR | 1 | 4 |
| CCCSR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CCCSR | 1 | 4 |
| CCVR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CCVR | 1 | 4 |
| CCCR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CCCR | 1 | 4 |
| PWRCR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.PWRCR | 1 | 4 |
| PKGR | 0x124 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.PKGR | 1 | 4 |
| UR0 | 0x300 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR0 | 1 | 4 |
| UR1 | 0x304 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR1 | 1 | 4 |
| UR2 | 0x308 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR2 | 1 | 4 |
| UR3 | 0x30C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR3 | 1 | 4 |
| UR4 | 0x310 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR4 | 1 | 4 |
| UR5 | 0x314 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR5 | 1 | 4 |
| UR6 | 0x318 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR6 | 1 | 4 |
| UR7 | 0x31C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR7 | 1 | 4 |
| UR8 | 0x320 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR8 | 1 | 4 |
| UR9 | 0x324 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR9 | 1 | 4 |
| UR10 | 0x328 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR10 | 1 | 4 |
| UR11 | 0x32C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR11 | 1 | 4 |
| UR12 | 0x330 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR12 | 1 | 4 |
| UR13 | 0x334 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR13 | 1 | 4 |
| UR14 | 0x338 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR14 | 1 | 4 |
| UR15 | 0x33C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR15 | 1 | 4 |
| UR16 | 0x340 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR16 | 1 | 4 |
| UR17 | 0x344 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.UR17 | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| PMCR | I2C1_FMP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C1_FMP_Msk |
| PMCR | I2C2_FMP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C2_FMP_Msk |
| PMCR | I2C3_FMP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C3_FMP_Msk |
| PMCR | I2C4_FMP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C4_FMP_Msk |
| PMCR | I2C_PB6_FMP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C_PB6_FMP_Msk |
| PMCR | I2C_PB7_FMP | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C_PB7_FMP_Msk |
| PMCR | I2C_PB8_FMP | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C_PB8_FMP_Msk |
| PMCR | I2C_PB9_FMP | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_I2C_PB9_FMP_Msk |
| PMCR | BOOSTEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_BOOSTEN_Msk |
| PMCR | BOOSTVDDSEL | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_BOOSTVDDSEL_Msk |
| PMCR | EPIS_SEL | 23:21 | 0xE00000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_EPIS_SEL_Msk |
| PMCR | PA0SO | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_PA0SO_Msk |
| PMCR | PA1SO | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_PA1SO_Msk |
| PMCR | PC2SO | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_PC2SO_Msk |
| PMCR | PC3SO | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PMCR_PC3SO_Msk |
| CFGR | PVDL | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_PVDL_Msk |
| CFGR | FLASHL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_FLASHL_Msk |
| CFGR | CM7L | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_CM7L_Msk |
| CFGR | BKRAML | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_BKRAML_Msk |
| CFGR | SRAM4L | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_SRAM4L_Msk |
| CFGR | SRAM3L | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_SRAM3L_Msk |
| CFGR | SRAM2L | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_SRAM2L_Msk |
| CFGR | SRAM1L | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_SRAM1L_Msk |
| CFGR | DTCML | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_DTCML_Msk |
| CFGR | ITCML | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_ITCML_Msk |
| CFGR | AXISRAML | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR_AXISRAML_Msk |
| CCCSR | EN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCSR_EN_Msk |
| CCCSR | CS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCSR_CS_Msk |
| CCCSR | READY | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCSR_READY_Msk |
| CCCSR | HSLV | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCSR_HSLV_Msk |
| CCVR | NCV | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCVR_NCV_Msk |
| CCVR | PCV | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCVR_PCV_Msk |
| CCCR | NCC | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCR_NCC_Msk |
| CCCR | PCC | 7:4 | 0xF0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CCCR_PCC_Msk |
| PWRCR | ODEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PWRCR_ODEN_Msk |
| PKGR | PKG | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_PKGR_PKG_Msk |
| UR0 | BKS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR0_BKS_Msk |
| UR0 | RDP | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR0_RDP_Msk |
| UR2 | BORH | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR2_BORH_Msk |
| UR2 | BOOT_ADD0 | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR2_BOOT_ADD0_Msk |
| UR3 | BOOT_ADD1 | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR3_BOOT_ADD1_Msk |
| UR4 | MEPAD_BANK1 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR4_MEPAD_BANK1_Msk |
| UR5 | MESAD_BANK1 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR5_MESAD_BANK1_Msk |
| UR5 | WRPN_BANK1 | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR5_WRPN_BANK1_Msk |
| UR6 | PABEG_BANK1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR6_PABEG_BANK1_Msk |
| UR6 | PAEND_BANK1 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR6_PAEND_BANK1_Msk |
| UR7 | SABEG_BANK1 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR7_SABEG_BANK1_Msk |
| UR7 | SAEND_BANK1 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR7_SAEND_BANK1_Msk |
| UR8 | MEPAD_BANK2 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR8_MEPAD_BANK2_Msk |
| UR8 | MESAD_BANK2 | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR8_MESAD_BANK2_Msk |
| UR9 | WRPN_BANK2 | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR9_WRPN_BANK2_Msk |
| UR9 | PABEG_BANK2 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR9_PABEG_BANK2_Msk |
| UR10 | PAEND_BANK2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR10_PAEND_BANK2_Msk |
| UR10 | SABEG_BANK2 | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR10_SABEG_BANK2_Msk |
| UR11 | SAEND_BANK2 | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR11_SAEND_BANK2_Msk |
| UR11 | IWDG1M | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR11_IWDG1M_Msk |
| UR12 | SECURE | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR12_SECURE_Msk |
| UR13 | SDRS | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR13_SDRS_Msk |
| UR13 | D1SBRST | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR13_D1SBRST_Msk |
| UR14 | D1STPRST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR14_D1STPRST_Msk |
| UR15 | FZIWDGSTB | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR15_FZIWDGSTB_Msk |
| UR16 | FZIWDGSTP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR16_FZIWDGSTP_Msk |
| UR16 | PKP | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR16_PKP_Msk |
| UR17 | IOHSLV | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_UR17_IOHSLV_Msk |

## Operating semantics unavailable

**syscfg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
