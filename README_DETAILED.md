# Project Praxis

**Docker knowledge server:** build with `docker build -t project-praxis:0.1.0 .`, then let
your MCP client launch the container with one published bundle mounted read-only. No host
Python or ingestion toolchain is required for retrieval. See [Docker setup and client
configurations](docs/docker.md). The optional build and hardware services retain their separate
Linux/Podman and probe requirements.

Praxis aims to let a coding model use an evaluation board as a tool: retrieve hardware knowledge,
generate firmware, build, flash, execute, debug and repair from observed results. The current
implementation supplies knowledge retrieval, isolated F407 building and ELF validation, and
optional ST-LINK inspection, and target-bound programming/execution tools gated by local operator
authorization. One approved LED/button flash/readback/reset-run path is now demonstrated on
the physical board, with user-confirmed visible behavior; see [the actual flash demonstration](docs/flash-demo.md).
A separately approved [UART/timer/EXTI scenario](docs/reports/uart-loopback-results.md)
also passed MCP flash/readback/reset-run, with user-confirmed loopback, pause, jumper-removed failure and restored-jumper recovery behavior.
Broader hardware qualification and test adapters remain open in [the hardware tool contract](docs/hardware-verification.md).

Praxis compiles local hardware sources into target-specific Markdown bundles and serves them
through three read-only FastMCP tools. It uses no embeddings, vector database, model calls, or
network calls during retrieval. The included STM32F401RE, STM32F407VGT6 and ATmega328P boards are **illustrative partial
connectivity fixtures**, not manufactured or electrically certified reference designs.

The compiler produces evidence; the MCP server retrieves it; the coding assistant generates
firmware in its own workspace. The separate F407 build service supplies pinned startup, system,
runtime and linker assets internally. Local retrieval does not imply a local coding model.

The optional [ingestion MCP](docs/ingestion-mcp.md) now exposes cataloged acquisition,
offline evidence search, complete source pages/tables, schematic images, declaration discovery
and reviewed immutable publication. Its new review-preparation tool checks manual candidates
against header declarations and reports conflicts and gaps. The same offline stage is available
as `praxis prepare-review`; see [the compiler workflow and sequence](docs/manual-review-compiler.md).
It is separate from the three-tool knowledge server.
The [UART/timer/interrupt example](examples/stm32f407g-disc1-uart-loopback/README.md) uses a new
source-backed bundle and matching knowledge/build configuration; existing default launchers
still select their prior bundle. Physical test status is recorded separately from compilation.

Start with the [documentation guide](docs/README.md), [system design and theoretical basis](docs/system-design.md),
[sequence diagrams](docs/sequences.md), [knowledge and asset contract](docs/asset-contract.md), and
[evaluation methodology](docs/evaluation.md). These distinguish implemented behavior, recorded
evidence and proposed extensions for publication.

Current release label: **experimental development alpha**, with qualified v1 approval pending.
See [publication readiness and remaining work](docs/PUBLICATION_READINESS.md). The optional
[firmware telemetry extension](docs/firmware-telemetry.md) adds artifact-bound UART/timer counters
through the build/hardware MCP; general autonomous debugging remains incomplete.

## Configurable MCU coverage

The [STM32/ARM core extension](docs/arm-core-support.md) now adds reviewed SysTick timing,
fixed Flash vector selection and system-exception priority/pending controls to the F407 baseline:
**22 reviewed subsets, 32 mode contracts and 20 ready authored workflows out of 33**. Actual MCP
retrieval, isolated linking and ELF revalidation pass; the new example is unflashed. The initial
local polling contract was corrected in a separate immutable revision. See the
[first experimental release scope](docs/experimental-release.md) and
[matching example](examples/stm32f407g-disc1-arm-core/README.md).

[Reusable Cortex-M target adapters](docs/target-adapters.md) now separate extraction CPU,
header identity and macro conventions from STM32-specific knowledge. A fictional Cortex-M3
bundle demonstrates another family using the same compiler and three-tool MCP. It supplies
declarations only and cannot inherit F407 firmware or flashing support. This does not establish
support for an NXP board or automatically extract all operating semantics from PDFs.

The [CAN RX follow-up](docs/can-rx-followup.md) adds an explicit, source-backed
GPIO prerequisite to a new immutable candidate bundle: **20 reviewed subsets,
26 mode contracts and 16 ready authored workflows out of 29**. The full regression
passed 772 tests with 4 KiCad skips. Actual MCP ingestion reproduced 49 byte-identical
files; an 18-call retrieval/build replay passed isolated linking and ELF checks.
Read-only hardware MCP prepared the 4,920-byte image plan and rejected the older
installed image before telemetry reads. A subsequent approved single flash/reset-run
and two fresh observation windows passed scoped internal-loopback qualification;
see [physical results](docs/reports/can-rx-results.md). External CAN, repeatability
and complete MCU support remain unestablished. See its
[exact evidence](docs/can-rx-evidence.json) and
[portable configuration](examples/opencode.can-rx.example.json).

The [CAN observation extension](docs/can-telemetry.md) adds an explicit, artifact-bound
software ABI and offline result qualification for the internal-loopback image.
It checks actual ISR-saved FIFO words, completion/errors, cleanup and publication
freshness. This strengthens Milestone 4 without expanding the published MCU modes.
Its first approved physical flash/readback/reset-run passed, but the CAN application
reported an initialization timeout. [The failed result and diagnosis](docs/reports/can-loopback-results.md)
are preserved; physical CAN qualification remains open.

The [CAN extension](docs/can-expansion.md) adds CAN1 silent internal loopback,
FIFO0 interrupt delivery and clock/NVIC dependencies through explicit compiler
profiles. Its bundle has **20 reviewed subsets and 24 mode contracts**, with
15 ready authored workflows out of28. Actual MCP retrieval, isolated ARM linking
and artifact validation pass. The model requires both ISR receipt and complete
transmit status; the ELF binds IRQ20 to the real handler. External CAN operation
and physical qualification remain open. See the [example and prompt](examples/stm32f407g-disc1-can/README.md)
and [matching configuration](examples/opencode.can.example.json).

The [DAC expansion](docs/dac-expansion.md) adds channel1 software triggering,
digital completion and its clock/reset contract through the generic compiler.
Its bundle has **19 reviewed subsets and 20 mode contracts**, with 13 ready authored
workflows out of 25. Actual MCP retrieval, rootless ARM build/link and artifact
revalidation pass. The transfer entry is retained in the linked image, while
main leaves analog outputs disabled. Board DAC wiring, voltage accuracy and
broader modes remain unqualified. See the [example and MCP prompt](examples/stm32f407g-disc1-dac/README.md)
and [matching configuration](examples/opencode.dac.example.json).

The [I²C compiler expansion](docs/i2c-expansion.md) adds a scoped I2C1 controller
transmitter, parent-state binding for successive extensions and compact complete
provenance. Its bundle has **18 reviewed subsets and 18 mode contracts**, with
12 ready authored workflows out of 23. Actual MCP retrieval, isolated ARM build
and artifact validation passed; wiring, receive modes and physical I²C remain
unsupported. Use the [matching configuration](examples/opencode.i2c.example.json)
and [configuration-only example](examples/stm32f407g-disc1-i2c/README.md).

The [ADC workflow expansion](docs/adc-expansion.md) adds ADC1 internal-reference
sampling and TIM2 polling settling, with no external wiring. It also adds
dependency-driven review packets and modular reviewed definition extensions.
The new bundle has **17 reviewed subsets and 16 mode contracts**. Real MCP
retrieval and host ordering/failure models pass. After restoring rootless Podman
and its locked image, the ADC example also passed actual MCP compilation, linking,
ELF validation and artifact revalidation. [Build evidence](docs/adc-build-evidence.json)
preserves the distinction from the initial missing-Podman attempt. No new firmware was flashed.
Use the [matching configuration](examples/opencode.adc.example.json) and
[example/test prompt](examples/stm32f407g-disc1-adc/README.md).

Use the [scoped support report](docs/capability-support.md) before selecting a firmware scenario.
It reports separate declaration/review/mode percentages and exact workflow blockers, with no
claim of overall MCU completion. The optional catalog tracks planned boot/update work as well
as authored peripheral workflows. Contributors can start with [CONTRIBUTING.md](CONTRIBUTING.md).

```bash
.venv/bin/praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --catalog examples/capabilities/stm32f407g-disc1.json --format markdown
.venv/bin/praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --workflow uart_timer_interrupts
```

The [clock-mode extension](docs/clock-modes.md) adds reviewed F407 FLASH latency/PWR Scale 1
contracts and reusable instance-scoped mode dependencies. The new bundle has **15 reviewed
subsets and 12 mode contracts**; its declared PLL/RNG clock workflows pass publication gates.
FLASH programming and unsupported modes remain blocked. A clock example passed actual MCP
sandbox linking/ELF checks and shared-callback model tests; it has not been flashed.

```bash
.venv/bin/praxis features --bundle bundles/stm32f407g-disc1-e01-clock-v1
.venv/bin/praxis serve --bundle bundles/stm32f407g-disc1-e01-clock-v1
```

Use the matching [optional OpenCode configuration](examples/opencode.clock.example.json).
The feature bundle below remains an earlier immutable baseline.

The [mode-scoped feature expansion](docs/peripheral-modes.md) now publishes **13 reviewed
subsets**, seven explicit operating-mode contracts and a target-wide support inventory.
CRC, DMA, SPI, RNG and IWDG gained reviewed guidance; missing board wiring and clock prerequisites
remain visible blockers. Complete MCU support is still unfinished. Milestone 4 now includes an
offline phase qualifier that preserves failed telemetry windows. A new CRC/DMA example passed
actual MCP sandbox compilation/linking and ELF validation, without flashing the board.

```bash
.venv/bin/praxis features --bundle bundles/stm32f407g-disc1-e01-features-v1
.venv/bin/praxis serve --bundle bundles/stm32f407g-disc1-e01-features-v1
```

Use the matching [optional OpenCode example](examples/opencode.features.example.json) for this
bundle. Existing client launchers retain their prior selection. The following discovery bundle
is retained as an earlier immutable baseline.

The [new discovery profile](sources/stm32f407g-disc1/profile-discovery.json) inventories CMSIS
register types and publishes a schema-2 bundle with branching dependencies and automatic
coverage/readiness reporting. The [expanded F407 index](bundles/stm32f407g-disc1-e01-discovery-v2/wiki/index.md)
contains 41 published register blocks, including TIM, EXTI, SYSCFG, SPI, I²C, CAN, ADC, DMA and USB.
Four documents retain reviewed operating subsets; other declarations require operating review.
See [configuration, coverage limits and sequence diagrams](docs/peripheral-discovery.md).

```bash
.venv/bin/praxis coverage --profile sources/stm32f407g-disc1/profile-discovery.json
.venv/bin/praxis serve --bundle bundles/stm32f407g-disc1-e01-discovery-v2
```

Existing OpenCode/build launchers retain the earlier reference bundle. Select the new bundle
explicitly for discovery testing; bundle-bound hardware profiles and authorizations need their
own validation. The three retrieval tool signatures are unchanged.

## Install and reproduce

Python 3.11+ is required. From this repository:

```bash
uv sync --extra ingest --extra test --extra web
uv run praxis compile --profile sources/stm32f401re/profile.json --output bundles/stm32f401re
uv run praxis compile --profile sources/atmega328p/profile.json --output bundles/atmega328p
uv run praxis lint --bundle bundles/stm32f401re
uv run praxis lint --bundle bundles/atmega328p
uv run pytest
```

Ingestion additionally needs Clang, `arm-none-eabi-gcc`, `avr-gcc`, `gcc`, `dtc`, and the
libfdt shared library. DTS overlays need `fdtoverlay`. Live `.kicad_sch` ingestion requires
`kicad-cli`. Python ingestion dependencies are optional; serving already published bundles
does not import Clang, XML parsers, libfdt, or any compiler.

The default fixture profiles use explicitly labeled, pre-exported KiCad XML inputs so they
remain reproducible without KiCad installed. Source-backed editorial imports, full pinned
ST/Arm headers, and an avr-libc target subset accompany the profiles. The same source hashes
pin approved compiler inputs; see [verification](docs/verification.md) and [release status](docs/STATUS.md).

Bundles are immutable. Rebuilding identical sources with identical extractor versions is
idempotent. Changed inputs require a new output directory; failed builds preserve old revisions.
Hashes establish internal integrity and reproducibility, not publisher authenticity.

## STM32F407VGT6 compiler

The F407 profile automatically discovers complete RCC/GPIO/USART/NVIC declaration maps and
enriches them with reviewed UART operating semantics. Its explicit example clock plan is
HSE8 → SYSCLK/HCLK168, PCLK1=42 MHz and PCLK2=84 MHz. The XML netlist is illustrative;
replace it with your board export before using its wiring as hardware evidence.

```bash
.venv/bin/python compiler.py --profile sources/stm32f407vgt6/profile.json --output bundles/stm32f407vgt6
.venv/bin/praxis lint --bundle bundles/stm32f407vgt6
.venv/bin/praxis serve --bundle bundles/stm32f407vgt6
```

See [F407 ingestion, adapter contracts, and limitations](docs/f407-ingestion.md). Missing reset
values or operating semantics remain explicitly unasserted; headers are not a replacement for
reviewed manuals. Changed source inputs require a new output revision directory.

## STM32F407G-DISC1 board knowledge

The separate MB997 E-01 reference bundle includes reviewed LED/button connections, active levels,
external pull configuration, component values and clock/timing facts from ST's board documents.
It does not assume that your physical card matches that revision or its solder bridge settings.

```bash
.venv/bin/praxis compile --profile sources/stm32f407g-disc1/profile.json --output bundles/stm32f407g-disc1-e01-m1
.venv/bin/praxis lint --bundle bundles/stm32f407g-disc1-e01-m1
```

Select the absolute `bundles/stm32f407g-disc1-e01-m1` path in your MCP client; `temp/opencode.json`
already selects it. Reconnect the server and query `LED_A`, `LED_B`, and `USER_BUTTON` after reading
the index. See [board ingestion](docs/board-ingestion.md) and the [Milestone 1 gate](docs/milestone1.md).

## Optional web scraping

Download and extract the official F407 datasheet, reference manual and errata into local evidence
archives. The optional `web` extra supplies HTML/PDF parsers.

```bash
.venv/bin/praxis scrape --catalog sources/stm32f407vgt6/web-sources.json --output imports/f407
```

Archives contain original files, extracted text/tables, requirement candidates and source hashes.
They remain pending review; the compiler checks review receipts before using imported evidence.
MCP retrieval stays offline. See [web import options and review workflow](docs/web-ingestion.md).

## MCP configuration

Replace all example paths with absolute paths. Install dependencies before starting the client;
runtime launch must not download anything. `server.py` requires an explicit bundle.

Claude Desktop (`claude_desktop_config.json`) and Cursor (`.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "project-praxis": {
      "command": "/absolute/path/Praxis_Bundle/.venv/bin/python",
      "args": ["/absolute/path/Praxis_Bundle/server.py", "--bundle", "/absolute/path/Praxis_Bundle/bundles/stm32f401re"]
    }
  }
}
```

VS Code (`.vscode/mcp.json`) uses a different top-level key:

```json
{
  "servers": {
    "project-praxis": {
      "type": "stdio",
      "command": "/absolute/path/Praxis_Bundle/.venv/bin/praxis",
      "args": ["serve", "--bundle", "/absolute/path/Praxis_Bundle/bundles/stm32f401re"]
    }
  }
}
```

For other MCP clients register the same executable/arguments with their stdio configuration
interface. On Windows use `.venv\\Scripts\\python.exe`. Run a separate process for the AVR
bundle. The server resolves knowledge relative to the selected bundle, not the client's cwd.
For F407 retrieval, use the absolute `bundles/stm32f407vgt6` path for `--bundle` in the same
client launch configuration.

## Tools and HEDG

| Tool | Behavior |
| --- | --- |
| `read_wiki_index()` | Complete target identity, assumptions, and execution roadmap |
| `read_peripheral_doc(peripheral_name)` | Complete canonical document after prerequisite retrieval |
| `query_schematic_netlist(query_target)` | Exact net/pin/endpoint lookup with every net endpoint |

STM32 route: index → RCC → GPIO → USART → NVIC. AVR route: index → clock → GPIO → USART →
interrupts. Read the index before topology queries. Querying a net does not advance HEDG state.
`usart2` is a declared STM32 alias; `usart0` is an AVR alias. Paths and extensions are rejected.
Net names are case-sensitive; MCU pin names are case-insensitive. `PA2` never matches `PA20`.
Ambiguous aliases return candidates. Nets remain separate across components.

Successful reads advance process-local state. Repeated reads are idempotent; restarting resets
the session. The process snapshots and verifies all registered Markdown at startup. Editing
files afterward cannot alter the active session. Logs use stderr, stdout is reserved for MCP.

HEDG gates prove document retrieval, **not generated code order or hardware correctness**.
Use the [agent instructions](docs/AGENT_INSTRUCTIONS.md) in the assistant's instruction system;
MCP prompts alone are not guaranteed to be automatically adopted by every client.

## Compilation and release

The separate `praxis verify` command uses a rootless, network-disabled Podman sandbox and fixed
target compiler profiles. It never runs project build scripts or flashes hardware. Missing
Podman or an unprovisioned image lock is a hard error; there is no native fallback. See
[sandbox setup and verification limits](docs/verification.md).

The optional [F407 build MCP](docs/build-service.md) now supplies pinned startup/system/linker
assets, performs isolated full linking, checks the main-SRAM stack and interrupt vectors, and
returns a content-addressed artifact ID. The original knowledge MCP remains read-only.
The [portable OpenCode configuration](examples/opencode.example.json) includes both servers;
replace its absolute paths, restart the client, and use
the [build validation scenario](docs/mcp-test-prompts.md#build-and-validate). Direct protocol tests do not
require OpenCode. No build tool flashes or runs the board.

The build MCP optionally exposes `list_debug_probes`, `inspect_target`, and `inspect_execution`
when launched with a reviewed, hash-pinned OpenOCD profile. Add the profile explicitly and restart
the client to discover these tools. See [read-only hardware inspection](docs/hardware-inspection.md)
and [the inspection scenario](docs/mcp-test-prompts.md#read-only-inspection). Knowledge and build remain
separate servers; the optional ingestion server is an additional authoring service.
Inspection does not flash, reset or halt the board. The separate opt-in
[programming/control contract](docs/hardware-programming.md) adds a read-only flash plan and
mutating tools only for actions in an operator-supplied authorization file. The default
hardware-enabled configuration exposes seven build/inspection/planning tools, with programming disabled.
Broader programming qualification and measured physical tests remain open in [the hardware verification loop](docs/hardware-verification.md).
The first authorized attempt wrote the approved image but failed during final register reporting;
separate readback confirmed the image. Execution-only MCP reset/run and the human LED/button
check subsequently passed. See [execution evidence](docs/hardware-execution-evidence.json)
and [recovery analysis](docs/hardware-recovery.md).

A later explicitly approved [physical flash demonstration](docs/flash-demo.md) completed one
sector-0 erase/program, exact 1,164-byte readback, successful halted register reporting and
reset/run. The user confirmed green blinking and orange following USER. Standalone halt/resume,
precise timing and broader peripheral hardware tests remain unqualified.

The runtime dependencies intentionally pin the official MCP SDK below v2 to retain its
FastMCP API. Dependency versions are recorded in `uv.lock`. See the
[architecture and source format](docs/architecture.md), [test scenarios](tests), and
[milestone evidence](docs/STATUS.md) before treating this implementation as a release candidate.


## Hardware-independent reference acquisition

For sensors, displays, modules or other hardware outside the selected MCU bundle,
use the optional [hardware reference MCP](docs/hardware-references.md). It accepts
explicit public documentation URLs without a predefined catalog, preserving source
hashes and complete extracted parts. It does not establish firmware or electrical support.
