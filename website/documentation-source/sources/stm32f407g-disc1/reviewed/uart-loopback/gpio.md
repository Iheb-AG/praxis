Applicability: STM32F407VGT6, **LQFP100**, with the following reviewed AF subset.

| MCU pin | Physical LQFP100 pin | Signal | AF | AFRL bits | MODER bits | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PA2 | 25 | USART2_TX | 7 | 11:8 | 5:4 | gpio_review:DS8626 tables 7/9 |
| PA3 | 26 | USART2_RX | 7 | 15:12 | 7:6 | gpio_review:DS8626 tables 7/9 |

After [[peripherals/rcc]], replace only the PA2/PA3 fields: MODER=10, AFRL=7,
OTYPER=0 (push-pull), PUPDR=00, and OSPEEDR=01 as an example medium-speed choice.
Preserve all other pins, especially SWD PA13/PA14. The external interface must
provide an appropriate idle level. Validate routing in [[schemas/custom_pcb_netlist]]
before [[peripherals/usart]]. A schematic signal label does not configure AF7.

The complete GPIO register map is shared by GPIO instances; reset values for
MODER, OSPEEDR, and PUPDR depend on the port and remain unasserted in this common
table. BSRR is a write-one set/reset action. LCKR has a prescribed lock sequence;
do not use generic read-modify-write to lock configuration.

Header-declared GPIOF/G/I bases do not establish that those ports are bonded in
LQFP100. Only the package-specific reviewed pin map establishes physical pins.
This AF subset does not establish another pin's capabilities.

Evidence: `gpio_review` (DS8626 Rev 12 package pin table 7 and AF table 9),
`header` (GPIO layout/masks), and `profile:pin_map` (reviewed package map).
See [[sources]] and [[index]].


## Loopback and status pins

The loopback wire is an external test connection between PA2/P1-14 and PA3/P1-13; it is not a fixed board net. Both pins use AF7, push-pull, medium speed, no internal pull for the fitted-wire test. With the wire absent RX may float; a negative test can fail with a UART error rather than precisely at the timeout. PD12/13/14/15 drive the four active-high board LEDs; preload all off with BSRR before output mode. PA0 is input with the existing external pull-down and no internal pull. Preserve SWD PA13/14. Sources: schematic_uart:page:2; schematic_mcu:page:7; uart_connector:page:18; rm_gpio_speed:page:284; board signal definitions. See [[peripherals/syscfg]] and [[peripherals/exti]].
