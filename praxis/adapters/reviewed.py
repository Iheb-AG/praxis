"""Reviewed transcription adapter for PDF-only schematics; no geometry inference."""

from pathlib import Path

from pydantic import ValidationError

from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import ReviewedSchematic, Target


def parse(path: Path, target: Target) -> ReviewedSchematic:
    try:
        result = ReviewedSchematic.model_validate(load_json(path.read_bytes()))
    except ValidationError as exc:
        raise PraxisError("INVALID_SCHEMATIC", str(exc)) from exc
    if (result.mcu, result.package, result.board_revision) != (
            target.mcu, target.package, target.board_revision):
        raise PraxisError("TARGET_MISMATCH", "Reviewed schematic MCU/package/revision differs")
    if result.coverage == "partial" and not result.omissions:
        raise PraxisError("INVALID_SCHEMATIC", "Partial schematics must state their omitted circuits")
    return result
