import json
import sys
from pathlib import Path

import pytest

from praxis.errors import PraxisError
from praxis.repair import repair_loop
from praxis.verify import bounded, command, snapshot, verify
from conftest import ROOT, require_image

IMAGE = "sha256:" + "a" * 64


def test_fixed_command_is_rootless_offline_and_bounded():
    args = command(IMAGE, "stm32", Path("/tmp/src"), Path("/tmp/headers"), Path("/tmp/out"),
                   "driver.c", "object", 16000000, "test")
    for flag in ["--pull=never", "--network=none", "--read-only", "--cap-drop=ALL",
                 "--security-opt=no-new-privileges", "--userns=keep-id", "--memory=1g",
                 "--cpus=1", "--pids-limit=64", "-mfloat-abi=soft", "-DSTM32F401xE", "-c"]:
        assert flag in args
    assert args[args.index("--entrypoint") + 1] == "/usr/bin/arm-none-eabi-gcc"
    assert not any("fplugin" in arg for arg in args)
    avr = command(IMAGE, "avr", Path("/tmp/src"), Path("/tmp/headers"), Path("/tmp/out"),
                  "driver.c", "syntax", 16000000, "test")
    assert "-mmcu=atmega328p" in avr and "-DF_CPU=16000000UL" in avr


@pytest.mark.parametrize("text", [
    '#include "/etc/passwd"\n', '#include "../secret.h"\n', '#include <stdio.h>\n',
    '#define HEADER "/etc/passwd"\n#include HEADER\n', '#include_next <stdint.h>\n',
    '#embed "/etc/passwd"\n', '%:include "/etc/passwd"\n', '??=include "/etc/passwd"\n',
    '#inc\\\nlude "/etc/passwd"\n', '#/**/include "/etc/passwd"\n',
])
def test_forbidden_source_includes_rejected(tmp_path, text):
    source, out = tmp_path / "source", tmp_path / "snapshot"
    source.mkdir()
    out.mkdir()
    (source / "driver.c").write_text(text)
    with pytest.raises(PraxisError, match="FORBIDDEN_INCLUDE"):
        snapshot(source, out)


def test_symlink_source_rejected(tmp_path):
    source, out = tmp_path / "source", tmp_path / "snapshot"
    source.mkdir()
    out.mkdir()
    (source / "driver.c").symlink_to("/etc/passwd")
    with pytest.raises(PraxisError, match="INVALID_SOURCE"):
        snapshot(source, out)


def test_snapshot_is_deterministic_and_size_limited(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "driver.c").write_text('#include <stdint.h>\n#include "local.h"\nuint32_t value;\n')
    (source / "local.h").write_text("/* header */\n")
    first, second = tmp_path / "first", tmp_path / "second"
    first.mkdir()
    second.mkdir()
    assert snapshot(source, first) == snapshot(source, second)
    (source / "driver.c").write_bytes(b"x" * (2 * 1024 * 1024 + 1))
    with pytest.raises(PraxisError, match="DOCUMENT_TOO_LARGE"):
        snapshot(source, second)


def test_process_diagnostic_limit_and_timeout():
    result = bounded([sys.executable, "-c", "print('x' * 200000)"], 5)
    assert result["failure"] == "OUTPUT_LIMIT" and len(result["diagnostics"]) == 65536
    result = bounded([sys.executable, "-c", "import time; time.sleep(10)"], 0.1)
    assert result["failure"] == "TIMEOUT"


def test_unprovisioned_lock_never_falls_back_to_native(tmp_path):
    unprovisioned = tmp_path / "unprovisioned.json"
    value = json.loads((ROOT / "toolchain.lock.json").read_text())
    value["image"] = None
    unprovisioned.write_text(json.dumps(value))
    with pytest.raises(PraxisError, match="UNPROVISIONED_IMAGE"):
        verify(ROOT / "bundles/stm32f401re", ROOT / "examples/stm32f401re", "syntax",
               unprovisioned, tmp_path / "output")
    assert not (tmp_path / "output").exists()


def test_repair_loop_stops_for_repetition_limit_and_missing_facts():
    def report(text, passed=False):
        return {"compile_passed": passed, "records": [{"diagnostics": text, "failure": None}],
                "source_sha256": "source", "bundle_revision": "revision", "compiler_identity": "compiler"}
    repairs = []
    assert repair_loop(lambda: report("same"), lambda r: repairs.append(r) or True)["stop"] == "repeated_diagnostics"
    assert len(repairs) == 1
    reports = iter([report("a"), report("b"), report("c")])
    result = repair_loop(lambda: next(reports), lambda r: True)
    assert result["stop"] == "attempt_limit" and len(result["attempts"]) == 3
    assert repair_loop(lambda: report("missing"), lambda r: False)["stop"] == "unsupported_or_missing_facts"
    assert repair_loop(lambda: report("", True), lambda r: pytest.fail("No repair needed"))["stop"] == "passed"


def sandbox_lock():
    return require_image(ROOT / "toolchain.lock.json")


def test_live_sandbox_compiles_and_cannot_write_inputs(tmp_path):
    lock = sandbox_lock()
    source = tmp_path / "input"
    source.mkdir()
    (source / "driver.c").write_text("#include <stdint.h>\nuint32_t value = 7;\n")
    report = verify(ROOT / "bundles/stm32f401re", source, "object", lock, tmp_path / "result")
    assert report["compile_passed"]
    assert list((tmp_path / "result").glob("*.o"))
    assert (source / "driver.c").read_text().endswith("= 7;\n")


def test_live_container_isolation_policy(tmp_path):
    lock_path = sandbox_lock()
    lock = json.loads(lock_path.read_text())
    source, headers, output = tmp_path / "source", tmp_path / "headers", tmp_path / "output"
    for path in [source, headers, output]:
        path.mkdir()
    from praxis.verify import _rootless
    _rootless()
    args = command(lock["image"], "stm32", source, headers, output, "x.c", "syntax", 16000000, "praxis-isolation-test")
    position = args.index("--entrypoint")
    # Test the exact mount/resource policy using a trusted shell probe, never generated code.
    args[position + 1] = "/bin/bash"
    args = args[:position + 3] + ["-c", """
        set -eu
        ! touch /src/forbidden
        ! touch /approved/forbidden
        ! touch /etc/forbidden
        test ! -e /dev/ttyUSB0
        test ! -e /dev/ttyACM0
        test "$(cat /sys/fs/cgroup/memory.max)" = 1073741824
        test "$(cat /sys/fs/cgroup/pids.max)" = 64
        if (echo test > /dev/tcp/1.1.1.1/80) 2>/dev/null; then exit 1; fi
        touch /out/allowed
    """]
    result = bounded(args, 10)
    assert result["returncode"] == 0, result["diagnostics"]
    assert (output / "allowed").exists()
    assert not (source / "forbidden").exists()
