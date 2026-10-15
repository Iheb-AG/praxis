# MCP test prompts

Use real tool calls and retain their actual results. Restart the client after changing a stdio
server configuration; each server process serves one fixed bundle revision. Replace absolute
path placeholders in the [OpenCode example](../examples/opencode.example.json) before use.
Hardware-profile, artifact and authorization paths are operator inputs, not shipped credentials.

## Discovery and routing

> Discover Praxis tools. Read the index and record exact target, package, board revision and
> bundle revision. Use only MCP-returned facts. Request the intended peripheral, follow missing
> prerequisites, and query its required board signals. Report declarations, reviewed operating
> semantics and workflow readiness separately. Stop on missing facts or wrong targets. Do not
> generate firmware or use web/shell tools to fill knowledge gaps. Record actual tool responses,
> not a narrated claim that calls passed.

## Build and validate

> Use the matching knowledge and build MCP. Confirm target/bundle identity with both. Retrieve
> index, required signals and prerequisite documents. Create application C/H within the approved
> workspace using returned facts. Use the build service's approved startup/linker assets rather
> than creating replacements. Call build_firmware and validate_firmware. Report compile and image
> validation separately, with artifact/source hashes. Do not flash. Missing supported facts block
> code generation; a successful compiler run does not establish physical behavior.

## Supported scenario and missing-feature boundary

Select the matching [clock bundle configuration](../examples/opencode.clock.example.json)
for knowledge/build servers, replace absolute paths and restart both MCP processes. This test
does not need a connected board. The local [support command](capability-support.md) can assess
the selected bundle first; the assistant must still obtain hardware facts through MCP.

```text
Test Project Praxis through real MCP calls only. Read the index and confirm target
stm32f407g_disc1_mb997_e01, reference revision MB997-E-01, and session bundle revision
0e8737e667f05858aa39cf6484cd7a5c30125fd5ae2910c441187185380eccda.
Compare it with the build MCP profile. Stop on any mismatch.

Assess these two requests separately:
1. The declared uart_timer_interrupts workflow: identify its exact scope, required board
   signals and prerequisite documents. Retrieve the required facts before proposing code.
   State additional requirements that the declared workflow does not cover.
2. An application bootloader that receives an image and erases/programs internal FLASH:
   identify the missing bootloader contract and the blocked feature_flash workflow.
   Do not infer erase/program support from FLASH read-latency guidance, supplied startup
   assets or the probe's ability to flash. Do not generate unsupported bootloader code.

Write mcp-support-results.md with actual calls, revisions, workflow scope, blockers and
the distinction between reviewed knowledge, compile results and physical qualification.
This scenario is a retrieval/readiness test: do not build, flash, reset, halt, resume or
change option bytes. Do not search manuals or remembered pinouts to bypass missing facts.
```

Expected evidence: the first request has a declared knowledge-ready scope; the second
remains unsupported. Neither outcome proves arbitrary generated firmware correctness.

## Read-only inspection

> Discover the optional hardware tools, enumerate probes and use only the explicitly selected
> probe. Inspect target and execution through MCP. Report MCU compatibility, physical board
> revision uncertainty, running-state uncertainty and observation limits. Do not reset, halt,
> resume or flash. Never silently switch to another probe.

## Approved programming

> Validate the intended artifact, inspect the selected target and obtain its exact plan through
> MCP. Present artifact identity, image bytes, erase sectors and execution actions for operator
> approval. Use only an applicable operator-provided authorization. Recheck the plan, flash once,
> require exact readback and reported halted state, then perform only the approved reset/run.
> Stop on uncertain or failed writes; do not automatically retry. Record actual run IDs, audit
> results and remaining attempt budgets. Physical behavior needs separate observations.

## Execution-only

> Use the selected target and exact installed artifact with the provided execution-only grant.
> Revalidate and reverify image bytes through MCP, then request only the permitted execution
> action. No programming tool should be exposed. Stop on mismatch or exhausted scope, and report
> execution state separately from human-visible function.

## UART loopback

> Use the STM32F407G-DISC1 UART bundle selected by the operator. Confirm exact identity and
> reference-versus-physical revision. Retrieve LED/button, USART2 and connector topology through
> MCP; follow clock/GPIO/USART/timer/EXTI/SYSCFG/NVIC dependencies as required. Generate a bounded
> loopback protocol with timer scheduling, interrupt-driven receive and debounced run/pause control
> only if all required operating facts are reviewed. Use approved build assets, build and validate
> through MCP. Show any required wiring before hardware testing; wiring changes require power
> disconnected. Programming requires exact-artifact approval. Report compiler, readback, human
> LED observations and telemetry/capture outcomes separately.

## Telemetry

> Discover read_firmware_telemetry and confirm its launch-selected artifact. Inspect the selected
> target in this process, then obtain bounded coherent samples. Report paused/running state,
> timer progress, validated-frame deltas and failure reasons. An image mismatch is a guard failure
> to resolve, not permission to flash. Ask for USER stimulus if required; absent UART progress
> while paused is expected. Treat counters and status LEDs as firmware self-reports rather than
> independent packet or timing measurements. Do not halt or write to make telemetry succeed.


## Mode-scoped feature bundle

Select both servers from [the feature configuration](../examples/opencode.features.example.json),
replace the absolute paths, provision the sandbox and restart the client MCP processes.
This configuration enables retrieval/building only, with no hardware profile or flash grant.

```text
Test Project Praxis through its MCP tools. Use hardware facts only from MCP responses.
Confirm session target stm32f407g_disc1_mb997_e01 and bundle revision
bd8b793388dff8303e5f7d46469b48afea1807dd2f7ae9b71541eb01779a3fbc;
compare that revision with project-praxis-build.get_build_profile. Stop on mismatch.
Read the index, follow returned prerequisites, and retrieve CRC, DMA and DMA2 stream 0.
Explain the CRC C-member versus bus-access-width distinction, the reset command versus
register reset value, and why DMA1 cannot inherit the DMA2 memory-copy mode. Cite the docs.
Retrieve SPI1 and RNG guidance. Query SPI1_SCK and report missing board connectivity and
the blocked RNG clock prerequisites. Do not supply remembered pins or mark those ready.
Build examples/stm32f407g-disc1-crc-dma/application through the matching build MCP
(source_directory stm32f407g-disc1-crc-dma/application), then validate the returned artifact.
Write mcp-test-results.md with actual calls, gate errors, bundle/artifact identity, compile
and ELF outcomes, and the distinction between reviewed modes and physical qualification.
Do not flash, reset, halt, resume, change option bytes, or claim runtime success.
The example result object is not the UART telemetry ABI; do not try to read it with that tool.
```

The build workspace must contain the example under the configured relative path. The deterministic
[replay client](../tools/check_feature_modes_mcp.py) covers this protocol/build scenario without
an external model. A live assistant's written report is supplementary evidence.
