"""Data-backed compatibility for previously published immutable target records.

This catalog is not an extraction fallback for new profiles. It preserves the
existing manifest validation and firmware qualification boundaries.
"""
from functools import lru_cache
from importlib.resources import files

from praxis.jsonio import load_json


@lru_cache(maxsize=1)
def catalog():
    return load_json(files("praxis").joinpath("data/legacy-targets.json").read_bytes())


def qualified_target(target):
    return next((entry for entry in catalog()["targets"] if
                 (entry["family"], entry["mcu"], entry["package"]) ==
                 (target.family, target.mcu, target.package)), None)
