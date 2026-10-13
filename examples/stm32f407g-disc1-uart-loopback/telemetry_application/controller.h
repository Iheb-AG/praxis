#ifndef PRAXIS_LOOPBACK_CONTROLLER_H
#define PRAXIS_LOOPBACK_CONTROLLER_H
#include "protocol.h"
typedef enum { PAUSED, RUNNING, PAUSING, FAILED } RunState;
typedef enum { FAIL_NONE, FAIL_TIMEOUT, FAIL_FRAME, FAIL_UNEXPECTED_RX,
               FAIL_UART, FAIL_QUEUE } FailureReason;
typedef struct {
    RunState state;
    FailureReason failure_reason;
    bool in_flight, blue, orange;
    uint32_t sequence, validated, sent_at, last_start, orange_at;
    unsigned received;
    uint8_t incoming[FRAME_SIZE];
} Controller;
typedef struct {
    bool candidate, stable, armed;
    uint32_t changed_at, generation;
} Button;
void controller_init(Controller *c);
bool controller_press(Controller *c, uint32_t now);
bool controller_tick(Controller *c, uint32_t now, uint8_t outgoing[FRAME_SIZE]);
void controller_receive(Controller *c, uint8_t byte, uint32_t now);
void controller_fail(Controller *c, FailureReason reason);
void button_init(Button *b, bool raw, uint32_t now, uint32_t generation);
bool button_step(Button *b, bool raw, uint32_t now, uint32_t generation);
#endif
