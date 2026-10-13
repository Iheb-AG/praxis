"""Bounded, read-only validation of the supported F407 flash image contract."""

from __future__ import annotations

import io
import struct
from pathlib import Path

from praxis.bundle import digest, read_inside
from praxis.errors import PraxisError
from praxis.firmware_assets import FirmwareAssets

MAX_ELF_BYTES = 8 * 1024 * 1024


def validate_elf(path: Path, assets: FirmwareAssets) -> dict:
    if path.is_symlink() or not path.is_file():
        raise PraxisError("INVALID_ELF", "ELF input must be a regular file")
    return validate_bytes(read_inside(path.parent.resolve(), path.name, MAX_ELF_BYTES), assets)


def validate_bytes(data: bytes, assets: FirmwareAssets) -> dict:
    try:
        from elftools.common.exceptions import ELFError
        from elftools.elf.elffile import ELFFile
    except ImportError as exc:
        raise PraxisError("MISSING_DEPENDENCY", "Install project-praxis[build] for ELF validation") from exc
    report = {"valid": False, "elf_sha256": digest(data), "errors": [],
              "profile": assets.manifest.profile, "asset_revision": assets.identity,
              "physical_behavior": "not tested", "checks": []}

    def fail(code, message):
        report["errors"].append({"code": code, "message": message})

    def within(address, size, region):
        start, length = region
        return size >= 0 and start <= address and address + size <= start + length

    try:
        if len(data) > MAX_ELF_BYTES:
            raise ValueError("ELF exceeds 8 MiB")
        elf = ELFFile(io.BytesIO(data))
        if (elf.elfclass != 32 or not elf.little_endian or elf['e_machine'] != 'EM_ARM'
                or elf['e_type'] != 'ET_EXEC' or elf['e_flags'] & 0x400):
            fail("ELF_PROFILE", "Require an executable little-endian ELF32 ARM soft-float image")
        if elf.num_sections() > 512 or elf.num_segments() > 64:
            raise ValueError("Excessive ELF section/segment count")
        sections = list(elf.iter_sections())
        loads = [s for s in elf.iter_segments() if s['p_type'] == 'PT_LOAD']
        if not loads:
            fail("LOAD_SEGMENTS", "No loadable image")
        for segment in loads:
            address, size = segment['p_vaddr'], segment['p_memsz']
            if not any(within(address, size, region) for region in (assets.flash, assets.ram)):
                fail("MEMORY_RANGE", f"Load segment outside flash/main SRAM: {address:#x}+{size:#x}")
            if segment['p_filesz'] > size or segment['p_offset'] + segment['p_filesz'] > len(data):
                fail("LOAD_SEGMENTS", "Load segment exceeds its memory/file bounds")
            if segment['p_filesz'] and not within(segment['p_paddr'], segment['p_filesz'], assets.flash):
                fail("LOAD_ADDRESS", "Initialized load bytes must reside in flash")
            if segment['p_flags'] & 3 == 3:
                fail("RWX_SEGMENT", "Writable executable load segment")
        ranges = sorted((s['p_vaddr'], s['p_vaddr'] + s['p_memsz']) for s in loads if s['p_memsz'])
        if any(a[1] > b[0] for a, b in zip(ranges, ranges[1:], strict=False)):
            fail("OVERLAPPING_SEGMENTS", "Loadable memory ranges overlap")
        allowed = {'.isr_vector', '.text', '.ARM.extab', '.ARM.exidx', '.preinit_array',
                   '.init_array', '.fini_array', '.data', '.bss', '.stack_reservation'}
        for section in sections:
            if not section['sh_flags'] & 2 or not section['sh_size']:
                continue
            address, size = section['sh_addr'], section['sh_size']
            if section.name not in allowed:
                fail("UNSUPPORTED_SECTION", f"Unreviewed allocated section: {section.name}")
            region = assets.ram if section['sh_flags'] & 1 else assets.flash
            if not within(address, size, region):
                fail("SECTION_RANGE", f"Section {section.name} outside its permitted memory")
            if not any(within(address, size, (s['p_vaddr'], s['p_memsz'])) for s in loads):
                fail("SECTION_SEGMENT", f"Section {section.name} lacks a containing load segment")
        table = elf.get_section_by_name('.symtab')
        symbols = {s.name: s['st_value'] for s in table.iter_symbols()} if table else {}
        required = ['_estack', '_stack_limit', '_sidata', '_sdata', '_edata', '_sbss', '_ebss',
                    'Reset_Handler', 'g_pfnVectors', 'SystemInit', '__libc_init_array', 'main']
        for name in required:
            if name not in symbols:
                fail("MISSING_SYMBOL", f"Approved startup/linker symbol missing: {name}")
        top = assets.ram[0] + assets.ram[1]
        if symbols.get('_estack') != top:
            fail("STACK_ADDRESS", f"_estack must be {top:#x}; CCM is a separate memory bank")
        if symbols.get('_stack_limit') != top - 4096 or symbols.get('_ebss', top) > top - 4096:
            fail("STACK_RESERVATION", "Preserve the reviewed 4 KiB stack in main SRAM")
        for section_name, start, end in (('.data', '_sdata', '_edata'), ('.bss', '_sbss', '_ebss')):
            section = elf.get_section_by_name(section_name)
            if section and (symbols.get(start) != section['sh_addr']
                            or symbols.get(end) != section['sh_addr'] + section['sh_size']):
                fail("STARTUP_RANGE", f"Startup symbols do not describe {section_name}")
            if section and section_name == '.data' and section['sh_size']:
                segment = next((s for s in loads if within(section['sh_addr'], section['sh_size'],
                                                           (s['p_vaddr'], s['p_memsz']))), None)
                if segment and symbols.get('_sidata') != (segment['p_paddr'] + section['sh_addr'] - segment['p_vaddr']):
                    fail("DATA_LOAD_ADDRESS", "Startup .data source differs from its flash load address")
        vector = elf.get_section_by_name('.isr_vector')
        if not vector or vector['sh_addr'] != assets.flash[0] or vector['sh_size'] != 392:
            fail("VECTOR_LAYOUT", "F407 requires 98 vectors at 0x08000000")
        if vector and 8 <= vector['sh_size'] <= 4096:
            raw = vector.data()
            words = struct.unpack('<' + 'I' * (len(raw) // 4), raw[:len(raw) // 4 * 4])
            report['initial_sp'] = hex(words[0])
            if words[0] != top or words[0] % 8:
                fail("INITIAL_SP", f"Initial SP {words[0]:#x} must be {top:#x}, 8-byte aligned")
            executable = [s for s in loads if s['p_flags'] & 1]
            if (words[1] & 1 == 0 or not any(within(words[1] & ~1, 2, (s['p_vaddr'], s['p_memsz']))
                                            for s in executable)):
                fail("RESET_ADDRESS", "Reset vector must be Thumb code inside an executable flash segment")
            if words[1] != elf['e_entry'] or words[1] != symbols.get('Reset_Handler'):
                fail("RESET_ENTRY", "ELF entry and reset vector must name Reset_Handler")
            for slot, name in enumerate(assets.vectors):
                if slot >= len(words):
                    break
                expected = 0 if name == '0' else symbols.get(name)
                if expected is None or words[slot] != expected:
                    fail("VECTOR_HANDLER", f"Slot {slot} must resolve to {name}")
        report['checks'] = ['ELF architecture', 'load/section memory bounds', 'main-SRAM stack',
                            '98-entry vendor/header vector layout', 'startup copy/zero symbols']
        report['valid'] = not report['errors']
    except (ELFError, ValueError, KeyError, IndexError, TypeError, struct.error, OSError) as exc:
        fail("MALFORMED_ELF", f"Cannot validate ELF: {exc}")
    return report
