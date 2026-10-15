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

## ADC1 / TIM2 exclusive startup gates

The adc_timer_gates contract requires the three ADC gate bits and TIM2EN initially
zero. An existing owner blocks this operation. Enable only ADC1EN and TIM2EN,
preserve unrelated bus gates, and read back each enable before accessing the
peripheral. ADC2/3 remain gated off. Configure shared ADC state only while all
ADCs are disabled. This contract accompanies the declared PLL clock mode.

Explicit source conflict: RM0090 Rev22 page250 prints “disabled” for both
ADC1EN encodings. ST's acquired RCC implementation sets ADC1EN to enable and
clears it to disable, with readback after enable. That resolves ADC1EN=1 for this
subset. It does not extend review to ADC2/3 operation. Evidence: rm_apb2_gate:page:250;
st_adc_gate:__HAL_RCC_ADC1_CLK_ENABLE/__HAL_RCC_ADC1_CLK_DISABLE, source SHA-256
eb6911d964b1cf8a83993b19c8feb9845e8793d7c0e5d643390b53207c8b078e.
See [[peripherals/adc_common]], [[peripherals/adc]] and [[peripherals/tim]].

## I2C1 owned-startup gate and reset

I2C1EN is APB1ENR bit21; I2C1RST is APB1RSTR bit21. Enable/read back, pulse reset and release under exclusive ownership; preserve other bits. PCLK1=42 MHz comes from the required PLL recipe. Gate enable establishes no board wiring. Sources: rm_i2c_238:page:238; rm_i2c_239:page:239; rm_i2c_247:page:247. See [[peripherals/i2c]].


DAC amendment: at the declared42 MHz PCLK1 point, exclusive ownership of both DAC channels is required before enabling/readback DACEN (APB1ENR bit29) and asserting/releasing DACRST (APB1RSTR bit29). Preserve unrelated fields. This shared reset must not disturb a live channel owner. The channel1 contract additionally needs GPIO/electrical review and the reviewed TIM2 bounded wait. See [[peripherals/dac]] and [[peripherals/tim]]. Sources: rm_dac_238:page:238; rm_dac_247:page:247; exact header macros.


## CAN1 silent-loopback gate/reset amendment

Require both CAN gates initially disabled and exclusive ownership of CAN1/CAN2 shared filters. Enable and read back CAN1EN, assert/release CAN1RST, preserve unrelated APB1 bits, and leave CAN2EN disabled. Use the reviewed PCLK1=42MHz recipe. Sources: rm_dac_239:page:239; rm_dac_247:page:247; rm_can_1070:page:1070. See [[peripherals/can]] and [[peripherals/nvic]].

## Separate checked HSI16 core context

The hsi16_core_checked mode validates HSION/HSIRDY, SW/SWS=HSI, AHB/APB divisors1 and an updated SystemCoreClock=16000000. It does not switch live clocks or change FLASH/PWR. This owned-startup context is separate from the reference HSE/PLL recipe. SysTick uses the processor clock directly and requires no APB gate. HSI frequency is nominal, not measured. Reject mismatches before starting the core timer. Sources: rm_hsi:page:219; rm_clock_v1_226:page:226; rm_clock_v1_230:page:230; rm_clock_v1_231:page:231. See [[peripherals/systick]] and [[peripherals/scb]].

## Additional owned TIM2 gate/reset contract

Preserve all previously reviewed RCC operating contracts and their individual clock bases.
The new tim2_owned_gate_reset mode requires hsi16_core_checked: nominal16MHz HSI,
HSION/HSIRDY, SW/SWS=HSI, AHB/APB divisors1 and synchronized SystemCoreClock.
It does not switch live clocks or activate the optional168MHz recipe.

Require fresh exclusive TIM2 startup ownership, no downstream TRGO consumers and TIM1EN=0.
TIM2EN (APB1ENR bit0) and TIM2RST (APB1RSTR bit0) must initially be zero. Refuse an existing
owner instead of resetting its timer. Preserve unrelated APB1 enable/reset bits. Set TIM2EN,
read back the gate before timer access, assert/read back TIM2RST, then release/read back reset.
A held reset or failed gate readback blocks dependent setup. All accesses here are words.

With APB1 divisor1, TIM2CLK=PCLK1=nominal16MHz. The multiplier2 rule under divided APB1
is preserved in earlier contracts but not used here. TIM1EN is APB2ENR bit0; keeping it gated
prevents new TIM1_TRGO events on TIM2 ITR0. The application additionally owns all consumers
of TIM2's own UG/TRGO pulse, per ES0182 section2.7.2. No GPIO/board wiring is implied.

Sources: timer_modes_evidence:rm0090/pages238–240,247–250,628;
timer_modes_evidence:es0182/pages17–19; existing checked HSI16 source records.
See [[peripherals/tim]], [[index]] and [[sources]].

## TIM2/TIM5 routed pair

Use timer_pair_gates after hsi16_core_checked. Both TIM2/TIM5 gates and resets
must initially be clear under exclusive startup ownership. Enable/read back GPIOA,
then TIM2/TIM5 gates; assert/read back/release/read back their resets. Preserve every
unrelated RCC bit. Never reset GPIOA. No downstream TRGO consumers may be active
during initialization UG, even with MMS=0. Source: timer_routes_evidence,
RM0090 pages240,243,245,248,249. See [[peripherals/gpio]] and [[peripherals/tim]].
