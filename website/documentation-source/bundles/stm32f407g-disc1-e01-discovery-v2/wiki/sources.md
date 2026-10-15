# Source provenance

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

| ID | Path | SHA-256 | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- | --- | --- |
| board | reviewed/board.json | 7ad9b54c7cdc26e5cf31314952c924f5fda1911cfdb627c5222cd6de89424869 | semantics | MB997-E-01 subset v1 | ST source document terms apply; local normalized records are MIT | Reviewed board role/polarity assertions; not automatic PDF wire reconstruction |
| board_manual | reviewed/um1472.provenance.json | 9444efaa35b893134df31825580fbcafa01348cf1d7c85a85bae365a6f4280b6 | configuration | UM1472 Rev 9 | ST source document terms apply; local normalized records are MIT | https://www.st.com/resource/en/user_manual/dm00039084-discovery-kit-with-stm32f407vg-mcu-stmicroelectronics.pdf |
| board_netlist | reviewed/netlist.json | 278e548d9b05b612831ddfb220710ed782fdd2fda81e5509f607b8245db14da4 | connectivity | MB997-E-01 subset v1 | ST source document terms apply; local normalized records are MIT | Reviewed transcription of ST MB997 E-01; not a CAD export |
| clock_review | raw/st_clock_example.c | a7457a224958f949e69bbebf17abec2fabead2a6932a0cf8016fb342bfab6553 | semantics | STM32CubeF4 v1.28.1 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/STM32CubeF4/v1.28.1/Projects/STM32F4-Discovery/Examples/UART/UART_TwoBoards_ComPolling/Src/main.c |
| cmsis_core | raw/vendor/core_cm4.h | f5b63d52dd1557b15ca414cb59c264f595a7b5669db2a5878dffe22f4caedc8c | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/core_cm4.h |
| definitions | reviewed/peripherals.json | 32de9bfa3972a28d408ccf79ced9e58f37bdd886b7f6cd079c1a2132a10ed9b2 | semantics | f407-fixture-1 | MIT | Source-backed editorial facts; RM0090/DS8626; independent review pending |
| gpio_review | reviewed/gpio.md | 4f1288c45c1d0faffe4cbc7161b2fc4117a0b7b1466826146cb93e25164f8d94 | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/datasheet/stm32f407vg.pdf |
| header | raw/vendor/stm32f407xx.h | ae1ab57d8ab750f64f04fd73476bc2760c761e18e45bde648e0bc350c9a1d9ac | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/Include/stm32f407xx.h |
| nvic_review | reviewed/nvic.md | df0a8e990fdd61861aaec94259cd640a36e23da4b5e92cdb3c2d4cc8389d6957 | semantics | f407-fixture-1 | MIT | Arm CMSIS core NVIC and ST device IRQ declarations |
| profile | profile-discovery.json | 5f5f6901902ff15d1df75e42c39027547dabf3af8db8a1995a88aac2a3e19afb | configuration | 1 | MIT | Local target profile |
| rcc_review | reviewed/rcc.md | 775654d8e3649946dec736ff7ae943f493e76dc42e2b4c1649f3f97b8fdf2469 | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0090-stm32f4xx-reference-manual-stmicroelectronics.pdf |
| schematic_e01 | reviewed/schematic-e01.provenance.json | 730be31b0809943920e0a4e635d2a5d40e9e8fcff9d4e0aea2587de8dcdfdd26 | connectivity | MB997-E-01 2020-04-09 | ST source document terms apply; local normalized records are MIT | https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-e01_schematic.pdf |
| usart_review | reviewed/usart.md | 7f66def9641ded5d70e59e845ebc8a89268e27c6a5ecf2526dd7ddd80c73f34b | semantics | f407-fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0090-stm32f4xx-reference-manual-stmicroelectronics.pdf |
| vendor_0 | raw/vendor/LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/LICENSE.txt |
| vendor_1 | raw/vendor/LICENSE-ST.md | dadb755f51d36614173b28c5790cb4a991e8f4cc822e5b634fd66a4f4145824d | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/LICENSE.md |
| vendor_2 | raw/vendor/cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_compiler.h |
| vendor_3 | raw/vendor/cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_gcc.h |
| vendor_4 | raw/vendor/cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/cmsis_version.h |
| vendor_6 | raw/vendor/mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | Apache-2.0 | https://raw.githubusercontent.com/ARM-software/CMSIS_5/5.9.0/CMSIS/Core/Include/mpu_armv7.h |
| vendor_7 | raw/vendor/provenance.json | d942d06c396ff3f1dc9be5135ef1546f458c24702f027dca93afe60909872d91 | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | MIT | Pinned vendor source inventory |
| vendor_9 | raw/vendor/system_stm32f4xx.h | 02c067d5a135f540c03215dc834b1e60a97bbd4e55bfd3994b0c82a15ea3012a | declarations | ST commit 3c77349ce04c8af401454cc51f85ea9a50e34fc1 / Arm CMSIS 5.9.0 | BSD-3-Clause | https://raw.githubusercontent.com/STMicroelectronics/cmsis-device-f4/3c77349ce04c8af401454cc51f85ea9a50e34fc1/Include/system_stm32f4xx.h |

Editorial reviewer: Codex source-backed board editorial review. Basis: Visual inspection of official MB997 E-01 pages 4/7 and UM1472 Rev9 sections 7.5/7.6/7.11/7.12; independent review pending; physical card revision unknown..

Editorial review is not independent hardware sign-off. See [[index]].
