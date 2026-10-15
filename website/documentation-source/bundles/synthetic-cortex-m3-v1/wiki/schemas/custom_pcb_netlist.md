# Resolved schematic netlist

Target: `synthetic_cortex_m3`; MCU: `PRAXIS-DEMO-M3`; package: `Fixture:QFP-16`; board revision: `synthetic-1`; silicon: `fictional-v1`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

Electrical nets are direct exported memberships. Components do not join their two nets. Device Tree configuration is separate evidence. See [[index]], and [[sources]].

| Net | Endpoint | Pin | Sheet | Package | Aliases | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| RX | J1:2 | RX | /fictional/ | Fixture:Header-2 | UART0_RX | profile:pin_map/net:RX; schematic:net:RX |
| RX | U1:2 | P0_3 | /fictional/ | Fixture:QFP-16 | UART0_RX | profile:pin_map/net:RX; schematic:net:RX |
| TX | J1:1 | TX | /fictional/ | Fixture:Header-2 | UART0_TX | profile:pin_map/net:TX; schematic:net:TX |
| TX | U1:1 | P0_2 | /fictional/ | Fixture:QFP-16 | UART0_TX | profile:pin_map/net:TX; schematic:net:TX |
