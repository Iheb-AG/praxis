"""Integrity checking and immutable Markdown snapshots. No ingestion imports."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path, PurePosixPath

from pydantic import ValidationError

from praxis.errors import PraxisError
from praxis.models import MAX_DOCUMENT_BYTES, Manifest


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def revision(manifest: dict) -> str:
    payload = {k: v for k, v in manifest.items() if k != "bundle_revision"}
    return digest(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def relative_path(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if (not value or "\\" in value or path.is_absolute() or any(p in (".", "..") for p in value.split("/"))
            or ":" in value or str(path) != value):
        raise PraxisError("INVALID_PATH", f"Unsafe bundle-relative path: {value!r}")
    return path


def read_inside(root: Path, name: str, limit: int = MAX_DOCUMENT_BYTES) -> bytes:
    path = root / relative_path(name)
    try:
        if not path.resolve(strict=True).is_relative_to(root.resolve(strict=True)):
            raise PraxisError("INVALID_PATH", f"Path escapes bundle: {name}")
        with path.open("rb") as handle:
            data = handle.read(limit + 1)
        if len(data) > limit:
            raise PraxisError("DOCUMENT_TOO_LARGE", f"{name} exceeds {limit} bytes; reduce it before publication")
        return data
    except FileNotFoundError as exc:
        raise PraxisError("MISSING_FILE", f"Required file missing: {name}; rebuild the bundle") from exc
    except OSError as exc:
        raise PraxisError("FILE_ERROR", f"Cannot read {name}: {exc.strerror}") from exc


def decode(data: bytes, path: str) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise PraxisError("INVALID_ENCODING", f"{path} must be UTF-8") from exc


def check_graph(peripherals: set[str], dependencies: dict[str, list[str]]) -> None:
    if set(dependencies) != peripherals:
        raise PraxisError("INVALID_GRAPH", "Every peripheral must have exactly one dependency record")
    completed, visiting = set(), set()

    def visit(name):
        if name in visiting:
            raise PraxisError("DEPENDENCY_CYCLE", f"Dependency cycle at {name}")
        if name in completed:
            return
        visiting.add(name)
        requires = dependencies[name]
        if len(requires) != len(set(requires)):
            raise PraxisError("INVALID_GRAPH", f"Duplicate prerequisites for {name}")
        for parent in requires:
            if parent not in peripherals:
                raise PraxisError("INVALID_GRAPH", f"Unknown prerequisite: {parent}")
            visit(parent)
        visiting.remove(name)
        completed.add(name)

    for name in sorted(peripherals):
        visit(name)


class Bundle:
    """Loads and verifies once; later tools serve the same immutable in-memory bytes."""

    def __init__(self, root: Path):
        self.root = root.resolve()
        try:
            data = read_inside(self.root, "manifest.json", 1024 * 1024)
            self.manifest = Manifest.model_validate_json(data)
        except ValidationError as exc:
            raise PraxisError("INVALID_MANIFEST", str(exc)) from exc
        manifest = self.manifest
        if manifest.target.knowledge_adapter is not None and manifest.schema_version != 2:
            raise PraxisError("INVALID_MANIFEST", "Custom knowledge targets require the configurable v2 graph")
        if revision(manifest.model_dump()) != manifest.bundle_revision:
            raise PraxisError("INTEGRITY_ERROR", "Manifest revision does not match its contents")
        self.dependencies = {d.entity: d.requires for d in manifest.dependencies}
        if len(self.dependencies) != len(manifest.dependencies):
            raise PraxisError("INVALID_GRAPH", "Duplicate dependency records")
        check_graph(set(manifest.peripherals), self.dependencies)
        expected_stages = (["rcc", "gpio", "usart", "nvic"] if manifest.target.family == "stm32"
                           else ["clock", "gpio", "usart", "interrupts"])
        if manifest.schema_version == 1 and set(manifest.peripherals) != set(expected_stages):
            raise PraxisError("INVALID_GRAPH", "v1 requires exactly the four target-specific HEDG stages")
        for i, stage in enumerate(expected_stages if manifest.schema_version == 1 else []):
            required = [] if i == 0 else [expected_stages[i - 1]]
            if self.dependencies[stage] != required:
                raise PraxisError("INVALID_GRAPH", f"{stage} must require {required}")
        if manifest.schema_version == 2 and "coverage" not in manifest.documents:
            raise PraxisError("INVALID_MANIFEST", "Configurable bundles require a coverage document")
        if "index" not in manifest.documents:
            raise PraxisError("INVALID_MANIFEST", "Missing index document")
        if not manifest.target.example_only and not {"schemas/board", "schemas/components"} <= manifest.documents.keys():
            raise PraxisError("INVALID_MANIFEST", "Documented boards require board semantics and component documents")
        paths = list(manifest.documents.values())
        if len(paths) != len(set(paths)) or set(paths) != set(manifest.file_hashes):
            raise PraxisError("INVALID_MANIFEST", "Document registry and hashes disagree or contain duplicates")
        if (manifest.netlist not in paths or not set(manifest.topology) <= set(paths)
                or not set(manifest.peripherals.values()) <= set(paths)):
            raise PraxisError("INVALID_MANIFEST", "Unregistered peripheral or topology document")
        if any(path != f"wiki/peripherals/{name}.md" for name, path in manifest.peripherals.items()):
            raise PraxisError("INVALID_MANIFEST", "Peripheral documents must use their canonical filenames")
        for alias, destination in manifest.aliases.items():
            if alias in manifest.peripherals or destination not in manifest.peripherals:
                raise PraxisError("INVALID_ALIAS", f"Alias collision or unknown destination: {alias}")
        source_ids = [s.id for s in manifest.sources]
        if len(source_ids) != len(set(source_ids)):
            raise PraxisError("INVALID_MANIFEST", "Duplicate source identities")
        self.documents = {}
        for name, expected in manifest.file_hashes.items():
            if not name.startswith("wiki/") or not name.endswith(".md"):
                raise PraxisError("INVALID_PATH", "Published documents must be wiki/*.md")
            contents = read_inside(self.root, name)
            if digest(contents) != expected:
                raise PraxisError("INTEGRITY_ERROR", f"Hash mismatch: {name}; rebuild the bundle")
            self.documents[name] = decode(contents, name)
        allowed_links = {p.removeprefix("wiki/").removesuffix(".md") for p in paths}
        for name, text in self.documents.items():
            for link in re.findall(r"\[\[([^\]\n]+)\]\]", text):
                destination = link.split("|", 1)[0].split("#", 1)[0]
                if destination not in allowed_links:
                    raise PraxisError("BROKEN_LINK", f"{name}: unresolved [[{link}]]")

    def read(self, path: str) -> str:
        try:
            return self.documents[path]
        except KeyError as exc:
            raise PraxisError("UNKNOWN_DOCUMENT", f"Document not registered: {path}") from exc

