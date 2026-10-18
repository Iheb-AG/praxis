"""Project reports preserve connectivity and evidence boundaries, rather than invent readiness."""
import asyncio
import copy
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path
from xml.etree import ElementTree

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from praxis.bundle import Bundle
from praxis.cli import main
from praxis.errors import PraxisError
from praxis.project_report import parse_spec, prepare, render, schematic, sequence_diagram, write_report
from tests.conftest import ROOT, require_image

BUNDLE = ROOT / 'bundles/stm32f407g-disc1-e01-timer-irq-v1'


@pytest.fixture(scope='module')
def reference():
    return Bundle(BUNDLE)


@pytest.fixture
def specification(reference):
    return {'format': 'praxis-project-v1', 'id': 'uart_supervisor', 'title': 'UART supervisor',
        'objective': 'A bounded protocol supervisor with a passive UART loopback jumper.',
        'target_id': reference.manifest.target.id, 'bundle_revision': reference.manifest.bundle_revision,
        'requirements': [{'id': 'protocol', 'description': 'Timer-driven UART with interrupts',
            'workflows': ['uart_timer_interrupts'], 'verification_plan': 'Check frame and error counters.'}],
        'explanations': [{'title': 'Clock route', 'explanation': 'Clock gates precede peripheral access.',
            'documents': ['peripherals/rcc']}],
        'signals': ['LED_A', 'PA2', 'PA3'],
        'proposed_wires': [{'from_endpoint': 'P1:14', 'to_endpoint': 'P1:13',
            'description': 'Fit while all board power is disconnected.'}],
        'limitations': ['The physical PCB revision and fitted wiring need operator confirmation.']}


def test_preserves_whole_nets_and_resistor_boundaries(reference, specification):
    report, files = prepare(reference, parse_spec(specification))
    assert report['knowledge_scope_ready'], report['gaps']
    nets = {n['name']: n['endpoints'] for n in report['nets']}
    assert {'PD12', 'LD4_ANODE', 'GND', 'PA2', 'PA3'} <= nets.keys()
    assert any(e['endpoint'] == 'R40:1' for e in nets['PD12'])
    assert any(e['endpoint'] == 'R40:2' for e in nets['LD4_ANODE'])
    assert all(e['sources'] for rows in nets.values() for e in rows)
    from praxis.project_report import _index
    index = _index(reference)
    for name, rows in nets.items():
        assert len(rows) == len(index.nets[name])
    assert 'references/' in next(iter(files))
    assert report['physical_verification'] == 'not_assessed'
    assert report['build'] == {'status': 'not_assessed'}
    assert not report['project_accepted']
    svg = ElementTree.fromstring(schematic(report))
    assert svg.tag.endswith('svg')


@pytest.mark.parametrize('field,value', [('target_id', 'different_board'), ('bundle_revision', '0' * 64)])
def test_wrong_target_or_revision_fails(reference, specification, field, value):
    specification[field] = value
    with pytest.raises(PraxisError, match='TARGET_MISMATCH'):
        prepare(reference, parse_spec(specification))


@pytest.mark.parametrize('change', ['unknown_workflow', 'no_workflow', 'unknown_signal'])
def test_gaps_are_explicit_and_never_certify_project(reference, specification, change):
    if change == 'unknown_signal':
        specification['signals'].append('PA20')
    else:
        specification['requirements'][0]['workflows'] = [] if change == 'no_workflow' else ['unpublished_usb']
    report, _ = prepare(reference, parse_spec(specification))
    assert report['gaps'] and not report['knowledge_scope_ready']
    assert not report['project_accepted']
    assert all('PA20' not in n['name'] for n in report['nets'])


def test_ambiguous_alias_fails_without_guessing(reference, specification, monkeypatch):
    from praxis import project_report
    index = project_report._index(reference)
    index.exact['ambiguous'] = {'PA2', 'PA3'}
    monkeypatch.setattr(project_report, '_index', lambda bundle: index)
    specification['signals'] = ['ambiguous']
    with pytest.raises(PraxisError, match='AMBIGUOUS_IDENTITY'):
        prepare(reference, parse_spec(specification))


def test_unknown_citations_or_endpoints_fail(reference, specification):
    bad = copy.deepcopy(specification)
    bad['explanations'][0]['documents'] = ['peripherals/imaginary']
    with pytest.raises(PraxisError, match='UNKNOWN_DOCUMENT'):
        prepare(reference, parse_spec(bad))
    specification['proposed_wires'][0]['to_endpoint'] = 'J999:1'
    with pytest.raises(PraxisError, match='UNKNOWN_ENDPOINT'):
        prepare(reference, parse_spec(specification))


def test_authored_html_cannot_execute(reference, specification):
    specification['title'] = '<script>alert("test")</script>'
    specification['explanations'][0]['explanation'] = '<img src=x onerror=alert(1)>'
    report, _ = prepare(reference, parse_spec(specification))
    _, page = render(report)
    assert '<script>' not in page and '<img src=x' not in page
    assert '&lt;script&gt;' in page and 'Content-Security-Policy' in page
    assert 'not confirmed fitted' in page


def test_diagram_schema_preserves_messages_and_citations(reference, specification, tmp_path):
    specification['diagrams'] = [{
        'id': 'message_flow', 'title': 'Intended message flow',
        'description': 'Authored responsibility diagram, not measured execution.',
        'documents': ['peripherals/usart'],
        'participants': [{'id': 'main', 'label': 'Main application'},
                         {'id': 'irq', 'label': 'Interrupt handler'}],
        'messages': [{'sender': 'main', 'receiver': 'irq', 'label': 'Enable bounded work'},
                     {'sender': 'irq', 'receiver': 'main', 'label': 'Publish bytes & errors'},
                     {'sender': 'main', 'receiver': 'main', 'label': '<script>not executable</script> ' * 12}]}]
    spec = parse_spec(specification)
    report, _ = prepare(reference, spec)
    raw = sequence_diagram(report['project']['diagrams'][0])
    svg = ElementTree.fromstring(raw)
    assert svg.tag.endswith('svg')
    text = ' '.join(svg.itertext())
    assert 'Enable bounded work' in text and 'Publish bytes & errors' in text
    assert '<script>' not in raw and '&lt;script&gt;' in raw
    assert ''.join(text.split()).count('<script>notexecutable</script>') == 12
    assert 'not a measured execution trace' in text
    for destination in ('one', 'two'):
        write_report(reference, spec, tmp_path / destination)
    first = tmp_path / 'one'
    for path in first.rglob('*'):
        if path.is_file():
            assert path.read_bytes() == (tmp_path / 'two' / path.relative_to(first)).read_bytes()
    assert (first / 'diagrams/message_flow.svg').read_text() == raw
    manifest = json.loads((first / 'manifest.json').read_bytes())
    assert manifest['files']['diagrams/message_flow.svg'] == hashlib.sha256(raw.encode()).hexdigest()
    page = (first / 'index.html').read_text()
    assert 'diagrams/message_flow.svg' in page and 'Intended sequences (authored)' in page
    # SVG styles are scoped so inlined diagrams cannot recolor one another.
    assert '.sequence-svg text' in page and '.net-svg text' in page
    assert '--paper:#fff' in page and '@media print' in page


@pytest.mark.parametrize('change', ['unknown_participant', 'duplicate_participant', 'duplicate_diagram', 'unknown_document'])
def test_diagrams_fail_for_unresolved_identities(reference, specification, change):
    diagram = {'id': 'flow', 'title': 'Design', 'description': 'Intended flow',
        'documents': ['peripherals/usart'],
        'participants': [{'id': 'main', 'label': 'Main'}, {'id': 'irq', 'label': 'IRQ'}],
        'messages': [{'sender': 'irq', 'receiver': 'main', 'label': 'Publish bytes'}]}
    specification['diagrams'] = [diagram]
    if change == 'unknown_participant':
        diagram['messages'][0]['receiver'] = 'missing'
    elif change == 'duplicate_participant':
        diagram['participants'][1]['id'] = 'main'
    elif change == 'duplicate_diagram':
        specification['diagrams'].append(copy.deepcopy(diagram))
    else:
        diagram['documents'] = ['peripherals/missing']
    with pytest.raises(PraxisError, match='UNKNOWN_DOCUMENT' if change == 'unknown_document' else 'INVALID_PROJECT'):
        prepare(reference, parse_spec(specification))


@pytest.mark.parametrize('change', ['duplicate', 'control', 'duplicate_json', 'unknown_field'])
def test_invalid_specs_fail_closed(specification, change):
    if change == 'duplicate':
        specification['requirements'] *= 2
    elif change == 'control':
        specification['explanations'][0]['explanation'] = 'Invalid\x00XML'
    elif change == 'unknown_field':
        specification['physical_passed'] = True
    else:
        with pytest.raises(PraxisError, match='DUPLICATE_IDENTITY'):
            parse_spec(b'{"id":"a","id":"b"}')
        return
    with pytest.raises(PraxisError, match='INVALID_PROJECT'):
        parse_spec(specification)


@pytest.mark.parametrize('name', ['../outside.c', '/tmp/outside.c', 'escape.c', 'pipe.c'])
def test_attachment_containment_and_special_files(reference, specification, tmp_path, name):
    root = tmp_path / 'workspace'
    root.mkdir()
    outside = tmp_path / 'outside.c'
    outside.write_text('secret')
    (root / 'escape.c').symlink_to(outside)
    os.mkfifo(root / 'pipe.c')
    specification['files'] = [name]
    with pytest.raises(PraxisError, match='INVALID_PATH|INVALID_PROJECT_FILE'):
        prepare(reference, parse_spec(specification), root)


def test_outputs_deterministic_complete_and_immutable(reference, specification, tmp_path):
    source = tmp_path / 'workspace'
    source.mkdir()
    raw = b'int main(void) { return 0; }\n'
    (source / 'main.c').write_bytes(raw)
    specification['files'] = ['main.c']
    spec = parse_spec(specification)
    for name in ('first', 'second'):
        write_report(reference, spec, tmp_path / name, source)
    first, second = tmp_path / 'first', tmp_path / 'second'
    for path in first.rglob('*'):
        if path.is_file():
            assert path.read_bytes() == (second / path.relative_to(first)).read_bytes()
    manifest = json.loads((first / 'manifest.json').read_bytes())
    for name, expected in manifest['files'].items():
        assert hashlib.sha256((first / name).read_bytes()).hexdigest() == expected
    assert (first / 'project_files/000.txt').read_bytes() == raw
    with pytest.raises(PraxisError, match='IMMUTABLE_REPORT'):
        write_report(reference, spec, first)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        write_report(reference, spec, reference.root / 'must_not_write')
    link = tmp_path / 'link'
    link.symlink_to(first, target_is_directory=True)
    with pytest.raises(PraxisError, match='IMMUTABLE_REPORT'):
        write_report(reference, spec, link)


def test_build_evidence_cannot_imply_physical_or_source_acceptance(reference, specification):
    receipt = {'bundle_revision': reference.manifest.bundle_revision, 'artifact_id': 'a' * 64,
               'compile_passed': True, 'image_validated': True, 'validation': {'valid': True}}
    report, _ = prepare(reference, parse_spec(specification), checked_build=receipt)
    assert report['build']['status'] == 'artifact_revalidated'
    assert report['build']['attachment_source_binding'] == 'not_assessed'
    assert not report['project_accepted']
    receipt['validation']['valid'] = False
    with pytest.raises(PraxisError, match='INVALID_BUILD_EVIDENCE'):
        prepare(reference, parse_spec(specification), checked_build=receipt)


def test_cli_creates_shareable_report_and_schema(specification, tmp_path, capsys):
    spec = tmp_path / 'project.json'
    spec.write_text(json.dumps(specification))
    assert main(['project-report', '--bundle', str(BUNDLE), '--spec', str(spec),
                 '--output', str(tmp_path / 'report')]) == 0
    assert json.loads(capsys.readouterr().out)['build_status'] == 'not_assessed'
    assert main(['schema', '--kind', 'project']) == 0
    assert 'requirements' in json.loads(capsys.readouterr().out)['properties']


async def test_opt_in_reporting_over_real_mcp_with_checked_build(specification, tmp_path):
    lock = require_image(ROOT / 'toolchain-f407.lock.json')
    workspace = tmp_path / 'workspace'
    shutil.copytree(ROOT / 'examples/stm32f407g-disc1-led-button/application', workspace / 'app')
    params = StdioServerParameters(command=sys.executable, args=['-m', 'praxis', 'build-serve',
        '--bundle', str(BUNDLE), '--assets', str(ROOT / 'assets/stm32f407vg'),
        '--workspace', str(workspace), '--artifacts', str(tmp_path / 'artifacts'),
        '--lock', str(lock), '--project-reports', str(tmp_path / 'reports')], cwd=str(tmp_path), env=dict(os.environ))

    def result(response):
        return response.structuredContent or json.loads(response.content[0].text)

    async def exercise():
        async with stdio_client(params) as (reader, writer), ClientSession(reader, writer) as client:
            await client.initialize()
            tools = {t.name for t in (await client.list_tools()).tools}
            assert tools == {'get_build_profile', 'build_firmware', 'validate_firmware', 'generate_project_report'}
            denied = await client.call_tool('generate_project_report',
                {'specification': specification, 'artifact_id': '0' * 64})
            assert denied.isError
            assert not (tmp_path / 'reports/uart_supervisor').exists()
            built = await client.call_tool('build_firmware', {'source_directory': 'app'})
            assert not built.isError, built
            artifact = result(built)
            assert artifact['compile_passed'] and artifact['image_validated'], artifact
            response = await client.call_tool('generate_project_report',
                {'specification': specification, 'artifact_id': artifact['artifact_id']})
            assert not response.isError, response
            report = result(response)
            assert report['build_status'] == 'artifact_revalidated'
            assert not report['project_accepted']
            saved = json.loads((Path(report['output']) / 'report.json').read_bytes())
            assert saved['build']['artifact_id'] == artifact['artifact_id']
            retry = await client.call_tool('generate_project_report', {'specification': specification})
            assert retry.isError and 'IMMUTABLE_REPORT' in str(retry.content)
    await asyncio.wait_for(exercise(), timeout=60)
