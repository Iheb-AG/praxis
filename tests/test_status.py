"""Status must not transfer historical evidence or certify the current checkout."""
import json
import shutil

import pytest

from conftest import ROOT
from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.status import generate, markdown


@pytest.fixture
def registry(tmp_path):
    spec = json.loads((ROOT / 'current-status.json').read_bytes())
    shutil.copytree(ROOT / spec['bundle'], tmp_path / spec['bundle'])
    for name in [spec['review'], *(row['path'] for row in spec['evidence'])]:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, path)
    path = tmp_path / 'current-status.json'
    path.write_text(json.dumps(spec))
    return path


def test_generated_public_snapshot_is_current_and_deterministic():
    report = generate(ROOT / 'current-status.json')
    assert markdown(report) == (ROOT / 'docs/CURRENT_STATUS.md').read_text()
    assert report == generate(ROOT / 'current-status.json')
    assert report['overall_mcu_completion_percent'] is None
    assert not report['release_qualified']
    assert report['current_checkout_regression'] == 'not_assessed'
    assert report['independent_review']['selected_bundle_record'] == 'missing'
    physical = next(row for row in report['evidence'] if row['kind'] == 'physical')
    assert not physical['applies_to_selected_bundle']
    assert physical['recorded_values']['reported_trial_passed'] is True
    assert all(row['applies_to_selected_bundle'] for row in report['evidence'] if row['kind'] != 'physical')


@pytest.mark.parametrize('fault,code', [('hash', 'EVIDENCE_HASH_MISMATCH'),
    ('revision', 'STATUS_REVISION_MISMATCH'), ('duplicate', 'DUPLICATE_IDENTITY'),
    ('locator', 'INVALID_STATUS_FIELD'), ('traversal', 'INVALID_PATH'),
    ('format', 'INVALID_STATUS_EVIDENCE')])
def test_invalid_or_stale_registry_fails_closed(registry, fault, code):
    spec = json.loads(registry.read_bytes())
    if fault == 'hash':
        spec['evidence'][0]['sha256'] = '0' * 64
    elif fault == 'revision':
        spec['bundle_revision'] = '0' * 64
    elif fault == 'duplicate':
        spec['evidence'].append(spec['evidence'][0])
    elif fault == 'locator':
        spec['evidence'][0]['fields']['unknown'] = ['missing', 'fact']
    elif fault == 'traversal':
        spec['evidence'][0]['path'] = '../outside.json'
    else:
        spec['evidence'][0]['format'] = 'wrong'
    registry.write_text(json.dumps(spec))
    with pytest.raises(PraxisError, match=code):
        generate(registry)


def test_matching_hash_cannot_hide_target_conflict(registry):
    spec = json.loads(registry.read_bytes())
    entry = next(e for e in spec['evidence'] if e['kind'] == 'software')
    path = registry.parent / entry['path']
    value = json.loads(path.read_bytes())
    value['target'] = 'another_mcu'
    path.write_text(json.dumps(value))
    entry['sha256'] = digest(path.read_bytes())
    registry.write_text(json.dumps(spec))
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        generate(registry)


def test_review_of_other_revision_is_not_promoted(registry):
    review = registry.parent / 'release-review.json'
    review.write_text(json.dumps({'schema_version': 1, 'status': 'independently-reviewed',
        'reviewer': 'test-only', 'bundle_revisions': {'other': '0' * 64}}))
    assert generate(registry)['independent_review']['selected_bundle_record'] == 'missing'


def test_physical_report_requires_exact_artifact_identity(registry):
    spec = json.loads(registry.read_bytes())
    entry = next(e for e in spec['evidence'] if e['kind'] == 'physical')
    path = registry.parent / entry['path']
    value = json.loads(path.read_bytes())
    del value['elf_sha256']
    path.write_text(json.dumps(value))
    entry['sha256'] = digest(path.read_bytes())
    registry.write_text(json.dumps(spec))
    with pytest.raises(PraxisError, match='Physical evidence must identify'):
        generate(registry)


def test_status_cli_reports_failure_and_preserves_evidence(registry, capsys):
    from praxis.cli import main
    assert main(['status', '--registry', str(registry)]) == 0
    assert json.loads(capsys.readouterr().out)['format'] == 'praxis-current-status-v1'
    spec = json.loads(registry.read_bytes())
    evidence = registry.parent / spec['evidence'][0]['path']
    evidence.write_bytes(evidence.read_bytes() + b' ')
    assert main(['status', '--registry', str(registry)]) == 2
    assert 'EVIDENCE_HASH_MISMATCH' in capsys.readouterr().err
