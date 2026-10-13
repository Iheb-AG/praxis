Supported operating subset: route **PA0 to EXTI0** through SYSCFG_EXTICR1.
Evidence: `rm_syscfg1:page:293`, RM0090 Rev22 section 9.2.3 (F405/407 section).

Enable RCC_APB2ENR.SYSCFGEN and read back the gate before accessing SYSCFG. The clock
and its enable bit are documented by `rm_apb2_gate:page:250`. SYSCFG is on APB2.
Keep EXTI0 masked and global interrupts disabled during routing. Replace only
SYSCFG->EXTICR[0] bits 3:0 with zero: 0000 selects PA0; 0001 would select PB0.
Preserve all other line-selection fields and reserved upper bits.

The declaration adapter explicitly expands EXTICR[4] into EXTICR0..EXTICR3, preserving
the C members EXTICR[0]..EXTICR[3] and offsets 0x08/0x0C/0x10/0x14. In this catalog,
EXTICR0 corresponds to the manual's **EXTICR1**, not a different silicon register.
The corresponding vendor macro prefixes are SYSCFG_EXTICR1..SYSCFG_EXTICR4.
All four route-register reset values are zero; other SYSCFG functions remain unreviewed.
Evidence: `rm_syscfg1:page:293`, `rm_syscfg2:page:294`, `rm_syscfg3:page:295`.

Do not reset SYSCFG wholesale to change one route. Board wiring and GPIO input setup
are separate prerequisites. See [[peripherals/gpio]], [[peripherals/exti]],
[[peripherals/rcc]], [[schemas/custom_pcb_netlist]] and [[sources]].
