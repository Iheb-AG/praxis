/* Synthetic DAC MMIO effects, executing the same controller as the ARM example.
 * The wait callback models a completed fresh interval, not analog settling.
 */
#include <stdio.h>
#include <stdlib.h>
#include "dac_controller.h"

struct model {
    uint32_t r[5], requested;
    unsigned fault, reads, writes, waits, timer_attempts, triggers, enabled;
    unsigned violation, transfers, dor_reads, enable_writes, shutdowns;
};
static uint32_t read_reg(void *context, enum dac_register name)
{
    struct model *m = context;
    ++m->reads;
    if (name == D_SWTRIGR) ++m->violation; /* WO has no pollable read contract. */
    if (name == D_DOR1) {
        ++m->dor_reads;
        if (m->waits != 2 || !m->triggers) ++m->violation;
        if (m->fault == 15) m->r[D_SR] |= DAC_SR_DMAUDR1;
    }
    return m->r[name];
}
static void write_reg(void *context, enum dac_register name, uint32_t value)
{
    struct model *m = context;
    ++m->writes;
    if (name == D_DOR1 || name == D_SR) ++m->violation;
    if (name == D_CR) {
        if (value != DAC_SOFTWARE_CONFIG && value != DAC_OWNED_OUTPUT) ++m->violation;
        if (m->r[D_CR] & DAC_CR_EN2) ++m->violation;
        if (m->fault == 7 && !m->enable_writes) return; /* Config write lost. */
        if (value & DAC_CR_EN1) {
            ++m->enable_writes;
            if (m->r[D_DHR12R1] != m->requested || m->waits) ++m->violation;
            m->enabled = 1;
            if (m->fault == 28) value |= DAC_CR_BOFF1;
        } else if (m->enabled) {
            ++m->shutdowns;
            if (m->fault == 23) return; /* Cleanup acknowledgement lost. */
            m->enabled = 0;
        }
    }
    if (name == D_DHR12R1) {
        if (m->enabled || value > 4095U || m->r[D_CR] != DAC_SOFTWARE_CONFIG)
            ++m->violation;
        if (m->fault == 17) return;
    }
    if (name == D_SWTRIGR) {
        if (!m->enabled || m->waits != 1 || value != DAC_SWTRIGR_SWTRIG1 ||
                m->r[D_CR] != DAC_OWNED_OUTPUT || m->r[D_SR]) ++m->violation;
        ++m->triggers;
        /* WO: the model never exposes this command as a readable status bit. */
        return;
    }
    m->r[name] = value;
}
static bool wait_interval(void *context, uint32_t budget)
{
    struct model *m = context;
    ++m->waits;
    if (!m->enabled || m->waits > 2 || (m->waits == 2 && !m->triggers))
        ++m->violation;
    bool blocked = (m->fault == 9 && m->waits == 1) ||
                   ((m->fault == 10 || m->fault == 20) && m->waits == 2);
    for (uint32_t n = 0; n < budget; ++n) {
        ++m->timer_attempts;
        if (n < 1 || blocked) continue; /* Fresh interval, not a stale equality. */
        if (m->waits == 1 && m->fault == 13) m->r[D_SR] |= DAC_SR_DMAUDR1;
        if (m->waits == 1 && m->fault == 16) m->r[D_CR] |= DAC_CR_EN2;
        if (m->waits == 2) {
            if (m->fault != 11) {m->r[D_DOR1] = m->r[D_DHR12R1]; ++m->transfers;}
            if (m->fault == 18) m->r[D_DOR1] |= 0x1000U;
            if (m->fault == 14) m->r[D_SR] |= DAC_SR_DMAUDR1;
            if (m->fault == 29) m->r[D_SR] |= DAC_SR_DMAUDR2;
        }
        return true;
    }
    return false;
}
int main(int argc, char **argv)
{
    unsigned fault = argc > 1 ? (unsigned)strtoul(argv[1], NULL, 10) : 0;
    struct model m = {.requested = 2048U, .fault = fault};
    struct dac_io io = {read_reg, write_reg, wait_interval, &m, false, true, false, 0U};
    if (fault == 6) m.r[D_CR] = DAC_CR_EN2;
    if (fault == 8) m.r[D_SR] = DAC_SR_DMAUDR1;
    if (fault == 27) io.wait_interval = NULL;
    bool configured = dac_configure(&io, fault == 4 ? 16000000U : 42000000U, fault != 5);
    if (fault == 25) configured = dac_configure(&io, 16000000U, true);
    unsigned config_writes = m.writes, config_reads = m.reads;
    if (fault == 12) m.r[D_SR] = DAC_SR_DMAUDR1;
    if (fault == 19 || fault == 20) m.r[D_DOR1] = m.requested;
    if (fault == 24) m.r[D_CR] |= DAC_CR_BOFF1;
    struct dac_result result = dac_output_once(&io, fault == 1 ? 4096U : m.requested,
                                               fault == 2 ? 0U : fault == 26 ? 1U : 3U,
                                               fault != 3);
    unsigned calls = m.reads + m.writes;
    bool retry_blocked = true, stopped = false;
    if (io.reset_required) {
        struct dac_result retry = dac_output_once(&io, m.requested, 3U, true);
        retry_blocked = retry.status == D_NOT_CONFIGURED && m.reads + m.writes == calls;
    }
    if (fault == 21) {
        struct dac_result retry = dac_output_once(&io, m.requested, 3U, true);
        retry_blocked = retry.status == D_STATE_ERROR && m.reads + m.writes == calls;
    }
    if (fault == 22 || fault == 23) stopped = dac_shutdown(&io);
    printf("{\"configured\":%u,\"status\":%u,\"loaded\":%u,\"analog\":%u,"
        "\"code\":%u,\"cleaned\":%u,\"reset_required\":%u,\"owned\":%u,"
        "\"triggers\":%u,\"waits\":%u,\"timer_attempts\":%u,\"transfers\":%u,"
        "\"dor_reads\":%u,\"violation\":%u,\"calls\":%u,\"config_writes\":%u,"
        "\"config_reads\":%u,\"writes\":%u,\"cr\":%u,\"sr\":%u,"
        "\"retry_blocked\":%u,\"stopped\":%u}\n", configured, result.status,
        result.digital_loaded, result.analog_settled, result.code, result.cleaned_up,
        io.reset_required, io.owns_output, m.triggers, m.waits, m.timer_attempts,
        m.transfers, m.dor_reads, m.violation, calls, config_writes, config_reads,
        m.writes, m.r[D_CR], m.r[D_SR], retry_blocked, stopped);
    return 0;
}
