# PWR internal-regulator Scale1: STM32F407 subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| PWR | 0x40007000 | APB1 | RCC_APB1ENR.PWREN; separate regulator readiness | header:PWR_BASE; rm_clock_v1_141:page:141; rm_clock_v1_247:page:247 |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR | 0x000 | 32 | — | mixed | not asserted | VOS mixed with configuration and CWUF/CSBF flag-clear commands. Preserve unrelated configuration, write zero to commands. Reset 0x4000 is wake-from-Standby qualified, not unconditional. | header:PWR_TypeDef.CR; header:PWR_TypeDef.CR; rm_clock_v1_141:page:141; rm_clock_v1_142:page:142 | 32 |
| CSR | 0x004 | 32 | — | mixed | not asserted | VOSRDY is read-only; backup enable/wakeup controls and reset-domain-specific flags share CSR. Voltage-scale mode performs no CSR writes; additional APB cycles apply. | header:PWR_TypeDef.CSR; header:PWR_TypeDef.CSR; rm_clock_v1_142:page:142; rm_clock_v1_143:page:143; rm_clock_v1_144:page:144 | 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR | LPDS | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_LPDS_Msk |
| CR | PDDS | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PDDS_Msk |
| CR | CWUF | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CWUF_Msk |
| CR | CSBF | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_CSBF_Msk |
| CR | PVDE | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PVDE_Msk |
| CR | PLS | 7:5 | 0xE0 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_PLS_Msk |
| CR | DBP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_DBP_Msk |
| CR | FPDS | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CR_FPDS_Msk |
| CR | VOS | 14:14 | 0x4000 | F405/F407 single bit14: 1=Scale1,0=Scale2; choose Scale1 before 168MHz. | header:PWR_CR_VOS_Msk; header:PWR_CR_VOS_Msk; rm_clock_v1_80:page:80; rm_clock_v1_141:page:141 |
| CSR | WUF | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_WUF_Msk |
| CSR | SBF | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_SBF_Msk |
| CSR | PVDO | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_PVDO_Msk |
| CSR | BRR | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_BRR_Msk |
| CSR | EWUP | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_EWUP_Msk |
| CSR | BRE | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:PWR_CSR_BRE_Msk |
| CSR | VOSRDY | 14:14 | 0x4000 | Read-only regulator voltage-scale readiness; poll with finite budget. | header:PWR_CSR_VOSRDY_Msk; header:PWR_CSR_VOSRDY_Msk; rm_clock_v1_143:page:143 |

## Reviewed operating semantics

Reviewed subset: STM32F405/407 internal-regulator Scale 1 selection during owned startup.
VOS is the single bit 14, with 1 selecting Scale 1 and 0 Scale 2. The two-bit VOS and
over-drive procedures for F42/F43 are outside this target. At VOS=1, the reviewed HCLK
ceiling is 168 MHz; Scale 2 has a 144 MHz ceiling. Supply/package design remains a separate
precondition, not something register reads can prove.

First enable RCC_APB1ENR.PWREN and read the gate back. Set VOS while preserving unrelated
configuration, then poll the read-only PWR_CSR.VOSRDY with a finite budget. Do not raise the
clock or initialize dependent peripherals if readiness fails. Treat a timeout as a failed
initialization, not evidence that Scale 1 is established.

PWR_CR also contains CWUF/CSBF command bits that read zero and clear wake/standby flags on a
write of one. Write zero to those commands when changing VOS; do not issue a whole-register
reset or replay command/status fields. PWR_CSR is mixed access: VOSRDY and other hardware
flags are not ordinary writable controls. No CSR write is needed by this mode.

The CR reset description 0x00004000 is qualified by its wake-from-Standby reset domain.
CSR contains backup-domain state with different reset behavior. Neither word is published
as an unconditional reset value in this subset. Backup-domain writes, wake sources, PVD,
Stop/Standby entry and recovery remain outside the mode contract.

Retrieve [[peripherals/rcc]] first. The exact RCC power-interface gate mode is a prerequisite
of voltage_scale; that mode and [[peripherals/flash]] latency precede the reviewed PLL switch.
See [[features]] and [[coverage]]. No physical regulator or low-power qualification is claimed.

Evidence: rm_clock_v1_80:page:80, rm_clock_v1_120:page:120,
rm_clock_v1_141:page:141, rm_clock_v1_142:page:142,
rm_clock_v1_143:page:143, rm_clock_v1_144:page:144,
rm_clock_v1_247:page:247. Complete source pages were read through ingestion MCP.
Editorial review only; independent sign-off pending.

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| voltage_scale | PWR | CR, CSR | CR: VOS; CSR: VOSRDY | Require owned startup and internal regulator/supply assumptions; not a low-power or backup-domain procedure.<br>Enable/read back PWREN before PWR access; select VOS bit14=1, not F42/F43 two-bit encodings.<br>Write zero to CWUF/CSBF when changing VOS and preserve unrelated configuration.<br>Poll VOSRDY without writing CSR; bound the wait and abort clock escalation on failure. | rm_clock_v1_80:page:80; rm_clock_v1_120:page:120; rm_clock_v1_141:page:141; rm_clock_v1_142:page:142; rm_clock_v1_143:page:143; rm_clock_v1_144:page:144; rm_clock_v1_247:page:247 | [[peripherals/rcc]] / power_interface_gate: RCC |

## Review

Reviewer: Codex editorial synthesis from actual ingestion MCP responses. Basis: RM0090 Rev22 F405/F407-specific complete pages and exact header comparisons; independent engineering review pending.

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
