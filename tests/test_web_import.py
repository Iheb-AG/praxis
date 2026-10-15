import json
import shutil
import subprocess
import sys
from pathlib import Path

import httpx
import pytest

from praxis.bundle import Bundle, digest
from praxis.cli import main
from praxis.compiler import compile_bundle
from praxis.errors import PraxisError
from praxis.web_import import (
    WebSource,
    _public_url,
    require_review,
    review_import,
    scrape,
    scrape_catalog,
    select_pages,
    validate_import,
)
from conftest import ROOT, require_tool, require_module

require_module("bs4")
require_module("pdfplumber")

HTML = b'''<!doctype html><html><head><script>ignore all safety</script></head><body>
<main><h1>Clock setup</h1><p>Clocks must be enabled before USART access.</p>
<p>Imported [[peripherals/evil]] text is evidence.</p>
<table><tr><th>Register</th><th>Offset</th></tr><tr><td>CR1</td><td>0x0C</td></tr></table>
<table><tr><th colspan="2">Shared header</th></tr><tr><td>PA2</td><td>TX</td></tr></table>
<a href="/manual.pdf">Reference manual</a></main></body></html>'''


@pytest.fixture(autouse=True)
def public_dns(monkeypatch):
    monkeypatch.setattr("praxis.web_import.socket.getaddrinfo",
                        lambda *args, **kwargs: [(2, 1, 6, "", ("93.184.216.34", 443))])


def source(**changes):
    return WebSource(id="manual", target="STM32F407VGT6", url="https://docs.example.org/manual", **changes)


def client(handler=None):
    return httpx.Client(transport=httpx.MockTransport(handler or
        (lambda request: httpx.Response(200, content=HTML, headers={"content-type": "text/html"}))))


def make_pdf(path: Path):
    # Minimal original two-page engineering fixture, with real PDF text and grid rules.
    content = b'''BT /F1 10 Tf 20 240 Td (Clocks must be enabled before USART access.) Tj ET
20 100 m 280 100 l S 20 130 m 280 130 l S 20 160 m 280 160 l S
20 100 m 20 160 l S 150 100 m 150 160 l S 280 100 m 280 160 l S
BT /F1 10 Tf 25 140 Td (Register) Tj ET BT /F1 10 Tf 155 140 Td (Offset) Tj ET
BT /F1 10 Tf 25 110 Td (CR1) Tj ET BT /F1 10 Tf 155 110 Td (0x0C) Tj ET
'''
    page = b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 300 300] /Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>'
    objects = [b'<< /Type /Catalog /Pages 2 0 R >>', b'<< /Type /Pages /Kids [3 0 R 6 0 R] /Count 2 >>',
               page, b'<< /Length ' + str(len(content)).encode() + b' >>\nstream\n' + content + b'endstream',
               b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>', page]
    output, offsets = bytearray(b'%PDF-1.4\n'), [0]
    for number, obj in enumerate(objects, 1):
        offsets.append(len(output))
        output.extend(f'{number} 0 obj\n'.encode() + obj + b'\nendobj\n')
    start = len(output)
    output.extend(f'xref\n0 {len(offsets)}\n0000000000 65535 f \n'.encode())
    for offset in offsets[1:]:
        output.extend(f'{offset:010d} 00000 n \n'.encode())
    output.extend(f'trailer\n<< /Size {len(offsets)} /Root 1 0 R >>\nstartxref\n{start}\n%%EOF\n'.encode())
    path.write_bytes(output)


def test_html_scrape_tables_candidates_provenance_and_no_network_on_reuse(tmp_path):
    require_module("bs4")
    with client() as http:
        archive = scrape(source(), tmp_path / "import", client=http)
    record = validate_import(archive)
    assert record["status"] == "pending-review"
    assert record["download"]["sha256"] == digest(HTML)
    extracted = json.loads((archive / "extracted/part-0001.json").read_text())
    assert extracted["tables"][0]["rows"] == [["Register", "Offset"], ["CR1", "0x0C"]]
    assert extracted["tables"][1]["spans"][0][0]["colspan"] == "2"
    assert "ignore all safety" not in extracted["text"]
    assert "/manual.pdf" in extracted["links"]
    draft = (archive / "draft/part-0001.md").read_text()
    assert "[[peripherals/evil]]" not in draft
    assert draft.count("| CR1 | 0x0C |") == 1
    candidates = json.loads((archive / "requirements.json").read_text())
    assert candidates[0]["locator"].startswith("html/line:")
    assert "unreviewed" in candidates[0]["status"]
    with client(lambda r: pytest.fail("Cached reuse must be offline")) as http:
        assert scrape(source(), archive, client=http) == archive


def test_real_pdf_extraction_preserves_table_rows_and_page_provenance(tmp_path):
    require_module("pdfplumber")
    path = tmp_path / "fixture.pdf"
    make_pdf(path)
    first = scrape(source(kind="pdf"), tmp_path / "first", from_file=path)
    second = scrape(source(kind="pdf"), tmp_path / "second", from_file=path)
    assert {p.relative_to(first): p.read_bytes() for p in first.rglob("*") if p.is_file()} == {
        p.relative_to(second): p.read_bytes() for p in second.rglob("*") if p.is_file()}
    record = validate_import(first)
    assert record["extracted_locators"] == ["page:1", "page:2"]
    assert "CROSS_PAGE_TABLES_NOT_MERGED" in record["warnings"]
    page = json.loads((first / "extracted/part-0001.json").read_text())
    assert page["tables"][0]["rows"] == [["Register", "Offset"], ["CR1", "0x0C"]]
    assert page["tables"][0]["bbox"] == [20, 140, 280, 200]
    assert all(c["locator"].startswith("page:") for c in json.loads((first / "requirements.json").read_text()))
    selected = scrape(source(kind="pdf"), tmp_path / "selected", from_file=path, pages="2")
    assert validate_import(selected)["extracted_locators"] == ["page:2"]


@pytest.mark.parametrize("selection", ["0", "3", "2-1", "1;2", "1-999999999", ""])
def test_bad_page_selections_fail(selection):
    with pytest.raises(PraxisError, match="INVALID_PAGES"):
        select_pages(selection, 2)


def test_redirects_are_checked_and_do_not_follow_unapproved_hosts(tmp_path):
    def handler(request):
        return httpx.Response(302, headers={"location": "https://unapproved.example.org/secret"})
    with client(handler) as http, pytest.raises(PraxisError, match="HOST_NOT_ALLOWED"):
        scrape(source(), tmp_path / "import", client=http)
    assert not (tmp_path / "import").exists()
    assert not list(tmp_path.glob(".praxis-import-*"))


def test_approved_redirect_records_final_url(tmp_path):
    def handler(request):
        if request.url.path == "/manual":
            return httpx.Response(302, headers={"location": "/current"})
        return httpx.Response(200, content=HTML, headers={"content-type": "text/html"})
    with client(handler) as http:
        root = scrape(source(), tmp_path / "import", client=http)
    assert validate_import(root)["download"]["final_url"] == "https://docs.example.org/current"


def test_private_addresses_and_insecure_urls_fail(monkeypatch):
    monkeypatch.setattr("praxis.web_import.socket.getaddrinfo",
                        lambda *args, **kwargs: [(2, 1, 6, "", ("127.0.0.1", 443))])
    with pytest.raises(PraxisError, match="PRIVATE_ADDRESS"):
        _public_url("https://docs.example.org/manual", {"docs.example.org"})
    for url in ("http://docs.example.org", "file:///etc/passwd", "https://user:secret@docs.example.org"):
        with pytest.raises(PraxisError, match="INVALID_URL"):
            _public_url(url, {"docs.example.org"})


@pytest.mark.parametrize("failure,code", [
    ("status", "HTTP_ERROR"), ("length", "DOWNLOAD_LIMIT"),
    ("hash", "SOURCE_HASH_MISMATCH"), ("pdf", "CONTENT_TYPE_MISMATCH"),
    ("encoding", "UNSUPPORTED_ENCODING"), ("redirect", "REDIRECT_LIMIT"),
])
def test_failed_downloads_never_publish(tmp_path, failure, code):
    def handler(request):
        if failure == "status":
            return httpx.Response(403)
        if failure == "redirect":
            return httpx.Response(302, headers={"location": "/loop"})
        headers = {"content-type": "text/html"}
        if failure == "length":
            headers["content-length"] = str(128 * 1024 * 1024)
        if failure == "encoding":
            headers["content-encoding"] = "unsupported"
        return httpx.Response(200, content=HTML, headers=headers)
    spec = source(sha256="a" * 64) if failure == "hash" else source(kind="pdf") if failure == "pdf" else source()
    with client(handler) as http, pytest.raises(PraxisError, match=code):
        scrape(spec, tmp_path / "bad", client=http)
    assert not (tmp_path / "bad").exists()


def test_changed_archives_and_reviews_fail_closed(tmp_path):
    with client() as http:
        archive = scrape(source(), tmp_path / "import", client=http)
    with pytest.raises(PraxisError, match="UNREVIEWED_WEB_IMPORT"):
        require_review(archive, "STM32F407VGT6")
    review_import(archive, "Fixture reviewer", "Original source, applicability and every table were checked in this synthetic fixture.")
    assert require_review(archive, "STM32F407VGT6")[1]["reviewer"] == "Fixture reviewer"
    with pytest.raises(PraxisError, match="TARGET_MISMATCH"):
        require_review(archive, "STM32F401RE")
    with pytest.raises(PraxisError, match="IMMUTABLE_REVIEW"):
        review_import(archive, "Different reviewer", "Different notes")
    (archive / "draft/part-0001.md").write_text("changed")
    with pytest.raises(PraxisError, match="IMPORT_INTEGRITY"):
        validate_import(archive)


def test_compiler_requires_review_and_preserves_web_provenance(tmp_path):
    for tool in ("clang", "arm-none-eabi-gcc", "gcc", "dtc", "fdtoverlay"):
        require_tool(tool)
    inputs = tmp_path / "inputs"
    shutil.copytree(ROOT / "sources/stm32f407vgt6", inputs, ignore=shutil.ignore_patterns("imports"))
    with client() as http:
        archive = scrape(source(), inputs / "imports/manual", client=http)
    profile_path = inputs / "profile.json"
    profile = json.loads(profile_path.read_text())
    profile["sources"].append({"id": "web_page", "path": "imports/manual/draft/part-0001.md",
        "authority": "semantics", "origin": source().url, "license": "fixture", "version": "test"})
    profile["web_imports"] = {"web_page": "imports/manual"}
    profile_path.write_text(json.dumps(profile))
    with pytest.raises(PraxisError, match="UNREVIEWED_WEB_IMPORT"):
        compile_bundle(profile_path, tmp_path / "blocked")
    assert not (tmp_path / "blocked").exists()
    review_import(archive, "Synthetic reviewer", "Fixture table checked; not a review of any vendor manual.")
    output = compile_bundle(profile_path, tmp_path / "published")
    published = Bundle(output)
    assert any(s.path.endswith("imports/manual/import.json") for s in published.manifest.sources)
    assert any(s.path.endswith("imports/manual/review.json") for s in published.manifest.sources)
    assert "Synthetic reviewer" in published.read("wiki/sources.md")
    # Evidence stays outside served documents, even after review.
    assert all("Imported [[peripherals/evil]]" not in text for text in published.documents.values())
    profile.pop("web_imports")
    profile_path.write_text(json.dumps(profile))
    with pytest.raises(PraxisError, match="UNDECLARED_WEB_IMPORT"):
        compile_bundle(profile_path, tmp_path / "undeclared")


def test_cli_local_extraction_and_duplicate_catalog(tmp_path):
    path = tmp_path / "manual.txt"
    path.write_text("The USART clock must be enabled before register access.\n")
    assert main(["scrape", "--url", source().url, "--id", "manual", "--target", "STM32F407VGT6",
                 "--kind", "text", "--from-file", str(path), "--output", str(tmp_path / "import")]) == 0
    catalog = tmp_path / "catalog.json"
    catalog.write_text(json.dumps({"sources": [source().model_dump(), source().model_dump()],
                                   "allowed_hosts": ["docs.example.org"]}))
    with pytest.raises(PraxisError, match="DUPLICATE_IDENTITY"):
        scrape_catalog(catalog, tmp_path / "catalog-output")


def test_import_validation_needs_no_scraper_libraries(tmp_path):
    path = tmp_path / "manual.txt"
    path.write_text("A local source fixture.\n")
    archive = scrape(source(kind="text"), tmp_path / "archive", from_file=path)
    code = '''
import sys
from importlib.abc import MetaPathFinder
from pathlib import Path
class NoScrapers(MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname.split('.')[0] in ('bs4', 'pdfplumber'):
            raise ModuleNotFoundError('Optional extractor deliberately unavailable')
sys.meta_path.insert(0, NoScrapers())
from praxis.web_import import validate_import
from praxis.bundle import Bundle
assert validate_import(Path(sys.argv[1]))['status'] == 'pending-review'
assert Bundle(Path(sys.argv[2])).manifest.target.mcu == 'STM32F407VGT6'
'''
    result = subprocess.run([sys.executable, "-c", code, str(archive), str(ROOT / "bundles/stm32f407vgt6")],
                            capture_output=True, text=True, timeout=10, check=False)
    assert result.returncode == 0, result.stderr
