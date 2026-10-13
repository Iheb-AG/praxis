/* I2C1 standard-mode controller transmitter, from actual ingestion MCP evidence.
 * RM0090 Rev22 pp842-844,846,855-866. No board wiring or target-device claim.
 * This same implementation is exercised by the host MMIO-effect model.
 */
#ifndef PRAXIS_I2C_CONTROLLER_H
#define PRAXIS_I2C_CONTROLLER_H
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stm32f407xx.h>

enum i2c_register { I_CR1, I_CR2, I_OAR1, I_OAR2, I_DR, I_SR1, I_SR2, I_CCR, I_TRISE };
enum i2c_status { I_OK, I_INVALID, I_NOT_CONFIGURED, I_WIRING_UNREVIEWED,
    I_TIMEOUT, I_NACK, I_ARBITRATION_LOST, I_BUS_ERROR, I_OVERRUN, I_STATE_ERROR };
struct i2c_io {
    uint32_t (*read)(void *, enum i2c_register);
    void (*write)(void *, enum i2c_register, uint32_t);
    void *context;
    bool configured, reset_required;
    uint32_t last_sr1;
};
struct i2c_result { enum i2c_status status; size_t bytes_queued; bool cleaned_up; };
#define I2C_COMMANDS (I2C_CR1_START | I2C_CR1_STOP | I2C_CR1_PEC)
#define I2C_ERRORS (I2C_SR1_ARLO | I2C_SR1_AF | I2C_SR1_BERR | I2C_SR1_OVR)
#define I2C_MAX_PAYLOAD 32U /* Project test policy, not a silicon limit. */

static inline enum i2c_status i2c_error(struct i2c_io *io)
{
    io->last_sr1 = io->read(io->context, I_SR1);
    if (io->last_sr1 & I2C_SR1_ARLO) return I_ARBITRATION_LOST;
    if (io->last_sr1 & I2C_SR1_BERR) return I_BUS_ERROR;
    if (io->last_sr1 & I2C_SR1_AF) return I_NACK;
    if (io->last_sr1 & I2C_SR1_OVR) return I_OVERRUN;
    return I_OK;
}

static inline enum i2c_status i2c_wait_sr1(struct i2c_io *io, uint32_t mask, uint32_t budget)
{
    for (uint32_t n = 0; n < budget; ++n) {
        enum i2c_status error = i2c_error(io);
        if (error != I_OK) return error; /* Errors win over simultaneous progress. */
        if ((io->last_sr1 & mask) == mask) return I_OK;
    }
    return I_TIMEOUT;
}

static inline enum i2c_status i2c_wait_commands(struct i2c_io *io, uint32_t budget)
{
    for (uint32_t n = 0; n < budget; ++n) {
        enum i2c_status error = i2c_error(io);
        if (error != I_OK) return error;
        if (!(io->read(io->context, I_CR1) & I2C_COMMANDS)) return I_OK;
    }
    return I_TIMEOUT;
}

static inline bool i2c_idle(struct i2c_io *io, uint32_t budget)
{
    /* Only pristine reset/pre-START or STOP-completed stages may call this.
     * Never read SR2 generically while waiting for ADDR.
     */
    for (uint32_t n = 0; n < budget; ++n)
        if (!(io->read(io->context, I_SR2) & I2C_SR2_BUSY)) return true;
    return false;
}

static inline bool i2c_configure(struct i2c_io *io, uint32_t pclk1_hz, bool fresh_reset)
{
    if (!io) return false;
    io->configured = false;
    io->reset_required = true;
    if (!io->read || !io->write || !fresh_reset || pclk1_hz != 42000000U) return false;
    /* Caller must actually enable/read back the RCC gate and pulse I2C1 reset.
     * The boolean is a caller precondition, not a proof of those operations.
     */
    if (io->read(io->context, I_CR1) != 0U || !i2c_idle(io, 1U)) return false;
    io->write(io->context, I_CR2, 42U);
    io->write(io->context, I_OAR1, 0x4000U); /* RM p859 mandatory bit14. */
    io->write(io->context, I_OAR2, 0U);
    io->write(io->context, I_CCR, 210U);
    io->write(io->context, I_TRISE, 43U);
    io->last_sr1 = 0U;
    io->configured = true;
    io->reset_required = false;
    return true; /* PE remains0; configuration emits no transaction. */
}

static inline bool i2c_abort(struct i2c_io *io, bool owned, enum i2c_status reason,
                             uint32_t budget)
{
    io->reset_required = true; /* Never retry without explicit owned reset. */
    if (!owned || reason == I_ARBITRATION_LOST ||
            i2c_error(io) == I_ARBITRATION_LOST) return false;
    if (io->read(io->context, I_CR1) & I2C_COMMANDS) return false;
    io->write(io->context, I_CR1, I2C_CR1_PE | I2C_CR1_STOP);
    /* Preserve the original rc_w0 error flags: don't write SR1 or RMW CR1.
     * Cleanup therefore checks ARLO separately from the retained AF/BERR.
     */
    for (uint32_t n = 0; n < budget; ++n) {
        if (i2c_error(io) == I_ARBITRATION_LOST) return false;
        if (!(io->read(io->context, I_CR1) & I2C_COMMANDS)) {
            if (!i2c_idle(io, budget)) return false;
            /* PE=0 would clear the rc_w0 error flags in hardware. Preserve them
             * with PE unchanged until the caller performs the required reset.
             * Cleanup completion means STOP/idle, not permission to retry.
             */
            return true;
        }
    }
    return false;
}

static inline struct i2c_result i2c_transmit(struct i2c_io *io, uint8_t address,
        const uint8_t *bytes, size_t length, uint32_t budget, bool wiring_reviewed)
{
    struct i2c_result result = {I_INVALID, 0U, false};
    bool owned = false;
    if (!io || !io->read || !io->write || !bytes || !length ||
            length > I2C_MAX_PAYLOAD || address > 0x7FU || !budget) return result;
    /* Project policy excludes reserved address ranges and all bus scanning. */
    if (address < 0x08U || address > 0x77U) return result;
    if (!io->configured || io->reset_required) { result.status = I_NOT_CONFIGURED; return result; }
    if (!wiring_reviewed) { result.status = I_WIRING_UNREVIEWED; return result; }
    if (io->read(io->context, I_CR1) != 0U) { result.status = I_STATE_ERROR; goto failed; }
    if (!i2c_idle(io, budget)) { result.status = I_TIMEOUT; goto failed; }
    io->write(io->context, I_CR1, I2C_CR1_PE);
    io->write(io->context, I_CR1, I2C_CR1_PE | I2C_CR1_START);
    result.status = i2c_wait_sr1(io, I2C_SR1_SB, budget);
    if (result.status != I_OK) goto failed;
    owned = true; /* SB establishes controller mode; ARLO overrides ownership. */
    result.status = i2c_wait_commands(io, budget);
    if (result.status != I_OK) goto failed;
    io->write(io->context, I_DR, (uint32_t)address << 1U);
    result.status = i2c_wait_sr1(io, I2C_SR1_ADDR, budget);
    if (result.status != I_OK) goto failed;
    /* Last SR1 read found ADDR: SR2 read is deliberate clearing, not polling. */
    if ((io->read(io->context, I_SR2) & (I2C_SR2_MSL | I2C_SR2_BUSY | I2C_SR2_TRA))
            != (I2C_SR2_MSL | I2C_SR2_BUSY | I2C_SR2_TRA)) {
        result.status = I_STATE_ERROR;
        goto failed;
    }
    for (size_t n = 0; n < length; ++n) {
        result.status = i2c_wait_sr1(io, I2C_SR1_TXE, budget);
        if (result.status != I_OK) goto failed;
        io->write(io->context, I_DR, bytes[n]);
        ++result.bytes_queued; /* Queued != acknowledged; success requires STOP. */
    }
    result.status = i2c_wait_sr1(io, I2C_SR1_BTF | I2C_SR1_TXE, budget);
    if (result.status != I_OK) goto failed;
    io->write(io->context, I_CR1, I2C_CR1_PE | I2C_CR1_STOP);
    result.status = i2c_wait_commands(io, budget);
    if (result.status != I_OK) goto failed;
    owned = false; /* STOP detected: a later BUSY cannot establish our ownership. */
    if (!i2c_idle(io, budget)) { result.status = I_TIMEOUT; goto failed; }
    io->write(io->context, I_CR1, 0U); /* STOP complete, bus idle: disable allowed. */
    result.cleaned_up = true;
    return result;
failed:
    result.cleaned_up = i2c_abort(io, owned, result.status, budget);
    return result;
}
#endif
