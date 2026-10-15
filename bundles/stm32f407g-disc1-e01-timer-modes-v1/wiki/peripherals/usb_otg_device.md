# USB_OTG_DEVICE — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USB_OTG_FS_DEVICE | 0x50000800 | Not asserted | Not asserted | header:USB_OTG_FS_PERIPH_BASE + USB_OTG_DEVICE_BASE; profile:discovery.peripherals.usb_otg_device.instances.USB_OTG_FS_DEVICE |
| USB_OTG_HS_DEVICE | 0x40040800 | Not asserted | Not asserted | header:USB_OTG_HS_PERIPH_BASE + USB_OTG_DEVICE_BASE; profile:discovery.peripherals.usb_otg_device.instances.USB_OTG_HS_DEVICE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DCFG | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DCFG |
| DCTL | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DCTL |
| DSTS | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DSTS |
| DIEPMSK | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DIEPMSK |
| DOEPMSK | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DOEPMSK |
| DAINT | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DAINT |
| DAINTMSK | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DAINTMSK |
| DVBUSDIS | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DVBUSDIS |
| DVBUSPULSE | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DVBUSPULSE |
| DTHRCTL | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DTHRCTL |
| DIEPEMPMSK | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DIEPEMPMSK |
| DEACHINT | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DEACHINT |
| DEACHMSK | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DEACHMSK |
| DINEP1MSK | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DINEP1MSK |
| DOUTEP1MSK | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_DeviceTypeDef.DOUTEP1MSK |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DCFG | DSPD | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_DSPD_Msk |
| DCFG | NZLSOHSK | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_NZLSOHSK_Msk |
| DCFG | DAD | 10:4 | 0x7F0 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_DAD_Msk |
| DCFG | PFIVL | 12:11 | 0x1800 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_PFIVL_Msk |
| DCFG | XCVRDLY | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_XCVRDLY_Msk |
| DCFG | ERRATIM | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_ERRATIM_Msk |
| DCFG | PERSCHIVL | 25:24 | 0x3000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCFG_PERSCHIVL_Msk |
| DCTL | RWUSIG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_RWUSIG_Msk |
| DCTL | SDIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_SDIS_Msk |
| DCTL | GINSTS | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_GINSTS_Msk |
| DCTL | GONSTS | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_GONSTS_Msk |
| DCTL | TCTL | 6:4 | 0x70 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_TCTL_Msk |
| DCTL | SGINAK | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_SGINAK_Msk |
| DCTL | CGINAK | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_CGINAK_Msk |
| DCTL | SGONAK | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_SGONAK_Msk |
| DCTL | CGONAK | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_CGONAK_Msk |
| DCTL | POPRGDNE | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DCTL_POPRGDNE_Msk |
| DSTS | SUSPSTS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DSTS_SUSPSTS_Msk |
| DSTS | ENUMSPD | 2:1 | 0x6 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DSTS_ENUMSPD_Msk |
| DSTS | EERR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DSTS_EERR_Msk |
| DSTS | FNSOF | 21:8 | 0x3FFF00 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DSTS_FNSOF_Msk |
| DIEPMSK | XFRCM | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_XFRCM_Msk |
| DIEPMSK | EPDM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_EPDM_Msk |
| DIEPMSK | TOM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_TOM_Msk |
| DIEPMSK | ITTXFEMSK | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_ITTXFEMSK_Msk |
| DIEPMSK | INEPNMM | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_INEPNMM_Msk |
| DIEPMSK | INEPNEM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_INEPNEM_Msk |
| DIEPMSK | TXFURM | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_TXFURM_Msk |
| DIEPMSK | NAKM | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPMSK_NAKM_Msk |
| DOEPMSK | XFRCM | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_XFRCM_Msk |
| DOEPMSK | EPDM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_EPDM_Msk |
| DOEPMSK | AHBERRM | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_AHBERRM_Msk |
| DOEPMSK | STUPM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_STUPM_Msk |
| DOEPMSK | OTEPDM | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_OTEPDM_Msk |
| DOEPMSK | OTEPSPRM | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_OTEPSPRM_Msk |
| DOEPMSK | B2BSTUP | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_B2BSTUP_Msk |
| DOEPMSK | OPEM | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_OPEM_Msk |
| DOEPMSK | BOIM | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_BOIM_Msk |
| DOEPMSK | BERRM | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_BERRM_Msk |
| DOEPMSK | NAKM | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_NAKM_Msk |
| DOEPMSK | NYETM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DOEPMSK_NYETM_Msk |
| DAINT | IEPINT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DAINT_IEPINT_Msk |
| DAINT | OEPINT | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DAINT_OEPINT_Msk |
| DAINTMSK | IEPM | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DAINTMSK_IEPM_Msk |
| DAINTMSK | OEPM | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DAINTMSK_OEPM_Msk |
| DVBUSDIS | VBUSDT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DVBUSDIS_VBUSDT_Msk |
| DVBUSPULSE | DVBUSP | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DVBUSPULSE_DVBUSP_Msk |
| DTHRCTL | NONISOTHREN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_NONISOTHREN_Msk |
| DTHRCTL | ISOTHREN | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_ISOTHREN_Msk |
| DTHRCTL | TXTHRLEN | 10:2 | 0x7FC | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_TXTHRLEN_Msk |
| DTHRCTL | RXTHREN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_RXTHREN_Msk |
| DTHRCTL | RXTHRLEN | 25:17 | 0x3FE0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_RXTHRLEN_Msk |
| DTHRCTL | ARPEN | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DTHRCTL_ARPEN_Msk |
| DIEPEMPMSK | INEPTXFEM | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPEMPMSK_INEPTXFEM_Msk |
| DEACHINT | IEP1INT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DEACHINT_IEP1INT_Msk |
| DEACHINT | OEP1INT | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DEACHINT_OEP1INT_Msk |

## Operating semantics unavailable

**usb_otg_device: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
