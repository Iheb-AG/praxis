# STM32F407VGT6 offline ingestion

The executable [compiler.py](../compiler.py) delegates to [praxis/compiler.py](../praxis/compiler.py).
The three public adapter functions are `parse_cmsis_headers`, `parse_kicad_netlist`, and
`parse_device_tree`. Importing `compiler.py` does not start compilation.

## Run

From the repository, with the existing virtual environment:

```bash
.venv/bin/python compiler.py \
  --profile sources/stm32f407vgt6/profile.json \
  --output bundles/stm32f407vgt6

.venv/bin/praxis lint --bundle bundles/stm32f407vgt6
.venv/bin/praxis evaluate --bundle bundles/stm32f407vgt6
.venv/bin/praxis serve --bundle bundles/stm32f407vgt6
```

`praxis compile --profile ... --output ...` is equivalent. From another working directory,
use absolute paths for the executable, profile and output. An identical rebuild is idempotent;
changed inputs need a new output directory, such as `bundles/my_f407_rev_a`. Existing revisions
are never replaced.

For a new environment use `uv sync --locked --extra ingest --extra test` first. Offline compilation
then needs no network access. System ingestion tools are Clang, `arm-none-eabi-gcc`, GCC, `dtc`,
`fdtoverlay` for overlays, and libfdt. Pre-exported XML does not require KiCad installed. Optional
Python dependencies supply libclang and defusedxml.

## Inputs and applicability

[sources/stm32f407vgt6/profile.json](../sources/stm32f407vgt6/profile.json) selects:

- Official ST `stm32f407xx.h` at commit `3c77349ce04c8af401454cc51f85ea9a50e34fc1`,
  Arm CMSIS 5.9.0, transitive vendor headers and upstream licenses.
- Reviewed JSON facts and Markdown operating sequences for the supported UART workflow.
- A **hand-authored partial example XML netlist**, not a live export of the user's board.
- A separate **synthetic DTS/overlay**, which does not establish physical board connectivity.
- An explicit package pin map and signal aliases: PA2 is LQFP100 pin 25; PA3 is pin 26.
- An assumed HSE8/PLL clock configuration, 3.3 V supply, and five FLASH wait states.

The clock plan validates M=8, N=336, P=2, Q=7, AHB /1, APB1 /4 and APB2 /2. It yields
SYSCLK/HCLK=168 MHz, PCLK1=42 MHz and PCLK2=84 MHz. These are declared assumptions, not
measurements of the oscillator or regulator. A pinned ST clock example provides additional local
evidence for this operating point. Silicon revision and errata review remain pending.

For your board, copy the source directory, replace `raw/netlist.xml` with its KiCad XML export,
and update the MCU reference, exact component value/footprint, board revision, source origins,
pin-name resolutions and signal aliases. Register every additional input in `sources`.
Keep the example label until actual qualification and target-model support justify changing it.

Review AF capabilities against the datasheet separately. A `USART2_TX` net label does not prove
that an MCU endpoint supports that signal or has AF7 configured. The reviewed AF subset covers
PA2/PA3 only. Exported pin names must match the explicit package map; symbols that use oscillator
or alternate-function suffixes need an explicit reviewed naming resolution.

The offline compiler performs no network requests, model calls, user build scripts or firmware
execution. The optional [web scraper](web-ingestion.md) downloads PDFs/HTML and extracts review
drafts in a separate online step. PDF-derived operating semantics still need reviewed facts.
Source hashes establish integrity, not publisher authenticity.

## Complete declarations and reviewed semantics

`header.discover: true` enables the complete non-reserved declaration maps for four structures:

| Peripheral | Register rows | Field definitions | Array handling |
| --- | --- | --- | --- |
| RCC | 23 | 244 | Reserved holes preserve offsets |
| GPIO | 10 | 161 | AFR[0]/AFR[1] become AFRL/AFRH |
| USART | 7 | 51 | All declared USART/UART instance bases retained |
| NVIC | 7 | 7 | Counts/strides retained; IP is 240 bytes |

This is not a complete chip manual. NVIC array capacity does not establish that every interrupt
slot exists on F407. GPIO bases do not establish which ports are bonded in LQFP100. UART4/5 share
a structure with USARTs, but operating feature availability still needs the manual.

Clang computes ARM ABI offsets, widths and array counts. The target preprocessor resolves
object macros; a restricted integer evaluator checks bases and masks. Explicit macro aliases
and identical encoded-value aliases do not become duplicate fields. Unexpected overlap,
non-contiguous masks, unsupported expressions and conflicting positions fail compilation.

Headers ordinarily do **not** specify reset values, electrical behavior or access side effects.
Explicit `*_RESET_VALUE` / `*_RESET` macros are recognized when present; conflicting values fail.
Otherwise reset stays `null` / "not asserted". C qualifiers do not establish hardware access
semantics, and a missing reset is never replaced with zero.

Reviewed registers enrich declarations with access, reset, side effects and meanings. Layout
or mask conflicts block publication. Unreviewed declarations stay visible as `unknown` /
"not asserted" and are outside supported code generation. Missing operating semantics for
mandatory UART workflow registers block publication even if the optional policy list is removed.
Another workflow needs additional reviewed facts and required-register policy.

## Topology and publication

XML parsing explicitly forbids DTDs, entities and external references. It validates MCU identity,
package, connected physical pins, endpoint uniqueness and net uniqueness. Every net endpoint
appears in a flat Markdown table. Series components never merge their adjacent nets.

DTS ingestion preprocesses includes, compiles with `dtc`, applies overlays and reads the resolved
DTB through libfdt. Supported address translations, phandles, inherited status, clocks and interrupt
relationships are resolved. Clock-provider specifiers remain relationships; binding-specific rates
are not invented. Unsupported properties stay raw and unresolved. C-preprocessor includes,
native DTS includes and incbin dependencies must all be hash-registered, as must vendor headers.

Generation sorts entities and records source locators, input hashes and extractor versions.
Identical inputs/tool versions yield identical Markdown and manifests even if the input tree moves.
Duplicate JSON keys or canonical identities, conflicts, missing files, invalid encoding, escaping
paths, broken links and invalid HEDG edges fail. The route is index → RCC → GPIO → USART → NVIC.

Output is staged, validated and atomically published on the same filesystem. Each complete
Markdown file is preserved completely without a fixed publication byte ceiling. No table is
truncated or silently split. Published Markdown remains the runtime knowledge source.

## Verification limits

[tests/test_f407_ingestion.py](../tests/test_f407_ingestion.py) covers declaration completeness,
determinism across paths, arrays, masks, reset handling, provenance, target identity, invalid inputs
and exact topology retrieval. Real ARM GCC assertions check every extracted offset and array size;
a wrong offset must fail. Real MCP protocol tests serve F407 alongside independent F401/AVR sessions.

These checks do not qualify a board or execute F407 firmware. The unprovisioned Podman lock has
no F407 header inventory; sandbox verification needs a separately pinned F407 lock. The command
builder now explicitly selects `STM32F407xx` instead of the F401 device definition.
