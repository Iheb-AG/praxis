# F407 firmware asset profile

`manifest.json` registers every build input, hash, origin, version and license. The
asset revision is distinct from the immutable knowledge bundle revision. Source files
are held as bytes when the service starts, then staged read-only for each build.

ST startup, system source and device headers are pinned to cmsis-device-f4 commit
`3c77349ce04c8af401454cc51f85ea9a50e34fc1`. Arm core headers use CMSIS 5.9.0.
Keep both upstream license files with redistributions; each source header governs.

The Praxis linker uses the DS8626 Rev12 memory map: 1 MiB flash, 128 KiB main SRAM and
a separate 64 KiB CCM bank. It reserves a 4 KiB stack, leaves CCM unused, keeps the
98-entry ST vector table, and exports the symbols consumed by the pinned startup.
The small MIT runtime executes preinit/init arrays; it supplies no heap, syscalls,
hosted library or C++ runtime. Linking uses `-nostdlib` plus compiler `libgcc` only.

The loader cross-checks every external IRQ against the vendor header, including the
RNG → HASH_RNG handler naming alias and the reserved CRYP slot. This is implementation
review, not independent embedded sign-off. Physical qualification remains pending.

The runtime application establishes the clock. The supplied ST SystemInit sets VTOR
for the selected flash profile; it does not implement the bundle's 168 MHz PLL recipe.
The reference application explicitly chooses HSI 16 MHz and updates SystemCoreClock.

Assets are repository-local and explicitly selected by path. They are not automatically
installed in the lightweight retrieval wheel. The build extra adds ELF inspection only.
