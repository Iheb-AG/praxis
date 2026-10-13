#include "controller.h"

void controller_init(Controller *c)
{
    /* No C library is linked. Leave unread frame storage alone until filled;
       clearing the whole aggregate can emit a freestanding memset call. */
    c->state = PAUSED;
    c->in_flight = false; c->blue = false; c->orange = false;
    c->sequence = 0U; c->validated = 0U; c->sent_at = 0U;
    c->last_start = 0U; c->orange_at = 0U; c->received = 0U;
}

bool controller_press(Controller *c, uint32_t now)
{
    if (c->state == RUNNING) {
        c->state = c->in_flight ? PAUSING : PAUSED;
        return false;
    }
    if (c->state == PAUSING) return false;
    controller_init(c);
    c->state = RUNNING;
    c->last_start = now - 100U; /* First frame immediately; later starts >=100 ms. */
    return true;
}

void controller_fail(Controller *c)
{
    c->state = FAILED; c->in_flight = false;
    c->blue = false; c->orange = false;
}

bool controller_tick(Controller *c, uint32_t now, uint8_t outgoing[FRAME_SIZE])
{
    if (c->orange && (uint32_t)(now - c->orange_at) >= 30U) c->orange = false;
    if (c->in_flight && (uint32_t)(now - c->sent_at) >= 250U) controller_fail(c);
    if (c->state != RUNNING || c->in_flight || (uint32_t)(now - c->last_start) < 100U)
        return false;
    frame_make(outgoing, c->sequence);
    c->received = 0U; c->in_flight = true;
    c->sent_at = now; c->last_start = now;
    return true;
}

void controller_receive(Controller *c, uint8_t byte, uint32_t now)
{
    if (c->state != RUNNING && c->state != PAUSING) return;
    if (!c->in_flight || (uint32_t)(now - c->sent_at) >= 250U) {
        controller_fail(c); return;
    }
    c->incoming[c->received++] = byte;
    if (c->received != FRAME_SIZE) return;
    if (!frame_valid(c->incoming, c->sequence)) { controller_fail(c); return; }
    ++c->sequence; /* Unsigned modulo-2^32 wrap is part of the protocol. */
    if (c->validated < UINT32_MAX) ++c->validated;
    if (c->validated >= 100U) c->blue = true;
    c->orange = true; c->orange_at = now; c->in_flight = false;
    if (c->state == PAUSING) c->state = PAUSED;
}

void button_init(Button *b, bool raw, uint32_t now, uint32_t generation)
{
    *b = (Button){.candidate = raw, .stable = raw, .armed = !raw,
                  .changed_at = now, .generation = generation};
}

bool button_step(Button *b, bool raw, uint32_t now, uint32_t generation)
{
    /* Any EXTI edge, even a bounce returning to the same sampled level,
       restarts qualification. All debounce work is outside the ISR. */
    if (raw != b->candidate || generation != b->generation) {
        b->candidate = raw; b->generation = generation; b->changed_at = now;
    }
    if (b->candidate == b->stable || (uint32_t)(now - b->changed_at) < 50U) return false;
    b->stable = b->candidate;
    if (!b->stable) { b->armed = true; return false; }
    if (!b->armed) return false;
    b->armed = false;
    return true;
}
