# Contributing to Project Praxis

Full F407 coverage currently takes priority before further family expansion. The
[manufacturer inventory](docs/manufacturer-inventory.md) supplies source-pinned scope,
explicit applicability bindings and unresolved extraction requirements. Contributions can
repair source layouts, reconcile applicability or author instance/mode requirements. Keep
target facts in registered data; related ready examples do not establish whole-section support.

Praxis is an experimental development alpha. Contributions should expand **explicitly scoped
knowledge or verification**, with evidence that another contributor can reproduce. Register
discovery, reviewed operation, compilation and physical qualification are separate outcomes.
No contribution needs to claim complete support for a peripheral, a board or an MCU family.

The first experimental release prioritizes STM32F407 and Cortex-M4 breadth. See the
[current release scope](docs/experimental-release.md) and [ARM core example](docs/arm-core-support.md).
Additional STM32 parts can use explicit knowledge adapters, while compilation and hardware
support remain separately qualified per target. The [experimental F1/G0/H7 matrix](docs/stm32-family-expansion.md)
demonstrates profile-driven MCU-only extraction without a schematic. Add a registered profile
to expand declarations, then reviewed contracts to expand operating support. Non-ST expansion
is deferred in the current roadmap.

New compilation profiles require a registered, hash-pinned publication contract. Put target
register requirements, clock constraints, array views and routing names in data; do not add
manufacturer branches to the core compiler. See [compiler contracts and migration](docs/compiler-contracts.md)
for the schema, validation sequence and examples. Existing immutable bundles remain unchanged.

## Choose a contribution

| Contribution | Expected changes |
| --- | --- |
| Peripheral mode on an existing MCU | Reviewed register/field semantics, exact instances, mode prerequisites, workflow requirements, positive and negative tests |
| Another board using an existing MCU | Exact board revision, package pin map, topology, circuit semantics, clock assumptions and scoped workflows |
| Another MCU in a supported family | Target validation, declarations, applicable manual/errata semantics, package/AF facts, toolchain profiles and tests |
| Another MCU family | Validated target/header adapters and normalized records; target compiler, startup/linker and hardware backends where requested |
| Evidence or hardware test contribution | Reproducible sources or exact-artifact observations, including failures and untested boundaries |

Hardware access is optional for source/fixture/compiler contributions. Without it, label the
result source-reviewed, modeled or compile-tested. Builtin guards remain deliberately narrow.
The [explicit Cortex-M knowledge adapter](docs/target-adapters.md) supports configurable extraction
for a new target; adding an NXP document or changing a name does not establish reviewed operation,
firmware assets, a flash backend or physical support. Start with the fictional portability example.

## Set up and establish the baseline

```bash
uv sync --locked --extra ingest --extra build --extra test --extra web
uv run ruff check praxis tests tools server.py compiler.py
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q
uv run praxis schema --kind profile
uv run praxis schema --kind capability-catalog
```

Native ingestion/build checks need the tools described in the [detailed guide](README_DETAILED.md) and
[verification guide](docs/verification.md). Rootless sandbox tests require a provisioned image.
For full qualification, use `PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q`; missing tools
then fail instead of skipping. Record which checks actually ran. Hosted CI has not yet been
qualified by the existing local evidence.

## Add a peripheral mode

1. Propose a bounded goal: exact target, instance, mode, expected inputs/outputs and exclusions.
   Add or extend a [capability catalog](docs/capability-support.md). This is a work checklist,
   never a substitute for engineering evidence or a claim that every silicon mode is known.
2. Register source versions/hashes and authority by fact type in a profile under `sources/`.
   Headers establish declarations; manuals/errata establish operation; package documents and
   schematics establish pins and connectivity. Preserve license/origin records. Use cataloged
   acquisition, or supply documented local inputs. Do not commit raw downloaded manuals or
   private logs to obtain reproducibility; record acquisition instructions and expected hashes.
3. Use the [shared manual review adapter](docs/manual-review-compiler.md) to prepare candidates.
   The ingestion MCP can prepare an entire authored workflow with
   `prepare_workflow_review`, expanding dependency/register scopes and retaining gaps.
   Inspect complete source parts and figures, resolve variants and contradictions, and author
   reviewed normalized records. Extraction matches never constitute automatic review. Visual
   clock trees or schematic connections need supported structured input or explicit review.
4. Define an `OperatingMode` with exact instances, required registers/fields, operating
   constraints, bounded waits, side effects and provenance. Use `requires_modes` for actual
   mode prerequisites and the separate document DAG for retrieval. Add a scoped profile
   workflow; require it for publication only when its missing facts should block that release.
   Use [definition extensions](docs/adc-expansion.md) for additions and explicit replacements
   without copying the base definitions. Export their schema with
   `praxis schema --kind definition-extension`; pin the exact base hash and MCU applicability.
   When amending an already extended entity, bind `parent_definitions_sha256` to
   `get_ingestion_profile().composed_definitions_sha256`; see the
   [I²C composition example](docs/i2c-expansion.md). Preserve existing reviewed
   modes and review the complete replacement record.
   When a register reuses its bits in different modes, configure explicit
   `discovery.peripherals.<entity>.field_views` and select one in
   `OperatingMode.field_views`. Do not combine overlapping interpretations or
   add a manufacturer-specific exception to Python. Keep selection conditions
   source-backed; see [register interpretation contracts](docs/register-field-views.md).
   If selected modes of one canonical peripheral use different exact instances,
   declare `WorkflowRequirement.mode_instances` for every selected mode of that
   entity. The optional aggregate instance scope must equal their union. Preserve
   existing uniform scopes when this distinction is unnecessary; see the
   [paired timer route example](docs/timer-routes.md).
5. Test the contribution's failure modes: wrong target/package/instance, unsupported encodings,
   missing dependencies, conflicting sources and invalid topology as applicable. Preserve
   complete tables without imposing a per-document byte ceiling. Test target compilation separately from
   modeled initialization order and physical behavior.
6. Publish to a **new** bundle directory. Never edit published Markdown/manifest files to make
   checks pass or overwrite an earlier revision. Repeat compilation to establish deterministic
   output, lint it and test real stdio MCP retrieval. If firmware assets apply, match their
   target and bundle binding before compiling. Do not assume an old build/hardware profile is
   compatible merely because the MCU name is unchanged.

Example commands, with author-selected input/output paths:

```bash
uv run praxis prepare-review --profile sources/my-target/profile.json \
  --archive imports/my-target/manual --peripheral adc --output /tmp/adc-review.json
uv run praxis coverage --profile sources/my-target/profile.json
uv run praxis compile --profile sources/my-target/profile.json --output bundles/my-target-v1
uv run praxis lint --bundle bundles/my-target-v1
uv run praxis support --bundle bundles/my-target-v1 --workflow my_reviewed_workflow
uv run praxis serve --bundle bundles/my-target-v1
```

Names above are placeholders; no general ADC support is implied. Review receipts must describe
review that actually occurred. Implementing-author editorial review is not independent
engineering approval. Record independent review only after the exact revision was reviewed.

## Add a board

For an example of extending MCU semantics without a new compiler branch, see
[CAN nested declarations and scoped modes](docs/can-expansion.md). Explicit
register-prefix/field views bind vendor mailbox macros to ABI-checked members;
they still require reviewed semantics, instance limits and negative checks.

Start with [board ingestion](docs/board-ingestion.md). Keep the exact MCU, package, board revision
and physical sample identity distinct. Provide a source-backed package map and either native
KiCad/exported XML connectivity or an explicitly reviewed PDF transcription with omissions.
Keep opposite sides of resistors, switches and bridges on separate nets. Add LED/button/protocol
aliases only when their endpoints and circuit semantics are established. Device Tree is separate
configuration evidence, not proof of schematic wiring.

Reuse MCU knowledge only where applicability is verified. Board clock/fuse assumptions, pin
routing, populated components and solder bridges may differ. Hardware qualification of one
board revision does not transfer automatically to another.

## Submit and qualify

Use the [pull request template](.github/PULL_REQUEST_TEMPLATE.md). Include source provenance,
scope, exact bundle revision, reproducible checks and unresolved issues. Catalog-only changes
must explain denominator changes; deleting blocked goals is not an increase in support.

For a physical test, record the exact board/revision if known, wiring, firmware/artifact hash,
toolchain/profile, approved operation, stimuli and all observed windows. Label human observations,
firmware self-reports and independent measurements separately. Preserve failures and anomalies.
No flash approval carries over to a different image, and no test script should program a board
by default. Redact probe serials, machine paths and operator grants from public reports.

Run relevant checks once, then broaden checks where the change warrants it. Before a public
release, also run distribution checks and the [release gate](docs/PUBLICATION_READINESS.md).
An expected release failure is evidence of remaining work; do not invent review sign-offs.
Review third-party redistribution terms and preserve required notices before publishing sources
or derived material. Praxis's license does not replace a source's license.
