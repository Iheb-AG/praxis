# Hardware-independent reference MCP

`praxis reference-serve` exposes documentation acquisition and retrieval for arbitrary
hardware: MCUs, sensors, displays, interface ICs, modules, and actuators. It requires
neither a firmware target profile nor a predefined catalog. Existing MCU knowledge,
ingestion/publication, and build services retain their target-specific checks.

## Start through the MCP client

Install the existing `web` extra in the Praxis environment. Configure a separate
stdio server; the client launches it:

```toml
[mcp_servers.praxis_references]
command = "/home/iheb/Desktop/Praxis_Bundle/.venv/bin/python"
args = ["-m", "praxis", "reference-serve", "--archive-root", "/home/iheb/Desktop/Praxis_Bundle/imports/hardware-references"]
cwd = "/home/iheb/Desktop/Praxis_Bundle"
enabled = true
startup_timeout_sec = 30
tool_timeout_sec = 180
```

The paths above match the local development checkout; adapt them elsewhere.
Reload the MCP client after adding the server. A running knowledge server does
not automatically expose these additional tools.

## Workflow

1. Identify the exact component and an authoritative documentation URL. The assistant
   may obtain a URL from the user or a separately available web-search tool.
2. Call `acquire_hardware_reference(source_id, hardware, url, ...)`. The hardware
   label is caller-supplied and is preserved as the generic archive's target label;
   it is not verified or required to match an MCU. Use a new document ID for new
   revisions, changed hardware labels, or different page selections.
3. Call `search_hardware_reference` with literal text, then `read_hardware_reference`
   on complete returned locators. PDF tables and source hashes remain attached.
4. Use `list_hardware_references` to discover the acquired documents and locators.

Example acquisition arguments (illustrative URL; replace with a real manufacturer URL):

```json
{
  "source_id": "sensor_model_revision1",
  "hardware": "Exact manufacturer / part / revision",
  "url": "https://manufacturer.example/datasheet.pdf",
  "kind": "pdf",
  "pages": "1-4"
}
```

The explicitly supplied HTTPS URL permits its own host. Additional redirect hosts
must be configured using repeated `--allow-host HOST` launch arguments. The existing
public-address, TLS, response-size, timeout, and immutable-archive checks still apply.
An optional SHA-256 pins expected source bytes. Search/read/list remain offline;
only acquisition uses the network, and existing matching archives are reused.

## Scope

This is an explicit-URL document scraper, not a general internet search engine or
recursive crawler. It supports extractable PDFs, static HTML, and text. JavaScript
rendering and OCR are not provided. No tool can promise extraction from every site
or every document format. Downloading a manual does not establish component identity,
voltage compatibility, board wiring, driver support or physical validation.

Imported contents remain unreviewed evidence. The service has no publication,
compile, flash or execution tools; cross-component facts must be reviewed before
entering a target-specific knowledge bundle. Existing MCU publication checks remain
unchanged. A library may contain at most 256 documents in list responses; use
separate roots for larger collections.
