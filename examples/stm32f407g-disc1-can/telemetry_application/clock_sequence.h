/* Supported startup example: finite ordered stages, shared by target/model checks. */
#ifndef PRAXIS_CLOCK_SEQUENCE_H
#define PRAXIS_CLOCK_SEQUENCE_H
#include <stdint.h>

enum clock_step {
    CLOCK_PRECONDITIONS, CLOCK_HSI_ENABLE, CLOCK_HSI_READY,
    CLOCK_HSI_SELECT, CLOCK_HSI_SELECTED, CLOCK_SAFE_DIVIDERS,
    CLOCK_PLL_DISABLE, CLOCK_PLL_DISABLED, CLOCK_HSE_DISABLE,
    CLOCK_HSE_DISABLED, CLOCK_PWR_GATE, CLOCK_PWR_SCALE,
    CLOCK_PWR_READY, CLOCK_FLASH_LATENCY, CLOCK_FLASH_ACK,
    CLOCK_HSE_CRYSTAL, CLOCK_HSE_ENABLE, CLOCK_HSE_READY,
    CLOCK_PLL_CONFIGURE, CLOCK_PLL_ENABLE, CLOCK_PLL_READY,
    CLOCK_PLL_SELECT, CLOCK_PLL_SELECTED, CLOCK_PUBLISH_FREQUENCY,
    CLOCK_STEP_COUNT
};
enum clock_action { CLOCK_REJECT = -1, CLOCK_PENDING = 0, CLOCK_DONE = 1 };
struct clock_result { uint32_t completed, failed_step, attempts; };
typedef enum clock_action (*clock_action_fn)(enum clock_step, void *);

static inline struct clock_result clock_sequence(clock_action_fn action, void *context,
                                                  uint32_t per_step_budget)
{
    struct clock_result result = {0U, CLOCK_PRECONDITIONS, 0U};
    if (action == 0 || per_step_budget == 0U) {
        return result;
    }
    for (unsigned step = 0U; step < CLOCK_STEP_COUNT; ++step) {
        result.failed_step = step;
        enum clock_action status = CLOCK_PENDING;
        for (uint32_t attempt = 0U; attempt < per_step_budget; ++attempt) {
            ++result.attempts;
            status = action((enum clock_step)step, context);
            if (status != CLOCK_PENDING) {
                break;
            }
        }
        if (status != CLOCK_DONE) {
            return result; /* Never advance dependent initialization after failure. */
        }
    }
    result.completed = 1U;
    result.failed_step = CLOCK_STEP_COUNT;
    return result;
}
#endif
