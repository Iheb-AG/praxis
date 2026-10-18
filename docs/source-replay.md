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
3. Require the manifest's extraction runtime and recorded extractor versions, then
   reproduce the original page selection.
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
uv python install 3.12
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 UV_PYTHON=3.12 UV_PROJECT_ENVIRONMENT=.venv-source-replay \
  uv run --locked --python 3.12 --extra web python tools/restore_source_inputs.py \
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
restoration with `--offline` in a separate Python 3.12 environment. The application
and full strict test suite still use the matrix interpreter (3.11, 3.12 or 3.13),
including native PDF ingestion tests. Historical byte replay is a separate pinned
toolchain check, not a claim that every interpreter produces identical PDF geometry.
A missing or corrupt cache fails explicitly.
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

PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 UV_PYTHON=3.12 UV_PROJECT_ENVIRONMENT=.venv-source-replay \
  uv run --locked --python 3.12 --extra web python tools/restore_source_inputs.py \
  --manifest sources/stm32f407g-disc1/source-replay.json \
  --profile sources/stm32f407g-disc1/profile-timer-irq-v1.json \
  --cache .praxis-output/source-downloads --offline
```

Download-only mode validates the target, metadata and pinned raw bytes without
extracting pages or restoring reviews. It is preparation, not bundle acceptance.
Retry configuration is bounded: `--download-attempts` accepts 1–5 and
`--read-timeout` accepts 15–120 seconds. Logs identify the source URL, attempt,
failure type and cache verification; CI retains the acquisition log separately.

## Historical extraction runtime

The next Actions run passed source acquisition and Python 3.12/3.13, but Python
3.11 reported `REPLAY_MISMATCH` for `imports/adc-scenario/ds_adc_review`. Local
reproduction with Python 3.11.17 confirmed identical page text and table cells,
but different binary floating-point table coordinates: `66.78499999999998`
instead of `66.785`. That changes the extracted JSON hash. Python 3.12 changed
[`sum()` to use compensated summation](https://docs.python.org/3.12/whatsnew/3.12.html);
pdfplumber uses it when averaging snapped table-edge coordinates.

The replay manifest now declares `extraction_runtime` with implementation `cpython`
and Python `3.12`. This is versioned source-recovery policy, not a manufacturer
branch in the compiler. The utility rejects a different runtime before source
access or extraction, with `EXTRACTION_RUNTIME` and recovery instructions.
Download-only preparation does not need that runtime. Already restored imports
can be verified and consumed by another supported application interpreter; every
artifact hash and original metadata/receipt is still checked.

CI installs the declared historical runtime in `.venv-source-replay`, while `.venv`
and the `UV_PYTHON` supplied by the matrix remain unchanged for subsequent tests.
The runtime pin is intentionally major/minor; extractor package versions and
original artifact hashes remain exact, so any future patch-level output drift
still fails closed. CI reads the version from the validated manifest, so the
recovery policy has one source of truth. No table-coordinate rounding, numerical
tolerance, library monkey-patching, new review or historical bundle rewrite is used.

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

The runtime-pin correction passes **75 source-replay/web-import checks on both
Python 3.11 and 3.12**, and the full strict Python 3.11.17 regression passes
**1,584 tests with zero skips**. Fresh offline extraction on Python 3.12 restored
all 16 archives in a tracked-files-only source tree, preserving every historical
record and receipt. Both Python 3.11 and 3.12 then compiled all 51 published bundle
files byte-for-byte. The CI `uv` environment-switch flow was exercised offline:
restoration used the manifest runtime and the next command retained Python 3.11.
Local evidence is under `.praxis-output/ci-runtime-replay-20261018/`.
A new remote Actions run is still required to verify this updated GitHub workflow;
local checks are not that evidence.

CI now provisions the required native tools and compiler image, disables matrix
fail-fast, and retains an explicit allowlist of restoration/pytest logs and JUnit
results. It also replays all 17 current F407 applications through knowledge/build MCP.
The updated log capture makes preparation failures visible even before pytest starts.
No firmware flash or new physical qualification is part of this work.
