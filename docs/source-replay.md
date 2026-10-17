# Restore source inputs in a clean checkout

The first timer IRQ push exposed a missing CI prerequisite. Full compilation tests
used reviewed imports present locally under `sources/stm32f407g-disc1/imports/`;
that directory is deliberately ignored and excluded from public packages. GitHub
reported 16 fixture errors even though tests using the published bundles worked.
The compiler correctly refused missing source bytes. Local validation had not yet
tested a checkout without those cached imports.

The [replay manifest](../sources/stm32f407g-disc1/source-replay.json) contains the
original metadata and review receipts for 16 archives, with six unique pinned
public downloads. It contains no PDF bytes or extracted manual pages. The generic
[restoration utility](../tools/restore_source_inputs.py) recovers these exact inputs
without changing published bundles or weakening provenance checks.

## Recovery sequence

1. Validate the manifest, original import revision, receipt and exact target against
   the selected profile. Every required archive must be covered.
2. Download each missing source from the configured public HTTPS hosts, checking its
   original SHA-256 and size; reuse verified local cache entries.
3. Require the recorded extractor versions and reproduce the original page selection.
4. Compare every regenerated artifact hash, complete locator list, extraction warning
   and source identity with the original import record.
5. Restore the original acquisition metadata and existing receipt only after those
   comparisons pass. This creates no new editorial or independent review.
6. Verify registered profile pins and publish the restored archive atomically.
   Existing different or corrupt archives fail; they are not overwritten.

No source mismatch, unsupported extractor or failed check becomes a passing skip.
Manufacturer content remains subject to its original terms. Raw downloads stay in
ignored local directories and are not included in public distribution archives.

```bash
uv sync --locked --extra ingest --extra test --extra web
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run python tools/restore_source_inputs.py \
  --manifest sources/stm32f407g-disc1/source-replay.json \
  --profile sources/stm32f407g-disc1/profile-timer-irq-v1.json \
  --cache .praxis-output/source-downloads
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run pytest -q
```

The tests also need the documented native tools and locally provisioned rootless
compiler image. Source restoration is an explicit networked preparation step;
serving a published Markdown bundle remains offline and does not require restoration.

## Evidence and current boundary

A checkout of commit `f87c7d8`, created from tracked files only, restored all 16
archives and passed **1,478 tests with zero skips** on Python 3.12 with required
external tools. Sixteen restoration tests cover exact replay, optional profile pins,
changed downloads/cache/profile pins, corrupt or escaped archives, altered extraction,
invalid metadata and incompatible extractor versions.

In [GitHub run 38741963511](https://github.com/Iheb-AG/praxis/actions/runs/38741963511),
Python 3.12, documentation, Docker knowledge retrieval, native KiCad and isolated
build jobs pass. Python 3.11 and 3.13 fail during source restoration; the exact errors
are still requested from the operator. The full remote matrix is **not verified**.
Do not infer those failures' cause from their Python versions alone.

CI now provisions the required native tools and compiler image, disables matrix
fail-fast, and retains an explicit allowlist of restoration/pytest logs and JUnit
results. It also replays all 17 current F407 applications through knowledge/build MCP.
The updated log capture makes preparation failures visible even before pytest starts.
No firmware flash or new physical qualification is part of this work.
