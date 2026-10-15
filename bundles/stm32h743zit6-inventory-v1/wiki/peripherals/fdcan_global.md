# FDCAN_GLOBAL — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FDCAN1 | 0x4000A000 | Not asserted | Not asserted | header:FDCAN1_BASE |
| FDCAN2 | 0x4000A400 | Not asserted | Not asserted | header:FDCAN2_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CREL | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.CREL |
| ENDN | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.ENDN |
| DBTP | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.DBTP |
| TEST | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TEST |
| RWD | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RWD |
| CCCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.CCCR |
| NBTP | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.NBTP |
| TSCC | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TSCC |
| TSCV | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TSCV |
| TOCC | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TOCC |
| TOCV | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TOCV |
| ECR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.ECR |
| PSR | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.PSR |
| TDCR | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TDCR |
| IR | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.IR |
| IE | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.IE |
| ILS | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.ILS |
| ILE | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.ILE |
| GFC | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.GFC |
| SIDFC | 0x084 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.SIDFC |
| XIDFC | 0x088 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.XIDFC |
| XIDAM | 0x090 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.XIDAM |
| HPMS | 0x094 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.HPMS |
| NDAT1 | 0x098 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.NDAT1 |
| NDAT2 | 0x09C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.NDAT2 |
| RXF0C | 0x0A0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF0C |
| RXF0S | 0x0A4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF0S |
| RXF0A | 0x0A8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF0A |
| RXBC | 0x0AC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXBC |
| RXF1C | 0x0B0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF1C |
| RXF1S | 0x0B4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF1S |
| RXF1A | 0x0B8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXF1A |
| RXESC | 0x0BC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.RXESC |
| TXBC | 0x0C0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBC |
| TXFQS | 0x0C4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXFQS |
| TXESC | 0x0C8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXESC |
| TXBRP | 0x0CC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBRP |
| TXBAR | 0x0D0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBAR |
| TXBCR | 0x0D4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBCR |
| TXBTO | 0x0D8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBTO |
| TXBCF | 0x0DC | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBCF |
| TXBTIE | 0x0E0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBTIE |
| TXBCIE | 0x0E4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXBCIE |
| TXEFC | 0x0F0 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXEFC |
| TXEFS | 0x0F4 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXEFS |
| TXEFA | 0x0F8 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FDCAN_GlobalTypeDef.TXEFA |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |

## Operating semantics unavailable

**fdcan_global: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
