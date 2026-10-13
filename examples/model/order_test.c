#include <assert.h>
#include "praxis_sequence.h"

static unsigned trace;
static bool fail_clock;
static bool clock_stage(void) { trace = trace * 10 + 1; return !fail_clock; }
static bool pin_stage(void) { assert(trace == 1); trace = trace * 10 + 2; return true; }
static bool control_stage(void) { assert(trace == 12); trace = trace * 10 + 3; return true; }
static bool irq_stage(void) { assert(trace == 123); trace = trace * 10 + 4; return true; }

int main(void) {
    assert(praxis_bring_up(clock_stage, pin_stage, control_stage, 0));
    assert(trace == 123);
    trace = 0;
    assert(praxis_bring_up(clock_stage, pin_stage, control_stage, irq_stage));
    assert(trace == 1234);
    trace = 0;
    fail_clock = true;
    assert(!praxis_bring_up(clock_stage, pin_stage, control_stage, irq_stage));
    assert(trace == 1); /* Failure prevents every later-stage callback. */
    return 0;
}
