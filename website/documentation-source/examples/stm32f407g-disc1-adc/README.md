# ADC1 internal-reference example

This example exercises the `adc1_internal_reference` knowledge workflow on the
STM32F407VGT6 MB997-E-01 reference board. **No external wire is needed.** It
selects ADC1 channel17, acquires one raw12-bit value, and stops ADC/reference/TIM2.
It contains no UART telemetry ABI and makes no calibrated voltage claim.

Use [the matching MCP configuration](../opencode.adc.example.json), replacing
absolute-path placeholders. Knowledge and build must advertise the same bundle
revision. Startup, vector table, system and linker assets come from the build
service; the assistant supplies only application C/H files.

The selected clock contract assumes an8MHz HSE crystal and the reviewed
168MHz operating point, appropriate supply/FLASH latency and exclusive fresh
startup. ADC additionally assumes VDDA/VREF+ in2.7–3.6V. These assumptions are
not physical measurements. Verify physical board revision and clock/supply
applicability before proposing programming.

`application/main.c` uses the previously tested clock callback, then a finite
ADC sequence. ADC common prescale4 gives21MHz; SMP17=111 chooses480cycles.
TIM2 PSC8399 and ARR9 supply nominal1ms settling under TIM2CLK=84MHz. UG can
set UIF, so the code clears SR after UG before starting. ADC EOCS enables
overrun detection. DR is read once after EOC, which clears EOC on silicon.
Every polling stage is bounded; failure stops subsequent initialization.
Existing ADC/TIM2 owners and unexpected clock state are rejected.

The result globals are `praxis_adc_clock_result` and `praxis_adc_result`.
Their `completed` fields describe the corresponding software sequence; the ADC
result contains a raw code only after successful completion. They are not
accepted by the existing UART telemetry reader. No new debugger or physical
result-read tool is claimed here.

```bash
.venv/bin/python tools/check_adc_workflow_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-adc-v1 \
  --source-directory stm32f407g-disc1-adc/application \
  --output /tmp/praxis-adc-build
```

The command requires a provisioned rootless Podman image. The initial attempt
returned `MISSING_TOOL`. After Podman installation and import of the exact locked
image, an actual MCP replay passed compilation, linking, ELF/vector validation
and artifact revalidation. The artifact ID is
`74a18d92fd2925ba52d343fc1c0d588b3a71afa2490a1c1d2ce28dd7b5e1c9d3`;
see [build evidence](../../docs/adc-build-evidence.json). It has not been flashed
or physically tested. Host tests exercise the same register callback with modeled
flag/command effects; they are not silicon simulation.

An MCP scenario prompt:

> Read the Praxis index and confirm STM32F407VGT6 and MB997-E-01 reference
> identity, distinguishing my unconfirmed physical revision. Select the exact
> adc1_internal_reference workflow. Follow its document and mode prerequisites;
> retrieve ADC/common, RCC, FLASH, PWR and TIM guidance. Explain why no GPIO or
> external jumper is required. Produce application C/H for one ADC1 VREFINT
> sample with bounded waits, proper startup/acquisition settling, overrun checks,
> and cleanup. Use the matching build MCP assets and build_firmware. Preserve
> actual diagnostics; if Podman or any required hardware fact is missing, report
> the blocker. Do not substitute another ADC mode, native compilation, a voltage
> calibration claim or the UART telemetry reader. Do not flash, reset or attach
> a debugger in this scenario. Write firmware files and a results report that
> separates retrieval, host models, target compilation and physical testing.

See [the compiler expansion and sequence](../../docs/adc-expansion.md).
