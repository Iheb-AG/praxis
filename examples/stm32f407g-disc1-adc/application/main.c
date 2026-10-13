/* ADC1 VREFINT smoke example, authored from actual Praxis MCP responses.
 * Bundle: stm32f407g-disc1-e01-adc-v1. Supply/clock assumptions must hold.
 * No wire, DMA, NVIC, calibrated voltage, or UART telemetry ABI is used.
 * This owned-startup example is not a general live reconfiguration API.
 */
#include <stdint.h>
#include <stddef.h>
#include <stm32f407xx.h>
#include "clock_setup.h"
#include "adc_sequence.h"

_Static_assert(offsetof(ADC_TypeDef, DR) == 0x4CU, "ADC DR offset");
_Static_assert(offsetof(ADC_Common_TypeDef, CCR) == 4U, "shared CCR offset");
_Static_assert(ADC_SMPR1_SMP17 == (7UL << 21), "channel17 sampling field");
_Static_assert(ADC_CCR_ADCPRE == (3UL << 16), "common prescaler field");
_Static_assert(ADC_CR2_EOCS == (1UL << 10), "EOCS enables overrun detection");

#define ADC_GATES_MASK (RCC_APB2ENR_ADC1EN | RCC_APB2ENR_ADC2EN | RCC_APB2ENR_ADC3EN)
#define ADC_BUDGET 1000000UL /* Finite iterations, not a wall-clock timeout. */
volatile struct clock_result praxis_adc_clock_result;
volatile struct adc_result praxis_adc_result;

static enum adc_action adc_apply(enum adc_step step, void *context)
{
    struct adc_context *ctx = context;
    switch (step) {
    case ADC_PRECONDITIONS:
        return (SystemCoreClock == 168000000UL &&
                (RCC->CFGR & (RCC_CFGR_SWS | BUS_MASK)) == (RCC_CFGR_SWS_PLL | BUS_DIVIDERS) &&
                (RCC->PLLCFGR & PLL_MASK) == PLL_RECIPE &&
                (RCC->APB2ENR & ADC_GATES_MASK) == 0U &&
                (RCC->APB1ENR & RCC_APB1ENR_TIM2EN) == 0U) ? ADC_DONE : ADC_REJECT;
    case ADC_GATES:
        ctx->owned = 1U;
        RCC->APB2ENR |= RCC_APB2ENR_ADC1EN;
        RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;
        return ((RCC->APB2ENR & ADC_GATES_MASK) == RCC_APB2ENR_ADC1EN &&
                (RCC->APB1ENR & RCC_APB1ENR_TIM2EN)) ? ADC_DONE : ADC_REJECT;
    case ADC_CONFIGURE:
        ADC1->CR2 = 0U;
        ADC1->CR1 = 0U;
        ADC1->SQR1 = 0U;
        ADC1->SQR3 = 17U;
        ADC1->SMPR1 = ADC_SMPR1_SMP17; /* 480 cycles = 22.86us at 21MHz. */
        return ADC_DONE;
    case ADC_REFERENCE:
        ADC123_COMMON->CCR = (1UL << ADC_CCR_ADCPRE_Pos) | ADC_CCR_TSVREFE;
        return ADC_DONE;
    case ADC_POWER: ADC1->CR2 = ADC_CR2_ADON | ADC_CR2_EOCS; return ADC_DONE;
    case ADC_TIMER_CONFIGURE:
        TIM2->CR1 = 0U;
        TIM2->DIER = 0U;
        TIM2->PSC = 8399U;
        TIM2->ARR = 9U; /* 84MHz / 8400 / 10 = 1kHz; one pulse = 1ms. */
        return ADC_DONE;
    case ADC_TIMER_UPDATE: TIM2->EGR = TIM_EGR_UG; return ADC_DONE;
    case ADC_TIMER_CLEAR: TIM2->SR = 0U; return ADC_DONE; /* Discard UG-created UIF. */
    case ADC_TIMER_START: TIM2->CR1 = TIM_CR1_OPM | TIM_CR1_CEN; return ADC_DONE;
    case ADC_TIMER_ELAPSED:
        return ((TIM2->SR & TIM_SR_UIF) && !(TIM2->CR1 & TIM_CR1_CEN)) ? ADC_DONE : ADC_PENDING;
    case ADC_FLAGS_CLEAR: ADC1->SR = 0U; return ADC_DONE; /* rc_w0, not W1C. */
    case ADC_START: ADC1->CR2 = ADC_CR2_ADON | ADC_CR2_EOCS | ADC_CR2_SWSTART; return ADC_DONE;
    case ADC_READY: {
        uint32_t status = ADC1->SR;
        if (status & ADC_SR_OVR) return ADC_REJECT;
        return (status & ADC_SR_EOC) ? ADC_DONE : ADC_PENDING;
    }
    case ADC_READ:
        if ((ADC1->SR & (ADC_SR_EOC | ADC_SR_OVR)) != ADC_SR_EOC) return ADC_REJECT;
        ctx->raw = ADC1->DR; /* Exactly one read; hardware clears EOC. Never write DR. */
        return ctx->raw <= 4095U ? ADC_DONE : ADC_REJECT;
    default: return ADC_REJECT;
    }
}

static void adc_stop(struct adc_context *ctx)
{
    if (!ctx->owned) return; /* Never touch an existing owner after a rejected guard. */
    if (RCC->APB2ENR & RCC_APB2ENR_ADC1EN) {
        ADC1->CR2 = 0U;
        ADC123_COMMON->CCR &= ~ADC_CCR_TSVREFE;
    }
    if (RCC->APB1ENR & RCC_APB1ENR_TIM2EN) {
        TIM2->CR1 = 0U;
        TIM2->DIER = 0U;
    }
    /* Leave owned gates enabled; no unsupported clock-disable sequence asserted. */
}

#ifndef PRAXIS_ADC_MODEL
int main(void)
{
    __disable_irq();
    praxis_adc_clock_result = clock_sequence(clock_apply, 0, CLOCK_BUDGET);
    if (praxis_adc_clock_result.completed) {
        struct adc_context context = {0U, 0U};
        praxis_adc_result = adc_sequence(adc_apply, &context, ADC_BUDGET);
        adc_stop(&context);
    }
    for (;;) __NOP(); /* Inspect the result with an approved debugger; no UART ABI. */
}
#endif
