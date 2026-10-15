# SYSCFG — declarations only

Target: `stm32g071rbt6_inventory`; MCU: `STM32G071RBT6`; package: `LQFP64 (pin map unreviewed)`; board revision: `not-applicable`; silicon: `unqualified`.

**Experimental MCU-only knowledge; no board wiring, active clock configuration or physical qualification is supplied.**

Prerequisites: [[index]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| SYSCFG | 0x40010000 | Not asserted | Not asserted | header:SYSCFG_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CFGR1 | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CFGR1 | 1 | 4 |
| CFGR2 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.CFGR2 | 1 | 4 |
| IT_LINE_SR | 0x080 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:SYSCFG_TypeDef.IT_LINE_SR | 32 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CFGR1 | MEM_MODE | 1:0 | 0x3 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_MEM_MODE_Msk |
| CFGR1 | PA11_RMP | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_PA11_RMP_Msk |
| CFGR1 | PA12_RMP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_PA12_RMP_Msk |
| CFGR1 | IR_POL | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_IR_POL_Msk |
| CFGR1 | IR_MOD | 7:6 | 0xC0 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_IR_MOD_Msk |
| CFGR1 | BOOSTEN | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_BOOSTEN_Msk |
| CFGR1 | UCPD1_STROBE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_UCPD1_STROBE_Msk |
| CFGR1 | UCPD2_STROBE | 10:10 | 0x400 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_UCPD2_STROBE_Msk |
| CFGR1 | I2C_PB6_FMP | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PB6_FMP_Msk |
| CFGR1 | I2C_PB7_FMP | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PB7_FMP_Msk |
| CFGR1 | I2C_PB8_FMP | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PB8_FMP_Msk |
| CFGR1 | I2C_PB9_FMP | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PB9_FMP_Msk |
| CFGR1 | I2C1_FMP | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C1_FMP_Msk |
| CFGR1 | I2C2_FMP | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C2_FMP_Msk |
| CFGR1 | I2C_PA9_FMP | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PA9_FMP_Msk |
| CFGR1 | I2C_PA10_FMP | 23:23 | 0x800000 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR1_I2C_PA10_FMP_Msk |
| CFGR2 | CLL | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR2_CLL_Msk |
| CFGR2 | SPL | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR2_SPL_Msk |
| CFGR2 | PVDL | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR2_PVDL_Msk |
| CFGR2 | ECCL | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR2_ECCL_Msk |
| CFGR2 | SPF | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:SYSCFG_CFGR2_SPF_Msk |

## Operating semantics unavailable

**syscfg: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
