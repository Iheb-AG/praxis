# RTC — declarations only

Target: `stm32f103c8t6_inventory`; MCU: `STM32F103C8T6`; package: `LQFP48 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RTC | 0x40002800 | Not asserted | Not asserted | header:RTC_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRH | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CRH |
| CRL | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CRL |
| PRLH | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.PRLH |
| PRLL | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.PRLL |
| DIVH | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.DIVH |
| DIVL | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.DIVL |
| CNTH | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CNTH |
| CNTL | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.CNTL |
| ALRH | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRH |
| ALRL | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:RTC_TypeDef.ALRL |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CRH | SECIE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRH_SECIE_Msk |
| CRH | ALRIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRH_ALRIE_Msk |
| CRH | OWIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRH_OWIE_Msk |
| CRL | SECF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_SECF_Msk |
| CRL | ALRF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_ALRF_Msk |
| CRL | OWF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_OWF_Msk |
| CRL | RSF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_RSF_Msk |
| CRL | CNF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_CNF_Msk |
| CRL | RTOFF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:RTC_CRL_RTOFF_Msk |
| PRLH | PRL | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_PRLH_PRL_Msk |
| PRLL | PRL | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_PRLL_PRL_Msk |
| DIVH | RTC_DIV | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:RTC_DIVH_RTC_DIV_Msk |
| DIVL | RTC_DIV | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_DIVL_RTC_DIV_Msk |
| CNTH | RTC_CNT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_CNTH_RTC_CNT_Msk |
| CNTL | RTC_CNT | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_CNTL_RTC_CNT_Msk |
| ALRH | RTC_ALR | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRH_RTC_ALR_Msk |
| ALRL | RTC_ALR | 15:0 | 0xFFFF | Declaration only; encoding requires reviewed semantics. | header:RTC_ALRL_RTC_ALR_Msk |

## Operating semantics unavailable

**rtc: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
