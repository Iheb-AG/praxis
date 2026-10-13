/* Instrument the target's actual callback. RAM registers are not silicon or a
 * timing simulator; emulate reviewed command/status side effects explicitly. */
#include <stdlib.h>
#include <stdio.h>
#include <stm32f407xx.h>
static RCC_TypeDef model_rcc;
static ADC_TypeDef model_adc;
static ADC_Common_TypeDef model_common;
static TIM_TypeDef model_tim;
#undef RCC
#undef ADC1
#undef ADC123_COMMON
#undef TIM2
#define RCC (&model_rcc)
#define ADC1 (&model_adc)
#define ADC123_COMMON (&model_common)
#define TIM2 (&model_tim)
#define PRAXIS_ADC_MODEL 1
#include "main.c"
uint32_t SystemCoreClock = 168000000UL;

struct model {
    struct adc_context adc;
    int fault, order_ok;
    uint32_t seen, calls, elapsed_polls, ready_polls, reads, ug_seen, fresh_delay;
};
#define SEEN(m, s) (((m)->seen & (1UL << (s))) != 0U)
static enum adc_action instrument(enum adc_step step, void *context)
{
    struct model *m = context;
    ++m->calls;
    int allowed = step == ADC_PRECONDITIONS || SEEN(m, step - 1U);
    if (step == ADC_TIMER_START) allowed &= TIM2->SR == 0U && m->ug_seen;
    if (step == ADC_START) allowed &= m->fresh_delay && (ADC1->CR2 & ADC_CR2_ADON);
    if (step == ADC_READ) allowed &= SEEN(m, ADC_READY) && !m->reads;
    if (!allowed) { m->order_ok = 0; return ADC_REJECT; }
    int fail = m->fault == (int)step;
    if (step == ADC_TIMER_ELAPSED) {
        ++m->elapsed_polls;
        if (!fail && m->elapsed_polls == 3U) {
            TIM2->SR |= TIM_SR_UIF;
            TIM2->CR1 &= ~TIM_CR1_CEN;
            m->fresh_delay = 1U;
        }
    } else if (step == ADC_READY) {
        ++m->ready_polls;
        if (m->fault == -5) ADC1->SR |= ADC_SR_OVR | ADC_SR_EOC;
        else if (!fail && m->ready_polls == 2U) {
            ADC1->CR2 &= ~ADC_CR2_SWSTART;
            ADC1->SR |= ADC_SR_EOC;
            ADC1->DR = m->fault == -6 ? 4096U : 1500U;
        }
    } else if (fail) return ADC_REJECT;
    enum adc_action action = adc_apply(step, &m->adc);
    if (step == ADC_TIMER_UPDATE && action == ADC_DONE) {
        if (TIM2->EGR != TIM_EGR_UG || TIM2->PSC != 8399U || TIM2->ARR != 9U || TIM2->DIER) {
            m->order_ok = 0; return ADC_REJECT;
        }
        TIM2->EGR = 0U; /* Self-clearing UG; pending update exists before SR=0. */
        TIM2->CNT = 0U;
        TIM2->SR |= TIM_SR_UIF;
        m->ug_seen = 1U;
    }
    if (step == ADC_READ) {
        ++m->reads;
        ADC1->SR &= ~ADC_SR_EOC; /* Reading DR clears EOC on silicon. */
    }
    if (action == ADC_DONE) m->seen |= 1UL << step;
    return action;
}

int main(int argc, char **argv)
{
    struct model model = {{0U, 0U}, argc > 1 ? atoi(argv[1]) : -1, 1, 0U, 0U, 0U, 0U, 0U, 0U, 0U};
    uint32_t budget = argc > 2 ? (uint32_t)atoi(argv[2]) : 3U;
    RCC->CFGR = RCC_CFGR_SWS_PLL | BUS_DIVIDERS;
    RCC->PLLCFGR = PLL_RECIPE;
    RCC->APB1ENR = RCC_APB1ENR_PWREN; /* An unrelated owner's gate must survive. */
    RCC->APB2ENR = RCC_APB2ENR_SPI1EN;
    ADC1->SR = ADC_SR_EOC | ADC_SR_OVR; /* Stale flags must not become results. */
    if (model.fault == -3) SystemCoreClock = 16000000U;
    if (model.fault == -4) RCC->APB2ENR |= RCC_APB2ENR_ADC2EN;
    if (model.fault == -7) RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;
    if (model.fault == -8) RCC->PLLCFGR ^= 1U;
    struct adc_result result;
    if (model.fault == -2) {
        result = (struct adc_result){0U, ADC_START, 1U, 0U};
        (void)instrument(ADC_START, &model);
    } else result = adc_sequence(instrument, &model, budget);
    adc_stop(&model.adc);
    printf("{\"completed\":%u,\"failed_step\":%u,\"attempts\":%u,\"calls\":%u,"
           "\"raw\":%u,\"reads\":%u,\"order_ok\":%d,\"fresh_delay\":%u,"
           "\"owned\":%u,\"stopped\":%u,\"preserved\":%u,\"sample_cycles\":%u,"
           "\"channel\":%u,\"eoc_cleared\":%u}\n",
           result.completed, result.failed_step, result.attempts, model.calls, result.raw,
           model.reads, model.order_ok, model.fresh_delay, model.adc.owned,
           !(ADC1->CR2 & ADC_CR2_ADON) && !(ADC123_COMMON->CCR & ADC_CCR_TSVREFE) &&
           !(TIM2->CR1 & TIM_CR1_CEN),
           (RCC->APB1ENR & RCC_APB1ENR_PWREN) && (RCC->APB2ENR & RCC_APB2ENR_SPI1EN),
           (ADC1->SMPR1 & ADC_SMPR1_SMP17) == ADC_SMPR1_SMP17 ? 480U : 3U,
           (uint32_t)(ADC1->SQR3 & ADC_SQR3_SQ1), !(ADC1->SR & ADC_SR_EOC));
    return 0;
}
