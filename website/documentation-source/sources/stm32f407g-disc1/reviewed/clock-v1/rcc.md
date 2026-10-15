Supported workflow: USART2 bring-up under an explicitly assumed 8 MHz HSE crystal,
3.3 V VDD, internal regulator in Scale 1, and the PLL configuration below. This
is an example operating point, not a measurement of the user's board.

| Quantity | Value | Evidence |
| --- | --- | --- |
| HSE | 8,000,000 Hz; crystal mode, HSEBYP=0 | profile:clock_plan; clock_review:SystemClock_Config |
| PLLM / PLLN / PLLP / PLLQ | 8 / 336 / 2 / 7 | profile:clock_plan; header:RCC_PLLCFGR_* |
| VCO input / output | 1 MHz / 336 MHz | profile:clock_plan; arithmetic |
| SYSCLK / HCLK | 168 MHz / 168 MHz (AHB /1) | profile:clock_plan; arithmetic |
| PCLK1 / PCLK2 | 42 MHz / 84 MHz (APB1 /4, APB2 /2) | profile:clock_plan; arithmetic |
| PLL48CLK | 48 MHz | profile:clock_plan; arithmetic; no USB accuracy certification |
| FLASH latency | 5 wait states at the assumed supply | clock_review:SystemClock_Config |

Keep interrupts masked and quiesce peripherals before changing clocks. First
enable HSI and wait for HSIRDY with a finite timeout; select HSI and confirm SWS
before disabling the PLL. Enable the PWR bus clock, read it back, and select
Scale 1. Program and read back five FLASH wait states before increasing HCLK.
Do not infer prefetch availability without checking the silicon revision.

Enable HSE in the board's documented crystal/bypass mode and wait for HSERDY.
Wait for PLLRDY=0 before replacing PLLM/N/P/Q and PLLSRC. Program AHB /1, APB1 /4,
and APB2 /2 before the 168 MHz switch. Enable the PLL, wait for PLLRDY=1, select
PLL as SYSCLK and confirm SWS=PLL. Every readiness wait needs a finite deadline
and an error path that prevents further peripheral initialization.

Enable GPIOAEN and USART2EN, then read back the enable registers before peripheral
access. USART2 baud generation uses PCLK1=42 MHz, not the doubled APB timer clock.
Reserved fields must retain their documented values; ready/status bits are not
ordinary writable controls. Resetting USART2 is an explicit operation on an idle
peripheral, never a blanket write to the entire reset register.

PWR and FLASH are prerequisites inside this clock stage. Their full peripheral
catalogs, electrical design, startup, and errata review remain outside this
UART fixture. Header-only entries marked unknown are declarations, not permission
to operate other clock domains. Unknown facts required by a new workflow need a
reviewed import before use.

Sources: `rcc_review` (RM0090 RCC/PWR/FLASH operating semantics), `clock_review`
(ST's UART example SystemClock_Config), and `profile:clock_plan` (local declared
assumptions). See [[peripherals/gpio]], [[peripherals/usart]], and [[sources]].


## UART/timer scenario: explicitly selected HSI operating point

Use HSI nominal 16 MHz, AHB /1, APB1 /1, APB2 /1 for this application. Enable HSI and bound the HSIRDY wait; select HSI and bound the SWS confirmation before changing divisors or disabling PLL. Keep FLASH latency conservatively unchanged while lowering frequency. Synchronize SystemCoreClock and verify the selected RCC bits. Enable/read back GPIOA/GPIOD, USART2/TIM2 on APB1 and SYSCFG on APB2. Reset only owned USART2 and TIM2. The 168 MHz recipe above is optional and is not used here. Sources: rm_clock:page:218; rm_hsi:page:219; rm_apb2_gate:page:250. See [[peripherals/tim]], [[peripherals/syscfg]] and [[peripherals/exti]].

## Explicit clock-mode publication

The new pll_hse8_168mhz mode requires exact FLASH latency_168mhz and PWR voltage_scale modes. The latter requires RCC power_interface_gate. These form a separate acyclic mode graph; retrieving RCC bus-gate information does not require changing any clock. Retrieve [[peripherals/flash]] and [[peripherals/pwr]] before implementing the PLL recipe. PLLM/PLLSRC are shared with PLLI2S; do not change them while either PLL is enabled. HSEBYP can change only after HSE is disabled and no longer ready. This startup subset rejects active PLLI2S/CSS ownership instead of altering their state. Preserve calibration/reserved bits; RCC_CR reset has undefined HSICAL bits and is not asserted as a complete number. All waits need a bounded failure exit. Failed switching does not permit dependent peripheral initialization.

Evidence: rm_clock_v1_80/81/82,218/219/220/221,225/226/227/228/229/230/231/247, with page locators matching each suffix. These complete pages and declarations were read through ingestion MCP. Editorial synthesis only; no physical clock/supply/errata qualification. See [[features]] and [[coverage]].
