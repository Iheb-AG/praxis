"""Optional online acquisition into immutable, unreviewed evidence archives.

Network and document-parser dependencies load only when explicitly scraping.
Neither this module nor its archives are part of the MCP retrieval interface.
PDF tables remain source-local fragments until a reviewer resolves continuity.
"""

from __future__ import annotations

import ipaddress
import json
import os
import re
import socket
import tempfile
import time
from datetime import UTC, datetime
from importlib.metadata import version
from pathlib import Path
from typing import Literal
from urllib.parse import urljoin, urlsplit

from pydantic import Field, ValidationError, field_validator

from praxis.bundle import digest, read_inside
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import Digest, Identifier, Record
from praxis.render import table

FORMAT = "praxis.web-import/v1"
MAX_DOWNLOAD = 64 * 1024 * 1024
MAX_EXTRACTION = 64 * 1024 * 1024
MAX_PAGE = 1024 * 1024
MAX_PAGES = 2500
USER_AGENT = "Project-Praxis/0.1 document-importer"
REQUIREMENT = re.compile(r"\b(?:must|shall|required|before|only when|reserved|write.one.to.clear)\b", re.I)


class WebSource(Record):
    id: Identifier
    target: str = Field(min_length=1, max_length=128)
    url: str = Field(min_length=1, max_length=4096)
    kind: str = Field(default="auto", pattern=r"^(auto|pdf|html|text)$")
    title: str = Field(default="", max_length=256)
    sha256: Digest | None = None

    @field_validator("url")
    @classmethod
    def https_only(cls, value):
        parts = urlsplit(value)
        if (parts.scheme != "https" or not parts.hostname or parts.username or parts.password
                or parts.fragment or any(ord(c) < 33 for c in value)):
            raise ValueError("Use a public HTTPS URL without credentials, fragments or whitespace")
        try:
            if parts.port not in (None, 443):
                raise ValueError("Only standard HTTPS port 443 is supported")
        except ValueError as exc:
            raise ValueError("Invalid HTTPS port") from exc
        return value


class Catalog(Record):
    schema_version: int = Field(default=1, ge=1, le=1)
    allowed_hosts: list[str] = Field(min_length=1)
    sources: list[WebSource] = Field(min_length=1, max_length=32)


class DownloadRecord(Record):
    original_url: str
    final_url: str
    sha256: Digest
    bytes: int = Field(gt=0, le=MAX_DOWNLOAD)
    transport: Literal["https", "local; URL is user-declared provenance"]
    fetched_at: str | None
    headers: dict[str, str]


class ImportRecord(Record):
    format: Literal[FORMAT]
    source: WebSource
    download: DownloadRecord
    selection: str | None
    extracted_locators: list[str]
    extractors: dict[str, str]
    status: Literal["pending-review"]
    warnings: list[str]
    file_hashes: dict[str, Digest] = Field(min_length=1, max_length=10_000)
    import_revision: Digest


class ReviewReceipt(Record):
    format: Literal[FORMAT]
    status: Literal["reviewed"]
    import_revision: Digest
    target: str
    reviewer: str = Field(min_length=1, max_length=256)
    notes: str = Field(min_length=1, max_length=65536)

    @field_validator("reviewer", "notes")
    @classmethod
    def meaningful_review(cls, value):
        if not value.strip():
            raise ValueError("Review identity and notes cannot be whitespace")
        return value


def _json(data) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def _revision(record: dict) -> str:
    stable = {k: v for k, v in record.items() if k != "import_revision"}
    stable["download"] = {k: v for k, v in stable["download"].items() if k != "fetched_at"}
    return digest(_json(stable))


def _public_url(url: str, allowed_hosts: set[str]):
    # Redirects use the same validation as initial requests. Private destinations
    # are unavailable; this is a local explicit-URL importer, not a public proxy.
    try:
        WebSource(id="check", target="check", url=url)
    except ValidationError as exc:
        raise PraxisError("INVALID_URL", "Use public HTTPS on port 443 without URL credentials") from exc
    host = urlsplit(url).hostname.lower()
    if host not in allowed_hosts:
        raise PraxisError("HOST_NOT_ALLOWED", f"Explicitly allow redirect/download host: {host}")
    try:
        addresses = {entry[4][0] for entry in socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)}
    except OSError as exc:
        raise PraxisError("DOWNLOAD_FAILED", f"Cannot resolve {host}") from exc
    if not addresses or any(not ipaddress.ip_address(address).is_global for address in addresses):
        raise PraxisError("PRIVATE_ADDRESS", "Web imports require publicly routed HTTPS hosts")


def download(source: WebSource, destination: Path, allowed_hosts: set[str], *, client=None) -> dict:
    """Stream a bounded download; follow at most five explicitly allowed redirects."""
    try:
        import httpx
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[web] for online document ingestion") from exc
    if client is None:
        with httpx.Client(timeout=httpx.Timeout(20, connect=10), follow_redirects=False,
                          trust_env=False, headers={"User-Agent": USER_AGENT,
                                                    "Accept-Encoding": "identity"}) as owned:
            return download(source, destination, allowed_hosts, client=owned)
    url, start = source.url, time.monotonic()
    try:
        for _ in range(6):
            _public_url(url, allowed_hosts)
            with client.stream("GET", url, follow_redirects=False, headers={"User-Agent": USER_AGENT,
                                                    "Accept-Encoding": "identity"}) as response:
                if response.status_code in (301, 302, 303, 307, 308):
                    location = response.headers.get("location")
                    if not location:
                        raise PraxisError("DOWNLOAD_FAILED", "Redirect is missing its Location header")
                    url = urljoin(url, location)
                    continue
                if response.status_code != 200:
                    raise PraxisError("HTTP_ERROR", f"HTTP {response.status_code} for {url}; no access-control bypass is attempted")
                if response.headers.get("content-encoding", "identity").lower() not in ("", "identity"):
                    raise PraxisError("UNSUPPORTED_ENCODING", "Server must honor Accept-Encoding: identity")
                length = response.headers.get("content-length")
                if length and (not length.isdigit() or int(length) > MAX_DOWNLOAD):
                    raise PraxisError("DOWNLOAD_LIMIT", "Remote document exceeds 64 MiB or has an invalid length")
                total = 0
                with destination.open("wb") as handle:
                    for chunk in response.iter_bytes(chunk_size=65536):
                        total += len(chunk)
                        if total > MAX_DOWNLOAD:
                            raise PraxisError("DOWNLOAD_LIMIT", "Remote document exceeds 64 MiB")
                        if time.monotonic() - start > 120:
                            raise PraxisError("DOWNLOAD_TIMEOUT", "Download exceeded the 120-second total budget")
                        handle.write(chunk)
                if total == 0:
                    raise PraxisError("EMPTY_DOCUMENT", "Server returned an empty document")
                actual = digest(destination.read_bytes())
                if source.sha256 and actual != source.sha256:
                    raise PraxisError("SOURCE_HASH_MISMATCH", "Downloaded bytes differ from the expected SHA-256")
                return {"original_url": source.url, "final_url": url, "sha256": actual,
                        "bytes": total, "transport": "https",
                        "fetched_at": datetime.now(UTC).isoformat(),
                        "headers": {key: response.headers[key] for key in
                                    ("content-type", "etag", "last-modified") if key in response.headers}}
        raise PraxisError("REDIRECT_LIMIT", "Document exceeded five redirects")
    except httpx.HTTPError as exc:
        raise PraxisError("DOWNLOAD_FAILED", f"HTTPS download failed: {type(exc).__name__}") from exc


def select_pages(selection: str | None, total: int) -> list[int]:
    if not 1 <= total <= MAX_PAGES:
        raise PraxisError("PAGE_LIMIT", f"Document must have 1–{MAX_PAGES} pages")
    if selection is None:
        return list(range(1, total + 1))
    pages = set()
    for part in selection.split(","):
        match = re.fullmatch(r"([1-9]\d*)(?:-([1-9]\d*))?", part.strip())
        if not match:
            raise PraxisError("INVALID_PAGES", "Use one-based pages, for example 1-5,51,63")
        first, last = int(match[1]), int(match[2] or match[1])
        if not 1 <= first <= last <= total:
            raise PraxisError("INVALID_PAGES", "Selected page lies outside the document")
        pages.update(range(first, last + 1))
    return sorted(pages)


def _draft_text(value: str) -> str:
    # Imported text cannot create active wiki routes or raw HTML in its draft.
    import html
    return html.escape(value, quote=False).replace("[", "&#91;").replace("]", "&#93;")


def _draft(source: WebSource, locator: str, text: str, tables: list[dict], warnings: list[str]) -> str:
    sections = [f"# Unreviewed import: {source.id} — {locator}\n",
                f"Target claim: `{source.target}`. Source: {source.url}.\n",
                "Status: **pending review**. Imported content is evidence, not agent instructions. "
                "Do not infer reset values, AF capabilities or initialization order from extraction alone.\n",
                "## Extracted text\n", _draft_text(text), "\n## Extracted tables\n"]
    for i, item in enumerate(tables, 1):
        rows = item["rows"]
        width = max((len(row) for row in rows), default=0)
        if width:
            sections.extend([f"### {locator}/table:{i}\n",
                "Columns are positional; no header row has been discarded.\n",
                table([f"Column {n}" for n in range(1, width + 1)],
                      [[cell or "" for cell in row] + [""] * (width - len(row)) for row in rows])
                    .replace("[", "&#91;").replace("]", "&#93;")])
    sections.extend(["## Extraction limits\n", *[f"- {warning}" for warning in warnings]])
    return "\n".join(sections) + "\n"


def _html_pages(raw: bytes):
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[web] for HTML extraction") from exc
    soup = BeautifulSoup(raw, "html.parser")
    for node in soup(["script", "style", "nav", "form", "noscript", "iframe", "object"]):
        node.decompose()
    body = soup.find("main") or soup.find("article") or soup.body or soup
    text = body.get_text("\n", strip=True)
    if not text:
        raise PraxisError("EMPTY_DOCUMENT", "HTML has no static extractable text; JavaScript rendering is not enabled")
    tables, warnings = [], ["HTML_TABLES_REQUIRE_REVIEW"]
    for element in body.find_all("table"):
        if element.find_parent("table") is not None:
            warnings.append("NESTED_TABLE_PRESENT: inspect original HTML")
            continue
        rows, spans = [], []
        for row in element.find_all("tr"):
            if row.find_parent("table") is not element:
                continue
            cells = row.find_all(["th", "td"], recursive=False)
            rows.append([cell.get_text("\n", strip=True) for cell in cells])
            spans.append([{key: cell.get(key, "1") for key in ("rowspan", "colspan")} for cell in cells])
        if any(cell[key] != "1" for row in spans for cell in row for key in ("rowspan", "colspan")):
            warnings.append("MERGED_CELLS_PRESENT: JSON preserves spans; Markdown columns are positional")
        tables.append({"rows": rows, "spans": spans, "locator": f"html/table:{len(tables) + 1}"})
    links = sorted({node.get("href") for node in soup.find_all("a", href=True)})
    yield {"locator": "html", "text": text, "tables": tables, "warnings": sorted(set(warnings)),
           "links": links}


def _pdf_pages(path: Path, selection: str | None):
    try:
        import pdfplumber
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[web] for PDF extraction") from exc
    try:
        with pdfplumber.open(path) as document:
            pages = select_pages(selection, len(document.pages))
            for number in pages:
                page = document.pages[number - 1]
                text = page.extract_text(layout=True) or ""
                tables = [{"rows": found.extract(), "bbox": list(found.bbox),
                           "locator": f"page:{number}/table:{i}"}
                          for i, found in enumerate(page.find_tables(), 1)]
                warnings = ["PDF_TABLES_REQUIRE_VISUAL_REVIEW", "CROSS_PAGE_TABLES_NOT_MERGED"]
                if not text.strip():
                    warnings.append("OCR_REQUIRED: no text layer found; OCR is not enabled")
                if not tables:
                    warnings.append("NO_TABLES_DETECTED: inspect source; absence is not proof of no tables")
                yield {"locator": f"page:{number}", "page": number, "total_pages": len(document.pages),
                       "text": text, "tables": tables, "warnings": warnings}
                page.close()
    except PraxisError:
        raise
    except Exception as exc:
        raise PraxisError("PDF_EXTRACTION_FAILED", f"PDF parser failed: {type(exc).__name__}; inspect the source file") from exc


def validate_import(root: Path) -> dict:
    record = load_json(read_inside(root, "import.json", 4 * 1024 * 1024))
    try:
        ImportRecord.model_validate(record)
    except ValidationError as exc:
        raise PraxisError("IMPORT_INTEGRITY", "Import metadata is malformed") from exc
    if record["import_revision"] != _revision(record):
        raise PraxisError("IMPORT_INTEGRITY", "Import metadata or revision is invalid")
    hashes = record["file_hashes"]
    raw_files = set(hashes) & {"source.pdf", "source.html", "source.txt"}
    if len(raw_files) != 1 or hashes[next(iter(raw_files))] != record["download"]["sha256"]:
        raise PraxisError("IMPORT_INTEGRITY", "Raw source registry and download hash disagree")
    for name, expected in hashes.items():
        data = read_inside(root, name, MAX_DOWNLOAD)
        if digest(data) != expected:
            raise PraxisError("IMPORT_INTEGRITY", f"Imported artifact changed: {name}")
        if name in raw_files and len(data) != record["download"]["bytes"]:
            raise PraxisError("IMPORT_INTEGRITY", "Raw source size disagrees with metadata")
    return record


def scrape(source: WebSource, output: Path, *, allowed_hosts: list[str] | None = None,
           pages: str | None = None, from_file: Path | None = None, client=None) -> Path:
    """Download/extract once into a new immutable archive; never publish to wiki."""
    output = output.absolute()
    if output.exists() or output.is_symlink():
        existing = validate_import(output)
        if (existing["source"] != source.model_dump() or existing["selection"] != pages or
                from_file is not None and digest(read_inside(from_file.parent.resolve(), from_file.name, MAX_DOWNLOAD)) != existing["download"]["sha256"]):
            raise PraxisError("IMMUTABLE_IMPORT", "Choose a new output directory for a changed source or selection")
        return output
    output.parent.mkdir(parents=True, exist_ok=True)
    hosts = {host.lower() for host in (allowed_hosts or [urlsplit(source.url).hostname])}
    with tempfile.TemporaryDirectory(prefix=".praxis-import-", dir=output.parent) as temporary:
        root = Path(temporary) / "archive"
        root.mkdir()
        raw = root / "source.download"
        if from_file is None:
            metadata = download(source, raw, hosts, client=client)
        else:
            data = read_inside(from_file.parent.resolve(), from_file.name, MAX_DOWNLOAD)
            actual = digest(data)
            if source.sha256 and actual != source.sha256:
                raise PraxisError("SOURCE_HASH_MISMATCH", "Local bytes differ from expected SHA-256")
            raw.write_bytes(data)
            metadata = {"original_url": source.url, "final_url": source.url, "sha256": actual,
                        "bytes": len(data), "transport": "local; URL is user-declared provenance",
                        "fetched_at": None, "headers": {}}
        prefix = raw.read_bytes()[:1024].lstrip()
        media = metadata["headers"].get("content-type", "").split(";", 1)[0].lower()
        kind = source.kind
        if kind == "auto":
            if prefix.startswith(b"%PDF-"):
                kind = "pdf"
            elif media in ("text/html", "application/xhtml+xml") or prefix.lower().startswith((b"<!doctype html", b"<html")):
                kind = "html"
            elif media == "text/plain":
                kind = "text"
            else:
                raise PraxisError("UNSUPPORTED_DOCUMENT", "Specify --kind pdf, html or text for this source")
        if kind == "pdf" and not prefix.startswith(b"%PDF-"):
            raise PraxisError("CONTENT_TYPE_MISMATCH", "Expected PDF bytes; server may have returned an access page")
        if pages is not None and kind != "pdf":
            raise PraxisError("INVALID_PAGES", "Page selection is only supported for PDF documents")
        name = {"pdf": "source.pdf", "html": "source.html", "text": "source.txt"}[kind]
        raw.rename(root / name)
        raw = root / name
        hashes, total, candidates, warnings, locators = {name: metadata["sha256"]}, 0, [], set(), []

        def write(path: str, data: bytes, *, limit: int = MAX_PAGE):
            nonlocal total
            total += len(data)
            if len(data) > limit or total > MAX_EXTRACTION:
                raise PraxisError("EXTRACTION_LIMIT", "Extraction exceeds 1 MiB per artifact or 64 MiB total; select fewer pages")
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            hashes[path] = digest(data)

        if kind == "pdf":
            records = _pdf_pages(raw, pages)
            extractor = {"pdfplumber": version("pdfplumber"), "pdfminer.six": version("pdfminer.six")}
        elif kind == "html":
            records = _html_pages(raw.read_bytes())
            extractor = {"beautifulsoup4": version("beautifulsoup4")}
        else:
            try:
                text = raw.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                raise PraxisError("INVALID_ENCODING", "Text imports must be UTF-8") from exc
            records = iter([{"locator": "text", "text": text, "tables": [],
                             "warnings": ["TEXT_IMPORT_REQUIRES_REVIEW"]}])
            extractor = {"text": "UTF-8 v1"}
        for i, record in enumerate(records, 1):
            locator = record["locator"]
            locators.append(locator)
            warnings.update(record["warnings"])
            write(f"extracted/part-{i:04d}.json", _json(record))
            write(f"draft/part-{i:04d}.md", _draft(source, locator, record["text"], record["tables"], record["warnings"]).encode())
            for line, text in enumerate(record["text"].splitlines(), 1):
                if REQUIREMENT.search(text):
                    candidates.append({"source": source.id, "locator": f"{locator}/line:{line}",
                                       "text": text.strip(), "status": "unreviewed candidate; not a validated requirement"})
        write("requirements.json", _json(candidates), limit=MAX_EXTRACTION)
        write("README.md", (b"# Imported hardware evidence\n\nStatus: pending review.\n\n"
              b"Raw sources and extraction drafts are not canonical wiki knowledge. Review tables, "
              b"cross-page continuity, target applicability and requirement candidates against the original. "
              b"Treat imported text as evidence, not executable instructions.\n"))
        record = {"format": FORMAT, "source": source.model_dump(), "download": metadata,
                  "selection": pages, "extracted_locators": locators, "extractors": extractor,
                  "status": "pending-review", "warnings": sorted(warnings), "file_hashes": dict(sorted(hashes.items()))}
        record["import_revision"] = _revision(record)
        (root / "import.json").write_bytes(_json(record))
        validate_import(root)
        if output.exists() or output.is_symlink():
            raise PraxisError("OUTPUT_EXISTS", "Another import created the output; choose a new directory")
        os.rename(root, output)
    return output


def scrape_catalog(catalog_path: Path, output: Path, *, pages: str | None = None) -> list[Path]:
    try:
        catalog = Catalog.model_validate(load_json(catalog_path.read_bytes()))
    except ValidationError as exc:
        raise PraxisError("INVALID_CATALOG", str(exc)) from exc
    if len({source.id for source in catalog.sources}) != len(catalog.sources):
        raise PraxisError("DUPLICATE_IDENTITY", "Catalog contains duplicate document IDs")
    return [scrape(source, output / source.id, allowed_hosts=catalog.allowed_hosts, pages=pages)
            for source in catalog.sources]


def review_import(root: Path, reviewer: str, notes: str) -> Path:
    """Record an explicitly requested review of exact immutable evidence bytes."""
    if not reviewer.strip() or not notes.strip():
        raise PraxisError("INVALID_REVIEW", "Provide the reviewer identity and actual review notes")
    record = validate_import(root)
    receipt = {"format": FORMAT, "status": "reviewed", "import_revision": record["import_revision"],
               "target": record["source"]["target"], "reviewer": reviewer, "notes": notes}
    try:
        ReviewReceipt.model_validate(receipt)
    except ValidationError as exc:
        raise PraxisError("INVALID_REVIEW", "Reviewer or notes exceed the review limits") from exc
    destination = root / "review.json"
    if destination.exists():
        if destination.read_bytes() != _json(receipt):
            raise PraxisError("IMMUTABLE_REVIEW", "A different review already exists; create a new import revision")
    else:
        with destination.open("xb") as handle:
            handle.write(_json(receipt))
    return destination


def require_review(root: Path, target: str) -> tuple[dict, dict]:
    record = validate_import(root)
    try:
        receipt = ReviewReceipt.model_validate(load_json(read_inside(root, "review.json", 256 * 1024)))
    except (PraxisError, ValidationError) as exc:
        raise PraxisError("UNREVIEWED_WEB_IMPORT", "Review this exact import and record reviewer/notes with praxis review-import") from exc
    if receipt.import_revision != record["import_revision"]:
        raise PraxisError("IMPORT_INTEGRITY", "Review does not cover the current imported bytes")
    if record["source"]["target"] != target or receipt.target != target:
        raise PraxisError("TARGET_MISMATCH", "Web evidence/review targets a different MCU")
    return record, receipt.model_dump()
