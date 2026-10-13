"""Evaluate integer-only C macro expressions; never eval(), execute, or guess."""

import ast
import operator
import re

from praxis.errors import PraxisError

_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
    ast.BitOr: operator.or_, ast.BitAnd: operator.and_, ast.BitXor: operator.xor,
    ast.LShift: operator.lshift, ast.RShift: operator.rshift,
}


def integer(expression: str, macros: dict[str, str], stack: tuple[str, ...] = ()) -> int:
    if len(expression) > 4096 or len(stack) > 32:
        raise PraxisError("UNSUPPORTED_EXPRESSION", "Macro expansion exceeds its bounds")
    # Only standard integer suffixes, never identifier substrings.
    expression = re.sub(r"\b(0[xX][0-9a-fA-F]+|[0-9]+)[uUlL]+\b", r"\1", expression)
    try:
        tree = ast.parse(expression.strip(), mode="eval")
    except (SyntaxError, ValueError) as exc:
        raise PraxisError("UNSUPPORTED_EXPRESSION", f"Unsupported C expression: {expression}") from exc

    def visit(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value
        if isinstance(node, ast.Name) and node.id in macros and node.id not in stack:
            return integer(macros[node.id], macros, (*stack, node.id))
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub, ast.Invert)):
            operand = visit(node.operand)
            return {ast.UAdd: operator.pos, ast.USub: operator.neg, ast.Invert: operator.invert}[
                type(node.op)
            ](operand)
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, (ast.LShift, ast.RShift)) and not 0 <= right <= 63:
                raise PraxisError("UNSUPPORTED_EXPRESSION", "Shift exceeds 64-bit bounds")
            result = _OPS[type(node.op)](left, right)
            if result.bit_length() > 64:
                raise PraxisError("UNSUPPORTED_EXPRESSION", "Integer exceeds 64-bit bounds")
            return result
        raise PraxisError("UNSUPPORTED_EXPRESSION", f"Unsupported C expression: {expression}")

    return visit(tree.body)

