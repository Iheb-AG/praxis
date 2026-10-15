"""Optional Linux ST-LINK preflight and bounded diagnostic reads.

No arbitrary commands/addresses, target halt/reset, flash driver, or firmware execution.
Debug attachment itself is not electrically passive; see docs/hardware-inspection.md.
"""

from __future__ import annotations

import json
import os
import platform
import re
import tempfile
import uuid
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from praxis.bundle import Bundle, digest, read_inside
from praxis.errors import PraxisError
from praxis.firmware_assets import FirmwareAssets
from praxis.verify import bounded

SERIAL = re.compile(r'[A-Za-z0-9_-]{1,64}\Z')
STLINK_PRODUCTS = {0x3748, 0x374B, 0x374D, 0x374E, 0x374F, 0x3752, 0x3753, 0x3754}
IDENTITY = {'idcode': (0xE0042000, 32), 'cpuid': (0xE000ED00, 32),
            'flash_kib': (0x1FFF7A22, 16), 'uid0': (0x1FFF7A10, 32),
            'uid1': (0x1FFF7A14, 32), 'uid2': (0x1FFF7A18, 32)}
# CFSR/HFSR and address registers have no read-to-clear behavior. SysTick CTRL
# and DHCSR are intentionally absent: reads can clear observation flags.
DIAGNOSTICS = {'cfsr': (0xE000ED28, 32), 'hfsr': (0xE000ED2C, 32),
               'mmfar': (0xE000ED34, 32), 'bfar': (0xE000ED38, 32),
               'rcc_cr': (0x40023800, 32), 'rcc_cfgr': (0x40023808, 32),
               'rcc_pllcfgr': (0x40023804, 32), 'rcc_cfgr_after': (0x40023808, 32),
               'rcc_ahb1enr': (0x40023830, 32),
               'gpioa_idr': (0x40020010, 32), 'gpiod_odr': (0x40020C14, 32),
               'systick_load': (0xE000E014, 32)}
GPIO_CLOCKS = {'gpioa_idr': 1, 'gpiod_odr': 1 << 3}
LIMITS = ['Debug attachment changes debug-transport state; it is not electrically passive.',
          'No reset, halt, resume, stepping, breakpoint, programming or target-register write is requested.',
          'Running-target samples are sequential and not an atomic snapshot.',
          'IDCODE/flash/CPUID establish family compatibility, not exact package, PCB revision or wiring.',
          'GPIO latches and input samples do not prove optical output or precise physical timing.',
          'No flash/readback comparison is performed; a build artifact is not assumed to be running.']


class HardwareProfile(BaseModel):
    model_config = ConfigDict(extra='forbid', frozen=True)
    schema_version: int = Field(ge=1, le=1)
    profile_revision: str = Field(pattern=r'^[0-9a-f]{64}$')
    bundle_revision: str = Field(pattern=r'^[0-9a-f]{64}$')
    asset_revision: str = Field(pattern=r'^[0-9a-f]{64}$')
    openocd_path: str
    openocd_sha256: str = Field(pattern=r'^[0-9a-f]{64}$')
    openocd_version: str
    physical_board_revision: str | None = None


def profile_revision(value: dict) -> str:
    return digest(json.dumps({k: v for k, v in value.items() if k != 'profile_revision'},
                             sort_keys=True, separators=(',', ':')).encode())


def executable_bytes(path: Path) -> bytes:
    if not path.is_absolute() or path.is_symlink() or not path.is_file() or not os.access(path, os.X_OK):
        raise PraxisError('INVALID_BACKEND', 'Select an absolute, regular, executable OpenOCD path')
    return read_inside(path.parent, path.name, 64 * 1024 * 1024)


def provision_profile(bundle_path: Path, assets_path: Path, backend: Path, output: Path) -> str:
    if platform.system() != 'Linux':
        raise PraxisError('UNSUPPORTED_PLATFORM', 'Hardware inspection profiles currently require Linux')
    bundle = Bundle(bundle_path)
    assets = FirmwareAssets(assets_path, bundle)
    if output.exists() or output.is_symlink():
        raise PraxisError('OUTPUT_EXISTS', 'Use a new hardware profile path')
    contents = executable_bytes(backend)
    result = bounded([str(backend), '--version'], 5)
    version = result['diagnostics'].splitlines()[0] if result['diagnostics'] else ''
    if result['returncode'] or result['failure'] or not version.startswith('Open On-Chip Debugger 0.12.'):
        raise PraxisError('INVALID_BACKEND', 'This inspection profile requires OpenOCD 0.12.x')
    value = HardwareProfile(schema_version=1, profile_revision='0' * 64,
        bundle_revision=bundle.manifest.bundle_revision, asset_revision=assets.identity,
        openocd_path=str(backend), openocd_sha256=digest(contents), openocd_version=version).model_dump()
    value['profile_revision'] = profile_revision(value)
    output.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation: never replace a profile used by another session.
    with output.open('x', encoding='utf-8') as handle:
        handle.write(json.dumps(value, indent=2, sort_keys=True) + '\n')
    return value['profile_revision']


def discover_probes(sysfs: Path = Path('/sys/bus/usb/devices')) -> list[dict]:
    if platform.system() != 'Linux':
        raise PraxisError('UNSUPPORTED_PLATFORM', 'Hardware inspection currently requires Linux/sysfs')
    if not sysfs.is_dir():
        raise PraxisError('USB_UNAVAILABLE', 'Linux USB sysfs is unavailable')
    result = []
    for entry in sorted(sysfs.iterdir()):
        try:
            vendor = int((entry / 'idVendor').read_text().strip(), 16)
            product = int((entry / 'idProduct').read_text().strip(), 16)
            if vendor != 0x0483 or product not in STLINK_PRODUCTS:
                continue
            serial = (entry / 'serial').read_text().strip() if (entry / 'serial').exists() else None
            name = (entry / 'product').read_text().strip() if (entry / 'product').exists() else 'ST-LINK'
            result.append({'serial': serial, 'vendor_id': vendor, 'product_id': product,
                           'usb_location': entry.name, 'product': name[:128],
                           'selectable': bool(serial and SERIAL.fullmatch(serial))})
        except FileNotFoundError:
            continue  # Device disappeared or this is a USB interface entry.
        except (OSError, ValueError) as exc:
            raise PraxisError('USB_ENUMERATION_FAILED', f'Cannot read USB descriptors for {entry.name}') from exc
    return result


def configuration(serial: str, product: int) -> str:
    if not SERIAL.fullmatch(serial) or product not in STLINK_PRODUCTS:
        raise PraxisError('INVALID_PROBE', 'Use an exact selectable ST-LINK serial from list_debug_probes')
    # Standalone configuration: no sourced target files, reset hooks or flash banks.
    return '\n'.join(['gdb_port disabled', 'tcl_port disabled', 'telnet_port disabled',
        'adapter driver st-link', 'st-link backend usb', f'st-link vid_pid 0x0483 0x{product:04x}',
        f'adapter serial {serial}', 'transport select dapdirect_swd', 'adapter speed 1000',
        'reset_config none', 'swd newdap praxis cpu -irlen 4 -expected-id 0x2ba01477',
        'dap create praxis.dap -chain-position praxis.cpu',
        'target create praxis.cpu cortex_m -endian little -dap praxis.dap -gdb-port disabled',
        'praxis.cpu configure -work-area-size 0']) + '\n'


def halted_core_register_script() -> list[str]:
    """Use OpenOCD's case-sensitive register names, preserving our public field names.

    OpenOCD armv7m.c names the status register `xPSR`; `get_reg` rejects `xpsr`.
    This shared fragment must never request a halt merely to obtain registers.
    """
    return ['if {[praxis.cpu curstate] eq "halted"} {',
            '  set regs [get_reg -force {pc sp lr xPSR}]',
            '  foreach {name backend_name} {pc pc sp sp lr lr xpsr xPSR} {',
            '    echo [format "PRAXIS|%s|0x%08x" $name [dict get $regs $backend_name]]',
            '  }', '}']


def read_script(include_diagnostics: bool, expected_uid: str | None = None) -> str:
    if (include_diagnostics and not expected_uid) or (expected_uid and not re.fullmatch('[0-9a-f]{24}', expected_uid)):
        raise PraxisError('UNKNOWN_CONNECTION', 'Diagnostic reads require a verified MCU UID')
    commands = ['init']
    for name, (address, width) in IDENTITY.items():
        commands += [f'set praxis_{name} [lindex [read_memory 0x{address:08x} {width} 1] 0]',
                     f'echo [format "PRAXIS|{name}|0x%08x" $praxis_{name}]']
        if name == 'cpuid':
            commands += ['if {($praxis_idcode & 0xfff) != 0x413 || (($praxis_cpuid >> 4) & 0xfff) != 0xc24 || ($praxis_cpuid >> 24) != 0x41} {',
                         '  error "PRAXIS_TARGET_MISMATCH: incompatible family or core"', '}']
        if name == 'flash_kib':
            commands += ['if {$praxis_flash_kib != 1024} {',
                         '  error "PRAXIS_TARGET_MISMATCH: incompatible flash capacity"', '}']
    if expected_uid:
        commands += ['set praxis_uid [format "%08x%08x%08x" $praxis_uid0 $praxis_uid1 $praxis_uid2]',
                     f'if {{$praxis_uid ne "{expected_uid}"}} {{',
                     '  error "PRAXIS_TARGET_CHANGED: MCU UID differs from preflight"', '}']
    if include_diagnostics:
        for name, (address, width) in DIAGNOSTICS.items():
            if name in GPIO_CLOCKS:
                commands.append(f'if {{$praxis_rcc_ahb1enr & {GPIO_CLOCKS[name]}}} {{')
            commands += [f'set praxis_{name} [lindex [read_memory 0x{address:08x} {width} 1] 0]',
                         f'echo [format "PRAXIS|{name}|0x%08x" $praxis_{name}]']
            if name in GPIO_CLOCKS:
                commands.append('}')
    commands += ['echo "PRAXIS|state|[praxis.cpu curstate]"']
    if include_diagnostics:
        commands += halted_core_register_script()
    commands.append('shutdown')
    return '\n'.join(commands) + '\n'


def parse_observation(output: str, diagnostics: bool, *, core_registers: bool = False) -> dict:
    values = {}
    numeric = {**IDENTITY, **(DIAGNOSTICS if diagnostics else {}),
               **({'pc': (0, 32), 'sp': (0, 32), 'lr': (0, 32), 'xpsr': (0, 32)} if diagnostics or core_registers else {})}
    for line in output.splitlines():
        if not line.startswith('PRAXIS|'):
            continue
        parts = line.split('|')
        if len(parts) != 3 or parts[1] in values or parts[1] not in {*numeric, 'state'}:
            raise PraxisError('BACKEND_PROTOCOL', 'Malformed or duplicate OpenOCD observation marker')
        name, value = parts[1:]
        if name == 'state':
            if value not in {'halted', 'running', 'debug-running', 'reset', 'unavailable', 'unknown'}:
                raise PraxisError('BACKEND_PROTOCOL', 'Unrecognized target execution state')
            values[name] = value
        else:
            if not re.fullmatch(r'0x[0-9a-fA-F]{1,8}', value) or int(value, 16) >= 1 << numeric[name][1]:
                raise PraxisError('BACKEND_PROTOCOL', f'Invalid numeric observation: {name}')
            values[name] = int(value, 16)
    required = {*IDENTITY, 'state', *(set(DIAGNOSTICS) - set(GPIO_CLOCKS) if diagnostics else {})}
    if not required.issubset(values):
        raise PraxisError('BACKEND_PROTOCOL', 'OpenOCD did not return all required observations')
    if diagnostics:
        for name, mask in GPIO_CLOCKS.items():
            if values['rcc_ahb1enr'] & mask and name not in values:
                raise PraxisError('BACKEND_PROTOCOL', f'Enabled-port observation is missing: {name}')
    if (diagnostics or core_registers) and values['state'] == 'halted' and not {'pc', 'sp', 'lr', 'xpsr'}.issubset(values):
        raise PraxisError('BACKEND_PROTOCOL', 'Halted-target register result is incomplete')
    return values


def identity(values: dict) -> dict:
    return {'device_id': values['idcode'] & 0xFFF, 'silicon_revision': values['idcode'] >> 16,
            'cpuid': values['cpuid'], 'flash_kib': values['flash_kib'],
            'uid': ''.join(f'{values[f"uid{i}"]:08x}' for i in range(3))}


def check_target(values: dict) -> dict:
    result = identity(values)
    if (result['device_id'] != 0x413 or (result['cpuid'] >> 4) & 0xFFF != 0xC24
            or (result['cpuid'] >> 24) != 0x41 or result['flash_kib'] != 1024
            or result['uid'] in {'0' * 24, 'f' * 24}):
        raise PraxisError('TARGET_MISMATCH', 'Require STM32F405/407-family ID 0x413, Arm Cortex-M4, 1024 KiB flash and a readable UID; no reset/programming was attempted')
    return result


def decode_clock(values: dict) -> dict:
    cfgr = values['rcc_cfgr']
    if cfgr != values['rcc_cfgr_after']:
        return {'stable_sample': False, 'nominal_hclk_hz': None, 'reason': 'RCC changed during sampling'}
    source = (cfgr >> 2) & 3
    source_hz = 16000000
    basis = 'HSI nominal 16 MHz'
    if source == 1:
        source_hz, basis = 8000000, 'HSE assumed 8 MHz from reference board; not physically measured'
    elif source == 2:
        pll = values['rcc_pllcfgr']
        m, n, p = pll & 63, (pll >> 6) & 511, (((pll >> 16) & 3) + 1) * 2
        if not m or not n:
            return {'stable_sample': True, 'nominal_hclk_hz': None, 'reason': 'Invalid PLL divisor/multiplier'}
        external = bool(pll & (1 << 22))
        source_hz = (8000000 if external else 16000000) * n / (m * p)
        basis = 'PLL derived from ' + ('assumed HSE 8 MHz' if external else 'nominal HSI 16 MHz')
    elif source == 3:
        return {'stable_sample': True, 'nominal_hclk_hz': None, 'reason': 'Reserved SYSCLK source'}
    divisor = [1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 64, 128, 256, 512][(cfgr >> 4) & 15]
    hclk = source_hz / divisor
    return {'stable_sample': True, 'basis': basis, 'ahb_divisor': divisor,
            'nominal_hclk_hz': hclk, 'systick_reload': values['systick_load'],
            'systick_period_if_processor_clock_ms': (values['systick_load'] + 1) * 1000 / hclk,
            'systick_source': 'unverified: CTRL omitted because reading clears COUNTFLAG'}


class HardwareService:
    def __init__(self, bundle: Bundle, assets: FirmwareAssets, profile_path: Path, lock_root: Path):
        if platform.system() != 'Linux':
            raise PraxisError('UNSUPPORTED_PLATFORM', 'Hardware inspection requires Linux')
        try:
            self.profile = HardwareProfile.model_validate_json(read_inside(profile_path.parent.resolve(), profile_path.name, 64 * 1024))
        except ValidationError as exc:
            raise PraxisError('INVALID_HARDWARE_PROFILE', str(exc)) from exc
        if profile_revision(self.profile.model_dump()) != self.profile.profile_revision:
            raise PraxisError('INTEGRITY_ERROR', 'Hardware profile revision mismatch')
        if (self.profile.bundle_revision != bundle.manifest.bundle_revision
                or self.profile.asset_revision != assets.identity):
            raise PraxisError('TARGET_MISMATCH', 'Hardware profile does not match the selected bundle/assets')
        self.bundle, self.assets = bundle, assets
        self.backend = Path(self.profile.openocd_path)
        self.verify_backend()
        self.lock_root = lock_root.resolve()
        self.connections = {}

    def verify_backend(self):
        if digest(executable_bytes(self.backend)) != self.profile.openocd_sha256:
            raise PraxisError('INTEGRITY_ERROR', 'OpenOCD executable changed; review and provision a new profile')

    def describe(self) -> dict:
        return {'enabled': True, 'profile_revision': self.profile.profile_revision,
                'backend': self.profile.openocd_version, 'mode': 'inspection only',
                'physical_board_revision': self.profile.physical_board_revision, 'limits': LIMITS}

    def list_probes(self) -> dict:
        return {'probes': discover_probes(), 'selection': 'Pass an exact selectable serial to inspect_target',
                'limits': ['USB enumeration does not attach to or identify the target MCU.']}

    @contextmanager
    def probe_lock(self, serial: str):
        import fcntl

        self.lock_root.mkdir(parents=True, exist_ok=True)
        path = self.lock_root / (digest(serial.encode()) + '.lock')
        fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise PraxisError('PROBE_BUSY', 'Another Praxis process is inspecting this probe') from exc
            yield
        finally:
            os.close(fd)

    def select(self, serial: str) -> dict:
        if not isinstance(serial, str) or not SERIAL.fullmatch(serial):
            raise PraxisError('INVALID_PROBE', 'Use an exact selectable serial from list_debug_probes')
        matches = [p for p in discover_probes() if p['serial'] == serial and p['selectable']]
        if not matches:
            raise PraxisError('PROBE_NOT_FOUND', 'Selected ST-LINK is not connected or its serial is unreadable')
        if len(matches) != 1:
            raise PraxisError('AMBIGUOUS_PROBE', 'Multiple probes report this serial; no probe selected')
        return matches[0]

    def observe(self, probe: dict, diagnostics: bool, expected_uid: str | None = None) -> tuple[dict, str]:
        self.verify_backend()
        with tempfile.TemporaryDirectory(prefix='praxis-inspect-') as directory:
            root = Path(directory)
            (root / 'attach.cfg').write_text(configuration(probe['serial'], probe['product_id']))
            (root / 'read.tcl').write_text(read_script(diagnostics, expected_uid))
            # -f is explicit; cwd is private. Neither implicit openocd.cfg nor user Tcl is loaded.
            result = bounded([str(self.backend), '-f', str(root / 'attach.cfg'),
                              '-f', str(root / 'read.tcl')], 8, cwd=root)
        if result['failure']:
            raise PraxisError(result['failure'], 'OpenOCD inspection stopped; check power, USB access and probe ownership. No reset/halt/programming fallback is attempted')
        if result['returncode']:
            for marker, code in [('PRAXIS_TARGET_CHANGED', 'TARGET_CHANGED'),
                                 ('PRAXIS_TARGET_MISMATCH', 'TARGET_MISMATCH')]:
                if marker in result['diagnostics']:
                    raise PraxisError(code, 'Target check failed before peripheral diagnostics; obtain a fresh preflight')
            raise PraxisError('PROBE_ACCESS_FAILED', 'OpenOCD could not inspect the selected target; check USB permissions, firmware support and other debugger connections. Diagnostics: ' + result['diagnostics'][-4096:])
        return parse_observation(result['diagnostics'], diagnostics), result['diagnostics']

    def report(self, probe: dict, values: dict, diagnostics: str) -> dict:
        return {'run_id': uuid.uuid4().hex, 'observed_at': datetime.now(UTC).isoformat(),
                'probe': probe, 'target_identity': check_target(values),
                'declared_target': self.bundle.manifest.target.model_dump(),
                'bundle_revision': self.bundle.manifest.bundle_revision,
                'hardware_profile_revision': self.profile.profile_revision,
                'compatibility': 'family/core/flash compatible; exact MCU package and PCB revision not detected',
                'execution_state': values['state'], 'backend_diagnostics': diagnostics,
                'physical_behavior': 'not tested', 'limits': LIMITS}

    def inspect_target(self, serial: str) -> dict:
        probe = self.select(serial)
        with self.probe_lock(serial):
            values, diagnostics = self.observe(probe, False)
        result = self.report(probe, values, diagnostics)
        # Bound the per-process state store and require fresh identity after restart.
        if len(self.connections) >= 32:
            self.connections.pop(next(iter(self.connections)))
        connection = uuid.uuid4().hex
        self.connections[connection] = (serial, result['target_identity']['uid'])
        return {**result, 'connection_id': connection}

    def inspect_execution(self, connection_id: str) -> dict:
        if connection_id not in self.connections:
            raise PraxisError('UNKNOWN_CONNECTION', 'Call inspect_target first; restart invalidates connection IDs')
        serial, uid = self.connections[connection_id]
        probe = self.select(serial)
        with self.probe_lock(serial):
            try:
                values, diagnostics = self.observe(probe, True, expected_uid=uid)
            except PraxisError as exc:
                if exc.code in {'TARGET_CHANGED', 'TARGET_MISMATCH'}:
                    del self.connections[connection_id]
                raise
        result = self.report(probe, values, diagnostics)
        if result['target_identity']['uid'] != uid:
            del self.connections[connection_id]
            raise PraxisError('TARGET_CHANGED', 'MCU UID changed since preflight; obtain a new connection ID')
        registers = {name: hex(values[name]) for name in ('pc', 'sp', 'lr', 'xpsr') if name in values}
        gpioa_enabled, gpiod_enabled = bool(values['rcc_ahb1enr'] & 1), bool(values['rcc_ahb1enr'] & 8)
        return {**result, 'connection_id': connection_id, 'core_registers': registers,
                'core_register_limits': 'Available only when target was already halted; no halt requested',
                'fault_status': {name: hex(values[name]) for name in ('cfsr', 'hfsr', 'mmfar', 'bfar')},
                'fault_address_valid': {'mmfar': bool(values['cfsr'] & (1 << 7)),
                                        'bfar': bool(values['cfsr'] & (1 << 15))},
                'clock': decode_clock(values),
                'raw_registers': {name: hex(values[name]) for name in DIAGNOSTICS if name in values},
                'signals': {'gpioa_clock_enabled': gpioa_enabled, 'gpiod_clock_enabled': gpiod_enabled,
                            'led_a_output_latch': bool(values['gpiod_odr'] & (1 << 12)) if gpiod_enabled else None,
                            'led_b_output_latch': bool(values['gpiod_odr'] & (1 << 13)) if gpiod_enabled else None,
                            'button_input_sample': bool(values['gpioa_idr'] & 1) if gpioa_enabled else None,
                            'limits': 'Disabled GPIO clocks suppress port reads; running firmware can change clock gates during sampling.'}}
