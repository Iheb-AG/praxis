# FLASH read-interface timing: STM32F407 subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| FLASH | 0x40023C00 | Internal Flash interface; HCLK read timing | HCLK; selected latency operating point only | header:FLASH_BASE; rm_clock_v1_80:page:80; rm_clock_v1_98:page:98 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ACR | 0x000 | 32 | — | mixed | 0x0 | Latency/configuration mixed with cache-reset commands; reserved bits 31:13 and7:3 zero; never issue reset commands during latency updates. | header:FLASH_TypeDef.ACR; header:FLASH_TypeDef.ACR; rm_clock_v1_98:page:98 | 8, 16, 32 |
| KEYR | 0x004 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.KEYR | not asserted |
| OPTKEYR | 0x008 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTKEYR | not asserted |
| SR | 0x00C | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.SR | not asserted |
| CR | 0x010 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.CR | not asserted |
| OPTCR | 0x014 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCR | not asserted |
| OPTCR1 | 0x018 | 32 | — | unknown | not asserted | Not asserted; consult reviewed operating semantics. | header:FLASH_TypeDef.OPTCR1 | not asserted |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ACR | LATENCY | 2:0 | 0x7 | Flash read latency: 0..7 wait states; 5 required for declared 168MHz HCLK and 2.7-3.6V. | header:FLASH_ACR_LATENCY_Msk; header:FLASH_ACR_LATENCY_Msk; rm_clock_v1_80:page:80; rm_clock_v1_81:page:81; rm_clock_v1_82:page:82; rm_clock_v1_98:page:98 |
| ACR | PRFTEN | 8:8 | 0x100 | Prefetch enable; not enabled by this mode; supply and silicon errata review required. | header:FLASH_ACR_PRFTEN_Msk; header:FLASH_ACR_PRFTEN_Msk; rm_clock_v1_80:page:80; rm_clock_v1_98:page:98 |
| ACR | ICEN | 9:9 | 0x200 | Instruction-cache enable; unchanged by latency mode. | header:FLASH_ACR_ICEN_Msk; header:FLASH_ACR_ICEN_Msk; rm_clock_v1_98:page:98 |
| ACR | DCEN | 10:10 | 0x400 | Data-cache enable; unchanged by latency mode. | header:FLASH_ACR_DCEN_Msk; header:FLASH_ACR_DCEN_Msk; rm_clock_v1_98:page:98 |
| ACR | ICRST | 11:11 | 0x800 | Instruction-cache reset command; writable only while that cache is disabled; never replay during latency update. | header:FLASH_ACR_ICRST_Msk; header:FLASH_ACR_ICRST_Msk; rm_clock_v1_98:page:98 |
| ACR | DCRST | 12:12 | 0x1000 | Data-cache reset command; writable only while that cache is disabled; never replay during latency update. | header:FLASH_ACR_DCRST_Msk; header:FLASH_ACR_DCRST_Msk; rm_clock_v1_98:page:98 |
| SR | EOP | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_EOP_Msk |
| SR | OPERR | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_OPERR_Msk |
| SR | WRPERR | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_WRPERR_Msk |
| SR | PGAERR | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGAERR_Msk |
| SR | PGPERR | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGPERR_Msk |
| SR | PGSERR | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_PGSERR_Msk |
| SR | BSY | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_SR_BSY_Msk |
| CR | PG | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PG_Msk |
| CR | SER | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_SER_Msk |
| CR | MER | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_MER_Msk |
| CR | SNB | 6:3 | 0x78 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_SNB_Msk |
| CR | PSIZE | 9:8 | 0x300 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_PSIZE_Msk |
| CR | STRT | 16:16 | 0x10000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_STRT_Msk |
| CR | EOPIE | 24:24 | 0x1000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_EOPIE_Msk |
| CR | ERRIE | 25:25 | 0x2000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_ERRIE_Msk |
| CR | LOCK | 31:31 | 0x80000000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_CR_LOCK_Msk |
| OPTCR | OPTLOCK | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTLOCK_Msk |
| OPTCR | OPTSTRT | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_OPTSTRT_Msk |
| OPTCR | BOR_LEV | 3:2 | 0xC | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_BOR_LEV_Msk |
| OPTCR | WDG_SW | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_WDG_SW_Msk |
| OPTCR | nRST_STOP | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nRST_STOP_Msk |
| OPTCR | nRST_STDBY | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nRST_STDBY_Msk |
| OPTCR | RDP | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_RDP_Msk |
| OPTCR | nWRP | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR_nWRP_Msk |
| OPTCR1 | nWRP | 27:16 | 0xFFF0000 | Declaration only; encoding requires reviewed semantics. | header:FLASH_OPTCR1_nWRP_Msk |

## Reviewed operating semantics

Reviewed subset: STM32F405/407 FLASH_ACR read-interface timing only. This is not flash
programming, option-byte, bootloader, cache-maintenance or low-power support. Other register
rows remain declarations. The F42/F43 register variants in the shared manual do not apply.

For the declared 2.7–3.6 V supply and Scale 1, 168 MHz HCLK requires LATENCY=5. Set and read
back latency before raising HCLK. When lowering frequency, first confirm the lower clock via
RCC SWS/prescalers; only then lower latency and read it back. Bound each acknowledgement wait
and stop initialization on failure. The loop budget is not a measured time deadline.

LATENCY is bits 2:0 for this target. Reserved bits 7:3 and 31:13 stay zero. ICEN/DCEN and
PRFTEN are separate controls. ICRST/DCRST are write commands permitted only while their
respective caches are disabled: never replay those command bits during a latency update.
This contract does not enable prefetch, change cache state or substitute for silicon errata
review. Prefetch must be disabled below 2.1 V, outside the supported operating point.

HEDG document retrieval starts with [[peripherals/rcc]]. The operating-mode graph separately
requires this latency contract before the high-speed RCC switch. See [[peripherals/pwr]],
[[features]] and [[coverage]]. No code execution, flash write or physical clock test was performed.

Evidence: rm_clock_v1_80:page:80 (voltage scale and frequency limits),
rm_clock_v1_81:page:81/table:1 (F405/F407 latency table),
rm_clock_v1_82:page:82 (increase/decrease ordering), rm_clock_v1_98:page:98 (ACR fields/access).
All complete pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| latency_168mhz | FLASH | ACR | ACR: LATENCY | Require declared supply range and Scale1; do not infer supply from an MCU register.<br>Set LATENCY=5 and confirm it before raising HCLK; lower HCLK and confirm before reducing latency.<br>Preserve unrelated RW configuration, keep reserved fields zero and write zero to cache-reset commands.<br>Use bounded acknowledgement polling and abort dependent initialization on failure; prefetch/cache/flash programming excluded. | rm_clock_v1_80:page:80; rm_clock_v1_81:page:81; rm_clock_v1_82:page:82; rm_clock_v1_98:page:98 |

## Review

Reviewer: Codex editorial synthesis from actual ingestion MCP responses. Basis: RM0090 Rev22 F405/F407-specific complete pages and exact header comparisons; independent engineering review pending.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
