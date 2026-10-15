# FLASH — declarations only

Target: `stm32h743zit6_inventory`; MCU: `STM32H743ZIT6`; package: `LQFP144 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FLASH | 0x52002000 | Not asserted | Not asserted | header:FLASH_R_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ACR | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ACR |
| KEYR1 | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR1 |
| OPTKEYR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTKEYR |
| CR1 | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR1 |
| SR1 | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR1 |
| CCR1 | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CCR1 |
| OPTCR | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCR |
| OPTSR_CUR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTSR_CUR |
| OPTSR_PRG | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTSR_PRG |
| OPTCCR | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCCR |
| PRAR_CUR1 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PRAR_CUR1 |
| PRAR_PRG1 | 0x02C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PRAR_PRG1 |
| SCAR_CUR1 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SCAR_CUR1 |
| SCAR_PRG1 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SCAR_PRG1 |
| WPSN_CUR1 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WPSN_CUR1 |
| WPSN_PRG1 | 0x03C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WPSN_PRG1 |
| BOOT_CUR | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.BOOT_CUR |
| BOOT_PRG | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.BOOT_PRG |
| CRCCR1 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCCR1 |
| CRCSADD1 | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCSADD1 |
| CRCEADD1 | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCEADD1 |
| CRCDATA | 0x05C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCDATA |
| ECC_FA1 | 0x060 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ECC_FA1 |
| KEYR2 | 0x104 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR2 |
| CR2 | 0x10C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR2 |
| SR2 | 0x110 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR2 |
| CCR2 | 0x114 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CCR2 |
| PRAR_CUR2 | 0x128 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PRAR_CUR2 |
| PRAR_PRG2 | 0x12C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.PRAR_PRG2 |
| SCAR_CUR2 | 0x130 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SCAR_CUR2 |
| SCAR_PRG2 | 0x134 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SCAR_PRG2 |
| WPSN_CUR2 | 0x138 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WPSN_CUR2 |
| WPSN_PRG2 | 0x13C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.WPSN_PRG2 |
| CRCCR2 | 0x150 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCCR2 |
| CRCSADD2 | 0x154 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCSADD2 |
| CRCEADD2 | 0x158 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCEADD2 |
| CRCDATA2 | 0x15C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CRCDATA2 |
| ECC_FA2 | 0x160 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.ECC_FA2 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ACR | LATENCY | 3:0 | 0xF | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_LATENCY_Msk |
| ACR | WRHIGHFREQ | 5:4 | 0x30 | Declaration only; encoding requires reviewed semantics. | header:FLASH_ACR_WRHIGHFREQ_Msk |
| OPTCR | OPTLOCK | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTLOCK_Msk |
| OPTCR | OPTSTART | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTSTART_Msk |
| OPTCR | MER | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_MER_Msk |
| OPTCR | OPTCHANGEERRIE | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTCHANGEERRIE_Msk |
| OPTCR | SWAP_BANK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_SWAP_BANK_Msk |
| OPTCCR | CLR_OPTCHANGEERR | 30:30 | 0x40000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCCR_CLR_OPTCHANGEERR_Msk |
| CRCDATA | CRC_DATA | 31:0 | 0xFFFFFFFF | Declaration only; encoding requires reviewed semantics. | header:FLASH_CRCDATA_CRC_DATA_Msk |

## Operating semantics unavailable

**flash: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
