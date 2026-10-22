"""Deterministic, revision-bound support and recorded-evidence summary.

Evidence digests establish which report is summarized, not truth or independent
approval. Historical software results never certify the current source checkout.
"""
from pathlib import Path
import re
from typing import Literal

from pydantic import Field

from praxis.bundle import Bundle, digest, read_inside, relative_path
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Record
from praxis.support import assess


class Evidence(Record):
    path: str
    sha256: str = Field(pattern='^[0-9a-f]{64}$')
    format: str
    kind: Literal['software', 'retrieval', 'physical']
    # Exact dictionary paths select recorded values; no expressions or interpretation.
    fields: dict[str, list[str]] = Field(min_length=1, max_length=32)


class Registry(Record):
    format: Literal['praxis-status-registry-v1']
    bundle: str
    bundle_revision: str = Field(pattern='^[0-9a-f]{64}$')
    review: str
    evidence: list[Evidence] = Field(max_length=64)


def select(record, path):
    if not path or len(path) > 16:
        raise PraxisError('INVALID_STATUS_FIELD', 'Select a nonempty dictionary path of at most 16 keys')
    value = record
    for key in path:
        if not isinstance(value, dict) or key not in value:
            raise PraxisError('INVALID_STATUS_FIELD', 'Missing recorded evidence field: ' + '.'.join(path))
        value = value[key]
    return value


def generate(registry_path: Path) -> dict:
    root = registry_path.absolute().parent
    registry_bytes = read_inside(root, registry_path.name, 1024 * 1024)
    spec = Registry.model_validate(load_json(registry_bytes))
    bundle_path = root / relative_path(spec.bundle)
    if not bundle_path.resolve().is_relative_to(root.resolve()):
        raise PraxisError('INVALID_PATH', 'Status bundle escapes registry root')
    bundle = Bundle(bundle_path)
    if bundle.manifest.bundle_revision != spec.bundle_revision:
        raise PraxisError('STATUS_REVISION_MISMATCH', 'Selected bundle changed; explicitly update the status registry')
    support = assess(bundle)
    records, paths = [], set()
    for entry in spec.evidence:
        if entry.path in paths:
            raise PraxisError('DUPLICATE_IDENTITY', 'Each evidence file may appear only once')
        paths.add(entry.path)
        raw = read_inside(root, entry.path, 16 * 1024 * 1024)
        if digest(raw) != entry.sha256:
            raise PraxisError('EVIDENCE_HASH_MISMATCH', f'Recorded evidence changed: {entry.path}')
        data = load_json(raw)
        if not isinstance(data, dict) or data.get('format') != entry.format:
            raise PraxisError('INVALID_STATUS_EVIDENCE', f'Unexpected evidence format: {entry.path}')
        revision = data.get('bundle_revision')
        if not isinstance(revision, str) or len(revision) != 64 or any(c not in '0123456789abcdef' for c in revision):
            raise PraxisError('INVALID_STATUS_EVIDENCE', 'Evidence must identify its exact bundle revision')
        if revision == spec.bundle_revision and 'target' in data:
            if data['target'] != bundle.manifest.target.id:
                raise PraxisError('TARGET_MISMATCH', 'Evidence target disagrees with selected bundle')
        artifact = data.get('artifact', data)
        identity = {key: artifact[key] for key in ('artifact_id', 'elf_sha256', 'image_sha256')
                    if isinstance(artifact, dict) and key in artifact}
        if entry.kind == 'physical' and len(identity) != 3:
            raise PraxisError('INVALID_STATUS_EVIDENCE', 'Physical evidence must identify artifact, ELF and image')
        if any(not isinstance(v, str) or re.fullmatch('[0-9a-f]{64}', v) is None for v in identity.values()):
            raise PraxisError('INVALID_STATUS_EVIDENCE', 'Invalid artifact identity')
        if isinstance(artifact, dict) and artifact.get('bundle_revision', revision) != revision:
            raise PraxisError('INVALID_STATUS_EVIDENCE', 'Artifact and report bundle revisions disagree')
        records.append({'path': entry.path, 'sha256': entry.sha256, 'kind': entry.kind,
            'bundle_revision': revision, 'applies_to_selected_bundle': revision == spec.bundle_revision,
            'artifact_identity': identity,
            'recorded_values': {label: select(data, locator) for label, locator in entry.fields.items()},
            'limits': data.get('limits', []), 'verification': 'recorded_report_not_reexecuted'})
    review_raw = read_inside(root, spec.review, 1024 * 1024)
    review = load_json(review_raw)
    if (not isinstance(review, dict) or review.get('schema_version') != 1
            or not isinstance(review.get('bundle_revisions'), dict)):
        raise PraxisError('INVALID_STATUS_REVIEW', 'Expected a release-review record')
    review_present = (review.get('status') == 'independently-reviewed'
                      and isinstance(review.get('reviewer'), str) and bool(review['reviewer'].strip())
                      and spec.bundle_revision in review['bundle_revisions'].values())
    return {'format': 'praxis-current-status-v1', 'registry_sha256': digest(registry_bytes),
        'bundle': spec.bundle, 'bundle_revision': spec.bundle_revision, 'target': support['target'],
        'knowledge': {'metrics': support['metrics'], 'reviewed_mode_contracts': support['reviewed_mode_contracts'],
                      'workflows': support['workflows']},
        'evidence': records, 'independent_review': {
            'path': spec.review, 'sha256': digest(review_raw),
            'selected_bundle_record': 'present' if review_present else 'missing',
            'identity_authentication': 'not_assessed'},
        'release_qualified': False, 'current_checkout_regression': 'not_assessed',
        'overall_mcu_completion_percent': None,
        'limits': ['Knowledge readiness is limited to authored workflows, not all MCU features.',
                   'Evidence counts are historical reported results, never summed or transferred between revisions.',
                   'A matching bundle does not establish matching application, toolchain or current source code.',
                   'Physical records apply only to their exact artifacts and fixtures; no whole-workflow qualification is inferred.',
                   'Independent review records are declarations, not authenticated signatures; release qualification is separate.']}


def markdown(report: dict) -> str:
    import json
    # JSON quoting inside fences keeps imported report text from becoming links/HTML.
    lines = ['# Current supported baseline', '',
        'Generated from `current-status.json`; regenerate with `praxis status --registry current-status.json --format markdown`.',
        '', '**Experimental alpha. Full MCU acceptance and qualified release are not established.**', '',
        f"Selected bundle: `{report['bundle']}`", f"Revision: `{report['bundle_revision']}`", '',
        '## Knowledge scope', '']
    for name, value in report['knowledge']['metrics'].items():
        lines.append(f"- {name}: **{value['numerator']}/{value['denominator']}** — {value['scope']}")
    lines += [f"- Reviewed mode contracts: **{report['knowledge']['reviewed_mode_contracts']}**", '',
              '## Authored workflows', '', '| Workflow | Knowledge state |', '| --- | --- |']
    for name, row in report['knowledge']['workflows'].items():
        lines.append(f"| `{name}` | {'Ready within authored scope' if row['knowledge_ready'] else 'Blocked'} |")
    lines += ['', 'Exact missing requirements and scopes are included in the JSON status output.', '',
              '## Recorded verification evidence', '',
              'These are historical reports, not tests rerun against the current checkout. Counts are not added together.', '']
    for record in report['evidence']:
        applies = 'Selected bundle' if record['applies_to_selected_bundle'] else 'Different historical bundle — does not qualify this baseline'
        lines += [f"### {record['kind']} evidence", '', f'**{applies}**', '', '```json',
                  json.dumps(record, sort_keys=True, indent=2).replace('`', '\\u0060'), '```', '']
    lines += ['## Independent review and limits', '',
        f"Independent review record for selected bundle: **{report['independent_review']['selected_bundle_record']}**.",
        'Current-checkout full regression: **not assessed by this command**.', '']
    lines += ['- ' + limit for limit in report['limits']]
    return '\n'.join(lines) + '\n'
