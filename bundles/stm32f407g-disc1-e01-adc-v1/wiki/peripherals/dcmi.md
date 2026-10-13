# DCMI — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DCMI | 0x50050000 | Not asserted | Not asserted | header:DCMI_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.CR; header:DCMI_TypeDef.CR |
| SR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.SR; header:DCMI_TypeDef.SR |
| RISR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.RISR; header:DCMI_TypeDef.RISR |
| IER | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.IER; header:DCMI_TypeDef.IER |
| MISR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.MISR; header:DCMI_TypeDef.MISR |
| ICR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.ICR; header:DCMI_TypeDef.ICR |
| ESCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.ESCR; header:DCMI_TypeDef.ESCR |
| ESUR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.ESUR; header:DCMI_TypeDef.ESUR |
| CWSTRTR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.CWSTRTR; header:DCMI_TypeDef.CWSTRTR |
| CWSIZER | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.CWSIZER; header:DCMI_TypeDef.CWSIZER |
| DR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:DCMI_TypeDef.DR; header:DCMI_TypeDef.DR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | CAPTURE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_CAPTURE_Msk; header:DCMI_CR_CAPTURE_Msk |
| CR | CM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_CM_Msk; header:DCMI_CR_CM_Msk |
| CR | CROP | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_CROP_Msk; header:DCMI_CR_CROP_Msk |
| CR | JPEG | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_JPEG_Msk; header:DCMI_CR_JPEG_Msk |
| CR | ESS | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_ESS_Msk; header:DCMI_CR_ESS_Msk |
| CR | PCKPOL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_PCKPOL_Msk; header:DCMI_CR_PCKPOL_Msk |
| CR | HSPOL | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_HSPOL_Msk; header:DCMI_CR_HSPOL_Msk |
| CR | VSPOL | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_VSPOL_Msk; header:DCMI_CR_VSPOL_Msk |
| CR | CRE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_CRE_Msk; header:DCMI_CR_CRE_Msk |
| CR | ENABLE | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_CR_ENABLE_Msk; header:DCMI_CR_ENABLE_Msk |
| SR | HSYNC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DCMI_SR_HSYNC_Msk; header:DCMI_SR_HSYNC_Msk |
| SR | VSYNC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DCMI_SR_VSYNC_Msk; header:DCMI_SR_VSYNC_Msk |
| SR | FNE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DCMI_SR_FNE_Msk; header:DCMI_SR_FNE_Msk |
| IER | FRAME_IE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DCMI_IER_FRAME_IE_Msk; header:DCMI_IER_FRAME_IE_Msk |
| IER | OVR_IE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DCMI_IER_OVR_IE_Msk; header:DCMI_IER_OVR_IE_Msk |
| IER | ERR_IE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DCMI_IER_ERR_IE_Msk; header:DCMI_IER_ERR_IE_Msk |
| IER | VSYNC_IE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DCMI_IER_VSYNC_IE_Msk; header:DCMI_IER_VSYNC_IE_Msk |
| IER | LINE_IE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DCMI_IER_LINE_IE_Msk; header:DCMI_IER_LINE_IE_Msk |
| ICR | FRAME_ISC | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ICR_FRAME_ISC_Msk; header:DCMI_ICR_FRAME_ISC_Msk |
| ICR | OVR_ISC | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ICR_OVR_ISC_Msk; header:DCMI_ICR_OVR_ISC_Msk |
| ICR | ERR_ISC | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ICR_ERR_ISC_Msk; header:DCMI_ICR_ERR_ISC_Msk |
| ICR | VSYNC_ISC | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ICR_VSYNC_ISC_Msk; header:DCMI_ICR_VSYNC_ISC_Msk |
| ICR | LINE_ISC | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ICR_LINE_ISC_Msk; header:DCMI_ICR_LINE_ISC_Msk |
| ESCR | FSC | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESCR_FSC_Msk; header:DCMI_ESCR_FSC_Msk |
| ESCR | LSC | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESCR_LSC_Msk; header:DCMI_ESCR_LSC_Msk |
| ESCR | LEC | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESCR_LEC_Msk; header:DCMI_ESCR_LEC_Msk |
| ESCR | FEC | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESCR_FEC_Msk; header:DCMI_ESCR_FEC_Msk |
| ESUR | FSU | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESUR_FSU_Msk; header:DCMI_ESUR_FSU_Msk |
| ESUR | LSU | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESUR_LSU_Msk; header:DCMI_ESUR_LSU_Msk |
| ESUR | LEU | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESUR_LEU_Msk; header:DCMI_ESUR_LEU_Msk |
| ESUR | FEU | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_ESUR_FEU_Msk; header:DCMI_ESUR_FEU_Msk |
| DR | BYTE0 | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:DCMI_DR_BYTE0_Msk; header:DCMI_DR_BYTE0_Msk |
| DR | BYTE1 | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:DCMI_DR_BYTE1_Msk; header:DCMI_DR_BYTE1_Msk |
| DR | BYTE2 | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_DR_BYTE2_Msk; header:DCMI_DR_BYTE2_Msk |
| DR | BYTE3 | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:DCMI_DR_BYTE3_Msk; header:DCMI_DR_BYTE3_Msk |

## Operating semantics unavailable

**dcmi: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
