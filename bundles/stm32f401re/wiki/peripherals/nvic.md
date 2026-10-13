# NVIC: final interrupt and DMA enablement

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Prerequisites: [[peripherals/usart]].

## Instances and clock dependencies

| Instance | Base address | Bus | Clock | Sources |
| --- | --- | --- | --- | --- |
| NVIC | 0xE000E100 | Cortex-M4 system | Core clock | header:instance:NVIC; nvic_review:clock:NVIC |

## Register map

| Register | Offset / data address | Width | I/O address | Access | Reset | Side effects | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISER0 | 0x000 | 32 | — | RW | 0x0 | Write 1 enables; writing 0 has no effect. | header:register:ISER0; nvic_review:register:ISER0 |
| ISER1 | 0x004 | 32 | — | RW | 0x0 | Write 1 enables; do not use read-modify-write. | header:register:ISER1; nvic_review:register:ISER1 |
| ICER1 | 0x084 | 32 | — | RW | 0x0 | Write 1 disables IRQ; writing 0 has no effect. | header:register:ICER1; nvic_review:register:ICER1 |
| ICPR1 | 0x184 | 32 | — | RW | 0x0 | Write 1 clears pending state; clear peripheral cause first. | header:register:ICPR1; nvic_review:register:ICPR1 |
| IPR38 | 0x326 | 8 | — | RW | 0x0 | STM32F401 implements four high priority bits; lower number is higher priority. | header:register:IPR38; nvic_review:register:IPR38 |

## Bit fields

| Register | Field | Bits | Mask | Meaning | Sources |
| --- | --- | --- | --- | --- | --- |
| ISER0 | SETENA | 31:0 | 0xFFFFFFFF | External IRQs 0–31 | nvic_review:field:SETENA |
| ISER1 | SETENA | 31:0 | 0xFFFFFFFF | External IRQs 32–63; USART2 IRQ38 uses bit6 | nvic_review:field:SETENA |
| ICER1 | CLRENA | 31:0 | 0xFFFFFFFF | Disable external IRQs 32–63 | nvic_review:field:CLRENA |
| ICPR1 | CLRPEND | 31:0 | 0xFFFFFFFF | Clear pending external IRQs 32–63 | nvic_review:field:CLRPEND |
| IPR38 | PRI38 | 7:4 | 0xF0 | Encoded priority for USART2 IRQ38 | nvic_review:field:PRI38 |

## Reviewed operating semantics

Supported scope: USART2 external IRQ38. Vector table entry is 16+38=54; provide USART2_IRQHandler in startup integration. The core NVIC register fields are write-one actions, not ordinary peripheral read-modify-write bits.

1. Keep USART2 RXNEIE and its NVIC line disabled while installing a handler and initializing receive state.
2. Configure GPIO/USART first. Drain pending receive/error data according to [[peripherals/usart]] and clear the peripheral cause before NVIC pending state.
3. Program priority through IP[38], using the implemented high four bits. Write bit6 of ICPR[1] to clear IRQ38 pending.
4. Enable RXNEIE, enable NVIC ISER[1] bit6, and only then restore the intended global interrupt state. The example does not globally unmask interrupts.
5. The handler must consume DR when RXNE is asserted and handle the documented error sequence without unbounded waits.

DMA is not implemented by the examples. Future USART2 DMA uses DMA1 stream5/channel4 RX or stream6/channel4 TX; IRQs 16/17 respectively. Enable the DMA clock, disable and wait for stream EN=0, configure addresses/length/channel/direction, clear flags, enable the stream, and enable USART DMA requests last. Detailed DMA register knowledge must be added before generating DMA code.

Sources: [RM0368 interrupt/DMA chapters](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf), pinned ST IRQ declarations and Arm CMSIS core header. See [[peripherals/usart]] and [[index]].

## Review

Reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

See [[index]], [[schemas/custom_pcb_netlist]], and [[sources]].
