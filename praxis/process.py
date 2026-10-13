"""Bounded subprocess execution for offline ingestion only."""

import subprocess
import tempfile

from praxis.errors import PraxisError


def run(args: list[str], *, timeout: int = 30, limit: int = 8 * 1024 * 1024,
        include_stderr: bool = False) -> str:
    try:
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            result = subprocess.run(args, stdout=stdout, stderr=stderr, timeout=timeout, check=False)
            if stdout.tell() > limit or stderr.tell() > limit:
                raise PraxisError("OUTPUT_LIMIT", f"{args[0]} exceeded the output limit")
            stdout.seek(0)
            stderr.seek(0)
            output = stdout.read().decode("utf-8", errors="replace")
            diagnostics = stderr.read().decode("utf-8", errors="replace")
        if result.returncode:
            raise PraxisError("EXTRACTOR_FAILED", f"{args[0]} exited {result.returncode}: {diagnostics}")
        return output + diagnostics if include_stderr else output
    except FileNotFoundError as exc:
        raise PraxisError("MISSING_TOOL", f"Install required offline tool: {args[0]}") from exc
    except subprocess.TimeoutExpired as exc:
        raise PraxisError("TIMEOUT", f"{args[0]} exceeded {timeout} seconds") from exc
