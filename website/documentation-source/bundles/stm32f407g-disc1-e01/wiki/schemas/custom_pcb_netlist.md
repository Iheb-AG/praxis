# Resolved schematic netlist

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Electrical nets are explicit source memberships. Coverage: partial. See [[schemas/board]] for omitted scope and reviewed circuit interpretation. Components do not join their two nets. Device Tree configuration is separate evidence. See [[index]], [[peripherals/gpio]], and [[sources]].

| Net | Endpoint | Pin | Sheet | Package | Aliases | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| B1_SERIES | R35:1 | 1 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SERIES; schematic_e01:page:4/B1 |
| B1_SERIES | SB20:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SERIES; schematic_e01:page:4/B1 |
| B1_SIGNAL | B1:1 | 1 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SIGNAL; schematic_e01:page:4/B1 |
| B1_SIGNAL | B1:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SIGNAL; schematic_e01:page:4/B1 |
| B1_SIGNAL | R35:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SIGNAL; schematic_e01:page:4/B1 |
| B1_SIGNAL | R39:1 | 1 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SIGNAL; schematic_e01:page:4/B1 |
| B1_SUPPLY | B1:3 | 3 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SUPPLY; schematic_e01:page:4/B1 |
| B1_SUPPLY | B1:4 | 4 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SUPPLY; schematic_e01:page:4/B1 |
| B1_SUPPLY | R38:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:B1_SUPPLY; schematic_e01:page:4/B1 |
| GND | LD3:2 | K | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:GND; schematic_e01:page:4/LEDs+B1 |
| GND | LD4:2 | K | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:GND; schematic_e01:page:4/LEDs+B1 |
| GND | LD5:2 | K | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:GND; schematic_e01:page:4/LEDs+B1 |
| GND | LD6:2 | K | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:GND; schematic_e01:page:4/LEDs+B1 |
| GND | R39:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:GND; schematic_e01:page:4/LEDs+B1 |
| LD3_ANODE | LD3:1 | A | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD3_ANODE; schematic_e01:page:4/LEDs |
| LD3_ANODE | R36:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD3_ANODE; schematic_e01:page:4/LEDs |
| LD4_ANODE | LD4:1 | A | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD4_ANODE; schematic_e01:page:4/LEDs |
| LD4_ANODE | R40:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD4_ANODE; schematic_e01:page:4/LEDs |
| LD5_ANODE | LD5:1 | A | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD5_ANODE; schematic_e01:page:4/LEDs |
| LD5_ANODE | R41:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD5_ANODE; schematic_e01:page:4/LEDs |
| LD6_ANODE | LD6:1 | A | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD6_ANODE; schematic_e01:page:4/LEDs |
| LD6_ANODE | R42:2 | 2 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:LD6_ANODE; schematic_e01:page:4/LEDs |
| PA0 | SB20:1 | 1 | /Peripherals | Not asserted from source PDF | b1;USER_BUTTON;B1 | profile:pin_map/net:PA0; schematic_e01:page:4/B1;page:7/MCU |
| PA0 | U4:23 | PA0 | /MCU | Package_QFP:LQFP-100_14x14mm_P0.5mm | b1;USER_BUTTON;B1 | profile:pin_map/net:PA0; schematic_e01:page:4/B1;page:7/MCU |
| PD12 | R40:1 | 1 | /Peripherals | Not asserted from source PDF | ld4;LED_A;LD4;GREEN_USER_LED | profile:pin_map/net:PD12; schematic_e01:page:4/LEDs;page:7/MCU |
| PD12 | U4:59 | PD12 | /MCU | Package_QFP:LQFP-100_14x14mm_P0.5mm | ld4;LED_A;LD4;GREEN_USER_LED | profile:pin_map/net:PD12; schematic_e01:page:4/LEDs;page:7/MCU |
| PD13 | R36:1 | 1 | /Peripherals | Not asserted from source PDF | ld3;LED_B;LD3;ORANGE_USER_LED | profile:pin_map/net:PD13; schematic_e01:page:4/LEDs;page:7/MCU |
| PD13 | U4:60 | PD13 | /MCU | Package_QFP:LQFP-100_14x14mm_P0.5mm | ld3;LED_B;LD3;ORANGE_USER_LED | profile:pin_map/net:PD13; schematic_e01:page:4/LEDs;page:7/MCU |
| PD14 | R41:1 | 1 | /Peripherals | Not asserted from source PDF | ld5;RED_LED;LD5;RED_USER_LED | profile:pin_map/net:PD14; schematic_e01:page:4/LEDs;page:7/MCU |
| PD14 | U4:61 | PD14 | /MCU | Package_QFP:LQFP-100_14x14mm_P0.5mm | ld5;RED_LED;LD5;RED_USER_LED | profile:pin_map/net:PD14; schematic_e01:page:4/LEDs;page:7/MCU |
| PD15 | R42:1 | 1 | /Peripherals | Not asserted from source PDF | ld6;BLUE_LED;LD6;BLUE_USER_LED | profile:pin_map/net:PD15; schematic_e01:page:4/LEDs;page:7/MCU |
| PD15 | U4:62 | PD15 | /MCU | Package_QFP:LQFP-100_14x14mm_P0.5mm | ld6;BLUE_LED;LD6;BLUE_USER_LED | profile:pin_map/net:PD15; schematic_e01:page:4/LEDs;page:7/MCU |
| VDD | R38:1 | 1 | /Peripherals | Not asserted from source PDF |  | profile:pin_map/net:VDD; schematic_e01:page:4/B1 |
