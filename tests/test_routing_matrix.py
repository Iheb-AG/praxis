"""Matrix reconstruction preserves complete evidence and refuses guesses."""

import asyncio
import copy
import json
import os
import sys

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic import ValidationError

from praxis.adapters.matrix import MatrixSpec, prepare
from praxis.bundle import digest
from praxis.definitions import definitions_digest, load_definitions
from praxis.errors import PraxisError
from praxis.models import Profile
from praxis.web_import import WebSource, scrape
import test_ingestion_mcp
from test_web_import import make_pdf
from conftest import ROOT


@pytest.fixture
def matrix_service(tmp_path):
    return test_ingestion_mcp.service.__wrapped__(tmp_path)


@pytest.fixture
def matrix():
    spec = MatrixSpec(
        format="praxis-routing-matrix-v1",
        id="fictional_mux",
        target="SYNTHETIC",
        group="MUX_A",
        evidence_source="fixture",
        source_sha256="a" * 64,
        context_locator="page:1",
        context_contains=["Fictional routing matrix"],
        table_locators=["page:1/table:1", "page:2/table:1"],
        row_axis="Selector",
        column_axis="Lane",
        row_ids=[0, 1],
        column_ids=[4, 5],
        join_suffixes=["_"],
    )
    parts = [
        dict(
            locator=f"page:{i}",
            text="Fictional routing matrix",
            artifact_sha256=str(i) * 64,
            tables=[dict(locator=f"page:{i}/table:1", bbox=[1, 2, 3, 4], rows=rows)],
        )
        for i, rows in enumerate(
            [
                [["Requests", "Lane 4", "Lane 5"], ["Selector 0", "SER_A_TX\nSER_A_RX", "-"]],
                [["Requests", "Lane 4", "Lane 5"], ["Selector 1", "PAD_\nRX", "SER_B_TX"]],
            ],
            1,
        )
    ]
    source = dict(
        id="fixture",
        sha256="a" * 64,
        target="SYNTHETIC",
        import_revision="b" * 64,
        origin="https://example.invalid/fictional.pdf",
    )
    return parts, spec, source


def run(matrix):
    parts, spec, source = matrix
    return prepare(parts, spec, source, "c" * 64)


def test_cross_page_axes_shared_requests_wrap_and_every_source_cell_are_preserved(matrix):
    before = copy.deepcopy(matrix)
    report = run(matrix)
    assert matrix == before and report == run(matrix)
    assert report["complete"] and report["counts"] == dict(
        expected_cells=4, cells=4, candidates=4, unresolved_cells=0
    )
    assert report["review_required"] and not report["publication_ready"]
    assert {(c["row_id"], c["column_id"], c["signal"]) for c in report["candidates"]} == {
        (0, 4, "SER_A_TX"),
        (0, 4, "SER_A_RX"),
        (1, 4, "PAD_RX"),
        (1, 5, "SER_B_TX"),
    }
    assert report["original_tables"][0]["table"] == matrix[0][0]["tables"][0]
    candidate = report["candidates"][0]
    assert candidate["provenance"]["locator"] == "page:1/table:1/row:2/column:2"
    assert candidate["provenance"]["artifact_sha256"] == "1" * 64
    assert candidate["provenance"]["sha256"] == "a" * 64 and candidate["status"] == "unreviewed"
    parts, spec, source = matrix
    assert prepare(list(reversed(parts)), spec, source, "c" * 64) == report


@pytest.mark.parametrize(
    "value", [None, "", "SER_B_TX(1)", "(1)\nSER_B_TX", "A/B", "A\nA", "[[evil]]", "A- B"]
)
def test_qualified_unknown_or_ambiguous_cells_are_gaps_not_guessed_routes(matrix, value):
    matrix[0][1]["tables"][0]["rows"][1][2] = value
    report = run(matrix)
    assert not report["complete"] and report["counts"]["unresolved_cells"] == 1
    assert not any(c["row_id"] == 1 and c["column_id"] == 5 for c in report["candidates"])
    assert report["gaps"][0]["raw"] == value
    assert report["original_tables"][1]["table"]["rows"][1][2] == value


def test_wrap_repair_requires_an_explicit_literal_rule(matrix):
    parts, spec, source = matrix
    spec = spec.model_copy(update={"join_suffixes": []})
    report = prepare(parts, spec, source, "c" * 64)
    assert not report["complete"] and report["counts"]["unresolved_cells"] == 1
    assert not any(c["signal"] in {"PAD_", "RX", "PAD_RX"} for c in report["candidates"])


@pytest.mark.parametrize(
    "change",
    ["short_row", "wrong_axis", "duplicate_column", "wrong_column", "duplicate_row", "empty_table"],
)
def test_broken_axes_widths_and_duplicate_cells_cannot_claim_complete(matrix, change):
    rows = matrix[0][1]["tables"][0]["rows"]
    if change == "short_row":
        rows[1].pop()
    elif change == "wrong_axis":
        rows[1][0] = "Different 1"
    elif change == "duplicate_column":
        rows[0][2] = rows[0][1]
    elif change == "wrong_column":
        rows[0][2] = "Lane 9"
    elif change == "duplicate_row":
        rows.append(copy.deepcopy(rows[1]))
    else:
        matrix[0][1]["tables"][0]["rows"] = []
    report = run(matrix)
    assert not report["complete"] and report["gaps"] and not report["publication_ready"]
    if change == "duplicate_row":
        assert not any(c["row_id"] == 1 for c in report["candidates"])


@pytest.mark.parametrize("key,value", [("sha256", "f" * 64), ("target", "OTHER"), ("id", "other")])
def test_policy_cannot_bind_a_different_source_or_target(matrix, key, value):
    matrix[2][key] = value
    with pytest.raises(PraxisError, match="SOURCE_HASH_MISMATCH"):
        run(matrix)


def test_missing_duplicate_or_wrong_context_evidence_fails_before_extracting(matrix):
    parts, spec, source = matrix
    with pytest.raises(PraxisError, match="UNKNOWN_LOCATOR"):
        prepare(parts[:1], spec, source, "c" * 64)
    with pytest.raises(PraxisError, match="DUPLICATE_SOURCE"):
        prepare([*parts, parts[0]], spec, source, "c" * 64)
    parts[0]["text"] = "Some unrelated matrix"
    with pytest.raises(PraxisError, match="MATRIX_CONTEXT"):
        run(matrix)


@pytest.mark.parametrize(
    "change",
    [
        {"table_locators": ["../file"]},
        {"table_locators": ["page:1/table:1"] * 2},
        {"row_ids": [0, 0]},
        {"row_ids": [True]},
        {"column_ids": ["4"]},
        {"column_ids": [-1]},
        {"context_contains": [""]},
        {"join_suffixes": [""]},
    ],
)
def test_invalid_versioned_policy_is_rejected(matrix, change):
    with pytest.raises(ValidationError):
        MatrixSpec.model_validate({**matrix[1].model_dump(), **change})


def test_review_packet_is_bounded_without_silent_truncation(matrix, monkeypatch):
    monkeypatch.setattr("praxis.adapters.matrix.MAX_PACKET", 10)
    with pytest.raises(PraxisError, match="REVIEW_LIMIT"):
        run(matrix)


def test_f407_rules_are_pinned_data_and_do_not_approve_a_new_operating_workflow():
    root = ROOT / "sources/stm32f407g-disc1"
    prior = Profile.model_validate_json((root / "profile-timer-irq-v1.json").read_bytes())
    current = Profile.model_validate_json((root / "profile-routing-review-v1.json").read_bytes())
    assert current.target == prior.target and current.workflows == prior.workflows
    assert current.publication_requires == prior.publication_requires
    source = next(s for s in current.sources if s.id == "dma1_routing_spec")
    body = (root / source.path).read_bytes()
    assert source.authority == "configuration" and source.expected_sha256 == digest(body)
    spec = MatrixSpec.model_validate_json(body)
    assert spec.table_locators == ["page:309/table:2", "page:310/table:1"]
    assert spec.row_ids == spec.column_ids == list(range(8))
    assert spec.target == current.target.mcu

    def definitions(profile):
        return load_definitions(profile, {s.id: root / s.path for s in profile.sources})

    assert definitions_digest(definitions(prior)) == definitions_digest(definitions(current))


async def test_actual_ingestion_mcp_uses_registered_rules_and_never_publishes(
    matrix_service, tmp_path
):
    service = matrix_service
    drawing = tmp_path / "matrix.pdf"
    make_pdf(drawing)
    drawing.write_bytes(
        drawing.read_bytes()
        .replace(b"Register", b"Request ")
        .replace(b"Offset", b"Lane 4")
        .replace(b"CR1", b"R 0")
        .replace(b"0x0C", b"TX_A")
    )
    source = WebSource(
        id="matrix_pdf",
        target=service.profile.target.mcu,
        kind="pdf",
        url="https://example.invalid/matrix.pdf",
    )
    archive = scrape(source, service.archive_root / "matrix_pdf", from_file=drawing)
    spec = MatrixSpec(
        format="praxis-routing-matrix-v1",
        id="test_routes",
        target=source.target,
        group="SYNTHETIC",
        evidence_source=source.id,
        source_sha256=digest(drawing.read_bytes()),
        table_locators=["page:1/table:1"],
        context_locator="page:1",
        context_contains=["Clocks must be enabled"],
        row_axis="R",
        column_axis="Lane",
        row_ids=[0],
        column_ids=[4],
    )
    policy = service.root / "matrix.json"
    policy.write_text(spec.model_dump_json())
    profile = json.loads(service.profile_path.read_bytes())
    profile["sources"].append(
        dict(
            id="matrix_rules",
            path=policy.name,
            authority="configuration",
            origin="synthetic test configuration",
            license="MIT",
            version="1",
            expected_sha256=digest(policy.read_bytes()),
        )
    )
    service.profile_path.write_text(json.dumps(profile))
    args = [
        "-m",
        "praxis",
        "ingest-serve",
        "--profile",
        str(service.profile_path),
        "--catalog",
        str(tmp_path / "catalog.json"),
        "--archive-root",
        str(service.archive_root),
        "--publication-root",
        str(service.publication_root),
        "--evidence-archive",
        str(archive),
    ]
    params = StdioServerParameters(
        command=sys.executable, args=args, cwd=str(tmp_path), env=dict(os.environ)
    )

    async def exercise():
        async with (
            stdio_client(params) as (reader, writer),
            ClientSession(reader, writer) as client,
        ):
            await client.initialize()
            tools = {t.name: t for t in (await client.list_tools()).tools}
            assert tools["prepare_routing_matrix"].annotations.readOnlyHint
            for name in ["unknown", "../matrix.json", "header"]:
                reply = await client.call_tool(
                    "prepare_routing_matrix", {"specification_source": name}
                )
                assert reply.isError and "UNKNOWN_SOURCE" in reply.content[0].text
            reply = await client.call_tool(
                "prepare_routing_matrix", {"specification_source": "matrix_rules"}
            )
            assert not reply.isError
            value = reply.structuredContent or json.loads(reply.content[0].text)
            report = value.get("result", value)
            assert report["complete"] and report["candidates"][0]["signal"] == "TX_A"
            assert report["review_required"] and not report["publication_ready"]
            assert report["policy_sha256"] == digest(policy.read_bytes())

    await asyncio.wait_for(exercise(), 30)
    assert not service.publication_root.exists()
