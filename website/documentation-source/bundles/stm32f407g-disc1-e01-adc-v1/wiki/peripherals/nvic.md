# NVIC: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/usart]], [[peripherals/tim]], [[peripherals/exti]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| NVIC | 0xE000E100 | Core PPB | Processor clock; device IRQ slots only | cmsis_core:NVIC_BASE; nvic_review:instance:NVIC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISER | 0x000 | 32 | — | RW | not asserted | Write-one sets enable; zero has no effect. | cmsis_core:NVIC_Type.ISER; nvic_review:ISER | 8 | 4 |
| ICER | 0x080 | 32 | — | RW | not asserted | Write-one clears enable; zero has no effect. | cmsis_core:NVIC_Type.ICER; nvic_review:ICER | 8 | 4 |
| ISPR | 0x100 | 32 | — | RW | not asserted | Write-one sets pending; zero has no effect. | cmsis_core:NVIC_Type.ISPR; nvic_review:ISPR | 8 | 4 |
| ICPR | 0x180 | 32 | — | RW | not asserted | Write-one clears pending; zero has no effect. | cmsis_core:NVIC_Type.ICPR; nvic_review:ICPR | 8 | 4 |
| IABR | 0x200 | 32 | — | RO | not asserted | Read-only active state. | cmsis_core:NVIC_Type.IABR; nvic_review:IABR | 8 | 4 |
| IP | 0x300 | 8 | — | RW | not asserted | Implemented high four bits per priority byte. | cmsis_core:NVIC_Type.IP; nvic_review:IP | 240 | 1 |
| STIR | 0xE00 | 32 | — | WO | not asserted | Write IRQ number to pend a supported device interrupt; privilege rules apply. | cmsis_core:NVIC_Type.STIR; nvic_review:STIR | 1 | 4 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Write-one sets enable; zero has no effect. | cmsis_core:NVIC_Type.ISER; nvic_review:ISER; cmsis_core:NVIC_Type.ISER |
| ICER | IRQ_BITS | 31:0 | 0xFFFFFFFF | Write-one clears enable; zero has no effect. | cmsis_core:NVIC_Type.ICER; nvic_review:ICER; cmsis_core:NVIC_Type.ICER |
| ISPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Write-one sets pending; zero has no effect. | cmsis_core:NVIC_Type.ISPR; nvic_review:ISPR; cmsis_core:NVIC_Type.ISPR |
| ICPR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Write-one clears pending; zero has no effect. | cmsis_core:NVIC_Type.ICPR; nvic_review:ICPR; cmsis_core:NVIC_Type.ICPR |
| IABR | IRQ_BITS | 31:0 | 0xFFFFFFFF | Read-only active state. | cmsis_core:NVIC_Type.IABR; nvic_review:IABR; cmsis_core:NVIC_Type.IABR |
| IP | PRIORITY | 7:4 | 0xF0 | Implemented high four bits per priority byte. | header:__NVIC_PRIO_BITS; cmsis_core:NVIC_Type.IP; nvic_review:IP; header:__NVIC_PRIO_BITS; cmsis_core:NVIC_Type.IP |
| STIR | INTID | 8:0 | 0x1FF | Write IRQ number to pend a supported device interrupt; privilege rules apply. | cmsis_core:NVIC_STIR_INTID_Msk; nvic_review:STIR; cmsis_core:NVIC_STIR_INTID_Msk |

## Reviewed operating semantics

Supported workflow: USART2 external IRQ38, vector-table slot 54, handler
USART2_IRQHandler. Four priority bits are implemented. Evidence:
`header:USART2_IRQn` and `header:__NVIC_PRIO_BITS`.

1. Keep global interrupts masked and USART2 RXNEIE/NVIC line disabled while
   installing the vector and initializing handler state.
2. Complete [[peripherals/rcc]], [[peripherals/gpio]], and [[peripherals/usart]].
3. Drain receive/error causes using the documented SR/DR procedure; clear the
   peripheral cause before clearing NVIC pending state.
4. Set IP[38]'s implemented high four bits. Clear pending with ICPR[1] bit6.
5. Enable the receive source and ISER[1] bit6 only after the handler is ready;
   restore the caller's intended global interrupt state last.

ISER/ICER/ISPR/ICPR are write-one action banks, not generic read-modify-write
controls. IABR reports active state. Core arrays describe the architectural
address layout; unimplemented device interrupt slots are reserved. Do not
enable IRQs based only on the array capacity. The priority values of core
exceptions are handled separately through the system-control block.

STIR is a software-pending action subject to privilege and implemented IRQ
limits. This fixture does not invoke it. DMA configuration must precede enabling
USART DMA requests; full DMA registers and stream routing remain unsupported
until reviewed DMA knowledge is added. No source is safe merely because its
documents were retrieved.

Evidence: `nvic_review` (Arm CMSIS core declarations and device IRQ usage),
`cmsis_core:NVIC_Type`, and `header:IRQn_Type`. See [[sources]] and [[index]].


## Multi-source interrupt scenario

Required sources: EXTI0_IRQn=6/slot22/EXTI0_IRQHandler; TIM2_IRQn=28/slot44/TIM2_IRQHandler; USART2_IRQn=38/slot54/USART2_IRQHandler. Source: header IRQn_Type and pinned startup vector table. Four priority bits are implemented. Example priorities TIM2=4, USART2=5, EXTI0=6 are software policy (lower numerical value has higher urgency); retain the reset priority grouping supplied by startup. Disable lines, initialize software state, configure source and clear its cause, clear NVIC pending, set priority, then enable source/line. Restore global interrupts last. Retrieve [[peripherals/tim]] and [[peripherals/exti]] before these final enables. SysTick is disabled in this scenario.

## Review

Reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
