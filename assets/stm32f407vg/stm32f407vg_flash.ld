/* Praxis reviewed C11 flash profile, MIT.
 * DS8626 Rev12 memory map: 1 MiB flash, 128 KiB contiguous SRAM,
 * separate 64 KiB CCM. CCM is intentionally unused by this profile.
 * ST startup symbols follow the pinned official startup_stm32f407xx.s.
 */
ENTRY(Reset_Handler)
MEMORY
{
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 1024K
    RAM (rw) : ORIGIN = 0x20000000, LENGTH = 128K
    CCMRAM (rw) : ORIGIN = 0x10000000, LENGTH = 64K
}
_estack = ORIGIN(RAM) + LENGTH(RAM);
_stack_limit = _estack - 4096;
SECTIONS
{
    .isr_vector : { . = ALIGN(512); KEEP(*(.isr_vector)) } > FLASH
    .text : { *(.text*) *(.rodata*) . = ALIGN(4); } > FLASH
    .ARM.extab : { *(.ARM.extab* .gnu.linkonce.armextab.*) } > FLASH
    .ARM.exidx : { __exidx_start = .; *(.ARM.exidx*) __exidx_end = .; } > FLASH
    .preinit_array : {
        . = ALIGN(4); __preinit_array_start = .;
        KEEP(*(.preinit_array*)) __preinit_array_end = .;
    } > FLASH
    .init_array : {
        . = ALIGN(4); __init_array_start = .;
        KEEP(*(SORT_BY_INIT_PRIORITY(.init_array.*))) KEEP(*(.init_array))
        __init_array_end = .;
    } > FLASH
    .fini_array : {
        . = ALIGN(4); KEEP(*(.fini_array*))
    } > FLASH
    _sidata = LOADADDR(.data);
    .data : { . = ALIGN(4); _sdata = .; *(.data*) . = ALIGN(4); _edata = .; } > RAM AT> FLASH
    .bss (NOLOAD) : { . = ALIGN(4); _sbss = .; *(.bss*) *(COMMON) . = ALIGN(4); _ebss = .; } > RAM
    .stack_reservation _stack_limit (NOLOAD) : { . += 4096; } > RAM
    .ARM.attributes 0 : { *(.ARM.attributes) }
    /DISCARD/ : { *(.comment) *(.note.GNU-stack) *(.note.gnu.build-id) }
    ASSERT(_ebss <= _stack_limit, "Main SRAM exhausted: preserve 4 KiB stack")
    ASSERT(SIZEOF(.isr_vector) == 392, "STM32F407 vector table must contain 98 words")
}
