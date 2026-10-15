# Schematic component catalog

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Values and fitted status describe imported sources. Circuit roles and electrical suitability require reviewed semantics. See [[schemas/custom_pcb_netlist]] and [[sources]].

| Reference | Value | Kind | Fitted | Package | Sheet | Pins | Properties | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | USER / WAKE-UP | switch | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2; 3=3; 4=4 | {"contact": "normally-open", "internal_groups": "1,2 and 3,4"} | schematic_e01:page:4/B1 |
| LD3 | Orange | led | True | Not asserted from source PDF | /Peripherals | 1=A; 2=K | {} | schematic_e01:page:4/LD3 |
| LD4 | Green | led | True | Not asserted from source PDF | /Peripherals | 1=A; 2=K | {} | schematic_e01:page:4/LD4 |
| LD5 | Red | led | True | Not asserted from source PDF | /Peripherals | 1=A; 2=K | {} | schematic_e01:page:4/LD5 |
| LD6 | Blue | led | True | Not asserted from source PDF | /Peripherals | 1=A; 2=K | {} | schematic_e01:page:4/LD6 |
| P1 | Header 25X2 (selected UART/timer pins) | other | True | Board header:2x25 | /Top | 11=PA1; 13=PA3; 14=PA2 | {"coverage": "Selected UART and routed timer pins only"} | schematic_uart:page:2/P1; timer_routes_connectivity_evidence:mb997/page:2; timer_routes_connectivity_evidence:mb997/page:7 |
| P2 | Header25X2 (selected CAN RX candidate pin) | other | True | Board header:2x25 | /Top | 34=PD0 | {"coverage": "Only PD0 pin transcribed. Not an external CAN interface."} | schematic_uart:page:2 |
| R35 | 330 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R35 |
| R36 | 680 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R36 |
| R38 | 100 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R38 |
| R39 | 220000 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R39 |
| R40 | 510 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R40 |
| R41 | 680 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R41 |
| R42 | 680 ohm | resistor | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/R42 |
| SB20 | Closed by default | bridge | True | Not asserted from source PDF | /Peripherals | 1=1; 2=2 | {"terminal_numbering": "Transcription-local terminal IDs for passive parts; the PDF does not print their pin numbers."} | schematic_e01:page:4/SB20 |
| U4 | STM32F407VGT6 | mcu | True | Package_QFP:LQFP-100_14x14mm_P0.5mm | /MCU | 23=PA0; 24=PA1; 25=PA2; 26=PA3; 59=PD12; 60=PD13; 61=PD14; 62=PD15; 81=PD0 | {"pin_scope": "Only selected GPIO pins are transcribed; other MCU pins are omitted."} | schematic_e01:page:7/MCU; schematic_mcu:page:7; timer_routes_connectivity_evidence:mb997/page:2; timer_routes_connectivity_evidence:mb997/page:7 |
