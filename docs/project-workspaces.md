# Independent projects and explicit bundle reuse

`praxis project-init` creates project-owned source inputs, bundle selection,
reference acquisition, authoring/publication, build artifacts, reports and handoff
state. It optionally creates local Codex settings. It never changes global client
settings, searches other chats, flashes a board or qualifies an application.

From the chosen project root, an example is:

```sh
python -m praxis project-init \
  --root . --id example_project --mode auto \
  --profile "$TARGET_PROFILE" --catalog "$SOURCE_CATALOG" \
  --assets "$FIRMWARE_ASSETS" --lock "$TOOLCHAIN_LOCK" \
  --bundle "$EXPLICIT_REUSE_CANDIDATE" \
  --install-codex
```

Resolve variables from the selected installation and target. Use the Python
containing Praxis. A valid reviewed source profile is required; an arbitrary raw
PDF is insufficient. Full-stack setup currently uses the supported F407 firmware
build profile; creating directories does not extend target support.

## Selection modes

| Mode | Behavior |
| --- | --- |
| `auto` | Check explicit candidates in order; reuse a compatible revision or compile selected sources |
| `reuse` | Require an explicit compatible bundle; fail without substituting another target |
| `fresh` | Compile the project-owned source snapshot; precompiled bundle inputs are rejected |

Repeat `--bundle` for multiple candidates. There is no implicit disk/bundle-database
search. Reuse requires exact MCU/package/board identity and assumptions, matching
reviewed profile/source hashes (including web-import/review metadata), and readiness
for every explicit `--workflow`. Similar peripheral names or shared MCU families do
not establish board connectivity, clock state or component compatibility.

Partial reuse across different boards means explicitly reusing applicable reviewed
source records, then compiling the new board's own profile, topology and constraints.
The initializer does not transplant netlists or merge operating semantics between
manufacturers. Missing/blocked requested workflows prevent acceptance. Legacy bundles
without coverage cannot prove requested workflow readiness. With no workflow selected,
initialization records the limited scope; a partial baseline remains partial.

`fresh` can reuse adapters, reviewed sources and cached evidence. The manifest
records `compiled_from_source` versus `reused_exact_bundle`; neither implies fresh
internet downloads. Request document reacquisition separately when needed.

## Ownership

```text
project/
  .codex/config.toml          # Optional local MCP overrides
  .praxis/
    project.json             # Decision, identity, scope and relative state paths
    source-snapshot.json     # Copied source hashes
    mcp-servers.json          # Launch inventory; adapt to each client's schema
    codex-mcp.toml           # Generated local MCP fragment
    authoring/profile.json
    authoring/catalog.json  # When a catalog was selected
    bundles/initial-r001/
    references/
    workspace/
    artifacts/
    reports/
    handoff/
    hardware-initial.json    # Optional read-only inspection profile
```

Every mutable service store is project-local. Pinned firmware assets and compiler
locks may be shared read-only. Source snapshots preserve registered inputs, header
include trees and declared reviewed evidence archives, including relative paths
and provenance. Unrelated sibling profiles, bundles, application code and grants
are not copied. Symlinks and nonregular source files fail. The snapshot resource
budget is 1 GiB/10,000 files; published Markdown retains no fixed size ceiling.

Reused bundle bytes are copied into the project's own store after validation. The
revision remains unchanged; mutable handoff state is separate. Publication in
project A does not change project B. Chats in the same project intentionally share
that project's state.

An optional `--hardware-profile` seeds an explicitly pinned inspection backend and
creates a matching local initial profile. Backend/assets are validated; physical
board uncertainty remains unchanged. No grant or probe connection is copied. The
service no longer depends on inspection data inside a disposable report folder.

## Client setup

`--install-codex` creates `.codex/config.toml` with the standard four Praxis service
IDs. Project entries override their global launch arguments without modifying the
global file. Codex loads local settings only for trusted projects; verify effective
connections and reconnect once after setup. See [official configuration guidance](https://learn.chatgpt.com/docs/config-file/config-advanced).

Generated settings contain resolved machine paths so launch works from an unrelated
working directory. Portable `praxis.md` and `project.md` should contain relative
examples and instructions for discovering actual paths. Keep generated host settings
private. The launch inventory is not a universal configuration format for all clients.

Existing project state/configuration is never overwritten. If local settings already
exist, initialize without `--install-codex`, inspect `codex-mcp.toml`, then explicitly
merge only the relevant entries. Without a selected catalog, local ingestion is
disabled to prevent inheriting an unrelated global authoring service.

Later publication uses [bundle handoff](bundle-handoff.md): compare returned revisions,
re-read prerequisites after adoption, and retain separate exact-image flash approval.
The application still needs its own supported workflows, implementation, verification
and physical qualification.

## Verification

```sh
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q \
  tests/test_project_workspace.py tests/test_bundle_handoff.py
```

Tests exercise exact reuse, fresh/fallback compilation, mismatched targets/sources,
missing workflows, source-path safety, existing-config preservation, independent
selections from one seed, isolated reference stores, real stdio services and a real
rootless target build. They do not establish physical behavior.
