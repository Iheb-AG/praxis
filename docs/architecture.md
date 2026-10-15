# Architecture and source format

This document maps source formats to implementation. For the conceptual model and publication
scope, read [system design](system-design.md), [sequence diagrams](sequences.md),
[knowledge and firmware assets](asset-contract.md), and [evaluation](evaluation.md).

[Configurable peripheral discovery](peripheral-discovery.md) adds a complete recognized
CMSIS register-type inventory, explicit peripheral selection/instance mappings, automatic
coverage reports and dependency-closure publication requirements. Schema-2 bundles support
branching HEDG graphs; legacy schema-1 bundles retain their original four-stage validation.

[Per-mode instance scopes](timer-routes.md) let a workflow select separate exact
instances for modes in the same canonical document. Generic validation checks
complete mappings, aggregate unions and each mode's reviewed applicability; all
target pin, clock and register facts remain in versioned source data.

Praxis has an offline compiler and a read-only runtime. No runtime retrieval operation invokes
a compiler, XML parser, network request, model, or vector database. A published bundle is sufficient
to serve knowledge, even after its input source directory is removed.

The separate optional [build service](build-service.md) stages pinned F407 firmware assets and
links/validates images in a rootless container. Its optional [inspection backend](hardware-inspection.md)
runs bounded host OpenOCD reads against an explicitly selected probe. The separately authorized
[programming executor](hardware-programming.md) binds writes/control to one target and checked
artifact, with persistent attempt limits. These operations are outside
the portable three-tool knowledge runtime; the build container has no debug-probe access.

An optional `praxis scrape` acquisition step downloads explicit HTTPS PDF, HTML, or text sources
into immutable evidence archives. It records original bytes, extraction versions, source locators,
requirement candidates and hashes. These archives are outside the served wiki. PDF table fragments
and requirement candidates require review before curating canonical peripheral facts. See
[web ingestion](web-ingestion.md) for acquisition limits and the review workflow.

The opt-in [ingestion MCP](ingestion-mcp.md) exposes this acquisition/compiler pipeline to an
assistant in a separate process. It also snapshots source evidence, returns full extracted
parts and rendered schematic pages, and records explicit editorial review receipts. This is
an authoring boundary: raw source content remains untrusted, and independent review is separate.
Only cataloged acquisition can use HTTPS. Published knowledge retrieval remains offline.

## Source profiles and compiler IR

`sources/<target>/profile.json` is validated by `praxis.models.Profile`. Paths are relative to
the profile directory. Every required input and transitive vendored header must be registered
in `sources`, with an identity, authority, version, license, and origin. The compiler records
SHA-256 hashes and checks that inputs have not changed during compilation.

Registered sources inside web archives must declare their archive in `web_imports`. Compilation
verifies artifact hashes, matching target identity and an explicit review receipt covering the
exact import revision. Acquisition metadata and the receipt become hashed bundle provenance.
Compilation never contacts the original website and does not require the optional PDF/HTML parsers.

The profile points to reviewed peripheral records, a header adapter, a netlist, a package pin
map, canonical aliases, and optional DTS/overlay/include sources. No arbitrary executable or
shell command can be selected by a profile. Header flags are limited to literal `-D` definitions;
include directories must remain inside the source tree.

The peripheral IR contains instances, registers, bit fields, prerequisite edges, source locators,
and a reviewed narrative path. It validates widths, masks, reset-value ranges, field overlap,
duplicate registers, canonical identities, provenance, and editorial review status. `reset: null`
means that a value is not asserted; it does not imply zero. Generated tables identify the supported
register scope rather than pretending to reproduce an entire silicon reference manual.

Register offsets, base macros, and every published bit-field mask are checked against header
declarations or explicit expressions over their position constants. Full-register masks derive
from the independently validated access width. Numeric macro evaluation
accepts integer literals, aliases, addition/subtraction/multiplication, bitwise operations, and
bounded shifts. Casts, calls, division, cycles, and unknown expressions fail explicitly. There is
no `eval()` or fallback guess. Clang preserves reserved structure fields and fixed arrays while
deriving target layouts. Its system include paths come from the ARM compiler; libclang and GCC
versions are recorded. AVR SFR decoding keeps data-memory and I/O addresses distinct.

The checked-in inputs include full pinned ST/Arm headers and the relevant avr-libc subset, with
their upstream licenses. Editorial narratives link to the source manuals without distributing
the PDF manuals. Software licenses and datasheet publication rights remain distinct.

## Topology

KiCad input may be `.kicad_sch` (live `kicad-cli` XML export) or an explicitly pre-exported XML
file. Safe XML parsing forbids entity expansion. The MCU component's value and footprint must
match the profile. Connected MCU pin numbers/names must match its reviewed package pin map.
Duplicate endpoint membership and duplicate net names fail validation.

The adapter also preserves component values, fitted/DNP state, properties, library identities and
pin inventories. Every native subsheet must be registered before export. Qualified local net names
remain qualified. A separately reviewed board model checks LED polarity, resistor/bridge paths,
button pulls and required workflow facts against distinct electrical nets. Board and component
tables are served from Markdown through the existing topology tool; runtime never reads the IR.

PDF-only schematics use an explicitly reviewed, source-located transcription adapter. This does
not claim automated wire/junction interpretation. The STM32F407G-DISC1 E-01 reference is a partial
GPIO subset, with a separate reviewed USART2 connector extension; actual PCB revision and
modifications remain unconfirmed. See [board ingestion](board-ingestion.md).

The sample XML fixtures are hand-authored, not claimed as CLI exports. Their companion KiCad
schematics contain only selected pins and connectivity. A live export comparison is a release
gate; both comparisons and native profile compilation have now been exercised with KiCad 9.0.4.
Missing supply, reset, oscillator, and decoupling details are intentional omissions, not
engineering guidance for constructing a board.

DTS input is preprocessed with GCC, compiled by `dtc`, optionally combined by `fdtoverlay`, and
read through the libfdt shared library. The ctypes binding checks the complete DTB before traversal.
Standard phandle references, inherited status, simple-bus `ranges`, `reg`, clocks, and interrupt
relationships are resolved. Only the synthetic UART pin binding is decoded further. Unsupported
properties remain hexadecimal bytes with an unresolved marker. Unsupported bus address encodings
are rejected rather than interpreted as generic addresses. Dangling references in supported
reference properties fail; arbitrary unknown integers are not presumed to be phandles.

Source authority is fact-specific: CAD for direct connectivity, datasheets for package/AF facts,
headers for declarations, and manuals/errata for semantics. Conflicting reviewed/header values
block publication. Resolving a conflict requires changing the reviewed input and its provenance;
there is no automatic precedence that silently overwrites an inconvenient fact.

The target adapters accept STM32F401RE/LQFP64 and ATmega328P-PU/DIP28 at the reviewed 16 MHz
fixture configurations, plus STM32F407VGT6/LQFP100 at the explicit 8 MHz HSE → 168 MHz PLL profile.
The F407 discovery adapter preserves complete RCC/GPIO/USART/NVIC declaration maps, including
bank counts and strides. Reviewed imports establish operating semantics only for the supported
workflow; other declarations remain explicitly unasserted. See [F407 ingestion](f407-ingestion.md).
Unsupported parts, packages, and clock profiles fail validation.
Adding another target requires extending and testing this adapter scope; changing metadata alone
must not silently select the existing compiler flags or examples for different hardware.

## Publication and runtime

The compiler stages all output in the destination filesystem, validates it, and publishes a new
directory with an atomic rename. Existing valid revisions can be reused only when their manifest
revision matches exactly. Changed sources/tool versions require a new output directory. Raw
inputs and IR never enter the knowledge MCP's retrieved context. The separate authoring MCP
explicitly exposes registered evidence and declaration records for review.

A bundle contains a versioned manifest and registered Markdown documents. The manifest hashes
the target, source registry, extractor versions, file hashes, aliases, and dependency graph into
its revision. This detects internal inconsistency; it is not a digital signature or trust policy.

At startup the server checks document hashes, UTF-8, registered
paths, cross-links, canonical identities, aliases, and the four-stage target HEDG. It then snapshots
the documents. Only registered wiki paths may be read, and resolved symlinks cannot escape the
bundle. Exact topology lookup indexes the published Markdown; it does not use hidden compiler IR.

Each stdio process owns one session and one target. A lock serializes prerequisite checks and
successful-read state changes. Failed calls cannot advance state. Repeated index/document reads
are idempotent. Netlist queries require the index but do not satisfy any peripheral prerequisite.
New processes start empty; there is no shared multi-client state store.

## Expected failures

Tool errors use stable code prefixes: `INVALID_INPUT`, `UNKNOWN_PERIPHERAL`,
`PREREQUISITE_REQUIRED`, `AMBIGUOUS_IDENTITY`, `MISSING_FILE`, `INVALID_ENCODING`,
`INVALID_PATH`, and `INTEGRITY_ERROR`. There is no fixed knowledge-document byte ceiling;
`DOCUMENT_TOO_LARGE` remains available for explicitly bounded nonknowledge inputs.
Compiler errors additionally identify
bad profiles, conflicting declarations, unsupported bindings/expressions, missing tools, and
immutable-output collisions. A valid topology query with no result returns an explicit no-match
string. No success response contains truncated Markdown.

