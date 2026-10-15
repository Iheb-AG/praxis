"""Opt-in F407 programming/control. Read-only planning is always separate from authorization.

No arbitrary paths, scripts, addresses or target changes are accepted from MCP arguments.
Authorization is provisioned by the local operator, never by a tool in this server.
"""

from __future__ import annotations

import io
import json
import math
import os
import struct
import time
import uuid
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from praxis.bundle import digest, read_inside
from praxis.elf_validation import validate_bytes
from praxis.errors import PraxisError
from praxis.firmware_build import BuildService
from praxis.hardware import (HardwareService, check_target, configuration,
    halted_core_register_script, parse_observation, read_script)
from praxis.verify import bounded

HEX64 = r'^[0-9a-f]{64}$'
Action = Literal['flash', 'reset_run', 'reset_halt', 'halt', 'resume']
CONTROLS = {'reset_run', 'reset_halt', 'halt', 'resume'}
# RM0090: single-bank 1 MiB STM32F405/407 sector organization.
SECTOR_SIZES = (16384,) * 4 + (65536,) + (131072,) * 7
MUTATION_LIMITS = [
    'Programming erases complete listed sectors, including bytes outside the image; no preservation/rollback.',
    'Flash resets and halts the MCU; approved backend writes flash/debug controller state.',
    'Timeout/disconnect may leave partially programmed flash and an unknown or halted target; no automatic retry.',
    'Reset/run and resume can continue executing firmware after the observation window and authorization expiry.',
    'Readback verifies image bytes, not startup, pin wiring, optical output, timing or application correctness.',
    'Family/UID checks cannot identify the exact MCU package, physical PCB revision or solder bridge state.',
]


def canonical_hash(value: dict, key: str) -> str:
    return digest(json.dumps({k: v for k, v in value.items() if k != key},
                             sort_keys=True, separators=(',', ':')).encode())


def sync_directory(path: Path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def durable_directories(path: Path):
    missing = []
    current = path
    while not current.exists():
        missing.append(current)
        current = current.parent
    for directory in reversed(missing):
        directory.mkdir(mode=0o700, exist_ok=True)
        sync_directory(directory.parent)


def exclusive_json(path: Path, value: dict):
    durable_directories(path.parent)
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w', encoding='utf-8') as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + '\n')
        handle.flush()
        os.fsync(handle.fileno())
    sync_directory(path.parent)


def save_plan(value: dict, output: Path):
    exclusive_json(output, checked_plan(value).model_dump())


class FlashPlan(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    schema_version: Literal[1] = 1
    plan_revision: str = Field(pattern=HEX64)
    artifact_id: str = Field(pattern=HEX64)
    elf_sha256: str = Field(pattern=HEX64)
    image_sha256: str = Field(pattern=HEX64)
    bundle_revision: str = Field(pattern=HEX64)
    asset_revision: str = Field(pattern=HEX64)
    hardware_profile_revision: str = Field(pattern=HEX64)
    probe_serial: str = Field(pattern=r'^[A-Za-z0-9_-]{1,64}$')
    target_uid: str = Field(pattern=r'^[0-9a-f]{24}$')
    image_start: Literal[0x08000000]
    image_length: int = Field(ge=392, le=1024 * 1024)
    erase_start: Literal[0x08000000]
    erase_length: int = Field(ge=16384, le=1024 * 1024)
    last_sector: int = Field(ge=0, le=11)
    physical_board_revision: str | None
    limits: list[str]


class Authorization(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    schema_version: Literal[1] = 1
    authorization_revision: str = Field(pattern=HEX64)
    nonce: str = Field(pattern=r'^[0-9a-f]{32}$')
    plan: FlashPlan
    operator: str = Field(min_length=1, max_length=128)
    board_confirmation: str = Field(min_length=3, max_length=1024)
    created_at: int
    expires_at: int
    actions: list[Action] = Field(min_length=1, max_length=5)
    max_flash_attempts: Literal[0, 1] = 1
    max_control_attempts: int = Field(ge=0, le=16)
    audit_root: str


@dataclass(frozen=True)
class Image:
    data: bytes
    elf_sha256: str
    last_sector: int
    erase_length: int


def image_from_elf(data: bytes, assets) -> Image:
    """Construct programmed bytes from validated PT_LOAD physical addresses, not an unchecked .bin."""
    from elftools.elf.elffile import ELFFile

    validation = validate_bytes(data, assets)
    if not validation['valid']:
        raise PraxisError('IMAGE_REJECTED', 'ELF failed the approved memory/vector/startup contract')
    elf = ELFFile(io.BytesIO(data))
    segments = sorted((s['p_paddr'], s.data()) for s in elf.iter_segments()
                      if s['p_type'] == 'PT_LOAD' and s['p_filesz'])
    if not segments or segments[0][0] != assets.flash[0]:
        raise PraxisError('IMAGE_REJECTED', 'Flash load image must begin at the approved vector address')
    end = assets.flash[0]
    for address, contents in segments:
        if address < end or address + len(contents) > sum(assets.flash):
            raise PraxisError('IMAGE_REJECTED', 'Overlapping or out-of-range physical load segments')
        end = address + len(contents)
    image = bytearray(b'\xff' * (end - assets.flash[0]))
    for address, contents in segments:
        offset = address - assets.flash[0]
        image[offset:offset + len(contents)] = contents
    erase_length = 0
    for last_sector, size in enumerate(SECTOR_SIZES):
        erase_length += size
        if erase_length >= len(image):
            return Image(bytes(image), digest(data), last_sector, erase_length)
    raise PraxisError('IMAGE_REJECTED', 'Image exceeds the supported 1 MiB flash organization')


def checked_plan(value: dict) -> FlashPlan:
    try:
        plan = FlashPlan.model_validate(value)
    except ValidationError as exc:
        raise PraxisError('INVALID_FLASH_PLAN', str(exc)) from exc
    if (canonical_hash(plan.model_dump(), 'plan_revision') != plan.plan_revision
            or plan.erase_length != sum(SECTOR_SIZES[:plan.last_sector + 1])
            or plan.image_length > plan.erase_length
            or (plan.last_sector and plan.image_length <= sum(SECTOR_SIZES[:plan.last_sector]))):
        raise PraxisError('INVALID_FLASH_PLAN', 'Plan hash or sector boundaries are inconsistent')
    return plan


def authorize_plan(plan_path: Path, output: Path, audit_root: Path, operator: str,
                   board_confirmation: str, actions: list[str], lifetime: int = 900,
                   max_controls: int = 6) -> str:
    """Operator-only CLI authoring; does not attach, reset or flash a board."""
    try:
        plan = checked_plan(json.loads(read_inside(plan_path.parent.resolve(), plan_path.name, 65536)))
        if (not 1 <= lifetime <= 3600 or not actions or len(set(actions)) != len(actions)
                or (set(actions) & CONTROLS and max_controls == 0)):
            raise PraxisError('INVALID_AUTHORIZATION', 'Use unique allowed actions, a 1–3600 second lifetime and a positive budget for requested controls')
        now = math.floor(time.time())
        value = Authorization(authorization_revision='0' * 64, nonce=uuid.uuid4().hex, plan=plan,
            operator=operator, board_confirmation=board_confirmation, created_at=now,
            expires_at=now + lifetime, actions=actions, max_flash_attempts=int('flash' in actions),
            max_control_attempts=max_controls,
            audit_root=str(audit_root.resolve())).model_dump()
    except (ValidationError, ValueError) as exc:
        raise PraxisError('INVALID_AUTHORIZATION', str(exc)) from exc
    value['authorization_revision'] = canonical_hash(value, 'authorization_revision')
    exclusive_json(output, value)
    return value['authorization_revision']


def mutation_configuration(serial: str, product: int, flash: bool) -> str:
    cfg = configuration(serial, product)
    cfg += 'cortex_m reset_config sysresetreq\n'
    if flash:
        cfg += 'flash bank praxis.flash stm32f2x 0x08000000 0 0 0 praxis.cpu\n'
    return cfg


def verify_script(image: bytes, *, detail: bool = False, confirm_mismatch: bool = False) -> list[str]:
    """Exact bounded reads, no target-side checksum algorithm or unchecked CRC shortcut."""
    commands = []
    for offset in range(0, len(image), 256):
        block = image[offset:offset + 256]
        words = len(block) // 4
        for start, width, expected in [
            (offset, 32, struct.unpack('<' + 'I' * words, block[:words * 4])),
            (offset + words * 4, 8, tuple(block[words * 4:]))]:
            if not expected:
                continue
            values = ' '.join(hex(value) for value in expected)
            commands += [f'set observed [read_memory 0x{0x08000000 + start:08x} {width} {len(expected)}]',
                f'if {{[llength $observed] != {len(expected)}}} {{ error "PRAXIS_READBACK_MISMATCH" }}']
            if detail or confirm_mismatch:
                commands.append(f'set praxis_verify_address 0x{0x08000000 + start:08x}')
            commands.append(f'foreach actual $observed expected {{{values}}} {{')
            if confirm_mismatch:
                commands += ['  if {$actual != $expected} {',
                    f'    set scalar [lindex [read_memory $praxis_verify_address {width} 1] 0]',
                    f'    set confirmation [lindex [read_memory $praxis_verify_address {width} 1] 0]',
                    '    if {$scalar != $expected || $confirmation != $expected} { error [format "PRAXIS_READBACK_MISMATCH: address=0x%08x actual=0x%08x expected=0x%08x scalar=0x%08x" $praxis_verify_address $actual $expected $scalar] }',
                    '    echo [format "PRAXIS_FLASH_WORD_RECHECK|0x%08x" $praxis_verify_address]',
                    '  }', f'  incr praxis_verify_address {width // 8}']
            elif detail:
                commands += [f'  if {{$actual != $expected}} {{ set scalar [lindex [read_memory $praxis_verify_address {width} 1] 0]; error [format "PRAXIS_READBACK_MISMATCH: address=0x%08x actual=0x%08x expected=0x%08x scalar=0x%08x" $praxis_verify_address $actual $expected $scalar] }}',
                             f'  incr praxis_verify_address {width // 8}']
            else:
                commands.append('  if {$actual != $expected} { error "PRAXIS_READBACK_MISMATCH" }')
            commands.append('}')
    return [*commands, 'echo PRAXIS_IMAGE_VERIFIED']


def mutation_script(uid: str, action: str, image: Image, run_ms: int) -> str:
    if action not in {'flash', *CONTROLS} or not isinstance(run_ms, int) or not 0 <= run_ms <= 5000:
        raise PraxisError('INVALID_OPERATION', 'Choose a registered operation and observation window of 0–5000 ms')
    # Identity and UID guards execute in this SAME process before any halt/reset/erase.
    prefix = read_script(False, uid).split('echo "PRAXIS|state|', 1)[0]
    commands = [prefix.rstrip()]
    if action == 'flash':
        commands += ['echo PRAXIS_PHASE_RESET', 'reset halt', 'wait_halt 2000',
                     'echo PRAXIS_PHASE_ERASE', 'flash probe 0',
                     f'flash erase_sector 0 0 {image.last_sector}',
                     'echo PRAXIS_PHASE_PROGRAM', 'flash write_image image.bin 0x08000000 bin',
                     f'dump_image readback.bin 0x08000000 {len(image.data)}',
                     'echo PRAXIS_OPERATION_COMPLETE']
    else:
        # Verify exact approved bytes before execution control; no unverified reset/run fallback.
        commands += ['echo PRAXIS_PHASE_VERIFY', *verify_script(image.data), 'echo PRAXIS_PHASE_CONTROL']
        commands += {'reset_run': ['reset run'], 'reset_halt': ['reset halt', 'wait_halt 2000'],
                     'halt': ['halt 2000', 'wait_halt 2000'], 'resume': ['poll', 'resume']}[action]
        if action in {'reset_run', 'resume'} and run_ms:
            commands.append(f'sleep {run_ms}')
        commands += ['poll', 'echo PRAXIS_OPERATION_COMPLETE']
    commands += ['echo "PRAXIS|state|[praxis.cpu curstate]"',
                 *halted_core_register_script(), 'shutdown']
    return '\n'.join(commands) + '\n'


class ProgrammingService:
    def __init__(self, build: BuildService, hardware: HardwareService, authorization: Path | None = None):
        self.build, self.hardware = build, hardware
        self.authorization = None
        self.authorization_path = authorization
        if authorization:
            try:
                grant = Authorization.model_validate_json(read_inside(authorization.parent.resolve(), authorization.name, 65536))
                checked_plan(grant.plan.model_dump())
            except ValidationError as exc:
                raise PraxisError('INVALID_AUTHORIZATION', str(exc)) from exc
            if (canonical_hash(grant.model_dump(), 'authorization_revision') != grant.authorization_revision
                    or not Path(grant.audit_root).is_absolute() or len(set(grant.actions)) != len(grant.actions)
                    or grant.max_flash_attempts != int('flash' in grant.actions)
                    or (set(grant.actions) & CONTROLS and grant.max_control_attempts == 0)
                    or not 0 < grant.expires_at - grant.created_at <= 3600):
                raise PraxisError('INVALID_AUTHORIZATION', 'Authorization hash, audit root or scope is invalid')
            for path in (authorization.resolve(), Path(grant.audit_root).resolve()):
                if path.is_relative_to(build.workspace):
                    raise PraxisError('INVALID_AUTHORIZATION', 'Keep operator authorization and audit records outside the generated-source workspace')
            if (grant.plan.bundle_revision != build.bundle.manifest.bundle_revision
                    or grant.plan.asset_revision != build.assets.identity
                    or grant.plan.hardware_profile_revision != hardware.profile.profile_revision):
                raise PraxisError('TARGET_MISMATCH', 'Authorization belongs to different bundle/assets/backend')
            self.authorization = grant

    def describe(self) -> dict:
        grant = self.authorization
        return {'enabled': grant is not None, 'planning_enabled': True,
                'authorization_revision': grant.authorization_revision if grant else None,
                'artifact_id': grant.plan.artifact_id if grant else None,
                'expires_at': grant.expires_at if grant else None,
                'max_flash_attempts': grant.max_flash_attempts if grant else 0,
                'max_control_attempts': grant.max_control_attempts if grant else 0,
                'actions': grant.actions if grant else [], 'limits': MUTATION_LIMITS}

    def snapshot_image(self, artifact_id: str) -> Image:
        result = self.build.validate(artifact_id)
        if not result['validation']['valid']:
            raise PraxisError('IMAGE_REJECTED', 'Artifact no longer passes image validation')
        elf = read_inside(self.build.artifacts / artifact_id, 'firmware.elf', 8 * 1024 * 1024)
        if digest(elf) != result['validation']['elf_sha256']:
            raise PraxisError('INTEGRITY_ERROR', 'ELF changed during the validated snapshot')
        return image_from_elf(elf, self.build.assets)

    def connection(self, connection_id: str) -> tuple[str, str]:
        if connection_id not in self.hardware.connections:
            raise PraxisError('UNKNOWN_CONNECTION', 'Call inspect_target first in this server process')
        return self.hardware.connections[connection_id]

    def make_plan(self, artifact_id: str, connection_id: str, image: Image) -> FlashPlan:
        serial, uid = self.connection(connection_id)
        value = FlashPlan(plan_revision='0' * 64, artifact_id=artifact_id,
            elf_sha256=image.elf_sha256, image_sha256=digest(image.data),
            bundle_revision=self.build.bundle.manifest.bundle_revision, asset_revision=self.build.assets.identity,
            hardware_profile_revision=self.hardware.profile.profile_revision, probe_serial=serial,
            target_uid=uid, image_start=0x08000000, image_length=len(image.data),
            erase_start=0x08000000, erase_length=image.erase_length, last_sector=image.last_sector,
            physical_board_revision=self.hardware.profile.physical_board_revision,
            limits=MUTATION_LIMITS).model_dump()
        value['plan_revision'] = canonical_hash(value, 'plan_revision')
        return checked_plan(value)

    def plan_firmware(self, artifact_id: str, connection_id: str) -> dict:
        self.connection(connection_id)
        image = self.snapshot_image(artifact_id)
        serial, uid = self.connection(connection_id)
        probe = self.hardware.select(serial)
        with self.hardware.probe_lock(serial):
            try:
                observation, _ = self.hardware.observe(probe, False, uid)
            except PraxisError as exc:
                if exc.code in {'TARGET_CHANGED', 'TARGET_MISMATCH'}:
                    self.hardware.connections.pop(connection_id, None)
                raise
            if check_target(observation)['uid'] != uid:
                self.hardware.connections.pop(connection_id, None)
                raise PraxisError('TARGET_CHANGED', 'MCU identity changed; obtain a fresh preflight')
        return self.make_plan(artifact_id, connection_id, image).model_dump()

    def check_authorization(self, action: str, plan: FlashPlan) -> Authorization:
        grant = self.authorization
        if not grant:
            raise PraxisError('AUTHORIZATION_REQUIRED', 'Review plan_firmware and provision a local operator authorization before programming/control')
        raw = read_inside(self.authorization_path.parent.resolve(), self.authorization_path.name, 65536)
        try:
            current = Authorization.model_validate_json(raw)
        except ValidationError as exc:
            raise PraxisError('INVALID_AUTHORIZATION', 'Authorization changed; stop and restart with a reviewed scope') from exc
        if current != grant:
            raise PraxisError('INVALID_AUTHORIZATION', 'Authorization changed during this session')
        if action not in grant.actions:
            raise PraxisError('OPERATION_NOT_AUTHORIZED', 'Requested action is outside the operator-approved scope')
        if not grant.created_at <= time.time() < grant.expires_at:
            raise PraxisError('AUTHORIZATION_EXPIRED', 'Authorization expired or is not yet valid; obtain a reviewed new scope')
        if plan != grant.plan:
            raise PraxisError('AUTHORIZATION_MISMATCH', 'Probe, MCU UID, artifact bytes or flash plan differ from the approved scope')
        return grant

    def reserve_attempt(self, grant: Authorization, action: str, run_id: str) -> Path:
        import fcntl

        root = Path(grant.audit_root) / grant.authorization_revision
        durable_directories(root)
        fd = os.open(root / 'budget.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise PraxisError('AUTHORIZATION_BUSY', 'Another process is reserving this scope; no operation started') from exc
            self.check_authorization(action, grant.plan)
            kind, maximum = ('flash', grant.max_flash_attempts) if action == 'flash' else ('control', grant.max_control_attempts)
            used = len(list(root.glob(kind + '-*.json')))
            if used >= maximum:
                raise PraxisError('OPERATION_BUDGET', 'Approved attempt budget exhausted; failed/uncertain attempts are not retried automatically')
            path = root / f'{kind}-{used:02d}-{run_id}.json'
            attempt = {'run_id': run_id, 'authorization_revision': grant.authorization_revision,
                       'action': action, 'started_at': datetime.now(UTC).isoformat(),
                       'status': 'reserved; result unknown until report is recorded'}
            out = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
            with os.fdopen(out, 'w') as handle:
                handle.write(json.dumps(attempt, sort_keys=True) + '\n')
                handle.flush()
                os.fsync(handle.fileno())
            sync_directory(root)
            return path
        finally:
            os.close(fd)

    def operate(self, action: str, artifact_id: str, connection_id: str, run_ms: int = 500) -> dict:
        if action not in {'flash', *CONTROLS} or type(run_ms) is not int or not 0 <= run_ms <= 5000:
            raise PraxisError('INVALID_OPERATION', 'Use flash, reset_run, reset_halt, halt or resume; observation window 0–5000 ms')
        if not self.authorization:
            raise PraxisError('AUTHORIZATION_REQUIRED', 'No programming/control scope has been provisioned')
        self.connection(connection_id)
        image = self.snapshot_image(artifact_id)
        plan = self.make_plan(artifact_id, connection_id, image)
        grant = self.check_authorization(action, plan)
        probe = self.hardware.select(plan.probe_serial)
        run_id = uuid.uuid4().hex
        report = {'run_id': run_id, 'action': action, 'artifact_id': artifact_id,
            'elf_sha256': image.elf_sha256, 'image_sha256': digest(image.data),
            'plan_revision': plan.plan_revision, 'authorization_revision': grant.authorization_revision,
            'bundle_revision': plan.bundle_revision, 'asset_revision': plan.asset_revision,
            'hardware_profile_revision': plan.hardware_profile_revision,
            'observed_at': datetime.now(UTC).isoformat(), 'success': False,
            'readback_verified': False, 'execution_state': 'unknown', 'physical_behavior': 'not tested',
            'observation_window_ms': run_ms if action in {'resume', 'reset_run'} else 0,
            'limits': MUTATION_LIMITS}
        with self.hardware.probe_lock(plan.probe_serial):
            self.hardware.verify_backend()
            # Persist the attempt BEFORE backend launch; uncertain results consume the budget.
            audit = self.reserve_attempt(grant, action, run_id)
            try:
                result = self.run_backend(probe, plan.target_uid, action, image, run_ms,
                                          grant.expires_at)
                report.update(result)
            except (OSError, PraxisError) as exc:
                report['failure'] = exc.code if isinstance(exc, PraxisError) else 'HARDWARE_IO_ERROR'
                report['diagnostics'] = str(exc)
            report['finished_at'] = datetime.now(UTC).isoformat()
            report['run_continues_after_return'] = report['execution_state'] in {'running', 'debug-running'}
            result_path = audit.with_suffix('.result')
            try:
                exclusive_json(result_path, report)
            except OSError as exc:
                raise PraxisError('AUDIT_FAILED', 'Operation may have occurred; persistent attempt remains consumed. Do not retry; inspect the target and filesystem.') from exc
        if report.get('failure') in {'TARGET_CHANGED', 'TARGET_MISMATCH'}:
            self.hardware.connections.pop(connection_id, None)
        return report

    def run_backend(self, probe: dict, uid: str, action: str, image: Image, run_ms: int, expires_at: int) -> dict:
        import tempfile

        with tempfile.TemporaryDirectory(prefix='praxis-program-') as directory:
            root = Path(directory)
            (root / 'attach.cfg').write_text(mutation_configuration(probe['serial'], probe['product_id'], action == 'flash'))
            (root / 'operate.tcl').write_text(mutation_script(uid, action, image, run_ms))
            (root / 'image.bin').write_bytes(image.data)
            timeout = min(30, expires_at - time.time())
            if timeout <= 0:
                raise PraxisError('AUTHORIZATION_EXPIRED', 'Scope expired before backend launch; no operation requested')
            result = bounded([str(self.hardware.backend), '-f', str(root / 'attach.cfg'),
                              '-f', str(root / 'operate.tcl')], timeout, cwd=root)
            answer = {'diagnostics': result['diagnostics'], 'failure': result['failure'],
                      'success': False, 'readback_verified': False, 'execution_state': 'unknown'}
            if result['failure']:
                return answer
            if result['returncode']:
                answer['failure'] = next((code for marker, code in [
                    ('PRAXIS_TARGET_CHANGED', 'TARGET_CHANGED'), ('PRAXIS_TARGET_MISMATCH', 'TARGET_MISMATCH'),
                    ('PRAXIS_READBACK_MISMATCH', 'READBACK_MISMATCH')]
                    if marker in result['diagnostics']), 'BACKEND_OPERATION_FAILED')
                return answer
            if result['diagnostics'].splitlines().count('PRAXIS_OPERATION_COMPLETE') != 1:
                raise PraxisError('BACKEND_PROTOCOL', 'Backend did not record operation completion')
            values = parse_observation(result['diagnostics'], False, core_registers=True)
            if check_target(values)['uid'] != uid:
                raise PraxisError('TARGET_CHANGED', 'Returned identity differs from preflight')
            if action == 'flash':
                readback = read_inside(root, 'readback.bin', len(image.data))
                if readback != image.data:
                    answer['failure'] = 'READBACK_MISMATCH'
                    return answer
                if values['state'] != 'halted':
                    raise PraxisError('BACKEND_PROTOCOL', 'Programming did not leave the target halted as requested')
            elif values['state'] != ('halted' if action in {'halt', 'reset_halt'} else 'running'):
                answer['failure'] = 'UNEXPECTED_EXECUTION_STATE'
                answer['execution_state'] = values['state']
                return answer
            if action != 'flash' and result['diagnostics'].splitlines().count('PRAXIS_IMAGE_VERIFIED') != 1:
                raise PraxisError('BACKEND_PROTOCOL', 'Execution control did not record exact image verification')
            return {**answer, 'success': True, 'readback_verified': True,
                    'execution_state': values['state'],
                    'core_registers': {name: hex(values[name]) for name in ('pc', 'sp', 'lr', 'xpsr') if name in values},
                    'programmed_range': {'start': 0x08000000, 'length': len(image.data)} if action == 'flash' else None,
                    'erased_range': {'start': 0x08000000, 'length': image.erase_length} if action == 'flash' else None}

    def flash_firmware(self, artifact_id: str, connection_id: str) -> dict:
        return self.operate('flash', artifact_id, connection_id, 0)

    def control_execution(self, artifact_id: str, connection_id: str, operation: str,
                          observation_ms: int = 500) -> dict:
        if operation not in CONTROLS:
            raise PraxisError('INVALID_OPERATION', 'Use reset_run, reset_halt, halt or resume')
        return self.operate(operation, artifact_id, connection_id, observation_ms)
