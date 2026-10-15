"""Source registry normalization must reconstruct exact paths and full metadata."""

import html

from praxis.models import Source
from praxis.render import source_catalog, source_documents


def source(identity, **changes):
    return Source(id=identity, path=f"parts/{identity}.json", sha256="a" * 64,
        authority="semantics", version="exact-import-hash", license="Vendor terms",
        origin="https://example.invalid/manual.pdf", **changes)


def test_shared_metadata_preserves_every_artifact_and_complete_origin():
    sources = [source("page_a"), source("page_b")]
    document = source_catalog(sources)
    assert document.count("https://example.invalid/manual.pdf") == 1
    assert document.count("| metadata_001 | semantics |") == 1
    for item in sources:
        assert f"| {item.id} | prefix_001 | {item.id}.json | {item.sha256} | metadata_001 |" in document
    assert '| prefix_001 | parts/ |' in document
    assert source_catalog(list(reversed(sources))) == document


def test_metadata_differences_are_never_conflated_and_cells_are_escaped():
    a = source("one")
    b = a.model_copy(update={"id": "two", "license": "Different | terms\nretained"})
    document = source_catalog([a, b])
    assert document.count("https://example.invalid/manual.pdf") == 2
    assert "Different &#124; terms<br>retained" in document
    assert "metadata_001" in document and "metadata_002" in document


def test_paths_round_trip_without_conflating_roots_nested_names_or_shared_basenames():
    paths = ['profile.json', './profile.json', 'one/part.json', 'two/part.json',
             'nested/long/path/part-0001.json', 'nested/long/path/part-0002.json',
             'escaped/&folder/part.json', 'literal//part.json']
    sources = [source(f'item_{i}').model_copy(update={'path': path}) for i, path in enumerate(paths)]
    document = source_catalog(sources)
    artifact_text, other = document.split('## Shared path prefixes\n\n')
    prefix_text, _ = other.split('## Shared source metadata')
    def rows(text):
        lines = [line for line in text.splitlines() if line.startswith('|')][2:]
        return [[html.unescape(c.strip()) for c in line.strip('|').split('|')] for line in lines]
    prefixes = {key: '' if value == '—' else value for key, value in rows(prefix_text)}
    reconstructed = {row[0]: (prefixes[row[1]] + row[2], row[3], row[4]) for row in rows(artifact_text)}
    assert reconstructed == {s.id: (s.path, s.sha256, 'metadata_001') for s in sources}
    assert source_catalog(list(reversed(sources))) == document


def test_long_repeated_directories_leave_room_for_more_reviewed_sources():
    directory = 'imports/board-scenario/exact-reviewed-manual-pages/extracted/'
    sources = [source(f'page_{i}').model_copy(update={'path': directory + f'part-{i:04}.json'}) for i in range(300)]
    document = source_catalog(sources)
    assert document.count(directory) == 1
    assert len(document.encode()) < 65536
    assert all(s.id in document and s.sha256 in document for s in sources)


def test_large_registry_keeps_every_complete_table_and_metadata_value(bundle):
    sources = [source(f"item_{i:03}").model_copy(update={
        "origin": f"https://example.invalid/{i:03}/" + "long-exact-origin-" * 27})
        for i in range(100)]
    documents = source_documents(bundle.manifest.target, sources, bundle.manifest.review)
    assert set(documents) == {"wiki/sources.md"}
    assert len(documents["wiki/sources.md"].encode()) > 65536
    assert source_documents(bundle.manifest.target, list(reversed(sources)), bundle.manifest.review) == documents
    artifact_text = documents["wiki/sources.md"]
    metadata_text = documents["wiki/sources.md"]
    for item in sources:
        assert artifact_text.count(f"| {item.id} |") == 1
        assert item.sha256 in artifact_text
        assert metadata_text.count(item.origin) == 1
    assert "## Shared source metadata" in artifact_text
    assert "## Shared path prefixes" in artifact_text
    assert "| Metadata | Authority | Version | License | Origin |" in metadata_text


def test_large_single_metadata_table_is_published_without_truncation(bundle):
    item = source("oversized").model_copy(update={"origin": "X" * 65536})
    docs = source_documents(bundle.manifest.target, [item], bundle.manifest.review)
    assert item.origin in docs["wiki/sources.md"]
    assert item.sha256 in docs["wiki/sources.md"]
