"""Author the deterministic partial KiCad fixtures; not a general schematic importer."""

from pathlib import Path
from uuid import NAMESPACE_URL, uuid5

ROOT = Path(__file__).resolve().parents[1]


def uid(value):
    return str(uuid5(NAMESPACE_URL, "project-praxis/" + value))


def make(family, target, package, tx, rx, power, ground):
    root_id = uid(family + "/root")
    components = [
        ("U1", "MCU", target, package, 50, 50,
         [(tx[0], tx[1], "output", "UART_TX_MCU"), (rx[0], rx[1], "input", "UART_RX"),
          (power[0], power[1], "power_in", "VCC"), (ground[0], ground[1], "power_in", "GND")]),
        ("J1", "Header", "UART header", "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 120, 50,
         [("1", "TX", "passive", "UART_TX_CONNECTOR"), ("2", "RX", "passive", "UART_RX"),
          ("3", "VCC", "passive", "VCC"), ("4", "GND", "passive", "GND")]),
        ("R1", "Resistor", "33R", "Resistor_SMD:R_0603_1608Metric", 85, 90,
         [("1", "1", "passive", "UART_TX_MCU"), ("2", "2", "passive", "UART_TX_CONNECTOR")]),
        ("C1", "Capacitor", "100nF", "Capacitor_SMD:C_0603_1608Metric", 120, 90,
         [("1", "1", "passive", "VCC"), ("2", "2", "passive", "GND")]),
    ]
    libraries, symbols, wiring = [], [], []
    for ref, kind, value, footprint, x, y, pins in components:
        properties = (f'(property "Reference" "{ref[0]}" (at 0 10 0) (effects (font (size 1.27 1.27))))\n'
                      f'(property "Value" "{value}" (at 0 7.5 0) (effects (font (size 1.27 1.27))))\n'
                      f'(property "Footprint" "{footprint}" (at 0 0 0) (effects (font (size 1.27 1.27)) hide))')
        pin_text = []
        for i, (number, name, electrical, net) in enumerate(pins):
            py = 3.81 - i * 2.54
            pin_text.append(f'(pin {electrical} line (at -7.62 {py:.2f} 0) (length 2.54) '
                            f'(name "{name}" (effects (font (size 1.0 1.0)))) '
                            f'(number "{number}" (effects (font (size 1.0 1.0)))))')
            gx, gy = x - 7.62, y - py
            label_x = gx - 5.08
            wiring.append(f'(wire (pts (xy {gx:.2f} {gy:.2f}) (xy {label_x:.2f} {gy:.2f})) '
                          f'(stroke (width 0) (type default)) (uuid "{uid(family + ref + number + "wire")}"))')
            wiring.append(f'(label "{net}" (at {label_x:.2f} {gy:.2f} 0) '
                          f'(effects (font (size 1.0 1.0)) (justify left bottom)) '
                          f'(uuid "{uid(family + ref + number + "label")}"))')
        libraries.append(f'(symbol "Fixture:{kind}" (pin_names (offset 0.508)) (in_bom yes) (on_board yes)\n'
                         f'{properties}\n(symbol "{kind}_0_1" '
                         '(rectangle (start -5.08 6.35) (end 5.08 -6.35) '
                         '(stroke (width 0.254) (type default)) (fill (type background))))\n'
                         f'(symbol "{kind}_1_1" {" ".join(pin_text)}))')
        symbols.append(f'(symbol (lib_id "Fixture:{kind}") (at {x} {y} 0) (unit 1) '
                       f'(in_bom yes) (on_board yes) (dnp no) (uuid "{uid(family + ref)}")\n'
                       f'(property "Reference" "{ref}" (at {x} {y-10} 0) (effects (font (size 1.27 1.27))))\n'
                       f'(property "Value" "{value}" (at {x} {y-7.5} 0) (effects (font (size 1.27 1.27))))\n'
                       f'(property "Footprint" "{footprint}" (at {x} {y} 0) (effects (font (size 1.27 1.27)) hide))\n'
                       f'(instances (project "board" (path "/{root_id}" (reference "{ref}") (unit 1)))))')
    libraries_text = "\n".join(libraries)
    wiring_text = "\n".join(wiring)
    symbols_text = "\n".join(symbols)
    contents = ('(kicad_sch (version 20250114) (generator "praxis_fixture")\n'
                f'(uuid "{root_id}") (paper "A4")\n'
                '(title_block (title "Praxis PARTIAL CONNECTIVITY FIXTURE") (rev "example-1") '
                '(comment 1 "Not a complete electrical design; omitted power/startup pins are intentional"))\n'
                f'(lib_symbols {libraries_text})\n'
                f'{wiring_text}\n{symbols_text}\n)\n')
    (ROOT / "sources" / family / "raw" / "board.kicad_sch").write_text(contents)


if __name__ == "__main__":
    make("stm32f401re", "STM32F401RE", "Package_QFP:LQFP-64_10x10mm_P0.5mm",
         ("16", "PA2"), ("17", "PA3"), ("19", "VDD"), ("18", "VSS"))
    make("atmega328p", "ATmega328P-PU", "Package_DIP:DIP-28_W7.62mm",
         ("3", "PD1"), ("2", "PD0"), ("7", "VCC"), ("8", "GND"))

