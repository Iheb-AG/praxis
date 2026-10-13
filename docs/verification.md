# Verification and sandbox provisioning

The production verification runner is separate from MCP retrieval and requires **Linux, rootless
Podman, and a provisioned immutable toolchain image**. It never executes generated firmware or
project build scripts. Native cross-compilation in the test suite runs only checked-in trusted
examples; it is not a fallback for agent-generated C.

## Provision once

Install Podman with rootless user namespaces and cgroup v2 resource limits. Select and pull a
Debian bookworm base using a verified digest. Keep that exact digest in your setup record.
Provisioning requires package download access; subsequent verification uses `--pull=never` and
no network. A Debian snapshot fixes the package universe, and the resulting image ID fixes the
entire installed filesystem. The image also records its installed package versions.

```bash
podman pull docker.io/library/debian@sha256:REPLACE_WITH_VERIFIED_64_HEX_DIGEST
uv run praxis sandbox-build \
  --base-image docker.io/library/debian@sha256:REPLACE_WITH_VERIFIED_64_HEX_DIGEST \
  --recipe sandbox/Containerfile \
  --lock toolchain.lock.json
```

The development locks now record an actually built image and compiler versions. That image
must be installed locally; copying a lock does not install its image. `sandbox-build` records
the actual image ID and compiler versions after a successful
build. It refuses to overwrite a provisioned lock. For another image revision copy the input lock
to a new filename in the repository root, clear its image/compiler fields, and provision that file.

Approved headers are specified relative to the lock's directory, hashed, and matched to the bundle's
pinned source hashes. The local shared example stage helper is separately hash-pinned. Generated
sources do not select header paths or compiler arguments.

## Verify generated C

```bash
uv run praxis verify \
  --bundle bundles/stm32f401re \
  --source examples/stm32f401re \
  --mode object \
  --lock toolchain.lock.json \
  --output .praxis-output/stm32-object-1
```

Use `bundles/atmega328p` and `examples/atmega328p` for AVR. `syntax` uses `-fsyntax-only`;
`object` compiles translation units with `-c`. Both use C11, `-ffreestanding`, `-Wall`,
`-Wextra`, and `-Werror`. ARM selects Cortex-M4/Thumb/soft-float and `STM32F401xE`; AVR selects
`atmega328p` and the reviewed `F_CPU`. The examples intentionally omit startup/linker integration.

Only `.c`/`.h` source snapshots are accepted: no symlinks, arbitrary build files, paths with
unsafe characters, or macro/absolute/traversal includes. Source snapshots are limited to 2 MiB
and 128 files. Standard includes use a small explicit allowlist; local literal includes must
remain relative. Source files and approved headers are mounted read-only. Output has its own
directory and diagnostics are bounded. New verification runs require new output directories.

Containers use no network, no added devices, a read-only root, dropped capabilities, no privilege
escalation, the invoking user's identity, one CPU, 1 GiB memory, 64 processes, and bounded file
sizes. Compilation has a total 30-second budget; output-limit/timeouts trigger container cleanup.
An unavailable rootless/cgroup feature fails closed. There is no registry pull during verification.

Each report records the bundle revision, source hash, image/compiler identity, fixed command
profile, exit status, and diagnostics. Compile success is not automatically labeled as successful
hardware validation, execution-order validation, or physical validation.

The [ARM core extension](arm-core-support.md) executes the same SysTick/SCB controller in a
host register-effect model and the ARM example, tests write/pending/flag/barrier effects, then
uses actual MCP sandbox linking and ELF revalidation. Its current image is unflashed. The
compiler's reviewed write-value masks constrain the operating subset separately from the
common header declaration envelope.

## Tests and repair integration

```bash
uv run pytest
uv run ruff check praxis tests tools server.py
uv run praxis evaluate --bundle bundles/stm32f401re
uv run praxis evaluate --bundle bundles/atmega328p
uv run python tools/release_check.py
```

The evaluation command replays deterministic tool-routing scenarios, not a live model benchmark.
Host register models execute the actual example C to check baud divisors, AF/pin values, preserved
bits, interrupt configuration, and failure paths. Both drivers use the shared stage orchestrator,
whose instrumented test checks ordering and failure short-circuiting. These models do not simulate
oscillator behavior, electrical timing, or every register side effect.

`praxis.repair.repair_loop(verify_callback, repair_callback)` is an optional local integration hook.
It invokes at most three verification attempts, stops on repeated diagnostics, and stops when the
repair callback returns false for missing/unsupported facts. It contains no model calls or shell
interface and does not itself edit files. Callback implementations must edit only generated C;
the knowledge bundle remains immutable. Attempt reports preserve provenance from the verification
callback.

External KiCad/Podman tests skip during ordinary development when the tools/image are missing.
The release checker requires them, a provisioned image, and an independent review record; it does
not convert skipped tests into release approval. Optional F407 full linking and ELF validation
are implemented by the separate [build service](build-service.md). Hardware simulation, flashing,
runtime probes, and automatic trusted interpretation of PDF semantics or schematic geometry are
outside v1. Optional PDF text/table evidence extraction is implemented separately; see
[web ingestion](web-ingestion.md).

