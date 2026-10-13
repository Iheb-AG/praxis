/* Synthetic bus/MMIO effect model. No host compiler substitutes for ARM builds.
 * It executes the application's controller, modeling flag/read side effects.
 */
#include <stdio.h>
#include <stdlib.h>
#include "i2c_controller.h"

enum phase { CONFIG, STARTING, ADDRESSING, TRANSMITTING, STOPPING, FINISHED };
struct model {
    uint32_t r[9];
    enum phase phase;
    unsigned fault, reads, writes, ticks, stop_ticks, queued, addresses, stops;
    unsigned violation, sr1_seen, addr_seen, command_violation, early_sr2, early_disable;
};
static const uint8_t payload[3] = {0x12U, 0x34U, 0x56U}; /* Synthetic values. */

static void error(struct model *m, uint32_t flag)
{
    m->r[I_SR1] |= flag;
    if (flag == I2C_SR1_ARLO) m->r[I_SR2] = I2C_SR2_BUSY; /* Other controller owns bus. */
}
static uint32_t read_reg(void *context, enum i2c_register name)
{
    struct model *m = context;
    ++m->reads;
    if (name == I_SR1) {
        ++m->ticks;
        if (m->phase == STARTING && m->ticks >= 2 && m->fault != 2) {
            m->r[I_SR1] |= I2C_SR1_SB;
            m->r[I_SR2] = I2C_SR2_MSL | I2C_SR2_BUSY;
            if (m->fault != 10) m->r[I_CR1] &= ~I2C_CR1_START;
        }
        if (m->phase == ADDRESSING && m->ticks >= 2) {
            if (m->fault == 4) error(m, I2C_SR1_AF);
            else if (m->fault == 5) error(m, I2C_SR1_ARLO);
            else if (m->fault != 3) {
                m->r[I_SR1] |= I2C_SR1_ADDR;
                m->r[I_SR2] = I2C_SR2_MSL | I2C_SR2_BUSY | I2C_SR2_TRA;
                if (m->fault == 11) error(m, I2C_SR1_ARLO);
                if (m->fault == 14) m->r[I_SR2] &= ~I2C_SR2_TRA;
            }
        }
        if (m->phase == TRANSMITTING) {
            if (m->ticks >= 1) m->r[I_SR1] |= I2C_SR1_TXE;
            if (m->queued == 3 && m->ticks >= 2 && m->fault != 7)
                m->r[I_SR1] |= I2C_SR1_BTF;
            if (m->fault == 6 && m->queued == 2) error(m, I2C_SR1_AF);
            if (m->fault == 12 && m->queued == 1) error(m, I2C_SR1_BERR);
            if (m->fault == 13 && m->queued == 3) error(m, I2C_SR1_OVR);
        }
        if (m->phase == STOPPING && m->fault == 24) error(m, I2C_SR1_ARLO);
        m->sr1_seen = 1;
        m->addr_seen = !!(m->r[I_SR1] & I2C_SR1_ADDR);
    }
    if (name == I_CR1 && m->phase == STOPPING && ++m->stop_ticks >= 2 &&
            m->fault != 8 && m->fault != 24) {
        m->r[I_CR1] &= ~I2C_CR1_STOP;
        m->r[I_SR1] &= ~(I2C_SR1_SB | I2C_SR1_ADDR | I2C_SR1_TXE | I2C_SR1_BTF);
        m->r[I_SR2] = m->fault == 9 ? I2C_SR2_BUSY : 0U;
        m->phase = FINISHED;
    }
    uint32_t result = m->r[name];
    if (name == I_SR2 && m->phase == ADDRESSING) {
        if (!m->addr_seen) { ++m->violation; ++m->early_sr2; }
        if (m->sr1_seen && (m->r[I_SR1] & I2C_SR1_ADDR)) {
            m->r[I_SR1] &= ~I2C_SR1_ADDR;
            m->phase = TRANSMITTING;
            m->ticks = 0;
        }
    }
    return result;
}

static void write_reg(void *context, enum i2c_register name, uint32_t value)
{
    struct model *m = context;
    ++m->writes;
    if (name == I_CR1) {
        if (m->r[I_CR1] & I2C_COMMANDS) { ++m->violation; ++m->command_violation; }
        if (!(value & I2C_CR1_PE) && (m->r[I_SR2] & I2C_SR2_BUSY)) {
            ++m->violation; ++m->early_disable;
        }
        if (!(value & I2C_CR1_PE)) m->r[I_SR1] = 0U; /* Hardware PE=0 flag clearing. */
        if (value & I2C_CR1_START) {
            if (m->r[I_CR2] != 42 || m->r[I_CCR] != 210 || m->r[I_TRISE] != 43 ||
                    m->r[I_OAR1] != 0x4000 || m->r[I_OAR2]) ++m->violation;
            m->phase = STARTING;
            m->ticks = 0;
        }
        if (value & I2C_CR1_STOP) {
            ++m->stops;
            if (m->r[I_SR1] & I2C_SR1_ARLO) ++m->violation;
            if (!m->fault && (m->queued != 3 ||
                    (m->r[I_SR1] & (I2C_SR1_TXE | I2C_SR1_BTF)) != (I2C_SR1_TXE | I2C_SR1_BTF)))
                ++m->violation;
            m->phase = STOPPING;
            m->stop_ticks = 0;
        }
    }
    if (name == I_DR) {
        if (m->phase == STARTING) {
            if (!m->sr1_seen || !(m->r[I_SR1] & I2C_SR1_SB) || value != 0xA0U)
                ++m->violation;
            ++m->addresses;
            m->phase = ADDRESSING;
        } else {
            if (m->phase != TRANSMITTING || !(m->r[I_SR1] & I2C_SR1_TXE) ||
                    m->queued >= 3 || value != payload[m->queued]) ++m->violation;
            ++m->queued;
        }
        m->ticks = 0;
        m->r[I_SR1] &= ~(I2C_SR1_SB | I2C_SR1_TXE | I2C_SR1_BTF);
        m->sr1_seen = m->addr_seen = 0;
    }
    if (name == I_SR1 || name == I_SR2) ++m->violation; /* No W1C or sampled writeback. */
    if (name != I_CR1 && name != I_DR && (m->r[I_CR1] & I2C_CR1_PE)) ++m->violation;
    m->r[name] = value;
}

int main(int argc, char **argv)
{
    unsigned fault = argc > 1 ? (unsigned)strtoul(argv[1], NULL, 10) : 0;
    struct model m = {.fault = fault};
    struct i2c_io io = {read_reg, write_reg, &m, false, true, 0};
    if (fault == 22) m.r[I_CR1] = I2C_CR1_PE;
    bool configured = i2c_configure(&io, fault == 20 ? 16000000U : 42000000U, fault != 21);
    if (fault == 25) configured = i2c_configure(&io, 16000000U, true);
    unsigned config_writes = m.writes;
    if (fault == 1) m.r[I_SR2] = I2C_SR2_BUSY;
    if (fault == 23) m.r[I_CR1] = I2C_CR1_PE;
    size_t length = fault == 16 ? 0U : fault == 17 ? 33U : 3U;
    struct i2c_result result = i2c_transmit(&io, fault == 18 ? 0U : 0x50U, payload,
                                          length, fault == 19 ? 0U : 4U, fault != 15);
    unsigned calls = m.reads + m.writes;
    bool retry_blocked = true;
    if (io.reset_required) {
        struct i2c_result retry = i2c_transmit(&io, 0x50U, payload, 3U, 4U, true);
        retry_blocked = retry.status == I_NOT_CONFIGURED && m.reads + m.writes == calls;
    }
    printf("{\"configured\":%u,\"status\":%u,\"queued\":%zu,\"cleaned\":%u,"
           "\"dirty\":%u,\"violation\":%u,\"stops\":%u,\"addresses\":%u,"
           "\"calls\":%u,\"config_writes\":%u,\"retry_blocked\":%u,"
           "\"sr1\":%u,\"cr1\":%u,\"early_sr2\":%u,\"early_disable\":%u,"
           "\"command_violation\":%u}\n", configured, result.status, result.bytes_queued,
           result.cleaned_up, io.reset_required, m.violation, m.stops, m.addresses, calls,
           config_writes, retry_blocked, m.r[I_SR1], m.r[I_CR1], m.early_sr2,
           m.early_disable, m.command_violation);
    return 0;
}
