The fixture uses STM32F401RE in LQFP64. The supported AF table is deliberately limited to the routed USART2 pins; never extrapolate AF7 to another pin.

| MCU pin | Physical LQFP64 pin | Signal | AF | AFRL bits | MODER bits |
| --- | --- | --- | --- | --- | --- |
| PA2 | 16 | USART2_TX | 7 | 11:8 | 5:4 |
| PA3 | 17 | USART2_RX | 7 | 15:12 | 7:6 |

After [[peripherals/rcc]], clear and replace the relevant fields: MODER=10, AFRL=7, OTYPER=0 (push-pull), OSPEEDR=01 (medium fixture choice), PUPDR=00. Preserve every other pin, especially SWD PA13/PA14. Inputs must have a defined electrical idle level from the attached interface; the fixture does not guarantee external biasing.

The register field table is contiguous and covers every GPIO bit position. Package-specific alternate functions come from [DS10086 pin and AF tables](https://www.st.com/resource/en/datasheet/stm32f401re.pdf); register semantics come from [RM0368 GPIO](https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf). Verify direct routing in [[schemas/custom_pcb_netlist]] before [[peripherals/usart]].

