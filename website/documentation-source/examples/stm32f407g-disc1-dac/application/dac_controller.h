/* Source-backed DAC channel1 one-shot software trigger; digital evidence only.
 * RM0090 Rev22 pp437-440,447-455; DS8626 Rev12 pp141-143.
 * This implementation also runs in the host MMIO-effect model.
 */
#ifndef PRAXIS_DAC_CONTROLLER_H
#define PRAXIS_DAC_CONTROLLER_H
#include <stdbool.h>
#include <stdint.h>
#include <stm32f407xx.h>

enum dac_register { D_CR, D_SWTRIGR, D_DHR12R1, D_DOR1, D_SR };
enum dac_status { D_OK, D_INVALID, D_NOT_CONFIGURED, D_OUTPUT_UNREVIEWED,
    D_WAIT_FAILED, D_UNDERRUN, D_STATE_ERROR, D_TIMEOUT };
struct dac_io {
    uint32_t (*read)(void *, enum dac_register);
    void (*write)(void *, enum dac_register, uint32_t);
    /* A bounded nominal1ms wait from the reviewed TIM2 clock/delay contract.
     * Reinitialize/discard a stale update for each invocation, even equal codes.
     */
    bool (*wait_interval)(void *, uint32_t);
    void *context;
    bool configured, reset_required, owns_output;
    uint32_t last_status;
};
struct dac_result {
    enum dac_status status;
    uint32_t code;
    bool digital_loaded, analog_settled, cleaned_up;
};
#define DAC_SOFTWARE_CONFIG (DAC_CR_TEN1 | DAC_CR_TSEL1)
#define DAC_OWNED_OUTPUT (DAC_SOFTWARE_CONFIG | DAC_CR_EN1)
#define DAC_ERRORS (DAC_SR_DMAUDR1 | DAC_SR_DMAUDR2)

static inline bool dac_configure(struct dac_io *io, uint32_t pclk1_hz, bool fresh_reset)
{
    if (!io) return false;
    /* A held/externally changed output cannot be silently taken over. */
    bool held = io->owns_output;
    io->configured = false;
    io->reset_required = true;
    if (!io->read || !io->write || !io->wait_interval || held ||
            !fresh_reset || pclk1_hz != 42000000U) return false;
    if (io->read(io->context, D_CR) != 0U || io->read(io->context, D_SR) != 0U)
        return false;
    io->write(io->context, D_CR, DAC_SOFTWARE_CONFIG); /* EN1=EN2=0. */
    if (io->read(io->context, D_CR) != DAC_SOFTWARE_CONFIG) return false;
    io->last_status = 0U;
    io->configured = true;
    io->reset_required = false;
    return true;
}

static inline bool dac_shutdown(struct dac_io *io)
{
    if (!io || !io->read || !io->write) return false;
    io->configured = false;
    io->reset_required = true;
    if (!io->owns_output) return false;
    /* Do not clear channel2 or overwrite a different owner/configuration. */
    if (io->read(io->context, D_CR) != DAC_OWNED_OUTPUT) return false;
    io->write(io->context, D_CR, DAC_SOFTWARE_CONFIG);
    if (io->read(io->context, D_CR) != DAC_SOFTWARE_CONFIG) return false;
    io->owns_output = false;
    return true; /* Status retained; an owned reset is still required. */
}

static inline struct dac_result dac_output_once(struct dac_io *io, uint32_t code,
        uint32_t budget, bool output_reviewed)
{
    struct dac_result result = {D_INVALID, 0U, false, false, false};
    if (!io || !io->read || !io->write || !io->wait_interval || code > 4095U || !budget)
        return result;
    if (!io->configured || io->reset_required) {
        result.status = D_NOT_CONFIGURED; return result;
    }
    /* A flag describes a caller precondition; it cannot review missing wiring. */
    if (!output_reviewed) { result.status = D_OUTPUT_UNREVIEWED; return result; }
    if (io->owns_output) { result.status = D_STATE_ERROR; return result; }
    if (io->read(io->context, D_CR) != DAC_SOFTWARE_CONFIG) {
        result.status = D_STATE_ERROR; goto failed;
    }
    io->last_status = io->read(io->context, D_SR);
    if (io->last_status != 0U) { result.status = D_UNDERRUN; goto failed; }
    io->write(io->context, D_DHR12R1, code);
    if (io->read(io->context, D_DHR12R1) != code) {
        result.status = D_STATE_ERROR; goto failed;
    }
    io->write(io->context, D_CR, DAC_OWNED_OUTPUT);
    io->owns_output = true;
    if (io->read(io->context, D_CR) != DAC_OWNED_OUTPUT) {
        result.status = D_STATE_ERROR; goto failed;
    }
    if (!io->wait_interval(io->context, budget)) {
        result.status = D_WAIT_FAILED; goto failed;
    }
    io->last_status = io->read(io->context, D_SR);
    if (io->last_status != 0U) { result.status = D_UNDERRUN; goto failed; }
    if (io->read(io->context, D_CR) != DAC_OWNED_OUTPUT) {
        result.status = D_STATE_ERROR; goto failed;
    }
    /* SWTRIGR is WO: no read, polling or RMW, including for command clearance. */
    io->write(io->context, D_SWTRIGR, DAC_SWTRIGR_SWTRIG1);
    /* Even an unchanged DOR code cannot replace a completed fresh interval. */
    if (!io->wait_interval(io->context, budget)) {
        result.status = D_WAIT_FAILED; goto failed;
    }
    for (uint32_t n = 0; n < budget; ++n) {
        io->last_status = io->read(io->context, D_SR);
        if (io->last_status != 0U) { result.status = D_UNDERRUN; goto failed; }
        if (io->read(io->context, D_CR) != DAC_OWNED_OUTPUT) {
            result.status = D_STATE_ERROR; goto failed;
        }
        uint32_t observed = io->read(io->context, D_DOR1);
        /* Recheck errors after the output observation; matching data cannot
         * swallow an error arriving during that read. No reserved-bit masking.
         */
        io->last_status = io->read(io->context, D_SR);
        if (io->last_status != 0U) { result.status = D_UNDERRUN; goto failed; }
        if (observed == code) {
            result.status = D_OK;
            result.code = observed;
            result.digital_loaded = true;
            return result; /* Analog settling/voltage remains unestablished. */
        }
    }
    result.status = D_TIMEOUT;
failed:
    io->configured = false;
    io->reset_required = true;
    if (io->owns_output) result.cleaned_up = dac_shutdown(io);
    return result;
}
#endif
