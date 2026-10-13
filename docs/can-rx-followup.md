# CAN initialization: source-backed RX follow-up

The first physical CAN image flashed correctly but failed its application test:
ten coherent observations reported `init_timeout`, no FIFO interrupt and no
received payload. A subsequent read-only MCP snapshot showed INRQ clear, INAK
set and RX low. These are preserved [failed results](reports/can-loopback-results.md),
not a successful CAN demonstration. They motivated this candidate; they do not
prove its root cause.

Current physical status: after fresh exact-image approval, the candidate passed
one MCP flash/readback/reset-run and two fresh internal-loopback observation
windows. Initial short-spaced windows failed the heartbeat freshness check and
remain retained. See [the complete physical result](reports/can-rx-results.md).
The software/preflight evidence below records the preceding preparation stage.

## Evidence and interpretation

All engineering evidence was retrieved through actual local ingestion MCP
calls, including complete text pages and selected page images. No online lookup
or guessed Discovery-board pinout supplied the following route.

| Evidence | Reviewed observation |
| --- | --- |
| RM0090 Rev22, PDF pages1073–1075 and1092 | Normal entry requires eleven consecutive recessive bits before INAK clears. Loopback mode selection takes place during initialization. Established combined silent/loopback mode disconnects CANRX internally; this does not establish that initialization synchronization ignores RX. MSR.RX monitors the actual CAN_RX input. |
| RM0090 Rev22, PDF pages283,285,287 | GPIOD mode, pull and alternate-function encodings; word-access input register; GPIO locking behavior. |
| DS8626 Rev12, PDF pages58,67 | STM32F407VGT6 LQFP100 PD0 is physical pin81; PD0 AF9 selects CAN1_RX. The alternate-function table was inspected as an image through MCP. |
| MB997-E-01 schematic, PDF pages2,7 | Direct net PD0 connects U4:81 and expansion header P2:34. Page images were inspected through MCP. |

The candidate owns PD0, requires **P2:34 to be externally unconnected**, sets
an internal pull-up while the pin is still an input, then selects AF9 and
alternate-function mode. It requires bounded high-input observation and a high
MSR.RX sample before clearing INRQ. The controller still waits for actual INAK
and SLAK acknowledgements with finite budgets. It never drives PD0 as an output.

This is an authored initialization policy to test the RX synchronization
hypothesis, not a universal vendor requirement for all loopback applications.
Established loopback isolation and initialization synchronization are separate
claims. A single high sample cannot prove eleven recessive bit times; the
controller acknowledgement remains mandatory. Internal loopback needs no CAN
transceiver or additional jumper. It does not qualify an external CAN bus.
The physical PCB revision remains unconfirmed.

## Compiler changes and publication

The new [profile](../sources/stm32f407g-disc1/profile-can-rx-v1.json) composes the
exact prior definition state and preserves existing operating contracts. Its
reviewed extension adds `gpio/can1_rx_pd0`, `rcc/can1_rx_gpio_gate` and the
`can1_rx_guarded_loopback_irq` workflow. CAN modes now explicitly require the
GPIO route. Exact topology lookup resolves `CAN1_RX_SYNC` and `P2:34` to the
same complete PD0 net. Removing the required GPIO mode fails dependency
validation; external CAN remains blocked.

Publication initially rejected invalid source references, non-semantic mode
provenance, missing access-width review and incomplete component pin declarations.
These drafts were corrected; validation rules were retained. Repeated page
provenance then exceeded the existing 64 KiB limit. The shared compiler now
normalizes repeated source directory prefixes in addition to metadata tuples.
An artifact row retains its source ID, filename, SHA-256 and registry references.
Concatenating its exact prefix and filename reconstructs the original path,
including literal `./` and repeated separators. Expanded paths remain in the
manifest. This is lossless registry normalization; register and field tables
are unchanged. Oversized documents still fail publication.

Actual ingestion MCP publication and independent repeated publication produced
**49 byte-identical files**. The largest Markdown document is60,793 bytes.
The immutable [new bundle](../bundles/stm32f407g-disc1-e01-can-rx-v1/wiki/index.md)
has20 reviewed subsets,26 mode contracts and16 ready authored workflows out of29.
Declaration counts remain41 published blocks,523 registers and2,131 fields.
These are scoped inventories, not a percentage of complete MCU support.
Review was performed by the implementing author; independent engineering
approval remains outstanding.

```mermaid
sequenceDiagram
    participant A as Contributor / assistant
    participant I as Ingestion MCP
    participant C as Offline compiler
    participant K as Knowledge MCP
    participant B as Build / hardware MCP
    participant P as Selected board
    A->>I: Read manual text and datasheet/schematic images
    I-->>A: Exact source pages, hashes and provenance
    A->>A: Author scoped RX route and finite failure models
    A->>I: Record editorial review and publish new profile
    I->>C: Validate sources, modes, topology, links and limits
    C-->>I: Immutable Markdown revision
    A->>K: Index, exact RX net and declared prerequisites
    K-->>A: Complete documents and dependency-gated contracts
    A->>B: Build candidate and revalidate artifact
    B-->>A: Isolated target compilation, linking and ELF checks
    A->>B: Inspect selected target and plan exact image
    B->>P: Bounded identity reads and installed-image comparison
    B-->>A: Plan; reject old image before candidate telemetry
    Note over A,P: Flash/reset requires fresh exact-image approval
```

## Software verification and initial preflight

The [candidate](../examples/stm32f407g-disc1-can/telemetry_rx_application/README.md)
uses the existing92-byte CAN telemetry ABI. Old failed application sources and
their immutable bundle remain intact. New portable effect models cover GPIO
ownership, readback failures, lost gate writes, pull/AF/mode ordering, low RX,
delayed RX and finite synchronization. CAN synchronization needs eleven
consecutive modeled recessive observations; dominant observations reset the
count. These samples are digital model steps, not measured hardware bit times.

**772 tests passed,4 skipped** in the full regression; the skipped checks require
KiCad. All155 focused CAN/catalog checks and Ruff passed. An actual18-call
knowledge/build MCP replay retrieved topology and prerequisites, checked blocked
workflows, built and linked through the pinned rootless sandbox, validated the
ARM ELF and revalidated the artifact. This did not execute the image.

Five actual read-only hardware MCP calls subsequently found the selected probe,
inspected its target, prepared the4,920-byte sector0 plan and rejected the older
installed image with `READBACK_MISMATCH` before candidate SRAM observation.
No flash, reset, halt or resume was requested. Probe identity and raw target
records stay private. [Sanitized evidence](can-rx-evidence.json) records the exact
candidate hashes and checks.

That planned single physical run subsequently passed after user approval and
confirmation that P2:34 was unconnected. It used the exact artifact above without
firmware edits or retries. [Physical results](reports/can-rx-results.md) preserve
both rejected short-spaced observations and qualified fresh windows. External-bus
support, measured timing, repeatability and qualified v1 release remain open.
The next development increment should follow the same source-to-model-to-MCP
process for a blocked capability; never rewrite the vault simply to pass a build.

## Reproduce the software MCP scenario

```bash
.venv/bin/python tools/check_workflow_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-can-rx-v1 \
  --workflow can1_rx_guarded_loopback_irq \
  --blocked-workflow can1_external_bus \
  --mode can/silent_loopback_fifo0_irq --mode gpio/can1_rx_pd0 \
  --signal CAN1_RX_SYNC --signal P2:34 \
  --source-directory stm32f407g-disc1-can/telemetry_rx_application \
  --output /tmp/praxis-can-rx-replay-new
.venv/bin/python -m pytest -q
```

Use a new replay output directory. The replay exposes no hardware tools.
For OpenCode, select the [matching candidate configuration](../examples/opencode.can-rx.example.json),
replace absolute paths and artifact placeholders, then restart both MCP
processes. Existing client configurations were not changed automatically.
