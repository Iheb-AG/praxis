# Scoped capability assessment and workflow preflight

`praxis support` derives a deterministic support report from a verified bundle's Markdown
coverage document. It needs no ingestion tools, network, compiler or board. It does not change
the bundle, MCP session or qualification records. The three knowledge MCP contracts are unchanged.

## Use before selecting a scenario

```bash
uv run praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1
uv run praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --workflow uart_timer_interrupts
uv run praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --workflow feature_flash
uv run praxis support --bundle bundles/stm32f407g-disc1-e01-clock-v1 \
  --catalog examples/capabilities/stm32f407g-disc1.json --format markdown
```

Exit codes: `0` for an informational report or a selected knowledge-ready workflow; `1` for a
selected blocked workflow; `2` for invalid input, an unknown exact workflow, unavailable coverage
or an integrity error. The third command is intentionally blocked. Workflow names are exact,
case-sensitive identities. Missing source/board/clock prerequisites remain visible in `issues`.
Legacy bundles without configurable coverage return `SUPPORT_REPORT_UNAVAILABLE` rather than a
guessed percentage. No workflow selection means no single scenario was approved by the command.

For the clock-v1 bundle the measured values are:

| Metric | Count | Percentage | Limit |
| --- | --- | --- | --- |
| Published recognized register blocks | 41/42 | 97.6% | Declaration coverage |
| Blocks with a reviewed subset | 15/42 | 35.7% | Partial operating knowledge |
| Blocks with an explicit mode contract | 9/42 | 21.4% | At least one mode, not all modes |
| Declared workflows that are knowledge-ready | 9/20 | 45.0% | Only this profile's authored workflows |

The subsequent [ADC bundle](adc-expansion.md) has 17 reviewed subsets,
16 mode contracts and 11 knowledge-ready authored workflows out of21. Select
`adc1_internal_reference` for its precise internal-channel/timer scope. The
clock-v1 figures above remain historical measurements of that immutable bundle.

There are 12 explicit mode contracts. **Overall MCU completion remains `null`**: none of the
denominators above enumerates every silicon feature, boot strategy or configuration combination.
Never average them. A source hash is not independent review, and a knowledge-ready workflow is
not automatically compile-tested or physically qualified. Those fields remain `not_assessed`
because this command does not consume artifact/physical evidence. It does not erase evidence
recorded elsewhere or mean that no physical test has ever occurred.

The report includes exact target metadata, bundle revision, retrieval closure, instance/mode
scope, authored mode order, required board signals and unresolved issues. Mode order is a
publication prerequisite plan; it does not prove actual generated C execution order. Counts and
ready workflow closures are checked against the verified bundle registry before assessment.

## Author a finite capability catalog

The [initial F407 catalog](../examples/capabilities/stm32f407g-disc1.json) contains the twenty
clock-v1 workflows plus six planned boot/update/power goals. It is a contributor work list,
not an exhaustive specification or evidence that every proposed feature applies to the target.
Nine of its 26 goals are knowledge-ready (34.6%). This percentage describes **that catalog only**;
it does not replace any percentage in the table or establish 34.6% complete MCU support.

```json
{
  "format": "praxis-capability-catalog-v1",
  "target": {
    "id": "stm32f407g_disc1_mb997_e01",
    "mcu": "STM32F407VGT6",
    "package": "Package_QFP:LQFP-100_14x14mm_P0.5mm",
    "board_revision": "MB997-E-01"
  },
  "scope": "CRC word-feed and a proposed application bootloader only",
  "exhaustive": false,
  "goals": [
    {"id": "crc", "category": "processing", "description": "Reviewed CRC word-feed scope", "workflows": ["crc_word_feed"]},
    {"id": "bootloader", "category": "boot", "description": "Planned, needs requirements and evidence", "workflows": []}
  ]
}
```

Generate the authoring schema with `praxis schema --kind capability-catalog`. Catalogs are
bounded to 256 KiB and 512 goals. Duplicate identities/requirements, extra qualification claims
and `exhaustive: true` are rejected. Exact target, MCU, package and board revision must match.
The report records the catalog's exact-byte SHA-256 so changes to the denominator are auditable.
No timestamps or local paths affect report bytes.

Each goal requires **all** its listed workflows. A missing or blocked workflow blocks the goal.
An empty workflow list means `planned`, never vacuously ready. A referenced workflow absent from
an earlier bundle remains blocked; catalog intent cannot publish new hardware facts. Even a
100% complete finite catalog leaves `all_features_supported: false` and overall completion null.
Goal sizes are unequal and unweighted, so percentages are not engineering effort estimates.
Schema validation cannot verify that an author's chosen scope covers every requirement in a
description; review the scope and workflow bindings themselves.

## Retrieval and verification remain separate

```mermaid
sequenceDiagram
    participant A as Contributor / assistant
    participant P as Support preflight CLI
    participant V as Verified Markdown bundle
    participant K as Knowledge MCP
    participant B as Build MCP
    A->>P: Exact bundle, optional catalog/workflow
    P->>V: Verify hashes and read coverage
    V-->>P: Scoped workflows, prerequisites, blockers
    P-->>A: Measured scopes; overall completion unknown
    alt Missing required knowledge
        Note over A: Review evidence and extend normalized records before generating unsupported configuration
    else Knowledge ready for selected scope
        A->>K: Index, board signals, prerequisite documents
        K-->>A: Target-bound facts and retrieval gates
        Note over A: Generate application in its workspace
        A->>B: Matching profile, isolated build, artifact validation
        B-->>A: Artifact-bound compilation and ELF evidence
        Note over A,B: Hardware execution requires a separate exact-image plan and approval
    end
```

Preflight is a contributor/automation aid, not an added MCP gate or a proof that arbitrary code
uses the approved instances. Assistants still retrieve facts through MCP and report unaddressed
requirements. Physical tests require compatible hardware and their own observation plan. Follow
the [contribution guide](../CONTRIBUTING.md) to expand a mode, board or MCU family.

## Validation evidence

The [recorded continuation](capability-support-evidence.json) reports 490 passed tests and nine
missing-tool skips (four KiCad, five Podman), including 27 new assessment checks. A real 17-call
knowledge MCP replay retained routing and missing-feature boundaries. Wheel/source contents and
public links passed; the installed-wheel CLI worked from `/tmp` with preinstalled dependencies.
This extension changes no published bundle or operating-mode coverage and performs no physical
board operation. Missing native tools and independent reviews still block full release qualification.
