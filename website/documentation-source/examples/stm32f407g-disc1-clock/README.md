# F407 clock-mode compilation and ordering example

This example implements the separately selected
[clock bundle](../../bundles/stm32f407g-disc1-e01-clock-v1/wiki/index.md), revision
`0e8737e667f05858aa39cf6484cd7a5c30125fd5ae2910c441187185380eccda`.
It passed actual knowledge/build MCP retrieval, rootless ARM compilation/full linking and
ELF revalidation. **It has not been flashed or physically qualified.**

The application explicitly establishes the declared HSE8 crystal / Scale 1 / five-wait-state
168 MHz operating point. Supply 2.7–3.6 V, clock hardware and exclusive reset/startup ownership
are preconditions, not detected physical facts. It rejects active PLLI2S/CSS and prefetch state,
preserves unrelated configuration, bounds every wait and stops dependent initialization on failure.
It leaves interrupts masked and publishes a local `praxis_clock_smoke` result. That structure
is not the UART telemetry ABI, so the existing UART observation tool cannot read it.

The [shared sequence](application/clock_sequence.h) orders the actual
[register-writing callback](application/main.c). The host
[register fixture](../../tests/fixtures/f407_clock_model.c) runs that same callback against RAM
instances of the approved CMSIS structures, simulates readiness/status responses and checks
clock prerequisites. Its tests cover a successful operating point, failure at all 24 stages,
zero budget and premature PLL switching. It checks the selected masks/encodings and preserves
unrelated gates, calibration, cache configuration and backup-domain configuration.

These tests establish this example's modeled ordering and bounded failure handling. They do
not establish analog regulator behavior, oscillator accuracy, bus timing, silicon errata
compliance, arbitrary generated firmware correctness or automatic rollback after a failed switch.
Host `gcc` tests the model; target compilation uses `arm-none-eabi-gcc` in the pinned sandbox.
No flashing or target-control tool is enabled by this reproduction command:

```bash
python tools/check_feature_modes_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --expect-rng-clock-ready \
  --source-directory stm32f407g-disc1-clock/application \
  --output /absolute/path/to/new-clock-check
```

Run from the repository root with installed dependencies and a provisioned rootless image.
See [clock-mode contracts and sequence diagrams](../../docs/clock-modes.md).
