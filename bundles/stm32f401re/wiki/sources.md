# Source provenance

Target: `stm32f401re_fixture`; MCU: `STM32F401RE`; package: `Package_QFP:LQFP-64_10x10mm_P0.5mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture uses RM0368 Rev 6 semantics`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

| ID | Path | SHA-256 | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- | --- | --- |
| definitions | reviewed/peripherals.json | c7512a64f43a7e5d13d537e82e37a3d1ae0d90b11a6663c27ece0b9ad22e2780 | semantics | fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf |
| dts | raw/topology.dts | b37c7f17e6097949ce55b8e1c35deb5f564137e72d64b1897864b14a774ff53e | configuration | synthetic-1 | MIT | Self-contained synthetic DT fixture |
| gpio_review | reviewed/gpio.md | 4449fe1d75d086a88b940c2f6875bf804d68df23fe8102044bf80ef4b11ef74a | semantics | fixture-1 | MIT | https://www.st.com/resource/en/datasheet/stm32f401re.pdf |
| header | raw/vendor/stm32f401xe.h | 9db8f3e317c6029ebdd1538f827885cf538850a20b17ac8491247e783134098c | declarations | ST commit recorded in raw/vendor/provenance.json | BSD-3-Clause | STMicroelectronics cmsis-device-f4 |
| netlist | raw/netlist.xml | 94b0b922bb3a33c2cc58f5e44896923c1e3c914f2fb022e3e8aed3056c49f223 | connectivity | fixture-1 | MIT | Hand-authored KiCad XML example; live export comparison pending |
| nvic_review | reviewed/nvic.md | ff11df1a97d48a1e19441e4af1cca85d1df12b7514948caff8f0ec8f328fe14d | semantics | fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf |
| overlay | raw/enable_uart.dtso | ff2875ef4d1f512231851396f5151f53c326a6eba9d438915092914fd8f0f436 | configuration | synthetic-1 | MIT | Enable synthetic UART |
| profile | profile.json | 0764a362d329bc9505b1b72cb0009aa67938a970e80bc7f9580190d8d2bc9889 | configuration | 1 | MIT | Local target profile |
| rcc_review | reviewed/rcc.md | 2dfc632ef889358ae320ebabfeffd8a351dea8a5db9d91d0c03cd33288287983 | semantics | fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf |
| schematic | raw/board.kicad_sch | d1271564abb70daf5d16ff8b8aa203ab09e037f74cf3dee7a3aa15cef5411986 | connectivity | fixture-1 | MIT | Original partial KiCad schematic; live export validation required |
| usart_review | reviewed/usart.md | 81c47ef022d5d4573f43f16abc235d96da69c32e040922279ca61ea9b1623297 | semantics | fixture-1 | MIT | https://www.st.com/resource/en/reference_manual/rm0368-stm32f401xb-c-d-e-mb-reference-manual-stmicroelectronics.pdf |
| vendor_0 | raw/vendor/LICENSE-CMSIS.txt | b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_1 | raw/vendor/LICENSE-ST.md | dadb755f51d36614173b28c5790cb4a991e8f4cc822e5b634fd66a4f4145824d | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_2 | raw/vendor/cmsis_compiler.h | b51963d271c1571ca3463654c76aa7ea50c4eac5d0a2710df10414ac64d9e0f8 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_3 | raw/vendor/cmsis_gcc.h | 43bfd1fe69fbbc2ca70aaf7d43cc3e20f16e0c7f66e1bdef9b51af6dc14b2617 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_4 | raw/vendor/cmsis_version.h | 184c19fd3ee73632edf35a0b4d49cd48be75fbf49e6ccb19d9db05fa83bea4b3 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_5 | raw/vendor/core_cm4.h | f5b63d52dd1557b15ca414cb59c264f595a7b5669db2a5878dffe22f4caedc8c | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_6 | raw/vendor/mpu_armv7.h | 29206b52ee02290ed6f5a5415ebd4187de802cf176d9b3cb844390d8e5571372 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_7 | raw/vendor/provenance.json | fedaf1a9e91a1739eafdd7af3d6dc056a6a2478a23e9a20c10d78ea388ec9e66 | declarations | pinned source bytes | Apache-2.0 | Upstream source and license included in raw/vendor |
| vendor_9 | raw/vendor/system_stm32f4xx.h | 02c067d5a135f540c03215dc834b1e60a97bbd4e55bfd3994b0c82a15ea3012a | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |

Editorial reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

Editorial review is not independent hardware sign-off. See [[index]].
