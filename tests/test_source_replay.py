"""Clean-checkout input restoration must preserve original hashes and receipts."""

import json
import shutil

import httpx
import pytest

from conftest import ROOT
from praxis.errors import PraxisError
from praxis.web_import import WebSource, require_review, review_import, scrape
from tools.restore_source_inputs import checked_manifest, restore


@pytest.fixture
def replay(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "praxis.web_import.socket.getaddrinfo",
        lambda *a, **kw: [(2, 1, 6, "", ("93.184.216.34", 443))],
    )
    body = b"Original synthetic engineering fixture; clocks must be enabled first.\n"
    mcu = json.loads((ROOT / "sources/atmega328p/profile.json").read_bytes())["target"]["mcu"]
    source = WebSource(id="manual", target=mcu, kind="text", url="https://docs.example.org/manual")
    client = httpx.Client(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, content=body))
    )
    with client:
        historical = scrape(source, tmp_path / "historical", client=client)
    review_import(
        historical, "Synthetic fixture author", "Original test review, not hardware approval"
    )
    record = json.loads((historical / "import.json").read_bytes())
    manifest = tmp_path / "source-replay.json"
    manifest.write_text(
        json.dumps(
            dict(
                format="praxis-source-replay-v1",
                allowed_hosts=["docs.example.org"],
                archives=[
                    dict(
                        path="imports/original",
                        record_utf8=(historical / "import.json").read_text(),
                        review_utf8=(historical / "review.json").read_text(),
                    )
                ],
            )
        )
    )
    root = tmp_path / "checkout"
    shutil.copytree(ROOT / "sources/atmega328p", root, ignore=shutil.ignore_patterns("imports"))
    profile = root / "profile.json"
    data = json.loads(profile.read_bytes())
    data["web_imports"] = {"replay_manual": "imports/original"}
    data["sources"].append(
        dict(
            id="replay_manual",
            path="imports/original/extracted/part-0001.json",
            authority="semantics",
            version="fixture-original",
            license="MIT",
            origin=source.url,
            expected_sha256=record["file_hashes"]["extracted/part-0001.json"],
        )
    )
    profile.write_text(json.dumps(data))
    return manifest, profile, tmp_path / "cache", historical, body


def execute(replay, *, body=None):
    manifest, profile, cache, _, original = replay
    with httpx.Client(
        transport=httpx.MockTransport(
            lambda request: httpx.Response(200, content=original if body is None else body)
        )
    ) as client:
        return restore(manifest, profile, cache, client=client)


@pytest.mark.parametrize("optional_profile_pin", [False, True])
def test_exact_original_content_metadata_and_review_survive_a_fresh_checkout(
    replay, optional_profile_pin
):
    manifest, profile, cache, historical, _ = replay
    if optional_profile_pin:
        data = json.loads(profile.read_bytes())
        data["sources"][-1]["expected_sha256"] = None
        profile.write_text(json.dumps(data))
    result = execute(replay)
    assert result["passed"] and result["new_reviews"] == result["published_bundles_changed"] == 0
    recovered = profile.parent / "imports/original"
    assert {
        p.relative_to(historical): p.read_bytes() for p in historical.rglob("*") if p.is_file()
    } == {p.relative_to(recovered): p.read_bytes() for p in recovered.rglob("*") if p.is_file()}
    require_review(recovered, json.loads(profile.read_bytes())["target"]["mcu"])

    def no_network(request):
        pytest.fail("A verified existing archive must not be downloaded again")

    with httpx.Client(transport=httpx.MockTransport(no_network)) as client:
        result = restore(manifest, profile, cache, client=client)
    assert result["archives"][0]["status"] == "verified existing"


def test_changed_vendor_bytes_never_restore_receipt_or_partial_archive(replay):
    with pytest.raises(PraxisError, match="SOURCE_HASH_MISMATCH"):
        execute(replay, body=b"Different source revision")
    assert not (replay[1].parent / "imports/original").exists()


def test_corrupt_download_cache_and_wrong_profile_pin_fail_before_publication(replay):
    manifest, profile, cache, historical, _ = replay
    record = json.loads((historical / "import.json").read_bytes())
    cache.mkdir()
    raw = cache / record["download"]["sha256"]
    raw.write_bytes(b"corrupted cache")
    with pytest.raises(PraxisError, match="SOURCE_HASH_MISMATCH"):
        execute(replay)
    raw.unlink()
    data = json.loads(profile.read_bytes())
    data["sources"][-1]["expected_sha256"] = "f" * 64
    profile.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match="SOURCE_HASH_MISMATCH.*Profile pin"):
        execute(replay)
    assert manifest.exists() and not (profile.parent / "imports/original").exists()


def test_changed_extraction_never_receives_the_historical_review(replay, monkeypatch):
    from tools import restore_source_inputs as module

    original = module.scrape

    def different_extraction(*args, **kwargs):
        path = original(*args, **kwargs)
        record_path = path / "import.json"
        record = json.loads(record_path.read_bytes())
        record["warnings"].append("Different extractor behavior")
        record_path.write_text(json.dumps(record))
        return path

    monkeypatch.setattr(module, "scrape", different_extraction)
    with pytest.raises(PraxisError, match="REPLAY_MISMATCH.*warnings"):
        execute(replay)
    assert not (replay[1].parent / "imports/original").exists()


@pytest.mark.parametrize("change", ["duplicate", "traversal", "receipt", "record", "host"])
def test_bad_replay_metadata_fails_closed(replay, change):
    manifest, profile, _, _, _ = replay
    data = json.loads(manifest.read_bytes())
    entry = data["archives"][0]
    if change == "duplicate":
        data["archives"].append(entry)
    elif change == "traversal":
        entry["path"] = "../imports/escape"
    elif change == "receipt":
        receipt = json.loads(entry["review_utf8"])
        receipt["import_revision"] = "f" * 64
        entry["review_utf8"] = json.dumps(receipt)
    elif change == "record":
        record = json.loads(entry["record_utf8"])
        record["selection"] = "1"
        entry["record_utf8"] = json.dumps(record)
    elif change == "host":
        data["allowed_hosts"] = ["another.example.org"]
    manifest.write_text(json.dumps(data))
    with pytest.raises(PraxisError):
        execute(replay)
    assert not (profile.parent / "imports/original").exists()


@pytest.mark.parametrize("change", ["source", "extracted", "receipt", "symlink"])
def test_existing_archives_are_verified_and_never_overwritten(replay, change, tmp_path):
    execute(replay)
    archive = replay[1].parent / "imports/original"
    path = (
        archive
        / {
            "source": "source.txt",
            "extracted": "extracted/part-0001.json",
            "receipt": "review.json",
            "symlink": "source.txt",
        }[change]
    )
    if change == "symlink":
        external = tmp_path / "external"
        external.write_bytes(path.read_bytes())
        path.unlink()
        path.symlink_to(external)
    else:
        path.write_bytes(path.read_bytes() + (b" " if change == "receipt" else b"changed"))
    with pytest.raises(PraxisError):
        execute(replay)


def test_incompatible_extractor_fails_before_download_or_publication(replay, monkeypatch):
    manifest = replay[0]
    data = json.loads(manifest.read_bytes())
    record = json.loads(data["archives"][0]["record_utf8"])
    # Version lookup itself is tested against the untouched original metadata.
    from tools import restore_source_inputs as module

    original = module.checked_manifest

    def pdf_version_record(path):
        data, records = original(path)
        records[0][1]["extractors"] = {"pdfplumber": "incompatible"}
        return data, records

    monkeypatch.setattr(module, "checked_manifest", pdf_version_record)
    assert record["extractors"] == {"text": "UTF-8 v1"}
    with pytest.raises(PraxisError, match="EXTRACTOR_VERSION"):
        execute(replay)
    assert not (replay[1].parent / "imports/original").exists()


def test_shipped_replay_covers_full_profile_without_embedding_document_content():
    root = ROOT / "sources/stm32f407g-disc1"
    data, records = checked_manifest(root / "source-replay.json")
    from praxis.models import Profile

    profile = Profile.model_validate_json((root / "profile-timer-irq-v1.json").read_bytes())
    assert {r[0] for r in records} == set(profile.web_imports.values()) and len(records) == 16
    assert set(data["allowed_hosts"]) == {"www.st.com", "raw.githubusercontent.com"}
    for _, record, record_text, review_text in records:
        assert record["download"]["sha256"] in record["file_hashes"].values()
        assert json.loads(record_text)["file_hashes"] == record["file_hashes"]
        assert json.loads(review_text)["status"] == "reviewed"
        assert not {"text", "tables"} & record.keys()
