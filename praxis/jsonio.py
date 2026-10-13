"""Strict input JSON: duplicate keys are conflicts, never last-value-wins."""

import json

from praxis.errors import PraxisError


def load_json(data: bytes | str):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise PraxisError("DUPLICATE_IDENTITY", f"Duplicate JSON key: {key!r}")
            result[key] = value
        return result

    try:
        if isinstance(data, bytes):
            data = data.decode("utf-8")
        return json.loads(data, object_pairs_hook=unique)
    except (ValueError, UnicodeDecodeError) as exc:
        raise PraxisError("INVALID_JSON", "Input must be valid UTF-8 JSON") from exc
