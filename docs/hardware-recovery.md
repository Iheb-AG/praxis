# First physical attempt and execution-only recovery

The first authorized MCP flash attempt on 2026-10-10 returned `BACKEND_OPERATION_FAILED`.
The audit run is `ea9c0a4961ff47448ad22ccfb58e933d`. The model stopped without retrying or
resetting/running the firmware. The failed result and consumed attempt remain unchanged.

OpenOCD fell back from block writes because the profile deliberately allocates no target RAM
work area. It then completed the program and dump commands. The fatal error came afterward:
`get_reg -force {pc sp lr xpsr}` requested an unknown register. OpenOCD names this register
`xPSR` with case significant. This is confirmed by its
[ARMv7-M register table](https://github.com/openocd-org/openocd/blob/v0.12.0/src/target/armv7m.c)
and the installed backend's read-only register-cache listing. Both inspection and programming
now share the corrected query and map the result to the existing MCP field `xpsr`.

Because the backend returned nonzero, the original service did not compare its temporary
readback. Its `readback_verified=false` means unverified, not proof that the write failed.
The report's attribution to the working-area fallback was incorrect.

A separate identity-guarded, read-only check on the same probe/MCU confirmed **all 1,164 approved
image bytes** at `0x08000000–0x0800048b`. The expected and actual SHA-256 are both
`b3f5623474ae8194a8cbf1c513b4d6de0020581a0db70f79aa2a1db34a94cb67`.
No reset, halt, run, erase, flash driver, target RAM work area or forced core-register read was
requested by that check. Debug attachment still changes debug-transport state. The execution
state remained `unknown`. That check did not observe boot or physical behavior.

The user subsequently reported a blinking green LED and the orange LED turning on when USER
was pressed. These are positive human observations, consistent with the candidate's intended
behavior and the separate matching readback. They do not establish a successful MCP reset/run
trace or explain when/how execution resumed. Orange turning off after release, continued green
blinking while USER is held were not confirmed by that initial report.

The subsequent execution-only MCP session succeeded: run `10f4f267847849dbaa57b6c14d1ac6db`
verified the approved bytes, performed `reset_run` and reported running after 500 ms. No flash or
halt/resume operation occurred. The user's actual answer confirmed green blinking, orange on
while USER was held and off after release, with continued green blinking. Later inspection
reported state unknown, nominal HSI 16 MHz, LOAD=15999 and enabled GPIOA/GPIOD clocks. The basic
scenario passes by human observation; precise timing/debounce and repetition count remain
unmeasured. At that stage the halted register query and full flash reporting were still unqualified.

The later [physical flash demonstration](flash-demo.md) used a new, explicitly approved scope
and succeeded through programming, exact readback, halted register reporting and reset/run.
The user confirmed both visible LED/button behaviors. The original failed attempt and its
consumed budget remain unchanged. This later success qualifies the corrected register-query
branch for the demonstrated path; it does not retrospectively make the first attempt successful.
See [the execution evidence](hardware-execution-evidence.json).

The register query is covered by strict case-sensitive Tcl fixtures, including the halted branch
and a negative reproduction of the old spelling. Protocol tests also cover execution-only scopes.
These do not replace a successful real forced-register-read/control test.
See [the redacted evidence record](hardware-recovery-evidence.json).

## Operator procedure for the already-written image

Reflashing is unnecessary if the image still matches. The execution tool independently compares
all approved image bytes and checks MCU identity before every control operation. A mismatch stops
the operation. The original authorization expired and its flash attempt remains consumed.

After approving reset/run and up to six controls on the selected board, run the following yourself
from the repository root. This creates a new **execution-only** scope, with zero flash attempts.
Firmware may continue running after the command returns or the 15-minute scope expires.
Do not replace the old scope or delete its audit records.

```bash
.venv/bin/praxis hardware-authorize \
  --plan .praxis-output/hardware-plans/led-button-first-flash.json \
  --output .praxis-output/hardware-execution-authorization.json \
  --audit-root .praxis-output/hardware-audit \
  --operator iheb \
  --board-confirmation 'STM32F407G-DISC1; image readback confirmed; PCB revision and SB20 unconfirmed' \
  --actions reset_run halt resume --lifetime-seconds 900 --max-control-attempts 6

```

Add `--hardware-authorization /absolute/path/to/hardware-execution-authorization.json` to
the build server's client command. Close the previous client instance and restart. Use
[the execution-only MCP scenario](mcp-test-prompts.md#execution-only).
There should be eight build MCP tools, including `control_execution`, with `flash_firmware` absent.
The test records actual LED/button observations and completes the remaining release/hold checks.
Precise 500 ms timing and 50 ms debounce remain unmeasured without instrumentation.
Stop on an error; do not auto-provision another scope.
