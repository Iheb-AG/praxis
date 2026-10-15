The independent watchdog uses LSI, not a precise application timebase. Do not derive a guaranteed timeout from a nominal diagram frequency. LSI tolerance and option-byte autostart assumptions require separate evidence.

Unlock using 0x5555; wait PVU/RVU=0 before protected writes and wait for synchronization before trusting readback. 0xAAAA reloads; 0xCCCC starts. Use bounded synchronization waits. Starting the watchdog can reset the target and is not authorized by retrieval or compilation. Never write option bytes as an automatic repair.

Debugger freeze behavior is not established by this contract. No watchdog start/reset hardware test has been performed. See [[peripherals/rcc]], [[features]] and [[coverage]].

Evidence: rm_features_704:page:704, rm_features_705:page:705, rm_features_706:page:706, rm_features_707:page:707, rm_features_708:page:708. Source pages were read through ingestion MCP. Editorial review only; independent sign-off pending.
