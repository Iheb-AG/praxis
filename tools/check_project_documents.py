"""Required native LaTeX/PDF checks, separate from firmware-toolchain dependencies."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from praxis.bundle import Bundle, digest
from praxis.errors import PraxisError
from praxis.project_pdf import render_pdf
from praxis.project_report import parse_spec, write_report

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='Fresh private evidence directory')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    text_tool = shutil.which('pdftotext')
    if text_tool is None:
        raise PraxisError('MISSING_DEPENDENCY', 'Install pdftotext (Poppler utilities)')
    spec = json.loads((ROOT / 'examples/projects/stm32f407-protocol-supervisor/project.json').read_bytes())
    spec['files'] = []
    spec['explanations'].append(dict(title='Literal text check', documents=['index'],
        explanation=r'TeX text remains literal: \input{/a/file/that/must/not/be/read} & % # _ { } $ ~ ^.'))
    raw = args.output / 'source'
    write_report(Bundle(ROOT / 'bundles/stm32f407g-disc1-e01-timer-irq-v1'), parse_spec(spec), raw)
    # Even a self-consistent edited TeX export must not become an executable input.
    payload = b'\\input{/this-file-does-not-exist-and-must-not-be-opened}\n'
    (raw / 'latex/report.tex').write_bytes(payload)
    manifest = json.loads((raw / 'manifest.json').read_bytes())
    manifest['files']['latex/report.tex'] = digest(payload)
    (raw / 'manifest.json').write_text(json.dumps(manifest, sort_keys=True, indent=2) + '\n')
    rendered = render_pdf(raw, args.output / 'typeset')
    destination = Path(rendered['output'])
    if (destination / 'latex/report.tex').read_bytes() == payload:
        raise AssertionError('Edited TeX was not regenerated')
    doc = json.loads((destination / 'report.json').read_bytes())
    receipt = json.loads((destination / 'typesetting.json').read_bytes())
    if receipt['layout_warnings']:
        raise AssertionError(f'Native typesetting layout warnings: {receipt["layout_warnings"]}')

    def pdf_text(path):
        result = subprocess.run([text_tool, str(path), '-'], capture_output=True, timeout=20, check=True)
        return ''.join(result.stdout.decode().split())

    body = pdf_text(destination / 'report.pdf')
    figures = pdf_text(destination / 'latex/figures/electrical.pdf')
    if r'\input{/a/file/that/must/not/be/read}' not in body:
        raise AssertionError('Authored TeX-like text was omitted or executed instead of printed literally')
    for value in ('Project scope and requirements', 'Electrical design', 'Traceability and exact identities', spec['title']):
        if ''.join(value.split()) not in body:
            raise AssertionError(f'PDF section missing: {value}')
    expected = {p['endpoint'] for n in doc['nets'] for p in n['endpoints']}
    for endpoint in expected:
        if ''.join(endpoint.split()) not in figures:
            raise AssertionError(f'Electrical sheet omitted endpoint: {endpoint}')
    output_manifest = json.loads((destination / 'manifest.json').read_bytes())
    for name, expected_hash in output_manifest['files'].items():
        if hashlib.sha256((destination / name).read_bytes()).hexdigest() != expected_hash:
            raise AssertionError(f'Changed output file: {name}')
    result = {'native_typesetting_passed': True, 'electrical_endpoints_checked': len(expected),
        'electrical_sheets': rendered['electrical_sheets'], 'layout_warnings': [],
        'edited_tex_not_executed': True, 'literal_tex_text_preserved': True,
        'output_hashes_passed': True, 'hardware_operations': 0,
        'physical_verification': 'not_assessed'}
    (args.output / 'checks.json').write_text(json.dumps(result, sort_keys=True, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
