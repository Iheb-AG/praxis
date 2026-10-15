"""Fixed-ABI telemetry tests. Fake probes and modeled Tcl never attach to hardware."""

import asyncio
import io
import json
import os
import re
import struct
import subprocess
import sys

import pytest
from elftools.elf.elffile import ELFFile
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from conftest import ROOT, require_tool
from praxis.bundle import digest
from praxis.errors import PraxisError
from praxis.firmware_build import FLAGS, build_commands
from praxis.hardware import HardwareService, IDENTITY, provision_profile
from praxis.programming import image_from_elf
from praxis.telemetry import (
    ABI,
    FIELDS,
    MAGIC,
    SIZE,
    TelemetryService,
    assess,
    decode_sample,
    parse_samples,
    read_telemetry_script,
    telemetry_address,
)
from test_firmware_build import good_elf as good_elf, service
from test_hardware_inspection import PROBE, values


@pytest.fixture(scope="module")
def telemetry_elf(tmp_path_factory):
    require_tool("arm-none-eabi-gcc")
    out = tmp_path_factory.mktemp("trusted-telemetry")
    src = ROOT / "examples/stm32f407g-disc1-uart-loopback/telemetry_application"
    assets = ROOT / "assets/stm32f407vg"
    for compiler, flags in build_commands(["controller.c", "main.c", "protocol.c"]):
        args = [
            a.replace("/approved/", str(assets) + "/")
            .replace("/src/", str(src) + "/")
            .replace("/out/", str(out) + "/")
            .replace("-I/src", "-I" + str(src))
            for a in flags
        ]
        subprocess.run([compiler, *args], cwd=out, check=True, capture_output=True, timeout=20)
    return (out / "firmware.elf").read_bytes()


def words(**changes):
    row = dict.fromkeys(FIELDS, 0)
    row.update(
        generation=2,
        magic=MAGIC,
        abi=ABI,
        size_bytes=SIZE,
        uptime_ms=100,
        timer_irqs=100,
        state=1,
        run_number=1,
    )
    row.update(changes)
    return [row[name] for name in FIELDS]


def output(*rows):
    return (
        "\n".join(
            [
                "PRAXIS_IMAGE_VERIFIED",
                *[
                    f"PRAXIS_TELEMETRY|{i}|" + ",".join(f"{x:08x}" for x in row)
                    for i, row in enumerate(rows)
                ],
                "PRAXIS_IMAGE_REVERIFIED",
                "PRAXIS_TELEMETRY_COMPLETE",
            ]
        )
        + "\n"
    )


@pytest.mark.parametrize(
    "changes,code",
    [
        ({"magic": 0}, "TELEMETRY_ABI"),
        ({"abi": 2}, "TELEMETRY_ABI"),
        ({"generation": 3}, "TELEMETRY_ABI"),
        ({"size_bytes": 4}, "TELEMETRY_ABI"),
        ({"state": 99}, "TELEMETRY_ABI"),
        ({"failure_reason": 99}, "TELEMETRY_ABI"),
        ({"flags": 16}, "TELEMETRY_ABI"),
        ({"rx_bytes": -1}, "TELEMETRY_PROTOCOL"),
    ],
)
def test_unknown_or_torn_records_rejected(changes, code):
    with pytest.raises(PraxisError, match=code):
        decode_sample(words(**changes))


def test_progress_paused_failure_staleness_and_rollover():
    first = decode_sample(words(frames_validated=99, run_validated=99))
    last = decode_sample(
        words(
            generation=4,
            uptime_ms=200,
            timer_irqs=200,
            frames_validated=100,
            run_validated=100,
            flags=1,
        )
    )
    result = assess([first, last])
    assert (
        result["fresh_progress"]
        and result["uart_progress_observed"]
        and result["blue_success_reported"]
    )
    assert not assess([last, last])["fresh_progress"]
    failed = decode_sample(
        words(generation=6, state=3, failure_reason=1, uptime_ms=300, timer_irqs=300)
    )
    assert assess([last, failed])["firmware_failure_reported"]
    assert not assess([last, failed])["uart_progress_observed"]
    paused = decode_sample(words(generation=8, state=0, uptime_ms=400, timer_irqs=400))
    paused2 = decode_sample(words(generation=10, state=0, uptime_ms=500, timer_irqs=500))
    assert assess([paused, paused2])["fresh_progress"]
    assert not assess([paused, paused2])["uart_progress_observed"]
    wrapped = [
        decode_sample(words(generation=0xFFFFFFFE, uptime_ms=0xFFFFFFF0, timer_irqs=0xFFFFFFF0)),
        decode_sample(words(generation=0, uptime_ms=20, timer_irqs=20)),
    ]
    assert assess(wrapped)["fresh_progress"]
    reset = decode_sample(words(generation=2, uptime_ms=0, timer_irqs=0))
    assert not assess([last, reset])["fresh_progress"]
    changed_run = decode_sample(words(generation=6, uptime_ms=300, timer_irqs=300, run_number=2))
    assert not assess([last, changed_run])["same_run"]
    assert not assess([last])["fresh_progress"]


@pytest.mark.parametrize(
    "bad",
    ["missing", "duplicate", "out_of_order", "word_count", "nonhex", "completion", "unbracketed"],
)
def test_backend_response_is_fail_closed(bad):
    text = output(words(), words(generation=4))
    if bad == "missing":
        text = text.replace("PRAXIS_IMAGE_VERIFIED\n", "")
    if bad == "duplicate":
        text += "PRAXIS_IMAGE_REVERIFIED\n"
    if bad == "out_of_order":
        text = text.replace("PRAXIS_TELEMETRY|1|", "PRAXIS_TELEMETRY|0|")
    if bad == "word_count":
        text = text.replace("50525831,", "")
    if bad == "nonhex":
        text = text.replace("50525831", "zzzzzzzz")
    if bad == "completion":
        text = text.replace("PRAXIS_TELEMETRY_COMPLETE", "")
    if bad == "unbracketed":
        text = text.replace("PRAXIS_IMAGE_VERIFIED\n", "") + "PRAXIS_IMAGE_VERIFIED\n"
    with pytest.raises(PraxisError, match="TELEMETRY_PROTOCOL"):
        parse_samples(text, 2)


@pytest.mark.parametrize(
    "count,interval", [(0, 100), (6, 100), (True, 100), (2, 0), (2, 1001), (2, True)]
)
def test_bounded_arguments(count, interval):
    with pytest.raises(PraxisError, match="INVALID_TELEMETRY_REQUEST"):
        read_telemetry_script("000000010000000200000003", bytes(392), 0x20000004, count, interval)


@pytest.mark.parametrize("size", [0, 391, 65537])
def test_image_verification_work_is_bounded(size):
    with pytest.raises(PraxisError, match="TELEMETRY_UNSUPPORTED"):
        read_telemetry_script("000000010000000200000003", bytes(size), 0x20000004, 2, 100)


def test_elf_object_layout_and_missing_symbol(telemetry_elf, good_elf):
    assert telemetry_address(telemetry_elf, (0x20000000, 128 * 1024)) % 4 == 0
    with pytest.raises(PraxisError, match="TELEMETRY_UNSUPPORTED"):
        telemetry_address(good_elf, (0x20000000, 128 * 1024))
    elf = ELFFile(io.BytesIO(telemetry_elf))
    table = elf.get_section_by_name(".symtab")
    index = next(i for i, s in enumerate(table.iter_symbols()) if s.name == "praxis_telemetry")
    for offset, value in [(4, 0x40020000), (8, 4)]:  # ELF32 symbol value / size
        bad = bytearray(telemetry_elf)
        struct.pack_into(
            "<I", bad, table["sh_offset"] + index * table["sh_entsize"] + offset, value
        )
        with pytest.raises(PraxisError, match="TELEMETRY_UNSUPPORTED"):
            telemetry_address(bytes(bad), (0x20000000, 128 * 1024))


def register_fixture(build, elf):
    image = image_from_elf(elf, build.assets)
    payloads = {
        "firmware.elf": elf,
        "firmware.bin": image.data,
        "firmware.hex": b"FIXTURE",
        "firmware.map": b"FIXTURE",
    }
    report = {
        "source_sha256": "a" * 64,
        "image": "sha256:" + "b" * 64,
        "compile_passed": True,
        "image_validated": True,
        "artifact_id": None,
    }
    hashes = {name: digest(data) for name, data in payloads.items()}
    artifact = digest(
        json.dumps(
            {
                "source": report["source_sha256"],
                "bundle": build.bundle.manifest.bundle_revision,
                "assets": build.assets.identity,
                "image": report["image"],
                "files": hashes,
                "flags": FLAGS,
                "build_report": {k: v for k, v in report.items() if k != "artifact_id"},
            },
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    )
    report["artifact_id"] = artifact
    payloads["report.json"] = json.dumps(report).encode()
    root = build.artifacts / artifact
    root.mkdir(parents=True)
    for name, data in payloads.items():
        (root / name).write_bytes(data)
    (root / "manifest.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "artifact_id": artifact,
                "bundle_revision": build.bundle.manifest.bundle_revision,
                "asset_revision": build.assets.identity,
                "files": {name: digest(data) for name, data in payloads.items()},
            }
        )
    )
    return artifact


@pytest.fixture
def telemetry(tmp_path, monkeypatch, telemetry_elf):
    build = service(tmp_path)
    artifact = register_fixture(build, telemetry_elf)
    observation = tmp_path / "observation.json"
    observation.write_text(json.dumps(values()))
    backend = tmp_path / "fixture-openocd"
    backend.write_text(
        "#!"
        + sys.executable
        + "\n"
        + """import sys,json,re,pathlib
if '--version' in sys.argv:
 print('Open On-Chip Debugger 0.12.0 (TEST FIXTURE ONLY)');sys.exit(0)
"""
        + f"data=json.loads(pathlib.Path({str(observation)!r}).read_text())\n"
        + r"""
script=pathlib.Path(sys.argv[-1]).read_text()
uid=''.join('%08x'%data['uid%d'%i] for i in range(3))
expected=re.search(r'if {\$praxis_uid ne "([0-9a-f]+)"}',script)
if expected and expected[1]!=uid:
 print('PRAXIS_TARGET_CHANGED');sys.exit(1)
for k,v in data.items():
 if ('|'+k+'|') in script:print('PRAXIS|'+k+'|'+(v if k=='state' else '0x%08x'%v))
if 'PRAXIS_TELEMETRY_COMPLETE' in script:
 if data.get('mismatch'):print('PRAXIS_READBACK_MISMATCH');sys.exit(1)
 if data.get('busy'):print('PRAXIS_TELEMETRY_BUSY');sys.exit(1)
 print('PRAXIS_IMAGE_VERIFIED')
 for i in range(script.count('echo "PRAXIS_TELEMETRY|')):
  row="""
        + repr(words())
        + """
  row[0]+=2*i;row[4]+=100*i;row[5]+=100*i;row[11]=i
  print('PRAXIS_TELEMETRY|%d|'%i+','.join('%08x'%v for v in row))
 print('PRAXIS_IMAGE_REVERIFIED');print('PRAXIS_TELEMETRY_COMPLETE')
"""
    )
    backend.chmod(0o700)
    profile = tmp_path / "hardware.json"
    provision_profile(build.bundle.root, build.assets.root, backend, profile)
    monkeypatch.setattr("praxis.hardware.discover_probes", lambda: [dict(PROBE)])
    hardware = HardwareService(build.bundle, build.assets, profile, tmp_path / "locks")
    connection = hardware.inspect_target("TEST123")["connection_id"]
    return TelemetryService(build, hardware, artifact), connection, observation, profile


def test_service_reads_fixed_scope_and_rejects_unknown_connection(telemetry):
    s, connection, _, _ = telemetry
    result = s.read(connection)
    assert result["readback_verified_before_and_after"]
    assert result["assessment"]["fresh_progress"] and result["assessment"]["uart_progress_observed"]
    assert result["artifact_id"] == s.artifact_id and result["record_bytes"] == 92
    with pytest.raises(PraxisError, match="UNKNOWN_CONNECTION"):
        s.read("not-a-connection")
    with s.hardware.probe_lock("TEST123"), pytest.raises(PraxisError, match="PROBE_BUSY"):
        s.read(connection)


@pytest.mark.parametrize(
    "case,code",
    [("mismatch", "READBACK_MISMATCH"), ("busy", "TELEMETRY_BUSY"), ("uid0", "TARGET_CHANGED")],
)
def test_service_guard_failures(telemetry, case, code):
    s, connection, observation, _ = telemetry
    row = json.loads(observation.read_text())
    row[case] = 99 if case == "uid0" else True
    observation.write_text(json.dumps(row))
    with pytest.raises(PraxisError, match=code):
        s.read(connection)
    if case == "uid0":
        assert connection not in s.hardware.connections


def test_corrupted_artifact_and_backend_fail_before_reads(telemetry, monkeypatch):
    s, connection, _, _ = telemetry
    (s.build.artifacts / s.artifact_id / "firmware.elf").write_bytes(b"changed")
    monkeypatch.setattr(
        "praxis.telemetry.bounded",
        lambda *_a, **_k: pytest.fail("Invalid artifact launched backend"),
    )
    with pytest.raises(PraxisError, match="INTEGRITY_ERROR"):
        s.read(connection)


@pytest.mark.parametrize("failure", ["TIMEOUT", "OUTPUT_LIMIT"])
def test_backend_limits_no_fallback(telemetry, monkeypatch, failure):
    s, connection, _, _ = telemetry
    monkeypatch.setattr(
        "praxis.telemetry.bounded",
        lambda *_a, **_k: dict(failure=failure, returncode=-9, diagnostics=""),
    )
    with pytest.raises(PraxisError, match=failure):
        s.read(connection)


@pytest.mark.parametrize(
    "case",
    [
        "ok",
        "wrong_uid",
        "wrong_family",
        "wrong_image",
        "busy",
        "torn",
        "image_changed",
        "transient_flash",
        "transient_row",
        "inconsistent_row",
    ],
)
@pytest.mark.parametrize('kind', ['uart-loopback-v1', 'can-loopback-v1', 'timer-routes-v1', 'timer-irq-v1'])
def test_actual_tcl_identity_image_and_seqlock_guards(tmp_path, case, kind):
    require_tool("openocd")
    image = bytes(range(256)) * 2
    address = 0x20000004
    data = values()
    if case == "wrong_uid":
        data["uid0"] = 99
    if case == "wrong_family":
        data["idcode"] = 0x433
    table = {f"0x{addr:08x}": data[name] for name, (addr, _) in IDENTITY.items()}
    if kind == 'can-loopback-v1':
        table.update({'0x40023840': 1 << 25, '0x40006400': 0x10018, '0x40006404': 0xC00})
    for offset in range(0, len(image), 4):
        table[f"0x{0x08000000 + offset:08x}"] = struct.unpack_from("<I", image, offset)[0]
    if case == "wrong_image":
        table["0x08000000"] ^= 1
    pairs = " ".join(f"{k} {hex(v)}" for k, v in table.items())
    from praxis.telemetry import get_contract
    contract = get_contract(kind)
    if kind == 'can-loopback-v1':
        from test_can_telemetry import words as sample_words
    elif kind == 'timer-routes-v1':
        from test_timer_route_telemetry import words as sample_words
    elif kind == 'timer-irq-v1':
        from test_timer_irq import words as sample_words
    else:
        sample_words = words
    row = " ".join(hex(v) for v in sample_words(generation=3 if case == "busy" else 2))
    prelude = (
        "gdb_port disabled\ntcl_port disabled\ntelnet_port disabled\n"
        f"set test_values [dict create {pairs}]\nset test_row {{{row}}}\n"
        f"set test_case {case}\nset test_state running\nset test_ram_reads 0\n"
        "proc test_read {addr width count} {\n global test_values test_row test_case test_ram_reads\n"
        f" if {{$addr == {address}}} {{\n"
        "  incr test_ram_reads\n echo TEST_SRAM_READ\n"
        '  if {$test_case eq "torn" && $count==1} {\n'
        "   lset test_row 0 [expr {[lindex $test_row 0]+2}]\n }\n"
        "  if {$count==1} {return [list [lindex $test_row 0]]}\n"
        "  set result $test_row\n"
        '  if {($test_case eq "transient_row" && $test_ram_reads==2) || ($test_case eq "inconsistent_row" && $test_ram_reads%4==2)} {lset result 10 999}\n'
        "  return $result\n }\n"
        " set result {}\n for {set i 0} {$i<$count} {incr i} {\n"
        '  lappend result [dict get $test_values [format "0x%08x" [expr {$addr+$i*($width/8)}]]]\n'
        ' }\n if {$test_case eq "transient_flash" && $count>1} {lset result 0 0}\n return $result\n}\n'
        "proc test_sleep {ms} {\n global test_values test_row test_case\n"
        " if {$ms>1} {\n"
        "  foreach index {0 4 5} {lset test_row $index [expr {[lindex $test_row $index]+100}]}\n"
        '  if {$test_case eq "image_changed"} {dict set test_values 0x08000000 0}\n }\n}\n'
    )
    if kind in ('can-loopback-v1', 'timer-routes-v1', 'timer-irq-v1'):
        prelude = prelude.replace(
            'foreach index {0 4 5} {lset test_row $index [expr {[lindex $test_row $index]+100}]}',
            'lset test_row 0 [expr {[lindex $test_row 0]+2}]\n'
            'lset test_row 4 [expr {[lindex $test_row 4]+1}]')
    script = read_telemetry_script("000000010000000200000003", image, address, 2, 100,
                                   contract=contract, can_state=kind == 'can-loopback-v1')
    assert not re.search(
        r"^\s*(halt|resume|reset|write_memory|mww|mwh|mwb|flash|program|step|bp)\b", script, re.M
    )
    script = script.replace("init\n", "echo TEST_NO_ADAPTER\n", 1).replace(
        "read_memory ", "test_read "
    )
    script = script.replace("praxis.cpu curstate", "set test_state").replace(
        "sleep ", "test_sleep "
    )
    path = tmp_path / "guard.tcl"
    path.write_text(prelude + script)
    result = subprocess.run(
        ["openocd", "-f", str(path)], cwd=tmp_path, capture_output=True, text=True, timeout=5
    )
    text = result.stdout + result.stderr
    if case in {"ok", "transient_flash", "transient_row"}:
        assert result.returncode == 0, text
        assert len(parse_samples(text, 2, contract=contract)) == 2
        if kind == 'can-loopback-v1':
            from praxis.can_diagnostics import parse
            assert parse(text)['clock_enabled']
        if case == "transient_flash":
            assert "PRAXIS_FLASH_WORD_RECHECK|" in text
    else:
        assert result.returncode != 0, text
        assert "PRAXIS_TELEMETRY_COMPLETE" not in text
        if case in {"wrong_uid", "wrong_family", "wrong_image"}:
            assert "TEST_SRAM_READ" not in text


async def test_real_stdio_optional_tool_contract(telemetry, tmp_path):
    s, _, _, profile = telemetry
    # Child process uses the fake probe backend; never enumerate/attach a real one.
    script = (
        "from pathlib import Path\nimport praxis.hardware\n"
        f"praxis.hardware.discover_probes=lambda:[{PROBE!r}]\n"
        "from praxis.build_server import create_build_server\n"
        f"create_build_server(Path({str(s.build.bundle.root)!r}),Path({str(s.build.assets.root)!r}),"
        f"Path({str(s.build.workspace)!r}),Path({str(s.build.artifacts)!r}),Path({str(s.build.lock_path)!r}),"
        f'Path({str(profile)!r}),telemetry_artifact={s.artifact_id!r}).run(transport="stdio")\n'
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
            tool = tools["read_firmware_telemetry"]
            assert tool.annotations.readOnlyHint and "flash_firmware" not in tools
            assert set(tool.inputSchema["properties"]) == {
                "connection_id",
                "samples",
                "interval_ms",
            }
            result = await client.call_tool("inspect_target", {"probe_serial": "TEST123"})
            target = result.structuredContent or json.loads(result.content[0].text)
            result = await client.call_tool(
                "read_firmware_telemetry", {"connection_id": target["connection_id"]}
            )
            data = result.structuredContent or json.loads(result.content[0].text)
            assert not result.isError and data["assessment"]["fresh_progress"]
            result = await client.call_tool(
                "read_firmware_telemetry", {"connection_id": target["connection_id"], "samples": 6}
            )
            assert result.isError and "INVALID_TELEMETRY_REQUEST" in result.content[0].text

    await asyncio.wait_for(exercise(), 30)
