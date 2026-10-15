# I2C — I2C1 standard-mode controller transmit subset

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/rcc]], [[peripherals/flash]], [[peripherals/pwr]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| I2C1 | 0x40005400 | APB1 | PCLK1=42 MHz under the declared clock contract; gate/reset required | header:I2C1_BASE; rm_i2c_842:page:842 |
| I2C2 | 0x40005800 | Not asserted | Not asserted outside reviewed workflow | header:I2C2_BASE |
| I2C3 | 0x40005C00 | Not asserted | Not asserted outside reviewed workflow | header:I2C3_BASE |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CR1 | 0x000 | 32 | — | RW | 0x0 | No CR1 write while START, STOP or PEC is hardware-pending. PE must not be cleared during active communication. Configure disabled; reserved bits stay zero. | header:I2C_TypeDef.CR1; header:I2C_TypeDef.CR1; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 | 16, 32 |
| CR2 | 0x004 | 32 | — | RW | 0x0 | FREQ is actual APB1 clock in MHz. Keep all interrupt, DMA and LAST requests zero. Contract uses only42 MHz; no intrinsic 50MHz operating claim. | header:I2C_TypeDef.CR2; header:I2C_TypeDef.CR2; rm_i2c_857:page:857; rm_i2c_858:page:858 | 16, 32 |
| OAR1 | 0x008 | 32 | — | RW | 0x0 | Bit14 must always be written1 (0x4000). Own-address target operation unsupported; ADDMODE=0 and other address bits zero. | header:I2C_TypeDef.OAR1; header:I2C_TypeDef.OAR1; rm_i2c_859:page:859 | 16, 32 |
| OAR2 | 0x00C | 32 | — | RW | 0x0 | Keep zero: no dual address or target operation. | header:I2C_TypeDef.OAR2; header:I2C_TypeDef.OAR2; rm_i2c_859:page:859 | 16, 32 |
| DR | 0x010 | 32 | — | RW | 0x0 | 16/32-bit bus access only; useful payload is low8 bits. Write address after SB/SR1, then write each payload byte only after TXE. Writing when TXE=0 is not hardware-protected. | header:I2C_TypeDef.DR; header:I2C_TypeDef.DR; rm_i2c_860:page:860 | 16, 32 |
| SR1 | 0x014 | 32 | — | mixed | 0x0 | Not W1C. Errors are rc_w0. SB clears via SR1-read then DR-write; ADDR via SR1-read then SR2-read. Do not write back a sampled status value. Preserve failure flags until explicit reset; no automatic retry. | header:I2C_TypeDef.SR1; header:I2C_TypeDef.SR1; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 | 16, 32 |
| SR2 | 0x018 | 32 | — | RO | 0x0 | Reading after SR1 clears ADDR even if it became set after the SR1 read. Read intentionally for ADDR acknowledgement or during known idle/STOP-completed stages; never as generic diagnostic polling while awaiting ADDR. | header:I2C_TypeDef.SR2; header:I2C_TypeDef.SR2; rm_i2c_863:page:863; rm_i2c_864:page:864 | 16, 32 |
| CCR | 0x01C | 32 | — | RW | 0x0 | Configure only with PE=0. Standard-mode F/S=0,DUTY=0: high=low=CCR/PCLK1, CCR=42MHz/(2*100kHz)=210. This is a recipe; actual edge timings are not measured. | header:I2C_TypeDef.CCR; header:I2C_TypeDef.CCR; rm_i2c_865:page:865 | 16, 32 |
| TRISE | 0x020 | 32 | — | RW | 0x2 | Configure only with PE=0. Standard maximum rise1000ns gives TRISE=42+1=43. Preserve reserved bits at reset. | header:I2C_TypeDef.TRISE; header:I2C_TypeDef.TRISE; rm_i2c_866:page:866 | 16, 32 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| CR1 | PE | 0:0 | 0x1 | 1 enables; disable only after completed STOP and bus idle. | header:I2C_CR1_PE_Msk; header:I2C_CR1_PE_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | SMBUS | 1:1 | 0x2 | 0 selects I2C, not SMBus. | header:I2C_CR1_SMBUS_Msk; header:I2C_CR1_SMBUS_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | SMBTYPE | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_SMBTYPE_Msk |
| CR1 | ENARP | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENARP_Msk |
| CR1 | ENPEC | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENPEC_Msk |
| CR1 | ENGC | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ENGC_Msk |
| CR1 | NOSTRETCH | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_NOSTRETCH_Msk |
| CR1 | START | 8:8 | 0x100 | Request START; hardware clears after start sent. | header:I2C_CR1_START_Msk; header:I2C_CR1_START_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | STOP | 9:9 | 0x200 | Request STOP; hardware clears when detected. | header:I2C_CR1_STOP_Msk; header:I2C_CR1_STOP_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | ACK | 10:10 | 0x400 | 0 in this transmit-only contract. | header:I2C_CR1_ACK_Msk; header:I2C_CR1_ACK_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | POS | 11:11 | 0x800 | 0; receive modes unsupported. | header:I2C_CR1_POS_Msk; header:I2C_CR1_POS_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR1 | PEC | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_PEC_Msk |
| CR1 | ALERT | 13:13 | 0x2000 | Declaration only; encoding requires reviewed semantics. | header:I2C_CR1_ALERT_Msk |
| CR1 | SWRST | 15:15 | 0x8000 | Not used: software reset recovery requires released lines/free bus and separate reviewed policy. | header:I2C_CR1_SWRST_Msk; header:I2C_CR1_SWRST_Msk; rm_i2c_855:page:855; rm_i2c_856:page:856; rm_i2c_857:page:857 |
| CR2 | FREQ | 5:0 | 0x3F | 42 at the declared PCLK1 operating point. | header:I2C_CR2_FREQ_Msk; header:I2C_CR2_FREQ_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| CR2 | ITERREN | 8:8 | 0x100 | 0 disables error interrupt. | header:I2C_CR2_ITERREN_Msk; header:I2C_CR2_ITERREN_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| CR2 | ITEVTEN | 9:9 | 0x200 | 0 disables event interrupt. | header:I2C_CR2_ITEVTEN_Msk; header:I2C_CR2_ITEVTEN_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| CR2 | ITBUFEN | 10:10 | 0x400 | 0 disables buffer interrupt. | header:I2C_CR2_ITBUFEN_Msk; header:I2C_CR2_ITBUFEN_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| CR2 | DMAEN | 11:11 | 0x800 | 0 disables DMA requests. | header:I2C_CR2_DMAEN_Msk; header:I2C_CR2_DMAEN_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| CR2 | LAST | 12:12 | 0x1000 | 0; DMA receive unsupported. | header:I2C_CR2_LAST_Msk; header:I2C_CR2_LAST_Msk; rm_i2c_857:page:857; rm_i2c_858:page:858 |
| OAR1 | ADD0 | 0:0 | 0x1 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD0_Msk |
| OAR1 | ADD1 | 1:1 | 0x2 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD1_Msk |
| OAR1 | ADD2 | 2:2 | 0x4 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD2_Msk |
| OAR1 | ADD3 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD3_Msk |
| OAR1 | ADD4 | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD4_Msk |
| OAR1 | ADD5 | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD5_Msk |
| OAR1 | ADD6 | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD6_Msk |
| OAR1 | ADD7 | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD7_Msk |
| OAR1 | ADD8 | 8:8 | 0x100 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD8_Msk |
| OAR1 | ADD9 | 9:9 | 0x200 | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR1_ADD9_Msk |
| OAR1 | ADDMODE | 15:15 | 0x8000 | 0 selects seven-bit own-address recognition; target operation is not supported by this mode. | header:I2C_OAR1_ADDMODE_Msk; header:I2C_OAR1_ADDMODE_Msk; rm_i2c_859:page:859 |
| OAR2 | ENDUAL | 0:0 | 0x1 | 0 disables dual own-address recognition. | header:I2C_OAR2_ENDUAL_Msk; header:I2C_OAR2_ENDUAL_Msk; rm_i2c_859:page:859 |
| OAR2 | ADD2 | 7:1 | 0xFE | Declaration only; encoding requires reviewed semantics. | header:I2C_OAR2_ADD2_Msk |
| DR | DR | 7:0 | 0xFF | Eight-bit address/data payload; address byte=(seven_bit_address&lt;&lt;1) with R/W=0. | header:I2C_DR_DR_Msk; header:I2C_DR_DR_Msk; rm_i2c_860:page:860 |
| SR1 | SB | 0:0 | 0x1 | START sent; read SR1 then write target address to DR. | header:I2C_SR1_SB_Msk; header:I2C_SR1_SB_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | ADDR | 1:1 | 0x2 | Seven-bit address acknowledged; read SR1 then SR2 to clear. | header:I2C_SR1_ADDR_Msk; header:I2C_SR1_ADDR_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | BTF | 2:2 | 0x4 | Final byte completed; require BTF and TXE before requesting STOP. | header:I2C_SR1_BTF_Msk; header:I2C_SR1_BTF_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | ADD10 | 3:3 | 0x8 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_ADD10_Msk |
| SR1 | STOPF | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_STOPF_Msk |
| SR1 | RXNE | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_RXNE_Msk |
| SR1 | TXE | 7:7 | 0x80 | DR empty; payload may be written. Not a transaction-completion guarantee. | header:I2C_SR1_TXE_Msk; header:I2C_SR1_TXE_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | BERR | 8:8 | 0x100 | Misplaced START/STOP; abort, retain diagnostic. | header:I2C_SR1_BERR_Msk; header:I2C_SR1_BERR_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | ARLO | 9:9 | 0x200 | Lost arbitration; hardware clears MSL/releases lines. Never generate STOP on this path. | header:I2C_SR1_ARLO_Msk; header:I2C_SR1_ARLO_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | AF | 10:10 | 0x400 | NACK; controller must generate STOP or repeated START; this mode uses bounded STOP when ownership/command state permits. | header:I2C_SR1_AF_Msk; header:I2C_SR1_AF_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | OVR | 11:11 | 0x800 | Overrun/underrun; abort. Errors clear on write0, not write1. | header:I2C_SR1_OVR_Msk; header:I2C_SR1_OVR_Msk; rm_i2c_860:page:860; rm_i2c_861:page:861; rm_i2c_862:page:862; rm_i2c_863:page:863 |
| SR1 | PECERR | 12:12 | 0x1000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_PECERR_Msk |
| SR1 | TIMEOUT | 14:14 | 0x4000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_TIMEOUT_Msk |
| SR1 | SMBALERT | 15:15 | 0x8000 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR1_SMBALERT_Msk |
| SR2 | MSL | 0:0 | 0x1 | 1 controller, cleared by STOP or arbitration loss. | header:I2C_SR2_MSL_Msk; header:I2C_SR2_MSL_Msk; rm_i2c_863:page:863; rm_i2c_864:page:864 |
| SR2 | BUSY | 1:1 | 0x2 | Communication ongoing; may stay high with stuck external line. Updated even with PE=0. | header:I2C_SR2_BUSY_Msk; header:I2C_SR2_BUSY_Msk; rm_i2c_863:page:863; rm_i2c_864:page:864 |
| SR2 | TRA | 2:2 | 0x4 | 1 transmitter; verify with MSL/BUSY when deliberately clearing ADDR. | header:I2C_SR2_TRA_Msk; header:I2C_SR2_TRA_Msk; rm_i2c_863:page:863; rm_i2c_864:page:864 |
| SR2 | GENCALL | 4:4 | 0x10 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_GENCALL_Msk |
| SR2 | SMBDEFAULT | 5:5 | 0x20 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_SMBDEFAULT_Msk |
| SR2 | SMBHOST | 6:6 | 0x40 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_SMBHOST_Msk |
| SR2 | DUALF | 7:7 | 0x80 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_DUALF_Msk |
| SR2 | PEC | 15:8 | 0xFF00 | Declaration only; encoding requires reviewed semantics. | header:I2C_SR2_PEC_Msk |
| CCR | CCR | 11:0 | 0xFFF | 210 for standard100 kHz at42 MHz; standard minimum4. | header:I2C_CCR_CCR_Msk; header:I2C_CCR_CCR_Msk; rm_i2c_865:page:865 |
| CCR | DUTY | 14:14 | 0x4000 | 0 in this standard-mode recipe. | header:I2C_CCR_DUTY_Msk; header:I2C_CCR_DUTY_Msk; rm_i2c_865:page:865 |
| CCR | FS | 15:15 | 0x8000 | 0 standard mode. | header:I2C_CCR_FS_Msk; header:I2C_CCR_FS_Msk; rm_i2c_865:page:865 |
| TRISE | TRISE | 5:0 | 0x3F | 43 for standard mode at42 MHz. | header:I2C_TRISE_TRISE_Msk; header:I2C_TRISE_TRISE_Msk; rm_i2c_866:page:866 |

## Reviewed operating semantics

Applicability: STM32F407VGT6 I2C1 only, seven-bit **controller transmitter** at standard100 kHz. The initial implementation is compile/model verified only. It does not establish a wired bus, pull-ups, target address or successful device transaction. Silicon revision/errata and independent engineering review remain pending.

Initialization: retrieve [[peripherals/rcc]], [[peripherals/flash]] and [[peripherals/pwr]] through the clock-mode dependency route. Establish the reviewed42 MHz PCLK1 operating point; under exclusive owned-startup ownership enable/read back I2C1 clock and pulse reset. With PE=0 configure CR2.FREQ=42, CCR=210 (FS=0,DUTY=0), TRISE=43, OAR1=0x4000 (mandatory bit14), OAR2=0. Interrupt/DMA/SMBus/ACK/POS requests remain zero. GPIO AF open-drain, pull-ups, electrical limits and target-device protocol require separate reviewed evidence before enabling PE or START; the wired workflow remains blocked. See [[peripherals/gpio]] and [[schemas/custom_pcb_netlist]].

Transmitter sequence: wait bus idle with a finite bound; set PE then START; wait SB and hardware-cleared START; the SR1 read followed by address DR write clears SB. Wait ADDR, then deliberately read SR2 after SR1 to clear ADDR and verify controller/transmitter/busy state. Wait TXE before each data write. After the final byte wait **BTF and TXE**, issue STOP, wait hardware command clearance and bus idle, then clear PE. A TXE-only observation is not transaction completion. Every wait is bounded; example policy limits payload to32 bytes (software policy, not a silicon limit).

Errors: sample BERR, ARLO, AF and OVR before progress flags. rc_w0 errors are **not W1C**; preserve them until explicit reset in this subset. NACK requires STOP if ownership and command state permit. ARLO releases the bus in hardware and **forbids software STOP**. No CR1 write while START/STOP/PEC remains pending; never disable PE during ongoing communication. A bounded cleanup failure is reset-required, not success; no retries or GPIO bus recovery are automated. Never poll SR2 generically while waiting ADDR: reading SR2 after SR1 can clear ADDR even when it became set between reads.

The exact header contains nine registers through TRISE. RM0090's shared register map includes FLTR but p866 restricts it to F42/F43; **FLTR is not available on F407**. CR2 p858 combines an intrinsic50 MHz statement and a greater-than42 prohibition; this contract uses only42 and does not generalize either limit. Shared-document applicability is checked against the exact target header.

Receive (including special one-/two-byte termination), ten-bit, fast-mode, target/slave, multicontroller, interrupt, DMA and SMBus modes remain unsupported. No board endpoint/device or physical I2C transaction was tested. Source provenance: rm_i2c_836:page:836; rm_i2c_842:page:842; rm_i2c_843:page:843; rm_i2c_844:page:844; rm_i2c_846:page:846; rm_i2c_855 through rm_i2c_867 (corresponding complete pages); exact header declarations. See [[sources]] and [[index]].

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| controller_transmit_polling | I2C1 | CR1, CR2, OAR1, OAR2, DR, SR1, SR2, CCR, TRISE | CCR: CCR, DUTY, FS; CR1: PE, SMBUS, START, STOP, ACK, POS, SWRST; CR2: FREQ, ITERREN, ITEVTEN, ITBUFEN, DMAEN, LAST; DR: DR; OAR1: ADDMODE; OAR2: ENDUAL; SR1: SB, ADDR, BTF, TXE, BERR, ARLO, AF, OVR; SR2: MSL, BUSY, TRA; TRISE: TRISE | Exact F407 target; exclusive owned-startup context and I2C1 ownership. Gate then pulse reset before configuration; preserve unrelated RCC bits.<br>PCLK1=42 MHz established by the required PLL operating contract. CR2=42, CCR=210, TRISE=43; configure while PE=0; OAR1 bit14=1, OAR2=0.<br>GPIO alternate-function open-drain routing, pull-ups, electrical limits and a consenting addressed target must be established separately before PE/START. This bundle adds no wired-I2C readiness.<br>Seven-bit transmitter only: SB/SR1 then address DR; ADDR/SR1 then SR2; TXE per byte; require final BTF and TXE; request STOP, wait command clear and bus idle before disabling PE.<br>No CR1 write while START/STOP/PEC pending. Every wait has a finite iteration bound. No automatic retry, bus scan or stuck-bus GPIO recovery.<br>Detect BERR/ARLO/AF/OVR before treating progress flags as success. ARLO forbids STOP. Failed/incomplete cleanup latches reset-required; never report transaction success.<br>Receiver, ten-bit, fast-mode, target/slave, multicontroller, IRQ, DMA and SMBus modes remain unsupported. F42/F43 FLTR is absent on this F407 target.<br>Controller semantics are editorially reviewed, not independently signed off or physically qualified; silicon revision and errata qualification remain open. | rm_i2c_842:page:842; rm_i2c_843:page:843; rm_i2c_844:page:844; rm_i2c_846:page:846; rm_i2c_855:page:855; rm_i2c_857:page:857; rm_i2c_859:page:859; rm_i2c_861:page:861; rm_i2c_863:page:863; rm_i2c_864:page:864; rm_i2c_865:page:865; rm_i2c_866:page:866 | [[peripherals/rcc]] / i2c1_gate_reset: RCC |

## Review

Reviewer: Codex scoped editorial review from actual Praxis ingestion MCP. Basis: Exact F407 header and complete RM0090 Rev22 parts; controller transmit subset only. Independent review, errata qualification and physical testing pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
