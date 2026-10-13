# Source provenance

Target: `atmega328p_fixture`; MCU: `ATmega328P-PU`; package: `Package_DIP:DIP-28_W7.62mm`; board revision: `praxis-example-1`; silicon: `Unspecified; fixture based on ATmega328P datasheet`.

**Illustrative fixture; not a manufactured or hardware-qualified board.**

| ID | Path | SHA-256 | Authority | Version | License | Origin |
| --- | --- | --- | --- | --- | --- | --- |
| clock_review | reviewed/clock.md | 021df8d5b651132ad63e56168bd5ee562c7928ae00f6239888e31350839e4f2d | semantics | fixture-1 | MIT | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf |
| definitions | reviewed/peripherals.json | 1944d11a87a55bbb4a7d40b908bc0fb5f38ab67555379f7a832e29bc1c3b2d0f | semantics | fixture-1 | MIT | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf |
| gpio_review | reviewed/gpio.md | aa761ddc3c9b200b0e2dc5f24065d315f1ac7b7fb565e2718799b73265e0bceb | semantics | fixture-1 | MIT | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf |
| header | raw/registers.h | 07ae83d2eb08c3c735e7cf332a394b0de37cb26122c85c759d7de167336afae9 | declarations | fixture-1 | MIT | Entry point to vendored avr-libc subset |
| interrupts_review | reviewed/interrupts.md | ce02de37d0babe4baa5298cd0b694f3638780d7ab5a9689eba7b3de5beb70008 | semantics | fixture-1 | MIT | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf |
| netlist | raw/netlist.xml | 23b99e04921066547d9788dc45fbfac0cc8d9149c4a935970a385e66bc4897b1 | connectivity | fixture-1 | MIT | Hand-authored KiCad XML example; live export comparison pending |
| profile | profile.json | c8c422b90164a7d22d14ae617a0b4ff03eafff5edde5f7883ee5fa3356374cf2 | configuration | 1 | MIT | Local target profile |
| schematic | raw/board.kicad_sch | ab38b486cfd98a893b9fde03ca5434ace1306b96cb3730f149073ede16d766df | connectivity | fixture-1 | MIT | Original partial KiCad schematic; live export validation required |
| usart_review | reviewed/usart.md | 4c261df76f7766e236f91ce9cc9bb9e6c6038eae7cce0e646270fd3cd0c91132 | semantics | fixture-1 | MIT | https://ww1.microchip.com/downloads/en/devicedoc/atmel-7810-automotive-microcontrollers-atmega328p_datasheet.pdf |
| vendor_0 | raw/vendor/LICENSE | 023a098a014da4dadd19dfb96e8240b1c493676be5df6dfa0a8dde1a97cb71ab | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_10 | raw/vendor/avr/version.h | be10dc83b9b70b7e37b74f9cbcb0291f8decc8a1626c8a1c0d93b6ee2764eadf | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_12 | raw/vendor/bits/devinfo.h | 123219f9630d10c02022acc5b744a03eed40cbd70cc07af0dd2b65bf78feb25c | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_2 | raw/vendor/avr/common.h | c139d2f0537a04c90f0c48bb46b9cb9a81e41ddc66e3f888904a6b2fb18ee4f3 | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_3 | raw/vendor/avr/fuse.h | cd3e6d2b0869fafe2ec7c7245939f732e59f7c4a1ff5db5ff685dc643f6346ec | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_4 | raw/vendor/avr/interrupt.h | 3312cb9c4ea88b3756770d4a7dba3fd2363eccf2d95bbe339809a4ad881b96d3 | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_5 | raw/vendor/avr/io.h | d7b8af97116c16665d91ae8675ec6420f005254c16b4fd9e6f007bbc1608f2a9 | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_6 | raw/vendor/avr/iom328p.h | c7227f0fb809ecd959087a79b3a8618bad60d1a6a92bc2050618e0c22f407024 | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_7 | raw/vendor/avr/lock.h | 07ca647f8cfecf38e4fafc1fbfd8ca5897a8a9dedf284d91ba3760877e92d687 | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_8 | raw/vendor/avr/portpins.h | 94d0e0e5ee7c0a6bec166e2c1e484a12b54ef27949a1ad95b50ac476c621ae3d | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |
| vendor_9 | raw/vendor/avr/sfr_defs.h | cc722e1abb189dd6d836d73af5e59527f315453e9d7a2d6422f3b19ea2b8539a | declarations | pinned source bytes | BSD-3-Clause | Upstream source and license included in raw/vendor |

Editorial reviewer: Codex source-backed fixture editorial review. Basis: Checked against the linked vendor manuals and pinned declarations; independent hardware sign-off remains pending..

Editorial review is not independent hardware sign-off. See [[index]].
