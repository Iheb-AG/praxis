"""Authoring MCP evidence isolation, provenance, complete parts and publication policy."""
import asyncio
import json
import shutil
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.errors import PraxisError
from praxis.ingestion_server import IngestionService
from praxis.web_import import WebSource, scrape
from conftest import ROOT, require_tool


@pytest.fixture
def service(tmp_path):
    root = tmp_path / 'sources'
    shutil.copytree(ROOT / 'sources/stm32f407g-disc1', root, ignore=shutil.ignore_patterns("imports"))
    text = tmp_path / 'manual.txt'
    text.write_text('TIM2 requires clocks before access.\nLiteral [query] must not execute.\n')
    source = WebSource(id='manual', target='STM32F407VGT6', url='https://example.org/manual', kind='text')
    archive = scrape(source, tmp_path / 'existing', from_file=text)
    catalog = tmp_path / 'catalog.json'
    catalog.write_text(json.dumps(dict(schema_version=1, allowed_hosts=['example.org'],
                                      sources=[source.model_dump()])))
    return IngestionService(root / 'profile-discovery.json', catalog,
                            tmp_path / 'acquired', tmp_path / 'published', [archive])


def test_evidence_search_read_snapshot_and_provenance(service):
    data = service.describe()
    assert data['archives'][0]['source_sha256']
    hit = service.search('manual', '[query]', 1)
    assert hit['matches'] == 1 and not hit['more']
    evidence = service.read('manual', hit['hits'][0]['locator'])
    assert evidence['source_sha256'] and evidence['artifact_sha256']
    assert 'not instructions' in evidence['status']
    assert 'TIM2 requires clocks' in evidence['evidence']['text']
    (service.archives['manual']['root'] / evidence['artifact']).write_text('corrupt')
    assert service.read('manual', evidence['locator']) == evidence  # fixed in-memory evidence
    with pytest.raises(PraxisError, match='IMPORT_INTEGRITY'):
        service._load_archive(service.archives['manual']['root'])


def test_profile_exposes_exact_composed_parent_hash_without_header_extraction(service):
    from praxis.definitions import definitions_digest, load_definitions
    expected = definitions_digest(load_definitions(service.profile,
        {s.id: service.root / s.path for s in service.profile.sources}))
    assert service.describe()['composed_definitions_sha256'] == expected
    assert service._declaration_snapshot is None


def test_parent_hash_cannot_describe_changed_sources(service):
    path = service.root / service.profile.sources[0].path
    path.write_bytes(path.read_bytes() + b'\n')
    with pytest.raises(PraxisError, match='SOURCE_CHANGED'):
        service.describe()


def test_registered_line_ranges_and_unknown_inputs(service):
    hits = service.search('header', 'TIM2_IRQn', 2)
    assert hits['matches'] >= 1
    part = service.read('header', hits['hits'][0]['locator'])
    assert 'TIM2_IRQn' in part['text'] and part['source_sha256']
    for operation in [lambda: service.read('header', '../etc/passwd'),
                      lambda: service.read('header', 'lines:1-999'),
                      lambda: service.read('unknown', 'page:1'),
                      lambda: service.search('manual', '', 2),
                      lambda: service.search('manual', 'TIM2', 100),
                      lambda: service.acquire('../manual', None),
                      lambda: service.publish('../profile.json', 'escape'),
                      lambda: service.publish('profile.json', '../escape')]:
        with pytest.raises(PraxisError):
            operation()


def test_publication_uses_compiler_and_target_check(service, monkeypatch):
    import praxis.compiler
    def block(*args):
        raise PraxisError('PUBLICATION_BLOCKED', 'required operating evidence absent')
    monkeypatch.setattr(praxis.compiler, 'compile_bundle', block)
    with pytest.raises(PraxisError, match='PUBLICATION_BLOCKED'):
        service.publish('profile-discovery.json', 'candidate')
    assert not service.publication_root.exists()
    path = service.root / 'wrong.json'
    data = json.loads(service.profile_path.read_text())
    data['target']['board_revision'] = 'another revision'
    path.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        service.publish('wrong.json', 'candidate')


def test_review_is_exact_and_restricted_to_authoring_archives(service):
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        service.record_review('manual', 'Reviewed actual evidence')
    service.stage_cached('manual', None, 'manual_review')
    result = service.record_review('manual_review', 'Read both source lines; test fixture only; no hardware facts approved.')
    assert result['review_sha256'] and 'not independent' in result['status']
    assert service.record_review('manual_review', 'Read both source lines; test fixture only; no hardware facts approved.') == result
    with pytest.raises(PraxisError, match='IMMUTABLE_REVIEW'):
        service.record_review('manual_review', 'Different notes')
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        service.stage_cached('manual', None, '../escape')


async def test_actual_stdio_tools_and_errors(service, tmp_path):
    require_tool('arm-none-eabi-gcc')
    data = json.loads(service.profile_path.read_text())
    data['workflows']['feature_adc'] = dict(peripherals=['adc'],
        registers={'adc': ['CR1', 'CR2']}, instances={'adc': ['ADC1']},
        modes={'adc': ['single_conversion']})
    service.profile_path.write_text(json.dumps(data))
    params = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'ingest-serve',
        '--profile', str(service.profile_path), '--catalog', str(tmp_path / 'catalog.json'),
        '--archive-root', str(service.archive_root), '--publication-root', str(service.publication_root),
        '--evidence-archive', str(service.archives['manual']['root'])], cwd=str(tmp_path))
    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            names = {tool.name for tool in (await client.list_tools()).tools}
            assert names == {'get_ingestion_profile', 'search_source_evidence', 'read_source_evidence',
                             'acquire_source_evidence', 'publish_reviewed_bundle',
                             'stage_cached_source', 'record_source_review', 'discover_source_declarations',
                             'read_source_page_image', 'prepare_peripheral_review', 'prepare_workflow_review'}
            result = await client.call_tool('search_source_evidence', {'source_id': 'manual', 'query': 'TIM2'})
            assert not result.isError
            result = await client.call_tool('read_source_evidence', {'source_id': 'manual', 'locator': '../source.txt'})
            assert result.isError and 'UNKNOWN_LOCATOR' in result.content[0].text
            result = await client.call_tool('prepare_peripheral_review', {'source_id': 'manual',
                'peripheral_name': 'tim', 'register_names': ['CR1']})
            assert not result.isError
            payload = result.structuredContent or json.loads(result.content[0].text)
            payload = payload.get('result', payload)
            assert payload['review_required'] and not payload['publication_ready']
            assert payload['counts']['candidates'] == 0  # Unrelated prose must not become facts.
            result = await client.call_tool('prepare_workflow_review', {
                'source_id': 'manual', 'workflow_name': 'feature_adc'})
            assert not result.isError
            packet = result.structuredContent or json.loads(result.content[0].text)
            packet = packet.get('result', packet)
            assert packet['scope']['retrieval_order'] == ['rcc', 'adc']
            assert packet['scope']['unresolved'] and packet['review_required']
            assert not packet['publication_ready'] and packet['status'] == 'pending-review'
            assert set(packet['peripherals']) == {'adc', 'rcc'}
            result = await client.call_tool('prepare_workflow_review', {
                'source_id': 'manual', 'workflow_name': 'feature_adc',
                'evidence_locators': {'gpio': ['text']}})
            assert result.isError and 'INVALID_INPUT' in result.content[0].text
            result = await client.call_tool('prepare_peripheral_review', {'source_id': 'manual',
                'peripheral_name': 'tim', 'evidence_locators': ['../source.txt']})
            assert result.isError and 'UNKNOWN_LOCATOR' in result.content[0].text
    await asyncio.wait_for(exercise(), 60)


def test_pdf_full_tables_image_and_changed_bytes(service, tmp_path):
    import base64
    import io
    from PIL import Image
    from test_web_import import make_pdf
    path = tmp_path / 'source.pdf'
    make_pdf(path)
    spec = WebSource(id='drawing', target='STM32F407VGT6', url='https://example.org/drawing', kind='pdf')
    archive = scrape(spec, service.archive_root / 'drawing', from_file=path)
    service._load_archive(archive)
    evidence = service.read('drawing', 'page:1')
    assert evidence['evidence']['tables'][0]['rows'] == [['Register', 'Offset'], ['CR1', '0x0C']]
    assert service.read('drawing', 'page:2')['artifact'] == 'extracted/part-0002.json'
    result = service.page_image('drawing', 1)
    assert evidence['source_sha256'] in result[0].text
    with Image.open(io.BytesIO(base64.b64decode(result[1].data))) as image:
        assert max(image.size) <= 1800 and image.format == 'PNG'
    with pytest.raises(PraxisError, match='UNKNOWN_LOCATOR'):
        service.page_image('drawing', 3)
    (archive / 'source.pdf').write_bytes(b'changed')
    with pytest.raises(PraxisError, match='IMPORT_INTEGRITY'):
        service.page_image('drawing', 1)


def test_symlink_authoring_and_publication_paths_rejected(service, tmp_path):
    service.archive_root.mkdir()
    outside = tmp_path / 'outside'
    outside.mkdir()
    (service.archive_root / 'manual_review').symlink_to(outside, target_is_directory=True)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        service.stage_cached('manual', None, 'manual_review')
    service.publication_root.mkdir()
    (service.publication_root / 'escape').symlink_to(outside, target_is_directory=True)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        service.publish('profile-discovery.json', 'escape')
    assert not list(outside.iterdir())


def test_declaration_cache_checks_every_registered_source(service, monkeypatch):
    import praxis.coverage
    calls = []
    monkeypatch.setattr(praxis.coverage, 'inventory', lambda *args: calls.append(args) or ({}, {}))
    for _ in range(2):
        with pytest.raises(PraxisError, match='UNKNOWN_PERIPHERAL'):
            service.discover('absent')
    assert len(calls) == 1
    (service.root / service.profile.sources[0].path).write_text('changed after snapshot')
    with pytest.raises(PraxisError, match='SOURCE_CHANGED'):
        service.discover('absent')
    assert service._declaration_snapshot is None and len(calls) == 1


def test_changed_profile_invalidates_declaration_cache(service, monkeypatch):
    import praxis.coverage
    monkeypatch.setattr(praxis.coverage, 'inventory', lambda *args: ({}, {}))
    with pytest.raises(PraxisError, match='UNKNOWN_PERIPHERAL'):
        service.discover('absent')
    service.profile_path.write_text(service.profile_path.read_text() + '\n')
    with pytest.raises(PraxisError, match='SOURCE_CHANGED'):
        service.discover('absent')
    assert service._declaration_snapshot is None


def test_review_cli_and_ingestion_share_exact_packet(service, monkeypatch, tmp_path, capsys):
    from praxis.adapters.discovery import Declaration
    from praxis.cli import main
    from praxis.models import Register
    from praxis.review import prepare_review
    import praxis.coverage
    import praxis.review
    declaration = Declaration(structure='SYNTHETIC_Type', instances={}, members={'CR': 'CR'},
        field_expressions={}, registers=[Register(name='CR', offset=0, width=32, access='unknown',
            side_effects='Synthetic only', sources=[dict(source='header', locator='synthetic')])])
    catalog = ({'synthetic': declaration}, {'synthetic': {'status': 'declarations_only'}})
    monkeypatch.setattr(praxis.coverage, 'inventory', lambda *args: catalog)
    monkeypatch.setattr(praxis.review, 'inventory', lambda *args: catalog)
    path = tmp_path / 'evidence.txt'
    path.write_text('Control (SYNTHETIC_CR)\nAddress offset: 0\nAccess: RW\nReset value: 0\n')
    source = WebSource(id='synthetic', target='STM32F407VGT6', url='https://example.org/test', kind='text')
    archive = scrape(source, tmp_path / 'synthetic', from_file=path)
    service._load_archive(archive)
    mcp_packet = service.prepare_review('synthetic', 'synthetic')
    cli_packet = prepare_review(service.profile_path, archive, 'synthetic')
    assert cli_packet == mcp_packet and cli_packet['counts']['candidates'] == 3
    output = tmp_path / 'packet.json'
    args = ['prepare-review', '--profile', str(service.profile_path), '--archive', str(archive),
            '--peripheral', 'synthetic', '--output', str(output)]
    assert main(args) == 0 and json.loads(output.read_text()) == mcp_packet
    assert main(args) == 2  # Existing review output cannot be overwritten.
    capsys.readouterr()
    with pytest.raises(PraxisError, match='UNKNOWN_SOURCE'):
        service.prepare_review('unregistered', 'synthetic')
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        service.prepare_review('synthetic', '../synthetic')
    wrong = WebSource(id='wrong', target='ATmega328P', url='https://example.org/test', kind='text')
    wrong_archive = scrape(wrong, tmp_path / 'wrong', from_file=path)
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        prepare_review(service.profile_path, wrong_archive, 'synthetic')
