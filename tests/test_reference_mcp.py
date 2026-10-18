"""Generic hardware evidence over MCP without weakening MCU publication gates."""
import json
import os
import sys
from datetime import timedelta
from pathlib import Path

import httpx
import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.errors import PraxisError
from praxis.reference_server import ReferenceService
from praxis import web_import
from test_web_import import make_pdf


@pytest.fixture
def references(tmp_path, monkeypatch):
    replies = {'body': b'Operating voltage must be checked. I2C requires pull-ups.',
               'type': 'text/plain'}
    original_download = web_import.download
    monkeypatch.setattr(web_import.socket, 'getaddrinfo',
                        lambda *a, **k: [(2, 1, 6, '', ('93.184.216.34', 443))])

    def download(source, destination, allowed_hosts, **kwargs):
        with httpx.Client(transport=httpx.MockTransport(lambda request:
                httpx.Response(200, content=replies['body'],
                               headers={'content-type': replies['type']}))) as client:
            return original_download(source, destination, allowed_hosts, client=client)

    monkeypatch.setattr(web_import, 'download', download)
    return ReferenceService(tmp_path / 'library'), replies


def test_arbitrary_hardware_acquire_search_read_and_restart(references):
    service, _ = references
    for key, hardware in [('lcd', 'LCD controller model A'), ('sensor', 'distance sensor model B'),
                          ('mcu', 'non-STM32 MCU model C')]:
        result = service.acquire(key, hardware, f'https://vendor.example/{key}.txt')
        assert result['hardware'] == hardware
        assert result['source_sha256'] and result['import_revision']
        hit = service.search(key, 'I2C', 1)['hits'][0]
        evidence = service.read(key, hit['locator'])
        assert evidence['hardware'] == hardware
        assert 'pull-ups' in evidence['evidence']['text']
        assert 'unreviewed' in evidence['evidence'].get('status', '').lower() or 'Unreviewed' in evidence['status']
    assert len(ReferenceService(service.root).list_references()['references']) == 3


def test_immutable_source_selection(references):
    service, _ = references
    first = service.acquire('doc', 'part-a', 'https://vendor.example/a.txt')
    assert service.acquire('doc', 'part-a', 'https://vendor.example/a.txt') == first
    with pytest.raises(PraxisError, match='IMMUTABLE_IMPORT'):
        service.acquire('doc', 'part-b', 'https://vendor.example/b.txt')


def test_pdf_complete_pages_and_provenance(references, tmp_path):
    service, replies = references
    pdf = tmp_path / 'original.pdf'
    make_pdf(pdf)
    replies.update(body=pdf.read_bytes(), type='application/pdf')
    result = service.acquire('manual', 'arbitrary controller', 'https://vendor.example/manual.pdf', pages='1')
    assert result['locators'] == ['page:1']
    page = service.read('manual', 'page:1')
    assert page['evidence']['tables']
    assert page['source_sha256'] == result['source_sha256']
    with pytest.raises(PraxisError, match='UNKNOWN_LOCATOR'):
        service.read('manual', 'page:2')


def test_html_and_casefolded_search(references):
    service, replies = references
    replies.update(body=b'<html><body><p>Timing must be checked.</p><script>not searchable</script></body></html>',
                   type='text/html')
    service.acquire('web', 'any part', 'https://vendor.example/documentation')
    assert service.search('web', 'TIMING')['matches'] == 1
    assert service.search('web', 'not searchable')['matches'] == 0


def test_changed_archive_fails_closed(references):
    service, _ = references
    service.acquire('doc', 'part', 'https://vendor.example/doc.txt')
    path = next((service.root / 'doc' / 'extracted').glob('*.json'))
    path.write_text('{}')
    with pytest.raises(PraxisError, match='IMPORT_INTEGRITY'):
        service.search('doc', 'voltage')


def test_invalid_identity_paths_and_queries(references, tmp_path):
    service, _ = references
    for key in ['../escape', '/tmp/escape', 'bad/name']:
        with pytest.raises(PraxisError, match='INVALID_INPUT'):
            service.acquire(key, 'part', 'https://vendor.example/doc.txt')
    service.root.mkdir()
    (service.root / 'linked').symlink_to(tmp_path)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        service.acquire('linked', 'part', 'https://vendor.example/doc.txt')
    with pytest.raises(PraxisError, match='INVALID_INPUT'):
        service.search('doc', '', 20)


def test_private_network_is_still_blocked(tmp_path, monkeypatch):
    monkeypatch.setattr(web_import.socket, 'getaddrinfo',
                        lambda *a, **k: [(2, 1, 6, '', ('127.0.0.1', 443))])
    with pytest.raises(PraxisError, match='PRIVATE_ADDRESS'):
        ReferenceService(tmp_path / 'library').acquire('doc', 'part', 'https://localhost/doc.txt')


@pytest.mark.asyncio
async def test_real_stdio_discovery_and_read(tmp_path):
    library = tmp_path / 'library'
    source = tmp_path / 'manual.txt'
    source.write_text('A generic sensor reference.\n')
    web_import.scrape(web_import.WebSource(id='sensor', target='arbitrary sensor',
                     url='https://vendor.example/manual.txt', kind='text'),
                     library / 'sensor', from_file=source)
    root = Path(__file__).resolve().parents[1]
    params = StdioServerParameters(command=sys.executable,
        args=['-m', 'praxis', 'reference-serve', '--archive-root', str(library)],
        cwd=str(root), env={**os.environ, 'PYTHONPATH': str(root)})
    async with stdio_client(params) as (read, write), ClientSession(read, write, read_timeout_seconds=timedelta(seconds=15)) as session:
        await session.initialize()
        tools = await session.list_tools()
        assert {tool.name for tool in tools.tools} == {'list_hardware_references',
            'acquire_hardware_reference', 'search_hardware_reference', 'read_hardware_reference'}
        result = await session.call_tool('list_hardware_references', {})
        assert not result.isError
        data = json.loads(result.content[0].text)
        locator = data['references'][0]['locators'][0]
        result = await session.call_tool('read_hardware_reference', {'source_id': 'sensor', 'locator': locator})
        assert not result.isError
        assert 'generic sensor' in result.content[0].text
