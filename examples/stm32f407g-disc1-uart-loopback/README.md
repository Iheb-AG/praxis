# STM32F407G-DISC1 UART loopback example

This application is generated from actual Praxis MCP retrieval, following publication through
the new ingestion MCP. Reference board: **MB997-E-01**, MCU STM32F407VGT6. Physical PCB revision
remains unknown. Source evidence and generated firmware have separate review/verification stages.

With power disconnected, verify connector orientation and fit **PA2/P1-14 ↔ PA3/P1-13**.
The user reported fitting this wire. Leave ST-LINK USB as the programming connection.
No USB-to-UART adapter or solder modification is needed. SB20 must connect USER to PA0.

Application C/H files are under `application/`. Praxis supplies approved startup, linker,
system and runtime assets through its isolated build service. Main SRAM is 128 KiB;
64 KiB CCM is a separate unused region. Do not supply a replacement linker/startup here.

`telemetry_application/` is a separate counter-enabled variant. Its original protocol/control
checks run alongside the baseline checks. Build it by selecting that source directory; do not
reuse the baseline artifact's programming grant. See the [telemetry ABI and MCP sequence](../../docs/firmware-telemetry.md).

## Operation

| Indicator/control | Behavior |
| --- | --- |
| Green / PD12 / LD4 | Toggles every nominal 500 ms in every application state |
| USER / PA0 | Debounced 50 ms press starts a fresh run or requests pause; release rearms |
| Orange / PD13 / LD3 | 30 ms pulse after a validated loopback frame |
| Blue / PD15 / LD6 | Latches after 100 consecutive validated frames, roughly ten seconds |
| Red / PD14 / LD5 | Latched timeout, malformed frame, UART error or queue overflow |

Boot is paused. Press USER to start; hold must not retrigger. Press again to pause, draining
one in-flight frame within its 250 ms deadline. A new run clears counters and result LEDs.
Green continues during pause/failure. A button held during reset must first be released.

Clock setup selects nominal HSI 16 MHz with AHB/APB1/APB2 /1 and bounded readiness waits.
TIM2 PSC=15, ARR=999 yields nominal 1 kHz. USART2 uses AF7 at PA2/PA3 and BRR=139 for nominal
115200 8N1 (actual nominal baud 115107.9). Oscillator accuracy is not measured. SysTick is off.
EXTI0 observes both USER edges; main performs debounce. IRQ policy is TIM2 priority4,
USART2 priority5, EXTI0 priority6. Timer flags clear by writing zero; EXTI pending uses W1C.
UART receive errors clear with SR followed by DR. No DMA or timer capture/PWM is used.

Frames are 19 bytes: A5 5A, version1, type1, sequence32 LE, length8, payload8, CRC16 BE.
Payload byte i is `((sequence >> (8*(i % 4))) ^ (0x31 + 17*i)) & 0xff`.
CRC-16 polynomial1021, initFFFF, no reflection/final XOR covers bytes2–16.
Sequence wraps modulo2^32. A valid CRC alone is insufficient: exact sequence/payload/framing
must match the one outstanding frame. Starts are at least100 ms apart; reply deadline250 ms.
Unexpected active-run bytes fail rather than silently resynchronize. RX/TX queues have63 usable
bytes each. Main queue operations are short interrupt-masked sections; ISR never blocks,
allocates, computes a whole-frame CRC or parses a protocol message.

## Verification and build

Run the trusted host checks:

```sh
.venv/bin/pytest -q tests/test_uart_loopback.py
```

Configure both knowledge and build services with
`bundles/stm32f407g-disc1-e01-uart-v1`. The separate
[temp/uart-loopback-test/opencode.json](../opencode.example.json) does this;
existing default launchers still select their prior bundle. Read index/topology and follow the
manifest prerequisites through MCP. Then call build MCP:

```json
{"source_directory": "stm32f407g-disc1-uart-loopback/application"}
```

Require both `compile_passed` and `image_validated`, then `validate_firmware` for the returned
artifact. Build/link success is not an electrical loopback or interrupt-order measurement.
The first MCP link caught aggregate initialization emitting a missing `memset`; scalar
initialization fixed it without changing the pinned freestanding runtime or vault.

Use a newly target-bound hardware profile and exact artifact plan for flashing. The old
LED/button authorization is consumed and does not cover this image. No automatic retry of a
failed/uncertain write. Actual progress is recorded in
[temp/uart-loopback-test/RESULTS_REPORT.md](../../docs/reports/uart-loopback-results.md).

For physical tests, start with the fitted wire and check orange activity, blue success and no
red. Check pause/restart and held-button behavior. For a negative test, pause, disconnect all
power, remove the jumper, reconnect and start: red should latch and green continue. An open RX
pin may produce a UART error before timeout; visual observation cannot prove a precise deadline.
Power off before restoring the jumper. This test does not establish external-device UART
interoperability, measured timing, DMA or arbitrary timer-mode support.
