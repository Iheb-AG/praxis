# TAMP — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| TAMP | 0x4000B000 | Not asserted | Not asserted | header:TAMP_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.CR2 |
| FLTCR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.FLTCR |
| IER | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.IER |
| SR | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.SR |
| MISR | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.MISR |
| SCR | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.SCR |
| BKP0R | 0x100 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.BKP0R |
| BKP1R | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.BKP1R |
| BKP2R | 0x108 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.BKP2R |
| BKP3R | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.BKP3R |
| BKP4R | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:TAMP_TypeDef.BKP4R |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | TAMP1E | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_TAMP1E_Msk |
| CR1 | TAMP2E | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_TAMP2E_Msk |
| CR1 | ITAMP3E | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_ITAMP3E_Msk |
| CR1 | ITAMP4E | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_ITAMP4E_Msk |
| CR1 | ITAMP5E | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_ITAMP5E_Msk |
| CR1 | ITAMP6E | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR1_ITAMP6E_Msk |
| CR2 | TAMP1NOERASE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP1NOERASE_Msk |
| CR2 | TAMP2NOERASE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP2NOERASE_Msk |
| CR2 | TAMP1MSK | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP1MSK_Msk |
| CR2 | TAMP2MSK | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP2MSK_Msk |
| CR2 | TAMP1TRG | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP1TRG_Msk |
| CR2 | TAMP2TRG | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_CR2_TAMP2TRG_Msk |
| FLTCR | TAMPFREQ | 2:0 | 0x7 | Declaration only; encoding requires reviewed semantics. | header:TAMP_FLTCR_TAMPFREQ_Msk |
| FLTCR | TAMPFLT | 4:3 | 0x18 | Declaration only; encoding requires reviewed semantics. | header:TAMP_FLTCR_TAMPFLT_Msk |
| FLTCR | TAMPPRCH | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:TAMP_FLTCR_TAMPPRCH_Msk |
| FLTCR | TAMPPUDIS | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:TAMP_FLTCR_TAMPPUDIS_Msk |
| IER | TAMP1IE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_TAMP1IE_Msk |
| IER | TAMP2IE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_TAMP2IE_Msk |
| IER | ITAMP3IE | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_ITAMP3IE_Msk |
| IER | ITAMP4IE | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_ITAMP4IE_Msk |
| IER | ITAMP5IE | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_ITAMP5IE_Msk |
| IER | ITAMP6IE | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_IER_ITAMP6IE_Msk |
| SR | TAMP1F | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_TAMP1F_Msk |
| SR | TAMP2F | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_TAMP2F_Msk |
| SR | ITAMP3F | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_ITAMP3F_Msk |
| SR | ITAMP4F | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_ITAMP4F_Msk |
| SR | ITAMP5F | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_ITAMP5F_Msk |
| SR | ITAMP6F | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SR_ITAMP6F_Msk |
| MISR | TAMP1MF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_TAMP1MF_Msk |
| MISR | TAMP2MF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_TAMP2MF_Msk |
| MISR | ITAMP3MF | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_ITAMP3MF_Msk |
| MISR | ITAMP4MF | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_ITAMP4MF_Msk |
| MISR | ITAMP5MF | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_ITAMP5MF_Msk |
| MISR | ITAMP6MF | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_MISR_ITAMP6MF_Msk |
| SCR | CTAMP1F | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CTAMP1F_Msk |
| SCR | CTAMP2F | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CTAMP2F_Msk |
| SCR | CITAMP3F | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CITAMP3F_Msk |
| SCR | CITAMP4F | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CITAMP4F_Msk |
| SCR | CITAMP5F | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CITAMP5F_Msk |
| SCR | CITAMP6F | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:TAMP_SCR_CITAMP6F_Msk |
| BKP0R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TAMP_BKP0R_Msk |
| BKP1R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TAMP_BKP1R_Msk |
| BKP2R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TAMP_BKP2R_Msk |
| BKP3R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TAMP_BKP3R_Msk |
| BKP4R |  | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:TAMP_BKP4R_Msk |

## Operating semantics unavailable

**tamp: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
