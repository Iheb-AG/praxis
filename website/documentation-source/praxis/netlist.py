"""Exact lookup of complete electrical nets from the published Markdown table."""

from __future__ import annotations

import html

from praxis.errors import PraxisError
from praxis.render import NET_COLUMNS


class NetlistIndex:
    def __init__(self, markdown: str, primary_mcu_ref: str,
                 board_markdown: str | None = None, components_markdown: str | None = None):
        lines = markdown.splitlines()
        start = next((i for i, line in enumerate(lines)
                      if line.startswith("| ") and self._cells(line) == NET_COLUMNS), None)
        if start is None or start + 1 >= len(lines):
            raise PraxisError("INVALID_NETLIST", "Published netlist lacks its canonical table")
        self.preamble = "\n".join(lines[:start]).rstrip() + "\n\n"
        self.header = "\n".join(lines[start:start + 2]) + "\n"
        if self._cells(lines[start + 1]) != ["---"] * len(NET_COLUMNS):
            raise PraxisError("INVALID_NETLIST", "Malformed netlist table separator")
        self.nets: dict[str, list[str]] = {}
        self.exact: dict[str, set[str]] = {}
        self.pins: dict[str, set[str]] = {}
        endpoint_nets = {}
        endpoints = set()
        for line in lines[start + 2:]:
            if not line.strip():
                continue
            if not line.startswith("|"):
                raise PraxisError("INVALID_NETLIST", "Unexpected content after netlist table")
            fields = self._cells(line)
            if len(fields) != len(NET_COLUMNS):
                raise PraxisError("INVALID_NETLIST", "Malformed netlist row")
            net, endpoint, pin, _sheet, _package, aliases, sources = fields
            if not net or not sources or endpoint in endpoints:
                raise PraxisError("INVALID_NETLIST", "Missing provenance or duplicated endpoint")
            endpoints.add(endpoint)
            endpoint_nets[endpoint] = net
            self.nets.setdefault(net, []).append(line)
            for key in [net, endpoint, *filter(None, aliases.split(";"))]:
                self.exact.setdefault(key, set()).add(net)
            if endpoint.startswith(primary_mcu_ref + ":"):
                self.pins.setdefault(pin.casefold(), set()).add(net)
        if not self.nets:
            raise PraxisError("INVALID_NETLIST", "Published netlist is empty")
        self.board_markdown = board_markdown
        self.components_markdown = components_markdown
        self.circuits: dict[str, set[str]] = {}
        if board_markdown is not None:
            from praxis.board import SIGNAL_COLUMNS
            board_lines = board_markdown.splitlines()
            start = next((i for i, line in enumerate(board_lines)
                          if line.startswith("| ") and self._cells(line) == SIGNAL_COLUMNS), None)
            if (start is None or start + 1 >= len(board_lines) or
                    self._cells(board_lines[start + 1]) != ["---"] * len(SIGNAL_COLUMNS)):
                raise PraxisError("INVALID_BOARD", "Published board document lacks its canonical signal table")
            signals = set()
            for line in board_lines[start + 2:]:
                if not line.startswith("|"):
                    break
                fields = self._cells(line)
                if len(fields) != len(SIGNAL_COLUMNS):
                    raise PraxisError("INVALID_BOARD", "Malformed board signal row")
                signal, aliases, kind, pin, endpoint, active, pull, circuit, sources = fields
                name = endpoint_nets.get(endpoint)
                nets = set(circuit.split(";"))
                if (signal in signals or name is None or not sources or not nets <= self.nets.keys()
                        or name not in nets or kind not in {"led", "button"} or active not in {"high", "low"}
                        or self.pins.get(pin.casefold()) != {name}):
                    raise PraxisError("INVALID_BOARD", "Board signal disagrees with published net membership")
                signals.add(signal)
                for alias in [signal, *aliases.split(";")]:
                    if self.exact.get(alias) != {name}:
                        raise PraxisError("INVALID_BOARD", "Board signal alias disagrees with published netlist")
                self.circuits.setdefault(name, set()).update(nets)
            if not signals or components_markdown is None:
                raise PraxisError("INVALID_BOARD", "Board signals require a published component catalog")

    @staticmethod
    def _cells(line):
        return [html.unescape(value.strip()).replace("\\\\", "\\")
                for value in line.strip().strip("|").split("|")]

    def query(self, target: str) -> str:
        if not isinstance(target, str) or not target.strip() or len(target) > 128:
            raise PraxisError("INVALID_INPUT", "query_target must contain 1–128 characters")
        target = target.strip()
        if any(ord(c) < 32 or ord(c) == 127 for c in target):
            raise PraxisError("INVALID_INPUT", "query_target cannot contain control characters")
        matches = self.exact.get(target, set()) | self.pins.get(target.casefold(), set())
        if len(matches) > 1:
            raise PraxisError("AMBIGUOUS_IDENTITY", f"{target!r} identifies multiple nets: {', '.join(sorted(matches))}; use an endpoint or exact net name")
        if not matches:
            return f"No match for {target!r} in this target's published schematic netlist."
        name = next(iter(matches))
        result = self.preamble + self.header + "\n".join(self.nets[name]) + "\n"
        if name in self.circuits:
            for related in sorted(self.circuits[name] - {name}):
                result += (f"\n## Separate circuit net: {related}\n\n" + self.header +
                           "\n".join(self.nets[related]) + "\n")
            result += "\n" + self.board_markdown + "\n" + self.components_markdown
        return result

