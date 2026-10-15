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
