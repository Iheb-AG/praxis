# STM32F407 RNG — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| RNG | 0x50060800 | AHB2 | RCC_AHB2ENR.RNGEN plus valid PLL-derived RNG clock | header:RNG_BASE; rm_features_245:page:245; rm_features_763:page:763 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | RW | 0x0 | RNGEN starts generation; clearing and setting restarts after a seed fault. IE enables interrupt requests. | header:RNG_TypeDef.CR; header:RNG_TypeDef.CR; rm_features_765:page:765 | 32 |
| SR | 0x004 | 32 | — | mixed | 0x0 | DRDY/CECS/SECS are read-only. CEIS and SEIS clear by writing zero to that flag; preserve other flags when clearing a selected latch. | header:RNG_TypeDef.SR; header:RNG_TypeDef.SR; rm_features_765:page:765; rm_features_766:page:766 | 32 |
| DR | 0x008 | 32 | — | RO | 0x0 | Read only when DRDY=1 and error checks pass; reading clears DRDY. Never use errored output as entropy. | header:RNG_TypeDef.DR; header:RNG_TypeDef.DR; rm_features_766:page:766 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | RNGEN | 2:2 | 0x4 | 1 enables the RNG. | header:RNG_CR_RNGEN_Msk; header:RNG_CR_RNGEN_Msk; rm_features_765:page:765 |
| CR | IE | 3:3 | 0x8 | Interrupt enable; zero in polling mode. | header:RNG_CR_IE_Msk; header:RNG_CR_IE_Msk; rm_features_765:page:765 |
| SR | DRDY | 0:0 | 0x1 | Data ready; reading DR clears it. | header:RNG_SR_DRDY_Msk; header:RNG_SR_DRDY_Msk; rm_features_765:page:765; rm_features_766:page:766 |
| SR | CECS | 1:1 | 0x2 | Clock error current status. | header:RNG_SR_CECS_Msk; header:RNG_SR_CECS_Msk; rm_features_765:page:765; rm_features_766:page:766 |
| SR | SECS | 2:2 | 0x4 | Seed error current status. | header:RNG_SR_SECS_Msk; header:RNG_SR_SECS_Msk; rm_features_765:page:765; rm_features_766:page:766 |
| SR | CEIS | 5:5 | 0x20 | Clock-error latched status, rc_w0. | header:RNG_SR_CEIS_Msk; header:RNG_SR_CEIS_Msk; rm_features_765:page:765; rm_features_766:page:766 |
| SR | SEIS | 6:6 | 0x40 | Seed-error latched status, rc_w0. | header:RNG_SR_SEIS_Msk; header:RNG_SR_SEIS_Msk; rm_features_765:page:765; rm_features_766:page:766 |

## Reviewed operating semantics

RNG needs both its AHB2 gate and a valid separate clock. The reviewed register procedure does not prove that the reference 168 MHz PLL recipe is currently running. A complete clock setup remains blocked on FLASH/PWR operating knowledge in this feature profile.

Poll DRDY with a timeout, reject clock/seed errors, discard the first output while retaining it for consecutive comparison, and reject equal consecutive outputs. DR reads clear DRDY. Seed-error recovery clears SEIS and restarts RNGEN. CEIS/SEIS are clear-on-write-zero, unlike DMA's W1C flags.

No entropy quality, cryptographic certification or board clock measurement is claimed. See [[peripherals/rcc]], [[features]] and [[coverage]].

Evidence: rm_features_763:page:763, rm_features_764:page:764, rm_features_765:page:765, rm_features_766:page:766. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| polling_health_checks | RNG | CR, SR, DR | CR: RNGEN, IE; SR: DRDY, CECS, SECS, CEIS, SEIS | Require a verified RNG clock; RNG_CLK must not be less than HCLK/16. A clock-gate write alone is insufficient.<br>Enable the AHB2 RNG gate and RNGEN, leave interrupts disabled for polling.<br>Wait for DRDY with a bounded timeout and reject current or latched clock/seed errors before consuming DR.<br>Discard the first sample after enable but retain it for the continuous comparison; reject consecutive equal samples.<br>On seed error discard output, clear SEIS and restart RNGEN; report persistent faults.<br>These checks do not establish cryptographic certification or physical clock qualification. | rm_features_763:page:763; rm_features_764:page:764; rm_features_765:page:765; rm_features_766:page:766 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
