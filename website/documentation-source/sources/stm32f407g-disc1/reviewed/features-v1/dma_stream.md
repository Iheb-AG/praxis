Only DMA2 supports the reviewed memory-to-memory mode. DMA1 is excluded. Use PAR as source, M0AR as destination, equal word widths, increments, FIFO, single bursts and a bounded item count. Buffers must be approved DMA-reachable memory; a C pointer value does not prove reachability.

Disable and wait for EN=0 before writing protected configuration. Clear flags through [[peripherals/dma]], configure, then set EN last. Completion polling must test errors and expire. Peripheral shutdown must follow stream disable/acknowledgement.

**Resolved source conflict:** the CMSIS header declares DMA_SxCR_ACK at bit 20. RM0090 pp.330–332 reserves that bit for this target. Header authority establishes the declaration, while the operating manual governs use: keep it zero.

Circular mode, direct mode, double buffering, peripheral handshakes and peripheral DMA routing are outside this memory-copy contract. See [[features]] and [[coverage]].

Evidence: rm_features_306:page:306, rm_features_311:page:311, rm_features_313:page:313, rm_features_324:page:324, rm_features_325:page:325, rm_features_330:page:330, rm_features_331:page:331, rm_features_332:page:332, rm_features_333:page:333, rm_features_334:page:334, rm_features_335:page:335, rm_features_336:page:336. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
