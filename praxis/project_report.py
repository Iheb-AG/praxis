"""Target-independent project documentation from a verified Markdown bundle.

Authored explanations remain authored claims. Only build-service revalidation can
supply checked image evidence; neither layer certifies physical operation.
"""
from __future__ import annotations

import html
import json
import math
import os
import stat
import tempfile
import textwrap
from pathlib import Path
from typing import Literal

from pydantic import Field, ValidationError, model_validator

from praxis.bundle import Bundle, decode, digest, read_inside, relative_path
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Digest, Identifier, Record
from praxis.netlist import NetlistIndex
from praxis.render import table


class Requirement(Record):
    id: Identifier
    description: str = Field(min_length=1, max_length=4096)
    workflows: list[Identifier] = Field(default_factory=list, max_length=64)
    verification_plan: str = Field(min_length=1, max_length=4096)


class Explanation(Record):
    title: str = Field(min_length=1, max_length=256)
    explanation: str = Field(min_length=1, max_length=12000)
    documents: list[str] = Field(min_length=1, max_length=64)


class ProposedWire(Record):
    from_endpoint: str = Field(min_length=1, max_length=128)
    to_endpoint: str = Field(min_length=1, max_length=128)
    description: str = Field(min_length=1, max_length=2048)


class Participant(Record):
    id: Identifier
    label: str = Field(min_length=1, max_length=128)


class Message(Record):
    sender: Identifier
    receiver: Identifier
    label: str = Field(min_length=1, max_length=512)


class SequenceDiagram(Record):
    id: Identifier
    title: str = Field(min_length=1, max_length=256)
    description: str = Field(min_length=1, max_length=4096)
    documents: list[str] = Field(min_length=1, max_length=64)
    participants: list[Participant] = Field(min_length=2, max_length=8)
    messages: list[Message] = Field(min_length=1, max_length=64)

    @model_validator(mode='after')
    def valid_connections(self):
        identities = [p.id for p in self.participants]
        if len(identities) != len(set(identities)):
            raise ValueError('Diagram participants must have unique IDs')
        for message in self.messages:
            if message.sender not in identities or message.receiver not in identities:
                raise ValueError('Diagram messages must reference declared participant IDs')
        return self


class ProjectSpec(Record):
    format: Literal['praxis-project-v1']
    id: Identifier
    title: str = Field(min_length=1, max_length=256)
    objective: str = Field(min_length=1, max_length=12000)
    target_id: Identifier
    bundle_revision: Digest
    requirements: list[Requirement] = Field(min_length=1, max_length=128)
    explanations: list[Explanation] = Field(default_factory=list, max_length=128)
    diagrams: list[SequenceDiagram] = Field(default_factory=list, max_length=16)
    signals: list[str] = Field(default_factory=list, max_length=64)
    proposed_wires: list[ProposedWire] = Field(default_factory=list, max_length=32)
    files: list[str] = Field(default_factory=list, max_length=128)
    procedure: list[str] = Field(default_factory=list, max_length=128)
    limitations: list[str] = Field(min_length=1, max_length=128)

    @model_validator(mode='after')
    def unique(self):
        for values in ([r.id for r in self.requirements], [d.id for d in self.diagrams], self.signals, self.files):
            if len(values) != len(set(values)):
                raise ValueError('Project identities, signals and file paths must be unique')
        for requirement in self.requirements:
            if len(requirement.workflows) != len(set(requirement.workflows)):
                raise ValueError('A requirement cannot repeat a workflow')
        def check(value):
            if isinstance(value, str):
                if not value.strip() or any(ord(c) < 32 and c not in '\n\r\t' for c in value):
                    raise ValueError('Describe each project field without control characters')
            elif isinstance(value, dict):
                for item in value.values():
                    check(item)
            elif isinstance(value, list):
                for item in value:
                    check(item)
        check(self.model_dump())
        return self


def parse_spec(raw: bytes | dict) -> ProjectSpec:
    try:
        return ProjectSpec.model_validate(load_json(raw) if isinstance(raw, bytes) else raw)
    except (ValueError, ValidationError) as exc:
        raise PraxisError('INVALID_PROJECT', str(exc)) from exc


def _json(value) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + '\n').encode()


def _index(bundle: Bundle) -> NetlistIndex:
    docs = bundle.manifest.documents
    return NetlistIndex(bundle.read(bundle.manifest.netlist), bundle.manifest.target.primary_mcu_ref,
        bundle.read(docs['schemas/board']) if 'schemas/board' in docs else None,
        bundle.read(docs['schemas/components']) if 'schemas/components' in docs else None,
        allow_empty=bundle.manifest.target.scope == 'mcu')


def prepare(bundle: Bundle, spec: ProjectSpec, workspace: Path | None = None,
            checked_build: dict | None = None) -> tuple[dict, dict[str, bytes]]:
    if (spec.target_id != bundle.manifest.target.id
            or spec.bundle_revision != bundle.manifest.bundle_revision):
        raise PraxisError('TARGET_MISMATCH', 'Project target and exact bundle revision must match')
    from praxis.support import assess
    try:
        available = assess(bundle)['workflows']
    except PraxisError as exc:
        if exc.code != 'SUPPORT_REPORT_UNAVAILABLE':
            raise
        available = {}
    netlist = _index(bundle)
    nets, queries, gaps, requirements = set(), [], [], []
    documents = {'index', 'sources'} & bundle.manifest.documents.keys()
    for item in spec.requirements:
        workflows = []
        for name in item.workflows:
            row = available.get(name)
            ready = row is not None and row['knowledge_ready']
            issues = row['issues'] if row else ['Workflow not declared in this bundle']
            workflows.append({'id': name, 'knowledge_ready': ready, 'issues': issues})
            if row:
                documents.update(f'peripherals/{entity}' for entity in row['retrieval_closure'])
            if not ready:
                gaps.append(f'{item.id}: {name}: ' + '; '.join(issues or ['Knowledge is blocked']))
        if not workflows:
            gaps.append(f'{item.id}: no published workflow mapping; application logic needs review')
        requirements.append({**item.model_dump(), 'workflow_assessment': workflows,
                             'implementation_verification': 'not_assessed'})
    for explanation in spec.explanations:
        documents.update(explanation.documents)
    for diagram in spec.diagrams:
        documents.update(diagram.documents)
    for key in documents:
        if key not in bundle.manifest.documents:
            raise PraxisError('UNKNOWN_DOCUMENT', f'Project cites unregistered document {key!r}')
    for signal in spec.signals:
        response = netlist.query(signal)  # Keep canonical input/ambiguity checks.
        matches = netlist.exact.get(signal.strip(), set()) | netlist.pins.get(signal.strip().casefold(), set())
        if not matches:
            gaps.append(f'Unresolved signal: {signal}')
            queries.append({'query': signal, 'nets': [], 'result': response})
            continue
        name = next(iter(matches))
        related = {name} | netlist.circuits.get(name, set())
        nets.update(related)
        queries.append({'query': signal, 'nets': sorted(related)})
    endpoints = {netlist._cells(line)[1]: name for name, rows in netlist.nets.items() for line in rows}
    for wire in spec.proposed_wires:
        if wire.from_endpoint == wire.to_endpoint:
            raise PraxisError('INVALID_WIRING', 'A proposed jumper needs two distinct endpoints')
        for endpoint in (wire.from_endpoint, wire.to_endpoint):
            if endpoint not in endpoints:
                raise PraxisError('UNKNOWN_ENDPOINT', f'Proposed jumper endpoint {endpoint!r} is not published')
            nets.add(endpoints[endpoint])
    topology = [{'name': name, 'endpoints': [dict(zip(
        ('net', 'endpoint', 'pin', 'sheet', 'package', 'aliases', 'sources'), netlist._cells(line), strict=True))
        for line in netlist.nets[name]]} for name in sorted(nets)]
    components, electrical_drawings = [], []
    if nets and 'schemas/components' in bundle.manifest.documents:
        from praxis.electrical import catalog, drawings
        published = catalog(bundle.read(bundle.manifest.documents['schemas/components']))
        selected = {p['endpoint'].rsplit(':', 1)[0] for n in topology for p in n['endpoints']}
        if not selected <= published.keys():
            raise PraxisError('INVALID_COMPONENTS', 'Selected endpoints lack published component evidence')
        components = [published[ref] for ref in sorted(selected)]
        for net in topology:
            for pin in net['endpoints']:
                ref, number = pin['endpoint'].rsplit(':', 1)
                if published[ref]['pins'].get(number) != pin['pin']:
                    raise PraxisError('INVALID_COMPONENTS', f'Component pin disagrees with netlist: {pin["endpoint"]}')
        electrical_drawings = drawings(components, topology)
    if nets:
        documents.add('schemas/custom_pcb_netlist')
        documents.update(key for key in ('schemas/board', 'schemas/components') if key in bundle.manifest.documents)
    output, references, project_files = {}, [], []
    for number, key in enumerate(sorted(documents)):
        path = f'references/{number:03}.md'
        raw = bundle.read(bundle.manifest.documents[key]).encode()
        output[path] = raw
        references.append({'id': key, 'file': path, 'sha256': digest(raw)})
    attached_bytes = 0
    for number, name in enumerate(spec.files):
        if workspace is None:
            raise PraxisError('MISSING_WORKSPACE', 'Project source attachments require an explicit workspace')
        root = workspace.resolve(strict=True)
        path = root / relative_path(name)
        if not path.resolve(strict=True).is_relative_to(root):
            raise PraxisError('INVALID_PATH', f'Attachment escapes workspace: {name}')
        if not stat.S_ISREG(path.stat().st_mode):
            raise PraxisError('INVALID_PROJECT_FILE', f'Only regular UTF-8 attachments are accepted: {name}')
        raw = read_inside(root, name, 8 * 1024 * 1024)
        attached_bytes += len(raw)
        if attached_bytes > 16 * 1024 * 1024:
            raise PraxisError('PROJECT_LIMIT', 'Project attachments exceed 16 MiB; select fewer files')
        decode(raw, name)
        path = f'project_files/{number:03}.txt'
        output[path] = raw
        project_files.append({'path': name, 'file': path, 'sha256': digest(raw)})
    build = {'status': 'not_assessed'}
    if checked_build is not None:
        if (checked_build.get('bundle_revision') != bundle.manifest.bundle_revision
                or checked_build.get('compile_passed') is not True
                or checked_build.get('image_validated') is not True
                or checked_build.get('validation', {}).get('valid') is not True):
            raise PraxisError('INVALID_BUILD_EVIDENCE', 'Attach a revalidated artifact for this exact bundle')
        artifact_id = checked_build.get('artifact_id')
        if not isinstance(artifact_id, str) or len(artifact_id) != 64 or any(c not in '0123456789abcdef' for c in artifact_id):
            raise PraxisError('INVALID_BUILD_EVIDENCE', 'Build evidence needs an exact accepted artifact ID')
        build = {'status': 'artifact_revalidated', **{key: checked_build[key] for key in
            ('artifact_id', 'bundle_revision', 'compile_passed', 'image_validated', 'validation')}}
        # Revalidating another image must not imply that attached source files produced it.
        build['attachment_source_binding'] = 'not_assessed'
    report = {'format': 'praxis-project-report-v1', 'project': spec.model_dump(),
        'target': bundle.manifest.target.model_dump(), 'bundle_revision': bundle.manifest.bundle_revision,
        'requirements': requirements, 'signal_queries': queries, 'nets': topology,
        'components': components, 'electrical_drawings': electrical_drawings,
        'references': references, 'project_files': project_files, 'build': build,
        'gaps': gaps, 'knowledge_scope_ready': not gaps, 'project_accepted': False,
        'physical_verification': 'not_assessed',
        'limits': ['Authored design explanations are not automatically proven by their citations.',
                  'Connectivity is a scoped published netlist view, not a full CAD/electrical audit.',
                  'Components do not merge nets; proposed external jumpers are not confirmed fitted.',
                  'Workflow readiness does not establish concurrent resource compatibility or firmware correctness.',
                  'An accepted artifact is not proof of its behavior or of these attached sources.']}
    report['report_revision'] = digest(_json(report))
    return report, output


def schematic(report: dict) -> str:
    """Bipartite net-membership schematic; preserve every scoped endpoint and distinct net."""
    esc = html.escape
    names = [n['name'] for n in report['nets']]
    labels = [e['endpoint'] + ' / ' + e['pin'] for n in report['nets'] for e in n['endpoints']]
    left = max(240, max(map(len, names), default=0) * 10 + 50)
    cell_width = max(280, max(map(len, labels), default=0) * 9 + 35)
    width = left + 3 * (cell_width + 35) + 80
    y, parts = 90, []
    for net in report['nets']:
        count = len(net['endpoints'])
        height = max(100, math.ceil(count / 3) * 110 + 45)
        parts.append(f'<text x="24" y="{y + 27}" class="net">{esc(net["name"])}</text>')
        parts.append(f'<path d="M{left - 25} {y + 15}V{y + height - 25}" class="wire"/>')
        for row in range(math.ceil(count / 3)):
            columns = min(3, count - row * 3)
            last_center = left + (columns - 1) * (cell_width + 35) + cell_width // 2
            parts.append(f'<path d="M{left - 25} {y + row * 110 + 15}H{last_center}" class="wire"/>')
        for i, endpoint in enumerate(net['endpoints']):
            x, top = left + (i % 3) * (cell_width + 35), y + (i // 3) * 110 + 35
            parts.extend([f'<path d="M{x + cell_width // 2} {top - 20}V{top}" class="wire"/>',
                f'<rect x="{x}" y="{top}" width="{cell_width}" height="60" rx="5"/>',
                f'<text x="{x + 14}" y="{top + 37}">{esc(endpoint["endpoint"] + " / " + endpoint["pin"])}</text>'])
        y += height + 25
    parts.append(f'<text x="24" y="{y + 20}" class="net">Proposed external wiring (not confirmed fitted)</text>')
    y += 65
    for wire in report['project']['proposed_wires']:
        label = f'{wire["from_endpoint"]} ↔ {wire["to_endpoint"]}'
        parts.append(f'<path d="M24 {y}H{width - 40}" class="planned"/>')
        parts.append(f'<text x="40" y="{y - 12}">{esc(label)}</text>')
        y += 70
    return (f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Scoped net connectivity" '
        f'class="net-svg" viewBox="0 0 {width} {y + 35}"><title>Resolved connectivity — separate electrical nets</title>'
        '<style>.net-svg text{font:18px sans-serif;fill:#263445}.net-svg .net{font-size:22px;fill:#173b58}'
        '.net-svg rect{fill:#f8fafc;stroke:#c6d2dd}.net-svg .wire{fill:none;stroke:#426783;stroke-width:2}'
        '.net-svg .planned{fill:none;stroke:#8a5b1f;stroke-width:2;stroke-dasharray:8 6}'
        '.net-svg .paper{fill:#fff;stroke:none}</style>'
        f'<rect class="paper" width="{width}" height="{y + 35}"/>'
        '<text x="24" y="40" class="net">Scoped connectivity / net membership</text>'
        + ''.join(parts) + '</svg>\n')


def _lines(value: str, width: int) -> list[str]:
    return [line for paragraph in value.splitlines() for line in
            (textwrap.wrap(paragraph, width=max(12, width)) or [''])] or ['']


def sequence_diagram(diagram: dict) -> str:
    """Render an authored message sequence; never infer firmware execution from reads."""
    esc = html.escape
    participants = diagram['participants']
    width = max(720, len(participants) * 240)
    step = width / len(participants)
    centers = {p['id']: (i + 0.5) * step for i, p in enumerate(participants)}
    heading = _lines(diagram['title'], (width - 80) // 13)
    header_y = 70 + len(heading) * 24
    label_lines = [_lines(p['label'], 18) for p in participants]
    header_height = 24 + max(map(len, label_lines)) * 21
    y = header_y + header_height + 40
    messages = []
    for i, message in enumerate(diagram['messages'], 1):
        start, end = centers[message['sender']], centers[message['receiver']]
        self_message = start == end
        span = 100 if self_message else abs(end - start)
        lines = _lines(f'{i:02d}. {message["label"]}', int((span - 32) / 10))
        text_x = start + 60 if self_message else (start + end) / 2
        for number, line in enumerate(lines):
            messages.append(f'<text x="{text_x:g}" y="{y + number * 21}" text-anchor="middle">{esc(line)}</text>')
        line_y = y + len(lines) * 21
        if self_message:
            # Every lifeline has a half-column of room for a local action/return.
            path = f'M{start:g} {line_y}h80v25h-80'
        else:
            path = f'M{start:g} {line_y}H{end:g}'
        messages.append(f'<path d="{path}" class="message"/>')
        # Draw the arrowhead directly: avoid SVG marker IDs colliding across diagrams.
        arrow_y = line_y + 25 if self_message else line_y
        sign = 1 if self_message or end < start else -1
        messages.append(f'<path d="M{end + sign * 7:g} {arrow_y - 4}L{end:g} {arrow_y}l{sign * 7} 4" class="message"/>')
        y = line_y + (70 if self_message else 50)
    height = y + 25
    parts = [f'<rect class="paper" width="{width}" height="{height}"/>']
    for number, line in enumerate(heading):
        parts.append(f'<text class="title" x="28" y="{38 + number * 24}">{esc(line)}</text>')
    for participant, labels in zip(participants, label_lines, strict=True):
        x = centers[participant['id']]
        parts.append(f'<path d="M{x:g} {header_y + header_height}V{y}" class="lifeline"/>')
        parts.append(f'<rect x="{x - 100:g}" y="{header_y}" width="200" height="{header_height}" rx="5"/>')
        for number, line in enumerate(labels):
            parts.append(f'<text x="{x:g}" y="{header_y + 25 + number * 21}" text-anchor="middle">{esc(line)}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="sequence-svg" role="img" '
        f'aria-label="{esc(diagram["title"], quote=True)}" viewBox="0 0 {width} {height}">'
        f'<title>{esc(diagram["title"])}</title><desc>Authored intended sequence; not a measured execution trace.</desc>'
        '<style>.sequence-svg text{font:16px monospace;fill:#263445}.sequence-svg .title{font-size:21px;fill:#173b58}'
        '.sequence-svg rect{fill:#f8fafc;stroke:#c6d2dd}.sequence-svg .paper{fill:#fff;stroke:none}'
        '.sequence-svg .lifeline{fill:none;stroke:#c6d2dd;stroke-dasharray:5 5}'
        '.sequence-svg .message{fill:none;stroke:#426783;stroke-width:1.6}</style>'
        + ''.join(parts + messages) + '</svg>\n')


def render(report: dict) -> tuple[str, str]:
    p, esc = report['project'], html.escape
    md = f'# {p["title"]}\n\n{p["objective"]}\n\n'
    md += ('Project acceptance: **not established**. Physical verification: **not assessed**.\n\n'
           f'Reference target: `{report["target"]["mcu"]}`; board revision: '
           f'`{report["target"]["board_revision"]}`. Confirm the physical board separately.\n\n'
           f'Knowledge scope: **{"ready" if report["knowledge_scope_ready"] else "gaps remain"}**. '
           f'Build evidence: **{report["build"]["status"]}**.\n\n'
           f'Bundle revision: `{report["bundle_revision"]}`.\n\n'
           '## Requirements and verification plan\n\n')
    md += table(['ID', 'Requirement', 'Published workflows', 'Verification plan'],
        [[r['id'], r['description'], ', '.join(r['workflows']) or 'Not mapped', r['verification_plan']]
         for r in report['requirements']])
    sections = ['<p class="eyebrow">PRAXIS / ENGINEERING REPORT</p>',
        f'<h1>{esc(p["title"])}</h1><p class="lead">{esc(p["objective"])}</p>',
        '<p class="document-status"><strong>Document status.</strong> Design and evidence review. '
        'Project acceptance is not established; physical verification is not assessed.</p>',
        f'<p>Reference MCU: <strong>{esc(report["target"]["mcu"])}</strong>; reference board revision: '
        f'{esc(report["target"]["board_revision"])}. Confirm your physical board separately.</p>',
        '<div class="status">'
        f'<span>Knowledge scope: <strong>{"ready" if report["knowledge_scope_ready"] else "gaps remain"}</strong></span>'
        f'<span>Build: <strong>{esc(report["build"]["status"])}</strong></span>'
        '<span>Physical: <strong>not assessed</strong></span></div>',
        '<nav aria-label="Report sections"><a href="#connectivity">Wiring diagram</a> · '
        '<a href="#design">Design</a> · '
        + ('<a href="#diagrams">Sequence diagrams</a> · ' if p.get('diagrams') else '') +
        '<a href="#procedure">Procedure</a> · '
        '<a href="#build">Build evidence</a> · <a href="#references">Sources</a></nav>',
        f'<details><summary>Exact bundle and report identities</summary><p>Bundle: '
        f'<code>{report["bundle_revision"]}</code></p><p>Report: <code>{report["report_revision"]}</code></p></details>',
        '<h2>Requirements and verification plan</h2>',
        '<p>Each implementation check remains unassessed in reporting v1. The plans below describe checks to perform.</p>']
    for req in report['requirements']:
        status = '; '.join(f'{w["id"]}: {"knowledge ready" if w["knowledge_ready"] else "blocked"}'
                           for w in req['workflow_assessment']) or 'No published workflow mapping'
        sections.append(f'<article><h3>{esc(req["id"].replace("_", " ").capitalize())}</h3><p>{esc(req["description"])}</p>'
                        f'<p class="muted">{esc(status)}</p><p><strong>Verification plan.</strong> {esc(req["verification_plan"])}</p></article>')
    md += '\n## Design explanation (authored)\n\n'
    sections.append('<h2 id="design">Design explanation (authored)</h2>')
    links = {r['id']: r['file'] for r in report['references']}
    for item in p['explanations']:
        citations = ', '.join(f'[{key}]({links[key]})' for key in item['documents'])
        md += f'### {item["title"]}\n\n{item["explanation"]}\n\nSources: {citations}\n\n'
        refs = ' · '.join(f'<a href="{links[key]}">{esc(key)}</a>' for key in item['documents'])
        sections.append(f'<h3>{esc(item["title"])}</h3><p>{esc(item["explanation"])}</p><p>Sources: {refs}</p>')
    if p.get('diagrams'):
        md += '\n## Intended sequences (authored)\n\n'
        sections.append('<h2 id="diagrams">Intended sequences (authored)</h2>'
            '<p>These diagrams explain the intended design. They are not measured execution traces.</p>')
        for diagram in p['diagrams']:
            path = f'diagrams/{diagram["id"]}.svg'
            refs = ' · '.join(f'<a href="{links[key]}">{esc(key)}</a>' for key in diagram['documents'])
            citations = ', '.join(f'[{key}]({links[key]})' for key in diagram['documents'])
            md += (f'### {diagram["title"]}\n\n{diagram["description"]}\n\n'
                   f'![{diagram["title"]}]({path})\n\nSources: {citations}\n\n')
            sections.append(f'<h3>{esc(diagram["title"])}</h3><p>{esc(diagram["description"])}</p>'
                f'<a href="{path}">Open full-size SVG</a><div class="diagram">'
                + sequence_diagram(diagram) + f'</div><p>Sources: {refs}</p>')
    md += '\n## Connectivity\n\n![Scoped connectivity](schematic.svg)\n\n'
    if report.get('electrical_drawings'):
        md += ('\n## Electrical schematics\n\nNative CircuitikZ drawings and the multi-part report are in '
               '[the LaTeX authoring kit](latex/README.md). Generate the typeset PDF with '
               '`praxis project-pdf --report REPORT_DIR --output NEW_PDF_DIR`.\n\n')
        sections.append('<h2 id="electrical">Electrical schematics</h2><p>Native electrical drawings use '
            'published component values, declared terminal roles and exact net connections. '
            'These are scoped reference redrawings; unknown internals remain terminal blocks.</p>'
            '<p><a href="latex/electrical.tex">CircuitikZ source</a> · '
            '<a href="latex/report.tex">LaTeX report</a> · <a href="latex/README.md">Authoring kit</a></p>'
            '<!-- electrical-preview -->')
    sections.append('<h2 id="connectivity">Connectivity</h2><p>All endpoints of each selected net are retained. '
                    'Dashed external wiring is proposed, not confirmed fitted.</p>'
                    '<a href="schematic.svg">Open full-size SVG</a><div class="diagram">' + schematic(report) + '</div>')
    for net in report['nets']:
        md += f'\n### Net: {net["name"]}\n\n' + table(['Endpoint', 'Pin', 'Sheet', 'Sources'],
            [[e['endpoint'], e['pin'], e['sheet'], e['sources']] for e in net['endpoints']])
        sections.append(f'<h3>Net: {esc(net["name"])}</h3><table><tr><th>Endpoint</th><th>Pin</th><th>Sources</th></tr>'
            + ''.join(f'<tr><td>{esc(e["endpoint"])}</td><td>{esc(e["pin"])}</td><td>{esc(e["sources"])}</td></tr>'
                      for e in net['endpoints']) + '</table>')
    for title, values in [('Procedure', p['procedure']), ('Limitations', p['limitations'] + report['limits']),
                          ('Open gaps', report['gaps'])]:
        md += f'\n## {title}\n\n' + ''.join(f'{i}. {text}\n' for i, text in enumerate(values, 1))
        anchor = ' id="procedure"' if title == 'Procedure' else ''
        sections.append(f'<h2{anchor}>{title}</h2><ol>' + ''.join(f'<li>{esc(v)}</li>' for v in values) + '</ol>')
    md += '\n## Build evidence\n\n```json\n' + _json(report['build']).decode() + '```\n'
    sections.append('<h2 id="build">Build evidence</h2><pre>' + esc(_json(report['build']).decode()) + '</pre>')
    for title, rows, key in [('Complete source documents', report['references'], 'id'),
                              ('Project files', report['project_files'], 'path')]:
        md += f'\n## {title}\n\n'
        anchor = ' id="references"' if key == 'id' else ''
        sections.append(f'<h2{anchor}>{title}</h2><ul>')
        for row in rows:
            md += f'- [{row[key]}]({row["file"]}) — SHA-256 `{row["sha256"]}`\n'
            sections.append(f'<li><a href="{row["file"]}">{esc(row[key])}</a> '
                            f'<code>{row["sha256"]}</code></li>')
        sections.append('</ul>')
    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; style-src \'unsafe-inline\'; img-src \'self\' data:; base-uri \'none\'; form-action \'none\'">'
        f'<title>{esc(p["title"])}</title><style>'
        ':root{color-scheme:light;--ink:#182635;--muted:#526476;--line:#dce3e9;--navy:#173b58;--paper:#fff;--wash:#f6f8fa}'
        '*{box-sizing:border-box}html{scroll-padding-top:24px}body{max-width:1120px;margin:56px auto;padding:0 32px 64px;'
        'background:var(--paper);color:var(--ink);font:16px/1.75 system-ui,-apple-system,"Segoe UI",sans-serif}'
        'h1,h2,h3{color:var(--ink);line-height:1.3;letter-spacing:-.02em}h1{font-size:clamp(30px,4vw,44px);max-width:940px;margin:14px 0 20px}'
        'h2{font-size:26px;margin:56px 0 22px;padding-bottom:14px;border-bottom:1px solid var(--line)}h3{font-size:19px;margin:24px 0 10px}'
        'p{margin:12px 0 18px}.eyebrow{font-size:11px;letter-spacing:.18em;font-weight:750;color:var(--navy)}'
        '.lead{font-size:18px;color:var(--muted);max-width:940px}.muted{color:var(--muted);font-size:14px}'
        'a{color:#205d83;text-underline-offset:3px}a:focus-visible,summary:focus-visible{outline:2px solid #205d83;outline-offset:4px}'
        '.document-status{border-top:1px solid var(--ink);border-bottom:1px solid var(--line);'
        'padding:14px 0;font-size:14px;color:var(--muted)}'
        'article{border-bottom:1px solid var(--line);padding:6px 0 20px;margin:12px 0}article:last-of-type{border-bottom:none}'
        '.status{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:28px 0}'
        '.status span{padding:12px 0;border-bottom:1px solid var(--line);font-size:13px}'
        '.status strong{display:block;color:var(--navy);font-size:15px;margin-top:3px;overflow-wrap:anywhere}'
        'nav{padding:16px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);font-size:14px;line-height:2.2}'
        'details{padding:14px 0;color:var(--muted);font-size:13px}summary{cursor:pointer}'
        '.diagram{overflow:auto;border:1px solid var(--line);border-radius:6px;background:#fff;margin:16px 0 24px}'
        '.diagram svg{display:block;width:100%;min-width:680px;height:auto}table{border-collapse:collapse;width:100%;font-size:14px;margin:16px 0 28px}'
        'th,td{border-bottom:1px solid var(--line);padding:12px;text-align:left;vertical-align:top;overflow-wrap:anywhere}'
        'th{background:var(--wash);font-weight:650;color:var(--muted)}code{overflow-wrap:anywhere;font:12px/1.7 ui-monospace,monospace}'
        'pre{overflow:auto;padding:20px;background:var(--wash);border:1px solid var(--line);border-radius:6px;font-size:13px}'
        'li{margin-bottom:8px}li code{display:inline-block;margin-left:6px}::selection{background:#dbeaf4}'
        '@media(max-width:640px){body{margin:28px auto;padding:0 20px 36px}.status{grid-template-columns:1fr}h2{font-size:23px}th,td{padding:8px}}'
        '@page{size:A4;margin:16mm}@media print{body{max-width:none;margin:0;padding:0;font-size:10pt}h1{font-size:26pt}'
        'h2{font-size:17pt;break-after:avoid}h3{break-after:avoid}nav,details{display:none}.status{grid-template-columns:repeat(3,1fr)}'
        '.diagram{overflow:visible}.diagram svg{min-width:0;width:100%}pre{white-space:pre-wrap;overflow-wrap:anywhere}'
        'thead{display:table-header-group}tr{break-inside:avoid}a{color:var(--navy)}}</style>'
        '</head><body>' + '\n'.join(sections) + '</body></html>\n')
    return md, page


def write_report(bundle: Bundle, spec: ProjectSpec, output: Path, workspace: Path | None = None,
                 checked_build: dict | None = None) -> dict:
    output = output.absolute()
    if output.exists() or output.is_symlink():
        raise PraxisError('IMMUTABLE_REPORT', 'Choose a new report directory; previous reports are immutable')
    if output.resolve().is_relative_to(bundle.root):
        raise PraxisError('INVALID_PATH', 'Project reports cannot be written inside a knowledge bundle')
    report, files = prepare(bundle, spec, workspace, checked_build)
    markdown, page = render(report)
    files.update({'report.json': _json(report), 'REPORT.md': markdown.encode(),
                  'index.html': page.encode(), 'schematic.svg': schematic(report).encode()})
    files.update({f'diagrams/{item.id}.svg': sequence_diagram(item.model_dump()).encode()
                  for item in spec.diagrams})
    from praxis.project_latex import sources
    files.update(sources(report))
    manifest = {'format': 'praxis-project-files-v1', 'report_revision': report['report_revision'],
                'files': {name: digest(raw) for name, raw in sorted(files.items())}}
    files['manifest.json'] = _json(manifest)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.project-report-', dir=output.parent) as directory:
        staging = Path(directory) / 'report'
        staging.mkdir()
        for name, raw in sorted(files.items()):
            path = staging / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(raw)
        if output.exists() or output.is_symlink():
            raise PraxisError('IMMUTABLE_REPORT', 'Report output appeared during rendering; choose a new directory')
        os.rename(staging, output)
    return {'report_revision': report['report_revision'], 'output': str(output),
            'knowledge_scope_ready': report['knowledge_scope_ready'], 'project_accepted': False,
            'build_status': report['build']['status'], 'gaps': report['gaps']}
