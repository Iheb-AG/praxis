# Scoped ARM core evidence resolutions

Source: ST PM0214 Rev10, acquired and read through the Praxis ingestion MCP on2026-10-13.
Exact input PDF SHA-256: fb54012a46c674a26dee56bc8cdfa281315f78634f18998001144980b08d1b03.
The author inspected complete text pages and MCP-rendered diagrams at227,234,248,251.
This is implementing-author editorial review; independent review is pending.

| Issue | Evidence | Reviewed resolution |
| --- | --- | --- |
| SysTick reset/calibration contradictions | pp246-251 summary, detailed reset lines, design hints and rendered table | Leave every SysTick reset unasserted; program LOAD/VAL/CTRL; never use CALIB to derive timing |
| VTOR shared mask broader than device | CMSIS TBLOFF bits31:7; PM0214 p227 diagram/text bits29:9; p40 general range broader | Retain the header declaration envelope, publish the stricter write-value mask0x3FFFFE00 and512-byte alignment, and support only the pinned table0x08000000 |
| VECTPENDING shared mask broader than device | Header bits20:12 versus p226 bits18:12 | Do not use this field in the supported mode; retain declarations without reviewed operating semantics |
| SHP array versus SHPR word registers | CMSIS twelve byte array at0x18; pp233-234 three word views | Preserve the array/stride; SysTick PRI_15 is byte11 at0x23; write only that byte and preserve PendSV |
| Priority wording inconsistent | p233 prose versus p234 diagram and device __NVIC_PRIO_BITS=4 | Use four high bits from the exact F407 declaration, supported priority0..15, byte encoding priority<<4 |
| Reload0 and single-shot wording | p248 | Support periodic operation only, cycles2..16777216, LOAD=cycles-1; no one-shot interpretation inferred |

These resolutions do not change vendor headers or erase extraction conflicts. Required operating
facts are narrowed to the reviewed subset; contradictory reset/calibration facts are not required.
