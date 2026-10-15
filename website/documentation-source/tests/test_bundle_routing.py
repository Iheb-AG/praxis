import json
import shutil
from concurrent.futures import ThreadPoolExecutor

import pytest

from praxis.bundle import Bundle, digest, revision
from praxis.errors import PraxisError
from praxis.evaluation import evaluate
from praxis.routing import Session


def edit_manifest(root, change):
    path = root / "manifest.json"
    data = json.loads(path.read_text())
    change(data)
    data["bundle_revision"] = revision(data)
    path.write_text(json.dumps(data))


def test_required_route_and_unbroken_documents(bundle):
    session = Session(bundle)
    with pytest.raises(PraxisError, match="PREREQUISITE_REQUIRED.*index"):
        session.read_peripheral_doc("usart")
    with pytest.raises(PraxisError, match="PREREQUISITE_REQUIRED"):
        session.query_schematic_netlist("UART_RX")
    assert session.read_wiki_index() == bundle.read("wiki/index.md")
    route = ["rcc", "gpio", "usart", "nvic"] if bundle.manifest.target.family == "stm32" else ["clock", "gpio", "usart", "interrupts"]
    with pytest.raises(PraxisError, match=", ".join(route[:2])):
        session.read_peripheral_doc("usart")
    session.query_schematic_netlist("UART_RX")
    assert session.served == {"index"}
    for name in route:
        assert session.read_peripheral_doc(name) == bundle.read(bundle.manifest.peripherals[name])
    assert session.read_peripheral_doc("USART") == bundle.read(bundle.manifest.peripherals["usart"])
    assert evaluate(bundle)["passed"]


@pytest.mark.parametrize("name", ["../usart", "/etc/passwd", "usart.md", "x\\y", "", "x" * 65])
def test_bad_names_cannot_escape(bundle, name):
    session = Session(bundle)
    session.read_wiki_index()
    with pytest.raises(PraxisError, match="INVALID_INPUT"):
        session.read_peripheral_doc(name)


def test_complete_net_not_component_traversal(bundle):
    session = Session(bundle)
    session.read_wiki_index()
    pin = "pa2" if bundle.manifest.target.family == "stm32" else "pd1"
    result = session.query_schematic_netlist(pin)
    assert "UART_TX_MCU" in result and "R1:1" in result and "U1:" in result
    assert "UART_TX_CONNECTOR" not in result and "J1:1" not in result
    assert "| Sources |" in result and "Illustrative fixture" in result
    assert session.query_schematic_netlist("PA20").startswith("No match")
    assert session.query_schematic_netlist("uart_rx").startswith("No match")
    assert "J1:2" in session.query_schematic_netlist("UART_RX")


def test_ambiguous_alias_lists_candidates(bundle):
    from praxis.netlist import NetlistIndex
    text = bundle.read(bundle.manifest.netlist)
    # Declare the same alias on two physically different nets without merging them.
    text = text.replace("|  | netlist:", "| COLLISION | netlist:")
    index = NetlistIndex(text, "U1")
    with pytest.raises(PraxisError, match="AMBIGUOUS_IDENTITY.*GND.*UART_TX_CONNECTOR"):
        index.query("COLLISION")


def test_session_isolation_and_concurrent_gates(bundle):
    first, second = Session(bundle), Session(bundle)
    first.read_wiki_index()
    assert second.served == set()
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(first.read_peripheral_doc, "usart") for _ in range(20)]
    assert all(isinstance(f.exception(), PraxisError) for f in futures)
    assert first.served == {"index"}


def test_exact_identifiers_roundtrip_markdown_escaping(bundle):
    from praxis.models import Net, Pin, SourceRef
    from praxis.netlist import NetlistIndex
    from praxis.render import netlist
    source = SourceRef(source="netlist", locator="fixture")
    name = "a|b &amp; \\c"
    pin = Pin(ref="U1", number="1", name="TEST", sheet="/", package="fixture", sources=[source])
    text = netlist(bundle.manifest.target, [Net(name=name, pins=[pin], sources=[source])])
    assert "No match" not in NetlistIndex(text, "U1").query(name)


def test_snapshot_survives_disk_edits(bundle, tmp_path):
    root = tmp_path / "bundle"
    shutil.copytree(bundle.root, root)
    active = Bundle(root)
    expected = active.read("wiki/index.md")
    (root / "wiki/index.md").write_text("corrupted")
    assert active.read("wiki/index.md") == expected
    with pytest.raises(PraxisError, match="INTEGRITY_ERROR"):
        Bundle(root)


@pytest.mark.parametrize("failure", ["missing", "encoding", "oversized", "symlink", "cycle", "broken_link", "duplicate", "traversal"])
def test_invalid_bundle_rejected(bundle, tmp_path, failure):
    root = tmp_path / "bundle"
    shutil.copytree(bundle.root, root)
    path = root / "wiki/index.md"
    if failure == "missing":
        path.unlink()
    elif failure == "symlink":
        outside = tmp_path / "outside.md"
        outside.write_text("outside")
        path.unlink()
        path.symlink_to(outside)
    elif failure in ("encoding", "oversized", "broken_link"):
        data = {"encoding": b"\xff", "oversized": b"x" * 65537, "broken_link": b"[[missing]]"}[failure]
        path.write_bytes(data)
        edit_manifest(root, lambda m: m["file_hashes"].update({"wiki/index.md": digest(data)}))
    elif failure == "cycle":
        def cycle(m):
            for dep in m["dependencies"]:
                if dep["entity"] == "usart":
                    dep["requires"] = ["usart"]
        edit_manifest(root, cycle)
    elif failure == "duplicate":
        edit_manifest(root, lambda m: m["documents"].update({"duplicate": "wiki/index.md"}))
    else:
        edit_manifest(root, lambda m: m["file_hashes"].update({"../outside.md": "0" * 64}))
    with pytest.raises(PraxisError):
        Bundle(root)


def test_runtime_imports_no_ingestion_or_subprocess(bundle):
    import subprocess
    import sys
    result = subprocess.run([sys.executable, "-c", "from pathlib import Path; from praxis.server import create_server; import sys; create_server(Path(sys.argv[1])); assert not any(k.startswith(('clang', 'defusedxml', 'praxis.adapters')) for k in sys.modules)", str(bundle.root)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr

