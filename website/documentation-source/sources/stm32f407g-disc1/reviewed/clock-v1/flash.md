Reviewed subset: STM32F405/407 FLASH_ACR read-interface timing only. This is not flash
programming, option-byte, bootloader, cache-maintenance or low-power support. Other register
rows remain declarations. The F42/F43 register variants in the shared manual do not apply.

For the declared 2.7–3.6 V supply and Scale 1, 168 MHz HCLK requires LATENCY=5. Set and read
back latency before raising HCLK. When lowering frequency, first confirm the lower clock via
RCC SWS/prescalers; only then lower latency and read it back. Bound each acknowledgement wait
and stop initialization on failure. The loop budget is not a measured time deadline.

LATENCY is bits 2:0 for this target. Reserved bits 7:3 and 31:13 stay zero. ICEN/DCEN and
PRFTEN are separate controls. ICRST/DCRST are write commands permitted only while their
respective caches are disabled: never replay those command bits during a latency update.
This contract does not enable prefetch, change cache state or substitute for silicon errata
review. Prefetch must be disabled below 2.1 V, outside the supported operating point.

HEDG document retrieval starts with [[peripherals/rcc]]. The operating-mode graph separately
requires this latency contract before the high-speed RCC switch. See [[peripherals/pwr]],
[[features]] and [[coverage]]. No code execution, flash write or physical clock test was performed.

Evidence: rm_clock_v1_80:page:80 (voltage scale and frequency limits),
rm_clock_v1_81:page:81/table:1 (F405/F407 latency table),
rm_clock_v1_82:page:82 (increase/decrease ordering), rm_clock_v1_98:page:98 (ACR fields/access).
All complete pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
