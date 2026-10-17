# Praxis promotional film

A 28-second, 1920×1080, 30 fps promotional film for the experimental alpha.
Open `final.mp4` in a video player, or serve this directory and open `preview.html`.
MP4 exports are kept local and can be uploaded as release assets separately from the editable source:

```bash
python3 -m http.server 4190 --directory promo/praxis-alpha
# http://localhost:4190/preview.html
```

`index.html` is the editable animation. It uses the Motionmaxxing seek-safe GSAP
runtime and one Three.js illustration. Its clock starts paused for rendering;
to inspect a particular time, run `window.__seek(8.2)` in browser developer tools.
Use a local HTTP server for WebGL assets. All visual assets and fonts are local.

The original Praxis logo/banner and documentation capture are used unchanged.
`assets/mcp-capture.json` records four successful read-only MCP calls. Full GPIO,
RCC, index and netlist responses are retained beside it. The visible document
views are crops/compositions of this evidence; the tool responses were not truncated.
The XML view is an illustrative transcription of the two net memberships, not a
newly exported KiCad schematic. The silicon package is an artistic illustration,
not a rendering of the Discovery PCB. No hardware was flashed for this video.

This edition is silent because ElevenLabs credentials were not available.
No synthesized voice, licensed stock soundtrack, fabricated compiler result or
new physical test is presented. Experimental-alpha wording is retained.

## Editing and reproducing

Requires Node 22+, Chromium, ffmpeg/ffprobe, Python with NumPy and Pillow,
and the installed Motionmaxxing skill. The repository's Praxis dependencies
are needed only to recapture MCP evidence, not to play the film.

```bash
export MOTIONMAXXING_SKILL="$HOME/.codex/skills/motionmaxxing"
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node "$MOTIONMAXXING_SKILL/scripts/render.mjs" \
  promo/praxis-alpha/index.html promo/praxis-alpha/final.mp4
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 python3 promo/praxis-alpha/review.py \
  promo/praxis-alpha/final.mp4 --out promo/praxis-alpha/look-final --expect 28 --strict
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node "$MOTIONMAXXING_SKILL/scripts/lint.mjs" \
  promo/praxis-alpha/index.html
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node promo/praxis-alpha/check-seek.mjs
```

`STORYBOARD.md` explains the creative choices; `NOTE.md` records the measured
checks and visual review. `SOURCES.json` records local source hashes.
`prepare_assets.py` regenerates the document data from the captured responses.
The animation, MP4 and captures are separate from Praxis compiler/server code
and from the independent `website/` repository.

Third-party runtime notices remain in the copied source files. Inter retains
its SIL Open Font License; Three.js, its dependencies and GSAP retain their own
notices and license terms. The project's MIT license does not replace those terms.
