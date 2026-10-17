"""Editable engineering-report parts and native LaTeX/CircuitikZ source.

The assistant authors the project text and cited design through ProjectSpec. These
templates keep generated evidence separate from prose and escape every text field.
"""
from __future__ import annotations

import json

from praxis.electrical import circuit_pages, electrical_document
from praxis.latex_text import breakable, tex

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=22mm,headheight=16pt]{geometry}
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\setsansfont{TeX Gyre Heros}
\setmonofont{Latin Modern Mono}
\usepackage{microtype,graphicx,longtable,array,booktabs,fancyhdr,xurl}
\usepackage[unicode,hidelinks]{hyperref}
\usepackage[europeanresistors]{circuitikz}
\usetikzlibrary{arrows.meta}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
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
    participants = diagram['participants']
    positions = {p['id']: i * 3.4 for i, p in enumerate(participants)}
    height = len(diagram['messages']) * 1.55 + 1.0
    code = [r'\begin{center}\resizebox{\linewidth}{!}{\begin{tikzpicture}[>=Stealth]']
    for participant in participants:
        x = positions[participant['id']]
        code.append(f'\\node[draw,align=center,text width=2.6cm,minimum height=0.85cm] at ({x:g},0) '
                    + '{\\small\\sffamily ' + tex(participant['label']) + '};')
        code.append(f'\\draw[dashed,black!30] ({x:g},-0.5) -- ({x:g},-{height:g});')
    for number, message in enumerate(diagram['messages'], 1):
        start, end = positions[message['sender']], positions[message['receiver']]
        y = -number * 1.55
        label = tex(f'{number:02d}. {message["label"]}')
        if start == end:
            code.append(f'\\draw[->] ({start:g},{y:g}) -- ++(1.15,0) -- ++(0,-0.4) -- ({start:g},{y - 0.4:g});')
            code.append(f'\\node[above right,align=left,text width=2.8cm,fill=white,inner sep=2pt] at ({start:g},{y:g}) '
                        + '{\\scriptsize ' + label + '};')
        else:
            span = abs(start - end) - 0.3
            code.append(f'\\draw[->] ({start:g},{y:g}) -- ({end:g},{y:g}) '
                        f'node[midway,above,align=center,text width={span:g}cm,fill=white,inner sep=2pt] '
                        + '{\\scriptsize ' + label + '};')
    code.append(r'\end{tikzpicture}}\end{center}')
    return '\n'.join(code) + '\n'


def sources(report: dict) -> dict[str, bytes]:
    project = report['project']
    lookup = {r['id']: i for i, r in enumerate(report['references'], 1)}
    files = {}
    title = (r'\begin{titlepage}\thispagestyle{empty}' + '\n'
        + r'{\sffamily\small PROJECT ENGINEERING REPORT}\par\vspace{20mm}' + '\n'
        + r'{\LARGE\bfseries ' + tex(project['title']) + r'\par}\vspace{8mm}' + '\n'
        + _prose(project['objective']) + r'\vfill' + '\n'
        + r'\begin{tabular}{@{}p{35mm}p{115mm}@{}}\toprule' + '\n'
        + r'Document ID & ' + tex(project['id']) + r'\\' + '\n'
        + r'Reference MCU & ' + tex(report['target']['mcu']) + r'\\' + '\n'
        + r'Reference PCB & ' + tex(report['target']['board_revision']) + r'\\' + '\n'
        + r'Knowledge scope & ' + ('Ready for the declared scope' if report['knowledge_scope_ready'] else 'Open gaps remain') + r'\\' + '\n'
        + r'Build evidence & ' + tex(report['build']['status'].replace('_', ' ')) + r'\\' + '\n'
        + r'Physical verification & Not assessed\\\bottomrule\end{tabular}' + '\n'
        + r'\vspace{8mm}\par{\small Document status: design and evidence review. Overall project acceptance '
        + r'is not established. Physical PCB revision and assembly must be confirmed separately.}' + '\n'
        + r'\end{titlepage}\tableofcontents\clearpage' + '\n')
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
        design.extend([r'\subsection{' + tex(diagram['title']) + '}', _prose(diagram['description']),
                       _sequence(diagram), _refs(diagram['documents'], lookup)])
    files['sections/02-design.tex'] = '\n'.join(design)
    electrical = [r'\clearpage\section{Electrical design}',
        'The following sheets redraw the selected reference circuits with native electrical symbols. '
        'Identical net labels denote connections. This is not the manufacturer\'s original sheet layout '
        'or a complete board schematic. Unknown component internals are drawn as terminal blocks.']
    for page_number, _ in enumerate(circuit_pages(report.get('electrical_drawings', [])), 1):
        electrical.append(r'\begin{figure}[p]\centering'
            + '\n' + r'\includegraphics[page=' + str(page_number) + r',width=\linewidth,height=.82\textheight,keepaspectratio]{figures/electrical.pdf}'
            + '\n' + r'\caption{Selected electrical reference, sheet ' + str(page_number) + r'.}\end{figure}\clearpage')
    if not report.get('electrical_drawings'):
        electrical.append('Component evidence is unavailable; no electrical drawing was inferred.')
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
    evidence = [r'\appendix\section{Traceability and exact identities}',
        r'Bundle revision: \texttt{' + breakable(report['bundle_revision']) + '}.',
        r'Report revision: \texttt{' + breakable(report['report_revision']) + '}.',
        r'\subsection{Source documents}']
    for row in report['references']:
        evidence.append(r'\textbf{R' + str(lookup[row['id']]) + ': ' + tex(row['id']) + r'}\par '
            + r'Complete document: \texttt{../' + breakable(row['file']) + r'}.\par SHA-256: \texttt{' + breakable(row['sha256']) + r'}.\par')
    evidence.append(r'\subsection{Project attachments}')
    for row in report['project_files']:
        evidence.append(tex(row['path']) + r'\par SHA-256: \texttt{' + breakable(row['sha256']) + r'}.\par')
    evidence.append(r'\section{Complete selected net memberships}')
    for net in report['nets']:
        evidence.append(r'\subsection{' + tex(net['name']) + '}')
        evidence.append(r'\begin{longtable}{@{}p{27mm}p{27mm}p{96mm}@{}}\toprule Endpoint & Pin & Provenance\\\midrule\endhead')
        for pin in net['endpoints']:
            evidence.append(tex(pin['endpoint']) + ' & ' + tex(pin['pin']) + ' & '
                            + breakable(pin['sources']) + r'\\')
        evidence.append(r'\bottomrule\end{longtable}')
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
