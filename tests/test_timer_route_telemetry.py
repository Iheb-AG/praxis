"""Timer software ABI, shared application effects and fake-probe MCP qualification."""

import asyncio
import io
import json
import os
import struct
import subprocess
import sys

import pytest
from elftools.elf.elffile import ELFFile
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_tool
from praxis import timer_route_telemetry as timer
from praxis.bundle import Bundle
from praxis.cli import main
from praxis.errors import PraxisError
from praxis.firmware_build import BuildService, build_commands
from praxis.hardware import provision_profile
from praxis.telemetry import get_contract, telemetry_address
from test_hardware_inspection import PROBE, values
from test_telemetry import register_fixture

APP = ROOT / "examples/stm32f407g-disc1-timer/routes_telemetry_application"
BUNDLE = ROOT / "bundles/stm32f407g-disc1-e01-timer-routes-v1"
ASSETS = ROOT / "assets/stm32f407vg"
ARTIFACT = "a" * 64
REVISION = Bundle(BUNDLE).manifest.bundle_revision


def words(**changes):
    row = dict.fromkeys(timer.FIELDS, 0)
    row.update(timer.EXPECTED)
    row.update(
        generation=2,
        magic=timer.MAGIC,
        abi=timer.ABI,
        size_bytes=timer.SIZE,
        publications=1,
        phase=1,
        status=0,
        flags=11,
        frames=8,
        captures=9,
        end_valid_mask=7,
    )
    row.update({f"capture{i}": (i + 1) * 1000 for i in range(9)})
    row.update(changes)
    return [row[k] for k in timer.FIELDS]


def observation(**changes):
    return dict(
        artifact_id=ARTIFACT,
        bundle_revision=REVISION,
        kind=timer.KIND,
        symbol=timer.SYMBOL,
        abi=timer.ABI,
        record_bytes=timer.SIZE,
        readback_verified_before_and_after=True,
        execution_state="running",
        image_sha256="b" * 64,
        elf_sha256="c" * 64,
        samples=[
            dict(
                zip(
                    timer.FIELDS,
                    words(generation=2 + i * 2, publications=i + 1, **changes),
                    strict=True,
                )
            )
            for i in range(3)
        ],
        assessment={"loopback_success_reported": True},
    )


def qualify(rows, **kwargs):
    return timer.qualify_windows(rows, artifact_id=ARTIFACT, bundle_revision=REVISION, **kwargs)


@pytest.mark.parametrize(
    "change",
    [
        {"generation": 3},
        {"magic": 0},
        {"abi": 2},
        {"size_bytes": 0},
        {"phase": 3},
        {"status": 9},
        {"flags": 16},
        {"end_valid_mask": 8},
        {"captures": 10},
        {"frames": 9},
        {"capture0": True},
        {"capture1": -1},
        {"publications": 2**32},
    ],
)
def test_malformed_or_torn_records_are_rejected(change):
    with pytest.raises(PraxisError, match="TELEMETRY_(ABI|PROTOCOL)"):
        timer.decode_sample(words(**change))


@pytest.mark.parametrize(
    "change",
    [
        {"phase": 0},
        {"phase": 2, "status": 6, "flags": 15},
        {"status": 5},
        {"flags": 15},
        {"frames": 7},
        {"captures": 8},
        {"capture3": 4003},
        {"capture4": 4997},
        {"clock_hz": 84000000},
        {"period_ticks": 1100},
        {"tolerance_ticks": 500},
        {"prescaler": 83},
        {"period_counts": 1100},
        {"high_counts": 750},
        {"end_valid_mask": 3},
        {"end_pwm_cr1": 1},
        {"end_pwm_ccer": 16},
        {"end_pwm_dier": 2},
        {"end_capture_cr1": 1},
        {"end_capture_ccer": 256},
        {"end_capture_dier": 1},
        {"end_pin_modes": 8},
    ],
)
def test_wrong_period_recipe_result_or_shutdown_cannot_pass(change):
    assert not qualify([observation(**change)])["passed"]


@pytest.mark.parametrize(
    "key,value",
    [
        ("artifact_id", "f" * 64),
        ("bundle_revision", "f" * 64),
        ("kind", "can-loopback-v1"),
        ("symbol", "arbitrary"),
        ("abi", True),
        ("record_bytes", True),
        ("image_sha256", []),
        ("elf_sha256", None),
        ("readback_verified_before_and_after", 1),
        ("execution_state", "halted"),
    ],
)
def test_identity_and_exact_image_metadata_fail_closed(key, value):
    row = observation()
    row[key] = value
    assert not qualify([row])["passed"]


def test_every_raw_interval_is_recomputed_and_cross_window_freshness_is_required():
    assert qualify([observation()])["passed"]
    row = observation(capture4=7000)
    for s in row["samples"]:
        s["phase_name"] = "passed"
    assert not qualify([row])["passed"]
    assert not qualify([observation(), observation()])["passed"]
    later = observation()
    for s in later["samples"]:
        s["generation"] += 6
        s["publications"] += 3
    assert qualify([observation(), later])["passed"]
    later["elf_sha256"] = "d" * 64
    assert not qualify([observation(), later])["passed"]
    row = observation()
    row["samples"][1]["capture4"] += 1
    assert not qualify([row])["passed"]  # Stable terminal result required, even within tolerance.


def test_only_bounded_coherent_rollovers_are_accepted():
    a = timer.decode_sample(words(generation=0xFFFFFFFE, publications=0xFFFFFFFF))
    b = timer.decode_sample(words(generation=0, publications=0))
    assert timer.assess([a, b])["loopback_success_reported"]
    b["generation"] = 2
    assert not timer.assess([a, b])["loopback_success_reported"]
    row = observation()
    for s in row["samples"]:
        for i in range(9):
            s[f"capture{i}"] = (0xFFFFF800 + i * 1000) & 0xFFFFFFFF
    assert qualify([row])["passed"]


@pytest.mark.parametrize("status", [5, 7])
def test_a_valid_stored_interval_cannot_be_falsely_reported_as_unvalidated(status):
    record = observation(
        phase=2,
        status=status,
        flags=15,
        frames=0,
        captures=2,
        **{f"capture{i}": 0 for i in range(2, 9)},
    )
    assert not qualify([record], expected="failed")["passed"]


@pytest.mark.parametrize("shape", [None, [], [{}], [{}] * 6])
def test_malformed_windows_are_rejected(shape):
    row = observation()
    row["samples"] = shape
    with pytest.raises(PraxisError, match="INVALID_OBSERVATION"):
        qualify([row])


@pytest.fixture(scope="module")
def model(tmp_path_factory):
    require_tool("gcc")
    out = tmp_path_factory.mktemp("timer-publisher") / "model"
    subprocess.run(
        [
            "gcc",
            "-std=c11",
            "-Wall",
            "-Wextra",
            "-Werror",
            "-isystem",
            str(ASSETS / "include"),
            "-I",
            str(APP),
            str(ROOT / "tests/fixtures/f407_timer_route_telemetry_model.c"),
            "-o",
            str(out),
        ],
        check=True,
        capture_output=True,
        timeout=30,
    )
    return out


def model_row(model, fault=0, wrap=False):
    result = json.loads(
        subprocess.check_output([str(model), str(fault), *(["wrap"] if wrap else [])], timeout=5)
    )
    assert result["violations"] == 0 and result["reads"] < 100600 and result["writes"] < 60
    assert result["fences"] == 4
    row = timer.decode_sample(result["words"])
    record = observation()
    for i in range(3):
        record["samples"][i] = {
            **row,
            "generation": row["generation"] + 2 * i,
            "publications": row["publications"] + i,
        }
    return row, record


@pytest.mark.parametrize("wrap", [False, True])
def test_shared_application_and_publisher_qualify_independent_model_capture(model, wrap):
    row, record = model_row(model, wrap=wrap)
    assert row["frames"] == 8 and row["captures"] == 9 and qualify([record])["passed"]


@pytest.mark.parametrize("fault", range(1, 32))
def test_every_modeled_fault_is_preserved_in_raw_terminal_observations(model, fault):
    row, record = model_row(model, fault)
    assert row["phase"] == 2 and not qualify([record])["passed"]
    safe = fault in [1, 8, 9, 10, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 30]
    assert qualify([record], expected="failed")["passed"] == safe
    assert qualify([record], expected="timeout")["passed"] == (fault == 1)


def test_header_layout_and_controller_snapshots_match_fixed_python_contract(model):
    row, _ = model_row(model)
    assert row["size_bytes"] == timer.SIZE == 136
    for name in ["timer_controller.h", "routed_timer.h"]:
        assert (APP / name).read_bytes() == (APP.parent / "routes_application" / name).read_bytes()
    assert timer.SPEC["scope"].startswith("Fixed one-shot")


def test_observation_acceptance_plan_preserves_every_previous_source_case():
    from praxis.acceptance import AcceptancePlan

    prior = AcceptancePlan.model_validate_json(
        (ROOT / "examples/acceptance/stm32f407g-disc1-timer-routes.json").read_bytes()
    )
    current = AcceptancePlan.model_validate_json(
        (ROOT / "examples/acceptance/stm32f407g-disc1-timer-observations.json").read_bytes()
    )
    assert current.cases[:-1] == prior.cases and len(current.cases) == 16
    assert current.cases[-1].source_directory.endswith("/routes_telemetry_application")


@pytest.fixture(scope="module")
def timer_elf(tmp_path_factory):
    require_tool("arm-none-eabi-gcc")
    out = tmp_path_factory.mktemp("timer-abi")
    for compiler, flags in build_commands(["main.c"]):
        args = [
            a.replace("/approved/", str(ASSETS) + "/")
            .replace("/src/", str(APP) + "/")
            .replace("/out/", str(out) + "/")
            .replace("-I/src", "-I" + str(APP))
            for a in flags
        ]
        subprocess.run([compiler, *args], cwd=out, check=True, capture_output=True, timeout=30)
    return (out / "firmware.elf").read_bytes()


def test_contract_object_size_address_and_other_abi_rejection(timer_elf):
    contract = get_contract(timer.KIND)
    assert telemetry_address(timer_elf, (0x20000000, 128 * 1024), contract=contract) % 4 == 0
    with pytest.raises(PraxisError, match="TELEMETRY_UNSUPPORTED"):
        telemetry_address(timer_elf, (0x20000000, 128 * 1024))
    elf = ELFFile(io.BytesIO(timer_elf))
    table = elf.get_section_by_name(".symtab")
    index = next(i for i, s in enumerate(table.iter_symbols()) if s.name == timer.SYMBOL)
    for offset, value in [(4, 0x40000000), (8, 4)]:
        bad = bytearray(timer_elf)
        struct.pack_into(
            "<I", bad, table["sh_offset"] + index * table["sh_entsize"] + offset, value
        )
        with pytest.raises(PraxisError, match="TELEMETRY_UNSUPPORTED"):
            telemetry_address(bytes(bad), (0x20000000, 128 * 1024), contract=contract)


def test_offline_cli_recomputes_and_refuses_overwriting_evidence(tmp_path):
    source = tmp_path / "observation.json"
    out = tmp_path / "qualification.json"
    source.write_text(json.dumps(observation()))
    args = [
        "qualify-timer",
        "--bundle",
        str(BUNDLE),
        "--artifact",
        ARTIFACT,
        "--observation",
        str(source),
        "--output",
        str(out),
    ]
    assert main(args) == 0
    assert json.loads(out.read_text())["passed"]
    assert main(args) == 2
    source.write_text(json.dumps(observation(capture4=9000)))
    assert main(args[:-2]) == 1


async def test_actual_stdio_mcp_with_explicit_fixture_probe(tmp_path, timer_elf):
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    build = BuildService(
        BUNDLE, ASSETS, workspace, tmp_path / "artifacts", ROOT / "toolchain-f407.lock.json"
    )
    artifact = register_fixture(build, timer_elf)
    data = values()
    rows = [words(), words(generation=4, publications=2)]
    backend = tmp_path / "fixture-openocd"
    backend.write_text(
        "#!" + sys.executable + "\nimport sys,pathlib\n"
        "if '--version' in sys.argv: print('Open On-Chip Debugger 0.12.0 (TEST ONLY)');sys.exit(0)\n"
        "script=pathlib.Path(sys.argv[-1]).read_text()\n"
        f"pathlib.Path({str(tmp_path / 'executed.tcl')!r}).write_text(script)\n"
        f"for k,v in {data!r}.items():\n"
        " if ('|'+k+'|') in script: print('PRAXIS|'+k+'|'+(v if k=='state' else '0x%08x'%v))\n"
        "if 'PRAXIS_TELEMETRY_COMPLETE' in script:\n"
        " print('PRAXIS_IMAGE_VERIFIED')\n"
        f" for i,row in enumerate({rows!r}[:script.count('echo \"PRAXIS_TELEMETRY|')]):\n"
        "  print('PRAXIS_TELEMETRY|%d|'%i+','.join('%08x'%v for v in row))\n"
        " print('PRAXIS_IMAGE_REVERIFIED');print('PRAXIS_TELEMETRY_COMPLETE')\n"
    )
    backend.chmod(0o700)
    profile = tmp_path / "hardware.json"
    provision_profile(BUNDLE, ASSETS, backend, profile)
    script = (
        "from pathlib import Path\nimport praxis.hardware\n"
        f"praxis.hardware.discover_probes=lambda:[{PROBE!r}]\n"
        "from praxis.build_server import create_build_server\n"
        f"create_build_server(Path({str(BUNDLE)!r}),Path({str(ASSETS)!r}),"
        f"Path({str(workspace)!r}),Path({str(build.artifacts)!r}),Path({str(build.lock_path)!r}),"
        f'Path({str(profile)!r}),telemetry_artifact={artifact!r},telemetry_kind={timer.KIND!r}).run(transport="stdio")'
    )
    params = StdioServerParameters(
        command=sys.executable, args=["-c", script], cwd=str(tmp_path), env=dict(os.environ)
    )

    async def exercise():
        async with (
            stdio_client(params) as (reader, writer),
            ClientSession(reader, writer) as client,
        ):
            await client.initialize()
            tools = {t.name: t for t in (await client.list_tools()).tools}
            assert tools["read_firmware_telemetry"].annotations.readOnlyHint
            assert set(tools["read_firmware_telemetry"].inputSchema["properties"]) == {
                "connection_id",
                "samples",
                "interval_ms",
            }
            assert (
                not {"flash_firmware", "control_execution", "read_can_diagnostics"} & tools.keys()
            )

            async def call(name, args):
                r = await client.call_tool(name, args)
                assert not r.isError
                return r.structuredContent or json.loads(r.content[0].text)

            p = await call("get_build_profile", {})
            assert p["firmware_telemetry"]["kind"] == timer.KIND
            target = await call("inspect_target", {"probe_serial": "TEST123"})
            result = await call(
                "read_firmware_telemetry", {"connection_id": target["connection_id"]}
            )
            assert timer.qualify_windows([result], artifact_id=artifact, bundle_revision=REVISION)[
                "passed"
            ]
            for args in [
                {"connection_id": "unknown"},
                {"connection_id": target["connection_id"], "samples": 6},
            ]:
                r = await client.call_tool("read_firmware_telemetry", args)
                assert r.isError
            # SDK v1 ignores surplus keys. They must never redirect the fixed reader.
            redirected = await call(
                "read_firmware_telemetry",
                {
                    "connection_id": target["connection_id"],
                    "address": 0xDEADBEEC,
                    "symbol": "arbitrary",
                    "artifact_id": "f" * 64,
                },
            )
            assert redirected["artifact_id"] == artifact and redirected["symbol"] == timer.SYMBOL
            executed = (tmp_path / "executed.tcl").read_text()
            address = telemetry_address(
                timer_elf, build.assets.ram, contract=get_contract(timer.KIND)
            )
            assert f"read_memory 0x{address:08x} 32" in executed
            assert "deadbeec" not in executed.lower() and "arbitrary" not in executed

    await asyncio.wait_for(exercise(), 30)
