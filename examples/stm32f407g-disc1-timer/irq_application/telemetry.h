#ifndef PRAXIS_TIMER_ROUTE_TELEMETRY_H
#define PRAXIS_TIMER_ROUTE_TELEMETRY_H
#include <stdint.h>
#include <stddef.h>
/* Software ABI only. Sole main publisher; uint32 words, little endian.
 * flags: timer quiet, pins quiet, controller failed, PRIMASK masked (bits0..3).
 * end_valid_mask: readable PWM, capture, GPIO snapshots (bits0..2).
 * phase: boot0, passed1, failed2; status follows enum route_status. */
#define ROUTE_TELEMETRY_MAGIC 0x50524931U
#define ROUTE_TELEMETRY_ABI 1U
#define ROUTE_TELEMETRY_FIELDS(X) \
    X(magic) \
    X(abi) \
    X(size_bytes) \
    X(publications) \
    X(phase) \
    X(status) \
    X(flags) \
    X(frames) \
    X(captures) \
    X(expected_frames) \
    X(clock_hz) \
    X(period_ticks) \
    X(tolerance_ticks) \
    X(prescaler) \
    X(period_counts) \
    X(high_counts) \
    X(capture0) \
    X(capture1) \
    X(capture2) \
    X(capture3) \
    X(capture4) \
    X(capture5) \
    X(capture6) \
    X(capture7) \
    X(capture8) \
    X(end_valid_mask) \
    X(end_pwm_cr1) \
    X(end_pwm_ccer) \
    X(end_pwm_dier) \
    X(end_capture_cr1) \
    X(end_capture_ccer) \
    X(end_capture_dier) \
    X(end_pin_modes) \
    X(irq_count) \
    X(data_reads) \
    X(discarded_edges) \
    X(irq_error) \
    X(irq_priority) \
    X(vector_verified) \
    X(end_irq_enabled) \
    X(end_irq_pending) \
    X(end_irq_active) \
    X(timeout_pending_capture) \
    X(irq_snapshot_valid)
#define ROUTE_TELEMETRY_DECLARE(name) uint32_t name;
typedef struct {
    uint32_t generation;
    ROUTE_TELEMETRY_FIELDS(ROUTE_TELEMETRY_DECLARE)
} PraxisTimerRouteTelemetry;
#undef ROUTE_TELEMETRY_DECLARE
_Static_assert(sizeof(PraxisTimerRouteTelemetry)==180U,"timer ABI size");
static inline void route_telemetry_publish(volatile PraxisTimerRouteTelemetry *destination,
        const volatile PraxisTimerRouteTelemetry *source, void (*fence)(void))
{
    uint32_t before=destination->generation;
    destination->generation=before+1U;fence();
#define ROUTE_TELEMETRY_COPY(name) destination->name=source->name;
    ROUTE_TELEMETRY_FIELDS(ROUTE_TELEMETRY_COPY)
#undef ROUTE_TELEMETRY_COPY
    fence();destination->generation=before+2U;
}
#endif
