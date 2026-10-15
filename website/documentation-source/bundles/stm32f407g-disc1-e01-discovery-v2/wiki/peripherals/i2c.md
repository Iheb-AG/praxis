# I2C — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| I2C1 | 0x40005400 | Not asserted | Not asserted | header:I2C1_BASE |
| I2C2 | 0x40005800 | Not asserted | Not asserted | header:I2C2_BASE |
| I2C3 | 0x40005C00 | Not asserted | Not asserted | header:I2C3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.CR1; header:I2C_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.CR2; header:I2C_TypeDef.CR2 |
| OAR1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.OAR1; header:I2C_TypeDef.OAR1 |
| OAR2 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.OAR2; header:I2C_TypeDef.OAR2 |
| DR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.DR; header:I2C_TypeDef.DR |
| SR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.SR1; header:I2C_TypeDef.SR1 |
| SR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.SR2; header:I2C_TypeDef.SR2 |
| CCR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.CCR; header:I2C_TypeDef.CCR |
| TRISE | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.TRISE; header:I2C_TypeDef.TRISE |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | PE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_PE_Msk; header:I2C_CR1_PE_Msk |
| CR1 | SMBUS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SMBUS_Msk; header:I2C_CR1_SMBUS_Msk |
| CR1 | SMBTYPE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SMBTYPE_Msk; header:I2C_CR1_SMBTYPE_Msk |
| CR1 | ENARP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENARP_Msk; header:I2C_CR1_ENARP_Msk |
| CR1 | ENPEC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENPEC_Msk; header:I2C_CR1_ENPEC_Msk |
| CR1 | ENGC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENGC_Msk; header:I2C_CR1_ENGC_Msk |
| CR1 | NOSTRETCH | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_NOSTRETCH_Msk; header:I2C_CR1_NOSTRETCH_Msk |
| CR1 | START | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_START_Msk; header:I2C_CR1_START_Msk |
| CR1 | STOP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_STOP_Msk; header:I2C_CR1_STOP_Msk |
| CR1 | ACK | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ACK_Msk; header:I2C_CR1_ACK_Msk |
| CR1 | POS | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_POS_Msk; header:I2C_CR1_POS_Msk |
| CR1 | PEC | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_PEC_Msk; header:I2C_CR1_PEC_Msk |
| CR1 | ALERT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ALERT_Msk; header:I2C_CR1_ALERT_Msk |
| CR1 | SWRST | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SWRST_Msk; header:I2C_CR1_SWRST_Msk |
| CR2 | FREQ | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_FREQ_Msk; header:I2C_CR2_FREQ_Msk |
| CR2 | ITERREN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_ITERREN_Msk; header:I2C_CR2_ITERREN_Msk |
| CR2 | ITEVTEN | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_ITEVTEN_Msk; header:I2C_CR2_ITEVTEN_Msk |
| CR2 | ITBUFEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_ITBUFEN_Msk; header:I2C_CR2_ITBUFEN_Msk |
| CR2 | DMAEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_DMAEN_Msk; header:I2C_CR2_DMAEN_Msk |
| CR2 | LAST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_LAST_Msk; header:I2C_CR2_LAST_Msk |
| OAR1 | ADD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD0_Msk; header:I2C_OAR1_ADD0_Msk |
| OAR1 | ADD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD1_Msk; header:I2C_OAR1_ADD1_Msk |
| OAR1 | ADD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD2_Msk; header:I2C_OAR1_ADD2_Msk |
| OAR1 | ADD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD3_Msk; header:I2C_OAR1_ADD3_Msk |
| OAR1 | ADD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD4_Msk; header:I2C_OAR1_ADD4_Msk |
| OAR1 | ADD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD5_Msk; header:I2C_OAR1_ADD5_Msk |
| OAR1 | ADD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD6_Msk; header:I2C_OAR1_ADD6_Msk |
| OAR1 | ADD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD7_Msk; header:I2C_OAR1_ADD7_Msk |
| OAR1 | ADD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD8_Msk; header:I2C_OAR1_ADD8_Msk |
| OAR1 | ADD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD9_Msk; header:I2C_OAR1_ADD9_Msk |
| OAR1 | ADDMODE | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADDMODE_Msk; header:I2C_OAR1_ADDMODE_Msk |
| OAR2 | ENDUAL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR2_ENDUAL_Msk; header:I2C_OAR2_ENDUAL_Msk |
| OAR2 | ADD2 | 7:1 | 0xFE | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR2_ADD2_Msk; header:I2C_OAR2_ADD2_Msk |
| DR | DR | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:I2C_DR_DR_Msk; header:I2C_DR_DR_Msk |
| SR1 | SB | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_SB_Msk; header:I2C_SR1_SB_Msk |
| SR1 | ADDR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_ADDR_Msk; header:I2C_SR1_ADDR_Msk |
| SR1 | BTF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_BTF_Msk; header:I2C_SR1_BTF_Msk |
| SR1 | ADD10 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_ADD10_Msk; header:I2C_SR1_ADD10_Msk |
| SR1 | STOPF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_STOPF_Msk; header:I2C_SR1_STOPF_Msk |
| SR1 | RXNE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_RXNE_Msk; header:I2C_SR1_RXNE_Msk |
| SR1 | TXE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_TXE_Msk; header:I2C_SR1_TXE_Msk |
| SR1 | BERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_BERR_Msk; header:I2C_SR1_BERR_Msk |
| SR1 | ARLO | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_ARLO_Msk; header:I2C_SR1_ARLO_Msk |
| SR1 | AF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_AF_Msk; header:I2C_SR1_AF_Msk |
| SR1 | OVR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_OVR_Msk; header:I2C_SR1_OVR_Msk |
| SR1 | PECERR | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_PECERR_Msk; header:I2C_SR1_PECERR_Msk |
| SR1 | TIMEOUT | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_TIMEOUT_Msk; header:I2C_SR1_TIMEOUT_Msk |
| SR1 | SMBALERT | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_SMBALERT_Msk; header:I2C_SR1_SMBALERT_Msk |
| SR2 | MSL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_MSL_Msk; header:I2C_SR2_MSL_Msk |
| SR2 | BUSY | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_BUSY_Msk; header:I2C_SR2_BUSY_Msk |
| SR2 | TRA | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_TRA_Msk; header:I2C_SR2_TRA_Msk |
| SR2 | GENCALL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_GENCALL_Msk; header:I2C_SR2_GENCALL_Msk |
| SR2 | SMBDEFAULT | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_SMBDEFAULT_Msk; header:I2C_SR2_SMBDEFAULT_Msk |
| SR2 | SMBHOST | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_SMBHOST_Msk; header:I2C_SR2_SMBHOST_Msk |
| SR2 | DUALF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_DUALF_Msk; header:I2C_SR2_DUALF_Msk |
| SR2 | PEC | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_PEC_Msk; header:I2C_SR2_PEC_Msk |
| CCR | CCR | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:I2C_CCR_CCR_Msk; header:I2C_CCR_CCR_Msk |
| CCR | DUTY | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CCR_DUTY_Msk; header:I2C_CCR_DUTY_Msk |
| CCR | FS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CCR_FS_Msk; header:I2C_CCR_FS_Msk |
| TRISE | TRISE | 5:0 | 0x3F | Declaration only; encoding requires reviewed semantics. | header:I2C_TRISE_TRISE_Msk; header:I2C_TRISE_TRISE_Msk |

## Operating semantics unavailable

**i2c: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
