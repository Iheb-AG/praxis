/* Source-backed F407 SysTick/SCB example. No live clock switching or boot handoff.
 * Startup/linker/runtime come from the separate pinned Praxis build MCP assets.
 * SysTick timing is calculated from checked nominal HSI16; not measured time.
 */
#include <stddef.h>
#include <stdint.h>
#include <stm32f407xx.h>
#include "core_controller.h"

_Static_assert(offsetof(SysTick_Type, LOAD) == 4U, "SysTick LOAD offset");
_Static_assert(offsetof(SysTick_Type, VAL) == 8U, "SysTick VAL offset");
_Static_assert(offsetof(SCB_Type, VTOR) == 8U, "SCB vector-table offset");
_Static_assert(offsetof(SCB_Type, SHP) + 11U == 0x23U, "SysTick priority byte");
_Static_assert(SysTick_IRQn == -1, "SysTick is a system exception, not an external NVIC line");

volatile uint32_t praxis_core_ticks;
volatile enum core_status praxis_core_status;
void SysTick_Handler(void) { ++praxis_core_ticks; }

static uint32_t read_core(void *unused, enum core_register reg)
{
    (void)unused;
    switch (reg) {
    case CORE_CLOCK: return SystemCoreClock;
    case CORE_RCC_CR: return RCC->CR;
    case CORE_RCC_CFGR: return RCC->CFGR;
    case CORE_PRIMASK: return __get_PRIMASK();
    case CORE_IPSR: return __get_IPSR();
    case CORE_CTRL: return SysTick->CTRL;
    case CORE_LOAD: return SysTick->LOAD;
    case CORE_VAL: return SysTick->VAL;
    case CORE_ICSR: return SCB->ICSR;
    case CORE_VTOR: return SCB->VTOR;
    case CORE_PRIORITY: return SCB->SHP[11];
    case CORE_VECTOR_SP: return ((volatile const uint32_t *)CORE_FLASH_TABLE)[0];
    case CORE_VECTOR_HANDLER: return ((volatile const uint32_t *)CORE_FLASH_TABLE)[15];
    case CORE_EXPECT_HANDLER: return (uint32_t)(uintptr_t)SysTick_Handler;
    default: return UINT32_MAX;
    }
}
static void write_core(void *unused, enum core_register reg, uint32_t value)
{
    (void)unused;
    switch (reg) {
    case CORE_CTRL: SysTick->CTRL = value; break;
    case CORE_LOAD: SysTick->LOAD = value; break;
    case CORE_VAL: SysTick->VAL = value; break;
    case CORE_ICSR: SCB->ICSR = value; break;
    case CORE_VTOR: SCB->VTOR = value; break;
    case CORE_PRIORITY: SCB->SHP[11] = (uint8_t)value; break;
    default: break;
    }
}
static void synchronize(void *unused) { (void)unused; __DSB(); __ISB(); }
static struct core_io core = {.read=read_core, .write=write_core, .barrier=synchronize};

int main(void)
{
    __disable_irq();
    SystemCoreClockUpdate(); /* Actual RCC state, not the bundle's optional PLL recipe. */
    praxis_core_ticks = 0U;
    praxis_core_status = core_start(&core, 1000U, 15U, true, true);
    if (praxis_core_status != CORE_OK) for (;;) __NOP();
    /* LED_A: reviewed MB997-E-01 LD4/PD12, active high. No additional wire.
     * Exclusive application ownership of this GPIO; preserve other pin fields.
     */
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIODEN;
    (void)RCC->AHB1ENR;
    GPIOD->BSRR = 1UL << (12U + 16U); /* Set inactive before output mode. */
    GPIOD->OTYPER &= ~(1UL << 12U);
    GPIOD->OSPEEDR &= ~(3UL << 24U);
    GPIOD->PUPDR &= ~(3UL << 24U);
    GPIOD->MODER = (GPIOD->MODER & ~(3UL << 24U)) | (1UL << 24U);
    __DSB(); __ISB();
    __enable_irq(); /* Handler/state, vector, priority and source are all ready. */
    uint32_t last = 0U;
    for (;;) {
        uint32_t now = praxis_core_ticks;
        if ((uint32_t)(now - last) >= 500U) {
            last = now;
            GPIOD->ODR ^= 1UL << 12U;
        }
        __WFI(); /* No delay loop or exception-mask manipulation in the ISR. */
    }
}
