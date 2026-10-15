# Experimental STM32 knowledge inputs

These profiles import exact-commit ST device headers and pinned CMSIS 5.9.0 core headers.
`acquisition-lock.json` records each original URL and SHA-256; matching expected hashes are
in the source profile. Original file bytes and upstream Apache-2.0 notices are retained in
each `raw/` directory. Local profiles, catalog and empty definitions are MIT metadata.

No board schematic, physical package pin map, active clock, reviewed operating mode,
startup/linker assets or programming support is supplied. This is MCU-only knowledge
extraction for the intended F103C8T6, G071RBT6 and H743ZIT6 parts, not board qualification.

```bash
praxis compile-matrix --catalog sources/stm32-experimental/catalog.json --output /tmp/stm32-matrix
```

Add another licensed, hash-registered profile and catalog entry to expand extraction.
See [architecture, sequence and contribution steps](../../docs/stm32-family-expansion.md).
