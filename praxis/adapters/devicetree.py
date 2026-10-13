"""Resolve DTBs with libfdt; only fixture bindings are decoded in v1."""

from __future__ import annotations

import struct
import shlex
from pathlib import Path
from tempfile import TemporaryDirectory

from praxis.errors import PraxisError
from praxis.models import SourceRef, TopologyNode
from praxis.process import run


def _cells(value: bytes) -> list[int]:
    if len(value) % 4:
        raise PraxisError("INVALID_DTB", "Cell property is not a multiple of four bytes")
    return list(struct.unpack(f">{len(value) // 4}I", value))


def _number(values: list[int]) -> int:
    result = 0
    for cell in values:
        result = (result << 32) | cell
    return result


def parse_dtb(data: bytes, source_id: str) -> list[TopologyNode]:
    from praxis.adapters import fdt as libfdt
    try:
        fdt = libfdt.Fdt(data)
        fdt.check_header()
        raw = {}

        def walk(offset: int, path: str, parent: str | None):
            properties = {}
            prop = fdt.first_property_offset(offset, quiet=(libfdt.NOTFOUND,))
            while prop >= 0:
                item = fdt.get_property_by_offset(prop)
                properties[item.name] = bytes(item)
                prop = fdt.next_property_offset(prop, quiet=(libfdt.NOTFOUND,))
            raw[path] = {"offset": offset, "parent": parent, "properties": properties}
            child = fdt.first_subnode(offset, quiet=(libfdt.NOTFOUND,))
            while child >= 0:
                name = fdt.get_name(child)
                walk(child, path.rstrip("/") + "/" + name, path)
                child = fdt.next_subnode(child, quiet=(libfdt.NOTFOUND,))

        walk(0, "/", None)
        phandles = {}
        for path, entry in raw.items():
            props = entry["properties"]
            handle = props.get("phandle", props.get("linux,phandle"))
            if handle:
                cells = _cells(handle)
                if len(cells) != 1 or cells[0] in (0, 0xFFFFFFFF) or cells[0] in phandles:
                    raise PraxisError("INVALID_DTB", "Invalid or duplicate phandle")
                phandles[cells[0]] = path

        def count(path, key, default):
            values = _cells(raw[path]["properties"].get(key, struct.pack(">I", default)))
            if len(values) != 1 or values[0] > 4:
                raise PraxisError("UNSUPPORTED_BINDING", f"{path}: invalid {key}")
            return values[0]

        def translate(bus, address, size):
            while raw[bus]["parent"] is not None:
                parent = raw[bus]["parent"]
                props = raw[bus]["properties"]
                if "ranges" not in props:
                    raise PraxisError("UNRESOLVED_ADDRESS", f"{bus}: missing ranges translation")
                ranges = _cells(props["ranges"])
                if ranges:
                    child_cells = count(bus, "#address-cells", 2)
                    parent_cells = count(parent, "#address-cells", 2)
                    size_cells = count(bus, "#size-cells", 1)
                    stride = child_cells + parent_cells + size_cells
                    if not stride or len(ranges) % stride:
                        raise PraxisError("INVALID_DTB", f"{bus}: malformed ranges")
                    matches = []
                    for start in range(0, len(ranges), stride):
                        row = ranges[start:start + stride]
                        child_base = _number(row[:child_cells])
                        parent_base = _number(row[child_cells:child_cells + parent_cells])
                        length = _number(row[child_cells + parent_cells:])
                        if child_base <= address and address + size <= child_base + length:
                            matches.append(parent_base + address - child_base)
                    if len(matches) != 1:
                        raise PraxisError("UNRESOLVED_ADDRESS", f"{bus}: no unique range for address")
                    address = matches[0]
                bus = parent
            return address

        def references(values, cells_key):
            result = []
            position = 0
            while position < len(values):
                handle = values[position]
                provider = phandles.get(handle)
                if provider is None:
                    raise PraxisError("DANGLING_PHANDLE", f"Unresolved phandle {handle}")
                props = raw[provider]["properties"]
                if cells_key not in props:
                    raise PraxisError("UNSUPPORTED_BINDING", f"{provider}: missing {cells_key}")
                length = count(provider, cells_key, 0)
                end = position + length + 1
                if end > len(values):
                    raise PraxisError("INVALID_DTB", "Truncated provider specifier")
                result.append({"provider": provider, "args": values[position + 1:end]})
                position = end
            return result

        output = []
        for path, entry in raw.items():
            props = entry["properties"]
            decoded = {}
            known = {"compatible", "status", "phandle", "linux,phandle", "#address-cells",
                     "#size-cells", "#clock-cells", "#interrupt-cells", "ranges", "reg",
                     "clocks", "interrupts", "interrupts-extended", "interrupt-parent",
                     "interrupt-controller", "clock-frequency", "model"}
            enabled = True
            ancestor = path
            while ancestor is not None:
                status = raw[ancestor]["properties"].get("status", b"okay\0").rstrip(b"\0")
                enabled &= status in (b"ok", b"okay")
                ancestor = raw[ancestor]["parent"]
            if "reg" in props:
                parent = entry["parent"]
                if parent is None:
                    raise PraxisError("INVALID_DTB", "Root cannot contain reg")
                bus_compatible = raw[parent]["properties"].get("compatible", b"").split(b"\0")
                if parent != "/" and b"simple-bus" not in bus_compatible:
                    raise PraxisError("UNSUPPORTED_BINDING", f"{parent}: reg decoding requires a supported simple-bus binding")
                ac, sc = count(parent, "#address-cells", 2), count(parent, "#size-cells", 1)
                values = _cells(props["reg"])
                stride = ac + sc
                if not stride or len(values) % stride:
                    raise PraxisError("INVALID_DTB", f"{path}: malformed reg")
                decoded["reg"] = [
                    {"address": translate(parent, _number(values[i:i + ac]),
                                          _number(values[i + ac:i + stride])),
                     "size": _number(values[i + ac:i + stride])}
                    for i in range(0, len(values), stride)
                ]
            if "clocks" in props:
                decoded["clocks"] = references(_cells(props["clocks"]), "#clock-cells")
            if "interrupts-extended" in props:
                decoded["interrupts"] = references(_cells(props["interrupts-extended"]),
                                                    "#interrupt-cells")
            elif "interrupts" in props:
                ancestor = path
                provider = None
                while ancestor is not None and provider is None:
                    value = raw[ancestor]["properties"].get("interrupt-parent")
                    if value:
                        cells = _cells(value)
                        if len(cells) != 1 or cells[0] not in phandles:
                            raise PraxisError("DANGLING_PHANDLE", f"{path}: invalid interrupt-parent")
                        provider = phandles[cells[0]]
                    ancestor = raw[ancestor]["parent"]
                if provider is None:
                    raise PraxisError("UNSUPPORTED_BINDING", f"{path}: missing interrupt-parent")
                length = count(provider, "#interrupt-cells", 0)
                values = _cells(props["interrupts"])
                if not length or len(values) % length:
                    raise PraxisError("INVALID_DTB", f"{path}: malformed interrupts")
                decoded["interrupts"] = [{"provider": provider, "args": values[i:i + length]}
                                         for i in range(0, len(values), length)]
            if "interrupt-parent" in props:
                handles = _cells(props["interrupt-parent"])
                if len(handles) != 1 or handles[0] not in phandles:
                    raise PraxisError("DANGLING_PHANDLE", f"{path}: invalid interrupt-parent")
            # Only the built-in synthetic binding is interpreted beyond standard properties.
            compatible = props.get("compatible", b"").split(b"\0")
            if b"praxis,fixture-uart" in compatible and "praxis,pins" in props:
                decoded["pins"] = props["praxis,pins"].rstrip(b"\0").decode("utf-8").split("\0")
                known.add("praxis,pins")
            output.append(TopologyNode(path=path, enabled=enabled,
                                      properties={k: v.hex() for k, v in sorted(props.items())},
                                      decoded=decoded, unresolved=sorted(set(props) - known),
                                      sources=[SourceRef(source=source_id, locator=path)]))
        return sorted(output, key=lambda n: n.path)
    except (libfdt.FdtException, UnicodeDecodeError, struct.error) as exc:
        raise PraxisError("INVALID_DTB", str(exc)) from exc


def compile_dts(path: Path, overlays: list[Path], include_dirs: list[Path], source_id: str, *,
                registered_sources: list[Path] | None = None):
    with TemporaryDirectory(prefix="praxis-dtc-") as directory:
        work = Path(directory)
        registered = ({source.resolve(strict=True) for source in registered_sources}
                      if registered_sources is not None else None)

        def check_dependencies(depfile, generated=None):
            if registered is None:
                return
            text = depfile.read_text(encoding="utf-8").replace("\\\n", " ")
            if ":" not in text:
                raise PraxisError("EXTRACTOR_FAILED", "Missing Device Tree dependency output")
            try:
                names = shlex.split(text.split(":", 1)[1].replace("$$", "$"))
            except ValueError as exc:
                raise PraxisError("EXTRACTOR_FAILED", "Invalid Device Tree dependency output") from exc
            for name in names:
                dependency = Path(name).resolve(strict=True)
                if dependency != generated and dependency not in registered:
                    raise PraxisError("UNREGISTERED_INCLUDE", f"Hash-register Device Tree dependency: {dependency.name}")

        def compile_one(source, name):
            preprocessed = work / f"{name}.dts"
            cppdeps = work / f"{name}.cpp.d"
            preprocessed.write_text(run(["gcc", "-E", "-P", "-MD", "-MF", str(cppdeps), "-MT", "praxis-dts",
                                         "-x", "assembler-with-cpp", "-nostdinc",
                                         "-undef", *[f"-I{p}" for p in include_dirs], str(source)]))
            check_dependencies(cppdeps)
            destination = work / f"{name}.dtb"
            dtdeps = work / f"{name}.dtc.d"
            run(["dtc", "-@", "-I", "dts", "-O", "dtb", "-d", str(dtdeps),
                 *[flag for p in include_dirs for flag in ("-i", str(p))],
                 "-o", str(destination), str(preprocessed)])
            check_dependencies(dtdeps, preprocessed)
            return destination

        base = compile_one(path, "base")
        if overlays:
            compiled = [compile_one(source, f"overlay{i}") for i, source in enumerate(overlays)]
            final = work / "resolved.dtb"
            run(["fdtoverlay", "-i", str(base), "-o", str(final), *map(str, compiled)])
        else:
            final = base
        return parse_dtb(final.read_bytes(), source_id)
