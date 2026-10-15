/* Digital MMIO/exception effects. No bus, analog, clock accuracy or silicon model. */
#include <stdio.h>
#include <stdlib.h>
#include "can_controller.h"
struct model {
    uint32_t r[28], filter_reserved;
    struct can_io *io;
    unsigned fault, reads, writes, staged, rx_reads, requests, releases, acks;
    unsigned violation, dispatched, fences;
    bool sent, progressed, in_isr;
};
static void progress(struct model *m)
{
    if (m->progressed || !m->sent) return;
    m->progressed = true;
    if (m->fault == 4) return; /* Request never completes. */
    m->r[C_TSR] = CAN_ALL_EMPTY | CAN_TSR_RQCP0 | CAN_TSR_TXOK0;
    if (m->fault == 6) m->r[C_TSR] |= CAN_TSR_TERR0;
    if (m->fault == 7) m->r[C_TSR] |= CAN_TSR_ALST0;
    if (m->fault == 8) m->r[C_ESR] = CAN_ESR_BOFF;
    if (m->fault == 9) m->r[C_TSR] &= ~CAN_TSR_TXOK0;
    if (m->fault == 10) m->r[C_TSR] &= ~CAN_TSR_RQCP0;
    if (m->fault == 11) m->r[C_TSR] &= ~(1UL << 26);
    if (m->fault == 5) return; /* TX completes but filtering delivers nothing. */
    m->r[C_RF0] = 1U;
    m->r[C_RIR] = CAN_TEST_IDENTIFIER;
    m->r[C_RDTR] = 8U;
    m->r[C_RDLR] = m->r[C_TDLR];
    m->r[C_RDHR] = m->r[C_TDHR];
    if (m->fault == 12) m->r[C_RF0] |= CAN_RF0R_FOVR0;
    if (m->fault == 13) m->r[C_RF0] = 3U | CAN_RF0R_FULL0;
    if (m->fault == 14) m->r[C_RIR] ^= (1UL << 21);
    if (m->fault == 15) m->r[C_RIR] |= CAN_RI0R_IDE;
    if (m->fault == 16) m->r[C_RIR] |= CAN_RI0R_RTR;
    if (m->fault == 17) m->r[C_RDTR] = 9U;
    if (m->fault == 18) m->r[C_RDTR] = 8U | (2UL << 8);
    if (m->fault == 19) m->r[C_RDLR] ^= 1U;
    if (m->fault == 20) m->r[C_RDHR] ^= 0x80000000U;
    if (m->fault == 21) m->r[C_RF0] = 2U;
    if (m->fault == 28) m->r[C_MCR] |= CAN_MCR_AWUM;
    if (m->fault != 3 && (m->r[C_IRQ_ENABLE] & CAN_IRQ_BIT) && m->r[C_IER] == CAN_IER_FMPIE0) {
        m->in_isr = true;
        ++m->dispatched;
        can_fifo0_isr(m->io);
        m->in_isr = false;
    }
}
static uint32_t read_reg(void *context, enum can_reg reg)
{
    struct model *m = context;
    ++m->reads;
    if (m->sent && !m->in_isr && reg == C_MCR) progress(m);
    if (m->fault == 45 && m->progressed && !m->in_isr && reg == C_TSR)
        m->r[C_ESR] = CAN_ESR_BOFF; /* Error arrives after a success observation. */
    if (reg == C_BTR && !(m->r[C_MSR] & CAN_MSR_INAK)) ++m->violation;
    if (reg >= C_RIR && reg <= C_RDHR) {
        if (!(m->r[C_RF0] & CAN_RF0R_FMP0) || !m->in_isr) ++m->violation;
        m->rx_reads |= 1U << (reg - C_RIR);
        if (reg == C_RDHR && m->fault == 22) m->r[C_ESR] = CAN_ESR_LEC_0;
    }
    if (reg == C_IRQ_DISABLE || reg == C_IRQ_CLEAR) ++m->violation;
    return m->r[reg];
}
static void write_reg(void *context, enum can_reg reg, uint32_t value)
{
    struct model *m = context;
    ++m->writes;
    if (reg == C_MSR || reg == C_ESR || reg == C_RF1 || reg == C_IRQ_ACTIVE ||
            (reg >= C_RIR && reg <= C_RDHR)) ++m->violation;
    if (reg == C_MCR) {
        if (value != CAN_TEST_CONTROL && value != (CAN_TEST_CONTROL | CAN_MCR_INRQ))
            ++m->violation;
        if (value & CAN_MCR_INRQ) {
            if (m->fault != 1) m->r[C_MSR] = CAN_MSR_INAK;
        } else if (m->fault != 2) m->r[C_MSR] = 0U;
    }
    if (reg == C_BTR) {
        if (!(m->r[C_MSR] & CAN_MSR_INAK) || value != CAN_TEST_TIMING) ++m->violation;
        if (m->fault == 30) return;
    }
    if (reg >= C_FM1 && reg <= C_FR2) {
        if (!(m->r[C_FMR] & CAN_FMR_FINIT)) ++m->violation;
        if (m->fault == 31 && reg == C_FR2) return;
    }
    if (reg == C_FMR && (value & ~(CAN_FMR_CAN2SB | CAN_FMR_FINIT)) != m->filter_reserved)
        ++m->violation;
    if (reg >= C_TIR && reg <= C_TDHR) {
        if (!(m->r[C_TSR] & (1UL << 26))) ++m->violation;
        m->staged |= 1U << (reg - C_TIR);
        if (m->fault == 32 && reg == C_TDHR) return;
        if (reg == C_TIR && (value & CAN_TI0R_TXRQ)) {
            if (m->staged != 15U || !m->io->busy || !m->io->armed ||
                    m->r[C_IER] != CAN_IER_FMPIE0 || !(m->r[C_IRQ_ENABLE] & CAN_IRQ_BIT) ||
                    m->r[C_TDTR] != 8U || m->r[C_TDLR] != m->io->expected_low ||
                    m->r[C_TDHR] != m->io->expected_high) ++m->violation;
            ++m->requests;
            m->sent = true;
            m->r[C_TSR] &= ~(1UL << 26);
        }
    }
    if (reg == C_RF0) {
        if (value != CAN_RF0R_RFOM0 || m->rx_reads != 15U || !m->in_isr ||
                (m->r[C_RF0] & CAN_RF0R_FMP0) != 1U) ++m->violation;
        ++m->releases;
        if (m->fault != 23) m->r[C_RF0] = 0U;
        return;
    }
    if (reg == C_TSR) {
        if (value != CAN_TSR_RQCP0 || !m->io->received || m->io->armed ||
                m->r[C_ESR] || (m->r[C_TSR] & (CAN_TSR_ALST0 | CAN_TSR_TERR0))) ++m->violation;
        ++m->acks;
        if (m->fault != 27) m->r[C_TSR] &= ~(CAN_TSR_RQCP0 | CAN_TSR_TXOK0 |
                                           CAN_TSR_ALST0 | CAN_TSR_TERR0);
        return;
    }
    if (reg == C_IER && value == 0U && m->fault == 24) return;
    if (reg == C_IRQ_ENABLE || reg == C_IRQ_DISABLE || reg == C_IRQ_CLEAR) {
        if (value != CAN_IRQ_BIT) ++m->violation;
        if (reg == C_IRQ_ENABLE) {
            if (m->r[C_IER] != CAN_IER_FMPIE0 || m->r[C_RF0] ||
                    m->r[C_IRQ_PRIORITY] != 0x50U || !m->io->armed) ++m->violation;
            if (m->fault != 26) m->r[C_IRQ_ENABLE] |= value;
        } else if (reg == C_IRQ_DISABLE) {
            if (m->r[C_IER]) ++m->violation;
            if (m->fault != 25) m->r[C_IRQ_ENABLE] &= ~value;
        } else if (m->r[C_IER]) ++m->violation;
        return;
    }
    if (reg == C_IRQ_PRIORITY && (m->r[C_IER] || (m->r[C_IRQ_ENABLE] & CAN_IRQ_BIT)))
        ++m->violation;
    m->r[reg] = value;
}
static void fence(void *context) { ++((struct model *)context)->fences; }
int main(int argc, char **argv)
{
    unsigned fault = argc > 1 ? (unsigned)strtoul(argv[1], NULL, 10) : 0U;
    struct model m = {.fault = fault};
    struct can_io io = {.read = read_reg, .write = write_reg, .fence = fence,
                       .context = &m, .reset_required = true};
    m.io = &io;
    m.r[C_MCR] = CAN_MCR_DBF | CAN_MCR_SLEEP;
    m.r[C_MSR] = 0xC02U;
    m.r[C_TSR] = CAN_ALL_EMPTY;
    m.r[C_FMR] = fault == 40 ? 0xE01U : 0x2A1C0E01U;
    m.filter_reserved = m.r[C_FMR] & ~(CAN_FMR_CAN2SB | CAN_FMR_FINIT);
    for (unsigned n = C_FR1; n <= C_RDHR; ++n) m.r[n] = 0xA5A5A5A5U;
    if (fault == 33) m.r[C_IRQ_ENABLE] = CAN_IRQ_BIT;
    if (fault == 34) m.r[C_IRQ_ACTIVE] = CAN_IRQ_BIT;
    if (fault == 35) m.r[C_FA1] = 2U;
    if (fault == 36) m.r[C_FMR] ^= 1UL << 8;
    enum can_status configured = can_configure(&io, fault == 37 ? 16000000U : 42000000U,
                                               fault != 38, fault != 39, 3U);
    unsigned config_writes = m.writes;
    enum can_status status = configured;
    if (status == C_OK) status = can_arm_fifo0(&io, fault != 41);
    const uint8_t payload[8] = {0x50U,0x52U,0x41U,0x58U,0x49U,0x53U,0x00U,0xFFU};
    if (status == C_OK && fault == 29) m.r[C_TSR] |= CAN_TSR_RQCP0 | CAN_TSR_TXOK0;
    if (status == C_OK) status = can_send_eight(&io, fault == 42 ? NULL : payload);
    if (status == C_OK && fault == 43) {
        m.in_isr = true; can_fifo0_isr(&io); m.in_isr = false; /* Empty spurious IRQ. */
    }
    if (status == C_OK) status = can_finish(&io, fault == 44 ? 0U : 4U);
    unsigned calls = m.reads + m.writes;
    bool retry_blocked = true;
    if (io.reset_required) {
        retry_blocked = can_send_eight(&io, payload) == C_STATE && m.reads + m.writes == calls;
    }
    printf("{\"configured_status\":%u,\"status\":%u,\"received\":%u,\"irq_count\":%u,"
        "\"reset_required\":%u,\"retry_blocked\":%u,\"requests\":%u,\"releases\":%u,"
        "\"acks\":%u,\"violation\":%u,\"calls\":%u,\"config_writes\":%u,"
        "\"ier\":%u,\"irq_enabled\":%u,\"esr\":%u,\"tsr\":%u,\"rf0\":%u,"
        "\"fmr\":%u,\"dispatched\":%u,\"rx_reads\":%u}\n", configured,status,
        io.received,io.irq_count,io.reset_required,retry_blocked,m.requests,m.releases,
        m.acks,m.violation,calls,config_writes,m.r[C_IER],m.r[C_IRQ_ENABLE],
        m.r[C_ESR],m.r[C_TSR],m.r[C_RF0],m.r[C_FMR],m.dispatched,m.rx_reads);
    return 0;
}
