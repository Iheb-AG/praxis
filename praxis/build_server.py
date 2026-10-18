"""Opt-in local build MCP; the knowledge MCP remains strictly read-only."""

from pathlib import Path
from threading import Lock

from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError
from mcp.types import ToolAnnotations

from praxis.errors import PraxisError
from praxis.firmware_build import BuildService


def create_build_server(bundle: Path, assets: Path, workspace: Path, artifacts: Path, lock: Path,
                        hardware_profile: Path | None = None,
                        hardware_authorization: Path | None = None,
                        telemetry_artifact: str | None = None,
                        telemetry_kind: str = 'uart-loopback-v1',
                        project_reports: Path | None = None) -> FastMCP:
    service = BuildService(bundle, assets, workspace, artifacts, lock)
    report_root = None
    if project_reports is not None:
        if project_reports.is_symlink() or project_reports.resolve().is_relative_to(service.bundle.root):
            raise PraxisError('INVALID_PATH', 'Keep project reports outside knowledge bundles; no symlink output root')
        report_root = project_reports.resolve()
    hardware = None
    programming = None
    telemetry = None
    if hardware_authorization and not hardware_profile:
        raise PraxisError('INVALID_AUTHORIZATION', 'Hardware authorization requires a pinned hardware profile')
    if telemetry_artifact and not hardware_profile:
        raise PraxisError('INVALID_PROFILE', 'Telemetry requires a pinned hardware profile')
    if telemetry_kind != 'uart-loopback-v1' and not telemetry_artifact:
        raise PraxisError('INVALID_PROFILE', 'A telemetry kind requires a launch-selected artifact')
    if hardware_profile:
        from praxis.hardware import HardwareService
        from praxis.programming import CONTROLS, ProgrammingService
        hardware = HardwareService(service.bundle, service.assets, hardware_profile,
                                   service.artifacts.parent / 'probe-locks')
        programming = ProgrammingService(service, hardware, hardware_authorization)
        if telemetry_artifact:
            from praxis.telemetry import TelemetryService
            telemetry = TelemetryService(service, hardware, telemetry_artifact, telemetry_kind)
    serial = Lock()
    server = FastMCP('project-praxis-build', log_level='WARNING', instructions=
        'Read the knowledge server first and confirm matching target/bundle revision. Read get_build_profile. '
        'Generate only application C/H inputs in the configured workspace. build_firmware supplies pinned '
        'startup, system, runtime and linker assets. Inspect compiler and ELF validation results separately. '
        'Optional hardware tools enumerate probes and inspect named target diagnostics only. '
        'Choose an exact probe serial, then use its connection_id. plan_firmware is read-only. '
        'Programming/control tools exist only with an operator-provisioned target/artifact scope. '
        'Check each success/failure result; never retry a failed or uncertain flash automatically. '
        'Reset/run may continue after return. Never claim boot or physical success from '
        'compile success, programming/readback success or GPIO latches. '
        'Optional telemetry reads one launch-selected artifact ABI, checks exact image bytes and '
        'returns firmware self-reports; it does not generate stimuli or capture wire traffic. '
        'Optional generate_project_report documents the requested application, cites published facts and '
        'renders scoped connectivity. Report generation never establishes physical acceptance.')
    readonly = ToolAnnotations(readOnlyHint=True, destructiveHint=False, openWorldHint=False)

    def call(operation, *args):
        with serial:
            try:
                return operation(*args)
            except PraxisError as exc:
                raise ToolError(str(exc)) from exc
            except OSError as exc:
                raise ToolError(f'BUILD_IO_ERROR: {exc.strerror}; check local runtime/output permissions') from exc

    @server.tool(annotations=readonly)
    def get_build_profile() -> dict:
        """Return target/revision, pinned assets, memory/clock contract and provisioning status."""
        return {**call(service.profile),
                'hardware_inspection': hardware.describe() if hardware else {'enabled': False},
                'hardware_programming': programming.describe() if programming else {'enabled': False},
                'firmware_telemetry': telemetry.describe() if telemetry else {'enabled': False}}

    @server.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, openWorldHint=False))
    def build_firmware(source_directory: str) -> dict:
        """Build C/H sources relative to the configured workspace in rootless Podman (30s limit).

        No paths outside the workspace, arbitrary compiler flags, scripts or custom startup/linker files.
        Success returns a content-derived artifact_id only after compile and ELF checks pass.
        """
        return call(service.build, source_directory)

    @server.tool(annotations=readonly)
    def validate_firmware(artifact_id: str) -> dict:
        """Recheck a previously accepted artifact's hashes and F407 memory/vector contract."""
        return call(service.validate, artifact_id)

    if report_root is not None:
        def project_documentation(specification, artifact_id):
            import json
            from praxis.bundle import read_inside
            from praxis.project_report import parse_spec, write_report
            spec = parse_spec(specification)
            destination = report_root / spec.id
            if not destination.resolve().is_relative_to(report_root):
                raise PraxisError('INVALID_PATH', 'Project output escapes the configured report root')
            checked = None
            if artifact_id is not None:
                validation = service.validate(artifact_id)
                checked = json.loads(read_inside(service.artifacts / artifact_id, 'report.json', 1024 * 1024))
                checked['validation'] = validation['validation']
            return write_report(service.bundle, spec, destination, service.workspace, checked)

        @server.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, openWorldHint=False))
        def generate_project_report(specification: dict, artifact_id: str | None = None) -> dict:
            """Write HTML/Markdown/SVG and a multi-part LaTeX/CircuitikZ authoring kit for the requested project.

            Supply a praxis-project-v1 spec with this exact target/bundle revision, requirement workflow
            IDs, authored explanations citing registered documents, exact signal/endpoint names, verification
            plans and limitations. Optional files are workspace-relative UTF-8 attachments. An artifact_id
            is revalidated from the configured store; callers cannot submit a success receipt. Output is
            report-root/spec.id and cannot be overwritten. No build, flash or physical acceptance is implied.
            Native PDF typesetting is a separate opt-in local project-pdf CLI; this tool executes no TeX.
            """
            return call(project_documentation, specification, artifact_id)

    if hardware:
        @server.tool(annotations=readonly)
        def list_debug_probes() -> dict:
            """Enumerate ST-LINK USB descriptors without attaching; never auto-select a probe."""
            return call(hardware.list_probes)

        @server.tool(annotations=readonly)
        def inspect_target(probe_serial: str) -> dict:
            """Attach to the exact serial without reset/halt, check family/core/flash/UID, return connection_id.

            Debug attachment affects debug transport; it cannot identify the PCB or exact MCU package.
            """
            return call(hardware.inspect_target, probe_serial)

        @server.tool(annotations=readonly)
        def inspect_execution(connection_id: str) -> dict:
            """Recheck target UID, read approved fault/clock/GPIO samples; no arbitrary commands/addresses.

            PC/SP/LR/xPSR are read only if already halted. Does not identify the running firmware artifact,
            prove optical output, or read SysTick CTRL/DHCSR observation flags.
            """
            return call(hardware.inspect_execution, connection_id)

        @server.tool(annotations=readonly)
        def plan_firmware(artifact_id: str, connection_id: str) -> dict:
            """Read-only target/artifact plan, including complete sectors erased and affected byte range.

            Does not authorize programming. Physical PCB revision/wiring remain unconfirmed.
            """
            return call(programming.plan_firmware, artifact_id, connection_id)

        if telemetry:
            @server.tool(annotations=readonly)
            def read_firmware_telemetry(connection_id: str, samples: int = 2, interval_ms: int = 100) -> dict:
                """Read the launch-selected built-in ABI after exact image checks (UART, CAN or timer).

                1–5 coherent samples, 10–1000ms spacing. No caller address/symbol/artifact,
                halt/reset or memory-write operation. Counters are firmware self-reports.
                """
                return call(telemetry.read, connection_id, samples, interval_ms)

            if telemetry_kind == 'can-loopback-v1':
                @server.tool(annotations=readonly)
                def read_can_diagnostics(connection_id: str) -> dict:
                    """Read fixed CAN1 MCR/MSR after exact-image checks; BTR only with INAK=1.

                    Gate snapshots bracket named reads. No caller address/register, FIFO action,
                    reset, halt or write. Requires the reviewed CAN/RCC bundle layout.
                    """
                    return call(telemetry.read_can_diagnostics, connection_id)

        if hardware_authorization:
            mutating = ToolAnnotations(readOnlyHint=False, destructiveHint=True,
                                       idempotentHint=False, openWorldHint=False)

            if 'flash' in programming.authorization.actions:
                @server.tool(annotations=mutating)
                def flash_firmware(artifact_id: str, connection_id: str) -> dict:
                    """Reset/halt, erase ONLY approved sectors, program checked ELF bytes, compare readback.

                    Requires local operator scope. Success leaves target halted; never retries failures.
                    Inspect success/failure and limits. Sector contents outside the image are erased.
                    """
                    return call(programming.flash_firmware, artifact_id, connection_id)

            if set(programming.authorization.actions) & CONTROLS:
                @server.tool(annotations=mutating)
                def control_execution(artifact_id: str, connection_id: str, operation: str,
                                      observation_ms: int = 500) -> dict:
                    """After exact flash-byte verification, perform an authorized reset_run/reset_halt/halt/resume.

                    Observation window 0–5000ms. Running firmware may continue after return and expiry.
                    No arbitrary commands, addresses, breakpoints or stepping. Reports do not prove boot.
                    """
                    return call(programming.control_execution, artifact_id, connection_id, operation, observation_ms)

    return server
