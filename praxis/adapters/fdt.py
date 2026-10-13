"""Small ctypes binding to libfdt, avoiding interpreter-specific Python extension requirements."""

import ctypes
import ctypes.util
import struct

from praxis.errors import PraxisError

NOTFOUND = 1


class FdtException(Exception):
    pass


class Property(bytes):
    def __new__(cls, name, data):
        item = super().__new__(cls, data)
        item.name = name
        return item


class Fdt:
    def __init__(self, data):
        if len(data) < 40 or struct.unpack(">I", data[:4])[0] != 0xD00DFEED:
            raise FdtException("Truncated or invalid DTB header")
        if struct.unpack(">I", data[4:8])[0] > len(data):
            raise FdtException("DTB total size exceeds input length")
        name = ctypes.util.find_library("fdt")
        if not name:
            raise PraxisError("MISSING_TOOL", "Install the libfdt shared library for offline ingestion")
        self.lib = ctypes.CDLL(name)
        self.buffer = ctypes.create_string_buffer(data)
        self.lib.fdt_check_header.argtypes = [ctypes.c_void_p]
        self.lib.fdt_check_header.restype = ctypes.c_int
        self.lib.fdt_check_full.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
        self.lib.fdt_check_full.restype = ctypes.c_int
        if self.lib.fdt_check_full(self.buffer, len(data)):
            raise FdtException("Malformed flattened Device Tree")
        for name in ("fdt_first_property_offset", "fdt_next_property_offset", "fdt_first_subnode", "fdt_next_subnode"):
            method = getattr(self.lib, name)
            method.argtypes = [ctypes.c_void_p, ctypes.c_int]
            method.restype = ctypes.c_int
        self.lib.fdt_get_name.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.lib.fdt_get_name.restype = ctypes.c_void_p
        self.lib.fdt_get_property_by_offset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
        self.lib.fdt_get_property_by_offset.restype = ctypes.c_void_p
        self.lib.fdt_string.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.fdt_string.restype = ctypes.c_char_p
        self.check_header()

    def check_header(self):
        status = self.lib.fdt_check_header(self.buffer)
        if status:
            raise FdtException(f"libfdt header error {status}")

    def _offset(self, name, offset, quiet):
        value = getattr(self.lib, name)(self.buffer, offset)
        if value < 0 and -value not in quiet:
            raise FdtException(f"{name}: libfdt error {value}")
        return value

    def first_property_offset(self, offset, quiet=()):
        return self._offset("fdt_first_property_offset", offset, quiet)

    def next_property_offset(self, offset, quiet=()):
        return self._offset("fdt_next_property_offset", offset, quiet)

    def first_subnode(self, offset, quiet=()):
        return self._offset("fdt_first_subnode", offset, quiet)

    def next_subnode(self, offset, quiet=()):
        return self._offset("fdt_next_subnode", offset, quiet)

    def get_name(self, offset):
        length = ctypes.c_int()
        pointer = self.lib.fdt_get_name(self.buffer, offset, ctypes.byref(length))
        if not pointer or length.value < 0:
            raise FdtException("Invalid node name")
        return ctypes.string_at(pointer, length.value).decode("utf-8")

    def get_property_by_offset(self, offset):
        length = ctypes.c_int()
        pointer = self.lib.fdt_get_property_by_offset(self.buffer, offset, ctypes.byref(length))
        if not pointer or length.value < 0:
            raise FdtException("Invalid property")
        _tag, size, name_offset = struct.unpack(">III", ctypes.string_at(pointer, 12))
        if size != length.value:
            raise FdtException("Property length mismatch")
        name = self.lib.fdt_string(self.buffer, name_offset)
        if not name:
            raise FdtException("Invalid property name")
        return Property(name.decode("utf-8"), ctypes.string_at(pointer + 12, size))

