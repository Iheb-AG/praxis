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
