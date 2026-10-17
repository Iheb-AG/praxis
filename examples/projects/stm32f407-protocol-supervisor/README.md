# Recording scenario: fault-aware UART protocol supervisor

Use the [ready-to-paste prompt](PROMPT.md) to record an assistant building a substantial
embedded project through Praxis. The demonstration combines clock/startup validation,
GPIO routing, timer interrupts, UART RX/TX interrupts, EXTI button handling, bounded
queues, binary framing, CRC, deadlines, a state machine and readable project reporting.
It uses a known joint workflow rather than combining unrelated peripheral examples and
assuming they work together.

## Equipment and wiring

- STM32F407G-DISC1, ST-LINK USB connection and one passive jumper.
- Reference design MB997-E-01; **the physical board revision remains unconfirmed**.
- With **all board power disconnected**, remove earlier test jumpers. After MCP
  verifies connector labels/orientation, connect **PA2 (P1-14) ↔ PA3 (P1-13)** only.
  Reconnect through ST-LINK USB. No USB-to-UART adapter is needed.
- Verify the USER-button solder-bridge condition returned by the board documentation.

That is the proposed wiring, not a claim about the board's current connections.
Pins and aliases must be reconfirmed through the selected knowledge MCP in the recording.

## Expected project behavior

The board boots paused with a green heartbeat. A debounced USER press starts a binary
UART loopback session. Orange pulses on accepted frames; blue latches after 100
consecutive valid frames. Another press requests pause after the outstanding frame;
the timer and green heartbeat continue. UART errors, malformed traffic, overflow or a
bounded response failure latch red. Removing the jumper for a failure test requires
powering off first; restoring it and rebooting permits a separately checked recovery run.

This is an application-level protocol running over UART, not a fieldbus certification
or an external-device interoperability test. The CRC is implemented in software.

## Recording chapters

| Chapter | Show | Evidence |
| --- | --- | --- |
| Request | Paste the prompt and show the requested behavior | User requirement |
| Knowledge | Index identity, blocked early access, resolved pins and prerequisite route | Actual MCP responses |
| Design | State machine, scheduling, protocol and IRQ responsibilities | Authored explanation with citations |
| Build | Application C/H generation, Podman compilation, ELF validation | Exact artifact ID and checked result |
| Report | Open the formal PDF, electrical sheets, requirements, source references and gaps | Generated project deliverable |
| Physical run | Separately approved flash; start, success latch, pause | Programming evidence, counters and human observation distinguished |
| Failure/recovery | Power-off wire removal/restoration and new runs | Fresh observations; report actual outcomes |

The knowledge/build/report portion can be recorded without touching the board. Physical
chapters require confirmed wiring, an appropriate hardware profile and a fresh approval
for the exact image. Do not reuse historical approvals or label an unrun chapter passed.

## Reproduce the report feature without a model or board

From the repository root, with the pinned rootless Podman image installed:

```bash
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 python tools/check_project_report_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-timer-irq-v1 \
  --assets assets/stm32f407vg \
  --workspace examples/stm32f407g-disc1-uart-loopback \
  --source telemetry_application \
  --artifacts .praxis-output/supervisor-demo/artifacts \
  --lock toolchain-f407.lock.json \
  --reports .praxis-output/supervisor-demo/reports \
  --spec examples/projects/stm32f407-protocol-supervisor/project.json \
  --evidence .praxis-output/supervisor-demo/replay
```

Use fresh output directories for each replay. Open the returned report's `index.html`.
This builds the **existing telemetry example**, not new model-generated firmware.
The report specification binds the exact reference bundle. For a new application,
update the project ID, attachment paths and explanations to match its actual code.

To typeset that generated report with native electrical symbols:

```bash
praxis project-pdf \
  --report .praxis-output/supervisor-demo/reports/f407_protocol_supervisor_v1 \
  --output .praxis-output/supervisor-demo/typeset
```

The result contains `report.pdf`, electrical SVG previews and the multi-part LaTeX
authoring kit. The optional TeX/Poppler dependencies are listed in the reporting guide.

The report feature is [documented separately](../../../docs/project-reporting.md).
