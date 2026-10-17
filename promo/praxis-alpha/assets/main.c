/* Praxis reference: MB997-E-01 bundle; confirm your physical revision and SB20.
 * LED_A=PD12 (LD4), LED_B=PD13 (LD3), B1=PA0, all active high.
 * Source: bundles/stm32f407g-disc1-e01-m1 wiki/schemas/custom_pcb_netlist.md.
 * C11 flash profile supplies ST startup and SystemCoreClockUpdate.
 */
#include <stm32f407xx.h>
#include <stdbool.h>

static volatile uint32_t milliseconds;

void SysTick_Handler(void) { ++milliseconds; }

static bool select_hsi(void)
{
    uint32_t budget = 1000000U;
    RCC->CR |= RCC_CR_HSION;
    while (!(RCC->CR & RCC_CR_HSIRDY)) {
        if (--budget == 0U) return false;
    }
    /* Switch first; only then remove AHB division. No HSE/PLL assumption. */
    RCC->CFGR = (RCC->CFGR & ~RCC_CFGR_SW) | RCC_CFGR_SW_HSI;
    budget = 1000000U;
    while ((RCC->CFGR & RCC_CFGR_SWS) != RCC_CFGR_SWS_HSI) {
        if (--budget == 0U) return false;
    }
    RCC->CFGR &= ~RCC_CFGR_HPRE;
    SystemCoreClockUpdate();
    return SystemCoreClock == 16000000U;
}

int main(void)
{
    __disable_irq();
    if (!select_hsi()) for (;;) { __NOP(); }

    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN | RCC_AHB1ENR_GPIODEN;
    (void)RCC->AHB1ENR; /* Clock-enable synchronization. */
    const uint32_t leds = (1U << 12) | (1U << 13);
    const uint32_t modes = (3U << 24) | (3U << 26);
    GPIOD->BSRR = leds << 16; /* Establish OFF before enabling output mode. */
    GPIOD->OTYPER &= ~leds;
    GPIOD->OSPEEDR &= ~modes;
    GPIOD->PUPDR &= ~modes;
    GPIOD->MODER = (GPIOD->MODER & ~modes) | (1U << 24) | (1U << 26);
    GPIOA->MODER &= ~3U;
    GPIOA->PUPDR &= ~3U; /* Board's external pull-down; SB20 must be closed. */

    if (SystemCoreClock % 1000U || SysTick_Config(SystemCoreClock / 1000U))
        for (;;) { __NOP(); }
    __enable_irq();

    uint32_t last_toggle = milliseconds, changed_at = milliseconds;
    bool led_a = false, candidate = false, stable = false;
    for (;;) {
        const uint32_t now = milliseconds;
        if ((uint32_t)(now - last_toggle) >= 500U) {
            last_toggle = now;
            led_a = !led_a;
            GPIOD->BSRR = led_a ? (1U << 12) : (1U << 28);
        }
        const bool pressed = (GPIOA->IDR & 1U) != 0U;
        if (pressed != candidate) { candidate = pressed; changed_at = now; }
        if (candidate != stable && (uint32_t)(now - changed_at) >= 50U) {
            stable = candidate;
            GPIOD->BSRR = stable ? (1U << 13) : (1U << 29);
        }
        __WFI();
    }
}
