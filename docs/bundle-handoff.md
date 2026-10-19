# Project bundle handoff without reconnecting MCP

When knowledge, ingestion and build services share an operator-provisioned
`--handoff` directory, a validated publication can become active without restarting
the client or its MCP processes. Without this option, the existing fixed-bundle
behavior is unchanged. The bundle files remain immutable in both modes.

## Provision a project

Install the build/ingestion extras and provision the normal compiler lock and,
optionally, read-only hardware profile first. Use real directories without symlinks.
This example uses placeholders; replace them with absolute paths for your project.

```sh
praxis handoff-init \
  --bundle /project/bundles/initial \
  --publication-root /project/publications \
  --assets /praxis/assets/stm32f407vg \
  --workspace /project/applications \
  --artifacts /project/artifacts \
  --lock /praxis/toolchain-f407.lock.json \
  --hardware-profile /project/inspection.json \
  --output /project/handoff
```

Keep control records outside knowledge bundles and the application workspace.
Omit `--hardware-profile` when inspection is not needed. Initialization validates
the selected bundle, assets, compiler lock and optional backend identity. It does
not attach to a probe, reset a target or grant programming access.

Add `--handoff /project/handoff` to the existing `serve`, `build-serve` and
`ingest-serve` launch commands. Keep the knowledge/build `--bundle` arguments set
to the provisioned initial bundle. Keep the build paths and original inspection
profile unchanged. Ingestion must use the same target and publication root.
Reconnect once to install this launch option; later activations need no reconnect.
Clients should have their own project control directory to avoid sharing selections.

## Publication and adoption

`publish_reviewed_bundle(reviewed_profile, output_name, activate=True)` still runs
the offline compiler and its publication checks. When handoff is configured, it
then preflights exact target identity, full bundle integrity, firmware asset
compatibility, pinned toolchain lock and optional inspection backend. It derives
a new immutable read-only hardware profile for the selected revision; backend,
asset identity and unconfirmed physical board status do not change.

Only after these checks succeed does it atomically replace `active.json`.
`policy.json` stays pinned and immutable; `selections/` retains content-addressed
selection receipts, and `profiles/` retains revision-bound inspection profiles.
These are integrity records, not signatures or independent engineering approval.

The publication result includes `handoff.status`, `bundle_revision`, `generation`
and `reconnect_required=false`. This means the selection is committed, not that
every client has already observed it. The assistant then calls:

1. `read_wiki_index()` — adopts the active bundle and returns its revision header
   followed by the complete published index. The HEDG retrieval history resets.
2. `get_build_profile()` — adopts and acknowledges the same revision. Compare
   both revision values before generating/building code; retrieve prerequisites
   again for the newly selected bundle.

No tools are added/removed during this transition and stdio sessions stay open.
Build, report and inspection calls require `get_build_profile` acknowledgment for
each new selection. A direct peripheral read after adoption still requires index
and prerequisite retrieval. Re-activating the already active path/revision is
idempotent and does not reset the session again.

To activate a bundle already published under this project's root, call the
handoff-only tool:

```text
activate_published_bundle(output_name="new-revision", expected_revision="<full SHA-256>")
```

No arbitrary paths or cross-target selections are accepted. Set `activate=false`
to publish without selecting the result. If compilation succeeds but activation
fails, the result explicitly reports `activation_failed`; the published bundle is
preserved and the previous active selection stays usable. Correct the reported
compatibility problem and activate the existing publication; do not recompile over
its immutable directory.

## Concurrency and hardware boundaries

Every tool executes against one immutable snapshot. A running build may finish
against the previous revision while another process activates a new one; its
receipt retains the actual old revision. The next tool call adopts the new snapshot.
There is no distributed transaction across all clients: compare returned revision
identities, and stop/recheck if another author publishes during your workflow.

Each service serializes its checks, state changes and operations. Publication uses
an exclusive writer lock and atomic selection replacement. Concurrent activation
returns `HANDOFF_BUSY`; after a crashed writer, an operator must confirm it has
stopped before removing the stale `.activation.lock` file. Missing, malformed,
escaped or mismatched selection/policy records fail closed instead of falling back
to stale knowledge. Recovery does not require editing an immutable bundle.

Adoption discards probe connection IDs, programming authorization and telemetry
bindings. Existing artifacts remain stored but are rejected for validation or
reporting under a different revision. Reinspect the target and create a fresh
flash plan. Enabling programming still requires an explicit operator-provisioned
grant for that exact image/target/profile and a launch exposing its tools. Handoff
cannot authorize a flash, manufacture physical observations, qualify a board or
add unsupported MCU workflows.

## Verification

`tests/test_bundle_handoff.py` exercises persistent stdio knowledge/build/ingestion
sessions, real compiler publication, real rootless Podman builds before and after
activation, ELF revalidation, project reporting, prerequisite reset, old artifact
rejection, pinned-server behavior, invalid candidates, selection corruption,
idempotence and read-only profile rebinding. Run with strict external dependencies:

```sh
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q tests/test_bundle_handoff.py
```

See [ingestion](ingestion-mcp.md), [builds](build-service.md) and
[programming authorization](hardware-programming.md) for their separate contracts.
