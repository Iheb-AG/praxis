"""Source-backed electrical recipes and escaped, editable engineering-report parts."""
import copy
import json
from pathlib import Path

import pytest

from praxis.bundle import Bundle, digest
from praxis.electrical import catalog, drawings
from praxis.errors import PraxisError
from praxis.project_latex import sources
from praxis.project_pdf import _inputs, dependencies, render_pdf
from praxis.project_report import parse_spec, prepare, write_report
from tests.conftest import ROOT


@pytest.fixture(scope='module')
def reference():
    return Bundle(ROOT / 'bundles/stm32f407g-disc1-e01-timer-irq-v1')


@pytest.fixture
def spec():
    raw = json.loads((ROOT / 'examples/projects/stm32f407-protocol-supervisor/project.json').read_bytes())
    raw['files'] = []
    return raw


@pytest.fixture
def report(reference, spec):
    return prepare(reference, parse_spec(spec))[0]


def test_every_selected_terminal_is_preserved_in_electrical_drawings(report):
    expected = {p['endpoint'] for net in report['nets'] for p in net['endpoints']}
    shown = [p['endpoint'] for figure in report['electrical_drawings'] for p in figure['connections']]
    assert set(shown) == expected
    assert len(shown) == len(set(shown))
    assert all(figure['sources'] for figure in report['electrical_drawings'])
    green = next(f for f in report['electrical_drawings'] if f['components'] == ['R40', 'LD4'])
    assert green['kind'] == 'led_resistor'
    assert (green['left'], green['middle'], green['right']) == ('PD12', 'LD4_ANODE', 'GND')
    assert '510 ohm' in green['resistor']
    switch = next(f for f in report['electrical_drawings'] if f['components'] == ['B1'])
    assert switch['kind'] == 'normally_open_switch'
    assert switch['groups'] == [['1', '2'], ['3', '4']]
    bridge = next(f for f in report['electrical_drawings'] if f['components'] == ['SB20'])
    assert bridge['kind'] == 'terminal_block'  # Fitted does not establish present closure.


def test_junction_with_another_endpoint_is_not_called_a_series_branch(report):
    net = next(n for n in report['nets'] if n['name'] == 'LD4_ANODE')
    net['endpoints'].append(dict(net='LD4_ANODE', endpoint='EXTRA:1', pin='1', sources='fixture'))
    result = drawings(report['components'], report['nets'])
    assert not any(f['kind'] == 'led_resistor' and 'LD4' in f['components'] for f in result)
    assert any(f['components'] == ['LD4'] and f['kind'] == 'led' for f in result)


@pytest.mark.parametrize('change', ['unknown_polarity', 'missing_contact_groups', 'not_fitted'])
def test_symbol_semantics_are_never_guessed_from_reference_names(report, change):
    components = copy.deepcopy(report['components'])
    if change == 'missing_contact_groups':
        component = next(c for c in components if c['ref'] == 'B1')
        component['properties'].pop('internal_groups')
    else:
        component = next(c for c in components if c['ref'] == 'LD4')
        if change == 'unknown_polarity':
            component['pins'] = {'1': 'unknown', '2': 'unknown'}
        else:
            component['fitted'] = False
    result = drawings(components, report['nets'])
    figure = next(f for f in result if component['ref'] in f['components'])
    assert figure['kind'] == 'terminal_block'


def test_component_catalog_rejects_conflicting_declarations(reference):
    raw = reference.read(reference.manifest.documents['schemas/components'])
    row = next(line for line in raw.splitlines() if line.startswith('| R40 |'))
    with pytest.raises(PraxisError, match='INVALID_COMPONENTS'):
        catalog(raw + '\n' + row)
    with pytest.raises(PraxisError, match='INVALID_COMPONENTS'):
        catalog(raw.replace('1=1; 2=2', '1=1; 1=2'))


def test_authored_tex_commands_are_literal_text(reference, spec):
    payload = r'}\input{/tmp/praxis_should_not_read}% $ & # _ ~ ^'
    spec['title'] = payload
    spec['explanations'][0]['explanation'] = payload
    report, _ = prepare(reference, parse_spec(spec))
    files = sources(report)
    assert all(isinstance(value, bytes) for value in files.values())
    front = files['latex/sections/00-front.tex'].decode()
    assert r'\input{/tmp/praxis_should_not_read}' not in front
    assert r'\textbackslash{}input\{' in front
    assert r'\%' in front and r'\$' in front and r'\&' in front
    assert rb'\begin{circuitikz}' in files['latex/electrical.tex']
    assert rb'\input{sections/00-front.tex}' in files['latex/report.tex']
    assert 'parts' in json.loads(files['latex/authoring.json'])


def test_integrity_checked_tex_is_still_regenerated_before_execution(reference, spec, tmp_path):
    root = tmp_path / 'report'
    write_report(reference, parse_spec(spec), root)
    changed = b'\\immediate\\write18{this-must-never-execute}\n'
    (root / 'latex/report.tex').write_bytes(changed)
    manifest = json.loads((root / 'manifest.json').read_bytes())
    manifest['files']['latex/report.tex'] = digest(changed)
    (root / 'manifest.json').write_text(json.dumps(manifest))
    parsed, contents, _ = _inputs(root)
    assert contents['latex/report.tex'] == changed
    assert sources(parsed)['latex/report.tex'] != changed
    (root / 'report.json').write_bytes(b'changed')
    with pytest.raises(PraxisError, match='INTEGRITY_ERROR'):
        _inputs(root)


def test_typesetter_requires_exact_dependencies(monkeypatch):
    monkeypatch.setattr('praxis.project_pdf.shutil.which', lambda name: None)
    with pytest.raises(PraxisError, match='MISSING_DEPENDENCY.*lualatex'):
        dependencies()


def test_typesetter_preserves_latex_format_launcher_name(monkeypatch):
    monkeypatch.setattr('praxis.project_pdf.shutil.which', lambda name: '/usr/bin/' + name)
    monkeypatch.setattr('praxis.project_pdf.bounded', lambda *args: {
        'returncode': 0, 'failure': None, 'diagnostics': '/tex/package.sty'})
    assert Path(dependencies()['lualatex']).name == 'lualatex'


def test_typesetting_never_overwrites_source_or_prior_outputs(reference, spec, tmp_path):
    root = tmp_path / 'report'
    write_report(reference, parse_spec(spec), root)
    with pytest.raises(PraxisError, match='INVALID_PATH'):
        render_pdf(root, root / 'inside')
    existing = tmp_path / 'existing'
    existing.mkdir()
    with pytest.raises(PraxisError, match='IMMUTABLE_REPORT'):
        render_pdf(root, existing)
