# Production and inspection notes

The idea is a single IDE task: unverified code reaches a simulated failure,
Praxis requires the missing prerequisite documents, and the correctly integrated
application moves through a real isolated build into an inspectable artifact.
The Hook's simulated-crash event and the Outro's collapse/click/brand-lock order
are retained from the user's locked narrative. Only the middle narrative was revised.

## Reality and staging

The IDE/chat, selection gestures and verification button are illustrative UI,
not a screen recording of an installed IDE client. The LLM's short unverified
snippet and fault are staged; none of that snippet was run on a physical MCU.
A clock-gate omission is not universally a HardFault cause. The simulation label
belongs to the depicted IDE target pane, and no physical failure is claimed.

Actual evidence was captured through eight MCP calls: five knowledge calls
(including the expected prerequisite refusal) and three build calls. The latter
were get_build_profile, build_firmware and validate_firmware. Only those three
build tools were exposed. No probe, flash, reset or hardware authorization was
enabled. Full private tool traces are retained separately; public source data,
returned Markdown, command arguments, checks and the build receipt are in assets/.

The UART-loopback example compiled successfully in the pinned rootless Podman
image, its ELF validated, and artifact revalidation returned valid=true:

- Artifact: 917b01317fd19e1dd2a7a34bfa559ff338a9dc7a3fd27194bce65a0de6d22d40
- Bundle: 9d2494ef9dcc4056ad83ef96f163801b5b57f89130528d5491b49d6482aa7404
- Image: sha256:4748b01d5c1d2313e5617878f9450ff1d432f8244416732d0cc57aa1867cc120
- ELF SHA-256: 7152482e9440eb57feb0f1c4bf84185fd519a6ede758fdd382f32517494e969d

The compiler profile and isolation settings are genuine. Success text is a
readable rendering of the real fields, not fabricated terminal stdout. Compilation,
ELF checks, prerequisite retrieval and actual hardware correctness are separate
claims. The build receipt reports physical_behavior="not tested".

The original Praxis logo/art is unchanged. The Framer reference is studied for
its 24 fps pacing and transition anchors; no reference footage, faces, UI assets
or audio are included. Spring parameters are authored approximations, not recovered
Framer source curves. The final edition is silent because no ElevenLabs key is
configured. Proposed narration is preserved in vo.txt; there is no synthesized voice.

## What each beat buys

1. Hook: makes the risk of plausible code concrete, explicitly as a simulation.
2. Tool refusal: makes prerequisite retrieval visible instead of claiming that MCP controls MCU execution.
3. Vault: preserves canonical links, target identity and complete source responses.
4. Collage: shows concrete source and approved integration inputs.
5. Compiler: identifies the actual cross-toolchain and target profile.
6. Isolation: exposes rootless Podman and the fixed resource/network/filesystem controls.
7. Receipt: distinguishes compilation from ELF validation and records an artifact identity.
8. Outro: collapses the same evidence surfaces into repeatable validation and the original brand lock.

## Review corrections

Initial stills caught an over-tight compiler crop and an LLM stream that continued
after the fault. The camera now retains the full key command fragments, and the
staged response finishes before the Run/fault sequence. The receipt's checks
retain line breaks, and the main verification control was enlarged for reading.

Measured final gates and contact-sheet descriptions are recorded after final export.
