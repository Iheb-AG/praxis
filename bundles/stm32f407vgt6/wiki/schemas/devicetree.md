# Synthetic Device Tree fixture

Target: `stm32f407vgt6_fixture`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `praxis-f407-example-1`; silicon: `Unspecified; errata review pending`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

This synthetic topology exercises ingestion; it is not a board wiring claim. Unresolved properties are retained as hexadecimal bytes. See [[index]] and [[sources]].

| Node | Enabled | Decoded | Raw properties | Unresolved | Sources |
| --- | --- | --- | --- | --- | --- |
| / | True | {} | {"#address-cells": "00000001", "#size-cells": "00000001", "compatible": "7072617869732c73796e7468657469632d746f706f6c6f677900", "model": "5072617869732073796e74686574696320445420696e67657374696f6e206669787475726500"} |  | dts:/; overlay:resolved-topology:/ |
| /__symbols__ | True | {} | {"clk": "2f636c6f636b00", "irq": "2f696e746572727570742d636f6e74726f6c6c657200", "serial0": "2f6275732f73657269616c403434303000"} | clk; irq; serial0 | dts:/__symbols__; overlay:resolved-topology:/__symbols__ |
| /bus | True | {} | {"#address-cells": "00000001", "#size-cells": "00000001", "compatible": "73696d706c652d62757300", "ranges": "000000004000000000010000"} |  | dts:/bus; overlay:resolved-topology:/bus |
| /bus/serial@4400 | True | {"clocks": [{"args": [], "provider": "/clock"}], "interrupts": [{"args": [38], "provider": "/interrupt-controller"}], "pins": ["PA2", "PA3"], "reg": [{"address": 1073759232, "size": 1024}]} | {"clocks": "00000001", "compatible": "7072617869732c666978747572652d7561727400", "interrupt-parent": "00000002", "interrupts": "00000026", "phandle": "00000003", "praxis,pins": "5041320050413300", "praxis,unknown": "00001234", "reg": "0000440000000400", "status": "6f6b617900"} | praxis,unknown | dts:/bus/serial@4400; overlay:resolved-topology:/bus/serial@4400 |
| /clock | True | {} | {"#clock-cells": "00000000", "clock-frequency": "0280de80", "compatible": "66697865642d636c6f636b00", "phandle": "00000001"} |  | dts:/clock; overlay:resolved-topology:/clock |
| /interrupt-controller | True | {} | {"#address-cells": "00000000", "#interrupt-cells": "00000001", "compatible": "7072617869732c666978747572652d696e746572727570747300", "interrupt-controller": "", "phandle": "00000002"} |  | dts:/interrupt-controller; overlay:resolved-topology:/interrupt-controller |
