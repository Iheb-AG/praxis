# STM32F407 IWDG — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| IWDG | 0x40003000 | Independent watchdog register interface | Independent LSI oscillator; exact frequency/tolerance not asserted | header:IWDG_BASE; rm_features_704:page:704; rm_features_705:page:705; rm_features_706:page:706 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| KR | 0x000 | 32 | — | WO | 0x0 | Key writes unlock configuration (0x5555), start (0xCCCC), or reload (0xAAAA). Reads return zero. Starting can reset the MCU; not exercised automatically. | header:IWDG_TypeDef.KR; header:IWDG_TypeDef.KR; rm_features_705:page:705; rm_features_706:page:706 | 16, 32 |
| PR | 0x004 | 32 | — | RW | 0x0 | Write only after unlocking and when PVU=0. Readback is valid only once PVU clears. | header:IWDG_TypeDef.PR; header:IWDG_TypeDef.PR; rm_features_706:page:706 | 16, 32 |
| RLR | 0x008 | 32 | — | RW | 0xFFF | Write low 12 bits only when unlocked and RVU=0. Value transfers to counter on reload. | header:IWDG_TypeDef.RLR; header:IWDG_TypeDef.RLR; rm_features_707:page:707 | 16, 32 |
| SR | 0x00C | 32 | — | RO | 0x0 | PVU/RVU report ongoing clock-domain updates; bound waits before rewriting configuration. | header:IWDG_TypeDef.SR; header:IWDG_TypeDef.SR; rm_features_707:page:707 | 16, 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| KR | KEY | 15:0 | 0xFFFF | 0x5555 unlocks PR/RLR, 0xCCCC starts, 0xAAAA reloads; other writes protect configuration. | header:IWDG_KR_KEY_Msk; header:IWDG_KR_KEY_Msk; rm_features_705:page:705; rm_features_706:page:706 |
| PR | PR | 2:0 | 0x7 | Codes 0..6 select /4,/8,/16,/32,/64,/128,/256; code 7 also /256. | header:IWDG_PR_PR_Msk; header:IWDG_PR_PR_Msk; rm_features_706:page:706 |
| RLR | RL | 11:0 | 0xFFF | 12-bit reload value; upper bits reserved at reset. | header:IWDG_RLR_RL_Msk; header:IWDG_RLR_RL_Msk; rm_features_707:page:707 |
| SR | PVU | 0:0 | 0x1 | Prescaler update pending; wait for zero before PR writes. | header:IWDG_SR_PVU_Msk; header:IWDG_SR_PVU_Msk; rm_features_707:page:707 |
| SR | RVU | 1:1 | 0x2 | Reload update pending; wait for zero before RLR writes. | header:IWDG_SR_RVU_Msk; header:IWDG_SR_RVU_Msk; rm_features_707:page:707 |

## Reviewed operating semantics

The independent watchdog uses LSI, not a precise application timebase. Do not derive a guaranteed timeout from a nominal diagram frequency. LSI tolerance and option-byte autostart assumptions require separate evidence.

Unlock using 0x5555; wait PVU/RVU=0 before protected writes and wait for synchronization before trusting readback. 0xAAAA reloads; 0xCCCC starts. Use bounded synchronization waits. Starting the watchdog can reset the target and is not authorized by retrieval or compilation. Never write option bytes as an automatic repair.

Debugger freeze behavior is not established by this contract. No watchdog start/reset hardware test has been performed. See [[peripherals/rcc]], [[features]] and [[coverage]].

Evidence: rm_features_704:page:704, rm_features_705:page:705, rm_features_706:page:706, rm_features_707:page:707, rm_features_708:page:708. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| configure_refresh | IWDG | KR, PR, RLR, SR | KR: KEY; PR: PR; RLR: RL; SR: PVU, RVU | Requires a reset/recovery plan and confirmed option-byte startup assumptions; this contract never authorizes option-byte modification.<br>LSI tolerance affects timeout; use manufacturer min/max bounds for a timing guarantee.<br>Write unlock key 0x5555; wait for PVU/RVU to clear with bounded waits, then set prescaler/reload.<br>Wait for updates to finish before relying on readback, reload with 0xAAAA and start with 0xCCCC when approved.<br>Refresh with 0xAAAA before expiry. Starting the watchdog cannot be treated as a reversible local calculation.<br>Debug halt freeze behavior is outside this mode and must be established separately. | rm_features_704:page:704; rm_features_705:page:705; rm_features_706:page:706; rm_features_707:page:707; rm_features_708:page:708 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
