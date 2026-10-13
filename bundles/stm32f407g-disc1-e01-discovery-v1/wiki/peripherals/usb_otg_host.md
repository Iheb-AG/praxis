# USB_OTG_HOST — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USB_OTG_FS_HOST | 0x50000400 | Not asserted | Not asserted | header:USB_OTG_FS_PERIPH_BASE + USB_OTG_HOST_BASE |
| USB_OTG_HS_HOST | 0x40040400 | Not asserted | Not asserted | header:USB_OTG_HS_PERIPH_BASE + USB_OTG_HOST_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HCFG | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HCFG; header:USB_OTG_HostTypeDef.HCFG |
| HFIR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HFIR; header:USB_OTG_HostTypeDef.HFIR |
| HFNUM | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HFNUM; header:USB_OTG_HostTypeDef.HFNUM |
| HPTXSTS | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HPTXSTS; header:USB_OTG_HostTypeDef.HPTXSTS |
| HAINT | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HAINT; header:USB_OTG_HostTypeDef.HAINT |
| HAINTMSK | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_HostTypeDef.HAINTMSK; header:USB_OTG_HostTypeDef.HAINTMSK |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| HCFG | FSLSPCS | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HCFG_FSLSPCS_Msk; header:USB_OTG_HCFG_FSLSPCS_Msk |
| HCFG | FSLSS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HCFG_FSLSS_Msk; header:USB_OTG_HCFG_FSLSS_Msk |
| HFIR | FRIVL | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HFIR_FRIVL_Msk; header:USB_OTG_HFIR_FRIVL_Msk |
| HFNUM | FRNUM | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HFNUM_FRNUM_Msk; header:USB_OTG_HFNUM_FRNUM_Msk |
| HFNUM | FTREM | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HFNUM_FTREM_Msk; header:USB_OTG_HFNUM_FTREM_Msk |
| HPTXSTS | PTXFSAVL | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HPTXSTS_PTXFSAVL_Msk; header:USB_OTG_HPTXSTS_PTXFSAVL_Msk |
| HPTXSTS | PTXQSAV | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HPTXSTS_PTXQSAV_Msk; header:USB_OTG_HPTXSTS_PTXQSAV_Msk |
| HPTXSTS | PTXQTOP | 31:24 | 0xFF000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HPTXSTS_PTXQTOP_Msk; header:USB_OTG_HPTXSTS_PTXQTOP_Msk |
| HAINT | HAINT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HAINT_HAINT_Msk; header:USB_OTG_HAINT_HAINT_Msk |
| HAINTMSK | HAINTM | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HAINTMSK_HAINTM_Msk; header:USB_OTG_HAINTMSK_HAINTM_Msk |

## Operating semantics unavailable

**usb_otg_host: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
