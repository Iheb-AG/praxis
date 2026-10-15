# From a blocked request to a reviewed ADC workflow

Praxis now publishes `stm32f407g-disc1-e01-adc-v1`, a new immutable bundle for the
STM32F407VGT6 on the MB997-E-01 reference board. It adds **ADC1 internal-reference
single conversion** and **TIM2 one-pulse polling delay** operating contracts.
No external wire is needed. The physical board revision remains unconfirmed.

This expands executable guidance rather than only counting more declarations.
The bundle has 17 reviewed subsets and 16 explicit mode contracts, compared with
15 and 12 in clock-v1. Its unchanged declaration inventory contains 41 published
blocks, 523 register rows and 2,100 field rows. These counts do not establish full
ADC or MCU support. External ADC channels, injected/scan modes, ADC DMA/interrupts,
ADC2/3 internal sampling, bootloaders and firmware FLASH programming are not
covered by this addition.

## Reusable compiler mechanisms

[Definition extensions](../praxis/definitions.py) compose reviewed normalized
records with an existing knowledge set. A profile can declare
`"definition_extensions": ["adc_extension"]`; each entry names a registered
semantics-authority source. The extension schema is available with:

```bash
.venv/bin/praxis schema --kind definition-extension
```

An extension contains `schema_version`, the exact base file's `base_sha256`,
`applicable_mcus`, `additions` and `replacements`. An addition must be new; a
replacement must name an existing peripheral. Replacements are complete records,
so existing facts are preserved or changed explicitly. A stale base hash, wrong
MCU or duplicate identity fails. Competing extensions fail unless a later change
explicitly binds the exact composed parent state; see the subsequent
[I²C composition mechanism](i2c-expansion.md).
Extensions use the existing declaration, provenance, mode, link and size checks.
They do not turn F40x family similarity into automatic F407 applicability.

The [ADC extension](../sources/stm32f407g-disc1/reviewed/adc-v1/extension.json)
adds ADC and ADC-common records and replaces RCC/TIM records to add the necessary
gate and settling modes. It leaves the base definitions file unchanged.

The ingestion MCP's new `prepare_workflow_review(source_id, workflow_name,
evidence_locators=None)` tool prepares all documents in an authored workflow's
dependency closure. It expands known mode prerequisites and register scopes,
reports missing contracts/instance scope, and returns per-peripheral review
packets. Unknown declarations/registers and dependency cycles fail. Results are
always pending review, bounded to 1 MiB, and never approve publication. The
knowledge MCP still has exactly three read-only tools; ingestion now has eleven.

```mermaid
sequenceDiagram
    participant A as Author / coding assistant
    participant I as Ingestion MCP
    participant C as Offline compiler
    participant K as Knowledge MCP
    participant B as Build MCP
    A->>I: prepare_workflow_review(source, blocked workflow)
    I-->>A: Dependency scope, candidates, conflicts and gaps
    A->>I: Read complete source parts and declarations
    Note over A: Resolve semantics and write reviewed extension records
    A->>I: Record exact-source editorial review receipts
    A->>I: publish_reviewed_bundle(new profile, new output)
    I->>C: Compose base and extensions; validate
    C-->>A: Immutable revision or blocking error
    Note over K: Select the new bundle and restart the client session
    A->>K: Index and prerequisite documents
    K-->>A: Complete ADC/common/clock/timer guidance
    Note over A: Generate firmware from supported facts
    A->>B: Build with matching bundle and pinned assets
    B-->>A: Build result, or explicit missing sandbox dependency
```

The compiler remains deterministic Python with validated records. It contains
no model calls. A contributor or coding assistant supplies the editorial
reasoning between evidence and operating contracts. This addition neither parses
every engineering diagram automatically nor establishes universal MCU support.

## Evidence and conflict resolution

Hardware facts for this expansion were obtained through actual ingestion and
knowledge MCP calls. The review used complete RM0090 Rev22 pages392–393,
417–427 and429–431, DS8626 Rev12 pages135–136 and141, and the already registered
RCC/timer/clock evidence. Extracted tables remained intact. Review receipts bind
the selected archives to exact bytes; implementing-author review is explicitly
separate from independent engineering approval.

RM0090 page250 labels both ADC1EN values “disabled.” The ingestion MCP acquired
ST's RCC header and returned its full text. The enable macro sets ADC1EN and
reads it back; the disable macro clears it. The RCC record preserves this
explicit resolution and both sources. The acquired text hash is
`eb6911d964b1cf8a83993b19c8feb9845e8793d7c0e5d643390b53207c8b078e`.
The [catalog](../sources/stm32f407g-disc1/web-sources-adc.json) pins that hash;
a changed upstream branch fails acquisition instead of silently changing facts.

The new workflow assumes HSE8 → SYSCLK/HCLK168MHz, PCLK1=42MHz,
PCLK2=84MHz, TIM2CLK=84MHz and VDDA/VREF+ in2.7–3.6V. ADC prescale4
gives21MHz. Channel17 sampling480cycles takes about22.86us, exceeding the
reviewed10us acquisition minimum. A nominal1ms timer delay follows reference
and ADC power-up. These are conditional calculations, not measured board timing
or supply. Results are raw12-bit codes, not calibrated voltage measurements.

The growing source registry initially exceeded the coverage document limit.
New coverage reports retain the profile hash and link to `[[sources]]`; the
complete source registry remains in that Markdown document and the manifest.
Every coverage gap and register/field table remains complete. All documents
now have no fixed publication byte ceiling; no table truncation is introduced.

## Reproduction and use

Serving the shipped bundle requires only runtime dependencies. Recompiling the
[profile](../sources/stm32f407g-disc1/profile-adc-v1.json) additionally requires
the existing clock-v1 inputs and the following reviewed authoring archives:

| Archive identity | Acquisition / staged pages | Expected source SHA-256 |
| --- | --- | --- |
| `rm_adc_review` | Cached `rm0090`, pages392–393,417–427,429–431 | `f3ff2322eec21f4e49081f68481b764506eee81dba6031bc767e2f8955b27cca` |
| `ds_adc_review` | Cached `ds8626`, page141 | `1f41b4fa49a9960215ebb76cd0a75f20241db82eed60d308345a80463caeed22` |
| `ds_adc_limits` | Cached `ds8626`, pages135–136 | `1f41b4fa49a9960215ebb76cd0a75f20241db82eed60d308345a80463caeed22` |
| `st_hal_rcc` | Cataloged ST RCC header, complete text | `eb6911d964b1cf8a83993b19c8feb9845e8793d7c0e5d643390b53207c8b078e` |

Archives live under `sources/stm32f407g-disc1/imports/adc-scenario` and are
excluded from public packaging. Stage through `stage_cached_source`, read and
review the actual evidence, then record review receipts. The exact artifact
locators appear in the profile; identical input bytes, extractor versions and
review metadata are required for byte-identical reproduction. Newly authored
review metadata intentionally produces another revision. Do not copy a review
claim without reviewing its source.

```bash
.venv/bin/praxis lint --bundle bundles/stm32f407g-disc1-e01-adc-v1
.venv/bin/praxis support --bundle bundles/stm32f407g-disc1-e01-adc-v1 \
  --workflow adc1_internal_reference
.venv/bin/python tools/check_adc_workflow_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-adc-v1 --output /tmp/praxis-adc-retrieval
.venv/bin/python -m pytest -q tests/test_adc_modes.py
```

Use a new output directory for each replay. For isolated target compilation,
provision the documented [sandbox](verification.md), then append
`--source-directory stm32f407g-disc1-adc/application` to the replay command.
The [OpenCode example](../examples/opencode.adc.example.json) selects the same
bundle for knowledge and build. Replace path placeholders and restart the
OpenCode session to reset its child MCP processes. Existing launchers were not
changed automatically.

The [firmware example](../examples/stm32f407g-disc1-adc/README.md),
[initial expansion evidence](adc-expansion-evidence.json) and
[subsequent build evidence](adc-build-evidence.json) distinguish modeled tests,
real MCP retrieval, compilation and untested physical behavior. The initial
build attempt was blocked by absent Podman. After installation, the exact existing
locked image was imported into the default rootless store. A twelve-call actual
MCP replay then passed compilation, full linking, ELF/vector checks and artifact
revalidation without changing the source or toolchain locks. No board operation
occurred. Physical ADC qualification, full v1 release approval and broad MCU
support remain incomplete.
