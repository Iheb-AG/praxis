# Changelog

## Unreleased — experimental alpha

First public release candidate, centered on STM32F407VGT6 / Cortex-M4 and the
STM32F407G-DISC1 MB997-E-01 reference bundle. No public release or image upload is implied.

### Included

- Deterministic offline compilation into validated, source-backed Markdown bundles.
- Vectorless, read-only MCP retrieval with exact topology lookup, target isolation and
  prerequisite-document gates.
- A Docker knowledge runtime, OpenCode / Claude Desktop configurations, and real stdio checks.
- Reviewed F407 operating subsets, Cortex-M4 core contracts and scoped coverage reporting.
- Optional Linux/Podman compilation, pinned firmware assets and ELF validation.
- Opt-in ST-LINK programming/control and artifact-bound telemetry for supported examples.
- Contribution guides, examples, evidence reports and publication checks.

### Validation and boundaries

Recorded evidence includes 861 passing software tests with four native KiCad skips, plus
110 Docker MCP calls across three sessions and 50 passing native routing/protocol checks.
Earlier physical LED/button, UART and scoped CAN demonstrations have separate evidence;
the latest ARM-core example is unflashed.

This is not complete STM32/ARM support or qualified production firmware tooling. Docker
verification currently covers Linux amd64 knowledge retrieval. Independent review, clean
hosted-CI evidence, broader operating modes and hardware qualification remain open.

See [experimental scope](docs/experimental-release.md), [status](docs/STATUS.md),
[Docker evidence](docs/docker-evidence.json) and [launch preparation](docs/alpha-launch.md).
