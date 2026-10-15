# I²C controller coverage and reusable compiler composition

The `stm32f407g-disc1-e01-i2c-v1` bundle adds an editorially reviewed **I2C1,
seven-bit, 100 kHz controller transmitter with bounded polling**. It retains
previous ADC/clock/UART contracts: 18 reviewed subsets, 18 mode contracts and
12 ready authored workflows out of 23. The declaration inventory remains
41 published blocks, 523 register rows and 2,100 field rows. These denominators
describe the authored inventory, not overall MCU completion.

The new `i2c1_controller_transmit` workflow is knowledge-ready. Broader
`feature_i2c` and `i2c1_wired_transmit` remain blocked. Receive, fast-mode,
ten-bit, target/slave, multicontroller, interrupt, DMA and SMBus contracts, board
SCL/SDA endpoints, pull-ups and a target-device protocol are not established by
this addition. Physical PCB/silicon revision, errata qualification and independent
engineering review remain open. No probe access, flash, reset or physical I²C
transaction occurred. The [example](../examples/stm32f407g-disc1-i2c/README.md)
configures the controller with PE disabled and does not drive a bus.

## Source-to-contract pipeline

Hardware facts came through actual ingestion MCP responses: header discovery,
complete RM0090 Rev22 pages 238–239, 247, 836, 841–844, 846 and 855–867, and
existing reviewed clock records. Selected cached pages were staged under
`sources/stm32f407g-disc1/imports/i2c-scenario/rm_i2c_review`, excluded from public
distributions. The source PDF hash is
`f3ff2322eec21f4e49081f68481b764506eee81dba6031bc767e2f8955b27cca`.
Exact artifact paths and review dependencies appear in the
[profile](../sources/stm32f407g-disc1/profile-i2c-v1.json) and generated manifest.
Recompilation also requires earlier ADC/clock archives; serving the bundle does not.

The manual adapter prepares candidates. An implementing author reviews semantics
and writes normalized records/narrative; Pydantic and the compiler validate them.
Neither compiler nor retrieval server calls a model. Editorial receipts bind
source bytes and do not constitute independent sign-off.

The shared manual's FLTR register is restricted to F42/F43 on page 866 and absent
from the exact F407 header; the F407 table retains all nine applicable registers.
Page 858 mixes an intrinsic 50 MHz statement with a greater-than-42 prohibition.
This contract uses only the reviewed 42 MHz PCLK1 point without generalizing either limit.

The controller preserves these operational requirements:

- Configure disabled: CR2.FREQ=42, CCR=210, TRISE=43; OAR1 mandatory bit 14 is set.
- Clear SB by SR1-read/address-DR-write and ADDR deliberately by SR1/SR2 reads.
  Generic SR2 polling during address acquisition can clear ADDR unexpectedly.
- Wait TXE per byte and final BTF/TXE before STOP; TXE alone is not completion.
- Never write CR1 while START, STOP or PEC is pending. Disable PE after completed
  STOP and idle. Every wait has a finite iteration bound.
- Errors take priority over simultaneous progress. rc_w0 errors are not W1C.
  ARLO forbids STOP. Failures latch reset-required, including failed cleanup;
  no automatic retries, scans or GPIO bus recovery. Completed failure cleanup
  leaves PE unchanged so hardware does not clear error flags before explicit reset.

```mermaid
sequenceDiagram
    participant A as Contributor / assistant
    participant I as Ingestion MCP
    participant C as Offline compiler
    participant K as Knowledge MCP
    participant B as Build MCP
    participant P as Rootless Podman
    A->>I: Discover declarations; prepare blocked workflow review
    I-->>A: Candidates, complete-part locators, unresolved contracts
    A->>I: Read complete evidence and existing reviewed records
    I-->>A: Source text/tables and hashes
    A->>I: Get composed-definition parent hash
    Note over A: Author scoped semantics and explicit extension
    A->>I: Record source review; publish new reviewed profile
    I->>C: Compose, validate facts/links/modes/size, render
    C-->>I: Immutable Markdown revision
    A->>K: Index, RCC, FLASH, PWR, I2C
    K-->>A: Complete documents; broad/wired workflows blocked
    A->>B: Matching build profile; build_firmware
    B->>P: Pinned isolated compilation and linking
    P-->>B: ELF and diagnostics
    B-->>A: ELF/vector validation and artifact identity
    A->>B: validate_firmware(exact artifact)
    B-->>A: Revalidated artifact; physical behavior untested
```

## Reusable compiler changes

[Definition extensions](../praxis/definitions.py) still bind exact base-file bytes
and MCU applicability. A later extension may amend an already extended entity
only with `parent_definitions_sha256`, binding the entire composed parent state.
This permits I²C to amend RCC after ADC without an implicit overwrite.

`get_ingestion_profile` exposes `composed_definitions_sha256`. Locally, the same
value is `definitions_digest(load_definitions(profile, paths))`: complete validated
Peripheral records, sorted by ID, `model_dump(mode="json")`, sorted JSON keys,
ASCII escaping, compact separators, then SHA-256. Defaults are included. Changed
preceding records or extension order invalidate the binding. Unbound competing
changes, duplicate additions, stale hashes, wrong targets and non-semantic source
authority still fail. Replacements remain complete explicit records.

Source provenance now uses two complete Markdown tables: artifact identity,
path, hash and metadata reference; then shared authority, version, license and
origin. The manifest retains expanded metadata. Every value is preserved while
repeated long URLs/import versions are stored once per identical tuple. The new
source catalog is 47,918 bytes and the largest document is 50,996 bytes. Register
and field tables remain contiguous. New compilation no longer imposes the historical 64 KiB ceiling;
see [complete-document behavior](document-scale.md).

The reusable [workflow MCP client](../tools/check_workflow_mcp.py) accepts exact
workflow/mode expectations, blocked workflows, optional register exclusions and
matching build/revalidation. It reads documents and routes through MCP, does not
parse vendor sources or invoke compilers itself, and exposes no hardware tools.

## Verification and reproduction

Repeated ingestion MCP publication produced 49 byte-identical files. The actual
ten-call knowledge/build replay passed all 13 expectations, including rootless
ARM compilation, full linking, ELF/vector checks and artifact revalidation.
The [evidence](i2c-expansion-evidence.json) records identities and regression results.

The [effect model](../tests/fixtures/f407_i2c_model.c) executes the same controller
header used in the target translation unit. It models command clearance,
SR1/SR2 effects, transmit progression, NACK/ARLO/BERR/OVR and stuck flags. Negative
cases cover clock/reset/ownership assumptions, invalid input, unreviewed wiring,
bounded failure, retained errors and retry blocking. A test caught a possible
second STOP after ownership ended; ownership is now cleared before post-STOP
idle checking. A routing test caught missing FLASH/PWR gates in an internal
draft; the final bundle explicitly requires their retrieval. Models establish
neither electrical behavior nor correctness of arbitrary generated code.

```bash
.venv/bin/praxis lint --bundle bundles/stm32f407g-disc1-e01-i2c-v1
.venv/bin/praxis support --bundle bundles/stm32f407g-disc1-e01-i2c-v1 \
  --catalog examples/capabilities/stm32f407g-disc1-i2c.json \
  --workflow i2c1_controller_transmit
.venv/bin/python tools/check_workflow_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-i2c-v1 \
  --workflow i2c1_controller_transmit \
  --blocked-workflow feature_i2c --blocked-workflow i2c1_wired_transmit \
  --mode i2c/controller_transmit_polling --mode rcc/i2c1_gate_reset \
  --peripheral flash --peripheral pwr --forbid-register i2c/FLTR \
  --source-directory stm32f407g-disc1-i2c/application \
  --output /tmp/praxis-i2c-replay
```

Use a new output directory per replay. Builds require the provisioned
[sandbox](verification.md). The [OpenCode configuration](../examples/opencode.i2c.example.json)
selects matching knowledge/build bundles; replace absolute paths and restart the
client session. Existing launchers are not switched automatically.

Next work can add separately reviewed receive termination and board/device
contracts. Physical transactions need that evidence, an appropriate device and
a separately authorized test. Broad MCU support and release approval remain incomplete.
