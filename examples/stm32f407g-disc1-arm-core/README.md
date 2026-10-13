# STM32F407 SysTick and SCB example

This source-backed example demonstrates the
[ARM core contracts](../../docs/arm-core-support.md) for the STM32F407G-DISC1 MB997-E-01
reference. It checks nominal HSI16 without switching a live clock, selects the pinned Flash
vector table, sets SysTick priority and clears pending state, then starts a 1 kHz SysTick ISR.
The green LED_A/LD4 on PD12 toggles every 500 software ticks. Timing is nominal, not measured.
No extra wiring is required; the physical PCB revision remains unconfirmed.

The artifact is built and ELF-validated but **unflashed and physically untested**. The example
does not implement USER-button behavior, UART, an RTOS tick or a bootloader. A failed startup
retains global masking and reports `praxis_core_status`; it does not retry automatically.

Use [the matching client configuration](../opencode.arm-core.example.json), replacing the
absolute paths. Both servers must select `stm32f407g-disc1-e01-arm-core-v2`. Hardware tools
are disabled in this example configuration. Compilation uses the provisioned rootless image;
it supplies pinned startup, system, runtime and linker assets rather than accepting generated ones.

Reproduce the real MCP retrieval/build test:

```bash
.venv/bin/python tools/check_workflow_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-arm-core-v2 \
  --workflow systick_1khz_interrupt \
  --blocked-workflow feature_usb_otg_global --blocked-workflow feature_flash \
  --mode systick/core_clock_interrupt --mode scb/flash_vector_table \
  --mode scb/systick_exception_setup --mode rcc/hsi16_core_checked \
  --signal LED_A --source-directory stm32f407g-disc1-arm-core/application \
  --output /tmp/praxis-arm-core-example-replay
```

Use a new output directory for each run. Source review starts from
[the programming-manual catalog](../../sources/stm32f407g-disc1/web-sources-arm-core.json).
Downloaded source bytes and private probe/operator files are not part of the public distribution.
Serving the published bundle needs neither PDFs nor ingestion tools; recompilation requires the
registered evidence archives and review receipts with their exact hashes.

A prompt for an assistant using the configured MCP pair:

> Read the Praxis index and confirm STM32F407VGT6, MB997-E-01 and the corrected ARM core
> bundle revision. Resolve LED_A through the netlist tool. Follow the dependency closure and
> read the checked HSI16, SCB vector/priority/pending and SysTick interrupt contracts. Explain
> the startup checklist with sources, then generate application C/header files for a green LED
> toggling every 500 SysTick software ticks. Use the supplied startup/linker assets. Check clock
> state rather than assuming the PLL recipe is running, preserve unrelated SCB state and reject
> unsupported configuration. Build and revalidate through the build MCP. Report retrieval,
> compilation and physical evidence separately; physical success is untested until an approved
> exact-image execution and observation are completed.
