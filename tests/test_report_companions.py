import json
from types import SimpleNamespace

import pytest

from praxis.errors import PraxisError
from praxis.reports import MARKER, partition, read_report


def bundle_for(documents):
    return SimpleNamespace(manifest=SimpleNamespace(documents={path[5:-3]: path for path in documents}),
                           read=documents.__getitem__)


def test_large_report_is_unbroken_and_keeps_complete_editorial_table():
    rows = [f"| field{i} | complete value{i} |" for i in range(1000)]
    table = "| Field | Meaning |\n| --- | --- |\n" + "\n".join(rows) + "\n"
    payload = {"format": "test-report", "data": "x" * 35_000}
    text = "# Coverage\n\n" + table + "\n" + MARKER + json.dumps(payload) + "\n```\n"
    assert len(text.encode()) > 65536
    documents = partition("coverage", text)
    assert documents == {"wiki/coverage.md": text}
    assert table in documents["wiki/coverage.md"]
    assert read_report(bundle_for(documents), "coverage") == payload
    assert partition("coverage", text) == documents


def test_small_reports_keep_their_original_bytes():
    payload = {"format": "praxis-features-v1", "target": "test"}
    text = "# Features\n\n" + MARKER + json.dumps(payload) + "\n```\n"
    docs = partition("features", text)
    assert docs == {"wiki/features.md": text}
    assert read_report(bundle_for(docs), "features") == payload


@pytest.mark.parametrize("destination", ["../outside", "sources", "reports/features"])
def test_report_references_cannot_select_other_documents(destination):
    text = MARKER + json.dumps({"format": "praxis-report-reference-v1", "document": destination}) + "\n```\n"
    with pytest.raises(PraxisError, match="fixed registered companion"):
        read_report(bundle_for({"wiki/coverage.md": text}), "coverage")


def test_nested_and_missing_report_companions_fail():
    text = MARKER + json.dumps({"format": "praxis-report-reference-v1", "document": "reports/coverage"}) + "\n```\n"
    with pytest.raises(PraxisError, match="REPORT_UNAVAILABLE"):
        read_report(bundle_for({"wiki/coverage.md": text}), "coverage")
    with pytest.raises(PraxisError, match="Nested report references"):
        read_report(bundle_for({"wiki/coverage.md": text, "wiki/reports/coverage.md": text}), "coverage")


def test_large_json_report_remains_complete_without_a_companion():
    payload = {"data": "x" * (2 * 1024 * 1024)}
    text = "# Coverage\n" + MARKER + json.dumps(payload) + "\n```\n"
    docs = partition("coverage", text)
    assert docs == {"wiki/coverage.md": text}
    assert read_report(bundle_for(docs), "coverage") == payload


def test_large_declaration_tables_keep_every_field_meaning_and_provenance():
    from conftest import ROOT
    from praxis.models import BitField, Instance, Peripheral, Profile, Register, SourceRef
    from praxis.render import peripheral
    target = Profile.model_validate_json((ROOT / "sources/synthetic-cortex-m3/profile.json").read_bytes()).target
    meaning = "Declaration only; the complete operating meaning requires independently reviewed source evidence."
    registers = [Register(name=f"R{i}", offset=i * 4, width=32, access="unknown", reset=None,
        side_effects="Not asserted", sources=[SourceRef(source="header", locator=f"TYPE.R{i}")],
        fields=[BitField(name=f"F{bit}", lsb=bit, width=1, mask=1 << bit, meaning=meaning,
            sources=[SourceRef(source="header", locator=f"DEMO_R{i}_F{bit}_Msk")]) for bit in range(32)])
        for i in range(15)]
    item = Peripheral(id="demo", title="Demo declarations", prerequisites=[], registers=registers,
        instances=[Instance(name="DEMO", base_address=0x40000000, bus="unknown", clock="unknown",
            sources=[SourceRef(source="header", locator="DEMO_BASE")])], reviewed_markdown="", review=None)
    text = peripheral(target, item, "Operating semantics unavailable.")
    assert len(text.encode()) > 65536
    assert text.count(meaning) == 15 * 32
    for register in registers:
        for field in register.fields:
            assert f"| {register.name} | {field.name} | {field.lsb}:{field.lsb} | 0x{field.mask:X} |" in text
            assert f"header:DEMO_{register.name}_{field.name}_Msk" in text
    assert text == peripheral(target, item, "Operating semantics unavailable.")
