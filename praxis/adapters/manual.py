"""Deterministic register evidence candidates, never reviewed operating facts.

Consumes complete extracted text/table parts from the existing PDF/HTML/text
adapters. Literal configured symbols bind evidence to header declarations.
Unsupported layouts remain gaps. Visual relations and operating semantics are
not inferred. Full source tables stay untouched in the evidence archive.
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from typing import Literal

from pydantic import Field, model_serializer

from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.models import ManualSpec, Record

FORMAT = 'praxis-manual-review/v1'
MAX_PACKET = 256 * 1024
MAX_FACTS = 2000
MAX_HINTS = 500
HEADING = re.compile(r'\(([A-Za-z_][A-Za-z0-9_]{0,127})\)\s*$')
SECTION = re.compile(r'^\d+(?:\.\d+)+\s+')
SYMBOL = re.compile(r'\(([A-Za-z_][A-Za-z0-9_]{0,127})\)')
FIELD = re.compile(r'^Bits?\s+([0-9]{1,2})(?::([0-9]{1,2}))?\s+([A-Za-z_][A-Za-z0-9_]*)(?:\[[^\]]*\])?(?=[:\s]|$)', re.I)
REQUIREMENT = re.compile(r'\b(?:must|shall|required|before|only when|reserved|cleared|read.only|write.only)\b', re.I)


class Candidate(Record):
    register_name: str = Field(alias='register')
    kind: Literal['offset', 'reset', 'access', 'field']
    field: str | None = None
    field_views: list[str] = []
    value: int | str | dict[str, int]
    qualifier: str = ''
    status: Literal['unreviewed', 'matches_declaration', 'conflict']
    locators: list[str] = Field(min_length=1)
    section_contexts: list[str] = []
    review_required: Literal[True] = True

    @model_serializer(mode='wrap')
    def serialize(self, handler):
        value = handler(self)
        if not self.field_views:
            value.pop('field_views', None)
        return value


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def number(text):
    """Only one hex literal (possibly spaced) or a decimal literal plus a note.

    Expressions, multiple resets, per-instance values and prose-only values are
    deliberately unsupported. Parenthetical reset-domain qualifiers survive.
    """
    value, separator, note = text.partition('(')
    value = value.strip()
    if len(value) > 128 or separator and not note.rstrip().endswith(')'):
        return None
    qualifier = ('(' + note).strip() if separator else ''
    if re.fullmatch(r'0[xX][0-9a-fA-F]+(?:\s+[0-9a-fA-F]{4})*', value):
        parsed = int(''.join(value.split()), 16)
    elif re.fullmatch(r'[0-9]+', value):
        parsed = int(value, 10)
    else:
        return None
    return (parsed, qualifier) if parsed <= 0xFFFFFFFF else None


def symbols_for(entity, declaration, discovery, spec):
    names = {}
    prefix = discovery.prefix if discovery and discovery.prefix else entity.upper()
    overrides = discovery.register_prefixes if discovery else {}
    aliases = spec.register_symbols.get(entity, {})
    if not aliases.keys() <= {r.name for r in declaration.registers}:
        raise PraxisError('INVALID_MANUAL_CONFIG', 'Manual symbols name an undeclared register')
    for register in declaration.registers:
        # Explicit aliases replace the default; no fuzzy matching or invented
        # mapping from a flattened C member to a manufacturer's document symbol.
        for symbol in aliases.get(register.name, [overrides.get(register.name, prefix + '_' + register.name)]):
            if symbol in names and names[symbol] != register.name:
                raise PraxisError('AMBIGUOUS_MANUAL_SYMBOL', f'{symbol}: multiple register identities')
            names[symbol] = register.name
    return names


def prepare(declaration, parts, *, entity, target, source, spec=None, discovery=None, registers=None,
            locators=None):
    spec = spec or ManualSpec()
    available = {r.name: r for r in declaration.registers}
    if len({p['locator'] for p in parts}) != len(parts):
        raise PraxisError('IMPORT_INTEGRITY', 'Duplicate evidence locators')
    if locators is not None:
        if (not locators or len(locators) != len(set(locators))
                or not set(locators) <= {p['locator'] for p in parts}):
            raise PraxisError('UNKNOWN_LOCATOR', 'Select unique complete evidence locators from this archive')
        parts = [p for p in parts if p['locator'] in set(locators)]
    selected = list(available) if registers is None else registers
    if (not selected or len(selected) != len(set(selected)) or not set(selected) <= available.keys()):
        raise PraxisError('INVALID_INPUT', 'Select unique declared register names or omit the selection')
    selected = set(selected)
    symbols = symbols_for(entity, declaration, discovery, spec)
    facts, hints, issues, used = [], [], [], {}
    active, active_context, previous_page = None, '', None
    labels = {" ".join(label.split()).casefold(): kind
              for kind, values in spec.labels.items() for label in values}

    def mark(part):
        used[part['locator']] = {k: part[k] for k in ('locator', 'artifact', 'artifact_sha256')}
        used[part['locator']]['table_locators'] = [t.get('locator', part['locator'] + f'/table:{i}')
            for i, t in enumerate(part.get('tables', []), 1)]

    def issue(code, locator, text):
        if len(issues) >= MAX_FACTS:
            raise PraxisError('REVIEW_LIMIT', 'Select fewer registers or a smaller evidence archive')
        issues.append(dict(code=code, locator=locator, text=text))

    def add(part, name, kind, raw, locator, field=None):
        if name not in selected:
            return
        register = available[name]
        qualifier, status = '', 'unreviewed'
        if kind == 'access':
            access = {'read-only': 'RO', 'read only': 'RO', 'ro': 'RO',
                      'read/write': 'RW', 'read-write': 'RW', 'rw': 'RW',
                      'write-only': 'WO', 'write only': 'WO', 'wo': 'WO'}
            value = access.get(raw.strip().casefold())
            if value is None:
                issue('UNSUPPORTED_ACCESS', locator, raw)
                return
        elif kind == 'field':
            high, low = raw
            if low > high or high >= register.width:
                issue('FIELD_RANGE', locator, f'{name}.{field}: bits {high}:{low} outside C member width')
                return
            value = dict(lsb=low, width=high-low+1, mask=((1 << (high-low+1))-1) << low)
            matches = [f for f in register.fields if f.name == field]
            view_names = [view for view, record in sorted(register.field_views.items())
                          if any(f.name == field for f in record.fields)]
            matches.extend(f for view in view_names for f in register.field_views[view].fields if f.name == field)
            if not matches:
                issue('UNMAPPED_FIELD', locator, f'{name}.{field}: no exact header field')
                return
            if len({(f.lsb, f.width, f.mask) for f in matches}) != 1:
                issue('AMBIGUOUS_FIELD_VIEW', locator, f'{name}.{field}: views disagree; review each interpretation')
                return
            known = matches[0]
            status = ('matches_declaration' if (known.lsb, known.width, known.mask) ==
                (value['lsb'], value['width'], value['mask']) else 'conflict')
        else:
            parsed = number(raw)
            if parsed is None:
                issue('UNSUPPORTED_VALUE', locator, f'{name}.{kind}: {raw}')
                return
            value, qualifier = parsed
            expected = register.offset if kind == 'offset' else register.reset
            # A reset-domain qualifier is never promoted to an unconditional fact.
            if expected is not None and not qualifier:
                status = 'matches_declaration' if expected == value else 'conflict'
            if kind == 'reset' and value >= 1 << register.width:
                status = 'conflict'
        if len(facts) >= MAX_FACTS:
            raise PraxisError('REVIEW_LIMIT', 'Select fewer registers before preparing review')
        facts.append(Candidate(register=name, kind=kind, field=field, value=value,
            field_views=view_names if kind == 'field' else [],
            qualifier=qualifier, status=status, locators=[locator],
            section_contexts=[active_context] if '/line:' in locator and active_context else []))
        mark(part)

    def table(part, record, index):
        rows = record.get('rows', [])
        locator = record.get('locator', part['locator'] + f'/table:{index}')
        if not rows or not isinstance(rows[0], list):
            return
        columns = {}
        for i, cell in enumerate(rows[0]):
            kind = labels.get(' '.join(str(cell or '').split()).casefold())
            if kind:
                if kind in columns:
                    issue('AMBIGUOUS_TABLE_COLUMNS', locator, 'Repeated semantic column; table not interpreted')
                    return
                columns[kind] = i
        if 'register' not in columns or not set(columns) & {'offset', 'reset', 'access', 'bits'}:
            return
        for row_number, row in enumerate(rows[1:], 2):
            if not isinstance(row, list) or len(row) != len(rows[0]):
                issue('IRREGULAR_TABLE', locator + f'/row:{row_number}', 'Retain and review the complete source table')
                continue
            if any(len(str(cell or '')) > 4096 for cell in row):
                raise PraxisError('REVIEW_LIMIT', 'Table has oversized cells; inspect the complete source table')
            token = str(row[columns['register']] or '').strip()
            name = symbols.get(token)
            if name is None and spec.table_scopes.get(locator) == entity and token in available:
                name = token
            if name is None:
                if token in selected:
                    issue('UNSCOPED_TABLE', locator + f'/row:{row_number}', 'Short register name requires an explicit table scope')
                continue
            if name not in selected:
                continue
            for kind in ('offset', 'reset', 'access'):
                if kind in columns and row[columns[kind]] is not None:
                    add(part, name, kind, str(row[columns[kind]]), locator + f'/row:{row_number}/column:{columns[kind]+1}')
            if 'field' in columns and 'bits' in columns:
                bits = re.fullmatch(r'([0-9]{1,2})(?::([0-9]{1,2}))?', str(row[columns['bits']] or '').strip())
                if bits:
                    add(part, name, 'field', (int(bits[1]), int(bits[2] or bits[1])),
                        locator + f'/row:{row_number}', field=str(row[columns['field']] or '').strip())

    # Numeric PDF page order; selected-page gaps break inherited register context.
    ordered = sorted(parts, key=lambda p: (p.get('page') is None, p.get('page', 0), p['locator']))
    for part in ordered:
        page = part.get('page')
        if page is None or previous_page is None or page != previous_page + 1:
            active, active_context = None, ''
        previous_page = page
        for line_number, original in enumerate(part['text'].splitlines(), 1):
            line = ' '.join(original.split())
            locator = part['locator'] + f'/line:{line_number}'
            if len(line) > 4096:
                raise PraxisError('REVIEW_LIMIT', 'Evidence has oversized lines; inspect the original part')
            heading = HEADING.search(line)
            if SECTION.match(line):
                # Any new numbered section ends inherited register context. A
                # heading may wrap after its exact symbol or include a mode note.
                matches = [symbols[m[1]] for m in SYMBOL.finditer(line) if m[1] in symbols]
                active = matches[0] if len(matches) == 1 else None
                active_context = line
                if active in selected:
                    mark(part)
                continue
            if heading:
                active, active_context = symbols.get(heading[1]), line
                if active in selected:
                    mark(part)
                continue
            if active not in selected:
                continue
            label, colon, raw = line.partition(':')
            kind = labels.get(label.strip().casefold()) if colon else None
            if kind in ('offset', 'reset', 'access'):
                add(part, active, kind, raw.strip(), locator)
            match = FIELD.match(line)
            if match and match[3].casefold() != 'reserved':
                add(part, active, 'field', (int(match[1]), int(match[2] or match[1])), locator, match[3])
            if REQUIREMENT.search(line):
                if len(hints) >= MAX_HINTS:
                    raise PraxisError('REVIEW_LIMIT', 'Select fewer registers or evidence pages for review hints')
                hints.append(dict(register=active, locator=locator, text=line,
                    status='incomplete source line; read the complete evidence part before review'))
                mark(part)
        for i, record in enumerate(part.get('tables', []), 1):
            table(part, record, i)

    grouped = defaultdict(list)
    for fact in facts:
        grouped[(fact.register_name, fact.kind, fact.field)].append(fact)
    merged, conflicts = [], []
    for key, values in sorted(grouped.items(), key=lambda row: tuple(v or '' for v in row[0])):
        alternatives = defaultdict(list)
        for fact in values:
            alternatives[(canonical(fact.value), fact.qualifier)].append(fact)
        disagree = len({value for value, _ in alternatives}) > 1
        if disagree or any(f.status == 'conflict' for f in values):
            conflicts.append(dict(register=key[0], kind=key[1], field=key[2],
                reason='Conflicting source values or disagreement with the header; reviewed resolution required'))
        for _, same in sorted(alternatives.items()):
            first = same[0]
            merged.append(first.model_copy(update={'locators': sorted({locator for f in same for locator in f.locators}),
                'section_contexts': sorted({context for f in same for context in f.section_contexts}),
                'status': 'conflict' if disagree else first.status}).model_dump(by_alias=True))
    gaps = {}
    for name in sorted(selected):
        present = {f['kind'] for f in merged if f['register'] == name}
        fields = {f['field'] for f in merged if f['register'] == name and f['kind'] == 'field'}
        gaps[name] = dict(missing_categories=sorted({'offset', 'reset', 'access'} - present),
            missing_field_positions=sorted({f.name for f in available[name].fields} - fields))
        if available[name].field_views:
            gaps[name]['missing_view_field_positions'] = {
                view: sorted({f.name for f in record.fields} - fields)
                for view, record in sorted(available[name].field_views.items())}
    result = dict(format=FORMAT, status='pending-review', review_required=True,
        publication_ready=False, target=target, entity=entity, source=source,
        parser='literal-register-evidence-v1', parser_config_sha256=digest(canonical(spec.model_dump())),
        declaration_sha256=digest(canonical(declaration.model_dump())),
        register_symbols={k: v for k, v in sorted(symbols.items()) if v in selected},
        selected_registers=sorted(selected), selected_evidence_locators=sorted(p['locator'] for p in parts),
        candidates=merged, conflicts=conflicts, gaps=gaps,
        review_hints=hints, extraction_issues=issues, evidence_parts=[used[k] for k in sorted(used)],
        counts=dict(parts_examined=len(ordered), matching_parts=len(used), candidates=len(merged),
                    conflicts=len(conflicts), registers_with_candidates=len({f['register'] for f in merged})),
        remaining_review=['Target/revision and per-instance applicability, including reset-domain qualifiers',
            'Operating semantics, field encodings, side effects and reserved-bit handling',
            'Readiness checks, bounded waits, clocks, dependencies, errata and electrical limits',
            'Package pin availability and board wiring from separate authority sources',
            'Diagrams, scans, OCR errors and unsupported or ambiguous text/table layouts'],
        limits=['A header match is not semantic review or hardware qualification.',
            'No model, embeddings, OCR, image interpretation, network or publication was used.',
            'Candidates do not replace or modify complete source tables or reviewed peripheral documents.'])
    result['packet_sha256'] = digest(canonical(result))
    if len(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False).encode()) > MAX_PACKET:
        raise PraxisError('REVIEW_LIMIT', 'Review packet exceeds 256 KiB; select fewer complete registers')
    return result
