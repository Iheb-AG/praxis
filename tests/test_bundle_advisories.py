"""Published mistakes are blocked without editing historical evidence."""

import shutil

import pytest

from praxis.bundle import Bundle
from praxis.errors import PraxisError
from praxis.routing import Session
from tools.release_check import bundle_revisions
from conftest import ROOT


@pytest.mark.parametrize('name', ['stm32f407g-disc1-e01-discovery-v1',
    'stm32f407g-disc1-e01-discovery-v2', 'stm32f407g-disc1-e01-uart-v1'])
def test_old_crc_publication_is_blocked_but_rcc_still_usable(name):
    session = Session(Bundle(ROOT / 'bundles' / name))
    session.read_wiki_index()
    session.read_peripheral_doc('rcc')
    with pytest.raises(PraxisError, match='SUPERSEDED_KNOWLEDGE.*PRAXIS-2026-001'):
        session.read_peripheral_doc('crc')
    assert 'crc' not in session.served
    assert session.read_peripheral_doc('rcc')


def test_corrected_crc_is_not_blocked():
    session = Session(Bundle(ROOT / 'bundles/stm32f407g-disc1-e01-features-v1'))
    session.read_wiki_index()
    session.read_peripheral_doc('rcc')
    assert '32-bit transaction' in session.read_peripheral_doc('crc')


def test_release_gate_discovers_added_bundles(tmp_path):
    original = ROOT / 'bundles/atmega328p'
    shutil.copytree(original, tmp_path / 'first')
    shutil.copytree(original, tmp_path / 'newly-added')
    assert set(bundle_revisions(tmp_path)) == {'first', 'newly-added'}


def test_release_gate_rejects_a_corrupt_shipped_bundle(tmp_path):
    (tmp_path / 'unfinished').mkdir()
    with pytest.raises((PraxisError, OSError)):
        bundle_revisions(tmp_path)
