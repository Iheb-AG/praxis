#ifndef PRAXIS_LOOPBACK_QUEUE_H
#define PRAXIS_LOOPBACK_QUEUE_H
#include <stdbool.h>
#include <stdint.h>
#define QUEUE_SIZE 64U
#define QUEUE_MASK (QUEUE_SIZE - 1U)
typedef struct { volatile uint8_t data[QUEUE_SIZE], head, tail; } Queue;
/* Caller serializes main/ISR access. No spinning or internal IRQ changes. */
static inline unsigned queue_available(const Queue *q)
{ return (q->tail - q->head - 1U) & QUEUE_MASK; }
static inline bool queue_push(Queue *q, uint8_t value)
{
    const uint8_t next = (uint8_t)((q->head + 1U) & QUEUE_MASK);
    if (next == q->tail) return false;
    q->data[q->head] = value; q->head = next;
    return true;
}
static inline bool queue_pop(Queue *q, uint8_t *value)
{
    if (q->tail == q->head) return false;
    *value = q->data[q->tail]; q->tail = (uint8_t)((q->tail + 1U) & QUEUE_MASK);
    return true;
}
#endif
