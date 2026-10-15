# Experimental alpha launch preparation

This is a local publication candidate. Nothing in this checklist creates a GitHub repository,
pushes a commit, creates a release, or uploads a container image.

## Public presentation

- Repository landing page: [README.md](../README.md), with original Praxis artwork, static alpha
  badges, a Docker quick start, examples, contribution links and explicit support boundaries.
- Original technical README: [README_DETAILED.md](../README_DETAILED.md), preserved unchanged.
- Release summary: [CHANGELOG.md](../CHANGELOG.md).
- Contributor guide and issue/PR templates: [CONTRIBUTING.md](../CONTRIBUTING.md).
- Full architecture, sequence diagrams and evidence: [documentation index](README.md).
- Code license: [MIT](../LICENSE); retain accompanying third-party notices.

Recommended repository description:

> Experimental vectorless hardware knowledge and MCP tooling for AI-assisted embedded
> development, starting with STM32F407 and Cortex-M4.

Suggested topics: `embedded`, `stm32`, `cortex-m`, `mcp`, `vectorless-rag`, `firmware`, `python`.
These describe the project; they do not establish broad device qualification.

## Prepare the public source

Use the checked source distribution as the public export. The wheel alone does not contain
the board bundles, assets or examples. The complete working directory also contains local
experiments and imported material that are intentionally excluded from publication.

```bash
uv build --out-dir /tmp/praxis-alpha-dist
uv run python tools/check_distribution.py /tmp/praxis-alpha-dist
```

The checker verifies required public files, local Markdown/image links, retained branding,
and private/raw exclusions. Extract the checked source archive into a **new** publishing
directory and initialize Git there. The current workspace's Git metadata is not a normal
publishing checkout. Review the actual file list before the first push; `.gitignore` alone
does not establish that a checkout is safe to publish.

Before upload, finish the existing third-party source/extract rights review described in
[publication readiness](PUBLICATION_READINESS.md). Preserve ST/Arm and other source notices.
The project MIT license does not replace third-party terms.

## Reproduce onboarding from the export

From the clean exported source directory:

```bash
docker build -t project-praxis:0.1.0 .
```

Apply the [Docker client configuration](docker.md) using the exported directory's absolute
bundle path. Read the index, confirm `stm32f407g_disc1_mb997_e01`, query `LED_A` and
`USER_BUTTON`, then follow the declared document prerequisites. This needs no board and
does not flash one. Record the host, image ID, bundle revision and actual responses.

For maintainer protocol checks:

```bash
uv sync --locked
uv run python tools/check_container_mcp.py \
  --image project-praxis:0.1.0 \
  --bundle bundles/stm32f407g-disc1-e01-arm-core-v2 \
  --bundle bundles/atmega328p \
  --output /tmp/praxis-alpha-container-report.json
```

The AVR input is an illustrative isolation fixture, not an additional physically qualified
board. A clean export test on this host is useful evidence but is not a fresh-machine or
cross-platform test. Run the included GitHub Actions checks after pushing to a selected
repository; display a passing-CI badge only once that repository has actual results.

## Publish the experimental alpha

1. Choose the public repository and owner, then push the reviewed source export.
2. Resolve its actual hosted CI failures or record outstanding experimental limits.
3. Create an explicitly labeled prerelease with the changelog, checked source archive,
   target/bundle identity and evidence links. The current Python package version is `0.1.0`;
   the public prerelease tag must be chosen before publishing, not inferred from this draft.
4. Choose a container registry, build/test every architecture being advertised, and publish
   a versioned knowledge image. Record its digest and update the pull instructions; current
   examples refer to a **local** image, not an existing registry artifact.
5. Share one short demonstration and invite bounded contributions. Present physical results
   alongside their exact firmware and limitations. Keep independent-review/qualified-v1 work
   distinct from experimental availability.

## Announcement draft

> Introducing Project Praxis, an experimental hardware knowledge and MCP toolkit for
> AI-assisted embedded development. Starting with STM32F407 and Cortex-M4, Praxis combines
> local vectorless retrieval, source-backed board knowledge, dependency-aware documentation,
> isolated firmware builds and opt-in board interaction. The knowledge MCP runs in Docker.
> Contributions are welcome for reviewed peripheral modes, board mappings, tests and docs.

Add the actual repository URL and demonstration link when they exist. No invented download,
CI, registry, contributor-count or performance claims belong in the announcement.

**Next:** inspect the curated export and complete remaining publication review, create the
GitHub repository, run its hosted checks, then publish the experimental prerelease and image.
