#ifndef PRAXIS_SEQUENCE_H
#define PRAXIS_SEQUENCE_H
#include <stdbool.h>

typedef bool (*praxis_stage)(void);

/* Used by both target examples and the instrumented host ordering test. */
static inline bool praxis_bring_up(praxis_stage clock, praxis_stage pins,
                                  praxis_stage control, praxis_stage interrupts) {
    if (!clock() || !pins() || !control()) {
        return false;
    }
    return interrupts == 0 || interrupts();
}
#endif

