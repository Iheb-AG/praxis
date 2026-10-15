# DAC channel1 software-trigger compile/model example

Bundle: `stm32f407g-disc1-e01-dac-v1`, STM32F407VGT6, LQFP100,
MB997-E-01 reference. Physical PCB/silicon revision remains unconfirmed.
The operating contract covers channel1, 12-bit right-aligned data, software
triggering and **digital completion** at the reviewed 42 MHz PCLK1 point.

`application/main.c` uses the reviewed owned-startup clock setup, enables and
resets the DAC block, then configures software triggering with **EN1=EN2=0**.
Main never calls the output entry, configures PA4, starts a timer or drives an
analog output. No jumper or physical action is needed to compile or model it.

`dac_controller.h` is shared with the host MMIO-effect model. The integration
entry `application_output` is retained in the linked ARM ELF through a volatile
address reference. The target-link test checks that retention, so the full
transfer path is compiled and linked despite main never executing it. This
establishes integration availability, not a physical output measurement.

A future caller must review board connectivity, GPIO analog configuration,
reference/supply, loading and pin conflicts before enabling an output. The
`output_reviewed` argument represents that caller precondition; setting it true
does not establish or retrieve those facts. The selected bundle lacks the
required DAC output/reference board endpoints, and its wired workflow is blocked.

The controller requires exclusive ownership of both DAC channels for reset,
uses literal writes to write-only SWTRIGR, never writes read-only DOR, and retains
W1C underrun diagnostics. A bounded fresh TIM2 interval precedes the trigger and
another precedes checking DOR, including when the old code already matches.
The callback owns TIM2 for each interval and releases its gate afterward. It
rejects a previously enabled TIM2 rather than taking over another owner.
Successful output remains held until explicit shutdown. Failures and shutdown
require an owned reset before reconfiguration; no automatic retry is provided.

Host GCC exercises the digital effect model. The build MCP uses the pinned
rootless Podman ARM toolchain, vendor startup/system assets and the validated
linker layout. No DAC voltage, settling accuracy, DMA, channel2 or waveform mode
is qualified. See [design and evidence](../../docs/dac-expansion.md) and the
[matching OpenCode configuration](../opencode.dac.example.json).

Suggested MCP prompt:

```text
Test Praxis DAC readiness through MCP only. Do not access a probe or flash.
Read the wiki index and confirm stm32f407g_disc1_mb997_e01, MB997-E-01.
Require dac_channel1_software_trigger to be ready, but feature_dac and
dac_channel1_wired_output to remain blocked. Follow every prerequisite and read
the complete RCC, FLASH, PWR, GPIO, TIM and DAC documents.
Explain SWTRIGR write-only access, DOR digital-only completion, retained W1C
errors, shared-channel reset ownership and bounded fresh waits. Do not infer
board output pins/reference endpoints or claim 12-bit analog settling accuracy.
Get the build profile and require its revision to match the knowledge session.
Build source_directory stm32f407g-disc1-dac/application and validate that artifact.
Report reviewed knowledge, modeled failures, ARM compile/link/ELF evidence and
untested physical behavior separately. Main must leave EN1=EN2=0. Do not call
the retained output entry until its board/electrical preconditions are reviewed.
```
