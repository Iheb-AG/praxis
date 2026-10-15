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
