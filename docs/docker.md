# Docker knowledge MCP

The Docker image packages the **read-only knowledge MCP**, including Python and the locked
runtime dependencies. Users need a Docker-compatible Linux-container installation and a
published bundle. No host Python, vector database, cross-compiler, or PDF parser is needed
to serve that bundle. Building the image initially needs registry and Python-package access;
retrieval runs with networking disabled after the image is available locally.

The image does not contain a default board, raw manuals, credentials, probe approvals, firmware
artifacts, or a copy of the working directory. Its default command explicitly serves `/bundle`;
mount exactly the bundle you intend to use there. Startup checks the manifest, hashes, paths,
document sizes, links and dependency graph before exposing any tools.

## Build and launch

From a source checkout containing `Dockerfile`, `.dockerignore` and `uv.lock`:

```bash
docker build --tag project-praxis:0.1.0 .
```

Example launch from Linux/macOS, with the repository as the current directory:

```bash
docker run --rm --init -i --pull=never \
  --network=none --read-only \
  --cap-drop=ALL --security-opt=no-new-privileges \
  --pids-limit=64 --memory=256m --cpus=1 \
  --mount "type=bind,source=$(pwd)/bundles/stm32f407g-disc1-e01-arm-core-v2,target=/bundle,readonly" \
  project-praxis:0.1.0
```

This is a stdio MCP process. A silent terminal waiting for protocol input is expected. Usually
the MCP client launches this command itself; there is no separate server to start manually.
Use `-i` to keep stdin open. Do not add `-t`, detach the container, or publish an HTTP port.
Each launch owns one session and one target revision; restarting resets prerequisite reads.

The container runs as UID/GID `10001:10001`. Bundle directories must be traversable and files
readable by that user; normal public `0755` directories and `0644` files work. An arbitrary
private home-directory mount may not. On Docker Desktop, share the selected bundle directory
with Docker and use its absolute host path. Windows clients use an absolute Windows host path
in the mount argument, with JSON backslashes escaped. Paths containing commas are unsupported
by these `--mount` examples; move the bundle to a path without commas.

The checked-in Python/uv bases use upstream multi-architecture index digests. **Local
verification covers Linux amd64 only**; ARM64, Windows and macOS host workflows need their
own checks before being advertised as tested. Containerization standardizes application
dependencies; it does not eliminate Docker daemon, file sharing, permission or USB constraints.

## Client configuration

Use the actual format for your client:

- [OpenCode configuration](../examples/opencode.docker.example.json): merge the `mcp` entry.
- [Claude Desktop configuration](../examples/claude-desktop.docker.example.json): merge the
  `mcpServers` entry into `claude_desktop_config.json`.

Replace `/absolute/path/to/docker` with the executable available to the client, and replace the
bundle source with your absolute host path. For example this development machine has
`/usr/bin/docker`. Build the image before launching the client: `--pull=never` deliberately
prevents implicit image downloads. Only one `project-praxis` knowledge entry should be enabled
for the selected target; disable an older native entry if it uses a different bundle.

The three tools remain `read_wiki_index`, `read_peripheral_doc` and
`query_schematic_netlist`. Read the index first and confirm the exact target and revision.
Existing HEDG gates, full-document responses and advisories are unchanged.

## What is packaged and what remains separate

| Component | Container status |
| --- | --- |
| Knowledge retrieval MCP | Packaged and tested through Docker stdio |
| Precompiled bundles | Mounted read-only; same image can serve different explicit targets |
| Offline ingestion and web acquisition | Existing native CLI/MCP; ingestion image is future work |
| Isolated F407 firmware build service | Existing Linux/rootless Podman integration; not provisioned in this runtime image |
| ST-LINK programming and telemetry | Existing opt-in host integration; USB/device passthrough is not configured or tested here |

Keep the optional native `project-praxis-build` server if you already use it, selecting the
**same bundle revision** as the Docker knowledge process. This runtime image does not replace
the pinned compiler sandbox. Do not mount a Docker socket or use `--privileged` to make that
bridge work implicitly. A future build-service deployment needs its own explicit architecture
and validation. No hardware action occurs during image build or these protocol checks.

## Verification and release

Maintainers with the Python runtime dependencies installed can reproduce the real protocol check:

```bash
uv run python tools/check_container_mcp.py \
  --image project-praxis:0.1.0 \
  --bundle bundles/stm32f407g-disc1-e01-arm-core-v2 \
  --bundle bundles/atmega328p \
  --output /tmp/praxis-container-report.json
```

The checker compares complete peripheral responses with the host's verified Markdown, tests
exact topology results and errors, repeats a fresh session to check gate reset, serves another
target without changing the image, rejects missing/corrupt bundles without stdout pollution,
and checks non-root execution and unwritable application/bundle paths. The AVR input is an
illustrative fixture, not a claim of physical AVR qualification. Reports record the exact local
image ID. Output files must be new paths. CI builds the image and runs the same check without
publishing it.

The [local acceptance evidence](docker-evidence.json) records 110 successful tool calls across
three sessions, five negative/runtime checks, and 50 passing native routing/protocol regression
tests. The final Linux amd64 image is approximately 250 MB uncompressed. These results are local;
the added GitHub Actions job has not yet run on a hosted repository.

The Docker build context is an allowlist: only runtime Python source, metadata, lock, README,
license and Docker build files reach the daemon. The final stage contains the installed package
and runtime dependencies, without uv or ingestion/test extras. Runtime dependencies are selected
by `uv.lock`; image bytes are not claimed reproducible across builds. Review/update upstream
base digests and the dependency lock deliberately to apply maintenance updates.

The source distribution includes the Docker recipe and configurations. **No registry image has
been published.** After choosing a repository/registry, release automation should build and
check each advertised architecture, publish a versioned image, and record the resulting image
digest. User configurations can then consume that immutable registry digest after an explicit
pull. Current `project-praxis:0.1.0` examples refer to the local build.

Design references: [uv Docker integration](https://docs.astral.sh/uv/guides/integration/docker/)
and [Docker run reference](https://docs.docker.com/reference/cli/docker/container/run/).

**Next:** validate the clean experimental source checkout and onboarding, then prepare the
versioned registry release. Dedicated ingestion/build containers and tested ARM64/Desktop
deployment remain separate follow-ups.
