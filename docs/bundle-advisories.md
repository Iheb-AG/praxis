# Bundle advisories

## PRAXIS-2026-001: CRC command macro interpreted as a reset value

Recorded 2026-10-11. Older declaration-only CRC documents report CRC_CR's reset value
as `0x1`. The parser incorrectly interpreted `CRC_CR_RESET`, a command-bit alias with
`_Pos`/`_Msk` definitions, as a register reset-value macro. The source-backed review of
RM0090 Rev22 page 115 establishes a zero CR reset value; writing RESET is a self-clearing
command that reinitializes DR. This issue does not change the RESET bit mask.

Affected immutable bundle revisions:

| Bundle | Revision |
| --- | --- |
| stm32f407g-disc1-e01-discovery-v1 | `5335ed3d1d4efca3960e5cccfb8f9f30800a59d6fd2c14f3d3c309409dd09f4c` |
| stm32f407g-disc1-e01-discovery-v2 | `84939f75664926a15854c881419d20d807ba7f93d98745ab0ac853e281ed9635` |
| stm32f407g-disc1-e01-uart-v1 | `1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b` |

The corrected parser excludes named bit-field aliases from reset-value inference. The
[features-v1 bundle](../bundles/stm32f407g-disc1-e01-features-v1/wiki/peripherals/crc.md)
publishes reviewed CRC operating semantics and the correct reset value with provenance.
Current servers advertise this advisory on affected sessions and reject their CRC reads
with `SUPERSEDED_KNOWLEDGE`, directing the caller to the corrected bundle. Restart an
already-running MCP process to load this policy. Historical files remain byte-identical.

The installed UART example does not use CRC. Its existing observations remain associated
with their original bundle/image; correcting a different document is not evidence of a
UART fix. Other peripheral documents retain their prior scoped status. Direct readers of
the old Markdown must heed this advisory because files themselves cannot enforce a gate.

This is an editorial defect correction, not an independent review of every older fact.
The release checker now discovers every shipped bundle dynamically, including historical
bundles previously omitted from its fixed list; all require review before a qualified release.

## PRAXIS-2026-002: polling pending SysTick state

Recorded 2026-10-13 during the ARM extension's local modeled validation. Initial bundle
`stm32f407g-disc1-e01-arm-core-v1`, revision
`e60c26a7ba6580c5ec8fcf98fbbeb1ba470b86d252242d19c3a62507db06e5d7`,
did not explicitly require polling to reject a pre-existing pending SysTick exception.
Disabling TICKINT or writing VAL is not evidence that SCB pending state is absent.

The separate [arm-core-v2](../bundles/stm32f407g-disc1-e01-arm-core-v2/wiki/index.md)
requires checking PENDSTSET before any polling timer write. Its controller rejects an already
pending exception; IRQ setup instead clears pending through the exact SCB action. The shared
effect model covers both paths. The original revision remains unchanged and its SysTick
document is blocked with `SUPERSEDED_KNOWLEDGE`. No image from the initial revision was flashed.
This correction does not qualify physical timing or alter earlier peripheral observations.
