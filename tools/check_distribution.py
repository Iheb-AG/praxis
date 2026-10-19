"""Check built wheel/sdist contents without extracting or executing archive files."""
from __future__ import annotations

import argparse
import hashlib
import json
import posixpath
import re
import tarfile
import zipfile
from pathlib import Path, PurePosixPath

REQUIRED = {
    'praxis/project_workspace.py', 'tests/test_project_workspace.py', 'docs/project-workspaces.md',
    'praxis/latex_text.py', 'praxis/electrical.py', 'praxis/project_latex.py', 'praxis/project_pdf.py',
    'tests/test_project_documents.py', 'tools/check_project_documents.py',
    'praxis/project_report.py', 'tests/test_project_report.py', 'docs/project-reporting.md',
    'tools/check_project_report_mcp.py',
    *{f'examples/projects/stm32f407-protocol-supervisor/{name}'
      for name in ('project.json', 'README.md', 'PROMPT.md')},
    'praxis/timer_irq_telemetry.py', 'praxis/data/timer-irq-telemetry-v1.json',
    'tests/test_timer_irq.py', 'tests/test_timer_irq_effects.py',
    'tests/fixtures/f407_timer_irq_model.c',
    'docs/timer-irq.md', 'docs/timer-irq-evidence.json',
    'examples/acceptance/stm32f407g-disc1-timer-irq.json',
    'examples/capabilities/stm32f407g-disc1-timer-irq.json',
    'sources/stm32f407g-disc1/profile-timer-irq-v1.json',
    *{f'sources/stm32f407g-disc1/reviewed/timer-irq-v1/{name}'
      for name in ('extension.json', 'evidence.json', 'scb.md', 'nvic.md', 'tim.md')},
    *{f'examples/stm32f407g-disc1-timer/irq_application/{name}'
      for name in ('timer_controller.h', 'routed_timer.h', 'route_scenario.h',
                   'telemetry.h', 'irq_controller.h', 'main.c')},
    'bundles/stm32f407g-disc1-e01-timer-irq-v1/manifest.json',
    'docs/reports/timer-route-results.md', 'docs/timer-route-physical-evidence.json',
    'praxis/timer_route_telemetry.py', 'praxis/data/timer-route-telemetry-v1.json',
    'tests/test_timer_route_telemetry.py', 'tests/fixtures/f407_timer_route_telemetry_model.c',
    'docs/timer-observations.md', 'docs/timer-observations-evidence.json',
    'examples/acceptance/stm32f407g-disc1-timer-observations.json',
    *{f'examples/stm32f407g-disc1-timer/routes_telemetry_application/{name}'
      for name in ('timer_controller.h', 'routed_timer.h', 'route_scenario.h', 'telemetry.h', 'main.c')},
    'tests/test_mode_instance_scopes.py', 'tests/test_timer_routes.py',
    'tests/fixtures/f407_timer_route_model.c',
    'docs/timer-routes.md', 'docs/timer-routes-evidence.json',
    'examples/acceptance/stm32f407g-disc1-timer-routes.json',
    'examples/capabilities/stm32f407g-disc1-timer-routes.json',
    'sources/stm32f407g-disc1/profile-timer-routes-v1.json',
    *{f'sources/stm32f407g-disc1/reviewed/timer-routes-v1/{name}'
      for name in ('extension.json', 'evidence.json', 'pin-evidence.json',
                   'connectivity-evidence.json', 'netlist.json', 'board.json',
                   'tim.md', 'rcc.md', 'gpio.md')},
    *{f'examples/stm32f407g-disc1-timer/routes_application/{name}'
      for name in ('timer_controller.h', 'routed_timer.h', 'main.c')},
    'bundles/stm32f407g-disc1-e01-timer-routes-v1/manifest.json',
    'tests/test_timer_modes.py', 'tests/fixtures/f407_timer_model.c',
    'docs/timer-modes.md', 'docs/timer-modes-evidence.json',
    'examples/stm32f407g-disc1-timer/README.md',
    'examples/acceptance/stm32f407g-disc1-timer.json',
    'examples/capabilities/stm32f407g-disc1-timer.json',
    'sources/stm32f407g-disc1/profile-timer-modes-v1.json',
    *{f'sources/stm32f407g-disc1/reviewed/timer-modes-v1/{name}'
      for name in ('extension.json', 'evidence.json', 'tim.md', 'rcc.md')},
    *{f'examples/stm32f407g-disc1-timer/{application}/{name}'
      for application in ('pwm_application', 'capture_application')
      for name in ('timer_controller.h', 'timer_mmio.h', 'main.c')},
    'bundles/stm32f407g-disc1-e01-timer-modes-v1/manifest.json',
    'tests/test_field_views.py', 'docs/register-field-views.md', 'docs/register-field-views-evidence.json',
    'sources/stm32f407g-disc1/profile-timer-views-v1.json',
    'sources/stm32f407g-disc1/reviewed/timer-views-v1/extension.json',
    'sources/stm32f407g-disc1/reviewed/timer-views-v1/tim.md',
    'examples/inventory/stm32f407g-disc1/timer-views-review.json',
    'bundles/stm32f407g-disc1-e01-timer-views-v1/manifest.json',
    'praxis/inventory_review.py', 'tests/test_inventory_review.py',
    'examples/inventory/stm32f407g-disc1/inventory-v2.json',
    'docs/inventory-reconciliation.md', 'docs/inventory-reconciliation-evidence.json',
    'praxis/adapters/outline.py', 'praxis/capability_inventory.py',
    'tests/test_source_outline.py', 'tests/test_capability_inventory.py',
    'examples/inventory/stm32f407g-disc1/inventory.json',
    *{f'examples/inventory/stm32f407g-disc1/outlines/{name}.json'
      for name in ('rm0090', 'ds8626', 'pm0214', 'es0182')},
    'docs/manufacturer-inventory.md', 'docs/manufacturer-inventory-evidence.json',
    'praxis/acceptance.py', 'tools/check_target_acceptance_mcp.py',
    'examples/acceptance/stm32f407g-disc1.json', 'tests/test_target_acceptance.py',
    'tests/test_union_storage.py', 'docs/f407-full-acceptance.md',
    'docs/f407-full-acceptance-evidence.json',
    'AGENTS.md', 'docs/document-scale.md', 'docs/document-scale-evidence.json',
    'tests/test_large_documents.py', 'tests/test_kicad_pin_names.py', 'tests/test_dependency_policy.py',
    'praxis/contracts.py', 'praxis/compatibility.py', 'praxis/data/legacy-targets.json',
    'praxis/adapters/constraints.py',
    'tests/test_publication_contracts.py', 'docs/compiler-contracts.md',
    'docs/compiler-contracts-evidence.json',
    'vercel.json', '.vercelignore', '.gitattributes', 'website/build.mjs', 'website/package.json',
    'website/README.md', 'website/tests/build.test.mjs', 'website/tests/reader.test.mjs',
    'website/index.html', 'website/vite.config.js', 'website/package-lock.json',
    'website/src/main.jsx', 'website/src/App.jsx', 'website/src/docs.mjs',
    'website/src/MarkdownView.jsx', 'website/src/MermaidDiagram.jsx',
    'website/src/styles.css', 'website/src/branding.css', 'website/scripts/licenses.mjs',
    'website/vercel.json', 'website/documentation-source/docs/README.md',
    'praxis/target_matrix.py', 'praxis/reports.py', 'tests/test_mcu_inventory.py',
    'tests/test_target_matrix.py', 'tests/test_report_companions.py',
    'tests/test_compound_masks.py',
    'docs/stm32-family-expansion.md', 'docs/stm32-family-expansion-evidence.json',
    'examples/opencode.stm32-inventory.example.json', 'sources/stm32-experimental/catalog.json',
    *{f'sources/stm32-experimental/{part}/{name}'
      for part in ('stm32f103c8t6', 'stm32g071rbt6', 'stm32h743zit6')
      for name in ('profile.json', 'acquisition-lock.json', 'definitions.json',
                   'raw/LICENSE-ST.md', 'raw/LICENSE-CMSIS.txt')},
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
    'examples/stm32f407g-disc1-can/README_RX.md',
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
             '.monitor', 'node_modules', '.build-staging', '.generated', 'dist'}


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
    if not {'praxis/telemetry.py', 'praxis/server.py', 'praxis/cli.py', 'praxis/project_report.py',
            'praxis/latex_text.py', 'praxis/electrical.py', 'praxis/project_latex.py', 'praxis/project_pdf.py',
            'praxis/adapters/manual.py', 'praxis/review.py', 'praxis/support.py',
            'praxis/definitions.py', 'praxis/workflow_review.py',
            'praxis/can_telemetry.py', 'praxis/can_diagnostics.py', 'praxis/targets.py',
            'praxis/contracts.py', 'praxis/compatibility.py', 'praxis/data/legacy-targets.json',
            'praxis/adapters/constraints.py', 'praxis/acceptance.py',
            'praxis/adapters/outline.py', 'praxis/capability_inventory.py', 'praxis/inventory_review.py',
            'praxis/timer_route_telemetry.py', 'praxis/data/timer-route-telemetry-v1.json',
            'praxis/timer_irq_telemetry.py', 'praxis/data/timer-irq-telemetry-v1.json'} <= wheel:
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
        archive_members = {member.name: member for member in members if member.isfile()}
        publication_contracts = 0
        for name, member in archive_members.items():
            path = PurePosixPath(name)
            relative = PurePosixPath(*path.parts[1:])
            if (relative.parts[0] != 'sources' or 'contracts' in relative.parts or path.suffix != '.json'
                    or not path.stem.startswith('profile')):
                continue
            profile = json.loads(archive.extractfile(member).read())
            selected = profile.get('compilation_contract')
            policy = next((s for s in profile.get('sources', []) if s['id'] == selected), None)
            if policy is None or policy['authority'] != 'configuration':
                raise ValueError(f'Missing explicit publication policy: {name}')
            target = posixpath.normpath(posixpath.join(str(path.parent), policy['path']))
            artifact = archive_members.get(target)
            if artifact is None or artifact.size > 1024 * 1024:
                raise ValueError(f'Missing or oversized publication policy: {target}')
            if hashlib.sha256(archive.extractfile(artifact).read()).hexdigest() != policy.get('expected_sha256'):
                raise ValueError(f'Publication policy pin mismatch: {target}')
            publication_contracts += 1
        experimental_inputs = 0
        inventory_inputs = 0
        for name, member in archive_members.items():
            path = PurePosixPath(name)
            relative = PurePosixPath(*path.parts[1:]).as_posix()
            if not (relative.startswith('examples/inventory/') and path.name.startswith('inventory')
                    and path.suffix == '.json'):
                continue
            spec = json.loads(archive.extractfile(member).read())
            if spec.get('format') != 'praxis-capability-inventory-v1':
                raise ValueError(f'Unexpected inventory format: {name}')
            for source in [*spec['documents'], *spec.get('supporting_evidence', [])]:
                selected = PurePosixPath(source['path'])
                if selected.is_absolute() or '..' in selected.parts or str(selected) != source['path']:
                    raise ValueError(f'Escaped inventory input: {name}')
                target = str(path.parent / selected)
                artifact = archive_members.get(target)
                if artifact is None:
                    raise ValueError(f'Missing inventory input: {target}')
                if hashlib.sha256(archive.extractfile(artifact).read()).hexdigest() != source['sha256']:
                    raise ValueError(f'Inventory input pin mismatch: {target}')
                inventory_inputs += 1
        for name, member in archive_members.items():
            relative = PurePosixPath(*PurePosixPath(name).parts[1:]).as_posix()
            if (not relative.startswith('sources/stm32-experimental/') or not name.endswith('/profile.json')
                    or '/contracts/' in name):
                continue
            profile = json.loads(archive.extractfile(member).read())
            for source in profile['sources']:
                target = posixpath.normpath(posixpath.join(str(PurePosixPath(name).parent), source['path']))
                artifact = archive_members.get(target)
                if artifact is None or artifact.size > 8 * 1024 * 1024:
                    raise ValueError(f'Missing or oversized experimental input: {target}')
                actual = hashlib.sha256(archive.extractfile(artifact).read()).hexdigest()
                if actual != source.get('expected_sha256'):
                    raise ValueError(f'Experimental source pin mismatch: {target}')
                experimental_inputs += 1
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
                   'stm32f407g-disc1-e01-arm-core-v1', 'stm32f407g-disc1-e01-arm-core-v2',
                   'stm32f103c8t6-inventory-v1', 'stm32g071rbt6-inventory-v1', 'stm32h743zit6-inventory-v1',
                   'stm32f103c8t6-inventory-v2', 'stm32g071rbt6-inventory-v2', 'stm32h743zit6-inventory-v2'):
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
                      'experimental_target_inputs_verified': experimental_inputs,
                      'publication_contracts_verified': publication_contracts,
                      'inventory_inputs_verified': inventory_inputs,
                      'branding_assets_passed': True}, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
