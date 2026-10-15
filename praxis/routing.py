"""Session-local HEDG retrieval evidence, not a claim about firmware correctness."""

import re
from threading import RLock

from praxis.bundle import Bundle
from praxis.advisories import document_advisory
from praxis.errors import PraxisError
from praxis.netlist import NetlistIndex


class Session:
    def __init__(self, bundle: Bundle):
        self.bundle = bundle
        self.lock = RLock()
        self.served: set[str] = set()
        self.netlist = NetlistIndex(bundle.read(bundle.manifest.netlist),
            bundle.manifest.target.primary_mcu_ref,
            bundle.read(bundle.manifest.documents["schemas/board"])
                if "schemas/board" in bundle.manifest.documents else None,
            bundle.read(bundle.manifest.documents["schemas/components"])
                if "schemas/components" in bundle.manifest.documents else None,
            allow_empty=bundle.manifest.target.scope == "mcu")

    def read_wiki_index(self) -> str:
        with self.lock:
            result = self.bundle.read(self.bundle.manifest.documents["index"])
            self.served.add("index")
            return result

    def _require_index(self):
        if "index" not in self.served:
            raise PraxisError("PREREQUISITE_REQUIRED", "Read read_wiki_index() first; missing: index")

    def read_peripheral_doc(self, peripheral_name: str) -> str:
        if not isinstance(peripheral_name, str) or not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]{0,63}", peripheral_name):
            raise PraxisError("INVALID_INPUT", "Use a canonical peripheral name or declared alias, without a path or extension")
        name = peripheral_name.lower()
        with self.lock:
            self._require_index()
            manifest = self.bundle.manifest
            name = manifest.aliases.get(name, name)
            if name not in manifest.peripherals:
                raise PraxisError("UNKNOWN_PERIPHERAL", f"Unknown peripheral {name!r}; available: {', '.join(sorted(manifest.peripherals))}")
            advisory = document_advisory(manifest.bundle_revision, name)
            if advisory:
                raise PraxisError("SUPERSEDED_KNOWLEDGE", advisory)
            missing = []
            visited = set()

            def prerequisites(entity):
                if entity in visited:
                    return
                visited.add(entity)
                for parent in self.bundle.dependencies[entity]:
                    prerequisites(parent)
                    if parent not in self.served and parent not in missing:
                        missing.append(parent)

            prerequisites(name)
            if missing:
                raise PraxisError("PREREQUISITE_REQUIRED", f"Before {name}, retrieve in order: {', '.join(missing)}")
            result = self.bundle.read(manifest.peripherals[name])
            self.served.add(name)
            return result

    def query_schematic_netlist(self, query_target: str) -> str:
        with self.lock:
            self._require_index()
            return self.netlist.query(query_target)

