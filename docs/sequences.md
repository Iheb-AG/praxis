# Project Praxis sequence diagrams

These diagrams document logical control/data flow in the current implementation. Tool names
inside the knowledge server are its three public contracts; a host may prefix them with the
server name. The separate build and optional inspection sequences are documented in
[the build service](build-service.md) and [hardware inspection](hardware-inspection.md).
The model is shown separately from the host because it proposes calls and code while the host
executes tool calls and file writes. External model service details are intentionally omitted.

Configurable discovery, dependency-driven publication and branching retrieval sequences are
documented in [peripheral discovery](peripheral-discovery.md). Schema-2 bundles use their
declared graph rather than a universal four-document chain.

The [Cortex-M adapter sequence](target-adapters.md#compilation-and-retrieval-sequence)
shows configurable CPU/header extraction and source mapping without inherited firmware support.

The [STM32 ARM core sequence](arm-core-support.md#two-graphs-and-one-actual-implementation)
connects complete manual/diagram review, scoped write masks, immutable correction, modeled
effects and the actual retrieval/build MCP loop.

The implemented [ingestion MCP sequence](ingestion-mcp.md#evidence-and-publication-workflow)
adds assistant-driven source acquisition, complete evidence/image review and immutable
publication before restarting retrieval against the new revision.

## 1. Acquisition, review and offline compilation

Optional web acquisition is online. Review, compilation and publication are distinct steps.
Structured source adapters do not need the acquisition step when files are already local.

```mermaid
sequenceDiagram
    actor Author as Bundle author
    participant Web as Optional scraper
    participant Vendor as Source website
    participant Archive as Evidence archive
    participant Review as Engineering review
    participant Compiler as Offline compiler
    participant Adapters as Header, CAD and DTS adapters
    participant Stage as Staging directory
    participant Bundle as Published bundle

    opt Sources acquired from explicit HTTPS URLs
        Author->>Web: praxis scrape with source catalog
        Web->>Vendor: Download bounded source bytes
        Vendor-->>Web: PDF, HTML or text
        Web->>Archive: Store bytes, hashes, fragments and candidates
        Archive-->>Author: Unreviewed evidence
        Author->>Review: Inspect source and applicability
        Review->>Archive: Record exact-import review receipt
    end
    Author->>Compiler: praxis compile with registered profile
    Compiler->>Compiler: Validate target, paths, sources and receipts
    Compiler->>Adapters: Parse registered local inputs
    Adapters-->>Compiler: Declarations, components, nets and topology
    Compiler->>Compiler: Merge reviewed semantics and check conflicts
    Compiler->>Compiler: Validate required board workflow facts
    Compiler->>Compiler: Render canonical Markdown and manifest in memory
    Compiler->>Compiler: Confirm source hashes unchanged
    Compiler->>Stage: Write candidate bundle
    Compiler->>Stage: Reopen and validate staged bundle
    Compiler->>Bundle: Atomic rename into a new revision directory
    Bundle-->>Author: Immutable output path
```

PDF wire geometry is not parsed automatically. Reviewed PDF transcription enters as a registered
structured source. A receipt
records review, but does not by itself establish independent hardware sign-off.

## 2. Publication success and failure

```mermaid
sequenceDiagram
    actor Author
    participant Compiler
    participant Inputs as Registered source files
    participant Stage as Temporary staging bundle
    participant Validator as Bundle validator
    participant Output as Requested output path

    Author->>Compiler: Compile profile into output
    Compiler->>Inputs: Read and hash inputs
    Compiler->>Compiler: Parse, validate and render in memory
    Compiler->>Inputs: Recheck original source hashes
    alt Invalid fact, unsupported input or changed source
        Compiler-->>Author: Error, no publication
    else Candidate passes source checks
        Compiler->>Stage: Write Markdown and manifest
        Compiler->>Validator: Load staged bundle
        alt Integrity, size, graph or link failure
            Validator-->>Compiler: Error
            Compiler-->>Author: Error, staging cleaned up
        else Staged bundle valid
            Validator-->>Compiler: Valid revision
            alt Output absent
                Compiler->>Output: Same-filesystem atomic rename
                Compiler-->>Author: Published path
            else Same revision already present
                Compiler->>Output: Verify existing bundle and revision
                Compiler-->>Author: Reuse existing output
            else Different revision already present
                Compiler-->>Author: IMMUTABLE_BUNDLE, select new output path
            end
        end
    end
    Note over Author,Output: Failed compilation does not replace a prior published revision
```

Publication is atomic at the directory rename boundary. It is not a signed-distribution system
or a transaction across multiple separately published bundles.

## 3. MCP startup and target confirmation

```mermaid
sequenceDiagram
    actor User
    participant Host as IDE or OpenCode host
    participant Client as MCP client
    participant Server as Praxis stdio process
    participant Snapshot as Bundle snapshot
    participant Model as Coding model

    User->>Host: Start with explicit bundle configuration
    Host->>Server: Launch executable with --bundle absolute path
    Server->>Snapshot: Validate manifest, hashes, links, paths and graph
    Snapshot-->>Server: Fixed Markdown snapshot and exact lookup index
    Client->>Server: initialize
    Server-->>Client: Negotiated capabilities and server instructions
    Client->>Server: notifications/initialized
    Client->>Server: tools/list
    Server-->>Client: Three read-only tool definitions
    Host->>Model: Task and available tools
    Model-->>Host: Request read_wiki_index
    Host->>Client: Execute requested tool
    Client->>Server: tools/call read_wiki_index
    Server->>Snapshot: Read complete index
    Server->>Server: Record successful index read
    Server-->>Client: Identity, assumptions, scope and routing
    Client-->>Host: Tool result
    Host->>Model: Add returned evidence to context
    Model-->>Host: Compare returned target to requested target
    Host-->>User: Confirm identity or report mismatch
```

Identity comparison is a host/agent workflow requirement. The server isolates the selected
bundle, but cannot know a user's intended board from an unrelated conversation. Tool annotations
and server instructions are supplied to the client; adoption of instructions is client-dependent.

Each process serves one snapshot. Editing a bundle/configuration file does not retarget an existing
process. A manually started stdio process in another terminal is not automatically the process
the host uses.

## 4. LED and button retrieval followed by code generation

```mermaid
sequenceDiagram
    actor User
    participant Host as Coding host
    participant Model as Coding model
    participant Server as Praxis tools
    participant State as Session read set
    participant Wiki as Markdown snapshot
    participant Project as Firmware workspace

    User->>Host: Blink LED_A and follow USER_BUTTON on LED_B
    Host->>Model: Task after target confirmation
    loop LED_A, LED_B and USER_BUTTON
        Model-->>Host: Request exact signal query
        Host->>Server: query_schematic_netlist with alias
        Server->>State: Require index already read
        Server->>Wiki: Resolve indexed net and registered board context
        Wiki-->>Server: Separate nets, components, polarity and provenance
        Server-->>Host: Source-backed signal evidence
        Host->>Model: Return evidence
    end
    Model-->>Host: Request RCC document
    Host->>Server: read_peripheral_doc rcc
    Server->>State: Check prerequisites
    Server->>Wiki: Read full RCC Markdown
    Wiki-->>Server: Complete document
    Server->>State: Add rcc after successful read
    Server-->>Host: Clock evidence
    Host->>Model: Return evidence
    Model-->>Host: Request GPIO document
    Host->>Server: read_peripheral_doc gpio
    Server->>State: Check index and rcc
    Server->>Wiki: Read full GPIO Markdown
    Wiki-->>Server: Complete document
    Server->>State: Add gpio after successful read
    Server-->>Host: Pin-control evidence
    Host->>Model: Return evidence
    Model-->>Host: Inspect firmware assets and clock setup
    Host->>Project: Read existing project files
    Project-->>Host: Assets present or missing
    Host->>Model: Project context
    alt Required facts and build assets available
        Model-->>Host: Propose application source and integration changes
        Host->>Project: Write requested firmware files
        Host-->>User: Files created, verification status reported separately
    else Essential facts or assets missing
        Model-->>Host: Identify missing inputs and supported integration scope
        Host-->>User: Explicit limitation, no invented hardware definitions
    end
```

The model's actual behavior is not guaranteed by this expected sequence. In particular, it can
ignore instructions or generate unsupported startup code. A client trace and artifact review are
needed to establish what happened. GPIO polling does not require USART retrieval. SysTick timing
still requires a valid clock basis, vector/handler integration and core exception setup.

## 5. Prerequisite failure and retry

```mermaid
sequenceDiagram
    participant Client
    participant Server as MCP tool wrapper
    participant Gate as Locked session
    participant Wiki as Markdown snapshot

    Note over Client,Gate: Index has been read, no peripheral documents served
    Client->>Server: read_peripheral_doc usart
    Server->>Gate: Check transitive prerequisites
    Gate-->>Server: Missing rcc and gpio, state unchanged
    Server-->>Client: Tool error PREREQUISITE_REQUIRED
    Client->>Server: read_peripheral_doc rcc
    Server->>Gate: Check prerequisites under lock
    Gate->>Wiki: Read rcc
    Wiki-->>Gate: Full document
    Gate->>Gate: Add rcc to read set
    Gate-->>Server: Document
    Server-->>Client: RCC Markdown
    Client->>Server: read_peripheral_doc gpio
    Server->>Gate: Check prerequisites and serve under lock
    Gate->>Wiki: Read gpio
    Wiki-->>Gate: Full document
    Gate->>Gate: Add gpio to read set
    Gate-->>Server: Document
    Server-->>Client: GPIO Markdown
    Client->>Server: read_peripheral_doc usart
    Server->>Gate: Check prerequisites and serve under lock
    Gate->>Wiki: Read usart
    Wiki-->>Gate: Full document
    Gate->>Gate: Add usart to read set
    Gate-->>Server: Document
    Server-->>Client: USART Markdown
```

The lock covers both checks and successful state updates. A concurrently submitted dependent
call may succeed only if prerequisites have already been successfully served when its locked
check runs. Topology results never satisfy a peripheral prerequisite.

## 6. Detecting a stale or wrong bundle

```mermaid
sequenceDiagram
    actor User
    participant Host
    participant Old as Existing MCP process
    participant New as Fresh MCP process

    Host->>Old: read_wiki_index
    Old-->>Host: stm32f407vgt6_fixture / praxis-f407-example-1
    Host->>Host: Compare against expected Discovery target
    Host-->>User: Wrong bundle, stop hardware-specific generation
    User->>Host: Exit old host and launch with explicit configuration
    Host->>Old: Close old connection
    Host->>New: Launch with Discovery bundle path
    New-->>Host: Initialize and expose tools
    Host->>New: read_wiki_index
    New-->>Host: stm32f407g_disc1_mb997_e01 / MB997-E-01
    Host->>New: Query LED_A, LED_B and USER_BUTTON
    New-->>Host: PD12, PD13 and PA0 with source context
    Host-->>User: Reference retrieval confirmed
```

This is the failure mode observed during the OpenCode walkthrough. The corrected retrieval was
reported by the user; it is not a controlled model benchmark or a physical board test. Reference
revision confirmation does not identify the physical PCB revision.

## 7. Separate compilation and optional repair

```mermaid
sequenceDiagram
    actor Operator as Host or developer
    participant Repair as Optional repair callback hook
    participant Verify as Verification CLI or callback
    participant Podman as Rootless sandbox
    participant Compiler as Target compiler
    participant Report as Verification report

    Operator->>Repair: Start bounded verification workflow
    loop At most three verification attempts
        Repair->>Verify: Verify current source snapshot
        Verify->>Verify: Check bundle, lock, approved headers and source policy
        alt Sandbox unavailable or unprovisioned
            Verify-->>Repair: Exception, workflow stops with no native fallback
        else Inputs and sandbox ready
            Verify->>Podman: Start fixed profile with mounts and limits
            Podman->>Compiler: Syntax check or object compilation
            Compiler-->>Podman: Exit status and bounded diagnostics
            Podman-->>Verify: Compilation result
            Verify->>Report: Record source hash, bundle and toolchain identity
            Verify-->>Repair: Result
            alt Compile passed
                Repair-->>Operator: Stop successfully
            else Repeated diagnostics, missing facts or attempt limit
                Repair-->>Operator: Stop with explicit reason
            else Another repair permitted
                Repair->>Operator: Invoke supplied repair callback
                Operator-->>Repair: Generated-source edit result
            end
        end
    end
```

The loop is a logical view with stop branches; success or a stop reason exits the loop immediately.
The callback hook is a Python API, not an autonomous agent or additional MCP tool. Its callbacks
own edits. Verification never changes the knowledge bundle. The CLI does not link, flash or run
generated firmware. Live Podman compilation/isolation checks now run in the recorded environment.
The separate [F407 build MCP sequence](build-service.md#build-and-validation-sequence) adds full
linking, supplied integration assets, image validation and immutable artifact publication.

The server's isolation from compilation is deliberate: read-only retrieval remains portable
while the sandbox is a separate Linux extension. See [verification](verification.md) for exact
limits and failure behavior.
