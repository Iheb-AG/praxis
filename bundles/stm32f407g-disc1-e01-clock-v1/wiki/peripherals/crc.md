# STM32F407 CRC — reviewed subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| CRC | 0x40023000 | AHB1 | RCC_AHB1ENR.CRCEN; AHB clock | header:CRC_BASE; rm_features_243:page:243; rm_features_244:page:244 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DR | 0x000 | 32 | — | RW | 0xFFFFFFFF | Write one 32-bit input word to advance the CRC; read the current CRC result. | header:CRC_TypeDef.DR; header:CRC_TypeDef.DR; rm_features_114:page:114 | 32 |
| IDR | 0x004 | 8 | — | RW | 0x0 | Low eight bits are independent general-purpose storage. CRC_CR.RESET does not reset IDR. Access with a 32-bit transaction despite the 8-bit CMSIS member. | header:CRC_TypeDef.IDR; header:CRC_TypeDef.IDR; rm_features_114:page:114; rm_features_115:page:115 | 32 |
| CR | 0x008 | 32 | — | RW | 0x0 | RESET is a self-clearing command; writing it reinitializes DR to 0xFFFFFFFF, without changing IDR. Reserved bits remain zero. | header:CRC_TypeDef.CR; header:CRC_TypeDef.CR; rm_features_115:page:115 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| DR | DR | 31:0 | 0xFFFFFFFF | 32-bit input word on write, computed CRC on read. | header:CRC_DR_DR_Msk; header:CRC_DR_DR_Msk; rm_features_114:page:114 |
| IDR | IDR | 7:0 | 0xFF | Independent low-eight-bit storage; upper bits reserved and kept at reset. | header:CRC_IDR_IDR_Msk; header:CRC_IDR_IDR_Msk; rm_features_115:page:115 |
| CR | RESET | 0:0 | 0x1 | Write 1 to reset the CRC calculator; hardware clears this command bit. | header:CRC_CR_RESET_Msk; header:CRC_CR_RESET_Msk; rm_features_115:page:115 |

## Reviewed operating semantics

This target implements a fixed 0x04C11DB7 polynomial with 32-bit word inputs (RM0090 pp.113–115). The host byte representation, reflection and final-XOR convention must be explicit before comparing a software CRC. Do not assume a generic CRC-32 library uses the same convention.

**Access-width correction:** the CMSIS IDR member is uint8_t, but the manual requires every CRC bus access to be a word. Use an aligned 32-bit access at CRC base + IDR offset and preserve reserved bits. The RESET field is a command, not a reset-value macro.

Route: [[peripherals/rcc]] → CRC. No board pins are required. See [[features]] and [[coverage]].

Evidence: rm_features_113:page:113, rm_features_114:page:114, rm_features_115:page:115. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources |
| --- | --- | --- | --- | --- | --- |
| word_feed | CRC | DR, IDR, CR | CR: RESET; DR: DR; IDR: IDR | Enable RCC_AHB1ENR.CRCEN.<br>Use only 32-bit bus accesses, including IDR.<br>Initialize with CRC_CR.RESET, then feed ordered 32-bit words; read DR after the feed.<br>The generator polynomial is 0x04C11DB7; byte ordering, padding and reflected host CRC conventions must be specified separately. | rm_features_113:page:113; rm_features_114:page:114; rm_features_115:page:115 |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: RM0090 Rev22 cached page evidence, import 76d4cc4fa4349310f75544d572bd2c6d326309e98f52dff9b1e044d17c85bd39. Target-scoped textual requirements; independent engineering review and new hardware qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
