"""Native union storage layouts preserve every scalar view without inventing bus semantics."""
import subprocess

import pytest

from conftest import require_tool
from praxis.adapters.discovery import parse_cmsis_headers
from praxis.adapters.headers import cmsis
from praxis.errors import PraxisError
from praxis.models import Register, SourceRef


HEADER = """typedef struct {
    unsigned int CTRL;
    union { volatile unsigned char byte; volatile unsigned short half;
            volatile unsigned int word; } DATA[2];
    unsigned int STATUS;
} UnionBlock_Type;
#define BLOCK_BASE 0x40000000UL
#define BLOCK ((UnionBlock_Type *) BLOCK_BASE)
"""


def test_all_union_views_counts_stride_and_origins_match_independent_compiler(tmp_path):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    header = tmp_path / "union.h"
    header.write_text(HEADER)
    layouts = cmsis(header, ["UnionBlock_Type"], [])
    data = layouts["UnionBlock_Type"]["DATA"]
    assert (data["offset"], data["width"], data["count"]) == (4, 32, 2)
    assert [(v["name"], v["width"]) for v in data["views"]] == [("byte", 8), ("half", 16), ("word", 32)]
    assert layouts["UnionBlock_Type"]["STATUS"]["offset"] == 12
    item = parse_cmsis_headers(header, structures={"serial": "UnionBlock_Type"}, stm32_views=False)["serial"]
    register = next(r for r in item.registers if r.name == "DATA")
    assert register.access == "unknown" and register.access_widths == [] and register.reset is None
    assert (register.offset, register.width, register.count) == (4, 32, 2)
    assert [v.name for v in register.storage_views] == ["byte", "half", "word"]
    assert register.storage_views[0].sources[0].locator == "UnionBlock_Type.DATA.byte"
    # GCC independently checks Clang's ABI conclusions; no source build script runs.
    unit = tmp_path / "assertions.c"
    unit.write_text('#include "union.h"\n'
        '_Static_assert(__builtin_offsetof(UnionBlock_Type, DATA[1].half) == 8, "stride");\n'
        '_Static_assert(sizeof(((UnionBlock_Type *)0)->DATA) == 8, "array");\n'
        '_Static_assert(sizeof(UnionBlock_Type) == 16, "size");\n')
    subprocess.run(["arm-none-eabi-gcc", "-mcpu=cortex-m4", "-mthumb", "-std=c11", "-fsyntax-only", str(unit)],
                   check=True, capture_output=True, timeout=20)


@pytest.mark.parametrize("alternative", ["unsigned char array[4]", "unsigned int bits:3",
    "void *pointer", "struct { unsigned int value; } nested", "float value"])
def test_unsupported_union_forms_fail_explicitly(tmp_path, alternative):
    require_tool("clang")
    require_tool("arm-none-eabi-gcc")
    header = tmp_path / "unsupported.h"
    header.write_text(f"typedef struct {{ union {{ unsigned int word; {alternative}; }} DATA; }} Block_Type;")
    with pytest.raises(PraxisError, match="UNSUPPORTED_DECLARATION"):
        cmsis(header, ["Block_Type"], [])


def test_empty_views_do_not_change_historical_definition_serialization():
    register = Register(name="DATA", offset=0, width=32, access="unknown", side_effects="Not asserted",
        sources=[SourceRef(source="header", locator="Block.DATA")])
    assert "storage_views" not in register.model_dump()
    assert "storage_views" not in register.model_dump_json()
