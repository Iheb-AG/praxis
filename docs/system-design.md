# Project Praxis: system design and theoretical basis

## Problem and scope

Embedded code generation needs several kinds of evidence at once: register declarations,
operating semantics, package pin capabilities, board wiring, clocks, and initialization
dependencies. A plausible peripheral name or familiar development board is insufficient to
select a physical pin or a safe register operation. The same MCU can appear on boards with
different LEDs, oscillators, bridges and connector assignments.

Praxis moves source interpretation into an offline, reviewable compilation step. Runtime
retrieval exposes a fixed target's canonical Markdown documents and exact schematic identities.
The coding assistant remains responsible for translating the requested behavior into firmware.
Verification produces separate evidence about that firmware.

The design objective is to make supported facts discoverable, source-located and internally
consistent, while making missing facts visible. It is not to infer arbitrary electronics or
prove arbitrary generated code correct.

## Responsibilities and trust boundaries

| Component | Owns | Does not establish |
| --- | --- | --- |
| Source publisher | Manuals, headers, schematic files and their revisions | Applicability to every board or silicon revision |
| Acquisition CLI | Exact downloaded bytes, extraction metadata and review drafts | Correct interpretation of requirements or PDF wiring |
| Reviewer and input author | Applicability, operating semantics, source-located resolutions | Independent sign-off unless an independent review actually occurs |
| Offline compiler | Normalization, mechanical checks, canonical rendering and publication | Electrical completeness or unmodeled operating behavior |
| MCP server | Target snapshot, exact retrieval and prerequisite read gates | Model understanding, emitted code order or firmware execution |
| Host and coding model | Task interpretation, tool selection, file creation and build orchestration | Correctness merely because a document was read |
| Verification tools | Specific compiler, model and isolation checks | Physical behavior without a corresponding hardware test |
| Hardware reviewer/tester | Actual PCB applicability and physical observations | Untested operating conditions |

MCP separates the host, its clients and specialized servers. The host manages the model and
connection lifecycle; Praxis provides a focused context service. This division follows the
[MCP architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture).
Praxis's SDK v1 implementation uses tools over stdio. It does not implement model sampling,
an autonomous coding agent, or a server-side firmware-generation loop.

Local acquisition/compilation/retrieval and local model inference are different properties.
Praxis retrieval performs no network requests. A host using a remote model may transmit
retrieved documents to its model provider. Deployment privacy depends on that host and model
configuration as well as the local server.

## Meaning of vectorless retrieval-augmented generation

The original RAG work combines a language generator with externally retrieved information and
uses a dense retrieval index in its proposed models. See Lewis et al.,
[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401).
Praxis does not reproduce that training architecture or its evaluation results.

Here, **vectorless RAG** is an architectural description: the host augments generation with
external evidence obtained by exact identities, a Markdown directory index and explicit links.
No embeddings or similarity rankings are used. The knowledge server is the retrieval component;
the coding model in the host supplies generation. This capability is already implemented, not
a future vector-search milestone.

For a published bundle B, query q and session read set S, retrieval can be described as:

```text
R(B, q, S) -> complete evidence | prerequisite error | identity error | no match
G(task, retrieved evidence, firmware project, model settings) -> candidate firmware
```

R is deterministic for the same bundle, query and session state. G need not be deterministic
and is not implemented by Praxis. Reproducible retrieval therefore does not imply reproducible
or correct firmware generation.

| Design choice | Intended benefit | Cost or limitation |
| --- | --- | --- |
| Canonical IDs and declared aliases | Avoid competing documents and accidental substring matches | Requires curated identities; unknown vocabulary can miss |
| Whole peripheral documents | Preserve register tables and nearby semantics | Context grows with document size |
| Exact net membership | Preserve electrical endpoints and sheet-qualified identities | Does not infer a circuit's function from geometry |
| Reviewed operating facts | Keep side effects and applicability explicit | Review requires engineering effort |
| Fixed target per process | Prevent silent target switching inside a server | Host must select and verify the right connection |
| Read gates | Mechanically require prerequisite retrieval | Cannot enforce instructions emitted by a model |

These are design tradeoffs, not benchmark findings about named competing tools. Semantic search
can be useful for broad discovery; Praxis's current contract favors exact supported workflows.

## Knowledge representation

Conceptually, a hardware fact contains an entity, property, value, applicability, source locator
and review/knowledge state. The implementation uses Pydantic records rather than a general RDF
store or a database. Relevant records include targets, peripheral instances, registers, bit
fields, components, pins, nets, source references and dependency edges.

Three evidence layers must remain distinct:

1. **Silicon declarations:** addresses, layouts, widths and masks extracted from headers.
2. **Operating and package semantics:** access effects, alternate functions, electrical and
   initialization conditions from reviewed manuals, datasheets and errata.
3. **Board connectivity and configuration:** component endpoints from a schematic, plus reviewed
   board roles, clock assumptions and topology configuration.

Headers generally cannot establish write-one-to-clear behavior, board polarity or clock readiness
requirements. Device Tree describes configuration and references; it is not proof of schematic
connectivity. A net name such as USART2_TX does not prove that an alternate function is enabled.

Authority is assigned by fact type. Conflicting supported declarations and reviewed values fail
publication rather than being silently resolved by source order. Authority labels and hashes do
not automatically verify the external publisher or the truth of a reviewed statement.

Unknown reset values remain unknown. Board facts distinguish documented facts, design assumptions
and unresolved items. Required workflow facts must be resolved before publication; declarations
outside the supported semantic scope may remain explicitly unasserted. A 168 MHz clock recipe is
not a measurement of running firmware.

## Two different graphs

### Hardware execution dependency graph

Let D be peripheral documents and let an edge p -> d mean that p must be retrieved before d.
The graph must be acyclic. For successful read set S, a peripheral request d is allowed only if
the index was read and all transitive prerequisites of d are in S. On a successful response,
S becomes S union {d}. A failed read leaves S unchanged.

The implementation validates exactly four stages per target family:

```text
STM32: RCC -> GPIO -> USART -> NVIC
AVR:   clock -> GPIO -> USART -> interrupts
```

The index is an additional session prerequisite. Topology queries need the index but do not
advance a peripheral stage. Successful repeated reads are idempotent. A process-local lock
serializes read checks and state changes; a restart creates an empty S.

These are routing paths for the supported bring-up workflows, not universal hardware laws.
GPIO polling uses the clocks/GPIO prefix. UART polling additionally needs USART. Supported
peripheral interrupt workflows use the final stage. A future unrelated peripheral should not
be forced to depend on USART merely because the v1 path is linear. Supporting arbitrary DAGs
requires changing the current fixed-stage validator and adding appropriate tests.

Startup, vector placement, core system exceptions, flash access configuration and clock changes
have additional dependencies. A SysTick-based time base requires those facts even when button
input is polled. DMA is unsupported by the current bundles. An emitted initialization sequence
requires its own checks; a read trace cannot prove that sequence.

### Electrical topology

A net is a set of directly connected endpoints. A component relates its terminals but does not
make all terminals one net. This can be viewed as a net/endpoint incidence graph with separate
component relationships. The implementation stores components and net memberships, not a
general circuit simulator.

For example, a GPIO-to-resistor-to-LED-to-ground path contains distinct electrical nets. Reviewed
board semantics identify the LED anode/cathode, fitted series path and active level. The board
validator follows explicitly supported passive paths and checks them against the schematic.
It does not merge nets across resistors or bridges, infer transistor behavior, or calculate
arbitrary circuit voltages.

The Discovery reference is a partial GPIO transcription. Complete membership within its
declared imported scope must not be described as a full-board netlist. Connector branches and
most supply endpoints are intentionally omitted and documented.

## Compilation and publication

The pipeline has distinct online and offline phases:

```text
Optional HTTPS acquisition -> immutable unreviewed archive
Source review and normalization -> registered target inputs
Offline adapters -> validated records -> canonical Markdown
Staging validation -> immutable bundle publication
```

Acquisition retains original bytes, selected pages, extracted fragments, mechanical requirement
candidates and hashes. It does not automatically promote those candidates into trusted rules.
Registered web archive inputs require an exact-import review receipt. PDF-only schematic wiring
currently requires reviewed transcription; automatic wire/junction interpretation is deferred.

CMSIS parsing uses target-aware Clang layouts and restricted macro evaluation. AVR parsing keeps
I/O and data-memory addresses distinct. KiCad parsing preserves component/pin/net identities and
disables XML entity expansion. DTS ingress preprocesses, compiles and applies declared overlays,
then resolves supported DTB relationships through libfdt. Unsupported bindings are not guessed.

The compiler sorts canonical records, records extractor versions and source hashes, renders
contiguous tables, checks links and dependencies, and rejects documents over 65,536 bytes.
It checks that registered inputs did not change during compilation. It validates a staged bundle
and publishes through a same-filesystem atomic rename. A different revision cannot overwrite an
existing output; the prior usable revision remains available after a failed import.

Determinism means byte-identical artifacts for identical registered inputs and extractor
versions within the supported environment. It is not a claim that different toolchains produce
identical output. The manifest revision hashes its canonical metadata and document hashes;
SHA-256 integrity detects inconsistency, not publisher authenticity or electrical correctness.

## Runtime retrieval

At startup, the server validates the manifest, registered paths, UTF-8, document hashes, size
limits, canonical filenames, links and the target graph. It snapshots Markdown into memory and
derives exact topology indexes from the published tables. No source adapters or web parsers run
on a retrieval call.

The read-only knowledge API is deliberately limited to three tools:

| Tool | Returned evidence | Preconditions |
| --- | --- | --- |
| read_wiki_index() | Complete identity, assumptions, routing and scope | Valid server snapshot |
| read_peripheral_doc(name) | Complete canonical peripheral Markdown | Index and transitive prerequisites read |
| query_schematic_netlist(target) | Matching net table and provenance; board context when registered | Index read; exact identity resolves |

Instance aliases select the canonical document, not a separate competing setup file. Exact
net names retain case; primary MCU pin lookup is case-insensitive. Ambiguity is an error with
candidates. A valid absent query returns an explicit no-match result. No fuzzy PA2/PA20 matching
is performed.

A board signal response may include related circuit nets as separate tables, the full reviewed
board document and component catalog. Published Markdown and retrieval responses have no fixed
Praxis byte ceiling. The process holds the verified bundle in memory; host memory and the
MCP client's model context remain practical constraints, with no silent truncation by Praxis.

Cross-links enable navigation but do not create additional public tools. In particular, rendered
Device Tree documents have no generic document-read endpoint in v1; an index link alone does not
make them directly retrievable through the three contracts. This is a current API coverage gap.

The host launches a local subprocess for stdio and routes model-requested tool calls. It owns
firmware file writes. Starting server.py in an unrelated terminal does not connect that process
to a separately launched stdio client. Restarting the client connection is needed after changing
the bundle selection; an active process retains its original snapshot.

## Verification boundaries and extension points

The separate Linux verification CLI accepts bounded C/header snapshots and uses fixed target
compiler profiles in a provisioned rootless Podman container. Syntax and object modes do not
link, flash or execute firmware. An unavailable sandbox fails closed. A model's independent
Makefile invocation is a host operation and is not the Praxis sandbox.

Static hardware golden cases and instrumented fixture drivers test selected configuration and
ordering properties. They do not simulate all silicon effects. The optional repair callback
allows at most three verification attempts and contains no model integration or automatic edits.

The optional [F407 build service](build-service.md) adds a separate MCP process with pinned
firmware asset staging, sandboxed full linking, ELF checks and immutable artifact identities.
It does not change the three-tool knowledge API. Its optional [read-only inspection backend](hardware-inspection.md)
adds live MCU diagnostics. [Programming/control](hardware-programming.md) are additional tools
enabled only by a separate target/artifact authorization; physical qualification is still open.

Current gaps include independent engineering sign-off, complete board coverage, automatic PDF
schematic interpretation, arbitrary target onboarding, physical programming qualification and
test adapters. ST-LINK inspection and separately authorized programming/control wrappers are
implemented; fixture-backed tests do not establish real programming behavior.
Assets are discussed in the
[knowledge and firmware asset contract](asset-contract.md); evidence and proposed experiments are
in [evaluation](evaluation.md). None of these gaps is concealed by a passing read trace.

## Implementation map

| Concern | Implementation |
| --- | --- |
| CLI and thin entry points | [cli.py](../praxis/cli.py), [server.py](../server.py), [compiler.py](../compiler.py) |
| Source models and compiler | [models.py](../praxis/models.py), [compiler.py](../praxis/compiler.py) |
| Input adapters | [adapters](../praxis/adapters) |
| Board semantics and paths | [board.py](../praxis/board.py) |
| Integrity and snapshots | [bundle.py](../praxis/bundle.py) |
| Markdown-derived exact lookup | [netlist.py](../praxis/netlist.py) |
| Retrieval state and MCP errors | [routing.py](../praxis/routing.py), [server.py](../praxis/server.py) |
| Isolated compilation and bounded repair | [verify.py](../praxis/verify.py), [repair.py](../praxis/repair.py) |
| Pinned asset staging and full linking | [firmware_assets.py](../praxis/firmware_assets.py), [firmware_build.py](../praxis/firmware_build.py) |
| Build MCP and read-only probe inspection | [build_server.py](../praxis/build_server.py), [hardware.py](../praxis/hardware.py) |
| Target-bound programming and scope/audit policy | [programming.py](../praxis/programming.py) |

The external references above establish terminology and protocol responsibilities. Praxis's
specific representation, gates and claimed properties are defined by its code and tests.

Hardware-backed verification is separate from retrieval. Its implemented inspection executor,
implemented programming/control stages, observation requirements and separation from the compilation
sandbox are documented in [hardware verification](hardware-verification.md).
