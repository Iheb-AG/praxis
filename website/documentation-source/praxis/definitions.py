"""Compose reviewed records without copying or modifying a base knowledge set."""

import json
from pathlib import Path

from pydantic import TypeAdapter, ValidationError

from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import DefinitionExtension, Peripheral


def definitions_digest(items: list[Peripheral]) -> str:
    """Hash the complete composed state, including defaults, in canonical ID order.

    Extensions that amend a previously extended entity must explicitly bind this
    parent state. Base-file byte binding remains mandatory and unchanged.
    """
    return digest(json.dumps([item.model_dump(mode="json") for item in
                              sorted(items, key=lambda item: item.id)],
                             sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode())


def load_definitions(profile, paths: dict[str, Path]) -> list[Peripheral]:
    try:
        raw = paths[profile.definitions].read_bytes()
        items = TypeAdapter(list[Peripheral]).validate_python(load_json(raw))
        if len({item.id for item in items}) != len(items):
            raise PraxisError("DUPLICATE_ENTITY", "Duplicate canonical peripheral in base definitions")
        result = {item.id: item for item in items}
        authorities = {source.id: source.authority for source in profile.sources}
        changed = set()
        for source_id in profile.definition_extensions:
            if source_id not in paths:
                raise PraxisError("UNKNOWN_SOURCE", f"Register definition extension source: {source_id}")
            if authorities.get(source_id) != "semantics":
                raise PraxisError("SOURCE_AUTHORITY", "Definition extensions require semantics authority")
            extension = DefinitionExtension.model_validate(load_json(paths[source_id].read_bytes()))
            if extension.base_sha256 != digest(raw):
                raise PraxisError("STALE_DEFINITION_EXTENSION",
                                  f"{source_id}: review against the exact selected base definitions")
            if profile.target.mcu not in extension.applicable_mcus:
                raise PraxisError("TARGET_MISMATCH", f"{source_id}: selected MCU is outside reviewed applicability")
            parent = extension.parent_definitions_sha256
            if parent is not None and parent != definitions_digest(list(result.values())):
                raise PraxisError("STALE_DEFINITION_EXTENSION",
                                  f"{source_id}: review against the exact composed parent definitions")
            for replacement, records in ((False, extension.additions), (True, extension.replacements)):
                for item in records:
                    if item.id in changed and parent is None:
                        raise PraxisError("DEFINITION_CONFLICT", f"Multiple extensions change {item.id}; resolve explicitly")
                    if replacement != (item.id in result):
                        raise PraxisError("DEFINITION_CONFLICT",
                            f"{item.id}: additions must be new and replacements must name existing peripherals")
                    result[item.id] = item
                    changed.add(item.id)
        return [result[key] for key in sorted(result)]
    except (ValidationError, ValueError) as exc:
        raise PraxisError("INVALID_DEFINITIONS", str(exc)) from exc

