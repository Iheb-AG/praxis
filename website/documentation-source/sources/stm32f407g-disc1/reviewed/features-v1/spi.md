This review establishes controller semantics for SPI1/SPI2/SPI3 master full-duplex polling. The I2S extension instances share a C layout but are excluded from this SPI mode. SPI CRC, TI framing, slave operation, I2S audio and DMA/interrupt transfers need their own reviewed contracts.

Select CPOL/CPHA and bit order from the peer, compute BR from the actual instance peripheral clock, configure with SPE=0 and select I2SMOD=0. Software NSS uses SSM=SSI=1; peer chip select requires separately supported GPIO connectivity. Use Motorola FRF=0 and read every received frame. Finish RX, then wait TXE=1 and BSY=0 before clearing SPE.

SR reads can clear FRE. OVR clears by DR read then SR read. MODF requires SR access then CR1 write and a safe NSS level before restoration. All waits are bounded.

**Board readiness is blocked:** no SPI1_SCK/MOSI/MISO mapping is asserted in the current schematic subset. Never fall back to a remembered evaluation-board pinout. Resolve [[schemas/custom_pcb_netlist]] and reviewed AF availability before generating wired firmware. Prerequisites: [[peripherals/rcc]], [[peripherals/gpio]]. See [[features]] and [[coverage]].

Evidence: rm_features_877:page:877, rm_features_880:page:880, rm_features_881:page:881, rm_features_882:page:882, rm_features_883:page:883, rm_features_887:page:887, rm_features_888:page:888, rm_features_889:page:889, rm_features_891:page:891, rm_features_892:page:892, rm_features_911:page:911, rm_features_912:page:912, rm_features_913:page:913, rm_features_914:page:914, rm_features_915:page:915, rm_features_917:page:917. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
