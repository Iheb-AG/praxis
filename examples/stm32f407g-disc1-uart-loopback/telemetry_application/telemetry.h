#ifndef PRAXIS_UART_TELEMETRY_H
#define PRAXIS_UART_TELEMETRY_H
#include <stdint.h>
#include <stddef.h>
/* Software ABI v1: each field is a uint32_t, in this order, little endian.
   Main is the sole publisher. Readers check an unchanged even generation. */
typedef struct {
    uint32_t generation, magic, abi, size_bytes;
    uint32_t uptime_ms, timer_irqs, uart_irqs, exti_irqs;
    uint32_t run_number, state, frames_started, frames_validated, run_validated;
    uint32_t rx_bytes, tx_bytes, uart_errors, queue_overflows;
    uint32_t failure_reason, flags, last_good_ms, next_sequence;
    uint32_t button_presses, main_iterations;
} PraxisTelemetry;
_Static_assert(sizeof(PraxisTelemetry) == 92U, "Telemetry ABI v1 size");
_Static_assert(offsetof(PraxisTelemetry, generation) == 0U, "Seqlock first");
_Static_assert(offsetof(PraxisTelemetry, main_iterations) == 88U, "Telemetry ABI last field");
extern volatile PraxisTelemetry praxis_telemetry;
#endif
