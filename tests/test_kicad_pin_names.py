"""Format normalization must use endpoint-specific evidence, never suffix guesses."""
import json
from xml.etree import ElementTree as E

import pytest

from conftest import ROOT
from praxis.adapters.kicad import parse_schematic
from praxis.errors import PraxisError
from praxis.models import Profile


@pytest.mark.parametrize("exported,library,passed", [
    ("PA2", "PA2", True), ("PA2_16", "PA2", True),
    ("PA2_17", "PA2", False), ("PA20_16", "PA2", False),
    ("PA2_16_16", "PA2", False), ("PA2_16", "PA2_16", False),
    ("PA2_16", None, False),
])
def test_endpoint_qualified_names_require_exact_library_evidence(tmp_path, exported, library, passed):
    root = ROOT / "sources/stm32f401re"
    profile = Profile.model_validate(json.loads((root / "profile.json").read_text()))
    tree = E.parse(root / "raw/netlist.xml")
    node = tree.find("./nets/net/node[@ref='U1'][@pin='16']")
    node.set("pinfunction", exported)
    if library is not None:
        component = tree.find("./components/comp[@ref='U1']")
        E.SubElement(component, "libsource", lib="Fixture", part="MCU")
        parts = E.SubElement(tree.getroot(), "libparts")
        pins = E.SubElement(E.SubElement(parts, "libpart", lib="Fixture", part="MCU"), "pins")
        E.SubElement(pins, "pin", num="16", name=library)
    path = tmp_path / "export.xml"
    tree.write(path, encoding="utf-8", xml_declaration=True)
    if passed:
        schematic = parse_schematic(path, "netlist", profile.target, profile.pin_map)
        assert next(p.name for n in schematic.nets for p in n.pins if p.endpoint == "U1:16") == "PA2"
    else:
        with pytest.raises(PraxisError, match="PIN_MISMATCH"):
            parse_schematic(path, "netlist", profile.target, profile.pin_map)
