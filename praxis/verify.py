"""Fixed-command, rootless Podman verification. Never a native compilation fallback."""

from __future__ import annotations

import json
import os
import platform
import re
import selectors
import shutil
import signal
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

from praxis.bundle import Bundle, digest, read_inside
from praxis.errors import PraxisError
from praxis.process import run

MAX_SOURCE_BYTES = 2 * 1024 * 1024
MAX_FILES = 128
MAX_DIAGNOSTICS = 64 * 1024
APPROVED_SYSTEM_INCLUDES = {"stdint.h", "stddef.h", "stdbool.h", "limits.h", "avr/io.h",
                            "avr/interrupt.h", "stm32f401xe.h", "stm32f407xx.h"}
IMAGE = re.compile(r"(?:[a-zA-Z0-9./:_-]+@)?sha256:[0-9a-f]{64}\Z")


def _rootless():
    if platform.system() != "Linux":
        raise PraxisError("UNSUPPORTED_PLATFORM", "Sandbox compilation requires Linux; retrieval is portable")
    if not shutil.which("podman"):
        raise PraxisError("MISSING_TOOL", "Install rootless Podman; native fallback is intentionally unavailable")
    if run(["podman", "info", "--format", "{{.Host.Security.Rootless}}"], limit=4096).strip() != "true":
        raise PraxisError("ROOTLESS_REQUIRED", "Run Podman as an unprivileged user with rootless support")


def _image(value):
    if not isinstance(value, str) or not IMAGE.fullmatch(value):
        raise PraxisError("UNPROVISIONED_IMAGE", "Provision a toolchain lock containing an immutable sha256 image reference")
    return value


def snapshot(source: Path, destination: Path) -> tuple[list[str], str]:
    if source.is_symlink() or not source.is_dir():
        raise PraxisError("INVALID_SOURCE", "Source must be a real directory, not a symlink")
    files, total, hashes = [], 0, {}
    for entry in sorted(source.rglob("*")):
        if entry.is_symlink():
            raise PraxisError("INVALID_SOURCE", f"Symlinks are forbidden: {entry.name}")
        if entry.is_dir():
            continue
        if not entry.is_file():
            raise PraxisError("INVALID_SOURCE", "Only regular source files are accepted")
        name = entry.relative_to(source).as_posix()
        if not re.fullmatch(r"[A-Za-z0-9_./-]+", name) or entry.suffix not in (".c", ".h"):
            raise PraxisError("INVALID_SOURCE", f"Only C/header files with simple names are accepted: {name}")
        contents = read_inside(source.resolve(), name, MAX_SOURCE_BYTES)
        total += len(contents)
        if total > MAX_SOURCE_BYTES or len(files) >= MAX_FILES:
            raise PraxisError("SOURCE_LIMIT", "Source exceeds 2 MiB or 128 files")
        try:
            text = contents.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise PraxisError("INVALID_SOURCE", "Generated C/header input must be UTF-8") from exc
        # Normalize physical line splices before checking preprocessing directives.
        text = re.sub(r"\\\r?\n", "", text)
        if re.search(r"\?\?[=/'()!<>-]", text):
            raise PraxisError("FORBIDDEN_INCLUDE", "Trigraphs are unavailable in generated sources")
        text = re.sub(r"^(\s*)%:", r"\1#", text, flags=re.M)
        text = re.sub(r"/\*.*?\*/|//[^\n]*", " ", text, flags=re.S)
        for directive in re.finditer(r"^\s*#\s*(include(?:_next)?|embed)\b([^\n]*)", text, re.M):
            if directive[1] != "include":
                raise PraxisError("FORBIDDEN_INCLUDE", "include_next and embed are unavailable in generated sources")
            match = re.fullmatch(r'\s*(?:<([^>]+)>|"([^"]+)")\s*', directive[2])
            if not match:
                raise PraxisError("FORBIDDEN_INCLUDE", "Only literal approved includes are accepted")
            if match[1] and match[1] not in APPROVED_SYSTEM_INCLUDES:
                raise PraxisError("FORBIDDEN_INCLUDE", f"System include is not approved: {match[1]}")
            if match[2]:
                include = Path(match[2])
                if (include.is_absolute() or ".." in include.parts or "\\" in match[2]
                        or ":" in match[2] or not re.fullmatch(r"[A-Za-z0-9_./-]+", match[2])):
                    raise PraxisError("FORBIDDEN_INCLUDE", f"Unsafe include: {match[2]}")
        dest = destination / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(contents)
        hashes[name] = digest(contents)
        files.append(name)
    units = [name for name in files if name.endswith(".c")]
    if not units:
        raise PraxisError("INVALID_SOURCE", "At least one C translation unit is required")
    fingerprint = digest(json.dumps(hashes, sort_keys=True, separators=(",", ":")).encode())
    return units, fingerprint


def command(image: str, family: str, source: Path, headers: Path, output: Path,
            unit: str, mode: str, clock_hz: int, name: str,
            mcu: str | None = None) -> list[str]:
    if mode not in ("syntax", "object") or family not in ("stm32", "avr"):
        raise PraxisError("INVALID_PROFILE", "Unsupported compiler family or mode")
    compiler = "arm-none-eabi-gcc" if family == "stm32" else "avr-gcc"
    device_defines = {"STM32F401RE": "STM32F401xE", "STM32F407VGT6": "STM32F407xx"}
    if family == "stm32" and mcu is not None and mcu not in device_defines:
        raise PraxisError("INVALID_PROFILE", "No compiler device definition for this MCU")
    flags = (["-mcpu=cortex-m4", "-mthumb", "-mfloat-abi=soft",
              f"-D{device_defines[mcu or 'STM32F401RE']}"]
             if family == "stm32" else ["-mmcu=atmega328p", f"-DF_CPU={clock_hz}UL"])
    args = ["podman", "run", "--name", name, "--pull=never", "--rm", "--network=none",
            "--http-proxy=false", "--env", "LC_ALL=C",
            "--read-only", "--cap-drop=ALL", "--security-opt=no-new-privileges",
            "--userns=keep-id", "--user", f"{os.getuid()}:{os.getgid()}",
            "--memory=1g", "--memory-swap=1g", "--cpus=1", "--pids-limit=64",
            "--ulimit", "fsize=65536:65536", "--tmpfs", "/tmp:rw,noexec,nosuid,size=64m",
            "--mount", f"type=bind,src={source},dst=/src,ro=true",
            "--mount", f"type=bind,src={headers},dst=/approved,ro=true",
            "--mount", f"type=bind,src={output},dst=/out,rw=true", "--workdir=/out",
            "--entrypoint", f"/usr/bin/{compiler}", _image(image), *flags,
            "-std=c11", "-ffreestanding", "-Wall", "-Wextra", "-Werror", "-fmax-errors=20",
            "-I/approved", "-I/src", "-fsyntax-only" if mode == "syntax" else "-c",
            f"/src/{unit}"]
    if mode == "object":
        args.extend(["-o", f"/out/{digest(unit.encode())[:16]}.o"])
    return args


def bounded(args: list[str], timeout: float, *, cwd: Path | None = None) -> dict:
    """Bound memory and stop the command as soon as diagnostic output exceeds its budget."""
    start = time.monotonic()
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               start_new_session=True, cwd=cwd)
    selector = selectors.DefaultSelector()
    output = bytearray()
    reason = None
    try:
        for pipe in (process.stdout, process.stderr):
            selector.register(pipe, selectors.EVENT_READ)
        while selector.get_map():
            remaining = timeout - (time.monotonic() - start)
            if remaining <= 0:
                reason = "TIMEOUT"
                break
            for key, _ in selector.select(min(remaining, 0.1)):
                chunk = os.read(key.fileobj.fileno(), 8192)
                if not chunk:
                    selector.unregister(key.fileobj)
                elif len(output) + len(chunk) > MAX_DIAGNOSTICS:
                    output.extend(chunk[:MAX_DIAGNOSTICS - len(output)])
                    reason = "OUTPUT_LIMIT"
                    break
                else:
                    output.extend(chunk)
            if reason:
                break
        if reason:
            os.killpg(process.pid, signal.SIGKILL)
        try:
            returncode = process.wait(timeout=max(0.1, timeout - (time.monotonic() - start)))
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            returncode = process.wait()
            reason = "TIMEOUT"
        return {"returncode": returncode, "failure": reason,
                "diagnostics": output.decode("utf-8", errors="replace")}
    finally:
        selector.close()
        process.stdout.close()
        process.stderr.close()
        if process.poll() is None:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()


def verify(bundle_path: Path, source_path: Path, mode: str, lock_path: Path, output: Path) -> dict:
    bundle = Bundle(bundle_path)
    from praxis.targets import require_firmware_target
    require_firmware_target(bundle.manifest.target)
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    image = _image(lock.get("image"))
    if lock.get("schema_version") != 1 or not isinstance(lock.get("headers"), list):
        raise PraxisError("INVALID_LOCK", "Unsupported toolchain lock schema")
    _rootless()
    if output.exists() or output.is_symlink():
        raise PraxisError("OUTPUT_EXISTS", "Choose a new verification output directory")
    # No package installation, registry pulls, or user-provided flags are performed here.
    with tempfile.TemporaryDirectory(prefix="praxis-verify-") as directory:
        root = Path(directory)
        source, headers, artifacts = root / "source", root / "headers", root / "artifacts"
        for path in (source, headers, artifacts):
            path.mkdir()
        units, source_hash = snapshot(source_path, source)
        family = bundle.manifest.target.family
        entries = [h for h in lock["headers"] if h.get("family") == family]
        if not entries:
            raise PraxisError("INVALID_LOCK", f"No approved headers for {family}")
        approved_names = set()
        for entry in entries:
            name = entry["destination"]
            if name in approved_names:
                raise PraxisError("INVALID_LOCK", f"Duplicate approved header: {name}")
            approved_names.add(name)
            contents = read_inside(lock_path.parent.resolve(), entry["path"], 8 * 1024 * 1024)
            if digest(contents) != entry["sha256"]:
                raise PraxisError("INTEGRITY_ERROR", f"Approved header changed: {name}")
            if name != "praxis_sequence.h" and entry["sha256"] not in {s.sha256 for s in bundle.manifest.sources}:
                raise PraxisError("INTEGRITY_ERROR", f"Header {name} is not part of this bundle's pinned sources")
            from praxis.bundle import relative_path
            destination = headers / relative_path(name)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(contents)
        records = []
        deadline = time.monotonic() + 30
        for unit in units:
            name = "praxis-verify-" + uuid.uuid4().hex
            args = command(image, family, source, headers, artifacts, unit, mode,
                           bundle.manifest.target.clock_hz, name, mcu=bundle.manifest.target.mcu)
            try:
                remaining = deadline - time.monotonic()
                result = (bounded(args, remaining) if remaining > 0 else
                          {"returncode": -1, "failure": "TIMEOUT", "diagnostics": "Compilation budget exhausted"})
                records.append({"unit": unit, "command_profile": args[args.index("--entrypoint") + 1:], **result})
            finally:
                # Timeout/output-limit cleanup must also stop a container whose CLI was killed.
                subprocess.run(["podman", "rm", "--force", "--ignore", name],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=10, check=False)
            if result["returncode"] or result["failure"]:
                break
        passed = len(records) == len(units) and all(r["returncode"] == 0 and not r["failure"] for r in records)
        report = {"schema_version": 1, "bundle_revision": bundle.manifest.bundle_revision,
                  "target": bundle.manifest.target.id, "source_sha256": source_hash,
                  "toolchain_image": image, "compiler_identity": lock.get("compiler_versions", {}),
                  "mode": mode, "compile_passed": passed, "records": records,
                  "static_hardware_checks": "Not inferred from compilation; run the golden validation suite",
                  "ordering_evidence": "Not inferred from compilation; instrumented examples are separately tested",
                  "physical_behavior": "Untested; no firmware was executed or flashed"}
        artifacts.joinpath("report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(artifacts, output)
        return report


def build_sandbox(base_image: str, recipe: Path, lock_path: Path) -> str:
    _image(base_image)
    _rootless()
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    if lock.get("image"):
        raise PraxisError("IMMUTABLE_LOCK", "Use a new lock file to provision another toolchain revision")
    tag = "localhost/praxis-toolchain:" + uuid.uuid4().hex
    # Provisioning downloads packages; generated-code builds always use --network=none.
    run(["podman", "build", "--pull=never", "--network=host", "--build-arg", f"BASE_IMAGE={base_image}",
         "--tag", tag, "--file", str(recipe.resolve()), str(recipe.parent.resolve())], timeout=600)
    image = run(["podman", "image", "inspect", "--format", "{{.Id}}", tag], limit=4096).strip()
    # Podman versions differ in whether .Id includes its algorithm prefix.
    if re.fullmatch(r"[0-9a-f]{64}", image):
        image = "sha256:" + image
    lock["image"] = _image(image)
    versions = {}
    for compiler in ("arm-none-eabi-gcc", "avr-gcc"):
        versions[compiler] = run(["podman", "run", "--pull=never", "--rm", "--network=none", "--read-only",
                                  "--cap-drop=ALL", "--security-opt=no-new-privileges",
                                  "--entrypoint", compiler, image, "--version"]).splitlines()[0]
    lock["compiler_versions"] = versions
    staged = lock_path.with_suffix(".tmp")
    staged.write_text(json.dumps(lock, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(staged, lock_path)
    return image

