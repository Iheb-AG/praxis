# Resolved schematic netlist

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Electrical nets are direct exported memberships. Components do not join their two nets. Device Tree configuration is separate evidence. See [[index]], [[peripherals/gpio]], and [[sources]].

| Net | Endpoint | Pin | Sheet | Package | Aliases | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| GND | C1:2 | 2 | / | Capacitor_SMD:C_0603_1608Metric |  | netlist:net:GND; profile:pin_map/net:GND |
| GND | J1:4 | GND | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:GND; profile:pin_map/net:GND |
| GND | U1:8 | GND | / | Package_DIP:DIP-28_W7.62mm |  | netlist:net:GND; profile:pin_map/net:GND |
| UART_RX | J1:2 | RX | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical | USART0_RX | netlist:net:UART_RX; profile:pin_map/net:UART_RX |
| UART_RX | U1:2 | PD0 | / | Package_DIP:DIP-28_W7.62mm | USART0_RX | netlist:net:UART_RX; profile:pin_map/net:UART_RX |
| UART_TX_CONNECTOR | J1:1 | TX | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:UART_TX_CONNECTOR; profile:pin_map/net:UART_TX_CONNECTOR |
| UART_TX_CONNECTOR | R1:2 | 2 | / | Resistor_SMD:R_0603_1608Metric |  | netlist:net:UART_TX_CONNECTOR; profile:pin_map/net:UART_TX_CONNECTOR |
| UART_TX_MCU | R1:1 | 1 | / | Resistor_SMD:R_0603_1608Metric | USART0_TX | netlist:net:UART_TX_MCU; profile:pin_map/net:UART_TX_MCU |
| UART_TX_MCU | U1:3 | PD1 | / | Package_DIP:DIP-28_W7.62mm | USART0_TX | netlist:net:UART_TX_MCU; profile:pin_map/net:UART_TX_MCU |
| VCC | C1:1 | 1 | / | Capacitor_SMD:C_0603_1608Metric |  | netlist:net:VCC; profile:pin_map/net:VCC |
| VCC | J1:3 | VCC | / | Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical |  | netlist:net:VCC; profile:pin_map/net:VCC |
| VCC | U1:7 | VCC | / | Package_DIP:DIP-28_W7.62mm |  | netlist:net:VCC; profile:pin_map/net:VCC |
