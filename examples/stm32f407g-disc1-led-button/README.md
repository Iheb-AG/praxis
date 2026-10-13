# Discovery LED/button reference application

This trusted fixture targets the **MB997-E-01 reference bundle**. The user's physical
revision remains unconfirmed. LED_A is LD4/PD12; LED_B is LD3/PD13; B1 is PA0, active
high, with an external pulldown and SB20 closed. See the bundle's circuit provenance.

LED_A toggles every 500 ms. LED_B follows B1 after 50 ms of stable input on both edges.
The application explicitly selects HSI, waits with bounded loops, selects AHB /1,
updates SystemCoreClock and configures processor-clock SysTick for 1 ms. HSI accuracy
limits physical timing. It preloads both LEDs OFF before enabling their output modes.

The build profile supplies pinned ST startup/system code, CMSIS headers, a minimal
C initialization runtime and a linker script. Flash is 1 MiB; main SRAM is 128 KiB;
CCM is a separate, unused 64 KiB bank. Initial SP is 0x20020000 with 4 KiB reserved.

```bash
uv sync --locked --extra build
uv run praxis build --bundle bundles/stm32f407g-disc1-e01-m1 \
  --assets assets/stm32f407vg --workspace examples \
  --source stm32f407g-disc1-led-button/application \
  --artifacts .praxis-output/firmware-artifacts --lock toolchain-f407.lock.json
```

Rootless Podman and the provisioned image are required. On this development machine,
source `.praxis-output/podman-env.sh` first to select the project-local runtime.
The service never runs this application or programs the board. Compilation and image
checks cannot establish LED output, button wiring, timing or general firmware correctness.

`validated_opencode_application/` is a reviewed copy of the user's generated application after
clock failure handling was corrected. The trusted host fixture tests establish its AHB-prescaler
synchronization and fail-stop behavior for modeled clock/SysTick failures. The original source
is retained as a negative regression fixture. Host model tests do not replace target compilation
or physical measurements. See [the updated run report](../../docs/build-service-evidence.json).
