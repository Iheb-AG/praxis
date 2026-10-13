"""Modular operating records retain target binding and explicit conflict handling."""

import json

import pytest

from conftest import ROOT
from praxis.bundle import digest
from praxis.definitions import definitions_digest, load_definitions
from praxis.errors import PraxisError
from praxis.models import Peripheral, Profile, SourceSpec


def peripheral(name):
    return Peripheral.model_validate({"id": name, "title": "Synthetic fixture", "instances": [
        {"name": name.upper(), "base_address": 0, "bus": "synthetic", "clock": "synthetic",
         "sources": [{"source": "header", "locator": "fixture"}]}], "registers": [
        {"name": "CR", "offset": 0, "width": 32, "access": "RW", "side_effects": "Synthetic only",
         "sources": [{"source": "header", "locator": "fixture"}]}],
        "reviewed_markdown": "fixture.md", "review": {"status": "reviewed",
            "reviewer": "Fixture author", "basis": "Synthetic validator test; no hardware claim"}})


@pytest.fixture
def context(tmp_path):
    profile = Profile.model_validate_json((ROOT / "sources/stm32f407g-disc1/profile-clock-v1.json").read_bytes())
    base = tmp_path / "base.json"
    base.write_text(json.dumps([peripheral("test").model_dump()]))
    paths = {"definitions": base}
    return profile, paths


def extend(context, tmp_path, name="extension", mutate=lambda d: None):
    profile, paths = context
    data = {"schema_version": 1, "base_sha256": digest(paths["definitions"].read_bytes()),
            "applicable_mcus": [profile.target.mcu], "additions": [peripheral("added").model_dump()]}
    mutate(data)
    path = tmp_path / (name + ".json")
    path.write_text(json.dumps(data))
    source = SourceSpec(id=name, path=path.name, authority="semantics", version="synthetic-v1",
                        license="MIT", origin="Synthetic test")
    profile = profile.model_copy(update={"definition_extensions": [*profile.definition_extensions, name],
                                         "sources": [*profile.sources, source]})
    paths[name] = path
    return profile, paths


def test_additions_and_explicit_replacements_leave_base_bytes_unchanged(context, tmp_path):
    before = context[1]["definitions"].read_bytes()
    replacement = peripheral("test").model_copy(update={"title": "Scoped reviewed replacement"}).model_dump()
    profile, paths = extend(context, tmp_path, mutate=lambda d: d.update(replacements=[replacement]))
    items = load_definitions(profile, paths)
    assert [item.id for item in items] == ["added", "test"]
    assert items[1].title == "Scoped reviewed replacement"
    assert paths["definitions"].read_bytes() == before


@pytest.mark.parametrize("change,code", [
    (lambda d: d.update(base_sha256="0" * 64), "STALE_DEFINITION_EXTENSION"),
    (lambda d: d.update(applicable_mcus=["another_mcu"]), "TARGET_MISMATCH"),
    (lambda d: d.update(additions=[peripheral("test").model_dump()]), "DEFINITION_CONFLICT"),
    (lambda d: d.update(additions=[], replacements=[peripheral("missing").model_dump()]), "DEFINITION_CONFLICT"),
    (lambda d: d["additions"].append(d["additions"][0]), "INVALID_DEFINITIONS"),
    (lambda d: d.update(additions=[]), "INVALID_DEFINITIONS"),
])
def test_extensions_cannot_silently_change_scope_or_overwrite_records(context, tmp_path, change, code):
    with pytest.raises(PraxisError, match=code):
        load_definitions(*extend(context, tmp_path, mutate=change))


def test_multiple_extensions_cannot_last_value_win(context, tmp_path):
    profile, paths = extend(context, tmp_path, "first")
    profile, paths = extend((profile, paths), tmp_path, "second")
    with pytest.raises(PraxisError, match="DEFINITION_CONFLICT"):
        load_definitions(profile, paths)


def test_base_byte_change_requires_an_actual_new_review(context, tmp_path):
    profile, paths = extend(context, tmp_path)
    paths["definitions"].write_bytes(paths["definitions"].read_bytes() + b"\n")
    with pytest.raises(PraxisError, match="STALE_DEFINITION_EXTENSION"):
        load_definitions(profile, paths)


def test_extensions_require_registered_semantics_authority(context, tmp_path):
    profile, paths = extend(context, tmp_path)
    wrong = [s.model_copy(update={"authority": "declarations"}) if s.id == "extension" else s
             for s in profile.sources]
    with pytest.raises(PraxisError, match="SOURCE_AUTHORITY"):
        load_definitions(profile.model_copy(update={"sources": wrong}), paths)
    del paths["extension"]
    with pytest.raises(PraxisError, match="UNKNOWN_SOURCE"):
        load_definitions(profile, paths)


def test_original_profile_still_loads_without_extensions(context):
    profile, paths = context
    assert [item.id for item in load_definitions(profile, paths)] == ["test"]


def test_reviewed_parent_binding_allows_explicit_successive_amendment(context, tmp_path):
    first = extend(context, tmp_path, "first")
    parent = definitions_digest(load_definitions(*first))
    changed = peripheral("added").model_copy(update={"title": "Second reviewed scope"}).model_dump()
    second = extend(first, tmp_path, "second", lambda d: d.update(
        parent_definitions_sha256=parent, additions=[], replacements=[changed]))
    assert load_definitions(*second)[0].title == "Second reviewed scope"
    assert load_definitions(*first)[0].title == "Synthetic fixture"


@pytest.mark.parametrize("mutation", ["parent", "order", "earlier_content"])
def test_parent_binding_rejects_stale_state_or_reordered_extensions(context, tmp_path, mutation):
    first = extend(context, tmp_path, "first")
    parent = definitions_digest(load_definitions(*first))
    second = extend(first, tmp_path, "second", lambda d: d.update(
        parent_definitions_sha256=parent, additions=[], replacements=[peripheral("added").model_dump()]))
    profile, paths = second
    if mutation == "order":
        profile = profile.model_copy(update={"definition_extensions": ["second", "first"]})
    else:
        path = paths["second" if mutation == "parent" else "first"]
        data = json.loads(path.read_bytes())
        if mutation == "parent":
            data["parent_definitions_sha256"] = "0" * 64
        else:
            data["additions"][0]["title"] = "Changed preceding review"
        path.write_text(json.dumps(data))
    with pytest.raises(PraxisError, match="STALE_DEFINITION_EXTENSION"):
        load_definitions(profile, paths)


def test_composed_digest_is_order_independent_and_covers_semantics():
    a, b = peripheral("one"), peripheral("two")
    assert definitions_digest([a, b]) == definitions_digest([b, a])
    changed = b.model_copy(update={"reviewed_markdown": "another-review.md"})
    assert definitions_digest([a, b]) != definitions_digest([a, changed])


def test_parent_binding_does_not_allow_duplicate_additions(context, tmp_path):
    first = extend(context, tmp_path, "first")
    second = extend(first, tmp_path, "second", lambda d: d.update(
        parent_definitions_sha256=definitions_digest(load_definitions(*first))))
    with pytest.raises(PraxisError, match="DEFINITION_CONFLICT"):
        load_definitions(*second)
