"""Check built wheel/sdist contents without extracting or executing archive files."""
from __future__ import annotations

import argparse
import json
import posixpath
import re
import tarfile
import zipfile
from pathlib import Path, PurePosixPath

REQUIRED = {
    'vercel.json', '.vercelignore', '.gitattributes', 'website/build.mjs', 'website/package.json',
    'website/README.md', 'website/tests/build.test.mjs', 'website/public/index.html',
    'website/public/app.js', 'website/public/styles.css', 'website/public/branding.css',
    'website/public/branding/praxis-logo.png', 'website/public/branding/praxis-background.jpg',
    'docs/vercel-hosting.md',
    'README_DETAILED.md', 'CHANGELOG.md', 'docs/alpha-launch.md', 'docs/images/README.md',
    'docs/images/praxis-banner.jpg', 'docs/images/praxis-logo.png',
    '.github/ISSUE_TEMPLATE/bug-report.yml',
    'Dockerfile', '.dockerignore', 'docs/docker.md', 'docs/docker-evidence.json', 'tools/check_container_mcp.py',
    'examples/opencode.docker.example.json', 'examples/claude-desktop.docker.example.json',
    'docs/arm-core-support.md', 'docs/arm-core-evidence.json', 'docs/experimental-release.md',
    'tests/test_arm_core_modes.py', 'tests/fixtures/f407_arm_core_model.c',
    'examples/opencode.arm-core.example.json', 'examples/capabilities/stm32f407g-disc1-arm-core.json',
    'examples/stm32f407g-disc1-arm-core/README.md',
    'examples/stm32f407g-disc1-arm-core/application/core_controller.h',
    'examples/stm32f407g-disc1-arm-core/application/main.c',
    'sources/stm32f407g-disc1/web-sources-arm-core.json',
    'sources/stm32f407g-disc1/profile-arm-core-v1.json',
    'sources/stm32f407g-disc1/profile-arm-core-v2.json',
    *{f'sources/stm32f407g-disc1/reviewed/arm-core-{version}/{name}'
      for version in ('v1', 'v2') for name in ('extension.json', 'scb.md', 'systick.md',
                                            'rcc.md', 'resolutions.md', 'assets-contract.json')},
    'praxis/targets.py', 'docs/target-adapters.md', 'docs/target-adapters-evidence.json', 'tests/test_target_adapters.py',
    'tools/check_bundle_mcp.py', 'sources/synthetic-cortex-m3/profile.json',
    'sources/synthetic-cortex-m3/raw/demo_m3.h', 'sources/synthetic-cortex-m3/raw/vendor_blocks.h',
    'sources/synthetic-cortex-m3/raw/netlist.xml', 'sources/synthetic-cortex-m3/reviewed/peripherals.json',
    'docs/can-rx-followup.md', 'docs/can-rx-evidence.json', 'docs/reports/can-rx-results.md',
    'examples/opencode.can-rx.example.json', 'tests/test_can_rx_prerequisite.py',
    'tests/fixtures/f407_can_rx_model.c', 'tests/fixtures/f407_can_rx_route_model.c',
    'sources/stm32f407g-disc1/profile-can-rx-v1.json',
    'sources/stm32f407g-disc1/reviewed/can-rx-v1/extension.json',
    'sources/stm32f407g-disc1/reviewed/can-rx-v1/gpio.md',
    'sources/stm32f407g-disc1/reviewed/can-rx-v1/can.md',
    'sources/stm32f407g-disc1/reviewed/can-rx-v1/netlist.json',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/README.md',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/main.c',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/can_rx_route.h',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/can_controller.h',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/telemetry.h',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/clock_setup.h',
    'examples/stm32f407g-disc1-can/telemetry_rx_application/clock_sequence.h',
    'praxis/can_diagnostics.py', 'tests/test_can_diagnostics.py',
    'docs/reports/can-loopback-results.md',
    'praxis/can_telemetry.py', 'tests/test_can_telemetry.py',
    'tests/fixtures/f407_can_publisher.c', 'docs/can-telemetry.md',
    'docs/can-telemetry-evidence.json', 'examples/opencode.can-telemetry.example.json',
    'examples/stm32f407g-disc1-can/telemetry_application/main.c',
    'examples/stm32f407g-disc1-can/telemetry_application/telemetry.h',
    'examples/stm32f407g-disc1-can/telemetry_application/can_controller.h',
    'examples/stm32f407g-disc1-can/telemetry_application/clock_setup.h',
    'examples/stm32f407g-disc1-can/telemetry_application/clock_sequence.h',
    'tests/test_can_modes.py', 'tests/fixtures/f407_can_model.c',
    'docs/can-expansion.md', 'docs/can-expansion-evidence.json',
    'sources/stm32f407g-disc1/profile-can-v1.json',
    'sources/stm32f407g-disc1/reviewed/can-v1/extension.json',
    'sources/stm32f407g-disc1/reviewed/can-v1/can.md',
    'sources/stm32f407g-disc1/reviewed/can-v1/rcc.md',
    'sources/stm32f407g-disc1/reviewed/can-v1/nvic.md',
    'examples/capabilities/stm32f407g-disc1-can.json', 'examples/opencode.can.example.json',
    'examples/stm32f407g-disc1-can/README.md',
    'examples/stm32f407g-disc1-can/application/main.c',
    'examples/stm32f407g-disc1-can/application/can_controller.h',
    'examples/stm32f407g-disc1-can/application/clock_setup.h',
    'examples/stm32f407g-disc1-can/application/clock_sequence.h',
    'tests/test_dac_modes.py', 'tests/fixtures/f407_dac_model.c',
    'docs/dac-expansion.md', 'docs/dac-expansion-evidence.json',
    'sources/stm32f407g-disc1/profile-dac-v1.json',
    'sources/stm32f407g-disc1/reviewed/dac-v1/extension.json',
    'sources/stm32f407g-disc1/reviewed/dac-v1/dac.md',
    'sources/stm32f407g-disc1/reviewed/dac-v1/rcc.md',
    'examples/capabilities/stm32f407g-disc1-dac.json', 'examples/opencode.dac.example.json',
    'examples/stm32f407g-disc1-dac/README.md',
    'examples/stm32f407g-disc1-dac/application/main.c',
    'examples/stm32f407g-disc1-dac/application/dac_controller.h',
    'examples/stm32f407g-disc1-dac/application/clock_setup.h',
    'examples/stm32f407g-disc1-dac/application/clock_sequence.h',
    'tests/test_source_catalog.py', 'tests/test_i2c_modes.py',
    'tests/fixtures/f407_i2c_model.c', 'tools/check_workflow_mcp.py',
    'docs/i2c-expansion.md', 'docs/i2c-expansion-evidence.json',
    'sources/stm32f407g-disc1/profile-i2c-v1.json',
    'sources/stm32f407g-disc1/reviewed/i2c-v1/extension.json',
    'examples/capabilities/stm32f407g-disc1-i2c.json', 'examples/opencode.i2c.example.json',
    'examples/stm32f407g-disc1-i2c/README.md',
    'examples/stm32f407g-disc1-i2c/application/main.c',
    'examples/stm32f407g-disc1-i2c/application/i2c_controller.h',
    'examples/stm32f407g-disc1-i2c/application/clock_setup.h',
    'examples/stm32f407g-disc1-i2c/application/clock_sequence.h',
    'praxis/definitions.py', 'praxis/workflow_review.py',
    'tests/test_definition_extensions.py', 'tests/test_workflow_review.py',
    'tests/test_adc_modes.py', 'tests/fixtures/f407_adc_model.c',
    'tools/check_adc_workflow_mcp.py', 'docs/adc-expansion.md', 'docs/adc-expansion-evidence.json',
    'docs/adc-build-evidence.json',
    'sources/stm32f407g-disc1/profile-adc-v1.json',
    'sources/stm32f407g-disc1/reviewed/adc-v1/extension.json',
    'examples/opencode.adc.example.json',
    'examples/stm32f407g-disc1-adc/README.md',
    'examples/stm32f407g-disc1-adc/application/main.c',
    'examples/stm32f407g-disc1-adc/application/adc_sequence.h',
    'examples/stm32f407g-disc1-adc/application/clock_sequence.h',
    'examples/stm32f407g-disc1-adc/application/clock_setup.h',
    'CONTRIBUTING.md', '.github/PULL_REQUEST_TEMPLATE.md',
    '.github/ISSUE_TEMPLATE/peripheral-mode.md', '.github/ISSUE_TEMPLATE/board-support.md',
    'praxis/support.py', 'tests/test_support.py', 'docs/capability-support.md',
    'docs/capability-support-evidence.json',
    'examples/capabilities/stm32f407g-disc1.json',
    'pyproject.toml', 'uv.lock', 'LICENSE', 'README.md', '.gitignore',
    '.github/workflows/tests.yml', 'sandbox/Containerfile', 'praxis/telemetry.py',
    'tools/check_distribution.py', 'tools/check_firmware_telemetry_mcp.py',
    'praxis/qualification.py', 'praxis/features.py', 'tools/check_feature_modes_mcp.py',
    'praxis/adapters/manual.py', 'praxis/review.py', 'tests/test_manual_review.py',
    'docs/manual-review-compiler.md', 'docs/manual-review-evidence.json',
    'docs/clock-modes.md', 'docs/clock-mode-evidence.json',
    'examples/opencode.clock.example.json', 'tests/test_clock_modes.py',
    'tests/fixtures/f407_clock_model.c',
    'examples/stm32f407g-disc1-clock/application/main.c',
    'examples/stm32f407g-disc1-clock/application/clock_sequence.h',
    'praxis/advisories.py', 'docs/peripheral-modes.md', 'docs/bundle-advisories.md',
    'docs/feature-expansion-evidence.json', 'examples/opencode.features.example.json',
    'examples/stm32f407g-disc1-crc-dma/application/main.c',
    'examples/stm32f407g-disc1-crc-dma/application/word_crc.h',
    'release-review.json', 'toolchain-f407.lock.json', 'toolchain.lock.json',
    'assets/stm32f407vg/manifest.json', 'assets/stm32f407vg/LICENSE-ST.md',
    'assets/stm32f407vg/LICENSE-CMSIS.txt', 'docs/PUBLICATION_READINESS.md',
    'docs/firmware-telemetry.md', 'docs/telemetry-evidence.json', 'docs/mcp-test-prompts.md',
    'examples/opencode.example.json',
    'examples/stm32f407g-disc1-uart-loopback/telemetry_application/main.c',
}
FORBIDDEN = {'.git', '.venv', '.praxis-output', 'temp', 'imports', '__pycache__',
             '.pytest_cache', '.ruff_cache', '.aws', '.codex', '.agents', '.vercel',
             '.monitor', 'node_modules', '.build-staging', 'dist'}


def checked_names(names):
    for name in names:
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or FORBIDDEN.intersection(path.parts):
            raise ValueError(f'Private or escaped archive member: {name}')
        if path.suffix.lower() in {'.pyc', '.elf', '.bin', '.hex', '.map', '.pdf'}:
            raise ValueError(f'Generated binary or raw evidence in source distribution: {name}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    wheels, sdists = list(args.directory.glob('*.whl')), list(args.directory.glob('*.tar.gz'))
    if len(wheels) != 1 or len(sdists) != 1:
        parser.error('Expected exactly one wheel and one source distribution')
    with zipfile.ZipFile(wheels[0]) as archive:
        wheel = set(archive.namelist())
    checked_names(wheel)
    if not {'praxis/telemetry.py', 'praxis/server.py', 'praxis/cli.py',
            'praxis/adapters/manual.py', 'praxis/review.py', 'praxis/support.py',
            'praxis/definitions.py', 'praxis/workflow_review.py',
            'praxis/can_telemetry.py', 'praxis/can_diagnostics.py', 'praxis/targets.py'} <= wheel:
        raise ValueError('Runtime modules missing from wheel')
    with tarfile.open(sdists[0], 'r:gz') as archive:
        members = archive.getmembers()
        documents = {member.name: archive.extractfile(member).read().decode('utf-8')
                     for member in members if member.isfile() and member.name.endswith('.md')
                     and member.size <= 200000}
        branding = {str(PurePosixPath(*PurePosixPath(member.name).parts[1:])):
                    archive.extractfile(member).read(16) for member in members
                    if member.isfile() and member.name.endswith(
                        ('/docs/images/praxis-banner.jpg', '/docs/images/praxis-logo.png'))}
    names = set()
    roots = set()
    for member in members:
        path = PurePosixPath(member.name)
        if not path.parts or path.is_absolute() or '..' in path.parts:
            raise ValueError('Invalid source member path')
        roots.add(path.parts[0])
        if not (member.isfile() or member.isdir()):
            raise ValueError(f'Unexpected link or special archive member: {member.name}')
        names.add(str(PurePosixPath(*path.parts[1:])))
    if len(roots) != 1:
        raise ValueError('Source distribution must have one root')
    checked_names(names)
    missing = REQUIRED - names
    for bundle in ('stm32f401re', 'atmega328p', 'stm32f407vgt6', 'stm32f407g-disc1-e01-m1',
                   'stm32f407g-disc1-e01-discovery-v2', 'stm32f407g-disc1-e01-uart-v1',
                   'stm32f407g-disc1-e01-features-v1', 'stm32f407g-disc1-e01-clock-v1',
                   'stm32f407g-disc1-e01-adc-v1', 'stm32f407g-disc1-e01-i2c-v1',
                   'stm32f407g-disc1-e01-dac-v1', 'stm32f407g-disc1-e01-can-v1',
                   'stm32f407g-disc1-e01-can-rx-v1', 'synthetic-cortex-m3-v1',
                   'stm32f407g-disc1-e01-arm-core-v1', 'stm32f407g-disc1-e01-arm-core-v2'):
        if f'bundles/{bundle}/manifest.json' not in names:
            missing.add(f'bundles/{bundle}/manifest.json')
    if missing:
        raise ValueError('Missing public files: ' + ', '.join(sorted(missing)))
    if (not branding['docs/images/praxis-banner.jpg'].startswith(b'\xff\xd8\xff')
            or not branding['docs/images/praxis-logo.png'].startswith(b'\x89PNG\r\n\x1a\n')):
        raise ValueError('Branding files have invalid image signatures or mismatched extensions')
    broken_links = []
    for name, body in documents.items():
        relative = str(PurePosixPath(*PurePosixPath(name).parts[1:]))
        if relative not in ('README.md', 'README_DETAILED.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'website/README.md') and not relative.startswith(('docs/', 'examples/')):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', body):
            path = target.strip('<>').split('#')[0]
            if not path or ':' in path:
                continue
            destination = posixpath.normpath(posixpath.join(str(PurePosixPath(relative).parent), path))
            if destination not in names and not any(n.startswith(destination + '/') for n in names):
                broken_links.append(f'{relative}: {target}')
    if broken_links:
        raise ValueError('Broken public documentation links: ' + '; '.join(broken_links))
    print(json.dumps({'distribution_contents_passed': True, 'wheel_members': len(wheel),
                      'source_members': len(names), 'private_and_raw_paths_excluded': True,
                      'public_documentation_file_links_passed': True,
                      'branding_assets_passed': True}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
