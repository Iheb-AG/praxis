/* Digital register effects only; no physical pull strength, signal timing or silicon model. */
#include <stdio.h>
#include <stdlib.h>
#include "can_rx_route.h"
struct model {
    uint32_t r[6];
    unsigned fault, reads, writes, stage, inputs, violation, fences;
};
static uint32_t read_reg(void *context, enum rx_reg reg)
{
    struct model *m = context;
    ++m->reads;
    if (reg != RX_GATE && !(m->r[RX_GATE] & RCC_AHB1ENR_GPIODEN)) ++m->violation;
    if (reg == RX_INPUT) {
        if (m->stage != 3U || !m->fences) ++m->violation;
        ++m->inputs;
        if (m->fault != 10 && !(m->fault == 11 && m->inputs < 3U)) return 1U;
        return 0U;
    }
    return m->r[reg];
}
static void write_reg(void *context, enum rx_reg reg, uint32_t value)
{
    struct model *m = context;
    ++m->writes;
    if (reg == RX_INPUT || reg == RX_LOCK) ++m->violation;
    if (reg != RX_GATE && !(m->r[RX_GATE] & RCC_AHB1ENR_GPIODEN)) ++m->violation;
    if (reg == RX_GATE && m->fault == 1) return;
    if (reg == RX_PULL) {
        if (m->stage || (value & 3U) != 1U) ++m->violation;
        if (m->fault == 7) return;
        m->stage = 1U;
    }
    if (reg == RX_AF) {
        if (m->stage != 1U || (value & 15U) != 9U) ++m->violation;
        if (m->fault == 8) return;
        m->stage = 2U;
    }
    if (reg == RX_MODE) {
        if (m->stage != 2U || (value & 3U) != 2U) ++m->violation;
        if (m->fault == 9) return;
        m->stage = 3U;
    }
    m->r[reg] = value;
}
static void fence(void *context) { ++((struct model *)context)->fences; }
int main(int argc, char **argv)
{
    struct model m = {.fault = argc > 1 ? (unsigned)strtoul(argv[1], NULL, 10) : 0U};
    m.r[RX_GATE] = 0x20000000U;
    m.r[RX_MODE] = 0xA0000000U;
    m.r[RX_PULL] = 0x40000000U;
    m.r[RX_AF] = 0x70000000U;
    if (m.fault == 2) m.r[RX_MODE] |= 2U;
    if (m.fault == 3) m.r[RX_PULL] |= 2U;
    if (m.fault == 4) m.r[RX_AF] |= 7U;
    if (m.fault == 5) m.r[RX_LOCK] = 0x10001U;
    struct rx_io io = {.read = read_reg, .write = write_reg, .fence = fence, .context = &m};
    if (m.fault == 13) io.read = NULL;
    enum rx_status status = can_rx_route(&io, m.fault != 6, m.fault == 12 ? 0U : 8U);
    printf("{\"status\":%u,\"violation\":%u,\"reads\":%u,\"writes\":%u,"
           "\"stage\":%u,\"inputs\":%u,\"gate\":%u,\"mode\":%u,\"pull\":%u,\"af\":%u}\n",
           status,m.violation,m.reads,m.writes,m.stage,m.inputs,
           m.r[RX_GATE],m.r[RX_MODE],m.r[RX_PULL],m.r[RX_AF]);
    return 0;
}
