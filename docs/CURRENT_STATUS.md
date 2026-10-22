# Current supported baseline

Generated from `current-status.json`; regenerate with `praxis status --registry current-status.json --format markdown`.

**Experimental alpha. Full MCU acceptance and qualified release are not established.**

Selected bundle: `bundles/stm32f407g-disc1-e01-timer-irq-v1`
Revision: `9d2494ef9dcc4056ad83ef96f163801b5b57f89130528d5491b49d6482aa7404`

## Knowledge scope

- published_register_blocks: **42/42** — Recognized register blocks only; declarations do not establish operating support
- blocks_with_reviewed_subset: **22/42** — At least some reviewed operating knowledge; not every mode of these blocks
- blocks_with_mode_contract: **19/42** — At least one explicit mode contract; legacy subsets may lack contracts
- declared_workflows_knowledge_ready: **24/39** — Only workflows declared in this profile; neither exhaustive nor hardware qualification
- Reviewed mode contracts: **43**

## Authored workflows

| Workflow | Knowledge state |
| --- | --- |
| `adc1_internal_reference` | Ready within authored scope |
| `arm_flash_vector_table` | Ready within authored scope |
| `arm_hsi16_core_checked` | Ready within authored scope |
| `can1_external_bus` | Blocked |
| `can1_rx_guarded_loopback_irq` | Ready within authored scope |
| `can1_silent_loopback` | Ready within authored scope |
| `can1_silent_loopback_irq` | Ready within authored scope |
| `crc_word_feed` | Ready within authored scope |
| `dac_channel1_software_trigger` | Ready within authored scope |
| `dac_channel1_wired_output` | Blocked |
| `dma2_memory_copy` | Ready within authored scope |
| `feature_adc` | Ready within authored scope |
| `feature_can` | Blocked |
| `feature_dac` | Blocked |
| `feature_eth` | Blocked |
| `feature_flash` | Blocked |
| `feature_fsmc_bank1` | Blocked |
| `feature_i2c` | Blocked |
| `feature_pwr` | Ready within authored scope |
| `feature_rtc` | Blocked |
| `feature_sdio` | Blocked |
| `feature_usb_otg_global` | Blocked |
| `flash_latency_168mhz` | Ready within authored scope |
| `gpio_led_button` | Ready within authored scope |
| `i2c1_controller_transmit` | Ready within authored scope |
| `i2c1_wired_transmit` | Blocked |
| `iwdg_configure_refresh` | Ready within authored scope |
| `pll_hse8_168mhz` | Ready within authored scope |
| `rng_pll_polling` | Ready within authored scope |
| `spi1_wired_polling` | Blocked |
| `systick_1khz_interrupt` | Ready within authored scope |
| `systick_core_polling` | Ready within authored scope |
| `tim2_capture_ch1_external` | Blocked |
| `tim2_pwm_ch1_pin` | Blocked |
| `tim2_pwm_ch1_reference` | Ready within authored scope |
| `tim2_software_capture_ch1` | Ready within authored scope |
| `tim2_tim5_capture_irq` | Ready within authored scope |
| `tim2_tim5_pwm_capture_loopback` | Ready within authored scope |
| `uart_timer_interrupts` | Ready within authored scope |

Exact missing requirements and scopes are included in the JSON status output.

## Recorded verification evidence

These are historical reports, not tests rerun against the current checkout. Counts are not added together.

### software evidence

**Selected bundle**

```json
{
  "applies_to_selected_bundle": true,
  "artifact_identity": {
    "artifact_id": "70aab2ee7184e666527f94ccc6bbf6d63bbaa7d74260baf7376d52c45d2be2bf",
    "elf_sha256": "af4983585e87ef15cd5311c7d2900406baa0ac3b297e9f172bb31a2d0c26d823",
    "image_sha256": "0995463eb5fbab7f13168824b2107f93c69f0aa6f7030179b21254b2222cb6c3"
  },
  "bundle_revision": "9d2494ef9dcc4056ad83ef96f163801b5b57f89130528d5491b49d6482aa7404",
  "kind": "software",
  "limits": [
    "Fresh exclusively owned privileged Thread/MSP startup only; no RTOS or live handoff. No AIRCR/system-exception writes, nested IRQ, DMA or other timer mode claim.",
    "All probe/model/qualification fixtures are explicitly synthetic; historical polling observations do not qualify the new artifact.",
    "Read-only physical preflight could not select the previously connected probe; no physical SRAM observation, reset or flash of the new artifact occurred.",
    "Same HSI basis for both timers; no independent absolute frequency/duty calibration.",
    "IRQ receipts and cleanup snapshots remain firmware self-reports, not arbitrary code/order proof or physical authentication.",
    "No full MCU acceptance, formal repeatability, independent signoff or confirmed physical PCB revision."
  ],
  "path": "docs/timer-irq-evidence.json",
  "recorded_values": {
    "application_acceptance": {
      "actual_mcp_calls": 94,
      "cases": 17,
      "full_mcu_accepted": false,
      "passed": true,
      "plan_sha256": "4eec49083a8b2e844f35c52a03ae3d77f72208c01ebed696b1627e74490ffc8c"
    },
    "artifact": {
      "artifact_id": "70aab2ee7184e666527f94ccc6bbf6d63bbaa7d74260baf7376d52c45d2be2bf",
      "asset_revision": "22310c7ad54daa553cf5cb11e4db08e4c8f9e93e191f3f12ec8410dd1fb40b59",
      "bundle_revision": "9d2494ef9dcc4056ad83ef96f163801b5b57f89130528d5491b49d6482aa7404",
      "elf_sha256": "af4983585e87ef15cd5311c7d2900406baa0ac3b297e9f172bb31a2d0c26d823",
      "flashed": false,
      "image_bytes": 5984,
      "image_sha256": "0995463eb5fbab7f13168824b2107f93c69f0aa6f7030179b21254b2222cb6c3",
      "image_validated": true,
      "source_sha256": "32d6349ec3728635e058f104f2821993adbb4f0bba6ad8821bb5156420012664"
    },
    "date": "2026-10-15",
    "docker_mcp": {
      "architecture": "amd64",
      "calls": 162,
      "image": "project-praxis:timer-irq",
      "image_id": "sha256:1c980518f63b2287f10d5b3144b971da48dba7785484edf69d8ebd151b1ce8e5",
      "limits": "Local architecture only; no compiler, physical board, or remote registry publication tested.",
      "negative_and_runtime_checks": [
        "MISSING_FILE",
        "INTEGRITY_ERROR",
        "non_root",
        "read_only_filesystem_and_bundle",
        "no_optional_extras"
      ],
      "os": "linux",
      "passed": true,
      "sessions": 4
    },
    "full_regression": {
      "passed": 1462,
      "required_external_tools": true,
      "seconds": 398.07,
      "skipped": 0
    },
    "knowledge_mcp": {
      "calls": 52,
      "passed": true
    },
    "physical_status": "not tested for the new IRQ artifact",
    "scope": "Exact TIM2_CH2 PA1 PWM paired with TIM5_CH3 PA2 IRQ50 capture: software/source/model/ELF/MCP checks; physical IRQ qualification pending"
  },
  "sha256": "0b865740080884c9eaa24ce19acf40ab54fbe8360dff4acd6b3e117f914263c1",
  "verification": "recorded_report_not_reexecuted"
}
```

### physical evidence

**Different historical bundle — does not qualify this baseline**

```json
{
  "applies_to_selected_bundle": false,
  "artifact_identity": {
    "artifact_id": "ba3ff2fcb1e2b2083af0849bdef3135f19d6bb04fca70184d13bb4e6106c246a",
    "elf_sha256": "033557658fc6f24d6912e2b47b154ac0abab4c87b735974b2338ff5f7cc51797",
    "image_sha256": "4c3ae24a5c68b25aa1a2b258d7e4ac7c935a6bda9adcec1375b5caff2d026ec2"
  },
  "bundle_revision": "2dbfa901ec294c0f8edc5e37e87d41a3aa69f169dcce18b4acf088d48f5c0167",
  "kind": "physical",
  "limits": [
    "Firmware self-reports and timer capture words, not independent waveform/optical measurement.",
    "Same HSI clock for both timers; no absolute frequency or duty-cycle calibration.",
    "Heartbeat progress republishes one terminal test, not repeated executions.",
    "Physical PCB revision remains unconfirmed.",
    "No timer IRQ/DMA,32-bit hardware wrap, repeatability, all-mode MCU acceptance or independent release review established."
  ],
  "path": "docs/timer-route-physical-evidence.json",
  "recorded_values": {
    "artifact_id": "ba3ff2fcb1e2b2083af0849bdef3135f19d6bb04fca70184d13bb4e6106c246a",
    "date": "2026-10-15",
    "elf_sha256": "033557658fc6f24d6912e2b47b154ac0abab4c87b735974b2338ff5f7cc51797",
    "image_sha256": "4c3ae24a5c68b25aa1a2b258d7e4ac7c935a6bda9adcec1375b5caff2d026ec2",
    "physical_pcb_revision": null,
    "reported_trial_passed": true,
    "scope": "One approved image: wired PWM/capture success, clean no-edge timeout after operator jumper removal, and a new successful boot after restoration. Not full MCU or statistical repeatability qualification."
  },
  "sha256": "9f628f38156705f379a37b9348d761e7d41566e6bf08a6c493b89dbf5b5017af",
  "verification": "recorded_report_not_reexecuted"
}
```

## Independent review and limits

Independent review record for selected bundle: **missing**.
Current-checkout full regression: **not assessed by this command**.

- Knowledge readiness is limited to authored workflows, not all MCU features.
- Evidence counts are historical reported results, never summed or transferred between revisions.
- A matching bundle does not establish matching application, toolchain or current source code.
- Physical records apply only to their exact artifacts and fixtures; no whole-workflow qualification is inferred.
- Independent review records are declarations, not authenticated signatures; release qualification is separate.
