The controller owns status and W1C flag-clear groups; [[peripherals/dma_stream]] owns each transfer configuration. A net is not a DMA request mapping. This review covers polling status/clear behavior and the DMA2 memory-copy subset, not every peripheral channel assignment.

Use the exact controller/stream flag group. Direct W1C writes clear selected flags; a read-modify-write is inappropriate. Enable the clock through [[peripherals/rcc]] first. See [[features]] and [[coverage]].

Evidence: rm_features_324:page:324, rm_features_325:page:325, rm_features_327:page:327, rm_features_328:page:328, rm_features_329:page:329, rm_features_330:page:330. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
