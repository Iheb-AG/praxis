# NVIC: STM32F407 declaration map and UART workflow

Target: `stm32f407vgt6_fixture`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `praxis-f407-example-1`; silicon: `Unspecified; errata review pending`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/usart]].

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

## Review

Reviewer: Codex source-backed F407 fixture editorial review. Basis: Pinned ST/Arm declarations, DS8626 and ST clock example; independent board and semantics sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
