# NVIC: STM32F407 declaration map and UART workflow

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Prerequisites: [[peripherals/usart]], [[peripherals/tim]], [[peripherals/exti]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| NVIC | 0xE000E100 | Core PPB | Processor clock; device IRQ slots only | cmsis_core:NVIC_BASE; nvic_review:instance:NVIC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources | Permitted bus access widths | Count | Stride bytes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ISER | 0x000 | 32 | — | RW | not asserted | Write-one sets enable; zero has no effect. | cmsis_core:NVIC_Type.ISER; nvic_review:ISER; timer_irq_evidence:pm0214/page:210 | 32 | 8 | 4 |
| ICER | 0x080 | 32 | — | RW | not asserted | Write-one clears enable; zero has no effect. | cmsis_core:NVIC_Type.ICER; nvic_review:ICER; timer_irq_evidence:pm0214/page:211 | 32 | 8 | 4 |
| ISPR | 0x100 | 32 | — | RW | not asserted | Write-one sets pending; zero has no effect. | cmsis_core:NVIC_Type.ISPR; nvic_review:ISPR; timer_irq_evidence:pm0214/page:212 | 32 | 8 | 4 |
| ICPR | 0x180 | 32 | — | RW | not asserted | Write-one clears pending; zero has no effect. | cmsis_core:NVIC_Type.ICPR; nvic_review:ICPR; timer_irq_evidence:pm0214/page:213 | 32 | 8 | 4 |
| IABR | 0x200 | 32 | — | RO | not asserted | Read-only active state. | cmsis_core:NVIC_Type.IABR; nvic_review:IABR; timer_irq_evidence:pm0214/page:214 | 32 | 8 | 4 |
| IP | 0x300 | 8 | — | RW | not asserted | Implemented high four bits per priority byte. | cmsis_core:NVIC_Type.IP; nvic_review:IP; timer_irq_evidence:pm0214/page:215 | 8 | 240 | 1 |
| STIR | 0xE00 | 32 | — | WO | not asserted | Write IRQ number to pend a supported device interrupt; privilege rules apply. | cmsis_core:NVIC_Type.STIR; nvic_review:STIR | not asserted | 1 | 4 |

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


## CAN1 FIFO0 interrupt amendment

CAN1_RX0_IRQn=20, vector slot36, handler CAN1_RX0_IRQHandler; exact device header. Use bank0 bit20 for literal action writes, IP[20] high4bits with priority5 software policy. Reject enabled/active ownership, keep global interrupts masked while preparing handler/state/source, clear source before pending, enable FMPIE0 then NVIC, restore global state last. The CAN receive handler validates and releases FIFO0 before disabling its source/line. Shared canonical NVIC retrieval retains UART/TIM/EXTI documentation prerequisites; reading those does not require their hardware initialization for CAN. Sources: header:CAN1_RX0_IRQn; nvic_review:ISER/ICER/ICPR/IP/IABR; rm_can_1089:page:1089. See [[peripherals/can]].

## TIM5 capture IRQ50

TIM5_IRQn=50, vector slot66, handlerTIM5_IRQHandler, bank1 bit18, priority byteIP[50].
Device header and PM0214 pages210–215 establish the identities/actions. Logical priority2
(encoded0x20) is application policy. Reject enabled/pending/active ownership at fresh startup.
Use literal write-one action masks and only the selected priority byte, preserving unrelated lines.
Clear pending after source disabled/cleared; enable line before capture request, keep global
mask until handler/state/source and PWM are ready. ISR drains CCR3 once, then disables request
before disabling/clearing line on terminal completion/failure. ICPR never clears active state.
Thread masks globally, verifies line/pending/active quiet and only then publishes the terminal result.
Read canonical USART/EXTI/TIM dependencies as routing policy; they do not require unrelated hardware
initialization for TIM5. Physical IRQ behavior and independent review remain pending.
See [[peripherals/scb]], [[peripherals/tim]], [[peripherals/gpio]].

## Reviewed operating modes

| Mode | Instances | Registers | Required fields | Operating requirements | Sources | Required modes |
| --- | --- | --- | --- | --- | --- | --- |
| can1_rx0_prepare | NVIC | ISER, ICER, ICPR, IP, IABR | IABR: IRQ_BITS; ICER: IRQ_BITS; ICPR: IRQ_BITS; IP: PRIORITY; ISER: IRQ_BITS | Exact device IRQ20/vector36/CAN1_RX0_IRQHandler; reject already enabled or active line ownership. Four implemented priority bits; priority5 policy gives IP[20]=0x50.<br>Keep global interrupts masked and the source/line disabled while installing handler/state. Literal bank0 bit20 actions only, not RMW.<br>Clear peripheral cause before ICPR[0] bit20. Enable source and line only through the dependent CAN IRQ workflow after initialization; restore intended global state last. | can_nvic_review:CAN1_RX0_IRQn binding to exact header:20; nvic_review:ISER/ICER/ICPR/IP/IABR |  |
| tim5_capture_prepare | NVIC | ISER, ICER, ISPR, ICPR, IABR, IP |  | Exact device TIM5_IRQn50, vector slot66; NVIC bank1 bit18 and IP[50]. Four implemented priority bits; write encoded0x20 for logical priority2.<br>Fresh exclusive startup with global mask1; inspect implemented external NVIC banks0..2 and reject any enabled/pending/active line, including TIM5. Highest device IRQ FPU_IRQn81 gives three banks. Preserve every unrelated line/priority byte.<br>Use literal write-one ISER/ICER/ICPR actions, never read-modify-write. ICPR does not clear active state.<br>Handler/vector and state ready first. Prepare/read back priority and clear pending only after source is disabled; enable/read back line while capture request remains disabled.<br>Enable/read back capture request before PWM output, enable PWM counter last, then unmask global interrupts with fences. No unrelated interrupt source is active.<br>On terminal outcome disable capture request before disabling/clearing line, mask globally in Thread, require no pending/active/enabled state; inaccessible/failed cleanup cannot claim quiet. | timer_irq_evidence:header/lines:40-170; timer_irq_evidence:cmsis_core/lines:1675-1830; timer_irq_evidence:pm0214/page:208; timer_irq_evidence:pm0214/page:210; timer_irq_evidence:pm0214/page:211; timer_irq_evidence:pm0214/page:212; timer_irq_evidence:pm0214/page:213; timer_irq_evidence:pm0214/page:214; timer_irq_evidence:pm0214/page:215 | [[peripherals/scb]] / tim5_fixed_irq_context: SCB |

## Review

Reviewer: Codex source-backed editorial review through Praxis ingestion MCP. Basis: Complete RM0090 Rev22 and PM0214 Rev10 source parts plus exact pinned IRQ/priority declarations. Implementing-author review only; independent signoff and new physical IRQ qualification pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
