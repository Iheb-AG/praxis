# CRC and DMA2 compile-only smoke example

This application uses the source-backed CRC word-feed and DMA2 FIFO memory-copy contracts
from `stm32f407g-disc1-e01-features-v1`, revision
`bd8b793388dff8303e5f7d46469b48afea1807dd2f7ae9b71541eb01779a3fbc`.
Hardware facts were read through the knowledge MCP after prerequisite retrieval. It needs
no external jumper, LED, button, guessed board pin or PLL setup. The pinned build service
supplies startup/system/runtime/linker assets; the application keeps their reset-HSI startup.

The application compares word-fed hardware CRC against a portable MSB-first calculation,
then requests a 16-word DMA2 stream-0 copy and checks the resulting words. Polls have iteration
bounds; no millisecond timing is claimed. Protected configuration follows EN=0 acknowledgement;
status clearing uses direct W1C masks; errors and timeouts are reported separately.

The current result object `praxis_feature_smoke` is **not** the UART telemetry ABI. The existing
UART telemetry tool cannot read arbitrary result objects. This example has passed compilation,
full linking and ELF revalidation through real MCP, but **has not been flashed or physically
qualified**. DMA buffer reachability and a separately constrained observation contract must
be reviewed before hardware use. Compiling it does not replace installed firmware.

Run with the preinstalled pinned sandbox runtime, from the repository root:

```bash
source .praxis-output/podman-env.sh
export PATH="$PWD/.praxis-output/bin:$PATH"
.venv/bin/python tools/check_feature_modes_mcp.py \
  --bundle bundles/stm32f407g-disc1-e01-features-v1 \
  --source-directory stm32f407g-disc1-crc-dma/application \
  --output .praxis-output/feature-build-NEW
```

The client makes real knowledge/build MCP calls, follows returned prerequisites and checks
matching revisions. It never exposes hardware tools, flashes, resets or debugs the board.
Raw responses and the compile report are saved locally. A new output directory is required.
Other machines must first provision the documented sandbox and dependencies.

The recorded build artifact is
`a40462305cd0971ad4c7b03cba7a5e330322db206aaf9d4ccab783d56c160e7d`;
ELF SHA-256 `6bc1f4913c6e373da77b6c27d11face3231607fc833d64cbb983b113c7df518a`.
See [mode coverage and qualification](../../docs/peripheral-modes.md).
