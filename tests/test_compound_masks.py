"""Compound declarations never become an invented contiguous operating field."""
import pytest

from praxis.adapters.discovery import _fields
from praxis.errors import PraxisError


def definitions(mask="_Msk", position="_Pos"):
    values = {"UART_CR1_M": "0x10001000", "UART_CR1_M0": "0x1000",
              "UART_CR1_M1": "0x10000000", "UART_CR1_UE": "1"}
    result = {name + mask: value for name, value in values.items()}
    result.update({"UART_CR1_M" + position: "12", "UART_CR1_M0" + position: "12",
                   "UART_CR1_M1" + position: "28", "UART_CR1_UE" + position: "0"})
    return result


@pytest.mark.parametrize("mask,position", [("_Msk", "_Pos"), ("_MASK", "_SHIFT")])
def test_exact_component_partition_retains_all_bits_and_sources(mask, position):
    values = definitions(mask, position)
    notes = []
    fields, expressions = _fields("UART_CR1", 32, values, "vendor", aggregate=True,
        mask_suffix=mask, position_suffix=position, notes=notes,
        macro_sources={"UART_CR1_M" + mask: "actual_header"})
    assert {f.name: f.mask for f in fields} == {"UE": 1, "M0": 0x1000, "M1": 0x10000000}
    assert set(expressions) == {"UE", "M0", "M1"}
    assert len(notes) == 1 and "0x10001000" in notes[0]
    assert "actual_header:UART_CR1_M" + mask in notes[0]
    assert "vendor:UART_CR1_M0" + mask in notes[0]
    assert "vendor:UART_CR1_M1" + mask in notes[0]


@pytest.mark.parametrize("mutation", ["missing", "overlapping", "outside", "noncontiguous"])
def test_unproven_component_partitions_still_fail(mutation):
    values = definitions()
    if mutation == "missing":
        del values["UART_CR1_M1_Msk"]
    elif mutation == "overlapping":
        values["UART_CR1_M2_Msk"] = "0x1000"
    elif mutation == "outside":
        values["UART_CR1_M2_Msk"] = "2"
    else:
        values["UART_CR1_M0_Msk"] = "0x10001000"
    with pytest.raises(PraxisError, match="UNSUPPORTED_MASK"):
        _fields("UART_CR1", 32, values, "header", aggregate=True, notes=[])


def test_compound_position_conflicts_and_unreviewed_selections_are_not_relaxed():
    values = definitions()
    values["UART_CR1_M_Pos"] = "13"
    with pytest.raises(PraxisError, match="DECLARATION_CONFLICT"):
        _fields("UART_CR1", 32, values, "header", aggregate=True, notes=[])
    values["UART_CR1_M_Pos"] = "12"
    with pytest.raises(PraxisError, match="UNSUPPORTED_MASK"):
        _fields("UART_CR1", 32, values, "header", aggregate=True, selected=["M"], notes=[])
    with pytest.raises(PraxisError, match="UNSUPPORTED_MASK"):
        _fields("UART_CR1", 32, values, "header", aggregate=False, notes=[])
    fields, _ = _fields("UART_CR1", 32, values, "header", selected=["M0", "M1", "UE"])
    assert {field.name for field in fields} == {"M0", "M1", "UE"}
