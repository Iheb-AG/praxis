#ifndef PRAXIS_CAN_TELEMETRY_H
#define PRAXIS_CAN_TELEMETRY_H
#include <stdint.h>
#include <stddef.h>

/* Software-only ABI. All fields uint32, little endian, sole main publisher.
   Flags: clock complete, configured, TX requested, ISR received, reset required,
   source disabled, line disabled, global IRQ masked (bits 0..7 respectively).
   Phase: boot0 / passed1 / failed2; status follows enum can_status. */
#define PRAXIS_CAN_MAGIC 0x50524331U
#define PRAXIS_CAN_ABI 1U
#define PRAXIS_CAN_FIELDS(X) \
    X(magic) X(abi) X(size_bytes) X(publications) X(phase) X(status) X(flags) \
    X(clock_step) X(irq_count) X(rx_words_read_mask) X(rx_identifier) X(rx_length) \
    X(rx_low) X(rx_high) X(last_esr) X(last_tsr) X(last_rf0) X(expected_identifier) \
    X(expected_low) X(expected_high) X(end_ier) X(end_irq_enabled)
#define PRAXIS_CAN_DECLARE(name) uint32_t name;
typedef struct {
    uint32_t generation;
    PRAXIS_CAN_FIELDS(PRAXIS_CAN_DECLARE)
} PraxisCanTelemetry;
#undef PRAXIS_CAN_DECLARE
_Static_assert(sizeof(PraxisCanTelemetry) == 92U, "CAN ABI record size");
_Static_assert(offsetof(PraxisCanTelemetry, end_irq_enabled) == 88U, "CAN ABI last word");

static inline void can_telemetry_publish(volatile PraxisCanTelemetry *destination,
        const volatile PraxisCanTelemetry *source, void (*barrier)(void))
{
    uint32_t before = destination->generation;
    destination->generation = before + 1U;
    barrier();
#define PRAXIS_CAN_COPY(name) destination->name = source->name;
    PRAXIS_CAN_FIELDS(PRAXIS_CAN_COPY)
#undef PRAXIS_CAN_COPY
    barrier();
    destination->generation = before + 2U;
}
#endif
