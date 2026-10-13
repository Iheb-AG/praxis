# Milestone 1 acceptance and closure

Milestone 1's v1 scope includes deterministic offline ingestion, reviewed manual imports, canonical
Markdown publication and validation. Automatic PDF schematic geometry recognition remains deferred;
the reviewed transcription adapter is explicit about this boundary. The STM32F401RE and ATmega328P
KiCad fixtures remain illustrative partial boards, not complete electrical reference designs.

The additional STM32F407G-DISC1 bundle supplies a source-backed MB997 E-01 LED/button subset.
It is separate from all example bundles and does not establish the user's unknown PCB revision.

| Acceptance requirement | Evidence |
| --- | --- |
| Byte-identical artifacts from identical inputs/tools | Cross-location compiler tests for STM32, AVR and the Discovery reference |
| Canonical identities, complete tables, links and acyclic HEDG | Compiler and bundle validators; corrupt/oversized/duplicate fixtures |
| Provenance for published hardware facts | Hash-registered inputs, reviewed records and component/pin/net/fact source locators |
| Header layouts and masks preserved | Clang layouts, AVR address decoding, CMSIS discovery and actual ARM assertions |
| Native KiCad connectivity preserved | Live export comparisons and native-profile compilation for both KiCad fixtures |
| Safe topology parsing | Entity rejection, source-registration checks, package/pin matching and distinct-net checks |
| Resolved Device Tree relationships | Real dtc/overlay/libfdt tests and dangling-reference failures |
| Invalid required board facts block publication | Wrong pins, polarity, pulls, disconnected paths, open bridges and unresolved timing tests |
| Failed imports preserve existing revisions | Immutable publication and rejection tests |
| Runtime needs no ingestion tools or source tree | Copied-bundle subprocess tests forbid ingestion imports, network and subprocess execution |
| Independent release review | Tracked separately; passing Milestone 1 does not certify hardware or close the v1 release gate |

## Run the gate

Install the `ingest`, `test` and `web` extras plus Clang, ARM/AVR GCC, dtc, fdtoverlay, libfdt
and KiCad 9+. These are acceptance-test dependencies, not runtime server requirements.

```bash
.venv/bin/python tools/milestone1_check.py
```

The command writes `.praxis-output/milestone1/report.json`. Missing tools are blockers,
not passing skips. Exit status is 0 only when the Milestone 1 implementation checks pass;
otherwise it is 2. CI uploads the report even on failure. The report separately records
independent review status and explicitly states that implementation acceptance is not v1
release readiness.

## Independent review record

Reviewed manual inputs and source-located editorial facts are required for v1 ingestion and are
included in the bundle. An implementing agent's editorial review does not constitute independent
engineering sign-off. The existing `release-review.json` and `tools/release_check.py` track that
separate release qualification. Any review of additional board bundles must also identify the
exact revisions and scope it covers.

After actually reviewing the sources, extracted topology, supported operating facts and generated
documents, an independent reviewer can record the revisions and basis:

```json
{
  "status": "independently-reviewed",
  "reviewer": "Actual reviewer identity",
  "basis": "Specific sources, workflows, limitations and corrections reviewed",
  "bundle_revisions": {
    "stm32f401re": "COPY_EXACT_REVISION_FROM_REPORT",
    "atmega328p": "COPY_EXACT_REVISION_FROM_REPORT",
    "stm32f407vgt6": "COPY_EXACT_REVISION_FROM_REPORT",
    "stm32f407g-disc1-e01-m1": "COPY_EXACT_REVISION_FROM_REPORT"
  }
}
```

Changing any bundle invalidates a review of its previous revision. Automatic tests cannot
substitute for independent review. Physical testing is recorded separately and is not inferred
from schematic review or successful compilation. Full linking, sandbox qualification and
hardware execution remain outside Milestone 1's implementation acceptance.
