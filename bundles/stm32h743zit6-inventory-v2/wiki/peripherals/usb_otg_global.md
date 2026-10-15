# USB_OTG_GLOBAL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| USB1_OTG_HS | 0x40040000 | Not asserted | Not asserted | header:USB1_OTG_HS_PERIPH_BASE |
| USB2_OTG_FS | 0x40080000 | Not asserted | Not asserted | header:USB2_OTG_FS_PERIPH_BASE |

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
| GSNPSID | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GSNPSID | 1 | 4 |
| GHWCFG1 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GHWCFG1 | 1 | 4 |
| GHWCFG2 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GHWCFG2 | 1 | 4 |
| GHWCFG3 | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GHWCFG3 | 1 | 4 |
| GLPMCFG | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GLPMCFG | 1 | 4 |
| GPWRDN | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GPWRDN | 1 | 4 |
| GDFIFOCFG | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GDFIFOCFG | 1 | 4 |
| GADPCTL | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.GADPCTL | 1 | 4 |
| HPTXFSIZ | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.HPTXFSIZ | 1 | 4 |
| DIEPTXF | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:USB_OTG_GlobalTypeDef.DIEPTXF | 15 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**usb_otg_global: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
