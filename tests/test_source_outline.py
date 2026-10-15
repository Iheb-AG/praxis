import copy

import pytest

from praxis.adapters.outline import prepare, validate_packet
from praxis.errors import PraxisError


SOURCE = dict(id="manual", target="TEST-MCU", sha256="a" * 64,
              import_revision="b" * 64, origin="https://example.org/manual.pdf")


def part(page, text):
    return dict(locator=f"page:{page}", page=page, text=text, artifact_sha256="c" * 64)


def pages():
    return [part(1, "Manual title"), part(2, "Contents\n1 Memory . . . 10\n"
                "1.1 Program and erase\noperations . . . 11\n1.2 Power . . . 13\n2/30"),
            part(3, "Contents\n2 Communication . . . 16\nA Appendix . . . 20\n3/30"),
            part(4, "List of tables\nTable 1. One . . . 12")]


def test_deterministic_complete_line_accounting_and_multiline_titles():
    parts = pages()
    result = prepare(parts, source=SOURCE)
    assert prepare(list(reversed(parts)), source=SOURCE) == result
    assert validate_packet(result) is result
    assert result["contents_boundaries_observed"]
    assert result["counts"]["entries"] == 5 and not result["unresolved"]
    assert result["entries"][1]["title"] == "Program and erase operations"
    assert result["entries"][1]["locators"] == ["page:2/line:3", "page:2/line:4"]
    assert len(result["line_accounting"]) == sum(bool(line.strip()) for p in parts for line in p["text"].splitlines())
    assert all(row["disposition"] in {"entry", "page_metadata", "outside_contents"} for row in result["line_accounting"])
    assert all(row["applicability"] == "unreviewed" and row["operating_knowledge"] == "not_established"
               for row in result["entries"])
    assert result["publication_ready"] is False


def test_missing_pages_never_join_unrelated_heading_fragments():
    result = prepare([part(2, "Contents\n1 Memory . . . 10\n1.1 Pending title"),
                      part(4, "Contents\ncontinuation . . . 20\n2 Timers . . . 30")], source=SOURCE)
    assert not result["contents_boundaries_observed"]
    assert [row["section"] for row in result["entries"]] == ["1", "1.1", "2"]
    assert result["entries"][1]["destination_page"] is None
    assert result["entries"][1]["extraction_flags"] == ["noncontiguous_evidence_pages"]
    assert {row["reason"] for row in result["unresolved"]} == {"noncontiguous_evidence_pages", "unrecognized_contents_line"}


def test_unsupported_and_unlabelled_lines_are_explicit_gaps():
    result = prepare([part(1, "Title"), part(2, "Contents\n1 Known . . . 4\n"
                    "2 Unsupported layout\n3 Known again . . . 5\nodd leader -> 6\n39"),
                    part(3, "List of figures")], source=SOURCE)
    assert len(result["unresolved"]) == 3
    assert sum(row["disposition"] == "unresolved" for row in result["line_accounting"]) == 3


@pytest.mark.parametrize("mutation,code", [("duplicate_section", "DUPLICATE_SECTION"),
    ("duplicate_locator", "UNKNOWN_LOCATOR"), ("duplicate_page", "IMPORT_INTEGRITY"),
    ("no_contents", "UNSUPPORTED_OUTLINE"), ("wrong_format", "UNSUPPORTED_OUTLINE")])
def test_ambiguous_or_unsupported_inputs_fail_explicitly(mutation, code):
    parts = pages()
    if mutation == "duplicate_section":
        parts[1]["text"] += "\n1 Conflicting title . . . 50"
    elif mutation == "duplicate_locator":
        parts.append(parts[1])
    elif mutation == "duplicate_page":
        parts.append({**parts[1], "locator": "other"})
    elif mutation == "wrong_format":
        parts[1].pop("page")
    else:
        parts = [part(1, "1 Memory . . . 10")]
    with pytest.raises(PraxisError, match=code):
        prepare(parts, source=SOURCE)


@pytest.mark.parametrize("mutation", ["title", "origin", "target", "hash"])
def test_packet_integrity_covers_metadata_titles_and_provenance(mutation):
    report = copy.deepcopy(prepare(pages(), source=SOURCE))
    if mutation == "title":
        report["entries"][0]["title"] = "Altered"
    elif mutation == "hash":
        report["evidence_parts"][0]["artifact_sha256"] = "d" * 64
    else:
        report["source"][mutation] = "Altered"
    with pytest.raises(PraxisError, match="INVENTORY_INTEGRITY"):
        validate_packet(report)


def test_configured_table_index_preserves_raw_revision_values_without_interpretation():
    selected = [part(1, "Title"), {**part(2, "Index source text"), "tables": [
        {"locator": "page:2/table:1", "rows": [["Group", "Section", "Issue", "Rev A", "Rev B"],
             ["Timer", "2.1", "Flag may persist", "A", "N"],
             [None, "2.2", "Recovery needs review", "P", "A"]]}]}, part(3, "Section bodies")]
    report = prepare(selected, source=SOURCE, table_columns={"section": "Section", "title": "Issue"})
    assert report["counts"]["entries"] == 2 and not report["unresolved"]
    assert report["contents_boundaries_observed"]
    assert report["entries"][0]["table_values"]["Rev A"] == "A"
    assert report["entries"][1]["table_values"]["Group"] == ""
    assert report["entries"][0]["destination_page"] is None
    assert len(report["table_accounting"]) == 3
    assert validate_packet(report) is report


@pytest.mark.parametrize("rows,code", [
    ([["Section", "Section", "Issue"], ["1", "1", "x"]], "AMBIGUOUS_OUTLINE"),
    ([["Section", "Issue"], ["1", "x"], ["1", "y"]], "DUPLICATE_SECTION"),
    ([["Other", "Unknown"], ["1", "x"]], "UNSUPPORTED_OUTLINE"),
])
def test_invalid_table_index_fails_instead_of_dropping_rows(rows, code):
    selected = [{**part(1, "Text"), "tables": [{"locator": "page:1/table:1", "rows": rows}]}]
    with pytest.raises(PraxisError, match=code):
        prepare(selected, source=SOURCE, table_columns={"section": "Section", "title": "Issue"})


def test_malformed_table_rows_remain_gaps():
    selected = [{**part(1, "Text"), "tables": [{"locator": "page:1/table:1", "rows": [
        ["Section", "Issue"], ["1", "Known"], ["2"], ["?", "Unknown"]]}]}]
    report = prepare(selected, source=SOURCE, table_columns={"section": "Section", "title": "Issue"})
    assert len(report["unresolved"]) == 2 and not report["contents_boundaries_observed"]
    assert len(report["table_accounting"]) == 4


def test_long_titles_short_leaders_appendices_and_separate_page_numbers():
    selected = [part(1, "Title"), part(2, "Contents\n1 Long title    10\n1.1 Short leader . 11\n"
        "1.2 Wrapped destination . . .\n12\nAppendix A Diagrams . . . 20"), part(3, "List of tables")]
    report = prepare(selected, source=SOURCE)
    assert not report["unresolved"]
    assert [r["destination_page"] for r in report["entries"]] == [10, 11, 12, 20]
    assert [r["title"] for r in report["entries"]] == ["Long title", "Short leader", "Wrapped destination", "Diagrams"]
