/* Finite sequencing shared by the target and instrumented host model. */
#ifndef PRAXIS_ADC_SEQUENCE_H
#define PRAXIS_ADC_SEQUENCE_H
#include <stdint.h>
enum adc_step {
    ADC_PRECONDITIONS, ADC_GATES, ADC_CONFIGURE, ADC_REFERENCE, ADC_POWER,
    ADC_TIMER_CONFIGURE, ADC_TIMER_UPDATE, ADC_TIMER_CLEAR, ADC_TIMER_START,
    ADC_TIMER_ELAPSED, ADC_FLAGS_CLEAR, ADC_START, ADC_READY, ADC_READ,
    ADC_STEP_COUNT
};
enum adc_action { ADC_REJECT = -1, ADC_PENDING = 0, ADC_DONE = 1 };
struct adc_result { uint32_t completed, failed_step, attempts, raw; };
struct adc_context { uint32_t owned, raw; };
typedef enum adc_action (*adc_action_fn)(enum adc_step, void *);
static inline struct adc_result adc_sequence(adc_action_fn action, void *context,
                                             uint32_t budget)
{
    struct adc_result result = {0U, ADC_PRECONDITIONS, 0U, 0U};
    if (!action || !context || !budget) return result;
    for (unsigned step = 0; step < ADC_STEP_COUNT; ++step) {
        result.failed_step = step;
        enum adc_action status = ADC_PENDING;
        for (uint32_t i = 0; i < budget; ++i) {
            ++result.attempts;
            status = action((enum adc_step)step, context);
            if (status != ADC_PENDING) break;
        }
        if (status != ADC_DONE) return result;
    }
    result.completed = 1U;
    result.failed_step = ADC_STEP_COUNT;
    result.raw = ((struct adc_context *)context)->raw;
    return result;
}
#endif
