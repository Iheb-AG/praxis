# Reviewed board wiring and operating assumptions

Target: `stm32f407g_disc1_mb997_e01`; MCU: `STM32F407VGT6`; package: `Package_QFP:LQFP-100_14x14mm_P0.5mm`; board revision: `MB997-E-01`; silicon: `Unspecified; errata review pending`.

**Documented reference board revision; physical board revision and modifications must be checked. Not hardware-qualified by Praxis.**

Board model: STM32F407G-DISC1. Reference revision: MB997-E-01.

Applicability: Reference E-01 circuit only. User confirmed the board model but not the PCB revision. Verify MB997 revision and SB20 before flashing; no equivalence to other revisions is asserted.

Coverage: partial. Net memberships are complete for the imported scope; this is not a full-board electrical audit.

## GPIO signal assignments

| Signal | Aliases | Kind | MCU pin | Endpoint | Active level | Pull | Circuit nets | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| b1 | USER_BUTTON;B1 | button | PA0 | U4:23 | high | external-down | B1_SERIES;B1_SIGNAL;B1_SUPPLY;GND;PA0;VDD | schematic_e01:page:4/USER+WAKE-UP;page:7/MCU |
| ld3 | LED_B;LD3;ORANGE_USER_LED | led | PD13 | U4:60 | high | none; output | GND;LD3_ANODE;PD13 | schematic_e01:page:4/LEDs;page:7/MCU |
| ld4 | LED_A;LD4;GREEN_USER_LED | led | PD12 | U4:59 | high | none; output | GND;LD4_ANODE;PD12 | schematic_e01:page:4/LEDs;page:7/MCU |
| ld5 | RED_LED;LD5;RED_USER_LED | led | PD14 | U4:61 | high | none; output | GND;LD5_ANODE;PD14 | schematic_e01:page:4/LEDs;page:7/MCU |
| ld6 | BLUE_LED;LD6;BLUE_USER_LED | led | PD15 | U4:62 | high | none; output | GND;LD6_ANODE;PD15 | schematic_e01:page:4/LEDs;page:7/MCU |

## Clock and timing facts

| Fact | State | Value | Sources |
| --- | --- | --- | --- |
| button_bridge | documented | SB20 must be closed for B1 to reach PA0. R39 is an external 220 kohm pulldown; use no internal pull unless an explicitly reviewed change requires one. Pressing B1 drives the signal high through R38; R35 is series protection. | schematic_e01:page:4/USER+WAKE-UP |
| clock_recipe | design-assumption | Optional 8 MHz HSE to 168 MHz recipe: M=8,N=336,P=2,Q=7, AHB/1, APB1/4, APB2/2. This does not establish the current firmware clock; verify clock source/bridges/supply first. | rcc_review:reviewed clock recipe |
| gpio_sequence | documented | After clock gating/readback, preload both LED outputs OFF using BSRR reset bits before selecting push-pull output mode. Configure only the selected GPIO fields; read PA0 through IDR. Preserve SWD pins. | gpio_review:GPIO MODER/OTYPER/PUPDR/IDR/BSRR reviewed semantics |
| oscillator | documented | E-01 MCU sheet shows X2=8 MHz. Clock options and board revisions affect fitted paths; verify the actual board before selecting HSE crystal or bypass mode. | schematic_e01:page:7/X2 |
| startup_boundary | unresolved | Startup/vector table, linker script, actual clock setup, system clock synchronization and safe SysTick interrupt enablement must come from the firmware project. Full linking and physical execution are not established by this bundle. | board:startup scope |
| systick_clock_source | documented | The pinned CMSIS SysTick_Config sets CTRL.CLKSOURCE=1, TICKINT=1, ENABLE=1 and programs the system exception priority. It uses the processor clock, not HCLK/8. | cmsis_core:core_cm4.h:SysTick_Config |
| systick_ms_formula | documented | Synchronize SystemCoreClock to the actual core clock, then require SystemCoreClock % 1000 == 0 and SysTick_Config(SystemCoreClock / 1000U) == 0. CMSIS writes LOAD=ticks-1. Do not divide the argument by 8. | cmsis_core:core_cm4.h:SysTick_Config |
| timing_source | design-assumption | Proposed software design: 1 ms SysTick interrupt incrementing a volatile uint32_t counter. GPIO button polling needs no EXTI. Provide the SysTick vector/handler and check the helper return code before enabling the application. | cmsis_core:SysTick_Config; SysTick_Type; SysTick_IRQn |
| uart_loopback_connector | documented | USART2_TX=PA2/U4:25/P1:14 and USART2_RX=PA3/U4:26/P1:13. Connect one external jumper only with board unpowered. ST-LINK VCP is not connected to the MCU UART by default. | schematic_uart:page:2/P1; schematic_mcu:page:7/U4; uart_connector:page:18;page:26/Table7 |

## Circuit interpretation

Paths cross only explicitly reviewed fitted components. Adjacent nets remain distinct. Solder bridges and board modifications must match the reference before physical use.

- b1: MCU → SB20 → R35 → B1; pull R39; pressed rail path R38.
- ld3: MCU → R36 → LD3; anode LD3:1, cathode LD3:2.
- ld4: MCU → R40 → LD4; anode LD4:1, cathode LD4:2.
- ld5: MCU → R41 → LD5; anode LD5:1, cathode LD5:2.
- ld6: MCU → R42 → LD6; anode LD6:1, cathode LD6:2.

## Omitted scope

- This is a reviewed GPIO circuit subset, not the entire MB997 netlist. Connector branches and other GND/VDD endpoints are omitted.
- ST-LINK, power regulation, decoupling, audio, USB, MEMS, reset and oscillator wiring are not represented as connectivity.
- C36 is not fitted in E-01 and is excluded from the button conduction path.
- Other PCB revisions, reworked solder bridges, external attachments and physical behavior are unverified.

Editorial reviewer: Codex source-backed editorial review via Praxis ingestion MCP. Basis: Actual MCP source evidence: RM0090 Rev22 selected pages; MB997 E-01 rendered pages 2/7; UM1472 Rev9 pages 18/26. Reviewed operating subset only; independent engineering sign-off pending.. Independent hardware sign-off remains separate.

See [[index]], [[schemas/components]], [[schemas/custom_pcb_netlist]], [[peripherals/rcc]], [[peripherals/gpio]], and [[sources]].
