from __future__ import annotations

from pathlib import Path
import re
from tempfile import TemporaryDirectory

from praxis.errors import PraxisError
from praxis.models import Component, Net, Pin, Schematic, SourceRef, Target
from praxis.process import run


def export(schematic: Path, destination: Path) -> None:
    run(["kicad-cli", "sch", "export", "netlist", "--format", "kicadxml",
         "--output", str(destination), str(schematic)])


def parse_schematic(path: Path, source_id: str, target: Target, pin_map: dict[str, str]) -> Schematic:
    try:
        from defusedxml import ElementTree
        from defusedxml.common import DefusedXmlException
    except ImportError as exc:
        raise PraxisError("MISSING_TOOL", "Install project-praxis[ingest] for safe XML parsing") from exc
    try:
        tree = ElementTree.parse(path, forbid_dtd=True, forbid_entities=True, forbid_external=True)
    except (ElementTree.ParseError, DefusedXmlException, ValueError) as exc:
        raise PraxisError("INVALID_NETLIST", f"Invalid XML: {path.name}: {exc}") from exc
    if tree.getroot().tag != "export":
        raise PraxisError("INVALID_NETLIST", "Expected a KiCad XML export root")
    library_pins = {}
    for part in tree.findall("./libparts/libpart"):
        key = (part.get("lib", ""), part.get("part", ""))
        pins = part.findall("./pins/pin")
        numbers = [pin.get("num", "") for pin in pins]
        if key in library_pins or len(numbers) != len(set(numbers)) or any(not n for n in numbers):
            raise PraxisError("INVALID_NETLIST", "Duplicate library identity or pin number")
        library_pins[key] = {pin.get("num"): pin.get("name", pin.get("num")) for pin in pins}
    components = {}
    for component in tree.findall("./components/comp"):
        ref = component.get("ref", "")
        if not ref or ref in components:
            raise PraxisError("INVALID_NETLIST", f"Missing or duplicated component reference: {ref}")
        sheet = component.find("sheetpath")
        components[ref] = {
            "package": component.findtext("footprint", ""),
            "sheet": sheet.get("names", "/") if sheet is not None else "/",
            "value": component.findtext("value", ""),
            "pins": {},
            "properties": {field.get("name", ""): field.text or ""
                           for field in component.findall("./fields/field")},
            "fitted": not any(prop.get("name") == "dnp" for prop in component.findall("property")),
        }
        for prop in component.findall("property"):
            components[ref]["properties"][prop.get("name", "")] = prop.get("value", "")
        library = component.find("libsource")
        if library is not None:
            components[ref]["properties"].update({"library": library.get("lib", ""),
                                                  "part": library.get("part", "")})
            components[ref]["pins"].update(library_pins.get(
                (library.get("lib", ""), library.get("part", "")), {}))
    mcu = components.get(target.primary_mcu_ref)
    if not mcu or mcu["package"] != target.package or mcu["value"] != target.mcu:
        raise PraxisError("PACKAGE_MISMATCH", "MCU value/package disagrees with target profile")
    nets = []
    names, endpoints = set(), set()
    for element in tree.findall("./nets/net"):
        name = element.get("name", "")
        if not name or name in names:
            raise PraxisError("INVALID_NETLIST", f"Missing or duplicate net name: {name}")
        names.add(name)
        pins = []
        source = SourceRef(source=source_id, locator=f"net:{name}")
        for node in element.findall("node"):
            ref, number = node.get("ref", ""), node.get("pin", "")
            if ref not in components or not number or (ref, number) in endpoints:
                raise PraxisError("INVALID_NETLIST", f"Unknown or duplicated endpoint {ref}:{number}")
            endpoints.add((ref, number))
            library_name = components[ref]["pins"].get(number)
            pin_name = node.get("pinfunction") or library_name or number
            # KiCad 10 exports shown-name + '_' + pad-number. Only decode an
            # exact match backed by the library record for this same endpoint;
            # never strip arbitrary suffixes or infer MCU pins from a profile.
            # https://docs.kicad.org/doxygen/netlist__exporter__xml_8cpp_source.html
            if library_name and pin_name == f"{library_name}_{number}":
                pin_name = library_name
            if ref == target.primary_mcu_ref:
                expected = pin_map.get(number)
                if not expected or pin_name != expected:
                    raise PraxisError("PIN_MISMATCH", f"{ref}:{number}: expected {expected}, got {pin_name}")
            component = components[ref]
            if number in component["pins"] and component["pins"][number] != pin_name:
                raise PraxisError("PIN_MISMATCH", f"Net and library pin names disagree: {ref}:{number}")
            component["pins"][number] = pin_name or number
            pins.append(Pin(ref=ref, number=number, name=pin_name or number,
                            sheet=component["sheet"], package=component["package"], sources=[source]))
        if not pins:
            raise PraxisError("INVALID_NETLIST", f"Net {name} has no endpoints")
        nets.append(Net(name=name, pins=sorted(pins, key=lambda p: p.endpoint), sources=[source]))
    if not nets:
        raise PraxisError("INVALID_NETLIST", "No nets found")
    records = []
    for ref, component in sorted(components.items()):
        part = component["properties"].get("part", "")
        kind = "mcu" if ref == target.primary_mcu_ref else {
            "R": "resistor", "LED": "led", "SW_Push": "switch",
            "SolderJumper_2_Bridged": "bridge"}.get(part, "other")
        if part == "SW_Push":
            component["properties"]["contact"] = "normally-open"
        records.append(Component(ref=ref, value=component["value"] or "Unspecified",
            package=component["package"], sheet=component["sheet"], kind=kind,
            fitted=component["fitted"],
            pins=dict(sorted(component["pins"].items())), properties=component["properties"],
            sources=[SourceRef(source=source_id, locator=f"component:{ref}")]))
    return Schematic(components=records, nets=sorted(nets, key=lambda n: n.name))


def parse(path: Path, source_id: str, target: Target, pin_map: dict[str, str]) -> list[Net]:
    return parse_schematic(path, source_id, target, pin_map).nets


def audit_hierarchy(path: Path, registered_sources: list[Path]) -> None:
    """Hash-register every sheet before KiCad reads it; reject untracked hierarchy."""
    registered = {p.resolve(strict=True) for p in registered_sources}
    visited = set()

    def visit(sheet):
        sheet = sheet.resolve(strict=True)
        if sheet not in registered:
            raise PraxisError("UNREGISTERED_DEPENDENCY", f"Register KiCad sheet: {sheet.name}")
        if sheet in visited:
            raise PraxisError("SCHEMATIC_CYCLE", "Recursive KiCad sheet hierarchy")
        visited.add(sheet)
        data = sheet.read_bytes()
        if len(data) > 8 * 1024 * 1024:
            raise PraxisError("DOCUMENT_TOO_LARGE", "KiCad sheet exceeds 8 MiB")
        for name in re.findall(r'\(property\s+"Sheetfile"\s+"([^"\n]+)"', data.decode("utf-8")):
            if "\\" in name or Path(name).is_absolute():
                raise PraxisError("INVALID_PATH", "KiCad subsheets must use literal relative paths")
            visit(sheet.parent / name)
        visited.remove(sheet)

    visit(path)


def import_schematic(path: Path, source_id: str, target: Target, pin_map: dict[str, str],
                     registered_sources: list[Path]) -> Schematic:
    audit_hierarchy(path, registered_sources)
    with TemporaryDirectory(prefix="praxis-kicad-") as temporary:
        destination = Path(temporary) / "netlist.xml"
        export(path, destination)
        return parse_schematic(destination, source_id, target, pin_map)


def schematic_nets(path: Path, source_id: str, target: Target, pin_map: dict[str, str]) -> list[Net]:
    with TemporaryDirectory(prefix="praxis-kicad-") as temporary:
        destination = Path(temporary) / "netlist.xml"
        export(path, destination)
        return parse(destination, source_id, target, pin_map)

