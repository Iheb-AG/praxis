"""A public status snapshot must work without ignored local evidence files."""
import json

import pytest

from conftest import ROOT
from tools.check_distribution import status_inputs


def test_public_status_uses_only_public_inputs():
    assert status_inputs(lambda name: (ROOT / name).read_bytes()) == 2
    spec = json.loads((ROOT / 'current-status.json').read_bytes())
    assert all('benchmark' not in row['path'] and 'demo' not in row['path'] for row in spec['evidence'])


@pytest.mark.parametrize('fault', ['missing', 'modified', 'escaped'])
def test_status_dependency_failures_block_archive(fault):
    def read(name):
        if name == 'current-status.json' and fault == 'escaped':
            spec = json.loads((ROOT / name).read_bytes())
            spec['evidence'][0]['path'] = '../private-evidence.json'
            return json.dumps(spec).encode()
        if name == 'docs/timer-irq-evidence.json':
            if fault == 'missing':
                raise ValueError('Missing packaged status input')
            if fault == 'modified':
                return (ROOT / name).read_bytes() + b' '
        return (ROOT / name).read_bytes()

    with pytest.raises(ValueError, match='Missing|pin mismatch|Invalid status input path'):
        status_inputs(read)
