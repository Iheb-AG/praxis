# Project Praxis — Reference-aware firmware

37-second production script and visual shot list. Only the Solution (8–16s) and
Sandbox (16–28s) are revised. The Hook and Outro below retain the user's events,
duration and order. This document proposes the next film; it does not describe
newly executed compiler or hardware tests.

## Reference and timing

Reference: [Framer: All Design, No Code, Real Websites](https://www.youtube.com/watch?v=6xJWQRVl9nw).
A private 1280×720 preview was inspected at its native 24 fps. The decoded preview
contains 886 frames / 36.916667 seconds. Praxis's requested 37-second master uses
888 frames at 24 fps. Original footage, people, UI, branding and audio are not
incorporated into the Praxis deliverable.

The reference is not a continuous rapid-cut montage: it combines short openings,
a longer moving product view, an editor handoff, a short moving collage, focused
selection/layout actions, then a click and logo. Detected transition candidates
include frames 377 (15.708s), 442 (18.417s), 674 (28.083s) and 810 (33.750s).
These are analysis anchors, not claims that every pixel spike is a hard edit.
Dense contact sheets of 8–16s and 16–28s were also inspected. The shot list follows
those action rhythms while preserving the user's exact 8/16/28/37-second act boundaries.
Original spring constants cannot be inferred exactly from the preview; the spring
settings below are authored starting values, not measured Framer implementation values.

## Read-through script

**0–8s — Hook, locked.**
Open on an IDE chat window where an LLM writes unverified low-level code that
triggers a simulated microcontroller crash: “Hard Fault / Missing RCC clock gate”.
No rewrite or extra narrative event is proposed here.

**8–16s — Solution, revised.**
Voice: “Praxis gives your assistant source-backed hardware context. MCP gates
require the prerequisite documents, in order.”

Visible action: the assistant invokes Praxis through its MCP client. An out-of-order
peripheral-document request is refused. The index, clock and pin documents arrive
in their required order; the requested peripheral context becomes available.
The same documents expand into the linked Markdown vault, with a complete register
table and source reference retained. Small, legible operating text belongs to the
actual tool response rather than an invented dashboard.

Visible copy, in sequence: “Hardware context through MCP.” → actual
`PREREQUISITE_REQUIRED` response → `index → rcc → gpio → usart` →
“Vectorless Markdown. Explicit sources.”

A downstream `nvic` branch may be shown as available. It advances only if this
filmed example actually requests interrupt setup. The assistant writes the code;
Praxis does not intercept chat messages or prove the generated instruction order.

**16–28s — Sandbox, revised.**
Voice: “Generated C is cross-compiled inside a rootless Podman container.
Pinned assets and ELF checks produce an artifact you can inspect.”

Visible action: the source-backed documents hand off to the generated C/H snapshot
and pinned integration assets. The separate build MCP invokes the fixed target
compiler inside Podman. Camera selection exposes networking disabled, read-only
inputs and bounded resources. Real diagnostics lead to separate compilation and
ELF-validation results, then an artifact receipt. The receipt remains the carried
object for the locked Outro.

Visible copy, in sequence: `build_firmware("application")` →
`arm-none-eabi-gcc` → “Rootless Podman” → “Compile passed” → “ELF validated”.
Success strings and artifact identity must be captured from a successful real run
before rendering; this script does not supply fabricated logs or benchmark values.

**28–37s — Outro, locked.**
UI panels collapse inward, a final verification click triggers, and the minimalist
Project Praxis logo and brand mark lock into place. No change to this event order
or the nine-second allocation is proposed.

## Frame-addressable visual shot list

Frames use start-inclusive, end-exclusive ranges at 24 fps. Sound directions are
production cues, not an already generated soundtrack. The Hook/Outro are recorded
as locked spans rather than rewritten into new subscenes.

| Time / frames | Shot and belief bought | Motion, composition and handoff | Copy / sound |
| --- | --- | --- | --- |
| 0.000–8.000 / 000–192 | **HOOK — LOCKED.** IDE chat, unverified low-level code, simulated crash. | Preserve the requested narrative and existing staging; no new hook action. | Preserve “Hard Fault / Missing RCC clock gate”. |
| 8.000–9.000 / 192–216 | Praxis enters the assistant's tool workflow. The viewer sees an actual MCP interaction. | Stay inside the same IDE from the Hook; reveal its Praxis tool activity. A response surface moves into focus while the editor recedes. | “Hardware context through MCP.” Close, dry UI click. |
| 9.000–10.000 / 216–240 | A peripheral read is refused because required documents were not retrieved. | Macro on the actual error line; halt the response surface, not the MCU. Preserve a single dominant plane. | `PREREQUISITE_REQUIRED`; exact missing-prerequisite text from the MCP capture. One restrained error tick. |
| 10.000–11.000 / 240–264 | The assistant follows the declared route. | Source document names travel through one horizontal response viewport: index, RCC, GPIO, then USART. Their entries overlap slightly; no equal-sized floating-card wall. | Actual tool-call labels. Soft page movements, no repeated success chimes. |
| 11.000–12.375 / 264–297 | The response is connected to an actual local vault. | Match the reference's editor handoff: the same response plane expands into the real vault/editor view. Camera lands on `wiki/index.md` and its explicit links. | `[[peripherals/rcc]]`, `[[peripherals/gpio]]`. Lower the sound bed for reading. |
| 12.375–13.750 / 297–330 | Praxis has a specific identity and source-backed content. | At the reference's icon-entry beat, the original Praxis mark accompanies the selected MCP connection, then yields to the actual source document. Do not invent an IDE installation gesture. | “Project Praxis” appears once in the genuine connection context. One short settling hit. |
| 13.750–15.708 / 330–377 | Vectorless retrieval preserves usable hardware context. | The selected document fills the editor, echoing the reference's populated-canvas shot. Magnify one intact register-table region and its source reference; an explicit link carries the camera to its prerequisite. | “Vectorless Markdown. Explicit sources.” No embedding/vector-search animation. |
| 15.708–16.000 / 377–384 | Knowledge hands off to verification. | Match the reference's collage entrance on frame 377: document planes move outward to expose the C/H snapshot and approved asset manifests. This is a transition inside the Solution's existing final seven frames. | Voice finishes; a short sweep carries into the Sandbox. |
| 16.000–18.417 / 384–442 | A reproducible build has concrete inputs. | The reference's moving collage becomes Praxis's real source snapshot, approved startup/header inventory and toolchain identity. Keep the selected application at least twice the visual area of supporting material. The camera travels; no capability-stat wall. | `get_build_profile()` and real target/compiler identity. Low rhythmic mechanical bed. |
| 18.417–19.250 / 442–462 | The separate build MCP starts cross-compilation. | Match the reference's return-to-editor transition at frame 442. The selected source plane settles into the actual build-tool/terminal capture. | `build_firmware("application")`. Cursor parks, presses in 2 frames, then the tool answers. |
| 19.250–20.667 / 462–496 | The compiler is the target toolchain. | Macro into the actual command profile; keep `arm-none-eabi-gcc` dominant. Camera moves past Cortex-M4, Thumb, C11 and the exact device define without enlarging every flag into a title. | `-mcpu=cortex-m4 -mthumb -mfloat-abi=soft -DSTM32F407xx`. |
| 20.667–21.417 / 496–514 | There is a deliberate verification boundary. | Borrow the reference's short held-selection rhythm. Keep the compiler view alive through one moving focus/selection, with a 0.75-second breath before the boundary reveal. | Brief sound dip; no fabricated progress percentage or simulated terminal flood. |
| 21.417–23.667 / 514–568 | Isolation controls are visible and specific. | Following the reference's element-selection cadence, select the actual Podman profile fragments in turn. Camera carries between selections within one real command surface. | `--network=none`, `--read-only`, `--cap-drop=ALL`; then the actual resource limits. Three restrained selection ticks. |
| 23.667–25.417 / 568–610 | Outputs are inspected as structured artifacts. | Use the reference's selection-to-layout gesture: existing command/output regions align into the compiler result, ELF inspection and artifact-manifest surfaces. One region dominates at a time. | Real build diagnostics and image-check records; no “firmware proven correct” wording. |
| 25.417–26.333 / 610–632 | A successful compile is distinct from a valid image. | Match the reference's outlined-compartments beat: the two actual outcomes occupy separate fields in the real receipt, with camera emphasis switching from compile to ELF status. | “Compile passed” then “ELF validated”, only if both are true in the captured run. Two separated, quiet confirmations. |
| 26.333–28.000 / 632–672 | Verification produces an inspectable artifact. | The receipt fills with the actual artifact identity and source/bundle references. The camera pulls back while preserving the receipt's pose, preparing the inward collapse at 28 seconds. | Actual hash/ID from the build capture. A slight upward sound movement leads into the locked Outro. |
| 28.000–37.000 / 672–888 | **OUTRO — LOCKED.** Inward panel collapse → verification click → logo/brand lock. | Preserve the user's sequence. The reference's click-to-mark handoff near frame 810 informs timing without changing this span. | Existing final verification action and minimal Praxis identity. |

## Art and motion direction for the editable sections

- Dark-mode world: the documentation's charcoal `#0d1015`, near-black `#07090c`,
  clear ink `#f4f6f8`, cyan `#7cc7e6` for selected evidence. Use the original stone
  imagery as a quiet textured plane, not a competing full-brightness logo behind every result.
- Real IDE/tool/document fragments supply the geometry and typography. UI text becomes
  readable by a macro camera move, with the key fragment at least 55% frame width
  and essential text at least 4% frame height. Do not redesign the IDE as a generic dashboard.
- Author at 24 fps. Main entries land over 8–12 frames; smaller related surfaces trail
  by 2–4 frames. Exit acceleration carries through cuts. Preserve readable holds.
- Spring starting values: mass 1, stiffness 240, damping 24; constrain overshoot to
  approximately 2–3% and settle before a result must be read. These are authored
  settings for the Praxis render, not recovered reference constants. Use one consistent
  spring grammar across panel motions; camera travel stays smooth.
- Cursor press: two-frame compression, response one frame later. A response must reflect
  the actual captured tool result. No spinning decorative progress indicators.
- Match the reference's internal action density and its frame-377/frame-442 handoffs.
  Preserve the user-owned act seam at frame 672 even though the reference's next large
  transition is detected two frames later. This is a 37-second adaptation, not a
  claim of pixel-identical or mathematically identical motion.

## Production accuracy notes

These notes do not change the locked Hook or Outro.

1. The Hook is a **simulated** failure. A missing RCC gate does not universally cause
   a Cortex-M HardFault; writes to a clock-disabled peripheral can have other outcomes.
   Do not present that label as a measured diagnostic from the physical board.
2. HEDG gates prerequisite **retrieval** within the knowledge MCP session. They do not
   enforce firmware write order or share a state gate with the independent build server.
3. The Sandbox compiles/links and statically validates the image; it does not execute
   the firmware in an MCU simulator, prove electrical correctness or flash a board.
4. Bind the locked final verification click to repeatable artifact validation. Do not
   turn it into a flash action or imply that a general UI click grants hardware consent.
5. Use the actual pinned image digest, approved header paths and captured diagnostics
   in filming. The shot-list command fragments are editorial crops, not executable
   shell instructions or newly completed test results.
6. Keep the original Praxis logo unchanged in the minimal lockup. Do not borrow the
   reference's logo, faces, website content, sound recording or other brand assets.
7. The user-locked nine-second Outro and reference-style final lock take precedence
   over the skill's default short-ending preference. No render-gate pass is claimed
   for this screenplay; the eventual animation must be reviewed with that exception explicit.

## Sources and next action

- Reference timing: the public Framer video linked above; private full-frame analysis and dense contact sheets.
- Current behavior: `praxis/routing.py` (retrieval gates), `docs/build-service.md`
  (separate build MCP and ELF checks), `praxis/verify.py` (Podman and target compiler profile).
- Brand/evidence assets: `docs/images/`, the independent website capture in
  `promo/praxis-alpha/brand/`, and four real read-only responses in
  `promo/praxis-alpha/assets/mcp-capture.json`.

Next: animate and capture the revised 8–28-second sections at 24 fps, joining them
to the unchanged Hook and Outro. Capture a real build/validation result before
rendering successful-result text. The prior 28-second MP4 remains a separate cut.
