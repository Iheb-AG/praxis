# I2C1 controller-transmit compile/model example

Selected bundle: `stm32f407g-disc1-e01-i2c-v1`; STM32F407VGT6, LQFP100,
MB997-E-01 reference. Actual board/silicon revisions remain unconfirmed.
**No physical I²C transaction is qualified.**

`application/main.c` uses the reviewed owned-startup clock callback, enables and
resets I2C1, and configures CR2/CCR/TRISE/OAR. It leaves PE disabled and does not
configure GPIO, choose a device address, issue START or transmit.
`application_transmit` is an integration entry with explicit wiring preconditions;
main never calls it. Its controller code is checked in the target translation
unit; the linker may discard the unused entry. The linked image demonstrates
configuration, not a device transaction.

`i2c_controller.h` supplies the bounded transmitter and cleanup logic shared with
the host effect model. That model checks read-to-clear ordering, simultaneous
errors, stuck commands, ownership and retry blocking. Host GCC runs the model;
ARM compilation/linking uses the separate build MCP and pinned Podman toolchain.
Startup, system and linker assets come from the build service. No UART telemetry
ABI or generic I²C debugger is added.

See [architecture, sequence and evidence](../../docs/i2c-expansion.md) and the
[matching OpenCode configuration](../opencode.i2c.example.json). No jumper or
physical action is needed for these software checks. A wired-device test remains
blocked pending bus pins, pull-ups, electrical and device-specific requirements.

Suggested MCP test prompt:

```text
Test Praxis I2C readiness using MCP only. Do not flash or access a probe.
Read the wiki index; confirm stm32f407g_disc1_mb997_e01 and MB997-E-01.
Confirm i2c1_controller_transmit is ready, but feature_i2c and i2c1_wired_transmit
are blocked. Follow prerequisites; retrieve complete RCC, FLASH, PWR and I2C docs.
Report controller_transmit_polling scope, clock assumptions, read side effects,
bounded waits and ARLO/STOP rules. Do not infer pins, pull-ups or a device address.
Get the build profile; require its revision to match the knowledge session.
Build source_directory stm32f407g-disc1-i2c/application and validate that artifact.
Write a report distinguishing reviewed facts, model checks, compilation/ELF checks
and untested physical behavior. Compilation does not establish an I2C transaction.
```
