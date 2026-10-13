# Physical flash demonstration through Praxis MCP

This demonstration uses the validated LED/button application, not the pending UART loopback
scenario. It needs only the ST-LINK USB connection; no jumper or serial adapter is needed.
The user requested a flashing demonstration while the board remained connected.

The selected knowledge bundle is `stm32f407g-disc1-e01-m1`, matched to the existing hardware
profile and approved startup/system/linker assets. This demonstration does not change the
new peripheral-discovery bundle or claim operating support for timers, EXTI, or UART loopback.
The physical PCB revision remains unconfirmed; MB997-E-01 is the documented reference.

## Actual result: passed

On 2026-10-10 the user explicitly approved the exact sector-0 erase, image write and reset/run.
Praxis completed **one flash and one reset/run**, with persistent server audits matching both
actual MCP responses. All 1,164 image bytes matched readback. Flash returned `halted` and the
reset/run returned `running` after its 1,000 ms observation window. The user then confirmed:
**green blinking, orange on while USER is held and off after release, with green continuing**.

Flash run: `c0722355ef5548d89e7ee4270a9c90e7`.
Reset/run: `625b8dd4839343849a9b530b5d0f4666`.

The corrected halted core-register query succeeded on the physical target:
SP=`0x20020000`, PC=`0x08000424`, xPSR=`0x01000000`. A later fresh diagnostic attachment
returned execution state `unknown`, nominal HSI 16 MHz, AHB /1, SysTick LOAD=15999 and zero
CFSR/HFSR. That attachment does not invalidate the preceding reset/run observation, and its
GPIO samples do not independently establish optical output. Fault address values were not valid.

This demonstrates the exact flash/readback/reset-run path for this artifact and board.
Standalone halt/resume, stepping, breakpoints, calibrated timing and UART loopback were not tested.
The earlier failed flash audit remains unchanged; this is a new approved attempt, not a rewrite
of that historical result. See [machine-readable evidence](flash-demo-evidence.json).

## Actual preparation

The direct MCP client retrieves the index, LED_A/LED_B/USER_BUTTON circuits and RCC/GPIO
documents. It then uses the build MCP to obtain the asset profile, compile and link in the
rootless sandbox, validate the artifact, enumerate the probe, inspect its target, collect
approved diagnostics and produce a read-only flash plan.

- Application: `examples/stm32f407g-disc1-led-button/validated_opencode_application`.
- Artifact: `0f3095c100e6311acb62ad085b9d6ec08e9c0a249741f6544a40280e94e39c44`.
- Programmed image: 1,164 bytes starting at `0x08000000`.
- Complete erase: sector 0, `0x08000000–0x08003FFF`, 16 KiB.
- Initial stack: `0x20020000`, within the 128 KiB main SRAM contract.
- Startup: pinned ST vector table, 98 entries; CCM remains a separate unused bank.
- Preflight: family/core/flash compatible, physical package/revision not detected;
  nominal HSI 16 MHz and AHB /1, CFSR/HFSR zero. A newly attached debugger returned execution
  state `unknown`; that is not evidence of a halted, running or failed firmware.

The first client attempt stopped at index handling because it did not unwrap the MCP SDK's
structured string result. It made no hardware requests. The response handling was corrected;
the subsequent preparation completed, including build and actual read-only board inspection.

See [recorded evidence](flash-demo-evidence.json). Raw preparation responses and device
identifiers remain in `.praxis-output/flash-demo-preflight-20261010-2/`; public evidence omits
full probe serials and MCU UIDs.

## Programming sequence

```mermaid
sequenceDiagram
    actor User
    participant Client as Direct MCP client
    participant Knowledge as Praxis knowledge MCP
    participant Build as Praxis build MCP
    participant Sandbox as Rootless compiler sandbox
    participant Probe as ST-LINK/OpenOCD
    participant Board as STM32F407
    Client->>Knowledge: Index, LED/button nets, RCC and GPIO
    Knowledge-->>Client: Complete documents and provenance
    Client->>Build: build_firmware(application)
    Build->>Sandbox: Compile and link with approved assets
    Sandbox-->>Build: ELF, binary, hex and diagnostics
    Build-->>Client: Validated artifact ID
    Client->>Build: inspect_target, inspect_execution, plan_firmware
    Build->>Probe: Read target identity and approved diagnostics
    Probe->>Board: Bounded reads; no reset/halt/write
    Build-->>Client: Exact artifact/target/erase plan
    Client-->>User: Review complete sector erase and new image
    User->>Client: Approve exact flash and reset/run scope
    Note over Client,Build: Fresh operator grant; one flash attempt and one reset/run
    Client->>Build: flash_firmware(artifact, connection)
    Build->>Probe: Recheck identity, reset/halt, erase sector 0, program
    Probe->>Board: Write approved image and read it back
    Build-->>Client: Exact readback result, halted state and audit ID
    alt Flash/readback succeeded
        Client->>Build: control_execution(reset_run)
        Build->>Probe: Reverify image bytes, reset/run, observe
        Build-->>Client: Execution result and audit ID
        Client-->>User: Request actual LED/button observations
    else Failure or uncertainty
        Client-->>User: Stop and report; no automatic programming retry
    end
```

`tools/flash_demo_mcp.py prepare` performs knowledge retrieval, isolated compilation and
read-only planning. Its `execute` mode requires a separate approved authorization file and
checks that the freshly obtained plan matches the scope exactly. It never creates an operator
grant, silently retries a flash, substitutes another probe, or runs firmware after a failed
programming result. Actual server-side persistent attempt budgets remain authoritative.

The operation scope is intentionally limited to `flash` and `reset_run`; it does not grant
breakpoints, stepping, arbitrary memory access, general debugging, or additional flashing.
The operator authoring procedure is described in [programming/control](hardware-programming.md).

## What to observe after a successful reset/run

Green LD4/PD12 should toggle every nominal 500 ms. Orange LD3/PD13 should follow the USER
button on PA0 after nominal 50 ms debounce, with green continuing. These are expected results
for precise timing; the user confirmed the visible LED/button behavior in this run. Blink and
debounce periods were not measured. Reference-board B1 connectivity requires SB20.
Host timestamps, GPIO latches, image readback and a running-core result do not independently
measure blink/debounce timing or prove optical output. No UART claim is made without its wiring
and separately reviewed firmware workflow.
