from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from praxis.errors import PraxisError


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="praxis", description="Local hardware knowledge compiler and MCP server")
    parser.add_argument("--version", action="version", version="project-praxis 0.1.0")
    commands = parser.add_subparsers(dest="command", required=True)
    compile_parser = commands.add_parser("compile", help="Compile reviewed inputs into an immutable bundle")
    compile_parser.add_argument("--profile", required=True, type=Path)
    compile_parser.add_argument("--output", required=True, type=Path)
    matrix_parser = commands.add_parser("compile-matrix", help="Compile registered target profiles independently; offline experimental batch support")
    matrix_parser.add_argument("--catalog", required=True, type=Path)
    matrix_parser.add_argument("--output", required=True, type=Path)
    matrix_parser.add_argument("--target", action="append", help="Exact registered target ID; repeat or omit to compile all")
    coverage_parser = commands.add_parser("coverage", help="Inventory declarations and report workflow publication gaps")
    coverage_parser.add_argument("--profile", required=True, type=Path)
    coverage_parser.add_argument("--output", type=Path, help="New JSON report file; default stdout")
    review_parser = commands.add_parser("prepare-review", help="Prepare unreviewed manual facts checked against declared registers")
    review_parser.add_argument("--profile", required=True, type=Path)
    review_parser.add_argument("--archive", required=True, type=Path)
    review_parser.add_argument("--peripheral", required=True)
    review_parser.add_argument("--register", action="append", help="Exact register name; repeat or omit for the whole entity")
    review_parser.add_argument("--locator", action="append", help="Complete archive part locator; repeat or omit for all parts")
    review_parser.add_argument("--output", required=True, type=Path, help="New candidate JSON; never published operating knowledge")
    features = commands.add_parser("features", help="Read feature/mode coverage from a verified bundle; no ingestion tools needed")
    features.add_argument("--bundle", required=True, type=Path)
    support = commands.add_parser("support", help="Assess scoped knowledge readiness from a verified bundle")
    support.add_argument("--bundle", required=True, type=Path)
    support.add_argument("--catalog", type=Path, help="Optional authored capability scope; not hardware evidence")
    support.add_argument("--workflow", help="Exact declared workflow; exit 1 if knowledge is blocked")
    support.add_argument("--format", choices=("json", "markdown"), default="json")
    project = commands.add_parser("project-report", help="Document a requested firmware project with scoped connectivity and evidence")
    for flag in ("bundle", "spec", "output"):
        project.add_argument("--" + flag, required=True, type=Path)
    project.add_argument("--workspace", type=Path, help="Explicit root for optional UTF-8 project attachments")
    pdf = commands.add_parser("project-pdf", help="Typeset controlled LaTeX/CircuitikZ sources into a new PDF report")
    pdf.add_argument("--report", required=True, type=Path)
    pdf.add_argument("--output", required=True, type=Path)
    inventory_parser = commands.add_parser("inventory", help="Reconcile pinned manufacturer source scope with bundle coverage; not all-mode qualification")
    inventory_parser.add_argument("--bundle", required=True, type=Path)
    inventory_parser.add_argument("--inventory", required=True, type=Path)
    inventory_parser.add_argument("--format", choices=("json", "markdown"), default="json")
    inventory_parser.add_argument("--require-complete", action="store_true", help="Exit 1 while manufacturer-wide inventory review remains incomplete")
    qualify = commands.add_parser("qualify-telemetry", help="Check recorded MCP telemetry against a phase; no hardware access")
    qualify.add_argument("--bundle", required=True, type=Path)
    qualify.add_argument("--artifact", required=True)
    qualify.add_argument("--phase", choices=("failure", "running", "paused"), required=True)
    qualify.add_argument("--observation", required=True, action="append", type=Path)
    qualify.add_argument("--minimum-frames", type=int, default=100)
    qualify.add_argument("--output", type=Path, help="New sanitized JSON report; default stdout")
    can_qualify = commands.add_parser("qualify-can", help="Qualify recorded internal-loopback telemetry; no hardware access")
    can_qualify.add_argument("--bundle", required=True, type=Path)
    can_qualify.add_argument("--artifact", required=True)
    can_qualify.add_argument("--expect", choices=("passed", "failed"), default="passed")
    can_qualify.add_argument("--observation", required=True, action="append", type=Path)
    can_qualify.add_argument("--output", type=Path, help="New sanitized report; default stdout")
    timer_qualify = commands.add_parser("qualify-timer", help="Recompute recorded paired timer capture results; no hardware access")
    timer_qualify.add_argument("--bundle", required=True, type=Path)
    timer_qualify.add_argument("--artifact", required=True)
    timer_qualify.add_argument("--expect", choices=("passed", "timeout", "failed"), default="passed")
    timer_qualify.add_argument("--observation", required=True, action="append", type=Path)
    timer_qualify.add_argument("--output", type=Path, help="New sanitized report; default stdout")
    irq_qualify = commands.add_parser("qualify-timer-irq", help="Qualify recorded timer IRQ receipts and raw periods; no hardware access")
    irq_qualify.add_argument("--bundle", required=True, type=Path)
    irq_qualify.add_argument("--artifact", required=True)
    irq_qualify.add_argument("--expect", choices=("passed", "timeout", "failed"), default="passed")
    irq_qualify.add_argument("--observation", required=True, action="append", type=Path)
    irq_qualify.add_argument("--output", type=Path, help="New sanitized report; default stdout")
    for name in ("lint", "serve", "verify", "evaluate"):
        sub = commands.add_parser(name)
        sub.add_argument("--bundle", required=True, type=Path)
        if name == "verify":
            sub.add_argument("--source", required=True, type=Path)
            sub.add_argument("--mode", choices=("syntax", "object"), default="syntax")
            sub.add_argument("--lock", required=True, type=Path, help="Provisioned immutable toolchain image lock")
            sub.add_argument("--output", required=True, type=Path, help="New directory for report/artifacts")
    provision = commands.add_parser("sandbox-build", help="Build and lock a local rootless toolchain image")
    provision.add_argument("--base-image", required=True)
    provision.add_argument("--recipe", required=True, type=Path)
    provision.add_argument("--lock", required=True, type=Path)
    for name in ("build", "build-serve", "hardware-plan"):
        sub = commands.add_parser(name, help="Optional isolated F407 full-link service")
        for flag in ("bundle", "assets", "workspace", "artifacts", "lock"):
            sub.add_argument("--" + flag, required=True, type=Path)
        if name == "build":
            sub.add_argument("--source", required=True, help="Directory relative to the configured workspace")
        elif name == "build-serve":
            sub.add_argument("--project-reports", type=Path, help="Opt in to immutable project reporting under this output root")
            sub.add_argument("--hardware-profile", type=Path, help="Opt in to read-only ST-LINK inspection")
            sub.add_argument("--hardware-authorization", type=Path, help="Operator scope for target-bound programming/control")
            sub.add_argument("--telemetry-artifact", help="Opt in to fixed ABI SRAM reads for this accepted artifact ID")
            sub.add_argument("--telemetry-kind", choices=("uart-loopback-v1", "can-loopback-v1", "timer-routes-v1", "timer-irq-v1"),
                             default="uart-loopback-v1", help="Explicit built-in ABI; defaults to existing UART ABI")
        else:
            sub.add_argument("--hardware-profile", required=True, type=Path)
            sub.add_argument("--probe-serial", required=True)
            sub.add_argument("--artifact-id", required=True)
            sub.add_argument("--output", required=True, type=Path)
    authorize = commands.add_parser("hardware-authorize", help="Operator-only: record a reviewed programming scope; no target access")
    for flag in ("plan", "output", "audit-root"):
        authorize.add_argument("--" + flag, required=True, type=Path)
    authorize.add_argument("--operator", required=True)
    authorize.add_argument("--board-confirmation", required=True)
    authorize.add_argument("--actions", nargs="+", required=True,
                           choices=("flash", "reset_run", "reset_halt", "halt", "resume"))
    authorize.add_argument("--lifetime-seconds", type=int, default=900)
    authorize.add_argument("--max-control-attempts", type=int, default=6)
    authorize.add_argument("--acknowledge-sector-erase", action="store_true",
                           help="Required with flash: acknowledge complete sector erase and loss of prior contents")
    for name in ("hardware-profile", "hardware-inspect"):
        sub = commands.add_parser(name, help="Provision or use bounded read-only F407 inspection")
        sub.add_argument("--bundle", required=True, type=Path)
        sub.add_argument("--assets", required=True, type=Path)
        if name == "hardware-profile":
            sub.add_argument("--backend", required=True, type=Path, help="Absolute OpenOCD 0.12.x executable")
            sub.add_argument("--output", required=True, type=Path)
        else:
            sub.add_argument("--profile", required=True, type=Path)
            sub.add_argument("--locks", required=True, type=Path)
            sub.add_argument("--probe-serial", help="Absent: enumerate only; present: inspect exact serial")
            sub.add_argument("--diagnostics", action="store_true", help="Read named diagnostics after identity check")
    elf_parser = commands.add_parser("validate-elf", help="Read-only F407 memory/vector validation")
    elf_parser.add_argument("--assets", required=True, type=Path)
    elf_parser.add_argument("--elf", required=True, type=Path)
    scrape_parser = commands.add_parser("scrape", help="Download PDF/HTML/text into unreviewed evidence archives")
    inputs = scrape_parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--url")
    inputs.add_argument("--catalog", type=Path)
    scrape_parser.add_argument("--output", required=True, type=Path)
    scrape_parser.add_argument("--id", dest="source_id")
    scrape_parser.add_argument("--target")
    scrape_parser.add_argument("--title", default="")
    scrape_parser.add_argument("--kind", choices=("auto", "pdf", "html", "text"), default="auto")
    scrape_parser.add_argument("--sha256")
    scrape_parser.add_argument("--allow-host", action="append", default=[])
    scrape_parser.add_argument("--pages", help="One-based PDF pages, e.g. 1-5,51,63; default all")
    scrape_parser.add_argument("--from-file", type=Path, help="Extract locally downloaded bytes; URL is declared provenance")
    review_parser = commands.add_parser("review-import", help="Record an actual review of immutable imported evidence")
    review_parser.add_argument("--import-dir", required=True, type=Path)
    review_parser.add_argument("--reviewer", required=True)
    review_parser.add_argument("--notes-file", required=True, type=Path)
    schema_parser = commands.add_parser("schema", help="Print an ingestion JSON Schema for authoring/validation")
    schema_parser.add_argument("--kind", choices=("profile", "board", "reviewed-netlist", "capability-catalog", "capability-inventory", "definition-extension", "target-matrix", "project"), required=True)
    ingest_server = commands.add_parser("ingest-serve", help="Opt-in source evidence and reviewed publication MCP")
    for flag in ("profile", "catalog", "archive-root", "publication-root"):
        ingest_server.add_argument("--" + flag, required=True, type=Path)
    ingest_server.add_argument("--evidence-archive", action="append", default=[], type=Path,
                               help="Explicit existing evidence archive; repeat as needed")
    args = parser.parse_args(argv)
    try:
        if args.command == "project-pdf":
            from praxis.project_pdf import render_pdf
            print(json.dumps(render_pdf(args.report, args.output), sort_keys=True))
        elif args.command == "project-report":
            from praxis.bundle import Bundle
            from praxis.project_report import parse_spec, write_report
            with args.spec.open("rb") as handle:
                raw = handle.read(1024 * 1024 + 1)
            if len(raw) > 1024 * 1024:
                raise PraxisError("PROJECT_LIMIT", "Select a project specification under 1 MiB")
            print(json.dumps(write_report(Bundle(args.bundle), parse_spec(raw), args.output,
                                          args.workspace), sort_keys=True))
        elif args.command == "prepare-review":
            from praxis.review import prepare_review
            report = prepare_review(args.profile, args.archive, args.peripheral, args.register, args.locator)
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            print(json.dumps({"packet_sha256": report["packet_sha256"], "counts": report["counts"],
                "status": report["status"], "publication_ready": False}, sort_keys=True))
        elif args.command == "ingest-serve":
            from praxis.ingestion_server import create_ingestion_server
            create_ingestion_server(args.profile, args.catalog, args.archive_root,
                args.publication_root, args.evidence_archive).run(transport="stdio")
        elif args.command == "features":
            from praxis.bundle import Bundle
            from praxis.features import from_bundle
            print(json.dumps(from_bundle(Bundle(args.bundle)), sort_keys=True, indent=2))
        elif args.command == "support":
            from praxis.bundle import Bundle
            from praxis.support import assess, markdown
            report = assess(Bundle(args.bundle), args.catalog, args.workflow)
            if args.format == "markdown":
                print(markdown(report), end="")
            else:
                print(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False))
            return 1 if args.workflow and not report["selected_workflow"]["knowledge_ready"] else 0
        elif args.command == "inventory":
            from praxis.bundle import Bundle
            from praxis.capability_inventory import from_spec, markdown
            report = from_spec(Bundle(args.bundle), args.inventory)
            print(markdown(report) if args.format == "markdown" else json.dumps(report, sort_keys=True, indent=2))
            return 1 if args.require_complete and not report["inventory_complete"] else 0
        elif args.command in ("qualify-telemetry", "qualify-can", "qualify-timer", "qualify-timer-irq"):
            from praxis.bundle import Bundle, digest
            from praxis.jsonio import load_json
            from praxis.qualification import qualify_windows
            inputs, hashes = [], []
            for path in args.observation:
                if path.stat().st_size > 256 * 1024:
                    raise PraxisError("EVIDENCE_LIMIT", "Select telemetry JSON files under 256 KiB")
                raw = path.read_bytes()
                if len(raw) > 256 * 1024:
                    raise PraxisError("EVIDENCE_LIMIT", "Telemetry input grew during reading")
                inputs.append(load_json(raw))
                hashes.append(digest(raw))
            revision = Bundle(args.bundle).manifest.bundle_revision
            if args.command == "qualify-can":
                from praxis.can_telemetry import qualify_windows as qualify_can
                report = qualify_can(inputs, artifact_id=args.artifact,
                                     bundle_revision=revision, expected=args.expect)
            elif args.command == "qualify-timer-irq":
                from praxis.timer_irq_telemetry import qualify_windows as qualify_irq
                report = qualify_irq(inputs, artifact_id=args.artifact,
                                     bundle_revision=revision, expected=args.expect)
            elif args.command == "qualify-timer":
                from praxis.timer_route_telemetry import qualify_windows as qualify_timer
                report = qualify_timer(inputs, artifact_id=args.artifact,
                                       bundle_revision=revision, expected=args.expect)
            else:
                report = qualify_windows(inputs, artifact_id=args.artifact,
                    bundle_revision=revision, phase=args.phase, minimum_frames=args.minimum_frames)
            report["input_sha256"] = hashes
            text = json.dumps(report, sort_keys=True, indent=2) + "\n"
            if args.output:
                with args.output.open("x", encoding="utf-8") as handle:
                    handle.write(text)
            else:
                print(text, end="")
            return 0 if report["passed"] else 1
        elif args.command == "compile":
            from praxis.compiler import compile_bundle
            result = compile_bundle(args.profile, args.output)
            print(result)
        elif args.command == "compile-matrix":
            from praxis.target_matrix import compile_matrix
            report = compile_matrix(args.catalog, args.output, args.target)
            print(json.dumps(report, sort_keys=True, indent=2))
            return 0 if report["passed"] else 1
        elif args.command == "coverage":
            import tempfile
            from praxis.bundle import Bundle
            from praxis.compiler import compile_bundle
            with tempfile.TemporaryDirectory(prefix="praxis-coverage-") as directory:
                bundle = Bundle(compile_bundle(args.profile, Path(directory) / "bundle", _coverage_only=True))
                if bundle.manifest.schema_version != 2:
                    raise PraxisError("INVALID_PROFILE", "Configure profile.discovery for a complete coverage inventory")
                from praxis.reports import read_report
                report = json.dumps(read_report(bundle, "coverage"), sort_keys=True, separators=(",", ":")) + "\n"
            if args.output:
                args.output.parent.mkdir(parents=True, exist_ok=True)
                with args.output.open("x", encoding="utf-8") as handle:
                    handle.write(report)
            else:
                print(report, end="")
        elif args.command == "lint":
            from praxis.bundle import Bundle
            from praxis.routing import Session
            bundle = Bundle(args.bundle)
            Session(bundle)
            print(json.dumps({"valid": True, "target": bundle.manifest.target.id,
                              "revision": bundle.manifest.bundle_revision}, sort_keys=True))
        elif args.command == "serve":
            from praxis.server import create_server
            create_server(args.bundle).run(transport="stdio")
        elif args.command == "evaluate":
            from praxis.bundle import Bundle
            from praxis.evaluation import evaluate
            report = evaluate(Bundle(args.bundle))
            print(json.dumps(report, sort_keys=True))
            return 0 if report["passed"] else 1
        elif args.command == "verify":
            from praxis.verify import verify
            report = verify(args.bundle, args.source, args.mode, args.lock, args.output)
            print(json.dumps(report, sort_keys=True))
            return 0 if report["compile_passed"] else 1
        elif args.command == "sandbox-build":
            from praxis.verify import build_sandbox
            print(build_sandbox(args.base_image, args.recipe, args.lock))
        elif args.command in ("build", "build-serve", "hardware-plan"):
            if args.command == "build-serve":
                from praxis.build_server import create_build_server
                create_build_server(args.bundle, args.assets, args.workspace, args.artifacts, args.lock,
                                    args.hardware_profile, args.hardware_authorization,
                                    args.telemetry_artifact, args.telemetry_kind,
                                    args.project_reports).run(transport="stdio")
            else:
                from praxis.firmware_build import BuildService
                service = BuildService(args.bundle, args.assets, args.workspace, args.artifacts, args.lock)
                if args.command == "build":
                    report = service.build(args.source)
                    print(json.dumps(report, sort_keys=True))
                    return 0 if report["image_validated"] else 1
                from praxis.hardware import HardwareService
                from praxis.programming import ProgrammingService, save_plan
                hardware = HardwareService(service.bundle, service.assets, args.hardware_profile,
                                           service.artifacts.parent / "probe-locks")
                connection = hardware.inspect_target(args.probe_serial)["connection_id"]
                plan = ProgrammingService(service, hardware).plan_firmware(args.artifact_id, connection)
                save_plan(plan, args.output)
                print(json.dumps(plan, sort_keys=True))
        elif args.command == "hardware-authorize":
            if "flash" in args.actions and not args.acknowledge_sector_erase:
                parser.error("--actions flash requires --acknowledge-sector-erase")
            from praxis.programming import authorize_plan
            print(authorize_plan(args.plan, args.output, args.audit_root, args.operator,
                                 args.board_confirmation, args.actions, args.lifetime_seconds,
                                 args.max_control_attempts))
        elif args.command == "hardware-profile":
            from praxis.hardware import provision_profile
            print(provision_profile(args.bundle, args.assets, args.backend, args.output))
        elif args.command == "hardware-inspect":
            from praxis.bundle import Bundle
            from praxis.firmware_assets import FirmwareAssets
            from praxis.hardware import HardwareService
            bundle = Bundle(args.bundle)
            hardware = HardwareService(bundle, FirmwareAssets(args.assets, bundle), args.profile, args.locks)
            if args.diagnostics and not args.probe_serial:
                parser.error("--diagnostics requires --probe-serial")
            report = hardware.inspect_target(args.probe_serial) if args.probe_serial else hardware.list_probes()
            if args.diagnostics:
                report = hardware.inspect_execution(report['connection_id'])
            print(json.dumps(report, sort_keys=True))
        elif args.command == "validate-elf":
            from praxis.elf_validation import validate_elf
            from praxis.firmware_assets import FirmwareAssets
            report = validate_elf(args.elf, FirmwareAssets(args.assets))
            print(json.dumps(report, sort_keys=True))
            return 0 if report["valid"] else 1
        elif args.command == "scrape":
            from praxis.web_import import WebSource, scrape, scrape_catalog
            if args.catalog:
                if args.source_id or args.target or args.from_file or args.sha256 or args.allow_host or args.kind != "auto" or args.title:
                    parser.error("Catalog declares source metadata/hosts; only --pages and --output can override it")
                print(json.dumps([str(path) for path in scrape_catalog(args.catalog, args.output, pages=args.pages)]))
            else:
                if not args.source_id or not args.target:
                    parser.error("--url requires --id and --target")
                from urllib.parse import urlsplit
                source = WebSource(id=args.source_id, target=args.target, url=args.url,
                                   kind=args.kind, title=args.title, sha256=args.sha256)
                hosts = [urlsplit(source.url).hostname, *args.allow_host]
                print(scrape(source, args.output, allowed_hosts=hosts, pages=args.pages, from_file=args.from_file))
        elif args.command == "review-import":
            from praxis.web_import import review_import
            print(review_import(args.import_dir, args.reviewer, args.notes_file.read_text(encoding="utf-8")))
        elif args.command == "schema":
            from praxis.board import BoardDefinition
            from praxis.models import DefinitionExtension, Profile, ReviewedSchematic
            from praxis.support import CapabilityCatalog
            from praxis.capability_inventory import InventorySpec
            from praxis.target_matrix import TargetMatrix
            from praxis.project_report import ProjectSpec
            model = {"profile": Profile, "board": BoardDefinition, "reviewed-netlist": ReviewedSchematic,
                     "capability-catalog": CapabilityCatalog, "definition-extension": DefinitionExtension,
                     "target-matrix": TargetMatrix, "capability-inventory": InventorySpec,
                     "project": ProjectSpec}[args.kind]
            print(json.dumps(model.model_json_schema(), indent=2, sort_keys=True))
        return 0
    except PraxisError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except (OSError, ValueError) as exc:
        print(f"INPUT_ERROR: {exc}", file=sys.stderr)
        return 2
