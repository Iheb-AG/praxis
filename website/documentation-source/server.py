"""Compatibility entry point: python /absolute/path/server.py --bundle /absolute/bundle."""

import sys

from praxis.cli import main

if __name__ == "__main__":
    raise SystemExit(main(["serve", *sys.argv[1:]]))

