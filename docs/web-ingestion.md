# Optional web document ingestion

Praxis can acquire engineering PDFs, static HTML documentation and plain text from explicit
HTTPS URLs. Acquisition is a separate online CLI or optional authoring-MCP step. Compilation and knowledge MCP retrieval remain
offline and vectorless. There are no model calls, embeddings, recursive crawls or hidden searches.

## Install and scrape

```bash
uv sync --locked --extra ingest --extra test --extra web

# Official F407 datasheet, reference manual and errata; all pages by default.
.venv/bin/praxis scrape \
  --catalog sources/stm32f407vgt6/web-sources.json \
  --output imports/f407

# One document, selecting the datasheet's package and AF pages for review.
.venv/bin/praxis scrape \
  --url https://www.st.com/resource/en/datasheet/stm32f407vg.pdf \
  --id ds8626 --target STM32F407VGT6 --kind pdf \
  --pages 51,63 --output imports/f407-pin-review
```

The catalog contains official document URLs, not a claim that the latest document revisions have
been approved for your silicon. Check the revision inside each downloaded PDF. Use `--sha256 HASH`
for a single URL to require previously approved bytes. Existing archives are reused without a
network request; changed source metadata, page selection or input bytes need a new output path.
Each catalog document is committed atomically. If a later download fails, earlier archives remain
usable and a retry reuses them.

If a site rejects automated downloads, acquire the file normally and extract it explicitly:

```bash
.venv/bin/praxis scrape \
  --url https://www.st.com/resource/en/datasheet/stm32f407vg.pdf \
  --id ds8626 --target STM32F407VGT6 --kind pdf \
  --from-file /absolute/path/stm32f407vg.pdf \
  --output imports/f407-local
```

This records the URL as **user-declared** provenance, not a verified HTTP download. It does not
bypass authentication, access challenges or paywalls. HTML uses `--kind html`; plain headers
or text use `--kind text`. Page selection is PDF-only and uses one-based pages, e.g. `1-5,51,63`.

## Archive contents

```text
imports/f407-pin-review/
├── source.pdf                # Exact downloaded bytes
├── import.json               # URL, final URL, hashes, versions, warnings, selection
├── extracted/part-0001.json  # Page text, table cells, bounding boxes and page locators
├── draft/part-0001.md        # Review draft; every detected table retains all its rows
├── requirements.json        # Source-located requirement candidates
└── README.md                 # Review status and interpretation boundary
```

The number of parts depends on the selected pages. These are **evidence archives**, not duplicate
peripheral wiki pages. They are excluded from knowledge MCP retrieval. The optional
[ingestion MCP](ingestion-mcp.md) exposes registered evidence for explicit review in a separate
authoring process. The compiler continues to publish
one canonical document per peripheral, preserving its complete tables and 64 KiB limit.

PDF text uses layout-aware extraction. Every detected table retains all rows, source-page identity
and bounding box in JSON. Cross-page tables stay explicitly flagged fragments; automatic joining
could silently mix bit fields. No detected tables does not establish that the page has no tables.
Pages without a text layer are marked `OCR_REQUIRED`; OCR is not implemented.

HTML extraction removes scripts and common navigation/form elements. Static text, table cells,
links, and rowspan/colspan metadata are retained. Merged/nested cells carry review flags; the
positional Markdown table is not a claim that the original geometry was resolved. JavaScript
rendering and arbitrary page execution are not supported.

Requirement candidates are lines matching words such as "must", "shall", "before" and "reserved".
They retain page/line locators and an unreviewed status. Detection is intentionally mechanical;
it does not resolve negation, line wrapping, conditional applicability or initialization order.
Use the original page and neighboring text when deciding what a sentence requires.

Imported text is evidence, not executable assistant instructions. Raw source bytes and structured
extractions remain available when Markdown rendering cannot express the source faithfully.

## Review and compiler integration

After actually inspecting the source, extraction and applicability, record the review:

```bash
.venv/bin/praxis review-import \
  --import-dir sources/my_f407/imports/ds8626 \
  --reviewer 'Reviewer name' \
  --notes-file /absolute/path/review-notes.md
```

Keep an import inside the target source tree before registering it in a compiler profile. For
example, after copying the F407 example profile to `sources/my_f407/` and placing the archive at
`sources/my_f407/imports/ds8626/`, add a source entry:

```json
{
  "id": "datasheet_page",
  "path": "imports/ds8626/extracted/part-0001.json",
  "authority": "pinout",
  "version": "DS8626 revision inspected by reviewer",
  "license": "ST document terms apply",
  "origin": "https://www.st.com/resource/en/datasheet/stm32f407vg.pdf"
}
```

Then declare the archive mapping at the profile's top level:

```json
{
  "web_imports": {
    "datasheet_page": "imports/ds8626"
  }
}
```

Use `SourceRef(source="datasheet_page", locator="page:51/table:1")` for supported facts in the
reviewed peripheral JSON, and cite it in reviewed operating notes. The selected page must
actually support the fact. Curating those facts and resolving table continuity is still an explicit
engineering step; the scraper does not convert requirement candidates into trusted register semantics.

The compiler checks artifact hashes, exact import revision, target identity and the review receipt.
It adds hashed acquisition metadata and the review receipt to bundle provenance. A pending or
undeclared web import cannot be used as a registered compiler source. Changed imported artifacts
invalidate the archive and review. Marking an archive reviewed does not automatically publish it,
independently certify hardware, or permit unsupported initialization operations.

## Limits and reproducibility

Downloads require public HTTPS hosts. Redirect hosts must be explicitly allowed with
`--allow-host HOST` or the catalog's `allowed_hosts`. Every redirect is checked. TLS verification
remains enabled; environment proxies are not inherited. Downloads are bounded to 64 MiB, five
redirects, connection/read timeouts and a checked 120-second total budget. Compressed HTTP
responses are rejected if the server does not honor `Accept-Encoding: identity`.

PDFs are limited to 2,500 pages; individual extracted page artifacts to 1 MiB and total extracted
output to 64 MiB. Use page selections for large manuals. These are acquisition/output bounds,
not an operating-system sandbox for the PDF parser.

Original bytes, HTTP ETag/Last-Modified when supplied, final URL, acquisition time and extraction
versions are recorded. The import revision excludes acquisition time; cached local extraction is
deterministic for identical bytes, selections and extractor versions. Recompilation uses the
recorded archive without contacting the source website. Hashes establish integrity, not vendor
authenticity or independent review.

The implementation uses [HTTPX streaming](https://www.python-httpx.org/quickstart/),
[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), and
[pdfplumber text/table extraction](https://github.com/jsvine/pdfplumber). Dependencies are optional
and locked in `uv.lock`; published bundles can be served without the HTML/PDF parser packages.
