"""Offline CLI orchestration for the same manual review adapter used by MCP."""

from pathlib import Path

from praxis.adapters.manual import prepare
from praxis.bundle import digest, read_inside
from praxis.coverage import inventory
from praxis.errors import PraxisError
from praxis.jsonio import load_json
from praxis.models import ManualSpec, Profile
from praxis.web_import import MAX_PAGE, validate_import


def prepare_review(profile_path: Path, archive_path: Path, entity: str, registers=None, locators=None):
    profile_path = profile_path.resolve(strict=True)
    root = profile_path.parent
    raw = read_inside(root, profile_path.name, 1024 * 1024)
    profile = Profile.model_validate(load_json(raw))
    if profile.discovery is None:
        raise PraxisError('INVALID_PROFILE', 'Review preparation requires configurable header discovery')
    paths, hashes = {}, {}
    for source in profile.sources:
        if source.id in paths:
            raise PraxisError('DUPLICATE_SOURCE', 'Source identities must be unique')
        hashes[source.id] = digest(read_inside(root, source.path, 8 * 1024 * 1024))
        paths[source.id] = root / source.path
    if profile.definitions not in paths:
        raise PraxisError('UNKNOWN_SOURCE', 'Profile definitions must name a registered source')
    from praxis.definitions import load_definitions
    reviewed = load_definitions(profile, paths)
    catalog, entries = inventory(profile, paths, reviewed, root)
    if entity not in catalog:
        raise PraxisError('UNKNOWN_PERIPHERAL', 'Select an extractable canonical peripheral identity')
    record = validate_import(archive_path)
    if record['source']['target'] != profile.target.mcu:
        raise PraxisError('TARGET_MISMATCH', 'Manual evidence must target the exact selected MCU')
    parts = []
    for name, expected in sorted(record['file_hashes'].items()):
        if not name.startswith('extracted/') or not name.endswith('.json'):
            continue
        data = read_inside(archive_path, name, MAX_PAGE)
        if digest(data) != expected:
            raise PraxisError('IMPORT_INTEGRITY', 'Manual evidence changed during preparation')
        parts.append(dict(**load_json(data), artifact=name, artifact_sha256=expected))
    for source in profile.sources:
        if digest(read_inside(root, source.path, 8 * 1024 * 1024)) != hashes[source.id]:
            raise PraxisError('SOURCE_CHANGED', 'Source changed during header discovery; retry against a fixed snapshot')
    if digest(read_inside(root, profile_path.name, 1024 * 1024)) != digest(raw):
        raise PraxisError('SOURCE_CHANGED', 'Profile changed during preparation')
    source_id = record['source']['id']
    return prepare(catalog[entity], parts, entity=entity, target=profile.target.model_dump(),
        source=dict(id=source_id, source_sha256=record['download']['sha256'],
            import_revision=record['import_revision'], origin=record['download']['final_url'],
            profile_sha256=digest(raw), declaration_sources=dict(sorted(hashes.items())),
            declaration_status=entries[entity]['status']),
        spec=profile.manuals.get(source_id, ManualSpec()),
        discovery=profile.discovery.peripherals.get(entity), registers=registers, locators=locators)
