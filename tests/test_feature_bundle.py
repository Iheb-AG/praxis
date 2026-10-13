"""Published mode contracts are narrower than header availability or hardware support."""

import json

from praxis.bundle import Bundle
from praxis.cli import main
from praxis.coverage import workflow_coverage
from praxis.features import from_bundle
from praxis.models import Peripheral, Profile
from conftest import ROOT

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-features-v1'
SOURCE = ROOT / 'sources/stm32f407g-disc1'


def test_published_feature_report_discloses_actual_scope(capsys):
    bundle = Bundle(BUNDLE)
    report = from_bundle(bundle)
    assert report['counts']['register_blocks'] == 42
    assert report['counts']['reviewed_mode_contracts'] == 7
    assert report['counts']['blocks_without_mode_contracts'] == 35
    assert report['all_features_supported'] is False
    assert report['features']['itm']['published'] is False
    assert report['features']['i2c']['reviewed_modes'] == {}
    assert main(['features', '--bundle', str(BUNDLE)]) == 0
    assert json.loads(capsys.readouterr().out) == report


def test_dma1_cannot_inherit_dma2_memory_copy_support():
    profile = Profile.model_validate_json((SOURCE / 'profile-features-v1.json').read_text())
    items = [Peripheral.model_validate(d) for d in json.loads(
        (SOURCE / 'reviewed/features-v1/peripherals.json').read_text())]
    requirement = profile.workflows['dma2_memory_copy']
    wrong = requirement.model_copy(update={'instances': {'dma_stream': ['DMA1_Stream0'], 'dma': ['DMA1']}})
    profile = profile.model_copy(update={'workflows': {'wrong_controller': wrong}, 'publication_requires': []})
    result = workflow_coverage(profile, items, {})['wrong_controller']
    assert not result['ready']
    assert any('outside reviewed mode scope' in s for s in result['issues'])


def test_publication_readiness_keeps_wiring_and_clock_gaps_visible():
    bundle = Bundle(BUNDLE)
    coverage = json.loads(bundle.read('wiki/coverage.md').split('```json\n')[1].split('\n```')[0])
    assert coverage['workflows']['crc_word_feed']['ready']
    assert coverage['workflows']['dma2_memory_copy']['ready']
    assert not coverage['workflows']['spi1_wired_polling']['ready']
    assert any('SPI1_SCK' in s for s in coverage['workflows']['spi1_wired_polling']['issues'])
    assert not coverage['workflows']['rng_pll_polling']['ready']
    assert not coverage['workflows']['feature_flash']['ready']
    crc = bundle.read('wiki/peripherals/crc.md')
    assert '8-bit CMSIS member' in crc and '32-bit transaction' in crc
    assert 'CRC_CR_RESET_Msk' in crc and 'self-clearing' in crc
    dma = bundle.read('wiki/peripherals/dma_stream.md')
    assert 'bit 20' in dma and 'keep zero' in dma
    assert max(len(s.encode()) for s in bundle.documents.values()) <= 64 * 1024
