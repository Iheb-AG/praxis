# OPAMP — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| OPAMP | 0x40009000 | Not asserted | Not asserted | header:OPAMP_BASE |
| OPAMP1 | 0x40009000 | Not asserted | Not asserted | header:OPAMP1_BASE |
| OPAMP2 | 0x40009010 | Not asserted | Not asserted | header:OPAMP2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CSR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OPAMP_TypeDef.CSR |
| OTR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OPAMP_TypeDef.OTR |
| HSOTR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:OPAMP_TypeDef.HSOTR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CSR | OPAMPxEN | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_OPAMPxEN_Msk |
| CSR | FORCEVP | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_FORCEVP_Msk |
| CSR | VPSEL | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_VPSEL_Msk |
| CSR | VMSEL | 6:5 | 0x60 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_VMSEL_Msk |
| CSR | OPAHSM | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_OPAHSM_Msk |
| CSR | CALON | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_CALON_Msk |
| CSR | CALSEL | 13:12 | 0x3000 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_CALSEL_Msk |
| CSR | PGGAIN | 17:14 | 0x3C000 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_PGGAIN_Msk |
| CSR | USERTRIM | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_USERTRIM_Msk |
| CSR | TSTREF | 29:29 | 0x20000000 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_TSTREF_Msk |
| CSR | CALOUT | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_CSR_CALOUT_Msk |
| OTR | TRIMOFFSETN | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:OPAMP_OTR_TRIMOFFSETN_Msk |
| OTR | TRIMOFFSETP | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_OTR_TRIMOFFSETP_Msk |
| HSOTR | TRIMHSOFFSETN | 4:0 | 0x1F | Declaration only; encoding requires reviewed semantics. | header:OPAMP_HSOTR_TRIMHSOFFSETN_Msk |
| HSOTR | TRIMHSOFFSETP | 12:8 | 0x1F00 | Declaration only; encoding requires reviewed semantics. | header:OPAMP_HSOTR_TRIMHSOFFSETP_Msk |

## Operating semantics unavailable

**opamp: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
