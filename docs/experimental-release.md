# First experimental STM32 release scope

The active engineering priority is now **full F407 coverage before further family expansion**.
The [full-scope acceptance audit](f407-full-acceptance.md) records the remaining gaps and
checks all existing F407 applications against one combined candidate. Full MCU acceptance
remains open; the published experimental baseline below is narrower.

The first public experimental baseline should center on **STM32F407VGT6, the MB997-E-01
reference bundle and Cortex-M4**, with explicit feature and evidence boundaries. This matches
the available board, reviewed sources and existing build/probe integration. Additional STM32
parts are extension targets, not automatically qualified devices. Included F401/AVR fixtures
retain their illustrative labels; non-ST expansion is deferred while STM32 support grows.

The [current ARM core bundle](../bundles/stm32f407g-disc1-e01-arm-core-v2/wiki/index.md)
includes all prior reviewed F407 extensions plus the new core contracts. It has 41 published
register blocks, 22 reviewed subsets, 32 mode contracts and 20 ready authored workflows out of 33.
Those denominators are intentionally limited; they do not establish an overall MCU completion
percentage or complete implementation of any register block.

## How to describe support publicly

| Area | Current evidence |
| --- | --- |
| Local vectorless retrieval | Implemented, protocol-tested, exact topology, dependency gates, immutable revisions |
| Docker knowledge runtime | Digest-pinned bases and locked runtime dependencies; Linux amd64 real stdio checks passed; no published registry image yet |
| Source ingestion | CMSIS/AVR, structured schematic/DTS adapters, cataloged web acquisition, full evidence and review packets |
| F407 operating knowledge | Scoped GPIO, USART/timer/EXTI, CRC, DMA memory-copy, watchdog, SPI, RNG, clocks, ADC, I2C, DAC, CAN and core contracts |
| ARM core example | SysTick/SCB modeled and isolated ARM build/link/ELF checked; current example unflashed |
| Physical demonstrations | Earlier exact LED/button and UART images with user observations; CAN internal-loopback software telemetry from its own image |
| Wider STM32 support | Real F103/G071/H743 MCU-only declaration bundles and offline batch compilation; reviewed operating/board/firmware support remains target-specific |
| Remaining complex workflows | Timer PWM/capture, richer SPI routing, USB, Ethernet, SDIO, RTC, firmware-controlled flash updates and bootloader handoff remain incomplete or blocked |
| General autonomous debugging | Scoped probe/programming/telemetry tools exist; arbitrary debugging and self-repair are incomplete |

“Experimental” must appear alongside the exact target and these limitations. Register discovery
is not operating support; compile success is not physical success; a physical observation does
not transfer to a different image, board revision or operating mode.

## Reproducible contributor entry points

```bash
uv sync --locked --extra ingest --extra build --extra test --extra web
uv run praxis lint --bundle bundles/stm32f407g-disc1-e01-arm-core-v2
uv run praxis support --bundle bundles/stm32f407g-disc1-e01-arm-core-v2 \
  --catalog examples/capabilities/stm32f407g-disc1-arm-core.json --format markdown
uv run pytest -q
uv run ruff check praxis tests tools server.py compiler.py
uv build --offline --out-dir /tmp/praxis-experimental-dist
uv run python tools/check_distribution.py /tmp/praxis-experimental-dist
```

Serving a prebuilt bundle needs runtime dependencies only. Native ingestion and sandbox tests
need their documented tools and a provisioned rootless image. Required task checks run with
`PRAXIS_REQUIRE_EXTERNAL_TOOLS=1`; install missing dependencies before proceeding. Unexpected
skips fail strict acceptance and never qualify missing coverage as verified.

The distribution checker verifies expected public sources/bundles/docs, rejects private/raw
paths and checks documentation links. Imported PDFs, operator approvals, probe identities,
private logs and build artifacts stay outside the source archive. Third-party header notices
and source provenance remain included. A built archive is a local release candidate, not an
upload or a repository publication.

The current [qualified-v1 gate](PUBLICATION_READINESS.md) still requires native KiCad validation
and independent review of exact bundle/firmware-asset revisions. Those are distinct from labeling
and sharing an explicitly scoped experimental development baseline. No qualified-v1 sign-off
is inferred from this experimental scope.

**Next:** make the provenance catalog scale beyond its current document budget, then expand
timer PWM/capture and SPI board routing with the same source/model/build checks. Follow with
USB/RTC and other requested workflows according to their dependencies. Publish a broad STM32
claim only as far as reviewed target profiles and recorded evidence actually support it.
