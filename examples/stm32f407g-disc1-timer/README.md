# STM32F407 timer examples

`irq_application` adds the separate TIM5 CH3 IRQ50 capture workflow paired with
TIM2 CH2 PWM. Its seventeen-case plan retains every previous application; the new
180-byte `timer-irq-v1` ABI records IRQ receipts and quiet cleanup independently of
the polling ABI. See [contracts, sequence and reproduction](../../docs/timer-irq.md).
This new image is software-tested; it has not been flashed or physically qualified.

`routes_telemetry_application` adds a fixed, coherent terminal report for the paired
route. See [MCP observation and qualification](../../docs/timer-observations.md).
Its sixteen-case acceptance plan retains every earlier source snapshot unchanged;
heartbeat publication does not repeat the loopback test. Its later exact-artifact
[physical trial](../../docs/reports/timer-route-results.md) passes wired success,
no-edge timeout and recovery; that evidence does not qualify the new IRQ image.

The newer `routes_application` adds PA1/TIM2_CH2 PWM and independent
PA2/TIM5_CH3 rising capture. See [source contracts, wiring preconditions and
qualification limits](../../docs/timer-routes.md). It uses the separately selected
`stm32f407g-disc1-e01-timer-routes-v1` bundle and the 15-case
`examples/acceptance/stm32f407g-disc1-timer-routes.json` plan. No flash or physical
route test has occurred. The internal examples below remain unchanged and need no wire.

Two separate C/header-only application snapshots use the same checked controller.
They are compile/model-tested examples, not flashed or physically qualified firmware.
The target is STM32F407VGT6 / STM32F407G-DISC1 reference MB997-E-01; physical revision is
unconfirmed. Neither example configures GPIO or needs a jumper.

| Application | Behavior | What it does not establish |
| --- | --- | --- |
| `pwm_application` | Configure nominal1kHz PWM1 OC1REF, change25%→75% through CCR1 preload, wait for fresh updates, stop | CC1E stays0: no external pin waveform or measured frequency |
| `capture_application` | Stopped CNT values0x12345678 and0xFFFFFFFE captured through EGR.CC1G; check flags/data and stop | No external input, edge filtering, period measurement or ISR/DMA handling |

Both require a fresh privileged startup with PRIMASK=1, checked nominal HSI16,
AHB/APB divisors1, exclusive TIM2 ownership, TIM1 clock-gated and no consumers of
TIM2's initialization UG/TRGO pulse. The mode is refused when those checked clock,
gate or context assumptions do not hold. Startup/linker/runtime are supplied by
the separately pinned `assets/stm32f407vg` profile; these directories contain no
startup or linker replacements.

The controller header and MMIO adapter are copied byte-for-byte into both directories
because the build service snapshots each application independently and forbids
includes escaping its snapshot. A test enforces equality. The host effect model
executes that same controller, with independent preload/flag/access semantics.

The examples leave status in `praxis_timer_status`, with `praxis_timer_completed=1`
only after all steps and checked shutdown succeed. The capture application records
two checked values in `praxis_timer_captures`. These are application symbols, not
a new telemetry MCP schema. No live read of them is included in compile acceptance.

Use the new bundle when launching the knowledge server; existing sessions retain
their original revision and require a restart to select another bundle:

```bash
praxis serve --bundle /absolute/path/to/praxis/bundles/stm32f407g-disc1-e01-timer-modes-v1
```

Replay all fourteen isolated builds and ELF validations through MCP:

```bash
.venv/bin/python tools/check_target_acceptance_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-timer-modes-v1 \
  --plan examples/acceptance/stm32f407g-disc1-timer.json \
  --catalog examples/capabilities/stm32f407g-disc1-timer.json \
  --workspace examples --assets assets/stm32f407vg --lock toolchain-f407.lock.json \
  --output /tmp/praxis-timer-acceptance
```

Use an unused output directory. Required pinned Podman images must be installed.
This command exposes no flash/probe/control tools. Compilation/ELF success does
not establish execution, pin routing or physical timing. Any later physical test
needs separate artifact-bound authorization and observations.

See [contracts, sequence and evidence](../../docs/timer-modes.md) and the
[published timer document](../../bundles/stm32f407g-disc1-e01-timer-modes-v1/wiki/peripherals/tim.md).
