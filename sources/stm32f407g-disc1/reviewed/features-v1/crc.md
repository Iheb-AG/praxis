This target implements a fixed 0x04C11DB7 polynomial with 32-bit word inputs (RM0090 pp.113–115). The host byte representation, reflection and final-XOR convention must be explicit before comparing a software CRC. Do not assume a generic CRC-32 library uses the same convention.

**Access-width correction:** the CMSIS IDR member is uint8_t, but the manual requires every CRC bus access to be a word. Use an aligned 32-bit access at CRC base + IDR offset and preserve reserved bits. The RESET field is a command, not a reset-value macro.

Route: [[peripherals/rcc]] → CRC. No board pins are required. See [[features]] and [[coverage]].

Evidence: rm_features_113:page:113, rm_features_114:page:114, rm_features_115:page:115. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
