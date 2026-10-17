Build a fault-aware UART protocol supervisor on my STM32F407G-DISC1 using Praxis MCP.
We are recording the complete engineering workflow, including a report about this
firmware project. Do not substitute a Praxis activity log for that deliverable.

Use the knowledge MCP as the hardware authority. Read its index and confirm target
`stm32f407g_disc1_mb997_e01`, reference board MB997-E-01, and the exact bundle revision.
My physical PCB revision is still unconfirmed. Read `get_build_profile` and stop if
its target/revision differs. Follow the actual prerequisite gates; do not use recalled
pinouts, external searches or undocumented register assumptions to fill gaps.

Resolve LED_A, LED_B, BLUE_LED, RED_LED, USER_BUTTON, USART2 TX/RX, PA2, PA3 and their
exact header endpoints through MCP. Explain the USER solder-bridge requirement and
active levels. Retrieve the full clock, GPIO, USART, timer, SYSCFG, EXTI, NVIC and
startup/core dependencies needed for this workflow. A returned declaration alone is
not reviewed operating guidance. Stop and identify any unsupported required facts.

Requested design:

1. Establish a checked nominal 16 MHz HSI clock with bounded readiness waits. Derive
   all bus, timer and UART settings from the retrieved clock route; do not assume
   the optional 168 MHz reference recipe is already running.
2. Use TIM2 for a nominal 1 kHz interrupt timebase. Use USART2 TX/RX interrupts at
   nominal 115200 baud, 8 data bits, no parity, one stop bit. Use EXTI for USER activity
   and nonblocking 50 ms debounce in the main loop. Keep SysTick unused here.
3. Use bounded TX/RX queues and short, justified critical sections. No dynamic allocation,
   polling waits inside handlers, full-frame parsing or CRC computation in an ISR.
   Follow each source's actual pending/error-clear semantics and safe enable order.
4. Implement a 19-byte binary frame: sync A5 5A; version 1; type 1; sequence uint32 little
   endian; payload length 8; eight payload bytes; CRC16 big endian. For byte i of the
   payload use `((seq >> (8 * (i % 4))) ^ (0x31 + 17 * i)) & 0xff`. Calculate software
   CRC-16/CCITT-FALSE over bytes 2 through 16: polynomial 0x1021, initial 0xffff,
   no reflection, no final XOR. Require exact version/type/length/sequence/payload
   agreement as well as CRC. Handle partial and malformed input without unbounded work.
5. Allow one outstanding frame; start frames at least 100 ms apart; bound completion
   to 250 ms. Use rollover-safe timing and sequence arithmetic. Handle overflow,
   UART errors and malformed responses explicitly; do not silently count them as success.
6. Boot paused. A fresh debounced USER press starts a run; another requests pause after
   the current frame completes or reaches its deadline. Holding USER must not retrigger;
   a button held at reset must first be released. A fresh run resets per-run results.
7. Green heartbeat toggles nominally every 500 ms, including while paused or failed.
   Orange pulses for 30 ms per validated frame. Blue latches after 100 consecutive
   valid frames; red latches a detected failure. Explain simultaneous indicators.
8. Use the existing supported UART telemetry ABI if available: coherent counter publication
   no faster than its reviewed probe-safe cadence. Expose state, timer/IRQ progress,
   frame and byte counts, errors and button/run counts. Never invent a new debug-memory
   reader or claim that self-reported counters prove physical signal timing.

The proposed loopback is one passive PA2↔PA3 jumper. Before any physical run, show the
MCP-derived header positions and ask me to confirm that, with all power disconnected,
I removed earlier jumpers and fitted only the proposed wire with orientation checked.
Do not assume the wiring is already present.

Create a fresh application directory under the build MCP's configured workspace. Supply
application `.c`/`.h` files only; use its pinned startup, system/runtime and linker assets.
Provide a short state-machine and interrupt-responsibility explanation before coding.
Run meaningful available protocol/controller/queue tests, build through `build_firmware`,
inspect both compile and ELF outcomes, and call `validate_firmware` on the accepted ID.
Report unavailable checks explicitly. Do not create a fake pass from a Markdown checklist.

Create a `praxis-project-v1` specification using the actual target/revision, source paths,
published workflow IDs and document IDs. Map each requirement to its knowledge scope
and its real verification plan. Author explanations of clock choices, bus gates, routing,
register side effects, interrupt priorities, concurrency, protocol validation, deadlines,
memory/startup and failure behavior. Cite the returned documents and state limitations.
Include a structured sequence diagram in `diagrams` with named participants and messages
showing IRQ-to-main-loop work transfer and status publication. Cite its source documents
and label it as intended design rather than a measured execution trace.
Pass it to `generate_project_report` with the accepted artifact ID. The operator must
have enabled `--project-reports` on the build MCP; if absent, report that missing option
instead of pretending a report was generated. Return the actual output path.

The report must contain white, formal, readable HTML, Markdown, a connectivity SVG showing all selected
net endpoints and the proposed jumper, source references, source-file attachments and
separate knowledge/build/physical statuses. Keep component nets separate and call this
a connectivity rendering rather than a full reconstructed CAD schematic. Do not claim
physical acceptance, or that arbitrary attachments produced the artifact, without evidence.
Use the generated LaTeX authoring kit for the formal deliverable: separate requirements,
design, electrical, verification and traceability parts. Where the optional document
toolchain is installed, run `praxis project-pdf` on the returned report into a new output
directory. Review the actual PDF and CircuitikZ electrical sheets. Stop and report any
missing typesetting dependency instead of treating an HTML printout as native LaTeX output.
Use plain document-control text for review status; avoid colored warning cards.

Stop after build/report review and present the exact read-only flash plan when hardware
inspection is configured. Request fresh exact-image approval before erasing, flashing or
resetting/running the board. Earlier approvals do not cover this image.

For a later approved physical recording, propose these chapters: boot-paused heartbeat;
USER start; at least 100 valid frames and blue latch; USER pause with frame counters
stopped and timer still advancing; a power-off jumper-removal failure test; and a
power-off jumper-restoration fresh-boot recovery. Record actual results separately from
expectations, including any unexpected timeout or extra start. Explain that an open RX
can fail through a UART error before its deadline. Always finish with what is verified,
what remains untested, and the next step.
