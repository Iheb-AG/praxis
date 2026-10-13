# UART, timer and interrupt MCP readiness test

Evidence: actual local MCP stdio responses. No external model or source-document lookup was used in this replay.

Scenario status: **blocked at knowledge readiness**.

## Configured knowledge server

# Project Praxis hardware execution index

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**



Index-first gate enforced: True.

Missing pin/net/connector queries: PA2, PA3, USART2_TX, USART2_RX, P1:14, P1:13.

Missing documents: tim2, exti, syscfg.

Unreviewed operating semantics: none.

## Configured build server

Bundle revision: `53474b5de83dddffbdccfb86057c6ec9ad362f1949afd6a74e90effb2c27fc9b`.

Only get_build_profile was called; compilation and board operations were not requested.

## Separate discovery-bundle diagnostic

This separate process does not change OpenCode configuration or the build/hardware profile.

Missing topology: PA2, PA3, USART2_TX, USART2_RX, P1:14, P1:13.

Missing documents: none.

Unreviewed operating semantics: tim2, syscfg, exti.

## Interpretation

MCP transport and routing responses are evidence of retrieval behavior. A returned header declaration is not reviewed initialization guidance.

The user reports the jumper is fitted. This test cannot validate its placement because the MCP does not return the requested UART connector nets.

No firmware was generated, built or flashed. The previous LED/button firmware was not replaced.

Required next work: publish source-backed UART connector nets and TIM2/SYSCFG/EXTI operating semantics, then repeat this MCP test with matching knowledge/build profiles.

Raw responses are retained in the private development workspace; this exported report is self-contained.
