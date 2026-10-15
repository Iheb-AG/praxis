# I2C — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| I2C1 | 0x40005400 | Not asserted | Not asserted | header:I2C1_BASE |
| I2C2 | 0x40005800 | Not asserted | Not asserted | header:I2C2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.CR1 |
| CR2 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.CR2 |
| OAR1 | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.OAR1 |
| OAR2 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.OAR2 |
| TIMINGR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.TIMINGR |
| TIMEOUTR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.TIMEOUTR |
| ISR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.ISR |
| ICR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.ICR |
| PECR | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.PECR |
| RXDR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.RXDR |
| TXDR | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:I2C_TypeDef.TXDR |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | PE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_PE_Msk |
| CR1 | TXIE | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_TXIE_Msk |
| CR1 | RXIE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_RXIE_Msk |
| CR1 | ADDRIE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ADDRIE_Msk |
| CR1 | NACKIE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_NACKIE_Msk |
| CR1 | STOPIE | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_STOPIE_Msk |
| CR1 | TCIE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_TCIE_Msk |
| CR1 | ERRIE | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ERRIE_Msk |
| CR1 | DNF | 11:8 | 0xF00 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_DNF_Msk |
| CR1 | ANFOFF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ANFOFF_Msk |
| CR1 | SWRST | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SWRST_Msk |
| CR1 | TXDMAEN | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_TXDMAEN_Msk |
| CR1 | RXDMAEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_RXDMAEN_Msk |
| CR1 | SBC | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SBC_Msk |
| CR1 | NOSTRETCH | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_NOSTRETCH_Msk |
| CR1 | WUPEN | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_WUPEN_Msk |
| CR1 | GCEN | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_GCEN_Msk |
| CR1 | SMBHEN | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SMBHEN_Msk |
| CR1 | SMBDEN | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SMBDEN_Msk |
| CR1 | ALERTEN | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ALERTEN_Msk |
| CR1 | PECEN | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_PECEN_Msk |
| CR2 | SADD | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_SADD_Msk |
| CR2 | RD_WRN | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_RD_WRN_Msk |
| CR2 | ADD10 | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_ADD10_Msk |
| CR2 | HEAD10R | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_HEAD10R_Msk |
| CR2 | START | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_START_Msk |
| CR2 | STOP | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_STOP_Msk |
| CR2 | NACK | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_NACK_Msk |
| CR2 | NBYTES | 23:16 | 0xFF0000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_NBYTES_Msk |
| CR2 | RELOAD | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_RELOAD_Msk |
| CR2 | AUTOEND | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_AUTOEND_Msk |
| CR2 | PECBYTE | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR2_PECBYTE_Msk |
| OAR1 | OA1 | 9:0 | 0x3FF | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_OA1_Msk |
| OAR1 | OA1MODE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_OA1MODE_Msk |
| OAR1 | OA1EN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_OA1EN_Msk |
| TIMINGR | SCLL | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMINGR_SCLL_Msk |
| TIMINGR | SCLH | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMINGR_SCLH_Msk |
| TIMINGR | SDADEL | 19:16 | 0xF0000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMINGR_SDADEL_Msk |
| TIMINGR | SCLDEL | 23:20 | 0xF00000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMINGR_SCLDEL_Msk |
| TIMINGR | PRESC | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMINGR_PRESC_Msk |
| TIMEOUTR | TIMEOUTA | 11:0 | 0xFFF | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMEOUTR_TIMEOUTA_Msk |
| TIMEOUTR | TIDLE | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMEOUTR_TIDLE_Msk |
| TIMEOUTR | TIMOUTEN | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMEOUTR_TIMOUTEN_Msk |
| TIMEOUTR | TIMEOUTB | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMEOUTR_TIMEOUTB_Msk |
| TIMEOUTR | TEXTEN | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:I2C_TIMEOUTR_TEXTEN_Msk |
| ISR | TXE | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_TXE_Msk |
| ISR | TXIS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_TXIS_Msk |
| ISR | RXNE | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_RXNE_Msk |
| ISR | ADDR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_ADDR_Msk |
| ISR | NACKF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_NACKF_Msk |
| ISR | STOPF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_STOPF_Msk |
| ISR | TC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_TC_Msk |
| ISR | TCR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_TCR_Msk |
| ISR | BERR | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_BERR_Msk |
| ISR | ARLO | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_ARLO_Msk |
| ISR | OVR | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_OVR_Msk |
| ISR | PECERR | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_PECERR_Msk |
| ISR | TIMEOUT | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_TIMEOUT_Msk |
| ISR | ALERT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_ALERT_Msk |
| ISR | BUSY | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_BUSY_Msk |
| ISR | DIR | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_DIR_Msk |
| ISR | ADDCODE | 23:17 | 0xFE0000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ISR_ADDCODE_Msk |
| ICR | ADDRCF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_ADDRCF_Msk |
| ICR | NACKCF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_NACKCF_Msk |
| ICR | STOPCF | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_STOPCF_Msk |
| ICR | BERRCF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_BERRCF_Msk |
| ICR | ARLOCF | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_ARLOCF_Msk |
| ICR | OVRCF | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_OVRCF_Msk |
| ICR | PECCF | 11:11 | 0x800 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_PECCF_Msk |
| ICR | TIMOUTCF | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_TIMOUTCF_Msk |
| ICR | ALERTCF | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_ICR_ALERTCF_Msk |
| PECR | PEC | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:I2C_PECR_PEC_Msk |
| RXDR | RXDATA | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:I2C_RXDR_RXDATA_Msk |
| TXDR | TXDATA | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | header:I2C_TXDR_TXDATA_Msk |

## Operating semantics unavailable

**i2c: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

Mask extraction gaps:

- OAR2: bit fields withheld: UNSUPPORTED_MASK: I2C_OAR2_OA2MASK05_Msk: non-contiguous bit field

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
