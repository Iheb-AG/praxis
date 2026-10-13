/* Synthetic PM0214 effects, executing the same controller as the ARM example.
 * No simulated elapsed wall time, physical interrupt delivery or board claim.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "core_controller.h"

struct model {
    uint32_t r[CORE_REGISTERS];
    unsigned fault, reads, writes, barriers, violation, enables, clears;
    unsigned load_written, val_written, vector_barrier, enable_barrier;
    unsigned polling, poll_reads, stopping, irq, priority_writes, vector_writes;
};
static uint32_t read_reg(void *context, enum core_register reg)
{
    struct model *m = context;
    ++m->reads;
    if (reg >= CORE_REGISTERS) { ++m->violation; return 0; }
    if (reg == CORE_CTRL) {
        if (m->polling) {
            ++m->poll_reads;
            if (m->fault == 22 && m->poll_reads == 3)
                m->r[reg] |= SysTick_CTRL_COUNTFLAG_Msk;
            if (m->fault == 24 && m->poll_reads == 2)
                m->r[reg] |= SysTick_CTRL_TICKINT_Msk;
        }
        uint32_t value = m->r[reg];
        m->r[reg] &= ~SysTick_CTRL_COUNTFLAG_Msk; /* Read-to-clear effect. */
        return value;
    }
    if (reg == CORE_ICSR)
        return m->r[reg] | SCB_ICSR_PENDSTCLR_Msk; /* Clear-action read is unknown. */
    return m->r[reg];
}
static void write_reg(void *context, enum core_register reg, uint32_t value)
{
    struct model *m = context;
    ++m->writes;
    if (reg == CORE_CTRL) {
        if (value & ~CORE_CONTROL_BITS) ++m->violation;
        if (value & SysTick_CTRL_ENABLE_Msk) {
            ++m->enables;
            if (!m->load_written || !m->val_written || m->r[CORE_LOAD] != 15999U ||
                    m->r[CORE_PRIMASK] != 1U) ++m->violation;
            if (m->irq && (!m->vector_barrier || !m->priority_writes ||
                    m->r[CORE_PRIORITY] != 0xF0U || !m->clears ||
                    (m->r[CORE_ICSR] & SCB_ICSR_PENDSTSET_Msk))) ++m->violation;
            if (!m->irq && (value & SysTick_CTRL_TICKINT_Msk)) ++m->violation;
            if (m->fault == 17) return;
        } else if ((m->fault == 27 && m->stopping) ||
                   (m->fault == 18 && m->load_written)) {
            m->r[reg] = CORE_CONTROL_BITS; return; /* Shutdown acknowledgement fails. */
        }
        m->r[reg] = value;
    } else if (reg == CORE_LOAD) {
        if (value > SysTick_LOAD_RELOAD_Msk || !value || m->r[CORE_CTRL] & 3U)
            ++m->violation;
        ++m->load_written;
        if (m->fault == 14 || m->fault == 18) return;
        m->r[reg] = value;
    } else if (reg == CORE_VAL) {
        if (!m->load_written || value || m->r[CORE_CTRL] & 3U) ++m->violation;
        ++m->val_written;
        if (m->fault == 15) return;
        m->r[reg] = 0U;
        m->r[CORE_CTRL] &= ~SysTick_CTRL_COUNTFLAG_Msk;
        /* Pending SysTick intentionally remains set: a distinct SCB action. */
    } else if (reg == CORE_VTOR) {
        ++m->vector_writes;
        if (!m->irq || value != 0x08000000U || value & 511U || m->r[CORE_CTRL] & 3U)
            ++m->violation;
        if (m->fault == 12) return;
        m->r[reg] = value;
    } else if (reg == CORE_PRIORITY) {
        ++m->priority_writes;
        if (!m->irq || !m->vector_barrier || value != 0xF0U || m->r[CORE_CTRL] & 3U)
            ++m->violation;
        if (m->fault == 13) return;
        m->r[reg] = value;
    } else if (reg == CORE_ICSR) {
        ++m->clears;
        if (!m->irq || value != SCB_ICSR_PENDSTCLR_Msk) ++m->violation;
        if (m->fault == 16 || (m->fault == 28 && m->stopping)) return;
        m->r[reg] &= ~SCB_ICSR_PENDSTSET_Msk; /* Preserve pending NMI/PendSV. */
    } else {
        ++m->violation; /* No clock/status/vector-memory writes, nor CALIB access. */
    }
}
static void barrier(void *context)
{
    struct model *m = context;
    ++m->barriers;
    if (m->vector_writes) m->vector_barrier = 1U;
    if (m->enables) m->enable_barrier = 1U;
}
int main(int argc, char **argv)
{
    if (argc == 4 && !strcmp(argv[1], "period")) {
        uint32_t reload = 0xDEADBEEFU;
        bool ok = core_period((uint32_t)strtoul(argv[2], NULL, 0),
                              (uint32_t)strtoul(argv[3], NULL, 0), &reload);
        printf("{\"ok\":%u,\"reload\":%u}\n", ok, reload);
        return 0;
    }
    struct model m = {0};
    m.fault = argc > 1 ? (unsigned)strtoul(argv[1], NULL, 10) : 0;
    m.irq = !(m.fault >= 22 && m.fault <= 25) && m.fault != 36 && m.fault != 39;
    m.r[CORE_CLOCK] = 16000000U;
    m.r[CORE_RCC_CR] = RCC_CR_HSION | RCC_CR_HSIRDY;
    m.r[CORE_PRIMASK] = 1U;
    m.r[CORE_CTRL] = SysTick_CTRL_COUNTFLAG_Msk; /* Stale flag; no reset assumptions. */
    m.r[CORE_LOAD] = 0xBADU; m.r[CORE_VAL] = 0x1234U;
    m.r[CORE_ICSR] = SCB_ICSR_PENDSTSET_Msk | SCB_ICSR_PENDSVSET_Msk | SCB_ICSR_NMIPENDSET_Msk;
    if (!m.irq && m.fault != 39) m.r[CORE_ICSR] &= ~SCB_ICSR_PENDSTSET_Msk;
    m.r[CORE_VECTOR_SP] = 0x20020000U;
    m.r[CORE_VECTOR_HANDLER] = m.r[CORE_EXPECT_HANDLER] = 0x08000401U;
    if (m.fault == 2) m.r[CORE_PRIMASK] = 0;
    if (m.fault == 3) m.r[CORE_IPSR] = 15;
    if (m.fault == 4) m.r[CORE_CLOCK] = 168000000;
    if (m.fault == 5) m.r[CORE_RCC_CR] &= ~RCC_CR_HSIRDY;
    if (m.fault == 6) m.r[CORE_RCC_CFGR] = RCC_CFGR_PPRE1_2;
    if (m.fault == 7) m.r[CORE_CTRL] |= SysTick_CTRL_ENABLE_Msk;
    if (m.fault == 8) m.r[CORE_VECTOR_SP] = 0x20030000U; /* Wrong contiguous RAM assumption. */
    if (m.fault == 9) m.r[CORE_VECTOR_HANDLER] &= ~1U;
    if (m.fault == 10) m.r[CORE_VECTOR_HANDLER] = 0x20000001U;
    if (m.fault == 11) m.r[CORE_EXPECT_HANDLER] = 0x08000601U;
    if (m.fault == 37) m.r[CORE_CTRL] |= SysTick_CTRL_TICKINT_Msk;
    if (m.fault == 38) m.r[CORE_RCC_CFGR] = RCC_CFGR_SW_PLL;
    struct core_io io = {.read=read_reg, .write=write_reg, .barrier=barrier, .context=&m};
    if (m.fault == 31) io.write = NULL;
    if (m.fault == 32) io.failed = true;
    if (m.fault == 33) io.configured = true;
    if (m.fault == 35) io.owned = true;
    enum core_status status;
    if (m.fault == 29 || m.fault == 30 || m.fault == 35)
        status = core_flash_vector(&io, m.fault == 29 ? 0x08000080U :
                                  m.fault == 30 ? 0x88000000U : CORE_FLASH_TABLE, true);
    else if (m.fault == 34)
        status = core_poll_event(&io, 4U);
    else
        status = core_start(&io, m.fault == 20 ? 0U : m.fault == 21 ? 3U : 1000U,
                            m.fault == 19 ? 16U : 15U, m.irq, m.fault != 1);
    unsigned enabled = m.r[CORE_CTRL] & CORE_CONTROL_BITS, wait = 99U, stopped = 0;
    if (status == CORE_OK && m.fault >= 22 && m.fault <= 26) {
        m.polling = 1;
        m.r[CORE_CTRL] |= SysTick_CTRL_COUNTFLAG_Msk; /* Must not satisfy a fresh wait. */
        wait = core_poll_event(&io, m.fault == 25 ? 0U : 4U);
        m.polling = 0;
    }
    if (status == CORE_OK && m.fault == 36) {
        m.r[CORE_PRIMASK] = 0;
        wait = core_poll_event(&io, 4U);
        m.r[CORE_PRIMASK] = 1;
    }
    if (status == CORE_OK && !io.failed) {
        m.stopping = 1;
        if (m.irq) m.r[CORE_ICSR] |= SCB_ICSR_PENDSTSET_Msk;
        stopped = core_stop(&io);
    }
    unsigned writes = m.writes, retry = 0;
    if (io.failed) {
        retry = core_start(&io, 1000U, 15U, m.irq, true) == CORE_RESET_REQUIRED;
        if (m.writes != writes) ++m.violation;
    }
    printf("{\"status\":%u,\"wait\":%u,\"stopped\":%u,\"violation\":%u,"
           "\"reads\":%u,\"writes\":%u,\"barriers\":%u,\"enables\":%u,"
           "\"load\":%u,\"val\":%u,\"control\":%u,\"enabled_control\":%u,"
           "\"priority\":%u,\"vector\":%u,\"icsr\":%u,\"poll_reads\":%u,"
           "\"failed\":%u,\"failure\":%u,\"quiet\":%u,\"retry_blocked\":%u,"
           "\"priority_writes\":%u,\"vector_writes\":%u}\n",
           status, wait, stopped, m.violation, m.reads, m.writes, m.barriers, m.enables,
           m.r[CORE_LOAD], m.r[CORE_VAL], m.r[CORE_CTRL], enabled,
           m.r[CORE_PRIORITY], m.r[CORE_VTOR], m.r[CORE_ICSR], m.poll_reads,
           io.failed, io.failure, io.quiet, retry, m.priority_writes, m.vector_writes);
    return 0;
}
