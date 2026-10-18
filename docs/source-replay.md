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

## Resilient CI acquisition

The Python 3.11 and 3.13 jobs in the reporting-feature push failed with
`DOWNLOAD_FAILED: HTTPS download failed: ReadTimeout` during restoration, before
pytest started. Python 3.12 passed. These logs establish an acquisition failure;
they do not establish a Python interpreter compatibility failure.

CI now prepares raw evidence in one `source-evidence` job, rather than downloading
the same manufacturer PDFs independently in each Python job. Its cache key includes
the complete replay-manifest hash. Cache hits still undergo SHA-256 and byte-count
validation. Each Python job restores that exact cache and runs extraction/receipt
restoration with `--offline`, preserving interpreter-specific extraction checks and
the full strict test suite. A missing or corrupt cache fails explicitly.
This uses the documented [GitHub cache restore action](https://github.com/actions/cache/blob/v4/restore/README.md).

Acquisition uses a 60-second HTTP read timeout and a 15-second connect timeout, with
at most four attempts by default. Transient transport errors and HTTP
408/429/500/502/503/504 use bounded 2/4/8-second backoff. Failed partial downloads
are discarded; only completed, hash-verified bytes enter the cache. Exhaustion still
fails the preparation job. Hash/size mismatches, access denials, unapproved hosts,
private addresses and invalid metadata are not bypassed or healed by retrying.
The downloader's existing byte, redirect and streamed-transfer limits remain in force.

For the same two-phase flow locally:

```bash
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run python tools/restore_source_inputs.py \
  --manifest sources/stm32f407g-disc1/source-replay.json \
  --profile sources/stm32f407g-disc1/profile-timer-irq-v1.json \
  --cache .praxis-output/source-downloads --download-only

PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 uv run python tools/restore_source_inputs.py \
  --manifest sources/stm32f407g-disc1/source-replay.json \
  --profile sources/stm32f407g-disc1/profile-timer-irq-v1.json \
  --cache .praxis-output/source-downloads --offline
```

Download-only mode validates the target, metadata and pinned raw bytes without
extracting pages or restoring reviews. It is preparation, not bundle acceptance.
Retry configuration is bounded: `--download-attempts` accepts 1–5 and
`--read-timeout` accepts 15–120 seconds. Logs identify the source URL, attempt,
failure type and cache verification; CI retains the acquisition log separately.

## Evidence and current boundary

A checkout of commit `f87c7d8`, created from tracked files only, restored all 16
archives and passed **1,478 tests with zero skips** on Python 3.12 with required
external tools. Sixteen restoration tests cover exact replay, optional profile pins,
changed downloads/cache/profile pins, corrupt or escaped archives, altered extraction,
invalid metadata and incompatible extractor versions.

Later operator-provided Actions logs identify the restoration failure as an HTTP
read timeout. The local retry/cache change was tested with 60 source-replay/web-import
checks, including transient/persistent timeouts, partial streams, permanent failures,
cache corruption, exact original receipt replay and enforced offline behavior.
All six pinned sources were acquired into a fresh cache and all 16 historical
archives restored into a separate clean source tree. Recompilation reproduced all
51 files of the published timer-IRQ bundle byte-for-byte, retaining revision
`9d2494ef9dcc4056ad83ef96f163801b5b57f89130528d5491b49d6482aa7404`.
A new remote Actions run is
still required to verify the updated GitHub matrix; local checks are not that evidence.

CI now provisions the required native tools and compiler image, disables matrix
fail-fast, and retains an explicit allowlist of restoration/pytest logs and JUnit
results. It also replays all 17 current F407 applications through knowledge/build MCP.
The updated log capture makes preparation failures visible even before pytest starts.
No firmware flash or new physical qualification is part of this work.
