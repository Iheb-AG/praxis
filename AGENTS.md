# Required working practices

- Run checks required for the current task with `PRAXIS_REQUIRE_EXTERNAL_TOOLS=1`.
- If a required dependency is missing, report the exact missing dependency and wait for the user to install it. Do not substitute a skipped check, suppress a failure, or report the task as verified.
- Preserve target-specific hardware facts and publication policy in versioned source profiles/contracts, rather than manufacturer branches in the core compiler.
- Published Markdown has no fixed 64 KiB ceiling. Preserve complete tables, source provenance, integrity checks and prerequisite validation.
- Keep historical published bundles immutable. Choose a new output directory for a changed revision.
- The `website/` directory is an independent documentation repository. Do not automatically synchronize it during compiler work.
- Prioritize full STM32F407 coverage before further family expansion. Do not equate complete declaration discovery or passing example builds with all-mode MCU acceptance; retain unsupported workflows, physical qualification and independent-review gaps explicitly.
