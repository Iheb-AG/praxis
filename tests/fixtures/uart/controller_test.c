#include <assert.h>
#include <stdio.h>
#include <string.h>
#include "controller.h"
#include "queue.h"

static void returned(Controller *c, const uint8_t *frame, uint32_t now)
{ for (unsigned i=0; i<FRAME_SIZE; ++i) controller_receive(c, frame[i], now); }
int main(void)
{
    Queue q = {0}; uint8_t byte;
    assert(!queue_pop(&q, &byte));
    for (unsigned turn=0; turn<200U; ++turn) {
        assert(queue_available(&q)==63U);
        for (unsigned i=0; i<63U; ++i) assert(queue_push(&q, (uint8_t)(turn+i)));
        assert(!queue_push(&q, 255U) && !queue_available(&q));
        for (unsigned i=0; i<63U; ++i) {
            assert(queue_pop(&q, &byte)); assert(byte==(uint8_t)(turn+i));
        }
        assert(!queue_pop(&q, &byte));
    }
    Controller c; uint8_t frame[FRAME_SIZE]; Button b;
    controller_init(&c);
    assert(!controller_tick(&c, 100000U, frame));
    assert(controller_press(&c, UINT32_MAX-60U));
    assert(controller_tick(&c, UINT32_MAX-60U, frame));
    assert(!controller_tick(&c, UINT32_MAX-59U, frame));
    assert(!controller_press(&c, UINT32_MAX-58U));
    assert(c.state==PAUSING);
    returned(&c, frame, UINT32_MAX-55U);
    assert(c.state==PAUSED && c.validated==1U);
    assert(!controller_tick(&c, 1000U, frame));
    assert(controller_press(&c, 0U));
    for (uint32_t i=0; i<100U; ++i) {
        assert(controller_tick(&c, i*100U, frame));
        returned(&c, frame, i*100U+2U);
        assert(c.state==RUNNING && !c.in_flight);
        assert(!controller_tick(&c, i*100U+99U, frame));
    }
    assert(c.blue && c.validated==100U && !c.orange);
    controller_press(&c, 10000U); assert(c.state==PAUSED && c.blue);
    assert(controller_press(&c, UINT32_MAX-100U));
    assert(!c.blue && !c.validated);
    assert(controller_tick(&c, UINT32_MAX-100U, frame));
    for (unsigned i=0; i<18U; ++i) controller_receive(&c, frame[i], UINT32_MAX-99U);
    assert(!controller_tick(&c, 148U, frame) && c.state==RUNNING);
    assert(!controller_tick(&c, 149U, frame) && c.state==FAILED && !c.blue);
    assert(controller_press(&c, 200U));
    c.sequence=UINT32_MAX;
    assert(controller_tick(&c, 200U, frame)); returned(&c, frame, 202U);
    assert(c.sequence==0U);
    assert(controller_tick(&c, 300U, frame));
    frame[10]^=1U; returned(&c, frame, 301U);
    assert(c.state==FAILED);
    assert(controller_press(&c, 400U));
    assert(controller_tick(&c, 400U, frame));
    returned(&c, frame, 650U); assert(c.state==FAILED); /* late frame */
    assert(controller_press(&c, 700U));
    controller_receive(&c, 0U, 700U); assert(c.state==FAILED); /* unsolicited */
    assert(controller_press(&c, 800U));
    assert(controller_tick(&c, 800U, frame)); controller_press(&c, 801U);
    controller_tick(&c, 1050U, frame); assert(c.state==FAILED); /* pause drain bounded */
    button_init(&b, false, 0U, 0U);
    assert(!button_step(&b, true, 10U, 1U));
    assert(!button_step(&b, true, 59U, 1U));
    assert(!button_step(&b, true, 60U, 3U)); /* unobserved bounce restarts */
    assert(button_step(&b, true, 110U, 3U));
    assert(!button_step(&b, true, 999U, 3U)); /* held */
    assert(!button_step(&b, false, 1000U, 4U));
    assert(!button_step(&b, false, 1050U, 4U));
    assert(!button_step(&b, true, 1060U, 5U));
    assert(button_step(&b, true, 1110U, 5U));
    button_init(&b, true, 0U, 0U); /* held at reset must release first */
    assert(!button_step(&b, true, 100U, 0U));
    button_init(&b, false, UINT32_MAX-20U, 0U);
    assert(!button_step(&b, true, UINT32_MAX-10U, 1U));
    assert(button_step(&b, true, 39U, 1U));
    puts("controller, debounce, drain, deadline and rollover checks passed");
}
