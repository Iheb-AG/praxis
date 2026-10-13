#!/usr/bin/env python3
"""Executable offline Project Praxis compiler; use Python from the project venv.

Example:
    .venv/bin/python compiler.py --profile sources/stm32f407vgt6/profile.json \
        --output bundles/stm32f407vgt6

Source locations and reviewed semantics are explicit in the profile. No network
requests, automatic PDF extraction, or shell build scripts occur during compile.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from praxis.compiler import (
    compile_bundle,
    parse_cmsis_headers,
    parse_device_tree,
    parse_kicad_netlist,
)
from praxis.errors import PraxisError

__all__ = ["compile_bundle", "parse_cmsis_headers", "parse_kicad_netlist", "parse_device_tree", "main"]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--profile", required=True, type=Path, help="Target profile with registered local inputs")
    parser.add_argument("--output", required=True, type=Path, help="New immutable bundle directory")
    args = parser.parse_args(argv)
    try:
        print(compile_bundle(args.profile, args.output))
        return 0
    except PraxisError as exc:
        print(str(exc), file=sys.stderr)
    except (OSError, ValueError) as exc:
        print(f"INPUT_ERROR: {exc}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
