"""Restore exact historical imports from pinned public sources, never create a review.

The committed manifest contains metadata/receipts, not manufacturer document text.
Extraction must reproduce every original artifact before original metadata is restored.
Published bundles and compiler validation are never modified by this utility.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import time
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from pydantic import ValidationError

from praxis.bundle import digest, read_inside, relative_path
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Profile
from praxis.web_import import (
    MAX_DOWNLOAD,
    ImportRecord,
    ReviewReceipt,
    WebSource,
    _revision,
    download,
    require_review,
    scrape,
)


def checked_manifest(path):
    data = load_json(read_inside(path.parent.resolve(), path.name, 4 * 1024 * 1024))
    if (
        not isinstance(data, dict)
        or data.get("format") != "praxis-source-replay-v1"
        or not isinstance(data.get("allowed_hosts"), list)
        or not data["allowed_hosts"]
        or any(not isinstance(h, str) or not h for h in data["allowed_hosts"])
        or not isinstance(data.get("archives"), list)
        or not 1 <= len(data["archives"]) <= 100
    ):
        raise PraxisError("INVALID_REPLAY", "Select a versioned bounded source replay manifest")
    if "extraction_runtime" in data:
        runtime = data["extraction_runtime"]
        if (
            not isinstance(runtime, dict)
            or set(runtime) != {"implementation", "python"}
            or not isinstance(runtime["implementation"], str)
            or re.fullmatch(r"[a-z][a-z0-9_]*", runtime["implementation"]) is None
            or not isinstance(runtime["python"], str)
            or re.fullmatch(r"[1-9][0-9]*\.[0-9]+", runtime["python"]) is None
        ):
            raise PraxisError(
                "INVALID_REPLAY", "extraction_runtime requires an implementation and major.minor Python version"
            )
    records, seen = [], set()
    for entry in data["archives"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise PraxisError("INVALID_REPLAY", "Each archive requires a relative path")
        name = str(relative_path(entry["path"]))
        if name in seen or name != entry["path"] or "imports" not in Path(name).parts:
            raise PraxisError("INVALID_REPLAY", "Use unique normalized import paths")
        seen.add(name)
        try:
            record_text, review_text = entry["record_utf8"], entry["review_utf8"]
            if not isinstance(record_text, str) or not isinstance(review_text, str):
                raise ValueError("metadata must be exact UTF-8 text")
            record = load_json(record_text.encode())
            ImportRecord.model_validate(record)
            review = ReviewReceipt.model_validate(load_json(review_text.encode()))
        except (KeyError, ValueError, ValidationError) as exc:
            raise PraxisError(
                "INVALID_REPLAY", "Malformed original import/review metadata"
            ) from exc
        if (
            record["import_revision"] != _revision(record)
            or review.import_revision != record["import_revision"]
            or review.target != record["source"]["target"]
        ):
            raise PraxisError("IMPORT_INTEGRITY", "Original receipt must bind this exact import")
        records.append((name, record, record_text, review_text))
    return data, records


def _require_extraction_runtime(data):
    """Historical extraction depends on interpreter arithmetic as well as packages."""
    expected = data.get("extraction_runtime")
    if expected is None:
        return
    actual = {"implementation": sys.implementation.name,
              "python": f"{sys.version_info.major}.{sys.version_info.minor}"}
    if actual != expected:
        raise PraxisError(
            "EXTRACTION_RUNTIME",
            f"Historical replay requires {expected['implementation']} Python {expected['python']}; "
            f"running {actual['implementation']} Python {actual['python']}. "
            "Run restoration in a separate environment using the manifest runtime, then use the "
            "verified imports with your application interpreter. No hashes or receipts were changed.",
        )


def _transient(exc: PraxisError) -> bool:
    import httpx
    if exc.code == "DOWNLOAD_TIMEOUT":
        return True
    if exc.code == "DOWNLOAD_FAILED":
        return isinstance(exc.__cause__, (httpx.TransportError, OSError))
    return exc.code == "HTTP_ERROR" and re.match(r"HTTP (408|429|500|502|503|504)\b", exc.message) is not None


def _download(record, pending, hosts, *, client, attempts, read_timeout):
    try:
        import httpx
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[web] for online source restoration") from exc
    source_hash = record["download"]["sha256"]
    source = WebSource.model_validate({**record["source"],
        "url": record["download"]["original_url"], "sha256": source_hash})
    for attempt in range(1, attempts + 1):
        pending.unlink(missing_ok=True)
        print(f"Download {source.url} (SHA-256 {source_hash[:12]}…); attempt {attempt}/{attempts}",
              file=sys.stderr, flush=True)
        try:
            if client is None:
                with httpx.Client(timeout=httpx.Timeout(read_timeout, connect=15),
                                  follow_redirects=False, trust_env=False) as owned:
                    metadata = download(source, pending, hosts, client=owned)
            else:
                metadata = download(source, pending, hosts, client=client)
            if metadata["bytes"] != record["download"]["bytes"]:
                raise PraxisError("SOURCE_HASH_MISMATCH", "Downloaded source size differs")
            return
        except PraxisError as exc:
            pending.unlink(missing_ok=True)
            if not _transient(exc):
                raise
            if attempt == attempts:
                raise PraxisError(exc.code, f"{source.url}: failed after {attempts} attempts; "
                    f"last error: {exc.message}. Retry preparation or supply the exact pinned cache bytes.") from exc
            delay = min(2 ** attempt, 8)
            print(f"Transient failure: {exc}; retrying in {delay}s", file=sys.stderr, flush=True)
            time.sleep(delay)


def _source_file(record, cache, hosts, *, client, attempts, read_timeout, offline):
    source_hash = record["download"]["sha256"]
    raw = cache / source_hash
    if raw.exists() or raw.is_symlink():
        contents = read_inside(cache, source_hash, MAX_DOWNLOAD)
        if digest(contents) != source_hash or len(contents) != record["download"]["bytes"]:
            raise PraxisError("SOURCE_HASH_MISMATCH", "Cached source differs; restore its pinned bytes")
        print(f"Verified cached source {source_hash}", file=sys.stderr, flush=True)
        return raw
    if offline:
        raise PraxisError("MISSING_CACHED_SOURCE", f"Offline replay needs {source_hash}; run download-only preparation first")
    with tempfile.TemporaryDirectory(prefix=".download-", dir=cache) as temporary:
        pending = Path(temporary) / "source"
        _download(record, pending, hosts, client=client, attempts=attempts, read_timeout=read_timeout)
        # Never replace an existing immutable cache entry after a concurrent writer.
        try:
            os.link(pending, raw)
        except FileExistsError:
            contents = read_inside(cache, source_hash, MAX_DOWNLOAD)
            if digest(contents) != source_hash or len(contents) != record["download"]["bytes"]:
                raise PraxisError("SOURCE_HASH_MISMATCH", "Concurrent cache writer changed bytes") from None
    return raw


def restore(manifest: Path, profile: Path, cache: Path, *, client=None,
            download_only=False, offline=False, download_attempts=4, read_timeout=60):
    if (type(download_attempts) is not int or not 1 <= download_attempts <= 5
            or type(read_timeout) is not int or not 15 <= read_timeout <= 120):
        raise PraxisError("INVALID_REPLAY_POLICY", "Use 1–5 download attempts and a 15–120 second read timeout")
    root = profile.parent.resolve(strict=True)
    selected = Profile.model_validate_json(read_inside(root, profile.name, 8 * 1024 * 1024))
    data, records = checked_manifest(manifest)
    by_path = {name: row for name, *row in records}
    required = set(selected.web_imports.values())
    if not required or not required <= by_path.keys():
        raise PraxisError(
            "INVALID_REPLAY", "Replay must cover every archive declared by the profile"
        )
    cache = cache.resolve()
    cache.mkdir(parents=True, exist_ok=True)
    results = []
    for name in sorted(required):
        record, record_text, review_text = by_path[name]
        if record["source"]["target"] != selected.target.mcu:
            raise PraxisError("TARGET_MISMATCH", "Replay archive targets another MCU")
        destination = root / name
        if not destination.resolve().is_relative_to(root) or destination.is_symlink():
            raise PraxisError("INVALID_PATH", "Replay archive escapes the source root")
        if destination.exists() and not download_only:
            require_review(destination, selected.target.mcu)
            if (
                read_inside(destination, "import.json", 4 * 1024 * 1024) != record_text.encode()
                or read_inside(destination, "review.json", 256 * 1024) != review_text.encode()
            ):
                raise PraxisError(
                    "IMMUTABLE_IMPORT", "Existing archive differs from the replay receipt"
                )
            results.append(dict(path=name, status="verified existing"))
            continue
        if not download_only:
            _require_extraction_runtime(data)
        for package, expected in (() if download_only else record["extractors"].items()):
            if package == "text":
                continue
            try:
                actual = version(package)
            except PackageNotFoundError as exc:
                raise PraxisError(
                    "MISSING_TOOL", f"Install required extractor {package}=={expected}"
                ) from exc
            if actual != expected:
                raise PraxisError(
                    "EXTRACTOR_VERSION", f"Requires {package}=={expected}; found {actual}"
                )
        raw = _source_file(record, cache, set(data["allowed_hosts"]), client=client,
                           attempts=download_attempts, read_timeout=read_timeout, offline=offline)
        if download_only:
            results.append(dict(path=name, status="verified source bytes", sha256=raw.name))
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".replay-", dir=destination.parent) as temporary:
            staging = Path(temporary) / "archive"
            scrape(
                WebSource.model_validate(record["source"]),
                staging,
                pages=record["selection"],
                from_file=raw,
            )
            regenerated = load_json(read_inside(staging, "import.json", 4 * 1024 * 1024))
            for key in (
                "source",
                "selection",
                "extractors",
                "extracted_locators",
                "warnings",
                "file_hashes",
            ):
                if regenerated[key] != record[key]:
                    details = ""
                    if key == "file_hashes":
                        changed = sorted(path for path in record[key].keys() | regenerated[key].keys()
                                         if record[key].get(path) != regenerated[key].get(path))
                        details = f" (differing artifacts: {', '.join(changed[:5])})"
                    raise PraxisError(
                        "REPLAY_MISMATCH",
                        f"{name}: original {key} not reproduced{details}; no receipt restored",
                    )
            # Preserve historical acquisition/review bytes only after all original files match.
            (staging / "import.json").write_bytes(record_text.encode())
            (staging / "review.json").write_bytes(review_text.encode())
            require_review(staging, selected.target.mcu)
            for source in selected.sources:
                if selected.web_imports.get(source.id) == name:
                    artifact = Path(source.path).relative_to(name).as_posix()
                    actual = digest(read_inside(staging, artifact, MAX_DOWNLOAD))
                    if (
                        actual != record["file_hashes"].get(artifact)
                        or source.expected_sha256 is not None
                        and actual != source.expected_sha256
                    ):
                        raise PraxisError(
                            "SOURCE_HASH_MISMATCH", f"Profile pin differs: {source.id}"
                        )
            if destination.exists() or destination.is_symlink():
                raise PraxisError("OUTPUT_EXISTS", "Replay destination appeared during extraction")
            os.rename(staging, destination)
        results.append(dict(path=name, status="restored exact bytes"))
        print(f"Restored {name}", flush=True)
    return dict(passed=True, archives=results, new_reviews=0, published_bundles_changed=0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--profile", required=True, type=Path)
    parser.add_argument("--cache", required=True, type=Path)
    parser.add_argument("--download-only", action="store_true", help="Acquire and verify raw sources; do not extract or restore receipts")
    parser.add_argument("--offline", action="store_true", help="Require every source in the verified cache; never download")
    parser.add_argument("--download-attempts", type=int, default=4, help="Bounded transient retries, 1–5; default 4")
    parser.add_argument("--read-timeout", type=int, default=60, help="HTTP read timeout, 15–120 seconds; default 60")
    args = parser.parse_args()
    try:
        print(json.dumps(restore(args.manifest, args.profile, args.cache,
            download_only=args.download_only, offline=args.offline,
            download_attempts=args.download_attempts, read_timeout=args.read_timeout), indent=2))
    except (PraxisError, OSError, ValidationError) as exc:
        parser.exit(1, f"{exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
