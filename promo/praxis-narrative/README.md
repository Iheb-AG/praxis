# Praxis — Reference-aware firmware

37-second promotional film, 1920×1080, 24 fps. The requested IDE/simulated-crash
Hook and collapse/verification/brand-lock Outro are preserved. The middle shows
actual Praxis knowledge-gate responses and one genuine isolated build.

Play `final.mp4`, or serve this directory and open `preview.html`:

```bash
python3 -m http.server 4190 --directory promo/praxis-narrative
# http://localhost:4190/preview.html
```

The film is silent: no ElevenLabs credentials are configured. The proposed
narration is retained in `SCRIPT_SHOTLIST.md` and `vo.txt`.

`index.html` is the editable animation. All art, fonts and runtime dependencies
are local. Its renderer clock starts paused; inspect any time using
`window.__seek(20)` in browser developer tools. The IDE is an illustrative
reconstruction; the MCP error, returned Markdown, compiler profile and artifact
results are actual captures, with full source data in `assets/`.

The simulated Hook is a narrative device, not physical failure footage. No
board, flash, reset or debug tools are enabled by `capture.py`. Compilation and
ELF validation do not establish physical firmware correctness. The reference
video is studied only for timing; its assets, people, footage and soundtrack
are not included.

## Reproduce

Requires Node 22+, Chromium, ffmpeg/ffprobe and Python with NumPy and Pillow.
Praxis's installed dependencies and the pinned rootless Podman toolchain image
are required only to recapture actual evidence. Missing required dependencies
must be installed rather than bypassed.

```bash
export MOTIONMAXXING_SKILL="$HOME/.codex/skills/motionmaxxing"
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node "$MOTIONMAXXING_SKILL/scripts/render.mjs" \
  promo/praxis-narrative/index.html promo/praxis-narrative/final.mp4 --fps 24
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 python3 promo/praxis-narrative/review.py \
  promo/praxis-narrative/final.mp4 --out promo/praxis-narrative/look-final --expect 37 --strict
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node "$MOTIONMAXXING_SKILL/scripts/lint.mjs" \
  promo/praxis-narrative/index.html
PRAXIS_REQUIRE_EXTERNAL_TOOLS=1 node promo/praxis-narrative/check-seek.mjs
```

`STORYBOARD.md` records creative choices, `NOTE.md` records inspection and measured
gates, and `SOURCES.json` pins the actual evidence. MP4 exports are ignored by
Git and can be uploaded separately as release/social assets.

The original Praxis artwork is unchanged. Inter, GSAP, Three.js and their
vendored dependencies retain the notices and terms included in `runtime/`.
The project's MIT license does not replace third-party terms.
