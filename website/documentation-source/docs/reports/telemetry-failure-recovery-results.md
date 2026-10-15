# UART telemetry failure/recovery results

Date: 2026-10-11. Milestone 4 qualification of the existing 250 ms telemetry firmware through
actual Praxis MCP. No new compilation, flash, halt, reset or resume was requested. The user
performed physical power cycles and button/wiring actions.

- Target reference: STM32F407G-DISC1 / MB997-E-01; physical PCB revision unconfirmed.
- Artifact: `c192a736ed2958697e4c89022094ae3b896b01529c8f391e074068c1c2c71688`.
- Bundle: `1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b`.
- Image: 3,060 bytes, SHA-256
  `ae0743630fda736973949f8c23e0d11e28fdce953e4b588fa6d93835bc20d8b6`.

## Observations

Initial MCP discovery exposed the telemetry tool without programming/control tools. Probe
enumeration returned zero probes, so no target inspection was attempted in that session.
The user then reported removing the jumper with all power disconnected, reconnecting ST-LINK
and pressing/releasing USER once.

The disconnected-loopback observation **passed failure detection**. Five coherent samples
reported application state `failed`, failure `uart_error`, zero validated frames and blue success
false. Between the first and last samples the timer advanced by 4,250 nominal ticks; UART error
and received-byte counters each advanced by 134. Transmitted bytes remained 13. The application
had latched failure and stopped transmitting; receive interrupts continued reporting errors.
All image bytes matched before/after sampling, including five block-word discrepancies accepted
only after two matching individual-word reads each. CPU execution state was running.

Restored-loopback recovery was **observed with anomalies**. The first window reported a timeout
after 75 validated frames, zero UART errors and a stopped frame count. The next window crossed
a second reported button press into run 2, so it was not accepted as a stable recovery window.
Two subsequent windows in run 2 passed: +42/+43 validated frames, +798/+817 TX and RX bytes,
+4,250 timer ticks each, zero UART/queue errors and blue success on. Every sample in those two
windows was running with at least 100 validated frames in the current run.

The first intended pause **did not pass**. Its samples showed healthy run 3 progressing by 42
frames, with button count 3. The intervening transition from run 2 to run 3 was not captured.
No conclusion about its cause is established. A follow-up without a requested stimulus confirmed
run 3 still progressing (+43 frames) without an active failure.

After a repeated USER press held about half a second, the final pause **passed**: all five samples
reported paused with no active failure, while frames, TX/RX bytes and UART IRQ counts remained
unchanged and the timer advanced 4,250 ticks. Run 3 retained 804 validated frames and blue success;
the button count was 4. Six block-word discrepancies passed the required individual-word
confirmations during that final read. The CPU remained running; the application is paused.

Across this experiment, eight telemetry windows (40 coherent samples) verified the same installed
image before/after each window. Firmware and knowledge bundles were not edited. The previous
successful loopback observations remain in [earlier telemetry evidence](../telemetry-evidence.json).

## Interpretation and limits

The result demonstrates detection of an unsuccessful run with the jumper reported removed.
It does not independently identify the electrical cause of UART errors on the disconnected RX
input. Timer ticks are firmware counters, not oscillator measurements. Wiring and button actions
are user reports; the counters and exact image checks are MCP observations.

This is **not a clean repeatability qualification**. Failure detection, subsequent recovery and
final pause are demonstrated, but the initial restored-loopback timeout and unexpected restart
remain unresolved. Next qualification work should capture the transition and distinguish firmware,
connection and observation effects; no cause should be inferred from the successful later windows.

Follow the [test procedure and sequence](../scenarios/telemetry-failure-recovery.md).
Sanitized MCP responses and phase checks are recorded in
[qualification evidence](../telemetry-qualification-evidence.json).
Independent engineering review, physical board revision, measured timing and broader debugger
qualification remain open in [publication readiness](../PUBLICATION_READINESS.md).
