# UART/timer/EXTI scenario — actual MCP results

Build/programming evidence: 2026-10-10. Physical confirmation received: 2026-10-11.
**Knowledge publication, retrieval, isolated build, exact-readback flash and reset/run passed
through actual MCP calls. Loopback, pause, jumper-removed failure and restored-jumper recovery
checks passed by user observation.**
The approved UART image has replaced the prior LED/button firmware. The user reports fitting PA2/P1-14 ↔ PA3/P1-13; no tool senses this wire.

## Evidence path

The user required hardware facts through MCP and authorized an ingestion MCP to fill missing
knowledge. The new authoring service was used for source acquisition, literal evidence search,
full page/table and CMSIS declaration reads, and schematic sheet images. No independent web search
or remembered pinout was used to supply missing facts. Source-backed editorial normalization was
performed in the authoring workspace, then reviewed receipts and publication used MCP tools.
Independent embedded engineering sign-off remains pending.

| Check | Actual result |
| --- | --- |
| New ingestion MCP | Nine tools discovered/called through real stdio; raw batches `temp/uart-ingestion-mcp-01` through `09` |
| ST documents | MB997-E-01 and UM1472 acquired via cataloged HTTPS; selected RM0090 pages staged from hash-checked cached bytes |
| Schematic visual review | Actual MCP images of P1 header and U4 MCU sheets; selected UART endpoints only |
| Publication | First attempt correctly blocked an ordinal-vs-page artifact path error; corrected profile published successfully |
| Determinism | Repeated MCP publication into a separate root; every generated file is byte-identical, see `reproduction.json` |
| Knowledge readiness | 22 actual tool calls, including expected index/prerequisite errors; all requested topology and operating docs returned |
| Build-profile readiness | One actual MCP call; same bundle revision as knowledge |
| Host checks | Seven tests: independent CRC reference, framing/payload/sequence corruption, queue wrap/full/empty, debounce, deadline/drain and time/sequence wrap |
| Full regression | 316 passed, zero skips, external tools required; follow-up run14 passed including two new PDF-preview/symlink cases |
| First target build | Link failed on compiler-generated `memset` from aggregate initialization; no artifact/board operations followed |
| Corrected target build | Actual build MCP passed isolated ARM compilation/linking with warnings as errors; approved startup/system/linker/runtime assets |
| ELF/artifact validation | Actual `validate_firmware` passed; all three linked IRQ vectors resolve to the strong application handlers |
| Hardware inspection | Explicit selected probe inspected read-only and exact new artifact plan returned |
| Packaging | Wheel and source distribution passed; raw acquisitions, private logs and temporary files excluded |
| Flash/reset/run | User approved one exact-artifact flash and reset/run; both actual MCP calls passed, every image byte matched, both attempt budgets consumed |
| Physical positive run/pause | User confirmed green heartbeat, orange activity, blue latch, no red; second USER press stops orange while green continues and blue stays on |
| Physical failure/recovery | User reports the jumper-removed error indication and restored-jumper successful operation work as described; no measured timeout or wire trace |

## Bound identities and image

- Target: `stm32f407g_disc1_mb997_e01`; MCU STM32F407VGT6/LQFP100.
- Reference PCB: MB997-E-01; physical PCB revision remains unknown.
- Bundle: `bundles/stm32f407g-disc1-e01-uart-v1`.
- Bundle revision: `1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b`.
- Artifact: `c408ee091107bbe5b741c1ec6648d2239c74098140c1a7194625552eef0dfc7d`.
- Image bytes: **2,568**; erase sector0, **0x08000000–0x08003FFF (16,384 bytes)**.
- Initial stack: `0x20020000`; 98 vector entries; EXTI0 slot22, TIM2 slot44, USART2 slot54.
- Source snapshot hash and pinned asset/compiler/container identities: [public evidence](../uart-loopback-evidence.json).

The image uses nominal HSI16 MHz and explicit bus /1, USART2 BRR139, TIM2 PSC15/ARR999 and
EXTI0 on PA0. These are application configuration choices supported by returned documents,
not measurements of the old running firmware. The retrieved reference168 MHz recipe is not used.

## Approved physical programming result

User approved the exact 2,568-byte image, sector0 erase and one reset/run. Praxis checked a fresh
plan against the scope before writing. `flash_firmware` passed, read back all 2,568 bytes and
reported halted. `control_execution(reset_run)` reverified the image and reported running during
its 1,000 ms observation window. No retry or extra execution control was requested. The persistent
server audit results exactly match the MCP responses; one flash and one control attempt are consumed.

- Flash run: `bb66e5164eef42e09b378355681b3b36`.
- Reset/run: `d562ae2f979e485ab891f311ffa67599`.
- Halted SP=`0x20020000`, PC=`0x08000424`, xPSR=`0x01000000`.
- Subsequent read-only inspection: nominal HSI16 MHz, AHB/1, CFSR/HFSR zero; USER sampled released,
  green output latch on and orange latch off. The later attachment reported state unknown;
  it did not request a halt and does not establish ongoing execution state.

This confirms the approved image bytes and the observed programming/control path. It does not
prove UART traffic or physical LED behavior. No automated USER press or packet capture was performed.

## Reported physical result, 2026-10-11

The user answered **“All these behaviors work”** to the following check: with the loopback jumper
fitted, press/release USER, wait about 12 seconds, observe green continuing to blink, orange pulsing,
blue turning on and red staying off; press USER again, observe orange stopping, green continuing
and blue remaining on. This records a successful positive-run and pause observation for this exact
programmed artifact. The blue indicator is firmware's report of its 100-frame criterion, not an
independent packet count. No measured timing, repeated-run count or held-button test was reported.

The user subsequently reported **“everything is going good i tested them”** in response to the
jumper-removed failure and restored-jumper recovery procedure. We record those functional checks
as passed by user report: red indication with blue off and green continuing when the wire is
removed, followed by normal orange activity and blue success after restoring it and starting again.
The procedure required power disconnected for both wiring changes. This observation does not
distinguish a UART receive error from timeout or measure the deadline. Repetition count was not
specified. No additional MCP flash, reset/run or other execution-control command was performed
to record these observations.

## Reproduction procedure

1. Leave the confirmed loopback jumper fitted; firmware is already programmed and starts paused.
2. Boot paused: green heartbeat; other result LEDs off.
3. Press/release USER: orange activity; blue after100 valid frames (roughly10 seconds); no red.
4. Press USER: bounded drain then pause. Green continues. Holding must not repeatedly toggle state.
5. Release/press: a fresh run clears prior result indicators and restarts sequence0.
6. Optional negative check: pause, disconnect all power, remove wire, reconnect and start.
   Red should latch; blue stay off; green continue. Floating RX may cause an error before timeout.
7. Disconnect power before restoring the wire; repeat a fresh positive run.

User observations now confirm positive-run, pause, jumper-removed failure and restored-jumper recovery behavior. Visual LEDs do not measure baud,
1 ms ISR timing, debounce duration or exact packet counts. Firmware's blue status is its own
self-report, not an independently captured wire trace. HEDG gates prove prerequisite retrieval;
linked vectors prove wiring in the ELF. Arbitrary initialization order and electrical behavior
are not established by compilation. No DMA, external UART peer or unrelated timer mode is qualified.

## Logs and configuration

- [Knowledge/build readiness and raw responses](uart-readiness.md).
- [Matching OpenCode configuration](../../examples/opencode.example.json), separate from old default launchers.
- Linked vector checks are summarized in the public evidence; detailed responses remain private.
- [Ingestion MCP documentation and sequence](../ingestion-mcp.md).
- [Application and test instructions](../../examples/stm32f407g-disc1-uart-loopback/README.md).
- Private build/inspection/plan responses: `.praxis-output/uart-loopback-prepare-02`.
- Private actual programming/control responses: `.praxis-output/uart-loopback-execution-20261010`.
- Preserved failed target build: `.praxis-output/uart-loopback-prepare-01`.
- Full test JUnit: `.praxis-output/uart-full-tests.xml`.

Raw hardware logs contain device identifiers and are kept private. Public evidence omits full
probe serial and MCU UID. Both the earlier LED/button grant and the new UART grant are consumed. Any further programming
or execution control requires its own applicable approval; read-only inspection remains separate.
