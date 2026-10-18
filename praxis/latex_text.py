"""Escape authored text; project fields are never executable TeX fragments."""

_ESCAPES = {
    '\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '$': r'\$', '&': r'\&',
    '#': r'\#', '%': r'\%', '_': r'\_', '^': r'\textasciicircum{}', '~': r'\textasciitilde{}',
    '→': r'\ensuremath{\rightarrow}', '↔': r'\ensuremath{\leftrightarrow}',
    'Ω': r'\ensuremath{\Omega}', 'µ': r'\ensuremath{\mu}', '≤': r'\ensuremath{\leq}',
    '≥': r'\ensuremath{\geq}', '\t': '    ', '\r': '', '\n': '\n',
}


def tex(value) -> str:
    return ''.join(_ESCAPES.get(char, char) for char in str(value))


def breakable(value) -> str:
    """Preserve long identifiers while allowing TeX to wrap them inside columns."""
    return r'\allowbreak{}'.join(tex(char) for char in str(value))
