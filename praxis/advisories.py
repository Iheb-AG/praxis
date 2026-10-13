"""Known publication defects keyed by immutable revision, not target guesses.

Historical bundles remain byte-identical. Affected documents must not silently
continue serving a fact whose source interpretation has been disproved.
"""

CRC_RESET_REVISIONS = frozenset({
    '5335ed3d1d4efca3960e5cccfb8f9f30800a59d6fd2c14f3d3c309409dd09f4c',
    '84939f75664926a15854c881419d20d807ba7f93d98745ab0ac853e281ed9635',
    '1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b',
})

CRC_RESET_NOTICE = (
    'PRAXIS-2026-001: the CRC document in this revision incorrectly inferred '
    'the CR reset value from the CRC_CR_RESET command-bit macro. CRC retrieval '
    'is blocked. Select the separately reviewed stm32f407g-disc1-e01-features-v1 '
    'bundle for CRC work. Other documents and historical UART evidence retain '
    'their original revision; see docs/bundle-advisories.md.'
)

SYSTICK_PENDING_REVISION = 'e60c26a7ba6580c5ec8fcf98fbbeb1ba470b86d252242d19c3a62507db06e5d7'
SYSTICK_PENDING_NOTICE = (
    'PRAXIS-2026-002: this initial ARM core revision does not explicitly require '
    'polling to reject a pre-existing pending SysTick exception. TICKINT=0 or '
    'clearing VAL does not establish that pending state is absent. SysTick '
    'retrieval is blocked; select stm32f407g-disc1-e01-arm-core-v2. '
    'No image based on this initial revision was flashed. See docs/arm-core-support.md.'
)


def document_advisory(revision: str, peripheral: str) -> str | None:
    if revision == SYSTICK_PENDING_REVISION and peripheral == 'systick':
        return SYSTICK_PENDING_NOTICE
    if revision in CRC_RESET_REVISIONS and peripheral == 'crc':
        return CRC_RESET_NOTICE
    return None


def session_advisory(revision: str) -> str:
    if revision == SYSTICK_PENDING_REVISION:
        return SYSTICK_PENDING_NOTICE
    return CRC_RESET_NOTICE if revision in CRC_RESET_REVISIONS else ''
