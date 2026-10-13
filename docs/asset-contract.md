# Knowledge and firmware assets

## What the MCP provides today

The intended division is straightforward: Praxis supplies supported hardware evidence and
prerequisite routing; the assistant uses that evidence to create firmware. The current server
returns Markdown through three tools. It does not generate files in the firmware workspace.

The complete product intention also includes a model-driven build/flash/debug/repair loop, with
Praxis bridging to the evaluation board. That executor is specified separately in
[the hardware tool contract](hardware-verification.md); it is not part of today's three tools.
The separate [F407 build MCP](build-service.md) now implements the build/link/image-validation
part of that bridge. It stages assets inside the sandbox rather than returning raw asset files
through the knowledge tools. The same optional server now supplies [read-only target inspection](hardware-inspection.md).
Target-bound programming/control are separately implemented with operator authorization in
[the programming contract](hardware-programming.md); physical integration remains unperformed.

In this document, **knowledge** means facts and operating conditions. **Firmware assets** means
reusable build inputs such as headers, startup assembly, linker scripts and system initialization
sources. They are related but have different delivery and verification requirements.

| Material | Present today | Available through the three MCP tools? |
| --- | --- | --- |
| Target, reference revision, clock assumptions and HEDG | Published index | Yes, index tool |
| Register layouts, fields and reviewed operating requirements | Canonical peripheral Markdown | Yes, peripheral tool |
| Board LED/button mappings, polarity, pulls and components | Discovery reference GPIO subset | Yes, topology queries and returned context |
| Raw vendor headers | Registered compiler inputs in the repository | No raw-file retrieval tool |
| Device Tree relationships | Compiled Markdown when configured | No generic topology-document read tool |
| Source origins, hashes and locators | Manifest and published provenance | Locators/context returned; no generic provenance-file read tool |
| Startup assembly and complete vector tables | Hash-pinned F407 build profile asset | No; supplied by separate build MCP |
| Linker scripts and memory maps | Hash-pinned F407 build profile; static checks, independent review pending | No; supplied by separate build MCP |
| Complete clock/system initialization implementation | Recipe and reviewed facts, not a supplied firmware module | No |
| Makefiles, flashing scripts and complete firmware templates | Not supplied by retrieval | No |

The server currently registers MCP tools, not firmware-download resources. The MCP protocol
offers multiple primitives; their existence in the protocol does not imply that Praxis exposes
them. See the [official SDK v1 documentation](https://github.com/modelcontextprotocol/python-sdk/tree/v1.x).

An assistant with filesystem access may independently find headers or assets in its workspace.
That is a host capability and must not be reported as an MCP asset response. A vendor URL in
provenance is a citation, not a downloaded, verified asset.

## Why startup and linking need their own evidence

A pin mapping can justify GPIO selection; it cannot establish vector-table completeness,
RAM-bank placement, boot mode, linker memory regions or runtime library initialization. A
supported clock recipe does not establish the current SystemCoreClock value. Compile success
alone also does not demonstrate that an image boots from the selected memory location.

If a model creates startup assembly, a linker script and a Makefile, it has expanded the firmware
work beyond the current served asset scope. That can be useful work, but the report should identify
where those definitions came from and what was checked. Their correctness must not be attributed
to the LED/button retrieval test.

For the current Discovery scenario, use either an existing target-matched firmware project or
separately verified vendor assets. Without those, source snippets can be labeled as integration
source. Producing a full image is a separate task with additional evidence requirements.

## A complete application workflow

1. Select a bundle and confirm the returned identity before using any pin or register fact.
2. Retrieve board signals and the applicable HEDG prefix.
3. Identify required build assets and their sources in the firmware project.
4. Map each implementation decision to evidence or an explicit application design choice.
5. Generate source without silently filling unresolved hardware facts.
6. Check syntax, object compilation and linking as distinct stages when available.
7. Record static configuration checks separately from physical tests.

Debounce intervals and blink periods can be application choices. MCU memory sizes, clock sources,
pin identities, access side effects and interrupt-vector definitions require target evidence.
Neither a model's familiarity with a board nor a passing tool call supplies missing evidence.

## Implemented asset staging and future delivery

F407 firmware assets are implemented as a separate versioned, hash-registered profile. The build
service verifies and stages them automatically. The registry includes applicability, upstream
origins, licenses and review limits. Raw-file asset delivery through retrieval remains a proposal;
the following contract describes that possible extension.

A future target bundle could register approved firmware assets with:

| Field | Purpose |
| --- | --- |
| Canonical asset ID and kind | Stable identity: header, startup, linker, system source or template |
| MCU, package, core and toolchain applicability | Prevent cross-target or ABI reuse |
| Board and memory-layout assumptions | Distinguish a reference setup from physical configuration |
| Upstream URL, version, license and source hash | Reproduce acquisition and preserve redistribution terms |
| Published asset hash and bundle revision | Verify the delivered bytes |
| Dependencies and compile settings | Make required companion files explicit |
| Review state and validation results | Distinguish source acquisition from qualified use |

Binary/text assets should have their own bounded file policy; the existing Markdown document
limit should not be silently repurposed. Runtime exposure could use explicitly registered MCP
resources or narrowly scoped asset tools. That choice needs a versioned contract and client
interoperability tests. Arbitrary paths and online fetches should remain outside retrieval.

The host would request an exact asset ID, verify its identity/hash, place the returned content in
the firmware workspace, and compile it with the reviewed toolchain. Delivery should never imply
permission to execute bundled scripts. Generated application code and immutable upstream assets
should remain distinguishable in reports.

Acceptance would require negative target/ABI tests, hash/path tests, license/provenance checks,
real-client asset retrieval, actual full linking against each asset set, and separate startup
qualification. Current automatic staging covers one F407 C11 flash profile; it is not a universal
firmware project generator or independent startup qualification.

## Adding another board today

For an already supported MCU/package/clock profile, reuse reviewed silicon knowledge and provide
new board connectivity, component roles, aliases, applicability and workflow-required facts.
Compile a separate immutable bundle and test positive and negative identities. Do not relabel an
existing board bundle or silently assume its LED and oscillator connections.

A new MCU, package or clock profile additionally requires adapter/profile support and tests.
Current validated target combinations are limited to STM32F401RE/LQFP64, STM32F407VGT6/LQFP100
and ATmega328P-PU/DIP28 with their supported clock configurations. Complex transistor/expander
circuits need additional board semantics support. PDF sources still require reviewed wiring
transcription. Detailed commands are in [board ingestion](board-ingestion.md).
