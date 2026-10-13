# Resolved schematic netlist

Target: `stm32f407vgt6_fixture`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `praxis-f407-example-1`; silicon: `Unspecified; errata review pending`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Electrical nets are direct exported memberships. Components do not join their two nets. Device Tree configuration is separate evidence. See [[index]], [[peripherals/gpio]], and [[sources]].

| Net | Endpoint | Pin | Sheet | Package | Aliases | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| GND | C1:2 | 2 | / | Capacitor_SMD:C_0603_1608Metric |  | netlist:net:GND; profile:pin_map/net:GND |
| GND | J1:4 | GND | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:GND; profile:pin_map/net:GND |
| GND | U1:27 | VSS | / | Package_QFP:LQFP-100_14x14mm_P0.5mm |  | netlist:net:GND; profile:pin_map/net:GND |
| UART_RX | J1:2 | RX | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical | USART2_RX | netlist:net:UART_RX; profile:pin_map/net:UART_RX |
| UART_RX | U1:26 | PA3 | / | Package_QFP:LQFP-100_14x14mm_P0.5mm | USART2_RX | netlist:net:UART_RX; profile:pin_map/net:UART_RX |
| UART_TX_CONNECTOR | J1:1 | TX | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:UART_TX_CONNECTOR; profile:pin_map/net:UART_TX_CONNECTOR |
| UART_TX_CONNECTOR | R1:2 | 2 | / | Resistor_SMD:R_0603_1608Metric |  | netlist:net:UART_TX_CONNECTOR; profile:pin_map/net:UART_TX_CONNECTOR |
| UART_TX_MCU | R1:1 | 1 | / | Resistor_SMD:R_0603_1608Metric | USART2_TX | netlist:net:UART_TX_MCU; profile:pin_map/net:UART_TX_MCU |
| UART_TX_MCU | U1:25 | PA2 | / | Package_QFP:LQFP-100_14x14mm_P0.5mm | USART2_TX | netlist:net:UART_TX_MCU; profile:pin_map/net:UART_TX_MCU |
| VCC | C1:1 | 1 | / | Capacitor_SMD:C_0603_1608Metric |  | netlist:net:VCC; profile:pin_map/net:VCC |
| VCC | J1:3 | VCC | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:VCC; profile:pin_map/net:VCC |
| VCC | U1:28 | VDD | / | Package_QFP:LQFP-100_14x14mm_P0.5mm |  | netlist:net:VCC; profile:pin_map/net:VCC |
