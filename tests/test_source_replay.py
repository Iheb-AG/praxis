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


def test_transient_read_timeouts_retry_without_changing_receipts(replay, monkeypatch, capsys):
    attempts, waits = [], []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', waits.append)

    def handler(request):
        attempts.append(str(request.url))
        if len(attempts) < 3:
            raise httpx.ReadTimeout('fixture timeout', request=request)
        return httpx.Response(200, content=replay[4])

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        result = restore(*replay[:3], client=client)
    assert result['passed'] and waits == [2, 4]
    assert attempts == ['https://docs.example.org/manual'] * 3
    archive = replay[1].parent / 'imports/original'
    for name in ('import.json', 'review.json', 'source.txt'):
        assert (archive / name).read_bytes() == (replay[3] / name).read_bytes()
    assert 'ReadTimeout' in capsys.readouterr().err


def test_exhausted_timeouts_fail_with_bounded_attempts_and_no_partial_publication(replay, monkeypatch, capsys):
    calls, waits = [], []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', waits.append)

    def handler(request):
        calls.append(request.url)
        raise httpx.ReadTimeout('persistent timeout', request=request)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(PraxisError, match='DOWNLOAD_FAILED.*failed after 4 attempts.*ReadTimeout'):
            restore(*replay[:3], client=client)
    assert len(calls) == 4 and waits == [2, 4, 8]
    assert not (replay[1].parent / 'imports/original').exists()
    assert list(replay[2].iterdir()) == []
    assert 'attempt 4/4' in capsys.readouterr().err


@pytest.mark.parametrize('status', [408, 429, 500, 502, 503, 504])
def test_only_transient_http_statuses_are_retried(replay, monkeypatch, status):
    calls, waits = [], []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', waits.append)

    def handler(request):
        calls.append(request.url)
        return httpx.Response(status) if len(calls) == 1 else httpx.Response(200, content=replay[4])

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        assert restore(*replay[:3], client=client)['passed']
    assert len(calls) == 2 and waits == [2]


@pytest.mark.parametrize('status', [400, 401, 403, 404])
def test_permanent_http_failures_are_not_retried(replay, monkeypatch, status):
    calls = []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', lambda seconds: pytest.fail('No retry allowed'))

    def handler(request):
        calls.append(request.url)
        return httpx.Response(status)

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(PraxisError, match=f'HTTP_ERROR: HTTP {status}'):
            restore(*replay[:3], client=client)
    assert len(calls) == 1
    assert list(replay[2].iterdir()) == []


def test_changed_bytes_after_a_transient_failure_still_fail_immediately(replay, monkeypatch):
    calls, waits = [], []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', waits.append)

    def handler(request):
        calls.append(request.url)
        return httpx.Response(503) if len(calls) == 1 else httpx.Response(200, content=b'new vendor revision')

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(PraxisError, match='SOURCE_HASH_MISMATCH'):
            restore(*replay[:3], client=client)
    assert len(calls) == 2 and waits == [2]
    assert list(replay[2].iterdir()) == []
    assert not (replay[1].parent / 'imports/original').exists()


def test_partial_stream_is_discarded_before_retry(replay, monkeypatch):
    calls = []
    monkeypatch.setattr('tools.restore_source_inputs.time.sleep', lambda seconds: None)

    class BrokenStream(httpx.SyncByteStream):
        def __iter__(self):
            yield b'x' * 65536  # Enough to reach the destination before the timeout.
            raise httpx.ReadTimeout('interrupted download')

    def handler(request):
        calls.append(request.url)
        return (httpx.Response(200, stream=BrokenStream()) if len(calls) == 1
                else httpx.Response(200, content=replay[4]))

    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        assert restore(*replay[:3], client=client)['passed']
    assert len(calls) == 2
    assert next(replay[2].iterdir()).read_bytes() == replay[4]
    assert (replay[1].parent / 'imports/original/source.txt').read_bytes() == replay[4]


def test_prepare_once_then_restore_offline_with_all_original_checks(replay, monkeypatch):
    with monkeypatch.context() as preparation:
        preparation.setattr('tools.restore_source_inputs.scrape', lambda *a, **k: pytest.fail('No extraction in preparation'))
        preparation.setattr('tools.restore_source_inputs.version', lambda *a: pytest.fail('No extractor needed in preparation'))
        with httpx.Client(transport=httpx.MockTransport(lambda request: httpx.Response(200, content=replay[4]))) as client:
            result = restore(*replay[:3], client=client, download_only=True)
    assert result['passed'] and result['archives'][0]['status'] == 'verified source bytes'
    assert not (replay[1].parent / 'imports').exists()
    with httpx.Client(transport=httpx.MockTransport(lambda request: pytest.fail('Offline replay used network'))) as client:
        assert restore(*replay[:3], client=client, offline=True)['passed']
    archive = replay[1].parent / 'imports/original'
    assert {p.relative_to(archive): p.read_bytes() for p in archive.rglob('*') if p.is_file()} == {
        p.relative_to(replay[3]): p.read_bytes() for p in replay[3].rglob('*') if p.is_file()}


def test_missing_offline_cache_fails_without_attempting_network(replay):
    with httpx.Client(transport=httpx.MockTransport(lambda request: pytest.fail('Offline replay used network'))) as client:
        with pytest.raises(PraxisError, match='MISSING_CACHED_SOURCE'):
            restore(*replay[:3], client=client, offline=True)
    assert not (replay[1].parent / 'imports').exists()


def test_cache_corruption_is_not_healed_or_downloaded_during_preparation(replay):
    record = json.loads((replay[3] / 'import.json').read_bytes())
    replay[2].mkdir()
    (replay[2] / record['download']['sha256']).write_bytes(b'bad cache')
    with httpx.Client(transport=httpx.MockTransport(lambda request: pytest.fail('Corruption must fail closed'))) as client:
        with pytest.raises(PraxisError, match='SOURCE_HASH_MISMATCH'):
            restore(*replay[:3], client=client, download_only=True)


def test_owned_client_uses_longer_read_timeout_and_retains_transport_policy(replay, monkeypatch):
    original, configurations = httpx.Client, []

    def factory(**kwargs):
        configurations.append(kwargs)
        return original(transport=httpx.MockTransport(lambda request: httpx.Response(200, content=replay[4])), **kwargs)

    monkeypatch.setattr('httpx.Client', factory)
    assert restore(*replay[:3])['passed']
    assert len(configurations) == 1
    settings = configurations[0]
    assert settings['timeout'].read == 60 and settings['timeout'].connect == 15
    assert settings['trust_env'] is False and settings['follow_redirects'] is False


@pytest.mark.parametrize('policy', [{'download_attempts': 0}, {'download_attempts': 6},
                                    {'download_attempts': True}, {'read_timeout': 14}, {'read_timeout': 121}])
def test_unbounded_or_invalid_replay_policies_are_rejected(replay, policy):
    with pytest.raises(PraxisError, match='INVALID_REPLAY_POLICY'):
        restore(*replay[:3], **policy)
