# Source provenance

Target: `stm32f407vgt6_fixture`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `praxis-f407-example-1`; silicon: `Unspecified; errata review pending`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

| ID | Path | SHA-256 | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- | --- | --- |
| clock_review | raw/st_clock_example.c | a7457a224958f949e69bbebf17abec2fabead2a6932a0cf8016fb342bfab6553 | semantics | STM32CubeF4 v1.28.1 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/STM32CubeF4/v1.28.1/Projects/STM32F4-Discovery/Examples/UART/UART_TwoBoards_ComPolling/Src/main.c |
| cmsis_core | raw/vendor/core_cm4.h | f5b63d52dd1557b15ca414cb59c264f595a7b5669db2a5878dffe22f4caedc8c | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/core_cm4.h |
| definitions | reviewed/peripherals.json | 32de9bfa3972a28d408ccf79ced9e58f37bdd886b7f6cd079c1a2132a10ed9b2 | semantics | f407-fixture-1 | MIT | Source-backed editorial facts; RM0090/DS8626; independent review pending |
| dts | raw/topology.dts | b0434388f9f1d570fb9e658b01db2cd5843388b4bbcaa7151aca7918fda708e3 | configuration | f407-fixture-1 | MIT | Synthetic DTS; 42 MHz clock is a declared configuration, not measured wiring |
| gpio_review | reviewed/gpio.md | 4f1288c45c1d0faffe4cbc7161b2fc4117a0b7b1466826146cb93e25164f8d94 | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/datasheet/stm32f407vg.pdf |
| header | raw/vendor/stm32f407xx.h | ae1ab57d8ab750f64f04fd73476bc2760c761e18e45bde648e0bc350c9a1d9ac | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/Include/stm32f407xx.h |
| netlist | raw/netlist.xml | 1d7f0afc65bc116d71182ab44d5e009dd1d936b4c2cf6909de59d96e7ce15dc0 | connectivity | f407-fixture-1 | MIT | Hand-authored partial illustrative KiCad XML; replace with actual board export |
| nvic_review | reviewed/nvic.md | df0a8e990fdd61861aaec94259cd640a36e23da4b5e92cdb3c2d4cc8389d6957 | semantics | f407-fixture-1 | MIT | Arm CMSIS core NVIC and ST device IRQ declarations |
| overlay | raw/enable_uart.dtso | ff2875ef4d1f512231851396f5151f53c326a6eba9d438915092914fd8f0f436 | configuration | f407-fixture-1 | MIT | Synthetic UART enable overlay |
| profile | profile.json | 2cc0302c1637834ea86b9dce7ac77ed34846cdd4cf05bfc14a779cc42eadfd14 | configuration | 1 | MIT | Local target profile |
| rcc_review | reviewed/rcc.md | 775654d8e3649946dec736ff7ae943f493e76dc42e2b4c1649f3f97b8fdf2469 | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0090-stm32f4xx-reference-manual-stmicroelectronics.pdf |
| usart_review | reviewed/usart.md | 7f66def9641ded5d70e59e845ebc8a89268e27c6a5ecf2526dd7ddd80c73f34b | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0090-stm32f4xx-reference-manual-stmicroelectronics.pdf |
| vendor_0 | raw/vendor/LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/LICENSE.txt |
| vendor_1 | raw/vendor/LICENSE-ST.md | dadb755f51d36614173b28c5790cb4a991e8f4cc822e5b634fd66a4f4145824d | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/LICENSE.md |
| vendor_2 | raw/vendor/cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_compiler.h |
| vendor_3 | raw/vendor/cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_gcc.h |
| vendor_4 | raw/vendor/cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_version.h |
| vendor_6 | raw/vendor/mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/mpu_armv7.h |
| vendor_7 | raw/vendor/provenance.json | d942d06c396ff3f1dc9be5135ef1546f458c24702f027dca93afe60909872d91 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | MIT | Pinned vendor source inventory |
| vendor_9 | raw/vendor/system_stm32f4xx.h | 02c067d5a135f540c03215dc834b1e60a97bbd4e55bfd3994b0c82a15ea3012a | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/Include/system_stm32f4xx.h |

Editorial reviewer: Codex source-backed F407 fixture editorial review. Basis: Pinned ST/Arm declarations, DS8626 and ST clock example; independent board and semantics sign-off remains pending..

Editorial review is not independent hardware sign-off. See [[index]].
