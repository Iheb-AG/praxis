"""Electrical drawing recipes from published component kinds and exact terminal nets.

No inference from reference prefixes, board names or MCU families is permitted.
Unknown symbols remain terminal blocks. Drawings cover the selected scope only.
"""
from __future__ import annotations

from praxis.board import COMPONENT_COLUMNS
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.latex_text import tex
from praxis.netlist import NetlistIndex


def catalog(markdown: str) -> dict[str, dict]:
    lines = markdown.splitlines()
    start = next((i for i, line in enumerate(lines)
                  if line.startswith('| ') and NetlistIndex._cells(line) == COMPONENT_COLUMNS), None)
    if (start is None or start + 1 >= len(lines)
            or NetlistIndex._cells(lines[start + 1]) != ['---'] * len(COMPONENT_COLUMNS)):
        raise PraxisError('INVALID_COMPONENTS', 'Published component catalog lacks its canonical table')
    result = {}
    for line in lines[start + 2:]:
        if not line.strip():
            continue
        row = NetlistIndex._cells(line)
        if len(row) != len(COMPONENT_COLUMNS):
            raise PraxisError('INVALID_COMPONENTS', 'Malformed published component row')
        ref, value, kind, fitted, package, sheet, raw_pins, properties, sources = row
        if not ref or ref in result or fitted not in ('True', 'False') or not sources:
            raise PraxisError('INVALID_COMPONENTS', 'Invalid component identity, fitted status or provenance')
        pins = {}
        for token in raw_pins.split(';'):
            number, separator, name = token.strip().partition('=')
            if not separator or not number or not name or number in pins:
                raise PraxisError('INVALID_COMPONENTS', f'Invalid declared terminals for {ref}')
            pins[number] = name
        parsed = load_json(properties)
        if not isinstance(parsed, dict):
            raise PraxisError('INVALID_COMPONENTS', f'Invalid properties for {ref}')
        result[ref] = dict(ref=ref, value=value, kind=kind, fitted=fitted == 'True',
                           package=package, sheet=sheet, pins=pins, properties=parsed, sources=sources)
    return result


def drawings(components: list[dict], nets: list[dict]) -> list[dict]:
    """Recognize only explicit two-terminal primitives and unambiguous LED branches."""
    by_ref = {c['ref']: c for c in components}
    endpoints = {p['endpoint']: p for net in nets for p in net['endpoints']}
    members = {n['name']: {p['endpoint'] for p in n['endpoints']} for n in nets}

    def terminals(component):
        return [dict(number=number, **endpoints[f'{component["ref"]}:{number}'])
                for number in sorted(component['pins']) if f'{component["ref"]}:{number}' in endpoints]

    def diode(component):
        if len(component['pins']) != 2 or set(component['pins'].values()) != {'A', 'K'}:
            return None
        pins = {p['pin']: p for p in terminals(component)}
        return pins if pins.keys() == {'A', 'K'} else None

    result, used = [], set()

    def add(kind, parts, **data):
        connections = [p for c in parts for p in terminals(c)]
        result.append(dict(id=f'electrical_{len(result):03}', kind=kind,
            title=' / '.join(c['ref'] + ' — ' + c['value'] for c in parts),
            components=[c['ref'] for c in parts], connections=connections,
            sources=[c['sources'] for c in parts], **data))
        used.update(c['ref'] for c in parts)

    for led in sorted(components, key=lambda c: c['ref']):
        pins = diode(led) if led['kind'] == 'led' and led['fitted'] else None
        if pins is None:
            continue
        candidates = []
        for resistor in components:
            terms = terminals(resistor)
            if (resistor['kind'] != 'resistor' or not resistor['fitted']
                    or resistor['ref'] in used or len(resistor['pins']) != 2 or len(terms) != 2):
                continue
            for inner in terms:
                if members[pins['A']['net']] == {pins['A']['endpoint'], inner['endpoint']}:
                    outer = next(p for p in terms if p != inner)
                    candidates.append((resistor, outer))
        if len(candidates) == 1:
            resistor, outer = candidates[0]
            add('led_resistor', [resistor, led], left=outer['net'], middle=pins['A']['net'],
                right=pins['K']['net'], resistor=resistor['ref'] + ' / ' + resistor['value'],
                led=led['ref'] + ' / ' + led['value'])

    for ref, component in sorted(by_ref.items()):
        if ref in used:
            continue
        terms = terminals(component)
        if not terms:
            continue
        common = dict(omitted_pins=sorted(set(component['pins']) - {p['number'] for p in terms}),
                      fitted=component['fitted'])
        if component['kind'] == 'resistor' and component['fitted'] and len(component['pins']) == len(terms) == 2:
            add('resistor', [component], left=terms[0]['net'], right=terms[1]['net'], **common)
        elif component['kind'] == 'led' and component['fitted'] and diode(component):
            pins = diode(component)
            add('led', [component], left=pins['A']['net'], right=pins['K']['net'], **common)
        elif (component['kind'] == 'switch' and component['fitted']
                and component['properties'].get('contact') == 'normally-open'):
            raw = component['properties'].get('internal_groups', '')
            groups = [set(part.strip().split(',')) for part in raw.split(' and ')] if isinstance(raw, str) else []
            assigned = {p['number']: p['net'] for p in terms}
            if (len(groups) == 2 and not groups[0] & groups[1]
                    and set.union(*groups) == set(component['pins']) == assigned.keys()
                    and all(len({assigned[p] for p in group}) == 1 for group in groups)):
                add('normally_open_switch', [component], left=assigned[sorted(groups[0])[0]],
                    right=assigned[sorted(groups[1])[0]], groups=[sorted(g) for g in groups], **common)
            else:
                add('terminal_block', [component], **common)
        else:
            # In particular a fitted solder bridge is not automatically declared closed.
            add('terminal_block', [component], **common)
    return result


def circuit(figure: dict) -> str:
    """Native CircuitikZ, containing only fixed commands and escaped published labels."""
    def node(value):
        return r'\shortstack{\ttfamily ' + tex(value) + '}'
    parts = [r'\begin{center}\begin{circuitikz}[european resistors]']
    kind = figure['kind']
    if kind in {'resistor', 'led', 'normally_open_switch', 'led_resistor'}:
        parts.append(r'\draw (0,0) node[ocirc,label=below:{' + node(figure['left']) + '}] {}')
        if kind == 'led_resistor':
            parts.append(r' to[R,l={' + tex(figure['resistor']) + r'}] (3.5,0) node[circ,label=below:{'
                         + node(figure['middle']) + r'}] {} to[led,l={' + tex(figure['led']) + r'}] (7,0)')
        else:
            symbol = {'resistor': 'R', 'led': 'led', 'normally_open_switch': 'nos'}[kind]
            parts.append(' to[' + symbol + ',l={' + tex(figure['title']) + '}] (7,0)')
        parts.append(' node[ocirc,label=below:{' + node(figure['right']) + '}] {};')
    else:
        terms = figure['connections']
        height = max(1.5, 0.7 * len(terms) + 0.5)
        parts.append(f'\\draw (0,0) rectangle (3,{height:g});')
        parts.append(f'\\node[align=center,text width=2.6cm,font=\\footnotesize] at (1.5,{height / 2:g}) '
                     + '{' + tex(figure['title']) + '};')
        for i, terminal in enumerate(terms):
            y = height - 0.55 - i * 0.7
            parts.append(f'\\draw (3,{y:g}) -- (4,{y:g}) node[ocirc] {{}} '
                + 'node[right,align=left] {' + tex(terminal['endpoint'] + ' / ' + terminal['pin'])
                + r'\quad\texttt{' + tex(terminal['net']) + '}};')
    parts.append(r'\end{circuitikz}\end{center}')
    return '\n'.join(parts) + '\n'


def circuit_pages(figures: list[dict]) -> list[list[dict]]:
    # Fixed small pages keep native symbols and their full terminal legends legible.
    pages, page, weight = [], [], 0
    for figure in figures:
        cost = 2 if len(figure['connections']) > 5 else 1
        if page and weight + cost > 3:
            pages.append(page)
            page, weight = [], 0
        page.append(figure)
        weight += cost
    if page:
        pages.append(page)
    return pages


def electrical_document(report: dict, preamble: str) -> str:
    pages = circuit_pages(report['electrical_drawings'])
    content = [preamble, r'\begin{document}']
    for page_number, figures in enumerate(pages, 1):
        if page_number > 1:
            content.append(r'\clearpage')
        content.extend([r'\section*{Electrical schematic — scoped reference}',
            'Sheet ' + str(page_number) + ' / ' + str(len(pages)) + '. Identical net labels denote connections. '
            'Distinct nets remain separate. External jumpers are proposed; physical assembly is unconfirmed.'])
        for figure in figures:
            content.append(r'\subsection*{' + tex(figure['title']) + '}')
            content.append(circuit(figure))
            content.append(r'{\small ' + tex('; '.join(p['endpoint'] + ' (' + p['pin'] + ') = ' + p['net']
                for p in figure['connections'])) + r'\par}')
            if figure.get('groups'):
                content.append('Declared switch groups: ' + tex(str(figure['groups'])) + '.')
            if figure.get('omitted_pins'):
                content.append('Pins outside the selected drawing scope: ' + tex(', '.join(figure['omitted_pins'])) + '.')
            if figure.get('fitted') is False:
                content.append('Documented as not fitted; no internal connection is asserted.')
            if figure['kind'] == 'terminal_block':
                content.append('Terminal representation only; no internal conducting state is inferred.')
            content.append(r'{\footnotesize\emph{Source: }' + tex('; '.join(figure['sources'])) + r'\par}')
    if not pages:
        content.append('Electrical component evidence is unavailable for this scope. No electrical circuit was inferred.')
    content.append(r'\end{document}')
    return '\n\n'.join(content) + '\n'
