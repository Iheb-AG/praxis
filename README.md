![PRAXIS — hardware knowledge for AI-assisted embedded development](docs/images/praxis-banner.jpg)

# Project Praxis

**From hardware references to AI-assisted firmware development.**

[![Status: experimental alpha](https://img.shields.io/badge/status-experimental_alpha-8b5cf6)](docs/experimental-release.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11%2B-3776ab)](pyproject.toml)
[![MCP: stdio](https://img.shields.io/badge/MCP-stdio-22c55e)](docs/docker.md)

[Quick start](#quick-start) · [Documentation](docs/README.md) · [Examples](#examples) · [Contribute](CONTRIBUTING.md) · [Roadmap](docs/experimental-release.md)

Praxis gives coding assistants source-backed hardware context through the Model Context
Protocol. It compiles engineering sources into indexed Markdown bundles, retrieves complete
register tables and board connections, and checks documentation dependencies before peripheral
bring-up. **Local, vectorless retrieval: no embeddings or vector database.**

**Experimental alpha · reviewed F407 workflows plus STM32F1/G0/H7 inventories.** Useful for supported prototypes,
experiments and contributions. Universal MCU support and production qualification remain open.

## Why Praxis?

- **Hardware context with provenance:** canonical peripheral documents, exact pin/net lookup,
  and explicit source references.
- **Dependency-aware retrieval:** clocks, pins, peripheral control and interrupts follow the
  selected bundle's Hardware Execution Dependency Graph (HEDG).
- **Portable knowledge MCP:** three read-only tools, Docker packaging, and OpenCode / Claude
  Desktop configuration examples.
- **A path to the board:** optional F407 sandbox builds, ELF checks, approved ST-LINK flashing
  and scoped telemetry.

## How it works

```mermaid
flowchart LR
    A[Headers, reviewed manuals, netlists and DTS] --> B[Offline compiler]
    B --> C[Validated Markdown bundle]
    C --> D[Read-only MCP]
    D --> E[Coding assistant]
    E --> F[Optional isolated build]
    F --> G[Approved board execution and observation]
```

The assistant generates the firmware. Praxis supplies knowledge and scoped verification tools.
Imported documents require review; reading them and compiling code do not prove hardware correctness.

## Quick start

**Requirements:** Docker with Linux containers, a source checkout, and an MCP client.
No board or host Python installation is needed for knowledge retrieval.

1. Build the knowledge image from the repository root:

   ```bash
   docker build -t project-praxis:0.1.0 .
   ```

2. Copy the [OpenCode](examples/opencode.docker.example.json) or
   [Claude Desktop](examples/claude-desktop.docker.example.json) configuration into your client.
   Replace the Docker executable and bundle placeholders with absolute paths. Select
   `bundles/stm32f407g-disc1-e01-timer-irq-v1` for the selected public F407 baseline.
3. Restart the client and try:

   > Use Project Praxis to read the wiki index and confirm the target and board reference.
   > Query LED_A and USER_BUTTON, then retrieve their required peripheral documents.
   > Explain the connections and list any missing facts. Do not flash hardware.

The client launches Docker over stdio; no HTTP port or manually started server is needed.
See [Docker setup](docs/docker.md) for launch commands and permissions, or the
[detailed guide](README_DETAILED.md) for native installation and ingestion.

## Alpha scope and evidence

The primary reference board is **STM32F407G-DISC1, MB997-E-01**, using STM32F407VGT6.
See the **[current supported baseline](docs/CURRENT_STATUS.md)** for generated coverage,
revision-bound software and retrieval evidence, historical physical observations,
and independent-review status. Its [registry](current-status.json) pins the selected
bundle and evidence hashes. Recorded test results do not certify the current checkout;
reviewed operating subsets do not imply complete MCU coverage.

For an initialized project, run `praxis project-check --root /path/to/project --live`
to check configuration and fresh MCP service connections before starting work.
This does not build firmware, access hardware or inspect an existing chat session.

Experimental [F103, G071 and H743 bundles](docs/stm32-family-expansion.md) add source-backed
register declarations through a reusable offline target matrix; their operating workflows,
board wiring and firmware support remain unreviewed. F401/AVR and synthetic inputs are labeled
fixtures. USB, Ethernet, SDIO, bootloader handoff and several peripheral modes remain incomplete.
The Docker image packages retrieval; ingestion, Linux/Podman builds and USB access require
separate setup. No registry image has been published yet. See [release scope](docs/experimental-release.md),
[historical test evidence](docs/STATUS.md) and [reliability work](docs/reliability-plan.md).

## Examples

- [LED blink and USER button](examples/stm32f407g-disc1-led-button/README.md)
- [UART loopback, timer and interrupts](examples/stm32f407g-disc1-uart-loopback/README.md)
- [CAN internal loopback](examples/stm32f407g-disc1-can/README.md)
- [Cortex-M4 / SysTick contracts](examples/stm32f407g-disc1-arm-core/README.md)

## Contributing and roadmap

Help add reviewed peripheral modes, exact board mappings, reproducible tests, or clearer docs.
Hardware is optional for source and software contributions. Start with
[CONTRIBUTING.md](CONTRIBUTING.md); use the repository's issue and pull-request templates.

Current priorities are reproducible project setup, service diagnostics, evidence-backed
support reporting and independent qualification. See the [stabilization plan](docs/reliability-plan.md),
[architecture](docs/system-design.md) and [sequence diagrams](docs/sequences.md).

## License

Praxis is [MIT licensed](LICENSE). Third-party headers, firmware assets and source-derived
material retain their respective notices; see the [detailed guide](README_DETAILED.md).

