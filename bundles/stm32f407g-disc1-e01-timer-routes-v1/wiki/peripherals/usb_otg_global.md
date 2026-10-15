# USB_OTG_GLOBAL — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USB_OTG_FS | 0x50000000 | Not asserted | Not asserted | header:USB_OTG_FS_PERIPH_BASE |
| USB_OTG_FS_GLOBAL | 0x50000000 | Not asserted | Not asserted | header:USB_OTG_FS_PERIPH_BASE + USB_OTG_GLOBAL_BASE; profile:discovery.peripherals.usb_otg_global.instances.USB_OTG_FS_GLOBAL |
| USB_OTG_HS | 0x40040000 | Not asserted | Not asserted | header:USB_OTG_HS_PERIPH_BASE |
| USB_OTG_HS_GLOBAL | 0x40040000 | Not asserted | Not asserted | header:USB_OTG_HS_PERIPH_BASE + USB_OTG_GLOBAL_BASE; profile:discovery.peripherals.usb_otg_global.instances.USB_OTG_HS_GLOBAL |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GOTGCTL | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GOTGCTL | 1 | 4 |
| GOTGINT | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GOTGINT | 1 | 4 |
| GAHBCFG | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GAHBCFG | 1 | 4 |
| GUSBCFG | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GUSBCFG | 1 | 4 |
| GRSTCTL | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GRSTCTL | 1 | 4 |
| GINTSTS | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GINTSTS | 1 | 4 |
| GINTMSK | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GINTMSK | 1 | 4 |
| GRXSTSR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GRXSTSR | 1 | 4 |
| GRXSTSP | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GRXSTSP | 1 | 4 |
| GRXFSIZ | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GRXFSIZ | 1 | 4 |
| DIEPTXF0_HNPTXFSIZ | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.DIEPTXF0_HNPTXFSIZ | 1 | 4 |
| HNPTXSTS | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.HNPTXSTS | 1 | 4 |
| GCCFG | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GCCFG | 1 | 4 |
| CID | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.CID | 1 | 4 |
| HPTXFSIZ | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.HPTXFSIZ | 1 | 4 |
| DIEPTXF | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.DIEPTXF | 15 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| GOTGCTL | SRQSCS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_SRQSCS_Msk |
| GOTGCTL | SRQ | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_SRQ_Msk |
| GOTGCTL | HNGSCS | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_HNGSCS_Msk |
| GOTGCTL | HNPRQ | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_HNPRQ_Msk |
| GOTGCTL | HSHNPEN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_HSHNPEN_Msk |
| GOTGCTL | DHNPEN | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_DHNPEN_Msk |
| GOTGCTL | CIDSTS | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_CIDSTS_Msk |
| GOTGCTL | DBCT | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_DBCT_Msk |
| GOTGCTL | ASVLD | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_ASVLD_Msk |
| GOTGCTL | BSVLD | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGCTL_BSVLD_Msk |
| GOTGINT | SEDET | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_SEDET_Msk |
| GOTGINT | SRSSCHG | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_SRSSCHG_Msk |
| GOTGINT | HNSSCHG | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_HNSSCHG_Msk |
| GOTGINT | HNGDET | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_HNGDET_Msk |
| GOTGINT | ADTOCHG | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_ADTOCHG_Msk |
| GOTGINT | DBCDNE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GOTGINT_DBCDNE_Msk |
| GAHBCFG | GINT | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GAHBCFG_GINT_Msk |
| GAHBCFG | HBSTLEN | 4:1 | 0x1E | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GAHBCFG_HBSTLEN_Msk |
| GAHBCFG | DMAEN | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GAHBCFG_DMAEN_Msk |
| GAHBCFG | TXFELVL | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GAHBCFG_TXFELVL_Msk |
| GAHBCFG | PTXFELVL | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GAHBCFG_PTXFELVL_Msk |
| GUSBCFG | TOCAL | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_TOCAL_Msk |
| GUSBCFG | PHYSEL | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_PHYSEL_Msk |
| GUSBCFG | SRPCAP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_SRPCAP_Msk |
| GUSBCFG | HNPCAP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_HNPCAP_Msk |
| GUSBCFG | TRDT | 13:10 | 0x3C00 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_TRDT_Msk |
| GUSBCFG | PHYLPCS | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_PHYLPCS_Msk |
| GUSBCFG | ULPIFSLS | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPIFSLS_Msk |
| GUSBCFG | ULPIAR | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPIAR_Msk |
| GUSBCFG | ULPICSM | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPICSM_Msk |
| GUSBCFG | ULPIEVBUSD | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPIEVBUSD_Msk |
| GUSBCFG | ULPIEVBUSI | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPIEVBUSI_Msk |
| GUSBCFG | TSDPS | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_TSDPS_Msk |
| GUSBCFG | PCCI | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_PCCI_Msk |
| GUSBCFG | PTCI | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_PTCI_Msk |
| GUSBCFG | ULPIIPD | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_ULPIIPD_Msk |
| GUSBCFG | FHMOD | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_FHMOD_Msk |
| GUSBCFG | FDMOD | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_FDMOD_Msk |
| GUSBCFG | CTXPKT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GUSBCFG_CTXPKT_Msk |
| GRSTCTL | CSRST | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_CSRST_Msk |
| GRSTCTL | HSRST | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_HSRST_Msk |
| GRSTCTL | FCRST | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_FCRST_Msk |
| GRSTCTL | RXFFLSH | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_RXFFLSH_Msk |
| GRSTCTL | TXFFLSH | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_TXFFLSH_Msk |
| GRSTCTL | TXFNUM | 10:6 | 0x7C0 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_TXFNUM_Msk |
| GRSTCTL | DMAREQ | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_DMAREQ_Msk |
| GRSTCTL | AHBIDL | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRSTCTL_AHBIDL_Msk |
| GINTSTS | CMOD | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_CMOD_Msk |
| GINTSTS | MMIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_MMIS_Msk |
| GINTSTS | OTGINT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_OTGINT_Msk |
| GINTSTS | SOF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_SOF_Msk |
| GINTSTS | RXFLVL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_RXFLVL_Msk |
| GINTSTS | NPTXFE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_NPTXFE_Msk |
| GINTSTS | GINAKEFF | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_GINAKEFF_Msk |
| GINTSTS | BOUTNAKEFF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_BOUTNAKEFF_Msk |
| GINTSTS | ESUSP | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_ESUSP_Msk |
| GINTSTS | USBSUSP | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_USBSUSP_Msk |
| GINTSTS | USBRST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_USBRST_Msk |
| GINTSTS | ENUMDNE | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_ENUMDNE_Msk |
| GINTSTS | ISOODRP | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_ISOODRP_Msk |
| GINTSTS | EOPF | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_EOPF_Msk |
| GINTSTS | IEPINT | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_IEPINT_Msk |
| GINTSTS | OEPINT | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_OEPINT_Msk |
| GINTSTS | IISOIXFR | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_IISOIXFR_Msk |
| GINTSTS | PXFR_INCOMPISOOUT | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_PXFR_INCOMPISOOUT_Msk |
| GINTSTS | DATAFSUSP | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_DATAFSUSP_Msk |
| GINTSTS | HPRTINT | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_HPRTINT_Msk |
| GINTSTS | HCINT | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_HCINT_Msk |
| GINTSTS | PTXFE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_PTXFE_Msk |
| GINTSTS | CIDSCHG | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_CIDSCHG_Msk |
| GINTSTS | DISCINT | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_DISCINT_Msk |
| GINTSTS | SRQINT | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_SRQINT_Msk |
| GINTSTS | WKUINT | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTSTS_WKUINT_Msk |
| GINTMSK | MMISM | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_MMISM_Msk |
| GINTMSK | OTGINT | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_OTGINT_Msk |
| GINTMSK | SOFM | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_SOFM_Msk |
| GINTMSK | RXFLVLM | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_RXFLVLM_Msk |
| GINTMSK | NPTXFEM | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_NPTXFEM_Msk |
| GINTMSK | GINAKEFFM | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_GINAKEFFM_Msk |
| GINTMSK | GONAKEFFM | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_GONAKEFFM_Msk |
| GINTMSK | ESUSPM | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_ESUSPM_Msk |
| GINTMSK | USBSUSPM | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_USBSUSPM_Msk |
| GINTMSK | USBRST | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_USBRST_Msk |
| GINTMSK | ENUMDNEM | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_ENUMDNEM_Msk |
| GINTMSK | ISOODRPM | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_ISOODRPM_Msk |
| GINTMSK | EOPFM | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_EOPFM_Msk |
| GINTMSK | EPMISM | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_EPMISM_Msk |
| GINTMSK | IEPINT | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_IEPINT_Msk |
| GINTMSK | OEPINT | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_OEPINT_Msk |
| GINTMSK | IISOIXFRM | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_IISOIXFRM_Msk |
| GINTMSK | PXFRM_IISOOXFRM | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_PXFRM_IISOOXFRM_Msk |
| GINTMSK | FSUSPM | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_FSUSPM_Msk |
| GINTMSK | PRTIM | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_PRTIM_Msk |
| GINTMSK | HCIM | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_HCIM_Msk |
| GINTMSK | PTXFEM | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_PTXFEM_Msk |
| GINTMSK | CIDSCHGM | 28:28 | 0x10000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_CIDSCHGM_Msk |
| GINTMSK | DISCINT | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_DISCINT_Msk |
| GINTMSK | SRQIM | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_SRQIM_Msk |
| GINTMSK | WUIM | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GINTMSK_WUIM_Msk |
| GRXSTSP | EPNUM | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRXSTSP_EPNUM_Msk |
| GRXSTSP | BCNT | 14:4 | 0x7FF0 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRXSTSP_BCNT_Msk |
| GRXSTSP | DPID | 16:15 | 0x18000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRXSTSP_DPID_Msk |
| GRXSTSP | PKTSTS | 20:17 | 0x1E0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRXSTSP_PKTSTS_Msk |
| GRXFSIZ | RXFD | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GRXFSIZ_RXFD_Msk |
| GCCFG | PWRDWN | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_PWRDWN_Msk |
| GCCFG | I2CPADEN | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_I2CPADEN_Msk |
| GCCFG | VBUSASEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_VBUSASEN_Msk |
| GCCFG | VBUSBSEN | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_VBUSBSEN_Msk |
| GCCFG | SOFOUTEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_SOFOUTEN_Msk |
| GCCFG | NOVBUSSENS | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_GCCFG_NOVBUSSENS_Msk |
| CID | PRODUCT_ID | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_CID_PRODUCT_ID_Msk |
| HPTXFSIZ | PTXSA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HPTXFSIZ_PTXSA_Msk |
| HPTXFSIZ | PTXFD | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_HPTXFSIZ_PTXFD_Msk |
| DIEPTXF | INEPTXSA | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPTXF_INEPTXSA_Msk |
| DIEPTXF | INEPTXFD | 31:16 | 0xFFFF0000 | Declaration only; encoding requires reviewed semantics. | header:USB_OTG_DIEPTXF_INEPTXFD_Msk |

## Operating semantics unavailable

**usb_otg_global: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
