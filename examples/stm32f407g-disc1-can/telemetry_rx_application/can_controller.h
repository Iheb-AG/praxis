/* Scoped CAN1 silent-loopback one-shot, shared with the MMIO effect model.
 * Engineering evidence: Praxis ingestion MCP, RM0090 Rev22 pp1073-1111.
 * Caller owns CAN1/CAN2 filters and IRQ20; setup runs with interrupts masked.
 */
#ifndef PRAXIS_CAN_CONTROLLER_H
#define PRAXIS_CAN_CONTROLLER_H
#include <stdbool.h>
#include <stdint.h>
#include <stm32f407xx.h>

enum can_reg { C_MCR, C_MSR, C_TSR, C_RF0, C_RF1, C_IER, C_ESR, C_BTR,
    C_FMR, C_FM1, C_FS1, C_FFA1, C_FA1, C_FR1, C_FR2,
    C_TIR, C_TDTR, C_TDLR, C_TDHR, C_RIR, C_RDTR, C_RDLR, C_RDHR,
    C_IRQ_ENABLE, C_IRQ_DISABLE, C_IRQ_CLEAR, C_IRQ_PRIORITY, C_IRQ_ACTIVE };
enum can_status { C_OK, C_INVALID, C_STATE, C_INIT_TIMEOUT, C_ERROR, C_FILTER,
    C_TX_ERROR, C_RX_ERROR, C_TIMEOUT, C_RELEASE_TIMEOUT, C_IRQ_ERROR };
struct can_io {
    uint32_t (*read)(void *, enum can_reg);
    void (*write)(void *, enum can_reg, uint32_t);
    void (*fence)(void *);
    void *context;
    volatile bool configured, reset_required, armed, irq_owned, busy, received;
    volatile enum can_status status;
    volatile uint32_t irq_count, last_esr, last_tsr, last_rf0;
    uint32_t expected_low, expected_high;
};
#define CAN_TEST_ID 0x123U
#define CAN_TEST_IDENTIFIER (CAN_TEST_ID << 21)
#define CAN_TEST_CONTROL (CAN_MCR_DBF | CAN_MCR_NART | CAN_MCR_RFLM)
#define CAN_TEST_TIMING (CAN_BTR_SILM | CAN_BTR_LBKM | (10UL << 16) | (1UL << 20) | 5UL)
#define CAN_IRQ_BIT (1UL << 20)
#define CAN_ALL_EMPTY CAN_TSR_TME
#define CAN_COMPLETIONS (CAN_TSR_RQCP0 | CAN_TSR_RQCP1 | CAN_TSR_RQCP2)

static inline bool can_valid(const struct can_io *io)
{
    return io && io->read && io->write && io->fence;
}
static inline bool can_disarm(struct can_io *io)
{
    if (!io->irq_owned) return true;
    uint32_t source = io->read(io->context, C_IER);
    if (source != CAN_IER_FMPIE0 && source != 0U) return false;
    io->write(io->context, C_IER, 0U);
    if (io->read(io->context, C_IER) != 0U) return false;
    io->write(io->context, C_IRQ_DISABLE, CAN_IRQ_BIT);
    if (io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT) return false;
    io->write(io->context, C_IRQ_CLEAR, CAN_IRQ_BIT); /* Source disabled first. */
    io->fence(io->context);
    io->armed = false;
    io->irq_owned = false;
    return true;
}
static inline enum can_status can_fail(struct can_io *io, enum can_status status)
{
    io->status = status;
    io->configured = false;
    io->reset_required = true;
    io->busy = false;
    (void)can_disarm(io); /* No drain, abort, W1C diagnostic clearing or auto-retry. */
    return status;
}
static inline bool can_no_error(struct can_io *io)
{
    io->last_rf0 = io->read(io->context, C_RF0);
    io->last_tsr = io->read(io->context, C_TSR);
    io->last_esr = io->read(io->context, C_ESR); /* Errors after progress observations. */
    return io->last_esr == 0U && !(io->last_rf0 & (CAN_RF0R_FULL0 | CAN_RF0R_FOVR0)) &&
           !(io->last_tsr & (CAN_TSR_ALST0 | CAN_TSR_TERR0));
}
static inline bool can_write_checked(struct can_io *io, enum can_reg reg, uint32_t value)
{
    io->write(io->context, reg, value);
    return io->read(io->context, reg) == value;
}
static inline enum can_status can_configure(struct can_io *io, uint32_t pclk1,
        bool fresh_reset, bool exclusive_pair, bool rx_route_ready, uint32_t budget)
{
    if (!can_valid(io) || !budget) return C_INVALID;
    if (io->irq_owned || io->busy) return C_STATE; /* Do not retake live state. */
    io->configured = false;
    io->reset_required = true;
    io->status = C_STATE;
    if (!fresh_reset || !exclusive_pair || !rx_route_ready || pclk1 != 42000000U) return C_STATE;
    if (io->read(io->context, C_MCR) != (CAN_MCR_DBF | CAN_MCR_SLEEP) ||
            io->read(io->context, C_IER) || io->read(io->context, C_RF0) ||
            io->read(io->context, C_RF1) ||
            (io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT) ||
            (io->read(io->context, C_IRQ_ACTIVE) & CAN_IRQ_BIT) || !can_no_error(io) ||
            (io->last_tsr & (CAN_ALL_EMPTY | CAN_COMPLETIONS)) != CAN_ALL_EMPTY)
        return C_STATE;
    io->write(io->context, C_MCR, CAN_TEST_CONTROL | CAN_MCR_INRQ);
    bool acknowledged = false;
    for (uint32_t n = 0; n < budget; ++n) {
        if (!can_no_error(io)) return can_fail(io, C_ERROR);
        if ((io->read(io->context, C_MSR) & (CAN_MSR_INAK | CAN_MSR_SLAK)) == CAN_MSR_INAK) {
            acknowledged = true; break;
        }
    }
    if (!acknowledged) return can_fail(io, C_INIT_TIMEOUT);
    if (io->read(io->context, C_MCR) != (CAN_TEST_CONTROL | CAN_MCR_INRQ) ||
            !can_write_checked(io, C_BTR, CAN_TEST_TIMING)) return can_fail(io, C_STATE);
    uint32_t filter = io->read(io->context, C_FMR);
    if ((filter & (CAN_FMR_CAN2SB | CAN_FMR_FINIT)) != ((14UL << 8) | CAN_FMR_FINIT) ||
            io->read(io->context, C_FA1) || io->read(io->context, C_FM1) ||
            io->read(io->context, C_FS1) || io->read(io->context, C_FFA1))
        return can_fail(io, C_FILTER);
    /* Preserve unmodeled FMR reset bits. Never assume mailbox/filter data reset0. */
    if (!can_write_checked(io, C_FA1, 0U) || !can_write_checked(io, C_FM1, 1U) ||
            !can_write_checked(io, C_FS1, 1U) || !can_write_checked(io, C_FFA1, 0U) ||
            !can_write_checked(io, C_FR1, CAN_TEST_IDENTIFIER) ||
            !can_write_checked(io, C_FR2, CAN_TEST_IDENTIFIER) ||
            !can_write_checked(io, C_FA1, 1U) ||
            !can_write_checked(io, C_FMR, filter & ~CAN_FMR_FINIT))
        return can_fail(io, C_FILTER);
    /* Initialization synchronization is still required before combined-mode operation. */
    if (!(io->read(io->context, C_MSR) & CAN_MSR_RX)) return can_fail(io, C_STATE);
    io->write(io->context, C_MCR, CAN_TEST_CONTROL);
    acknowledged = false;
    for (uint32_t n = 0; n < budget; ++n) {
        if (!can_no_error(io)) return can_fail(io, C_ERROR);
        if (!(io->read(io->context, C_MSR) & (CAN_MSR_INAK | CAN_MSR_SLAK))) {
            acknowledged = true; break;
        }
    }
    if (!acknowledged) return can_fail(io, C_INIT_TIMEOUT);
    if (io->read(io->context, C_MCR) != CAN_TEST_CONTROL) return can_fail(io, C_STATE);
    io->configured = true;
    io->reset_required = false;
    io->received = false;
    io->irq_count = 0U;
    io->status = C_OK;
    return C_OK;
}
static inline enum can_status can_arm_fifo0(struct can_io *io, bool handler_ready)
{
    if (!can_valid(io)) return C_INVALID;
    if (!io->configured || io->reset_required || io->armed || io->busy || !handler_ready)
        return C_STATE;
    if (io->read(io->context, C_MCR) != CAN_TEST_CONTROL ||
            io->read(io->context, C_IER) || io->read(io->context, C_RF0) ||
            io->read(io->context, C_RF1) ||
            (io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT) ||
            (io->read(io->context, C_IRQ_ACTIVE) & CAN_IRQ_BIT) || !can_no_error(io))
        return can_fail(io, C_STATE);
    io->irq_owned = true;
    io->write(io->context, C_IRQ_CLEAR, CAN_IRQ_BIT);
    if (!can_write_checked(io, C_IRQ_PRIORITY, 0x50U) ||
            !can_write_checked(io, C_IER, CAN_IER_FMPIE0)) return can_fail(io, C_IRQ_ERROR);
    io->armed = true; /* Handler state published before the final line enable. */
    io->fence(io->context);
    io->write(io->context, C_IRQ_ENABLE, CAN_IRQ_BIT);
    if (!(io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT)) return can_fail(io, C_IRQ_ERROR);
    return C_OK;
}
static inline enum can_status can_send_eight(struct can_io *io, const uint8_t *data)
{
    if (!can_valid(io)) return C_INVALID;
    if (!data) return io->irq_owned ? can_fail(io, C_INVALID) : C_INVALID;
    if (!io->configured || io->reset_required || !io->armed || io->busy) return C_STATE;
    if (io->read(io->context, C_MCR) != CAN_TEST_CONTROL ||
            io->read(io->context, C_IER) != CAN_IER_FMPIE0 ||
            !(io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT) ||
            io->read(io->context, C_RF0) || io->read(io->context, C_RF1) || !can_no_error(io) ||
            (io->last_tsr & (CAN_ALL_EMPTY | CAN_COMPLETIONS)) != CAN_ALL_EMPTY)
        return can_fail(io, C_STATE);
    uint32_t low = 0U, high = 0U;
    for (unsigned n = 0; n < 4; ++n) {
        low |= (uint32_t)data[n] << (8U * n);
        high |= (uint32_t)data[n + 4] << (8U * n);
    }
    if (!can_write_checked(io, C_TIR, CAN_TEST_IDENTIFIER) ||
            !can_write_checked(io, C_TDTR, 8U) ||
            !can_write_checked(io, C_TDLR, low) || !can_write_checked(io, C_TDHR, high))
        return can_fail(io, C_STATE);
    io->expected_low = low;
    io->expected_high = high;
    io->received = false;
    io->busy = true;
    io->fence(io->context);
    io->write(io->context, C_TIR, CAN_TEST_IDENTIFIER | CAN_TI0R_TXRQ);
    return C_OK;
}
static inline void can_fifo0_isr(struct can_io *io)
{
    if (!can_valid(io) || !io->armed || !io->configured || io->reset_required) return;
    ++io->irq_count;
    if (!can_no_error(io)) { (void)can_fail(io, C_ERROR); return; }
    if (!(io->last_rf0 & CAN_RF0R_FMP0)) return; /* Spurious IRQ is not a receipt. */
    if (!io->busy || io->received || (io->last_rf0 & CAN_RF0R_FMP0) != 1U ||
            io->read(io->context, C_MCR) != CAN_TEST_CONTROL ||
            io->read(io->context, C_IER) != CAN_IER_FMPIE0) {
        (void)can_fail(io, C_STATE); return;
    }
    uint32_t identifier = io->read(io->context, C_RIR);
    uint32_t length = io->read(io->context, C_RDTR);
    uint32_t low = io->read(io->context, C_RDLR);
    uint32_t high = io->read(io->context, C_RDHR);
    if (!can_no_error(io)) { (void)can_fail(io, C_ERROR); return; }
    if (identifier != CAN_TEST_IDENTIFIER || (length & 0xFFU) != 8U ||
            ((length >> 8) & 0xFFU) > 1U || low != io->expected_low || high != io->expected_high ||
            (io->last_rf0 & CAN_RF0R_FMP0) != 1U) {
        (void)can_fail(io, C_RX_ERROR); return;
    }
    io->write(io->context, C_RF0, CAN_RF0R_RFOM0); /* No RMW/W1C flag erasure. */
    for (unsigned n = 0; n < 8; ++n) {
        if (!can_no_error(io)) { (void)can_fail(io, C_ERROR); return; }
        if (io->last_rf0 == 0U) {
            if (!can_disarm(io)) { (void)can_fail(io, C_IRQ_ERROR); return; }
            io->fence(io->context);
            io->received = true;
            return;
        }
    }
    (void)can_fail(io, C_RELEASE_TIMEOUT);
}
static inline enum can_status can_finish(struct can_io *io, uint32_t budget)
{
    if (!can_valid(io)) return C_INVALID;
    if (!budget) return io->busy ? can_fail(io, C_INVALID) : C_INVALID;
    if (io->reset_required) return io->status == C_OK ? C_STATE : io->status;
    if (!io->busy || !io->configured) return C_STATE;
    for (uint32_t n = 0; n < budget; ++n) {
        if (io->reset_required) return io->status;
        if (io->read(io->context, C_MCR) != CAN_TEST_CONTROL) return can_fail(io, C_STATE);
        if (!can_no_error(io)) return can_fail(io, C_ERROR);
        uint32_t complete = CAN_TSR_RQCP0 | CAN_TSR_TXOK0 | (1UL << 26);
        if ((io->last_tsr & CAN_TSR_RQCP0) && (io->last_tsr & complete) != complete)
            return can_fail(io, C_TX_ERROR);
        if (io->received && (io->last_tsr & complete) == complete) {
            io->fence(io->context);
            if (!can_no_error(io)) return can_fail(io, C_ERROR);
            if ((io->last_tsr & complete) != complete || io->last_rf0 != 0U)
                return can_fail(io, C_STATE);
            if (io->armed || io->irq_owned || io->read(io->context, C_IER) ||
                    (io->read(io->context, C_IRQ_ENABLE) & CAN_IRQ_BIT))
                return can_fail(io, C_IRQ_ERROR);
            io->write(io->context, C_TSR, CAN_TSR_RQCP0); /* Success only, literal group ack. */
            if (io->read(io->context, C_TSR) & (CAN_TSR_RQCP0 | CAN_TSR_TXOK0 |
                    CAN_TSR_ALST0 | CAN_TSR_TERR0)) return can_fail(io, C_STATE);
            io->busy = false;
            io->configured = false;
            io->reset_required = true; /* One-shot contract: reset before reuse. */
            io->status = C_OK;
            return C_OK;
        }
    }
    return can_fail(io, C_TIMEOUT);
}
#endif
