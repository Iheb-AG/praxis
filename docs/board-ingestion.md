# Board-specific schematic ingestion

Praxis distinguishes chip capabilities, a board reference revision, and the user's physical card.
The new `stm32f407g-disc1-e01-m1` bundle describes a reviewed **MB997 E-01 GPIO subset** for
STM32F407G-DISC1. The user confirmed the model, but not the PCB revision. Check the MB997
marking, solder bridges and modifications before using this reference for physical firmware.

## Retrieve the Discovery reference

```bash
.venv/bin/praxis compile \
  --profile sources/stm32f407g-disc1/profile.json \
  --output bundles/stm32f407g-disc1-e01-m1
.venv/bin/praxis lint --bundle bundles/stm32f407g-disc1-e01-m1
```

OpenCode's `temp/opencode.json` selects this bundle. Disconnect/reconnect the server after
changing its selection; an existing process retains its original target and immutable snapshot.
The three MCP tool names have not changed. In a fresh session:

```text
read_wiki_index()
query_schematic_netlist("LED_A")
query_schematic_netlist("LED_B")
query_schematic_netlist("USER_BUTTON")
read_peripheral_doc("rcc")
read_peripheral_doc("gpio")
```

Expected reference mappings:

| Application alias | Board device | MCU connection | Active level | Circuit |
| --- | --- | --- | --- | --- |
| LED_A | LD4, green | PD12, U4:59 | High | R40, 510 ohm, LED cathode to GND |
| LED_B | LD3, orange | PD13, U4:60 | High | R36, 680 ohm, LED cathode to GND |
| RED_LED | LD5, red | PD14, U4:61 | High | R41, 680 ohm, LED cathode to GND |
| BLUE_LED | LD6, blue | PD15, U4:62 | High | R42, 680 ohm, LED cathode to GND |
| USER_BUTTON | B1 | PA0, U4:23 | High when pressed | SB20 closed, R35 series, R39 external 220 kohm pulldown, R38 supply series |

These are normalized facts from the official [MB997 E-01 schematic](https://www.st.com/resource/en/schematic_pack/mb997-f407vgt6-e01_schematic.pdf)
pages 4 and 7, cross-checked with [UM1472](https://www.st.com/resource/en/user_manual/dm00039084-discovery-kit-with-stm32f407vg-mcu-stmicroelectronics.pdf).
The source records contain downloaded PDF hashes and extraction revisions. They are an editorial
review, not independent sign-off or confirmation that another PCB revision is equivalent.

A signal query returns complete net membership **within the declared imported scope**, additional
circuit nets as separate tables, and the reviewed board/component context. It never joins the two
sides of a resistor or solder bridge into one electrical net. The imported subset omits connector
branches and most board circuitry; its global GND/VDD lists do not claim all physical endpoints.

## Native KiCad input

1. Place the `.kicad_sch` and all referenced subsheets inside the target source directory.
2. Register every sheet in the profile's `sources` with connectivity authority.
3. Select the root sheet's source ID as `netlist`, with `netlist_format: "kicad"`.
4. Supply the exact MCU value, footprint, primary reference and reviewed package pin map.
5. Compile. KiCad exports XML; safe parsing disables DTDs, entities and external expansion.

Pre-exported KiCad XML is also accepted. Component values, pin names/numbers, sheets, properties,
library identities, DNP status and net memberships are retained. Recognized standard library parts
provide limited component classification; unknown roles remain `other` and cannot satisfy a
reviewed LED/button circuit. No electrical role is guessed from a component reference prefix.

Native local labels keep KiCad's sheet-qualified names, such as `/UART_RX`. Do not strip prefixes
or merge identically named signals across sheets. Declare aliases against the actual exported
name. The hand-authored UART XML fixtures use unqualified names; live export tests explicitly
account for the native root-sheet namespace while comparing every endpoint.

KiCad 9.0.4 was used for the local export evidence. The fixture schematic format requires KiCad
9 or newer. Install instructions are available from [KiCad](https://www.kicad.org/download/details/ubuntu/).
Compilation and retrieval do not download or install it automatically.

## PDF-only input

Web acquisition can download a schematic PDF and preserve text, page identity and source bytes:

```bash
.venv/bin/praxis scrape \
  --catalog sources/stm32f407g-disc1/web-sources.json \
  --output imports/discovery-board
```

PDF text/table extraction does not reconstruct wires, junctions or component polarity. For v1,
review the original drawing and author a `ReviewedSchematic` transcription. This is the adapter
used for ST's PDF-only reference. Its origin and partial scope are explicit; it is not described
as a KiCad export or automatic geometry recognition.

The transcription records components with values, kinds, fitted status, terminal names and
properties; each net lists its endpoints and source locators. MCU terminal numbers must match
the reviewed package map. Passive terminal IDs assigned locally because the PDF does not print
numbers must be identified as transcription-local in component properties. Do not present them
as verified physical package pin numbers.

Register the normalized JSON as a connectivity source and select `netlist_format: "reviewed"`.
It must carry the exact MCU/package/board revision, reviewed status, coverage and omissions.
Source provenance may reference separately reviewed evidence records containing official URLs,
observed source hashes and page/figure locators. Directly registered web extraction artifacts
additionally require the archive's exact-byte review receipt through `web_imports`.

## Reviewed board semantics

Set the profile's `board` field to a registered semantics source containing `BoardDefinition`.
The Discovery example is `sources/stm32f407g-disc1/reviewed/board.json`.

For LEDs, declare the MCU endpoint, aliases, active level, LED anode/cathode and explicit series
resistor path. For buttons, declare switch terminals, the MCU path, pressed supply path and
external pull resistor. The v1 circuit validator supports these simple passive circuits; it rejects
unsupported transistor/expander paths rather than guessing. Normally open switches may have
multiple physical terminals on each of their two nets.

Add `required_workflows: ["led_button_polling"]` to require distinct LED_A, LED_B and USER_BUTTON
mappings plus clock/timing facts. The compiler rejects disconnected paths, wrong pin numbers,
reversed polarity, contradictory pulls, unfitted series bridges, missing required facts, duplicate
identities, unknown provenance and inconsistent revisions. Nets remain distinct during validation.

Generate current authoring schemas with:

```bash
.venv/bin/praxis schema --kind profile
.venv/bin/praxis schema --kind reviewed-netlist
.venv/bin/praxis schema --kind board
```

Clock/timing records distinguish documented facts, proposed design assumptions and unresolved
items. The 168 MHz plan is a recipe, not a measurement or proof of firmware initialization.
The pinned CMSIS `SysTick_Config` uses the processor clock: for a 1 ms tick, synchronize
`SystemCoreClock`, use `SystemCoreClock / 1000U`, check divisibility and the helper's return value,
and provide the required vector/handler. Dividing that helper argument by 8 is incorrect.

GPIO button polling stops at RCC → GPIO and needs no EXTI configuration. A SysTick-based time
counter still requires reviewed core exception/startup integration. Startup code, a linker script
and an actual build are separate firmware work; no build result may be inferred from this bundle.

## Publication and review

Generation is deterministic for identical inputs and tool versions. Markdown tables are contiguous;
any document over 65,536 bytes fails publication. Cross-links, identities, provenance and dependency
graphs are checked before atomic publication. Existing revisions are never overwritten.

Published bundles serve offline without KiCad, Clang, XML/PDF parsers or their source trees.
Runtime indexes are derived from the published Markdown. Independent source/semantics review
is recorded separately using the exact bundle revisions, as described in [Milestone 1](milestone1.md).
