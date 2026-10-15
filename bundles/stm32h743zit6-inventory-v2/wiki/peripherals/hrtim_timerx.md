# HRTIM_TIMERX — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| HRTIM1_TIMA | 0x40017480 | Not asserted | Not asserted | header:HRTIM1_TIMA_BASE |
| HRTIM1_TIMB | 0x40017500 | Not asserted | Not asserted | header:HRTIM1_TIMB_BASE |
| HRTIM1_TIMC | 0x40017580 | Not asserted | Not asserted | header:HRTIM1_TIMC_BASE |
| HRTIM1_TIMD | 0x40017600 | Not asserted | Not asserted | header:HRTIM1_TIMD_BASE |
| HRTIM1_TIME | 0x40017680 | Not asserted | Not asserted | header:HRTIM1_TIME_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TIMxCR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.TIMxCR |
| TIMxISR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.TIMxISR |
| TIMxICR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.TIMxICR |
| TIMxDIER | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.TIMxDIER |
| CNTxR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CNTxR |
| PERxR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.PERxR |
| REPxR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.REPxR |
| CMP1xR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CMP1xR |
| CMP1CxR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CMP1CxR |
| CMP2xR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CMP2xR |
| CMP3xR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CMP3xR |
| CMP4xR | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CMP4xR |
| CPT1xR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CPT1xR |
| CPT2xR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CPT2xR |
| DTxR | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.DTxR |
| SETx1R | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.SETx1R |
| RSTx1R | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.RSTx1R |
| SETx2R | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.SETx2R |
| RSTx2R | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.RSTx2R |
| EEFxR1 | 0x04C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.EEFxR1 |
| EEFxR2 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.EEFxR2 |
| RSTxR | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.RSTxR |
| CHPxR | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CHPxR |
| CPT1xCR | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CPT1xCR |
| CPT2xCR | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.CPT2xCR |
| OUTxR | 0x064 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.OUTxR |
| FLTxR | 0x068 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:HRTIM_Timerx_TypeDef.FLTxR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**hrtim_timerx: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
