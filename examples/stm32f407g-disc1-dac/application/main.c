/* Configuration-only example: main never enables or triggers analog output.
 * The retained integration entry needs separately reviewed board/electrical facts.
 */
#include "clock_setup.h"
#include "dac_controller.h"
#include <stddef.h>

_Static_assert(offsetof(DAC_TypeDef, SWTRIGR) == 0x04U, "WO trigger offset");
_Static_assert(offsetof(DAC_TypeDef, DHR12R1) == 0x08U, "holding offset");
_Static_assert(offsetof(DAC_TypeDef, DOR1) == 0x2CU, "RO output offset");
_Static_assert(offsetof(DAC_TypeDef, SR) == 0x34U, "W1C status offset");
_Static_assert(sizeof(DAC_TypeDef) == 0x38U, "all14 registers retained");
_Static_assert(DAC_CR_TSEL1 == (7UL << 3), "software trigger selection");
_Static_assert(DAC_DHR12R1_DACC1DHR == 4095U, "12-bit right alignment");
_Static_assert(DAC_SR_DMAUDR1 == (1UL << 13), "W1C underrun");
_Static_assert(RCC_APB1ENR_DACEN == (1UL << 29), "DAC gate");
_Static_assert(RCC_APB1RSTR_DACRST == (1UL << 29), "shared DAC reset");

static uint32_t mmio_read(void *unused, enum dac_register name)
{
    (void)unused;
    switch (name) {
    case D_CR: return DAC->CR;
    case D_DHR12R1: return DAC->DHR12R1;
    case D_DOR1: return DAC->DOR1;
    case D_SR: return DAC->SR;
    case D_SWTRIGR: break; /* WO: unreachable in the reviewed controller. */
    }
    return UINT32_MAX;
}
static void mmio_write(void *unused, enum dac_register name, uint32_t value)
{
    (void)unused;
    switch (name) {
    case D_CR: DAC->CR = value; break;
    case D_DHR12R1: DAC->DHR12R1 = value; break;
    case D_SWTRIGR: DAC->SWTRIGR = value; break;
    default: break; /* Neither DOR nor SR is written by this subset. */
    }
}

static bool timer_interval(void *unused, uint32_t budget)
{
    (void)unused;
    /* Caller owns TIM2 for this invocation; an existing gate rejects takeover. */
    if (!budget || SystemCoreClock != 168000000UL ||
            (RCC->CFGR & (RCC_CFGR_SWS | BUS_MASK)) != (RCC_CFGR_SWS_PLL | BUS_DIVIDERS) ||
            (RCC->PLLCFGR & PLL_MASK) != PLL_RECIPE ||
            (RCC->APB1ENR & RCC_APB1ENR_TIM2EN)) return false;
    RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;
    if (!(RCC->APB1ENR & RCC_APB1ENR_TIM2EN)) return false;
    TIM2->CR1 = 0U;
    TIM2->DIER = 0U;
    TIM2->PSC = 8399U;
    TIM2->ARR = 9U; /* 84MHz/8400/10 = nominal1ms. */
    TIM2->EGR = TIM_EGR_UG;
    TIM2->SR = 0U; /* Discard the UG-created UIF (rc_w0, not W1C). */
    TIM2->CR1 = TIM_CR1_OPM | TIM_CR1_CEN;
    bool elapsed = false;
    for (uint32_t n = 0; n < budget; ++n) {
        if ((TIM2->SR & TIM_SR_UIF) && !(TIM2->CR1 & TIM_CR1_CEN)) {
            elapsed = true; break;
        }
    }
    TIM2->CR1 = 0U;
    TIM2->DIER = 0U;
    RCC->APB1ENR &= ~RCC_APB1ENR_TIM2EN;
    return elapsed;
}
static struct dac_io controller = {
    mmio_read, mmio_write, timer_interval, NULL, false, true, false, 0U
};
volatile uint32_t praxis_dac_configured;
struct dac_result application_output(uint32_t code, bool output_reviewed)
{
    return dac_output_once(&controller, code, 1000000U, output_reviewed);
}
/* Referenced volatile relocation keeps the full integration path in the ELF;
 * main loads its address without calling it. Isolated linking must check it.
 */
static struct dac_result (*volatile output_entry)(uint32_t, bool) = application_output;

int main(void)
{
    __disable_irq();
    struct clock_result clock = clock_sequence(clock_apply, NULL, CLOCK_BUDGET);
    if (clock.completed && !(RCC->APB1ENR & RCC_APB1ENR_DACEN)) {
        RCC->APB1ENR |= RCC_APB1ENR_DACEN;
        if (RCC->APB1ENR & RCC_APB1ENR_DACEN) {
            RCC->APB1RSTR |= RCC_APB1RSTR_DACRST;
            RCC->APB1RSTR &= ~RCC_APB1RSTR_DACRST;
            praxis_dac_configured = dac_configure(&controller, 42000000U, true);
        }
    }
    (void)output_entry;
    /* EN1/EN2 remain0. No PA4 setup, timer start, trigger or analog drive. */
    for (;;) __NOP();
}
