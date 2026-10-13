# DWT — declarations only

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| DWT | 0xE0001000 | Not asserted | Not asserted | cmsis_core:DWT_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CTRL | 0x000 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.CTRL; cmsis_core:DWT_Type.CTRL |
| CYCCNT | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.CYCCNT; cmsis_core:DWT_Type.CYCCNT |
| CPICNT | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.CPICNT; cmsis_core:DWT_Type.CPICNT |
| EXCCNT | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.EXCCNT; cmsis_core:DWT_Type.EXCCNT |
| SLEEPCNT | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.SLEEPCNT; cmsis_core:DWT_Type.SLEEPCNT |
| LSUCNT | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.LSUCNT; cmsis_core:DWT_Type.LSUCNT |
| FOLDCNT | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.FOLDCNT; cmsis_core:DWT_Type.FOLDCNT |
| PCSR | 0x01C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.PCSR; cmsis_core:DWT_Type.PCSR |
| COMP0 | 0x020 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.COMP0; cmsis_core:DWT_Type.COMP0 |
| MASK0 | 0x024 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.MASK0; cmsis_core:DWT_Type.MASK0 |
| FUNCTION0 | 0x028 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.FUNCTION0; cmsis_core:DWT_Type.FUNCTION0 |
| COMP1 | 0x030 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.COMP1; cmsis_core:DWT_Type.COMP1 |
| MASK1 | 0x034 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.MASK1; cmsis_core:DWT_Type.MASK1 |
| FUNCTION1 | 0x038 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.FUNCTION1; cmsis_core:DWT_Type.FUNCTION1 |
| COMP2 | 0x040 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.COMP2; cmsis_core:DWT_Type.COMP2 |
| MASK2 | 0x044 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.MASK2; cmsis_core:DWT_Type.MASK2 |
| FUNCTION2 | 0x048 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.FUNCTION2; cmsis_core:DWT_Type.FUNCTION2 |
| COMP3 | 0x050 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.COMP3; cmsis_core:DWT_Type.COMP3 |
| MASK3 | 0x054 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.MASK3; cmsis_core:DWT_Type.MASK3 |
| FUNCTION3 | 0x058 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | cmsis_core:DWT_Type.FUNCTION3; cmsis_core:DWT_Type.FUNCTION3 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CTRL | CYCCNTENA | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_CYCCNTENA_Msk; cmsis_core:DWT_CTRL_CYCCNTENA_Msk |
| CTRL | POSTPRESET | 4:1 | 0x1E | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_POSTPRESET_Msk; cmsis_core:DWT_CTRL_POSTPRESET_Msk |
| CTRL | POSTINIT | 8:5 | 0x1E0 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_POSTINIT_Msk; cmsis_core:DWT_CTRL_POSTINIT_Msk |
| CTRL | CYCTAP | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_CYCTAP_Msk; cmsis_core:DWT_CTRL_CYCTAP_Msk |
| CTRL | SYNCTAP | 11:10 | 0xC00 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_SYNCTAP_Msk; cmsis_core:DWT_CTRL_SYNCTAP_Msk |
| CTRL | PCSAMPLENA | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_PCSAMPLENA_Msk; cmsis_core:DWT_CTRL_PCSAMPLENA_Msk |
| CTRL | EXCTRCENA | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_EXCTRCENA_Msk; cmsis_core:DWT_CTRL_EXCTRCENA_Msk |
| CTRL | CPIEVTENA | 17:17 | 0x20000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_CPIEVTENA_Msk; cmsis_core:DWT_CTRL_CPIEVTENA_Msk |
| CTRL | EXCEVTENA | 18:18 | 0x40000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_EXCEVTENA_Msk; cmsis_core:DWT_CTRL_EXCEVTENA_Msk |
| CTRL | SLEEPEVTENA | 19:19 | 0x80000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_SLEEPEVTENA_Msk; cmsis_core:DWT_CTRL_SLEEPEVTENA_Msk |
| CTRL | LSUEVTENA | 20:20 | 0x100000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_LSUEVTENA_Msk; cmsis_core:DWT_CTRL_LSUEVTENA_Msk |
| CTRL | FOLDEVTENA | 21:21 | 0x200000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_FOLDEVTENA_Msk; cmsis_core:DWT_CTRL_FOLDEVTENA_Msk |
| CTRL | CYCEVTENA | 22:22 | 0x400000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_CYCEVTENA_Msk; cmsis_core:DWT_CTRL_CYCEVTENA_Msk |
| CTRL | NOPRFCNT | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_NOPRFCNT_Msk; cmsis_core:DWT_CTRL_NOPRFCNT_Msk |
| CTRL | NOCYCCNT | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_NOCYCCNT_Msk; cmsis_core:DWT_CTRL_NOCYCCNT_Msk |
| CTRL | NOEXTTRIG | 26:26 | 0x4000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_NOEXTTRIG_Msk; cmsis_core:DWT_CTRL_NOEXTTRIG_Msk |
| CTRL | NOTRCPKT | 27:27 | 0x8000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_NOTRCPKT_Msk; cmsis_core:DWT_CTRL_NOTRCPKT_Msk |
| CTRL | NUMCOMP | 31:28 | 0xF0000000 | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CTRL_NUMCOMP_Msk; cmsis_core:DWT_CTRL_NUMCOMP_Msk |
| CPICNT | CPICNT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_CPICNT_CPICNT_Msk; cmsis_core:DWT_CPICNT_CPICNT_Msk |
| EXCCNT | EXCCNT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_EXCCNT_EXCCNT_Msk; cmsis_core:DWT_EXCCNT_EXCCNT_Msk |
| SLEEPCNT | SLEEPCNT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_SLEEPCNT_SLEEPCNT_Msk; cmsis_core:DWT_SLEEPCNT_SLEEPCNT_Msk |
| LSUCNT | LSUCNT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_LSUCNT_LSUCNT_Msk; cmsis_core:DWT_LSUCNT_LSUCNT_Msk |
| FOLDCNT | FOLDCNT | 7:0 | 0xFF | Declaration only; encoding requires reviewed semantics. | cmsis_core:DWT_FOLDCNT_FOLDCNT_Msk; cmsis_core:DWT_FOLDCNT_FOLDCNT_Msk |

## Operating semantics unavailable

**dwt: declarations only; operating semantics are NOT reviewed.**

Do not generate initialization code from this document alone. Register access modes, side effects, readiness checks, clock domains, pin routing, and supported modes require reviewed manual/datasheet/errata evidence. Dependencies are configuration policy from `profile:discovery`, not operating facts. See the coverage report in [[index]].

## Review

Not reviewed. Declaration extraction is not semantic review.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
