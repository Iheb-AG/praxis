# Alternate register interpretations

This compiler increment removes a representation gap needed for STM32F407 timer
PWM and input capture. It preserves different meanings of the same bits without
adding timer, register-name or manufacturer rules to Python. It does **not** add
a reviewed PWM/capture operating mode or physical qualification.

Recorded revisions, source hashes and verification results are in the
[machine-readable evidence](register-field-views-evidence.json).

The subsequent [timer operating increment](timer-modes.md) uses this representation
for scoped internal TIM2 PWM reference and software capture. External routed modes
and physical qualification remain separate work.

The previous profile selected only output-compare fields for CCMR1/CCMR2. Input
capture reuses those bit positions, so combining the header masks in a flat table
correctly failed the overlap check. The replacement is an explicit set of
alternative field views, supplied as source-profile data.

The [new profile](../sources/stm32f407g-disc1/profile-timer-views-v1.json) retains
four direction combinations for each register: `input_input`, `input_output`,
`output_input`, and `output_output`. The first word describes the lower channel
of the pair. These names select declaration sets; they do not grant permission to
configure every timer instance. The shared CMSIS structure includes registers
and fields that are absent or reserved on some instances.

The [immutable bundle](../bundles/stm32f407g-disc1-e01-timer-views-v1/wiki/index.md)
publishes all eight complete tables, including eight previously omitted input
filter/prescaler declarations. There are 64 view-table rows but only 28 distinct
name/mask pairs across the two registers; coverage does not count repeated rows
as newly discovered fields. Existing bundles remain unchanged.

## Representation and validation

`Register.fields` contains common fields. `Register.field_views` maps an explicit
identifier to fields, selection text and provenance. Common fields must be
disjoint from each selected view. Fields inside one view must also be disjoint,
unique and fit the register width. Different views may overlap each other.

`OperatingMode.field_views` selects exactly one view for each required register
that has alternatives. Required field names are checked against common fields
plus that selected view. A field from another view fails validation, even if it
occupies the same bits. View selection and required field semantics need registered
semantic evidence before an operating contract can be published.

```text
for configured register:
    for configured view:
        require a nonempty, unique list of exact header field names
        evaluate each declared mask with the restricted integer evaluator
        require contiguous masks and correct declared positions
        reject overlap within this view; never suppress explicit view errors
        retain each macro and its source under register.view.field

for reviewed view:
    require a configured declaration view with the same identity
    require every reviewed field name and mask to match its declaration
    merge explanatory meaning/provenance only into that view

for operating mode:
    require an explicit view for every required register with alternatives
    require all requested fields in the selected interpretation
    require semantic authority for selection, fields and register accesses

validate all published field masks against target-preprocessed header expressions
render one complete table per view; preserve normal link/hash/HEDG validation
```

The core has no rule that recognizes `TIM`, `CCMR`, PWM, ST or a particular part.
The synthetic tests use unrelated block, field and view names. No changes to
Python are needed to configure another register interpretation using this schema.

Implementation locations:

- [IR and mode validation](../praxis/models.py): `FieldView`, `Register.fields_for`, `OperatingMode`, `Peripheral`.
- [Declaration adapter](../praxis/adapters/discovery.py): exact names, mask evaluation and view-qualified expressions.
- [Compiler merge and provenance checks](../praxis/compiler.py): reject missing views, name/mask conflicts and unauthoritative selections.
- [Header verification](../praxis/adapters/constraints.py): every view field needs a checked header expression.
- [Manual adapter](../praxis/adapters/manual.py): view-aware position candidates and explicit unresolved gaps.
- [Rendering](../praxis/render.py) and [coverage](../praxis/coverage.py): complete tables, distinct declaration counts and separate view row counts.
- [Positive and negative checks](../tests/test_field_views.py): interpretation mixing, provenance, conflicting masks, missing names, repeat compilation and historical serialization.

Empty new fields are omitted during serialization. This preserves hash inputs
for existing definition-extension parent bindings and historical bundles.

## Source evidence and sequence

Evidence was obtained through actual ingestion MCP calls, from the registered
STM32F407 header and cached RM0090 Rev22 PDF. Complete pages 632–636 and the original
register diagrams were inspected. Header and manual naming are joined only by
the explicit `TIM_CCMR1` → `TIMx_CCMR1` / `TIM_CCMR2` → `TIMx_CCMR2` profile mappings.
No fuzzy matcher or inferred diagram relationships are used.

The [recorded MCP review packet](../examples/inventory/stm32f407g-disc1/timer-views-review.json)
has 32 source-bound candidates and no conflicts: 28 field positions, two offsets
and two reset candidates. All field positions match the header. Reset candidates
remain unreviewed because the header provides no independent reset declaration.
Access categories remain unresolved: the extractor does not promote spatial
`rw` rows into unconditional permissions. Original tables and visual evidence
remain available in the private source archive. Pending review never changes
workflow readiness.

```mermaid
sequenceDiagram
    participant Author
    participant Ingestion as Ingestion MCP
    participant Adapter as Header/manual adapters
    participant Compiler
    participant Bundle as Immutable bundle
    participant Client as Knowledge MCP client
    Author->>Ingestion: Read header and cached manual pages/images
    Ingestion-->>Author: Complete source evidence and hashes
    Author->>Ingestion: Discover configured views; prepare review packet
    Ingestion->>Adapter: Exact field names and explicit register aliases
    Adapter-->>Author: Candidates, matching views, unresolved access/reset review
    Author->>Compiler: Source profile and existing reviewed contracts
    Compiler->>Adapter: Target layout/mask verification
    Compiler->>Compiler: Check views, provenance, links and dependencies
    Compiler->>Bundle: Atomically publish complete tables and honest coverage
    Client->>Bundle: Read index, retrieve prerequisite documents
    Bundle-->>Client: Full documents; existing mode support only
```

## Reproduce

```bash
praxis compile --profile sources/stm32f407g-disc1/profile-timer-views-v1.json \
  --output /tmp/praxis-f407-timer-views
praxis lint --bundle /tmp/praxis-f407-timer-views
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 .venv/bin/pytest -q tests/test_field_views.py
.venv/bin/python tools/check_bundle_mcp.py \
  --bundle /tmp/praxis-f407-timer-views --peripheral tim --signal LED_A \
  --output /tmp/praxis-timer-view-mcp
```

Choose unused output directories. Native target tools are required for compilation;
published bundle retrieval works without ingestion tools. Full compiler/build
acceptance additionally requires the pinned Podman images and native KiCad checks.

Next: use this representation to publish instance-scoped TIM2 PWM/capture
operating contracts, validate ownership, preloads, stale/overcapture flags and
bounded handling, then build instrumented examples through isolated build MCP.
External waveform/capture tests will require separately verified package/board
routing, wiring and an exact-artifact flash approval. Full F407 acceptance and
independent engineering review remain open.
