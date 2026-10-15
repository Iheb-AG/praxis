"""Restore exact historical imports from pinned public sources, never create a review.

The committed manifest contains metadata/receipts, not manufacturer document text.
Extraction must reproduce every original artifact before original metadata is restored.
Published bundles and compiler validation are never modified by this utility.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
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


def restore(manifest: Path, profile: Path, cache: Path, *, client=None):
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
        if destination.exists():
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
        for package, expected in record["extractors"].items():
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
        source_hash = record["download"]["sha256"]
        raw = cache / source_hash
        if raw.exists() or raw.is_symlink():
            contents = read_inside(cache, source_hash, MAX_DOWNLOAD)
            if digest(contents) != source_hash or len(contents) != record["download"]["bytes"]:
                raise PraxisError(
                    "SOURCE_HASH_MISMATCH", "Cached source differs; restore its pinned bytes"
                )
        else:
            source = WebSource.model_validate(
                {
                    **record["source"],
                    "url": record["download"]["original_url"],
                    "sha256": source_hash,
                }
            )
            with tempfile.TemporaryDirectory(prefix=".download-", dir=cache) as temporary:
                pending = Path(temporary) / "source"
                metadata = download(source, pending, set(data["allowed_hosts"]), client=client)
                if metadata["bytes"] != record["download"]["bytes"]:
                    raise PraxisError("SOURCE_HASH_MISMATCH", "Downloaded source size differs")
                # Never replace an existing immutable cache entry after a concurrent writer.
                try:
                    os.link(pending, raw)
                except FileExistsError:
                    if digest(read_inside(cache, source_hash, MAX_DOWNLOAD)) != source_hash:
                        raise PraxisError(
                            "SOURCE_HASH_MISMATCH", "Concurrent cache writer changed bytes"
                        ) from None
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
                    raise PraxisError(
                        "REPLAY_MISMATCH",
                        f"{name}: original {key} not reproduced; no receipt restored",
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
    args = parser.parse_args()
    try:
        print(json.dumps(restore(args.manifest, args.profile, args.cache), indent=2))
    except (PraxisError, OSError, ValidationError) as exc:
        parser.exit(1, f"{exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
