"""Opt-in typesetting of fixed, regenerated report templates; no arbitrary TeX execution."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
import time
from pathlib import Path

from praxis.bundle import digest, read_inside
from praxis.electrical import circuit_pages
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.project_latex import sources
from praxis.project_report import parse_spec
from praxis.verify import bounded

TOOLS = ('lualatex', 'kpsewhich', 'pdftocairo', 'pdfinfo')
PACKAGES = ('circuitikz.sty', 'fontspec.sty', 'geometry.sty', 'microtype.sty',
            'graphicx.sty', 'longtable.sty', 'array.sty', 'booktabs.sty', 'fancyhdr.sty',
            'xurl.sty', 'hyperref.sty', 'needspace.sty')


def dependencies() -> dict[str, str]:
    tools = {}
    for name in TOOLS:
        path = shutil.which(name)
        if path is None:
            raise PraxisError('MISSING_DEPENDENCY', f'Install the document-rendering executable: {name}')
        # TeX selects its format from argv[0]; resolving lualatex to luahbtex
        # would invoke the bare engine instead of the LaTeX format.
        tools[name] = str(Path(path).absolute())
    for name in PACKAGES:
        result = bounded([tools['kpsewhich'], name], 10)
        if result['returncode'] or result['failure'] or not result['diagnostics'].strip():
            raise PraxisError('MISSING_DEPENDENCY', f'Install the TeX package providing {name}')
    return tools


def _inputs(root: Path) -> tuple[dict, dict[str, bytes], str]:
    raw = read_inside(root, 'manifest.json', 1024 * 1024)
    manifest = load_json(raw)
    if (not isinstance(manifest, dict) or manifest.get('format') != 'praxis-project-files-v1'
            or not isinstance(manifest.get('files'), dict)):
        raise PraxisError('INVALID_PROJECT_REPORT', 'Select an integrity-checked Praxis project report')
    contents = {}
    for name, expected in manifest['files'].items():
        if not isinstance(expected, str) or re.fullmatch('[0-9a-f]{64}', expected) is None:
            raise PraxisError('INVALID_PROJECT_REPORT', 'Invalid report file hash')
        contents[name] = read_inside(root, name)
        if digest(contents[name]) != expected:
            raise PraxisError('INTEGRITY_ERROR', f'Project report changed: {name}')
    if 'report.json' not in contents or len(contents['report.json']) > 16 * 1024 * 1024:
        raise PraxisError('INVALID_PROJECT_REPORT', 'Missing or oversized project report JSON')
    report = load_json(contents['report.json'])
    if not isinstance(report, dict) or report.get('format') != 'praxis-project-report-v1':
        raise PraxisError('INVALID_PROJECT_REPORT', 'Unsupported report format')
    parse_spec(report['project'])
    identity = {key: value for key, value in report.items() if key != 'report_revision'}
    encoded = (json.dumps(identity, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode()
    if digest(encoded) != report.get('report_revision') or report['report_revision'] != manifest.get('report_revision'):
        raise PraxisError('INTEGRITY_ERROR', 'Project report data no longer matches its revision')
    return report, contents, digest(raw)


def render_pdf(root: Path, output: Path) -> dict:
    root, output = root.resolve(strict=True), output.absolute()
    if output.exists() or output.is_symlink():
        raise PraxisError('IMMUTABLE_REPORT', 'Choose a new PDF output directory')
    if output.resolve().is_relative_to(root):
        raise PraxisError('INVALID_PATH', 'PDF output must stay outside the source report')
    report, contents, input_hash = _inputs(root)
    tools = dependencies()
    # Ignore exported TeX as executable input, even when its file hash is valid.
    # Recreate every compiler input from escaped text and fixed command templates.
    regenerated = sources(report)
    contents = {name: raw for name, raw in contents.items() if not name.startswith('latex/')}
    contents.update(regenerated)
    output.parent.mkdir(parents=True, exist_ok=True)
    commands, warnings, deadline = [], [], time.monotonic() + 120
    with tempfile.TemporaryDirectory(prefix='.project-pdf-', dir=output.parent) as directory:
        stage = Path(directory) / 'document'
        stage.mkdir()
        for name, raw in sorted(contents.items()):
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        work = stage / 'latex'
        (work / 'figures').mkdir(exist_ok=True)

        def run(command):
            # bounded() already caps diagnostics and terminates the process group.
            result = bounded(command, max(0.1, min(40, deadline - time.monotonic())), cwd=work)
            commands.append({'executable': Path(command[0]).name, 'arguments': command[1:],
                             'returncode': result['returncode'], 'failure': result['failure']})
            warnings.extend(re.findall(r'^(?:Overfull[^\n]*|Missing character[^\n]*)', result['diagnostics'], re.M))
            if re.search(r'^Overfull|^Missing character', result['diagnostics'], re.M):
                commands[-1]['layout_diagnostics'] = result['diagnostics'][-20000:]
            if result['returncode'] or result['failure']:
                raise PraxisError('TYPESETTING_FAILED', result['diagnostics'][-10000:] or str(result['failure']))
            return result['diagnostics']

        def compile_job(name):
            run([tools['lualatex'], '--no-shell-escape', '--interaction=nonstopmode',
                 '--halt-on-error', '--file-line-error', name + '.tex'])
            pdf = work / (name + '.pdf')
            if not pdf.is_file() or pdf.stat().st_size > 16 * 1024 * 1024:
                raise PraxisError('TYPESETTING_FAILED', 'Missing or oversized generated PDF')

        page_count = len(circuit_pages(report.get('electrical_drawings', [])))
        if page_count:
            compile_job('electrical')
            information = run([tools['pdfinfo'], 'electrical.pdf'])
            count = re.search(r'^Pages:\s+(\d+)', information, re.M)
            if count is None or int(count[1]) != page_count:
                raise PraxisError('ELECTRICAL_LAYOUT', 'Electrical sheets overflowed; no incomplete PDF was published')
            shutil.move(work / 'electrical.pdf', work / 'figures/electrical.pdf')
            (stage / 'electrical').mkdir()
            for number in range(1, page_count + 1):
                run([tools['pdftocairo'], '-svg', '-f', str(number), '-l', str(number),
                     'figures/electrical.pdf', f'../electrical/sheet-{number:03}.svg'])
        compile_job('report')
        compile_job('report')  # Resolve contents and page references.
        if any(w.startswith('Missing character') or float(re.search(r'\(([\d.]+)pt', w)[1]) > 1
               for w in warnings):
            raise PraxisError('TYPESETTING_LAYOUT', 'Missing glyph or overflowing text; no incomplete report was published')
        shutil.copyfile(work / 'report.pdf', stage / 'report.pdf')
        for stem in ('electrical', 'report'):
            for suffix in ('.aux', '.log', '.out', '.toc'):
                (work / (stem + suffix)).unlink(missing_ok=True)
        previews = ('<p class="pdf-download"><a href="report.pdf">Download typeset PDF report</a></p>'
                    + ''.join(f'<figure><img src="electrical/sheet-{i:03}.svg" '
                        f'alt="Electrical reference schematic, sheet {i}" style="width:100%;height:auto">'
                        f'<figcaption>Electrical reference, sheet {i} — scoped redraw.</figcaption></figure>'
                        for i in range(1, page_count + 1)))
        index = (stage / 'index.html').read_text(encoding='utf-8')
        index = index.replace('<!-- electrical-preview -->', previews)
        index = index.replace('<body>', '<body><p><a href="report.pdf">PDF / engineering report</a></p>', 1)
        (stage / 'index.html').write_text(index, encoding='utf-8')
        receipt = {'format': 'praxis-project-typesetting-v1',
            'input_manifest_sha256': input_hash, 'report_revision': report['report_revision'],
            'electrical_sheets': page_count, 'pdf_sha256': digest((stage / 'report.pdf').read_bytes()),
            'commands': commands, 'layout_warnings': warnings,
            'custom_tex_executed': False, 'physical_verification': 'not_assessed'}
        (stage / 'typesetting.json').write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
        hashes = {}
        for path in sorted(stage.rglob('*')):
            if path.is_file() and path.name != 'manifest.json':
                hashes[path.relative_to(stage).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        (stage / 'manifest.json').write_text(json.dumps({'format': 'praxis-project-files-v1',
            'report_revision': report['report_revision'], 'files': hashes}, sort_keys=True, indent=2) + '\n')
        if output.exists() or output.is_symlink():
            raise PraxisError('IMMUTABLE_REPORT', 'PDF destination appeared while typesetting')
        os.rename(stage, output)
    return {'output': str(output), 'pdf': str(output / 'report.pdf'),
        'electrical_sheets': page_count, 'pdf_sha256': receipt['pdf_sha256'],
        'project_accepted': False, 'physical_verification': 'not_assessed'}
