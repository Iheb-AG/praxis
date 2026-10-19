"""Editable engineering-report parts and native LaTeX/CircuitikZ source.

The assistant authors the project text and cited design through ProjectSpec. These
templates keep generated evidence separate from prose and escape every text field.
"""
from __future__ import annotations

import json

from praxis.electrical import electrical_figure, electrical_document
from praxis.latex_text import breakable, tex

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=22mm,headheight=16pt]{geometry}
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{Latin Modern Mono}
\usepackage{microtype,graphicx,longtable,array,booktabs,fancyhdr,xurl,needspace}
\usepackage[unicode,hidelinks]{hyperref}
\usepackage[europeanresistors]{circuitikz}
\usetikzlibrary{arrows.meta,backgrounds}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\raggedbottom
\setcounter{tocdepth}{1}
\emergencystretch=3em
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily PRAXIS / PROJECT ENGINEERING}
\fancyhead[R]{\small\sffamily Reference design}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\newcommand{\reftext}[1]{{\small\sffamily #1}}
\hypersetup{pdfauthor={Praxis project report}}
'''


def _prose(value: str) -> str:
    return '\n\n'.join(tex(part.strip()) for part in value.split('\n\n')) + '\n'


def _list(values: list[str]) -> str:
    return ('\\begin{enumerate}\n' + ''.join('\\item ' + tex(v) + '\n' for v in values)
            + '\\end{enumerate}\n') if values else 'None recorded.\n'


def _refs(documents: list[str], lookup: dict) -> str:
    return r'\reftext{Sources: ' + '; '.join(tex(d) + ' [R' + str(lookup[d]) + ']' for d in documents) + '}\n'


def _sequence(diagram: dict) -> str:
    """Place each message below the actual preceding text box, never a fixed row."""
    participants = diagram['participants']
    count = len(participants)
    positions = {p['id']: (i + .5) / count for i, p in enumerate(participants)}
    code = [r'\begin{center}\begin{tikzpicture}[>=Stealth,x=\linewidth]']
    for number, participant in enumerate(participants):
        width = .90 / count
        code.append(f'\\node[draw,anchor=north,align=center,text width={width:g}\\linewidth,'
                    'minimum height=11mm,inner sep=3pt,font=\\small\\sffamily] '
                    f'(actor{number}) at ({positions[participant["id"]]:g},0) '
                    + '{' + tex(participant['label']) + '};')
    code.append(r'\coordinate (row0) at ([yshift=-4mm]current bounding box.south);')
    for number, message in enumerate(diagram['messages'], 1):
        start, end = positions[message['sender']], positions[message['receiver']]
        label = tex(f'{number:02d}. {message["label"]}')
        if start == end:
            # Use the adjacent lane for the local-action label; keep the loop
            # under the label, so it cannot cross this or the next message.
            direction = 1 if start <= .5 else -1
            mid = start + direction * .44 / count
            width = min(.90, 2 / count - .05)
        else:
            mid = (start + end) / 2
            width = min(.90, max(abs(start - end) - .035, 2 / count - .05))
        mid = max(width / 2 + .015, min(1 - width / 2 - .015, mid))
        code.append(f'\\node[anchor=north,align=center,text width={width:g}\\linewidth,'
                    'fill=white,inner sep=2pt,font=\\footnotesize] '
                    f'(message{number}) at ({mid:g},0 |- row{number-1}) '
                    + '{' + label + '};')
        code.append(f'\\coordinate (arrow{number}) at ([yshift=-2pt]message{number}.south);')
        if start == end:
            turn = start + direction * .30 / count
            code.append(f'\\coordinate (return{number}) at ([yshift=-3mm]arrow{number});')
            code.append(f'\\draw[->] ({start:g},0 |- arrow{number}) -- '
                        f'({turn:g},0 |- arrow{number}) -- ({turn:g},0 |- return{number}) '
                        f'-- ({start:g},0 |- return{number});')
            code.append(f'\\coordinate (row{number}) at ([yshift=-3mm]return{number});')
        else:
            code.append(f'\\draw[->] ({start:g},0 |- arrow{number}) -- ({end:g},0 |- arrow{number});')
            code.append(f'\\coordinate (row{number}) at ([yshift=-3mm]arrow{number});')
    code.append(r'\begin{pgfonlayer}{background}')
    for number, _ in enumerate(participants):
        code.append(f'\\draw[dashed,black!30] (actor{number}.south) -- '
                    f'(actor{number}.south |- row{len(diagram["messages"])});')
    code.extend([r'\end{pgfonlayer}', r'\end{tikzpicture}\end{center}'])
    return '\n'.join(code) + '\n'


def sources(report: dict) -> dict[str, bytes]:
    project = report['project']
    lookup = {r['id']: i for i, r in enumerate(report['references'], 1)}
    files = {}
    title = (r'\thispagestyle{empty}' + '\n'
        + r'{\sffamily\small PROJECT ENGINEERING REPORT}\par\vspace{5mm}' + '\n'
        + r'{\LARGE\bfseries ' + tex(project['title']) + r'\par}\vspace{3mm}' + '\n'
        + _prose(project['objective']) + r'\par\vspace{3mm}' + '\n'
        + r'\begin{tabular}{@{}p{.24\linewidth}p{\dimexpr.76\linewidth-2\tabcolsep\relax}@{}}\toprule' + '\n'
        + r'Document ID & ' + tex(project['id']) + r'\\' + '\n'
        + r'Reference MCU & ' + tex(report['target']['mcu']) + r'\\' + '\n'
        + r'Reference PCB & ' + tex(report['target']['board_revision']) + r'\\' + '\n'
        + r'Knowledge scope & ' + ('Ready for the declared scope' if report['knowledge_scope_ready'] else 'Open gaps remain') + r'\\' + '\n'
        + r'Build evidence & ' + tex(report['build']['status'].replace('_', ' ')) + r'\\' + '\n'
        + r'Physical verification & Not assessed\\\bottomrule\end{tabular}' + '\n'
        + r'\vspace{3mm}\par{\small Document status: design and evidence review. Overall project acceptance '
        + r'is not established. Physical PCB revision and assembly must be confirmed separately.}' + '\n'
        + r'\tableofcontents\clearpage' + '\n')
    files['sections/00-front.tex'] = title
    requirements = [r'\section{Project scope and requirements}', _prose(project['objective'])]
    for requirement in report['requirements']:
        requirements.append(r'\subsection{' + tex(requirement['id'].replace('_', ' ').capitalize()) + '}')
        requirements.append(_prose(requirement['description']))
        requirements.append(r'\textbf{Knowledge route.} ' + tex(', '.join(requirement['workflows']) or 'Unmapped') + '\n')
        requirements.append(r'\textbf{Verification plan.} ' + tex(requirement['verification_plan']) + '\n')
        requirements.append(r'{\small Implementation verification: not assessed.}\par')
    files['sections/01-requirements.tex'] = '\n'.join(requirements)
    design = [r'\section{Design rationale}',
              'The following explanations and message sequences are authored design interpretations, '
              'not measured execution traces. Their source references establish traceability, not automatic approval.']
    for explanation in project['explanations']:
        design.extend([r'\subsection{' + tex(explanation['title']) + '}', _prose(explanation['explanation']),
                       _refs(explanation['documents'], lookup)])
    for diagram in project.get('diagrams', []):
        design.extend([r'\par\medskip\noindent\begin{minipage}{\linewidth}',
                       r'\subsection{' + tex(diagram['title']) + '}', _prose(diagram['description']),
                       _sequence(diagram), _refs(diagram['documents'], lookup), r'\end{minipage}\par'])
    files['sections/02-design.tex'] = '\n'.join(design)
    electrical = [r'\Needspace{8\baselineskip}\section{Electrical design}',
        'The selected reference circuits are redrawn below with native electrical symbols. '
        'Identical net labels denote connections. Unknown component internals are terminal blocks. '
        'These scoped drawings do not replace the complete manufacturer schematic.']
    for figure in report.get('electrical_drawings', []):
        electrical.extend([r'\par\medskip\noindent\begin{minipage}{\linewidth}',
                           electrical_figure(figure), r'\end{minipage}\par'])
    if not report.get('electrical_drawings'):
        electrical.append('Component evidence is unavailable; no electrical drawing was inferred.')
    if project['proposed_wires']:
        electrical.append(r'\subsection{Proposed external connections}')
    for wire in project['proposed_wires']:
        electrical.append(r'\textbf{' + tex(wire['from_endpoint'] + ' ↔ ' + wire['to_endpoint'])
                          + '}. ' + tex(wire['description']) + '\n')
        electrical.append(r'\begin{center}\begin{circuitikz}' + '\n'
            + r'\draw[dashed] (0,0) node[ocirc,label=below:{' + tex(wire['from_endpoint']) + r'}] {} -- '
            + r'(7,0) node[ocirc,label=below:{' + tex(wire['to_endpoint']) + r'}] {} '
            + r'node[midway,above]{\small Proposed jumper / unconfirmed};' + '\n'
            + r'\end{circuitikz}\end{center}')
    files['sections/03-electrical.tex'] = '\n'.join(electrical)
    verify = [r'\section{Verification and operating procedure}', _list(project['procedure']),
              r'\subsection{Build evidence}', 'Status: ' + tex(report['build']['status'].replace('_', ' ')) + '.']
    if report['build'].get('artifact_id'):
        verify.extend([r'Artifact ID: \texttt{' + breakable(report['build']['artifact_id']) + '}.',
            'The image was revalidated. Attached source-to-artifact binding and physical behavior remain unassessed.'])
    verify.extend([r'\subsection{Limitations and open work}', _list(project['limitations'] + report['limits']),
                   r'\subsection{Knowledge gaps}', _list(report['gaps'])])
    files['sections/04-verification.tex'] = '\n'.join(verify)
    evidence = [r'\Needspace{8\baselineskip}\appendix\section{Traceability and exact identities}',
        r'Bundle revision: \texttt{' + breakable(report['bundle_revision']) + '}.',
        r'Report revision: \texttt{' + breakable(report['report_revision']) + '}.',
        r'\subsection{Source documents}',
        r'{\small\renewcommand{\arraystretch}{1.15}',
        r'\begin{longtable}{@{}p{.06\linewidth}p{.48\linewidth}p{\dimexpr.46\linewidth-4\tabcolsep\relax}@{}}',
        r'\toprule Key & Document / file & SHA-256\\\midrule\endhead']
    for row in report['references']:
        evidence.append('R' + str(lookup[row['id']]) + ' & ' + tex(row['id'])
            + r'\newline {\scriptsize\ttfamily ' + breakable('../' + row['file']) + '} & '
            + r'{\scriptsize\ttfamily ' + breakable(row['sha256']) + r'}\\')
    evidence.extend([r'\bottomrule\end{longtable}}', r'\subsection{Project attachments}',
        r'{\footnotesize\renewcommand{\arraystretch}{1.0}',
        r'\begin{longtable}{@{}p{.58\linewidth}p{\dimexpr.42\linewidth-2\tabcolsep\relax}@{}}',
        r'\toprule File & SHA-256\\\midrule\endhead'])
    for row in report['project_files']:
        evidence.append(r'{\scriptsize\ttfamily ' + breakable(row['path']) + '} & '
                        + r'{\scriptsize\ttfamily ' + breakable(row['sha256']) + r'}\\')
    evidence.append(r'\bottomrule\end{longtable}}')
    provenance = {}
    for net in report['nets']:
        for pin in net['endpoints']:
            for source in pin['sources'].split(';'):
                source = source.strip()
                if source and source not in provenance:
                    provenance[source] = 'N' + str(len(provenance) + 1)
    evidence.extend([r'\Needspace{8\baselineskip}\section{Selected net connections}',
        'Endpoints use component:pin notation. Terminals in the same row share the listed sources. '
        'A differing pin label is shown in parentheses. Full source locators follow the table.',
        r'{\small\renewcommand{\arraystretch}{1.2}',
        r'\begin{longtable}{@{}p{.10\linewidth}p{.20\linewidth}p{.30\linewidth}p{\dimexpr.40\linewidth-6\tabcolsep\relax}@{}}',
        r'\toprule Net & MCU pad & Header / component & Sources\\\midrule\endhead'])
    for net in report['nets']:
        groups = {}
        for pin in net['endpoints']:
            keys = tuple(provenance[s.strip()] for s in pin['sources'].split(';') if s.strip())
            groups.setdefault(keys, []).append(pin)
        for keys, pins in groups.items():
            pads, terminals = [], []
            for pin in pins:
                label = pin['endpoint'] + (' (' + pin['pin'] + ')' if pin['pin'] != net['name'] else '')
                is_mcu = pin['endpoint'].split(':')[0] == report['target']['primary_mcu_ref']
                (pads if is_mcu else terminals).append(label)
            evidence.append(' & '.join(tex(v) for v in
                [net['name'], ', '.join(pads) or '—', ', '.join(terminals) or '—', ', '.join(keys)]) + r'\\')
    evidence.extend([r'\bottomrule\end{longtable}}',
        r'\Needspace{5\baselineskip}\subsection{Net source key}',
        r'{\small\renewcommand{\arraystretch}{1.15}',
        r'\begin{longtable}{@{}p{.08\linewidth}p{\dimexpr.92\linewidth-2\tabcolsep\relax}@{}}',
        r'\toprule Key & Complete source locator\\\midrule\endhead'])
    for source, key in provenance.items():
        evidence.append(tex(key) + r' & {\footnotesize\ttfamily ' + breakable(source) + r'}\\')
    evidence.append(r'\bottomrule\end{longtable}}')
    files['sections/05-evidence.tex'] = '\n'.join(evidence)
    main = [PREAMBLE, r'\begin{document}', *(r'\input{' + name + '}' for name in sorted(files)), r'\end{document}']
    files['report.tex'] = '\n'.join(main) + '\n'
    files['electrical.tex'] = electrical_document(report, PREAMBLE)
    files['authoring.json'] = json.dumps({
        'format': 'praxis-latex-authoring-v1', 'project_id': project['id'],
        'bundle_revision': report['bundle_revision'], 'report_revision': report['report_revision'],
        'parts': [{'file': name, 'role': name.split('/')[-1].removesuffix('.tex')}
                  for name in sorted(files) if name.startswith('sections/')],
        'evidence': '../report.json', 'electrical_recipes': report.get('electrical_drawings', []),
        'instruction': 'Copy this authoring kit into a new workspace before editing. Author prose and '
            'design with citations. Preserve target identities and separate observed results from plans. '
            'Do not promote missing or unassessed verification to a pass. Custom TeX is not executed by Praxis.'
        }, indent=2, sort_keys=True, ensure_ascii=False) + '\n'
    files['README.md'] = '''# LaTeX authoring kit

This is an editable, multi-part engineering report. `authoring.json` identifies its
sections and evidence inputs. The coding assistant can author the specification's
requirements, explanations and sequences, or copy this kit to a separate working
directory and customize the LaTeX sections. Preserve the evidence and its limitations.

`electrical.tex` uses native CircuitikZ components and exact published net labels.
`report.tex` assembles the cover, contents, requirements, design, electrical sheets,
verification and traceability appendices. Neither input contains model-supplied raw
TeX commands: authored fields are escaped during generation.

For the controlled PDF renderer, use:

    praxis project-pdf --report /absolute/path/to/report --output /absolute/path/to/new-pdf-report

The renderer regenerates the fixed templates from integrity-checked report data;
it does not execute edits to exported TeX. Custom AI-authored TeX can be compiled
separately in an appropriate trusted or isolated authoring environment. Praxis does
not certify custom TeX or its engineering claims.
'''
    return {'latex/' + name: body.encode() for name, body in files.items()}
