/* Source-backed candidate: actual ingestion MCP, DS8626 pp58/67 and
 * MB997-E-01 sheets2/7; RM0090 pp283/285/287. No physical qualification.
 * Own PD0, with P2:34 externally unconnected. Never drive a GPIO output.
 */
#ifndef PRAXIS_CAN_RX_ROUTE_H
#define PRAXIS_CAN_RX_ROUTE_H
#include <stdbool.h>
#include <stdint.h>
#include <stm32f407xx.h>

enum rx_reg { RX_GATE, RX_MODE, RX_PULL, RX_AF, RX_INPUT, RX_LOCK };
enum rx_status { RX_OK, RX_INVALID, RX_GATE_FAILED, RX_OWNED, RX_WRITE_FAILED, RX_LOW };
struct rx_io {
    uint32_t (*read)(void *, enum rx_reg);
    void (*write)(void *, enum rx_reg, uint32_t);
    void (*fence)(void *);
    void *context;
};
static inline bool rx_write_checked(struct rx_io *io, enum rx_reg reg, uint32_t value)
{
    io->write(io->context, reg, value);
    return io->read(io->context, reg) == value;
}
static inline enum rx_status can_rx_route(struct rx_io *io, bool exclusive_pd0, uint32_t budget)
{
    if (!io || !io->read || !io->write || !io->fence || !budget) return RX_INVALID;
    if (!exclusive_pd0) return RX_OWNED;
    uint32_t gates = io->read(io->context, RX_GATE);
    if (!rx_write_checked(io, RX_GATE, gates | RCC_AHB1ENR_GPIODEN)) return RX_GATE_FAILED;
    io->fence(io->context);
    uint32_t mode = io->read(io->context, RX_MODE);
    uint32_t pull = io->read(io->context, RX_PULL);
    uint32_t af = io->read(io->context, RX_AF);
    if ((mode & 3U) || (pull & 3U) || (af & 15U) || io->read(io->context, RX_LOCK))
        return RX_OWNED;
    /* Set the bias while still an input, then route RX. Other pins are preserved. */
    if (!rx_write_checked(io, RX_PULL, pull | 1U) ||
            !rx_write_checked(io, RX_AF, af | 9U) ||
            !rx_write_checked(io, RX_MODE, mode | 2U)) return RX_WRITE_FAILED;
    io->fence(io->context);
    for (uint32_t n = 0; n < budget; ++n) {
        if (io->read(io->context, RX_INPUT) & 1U) return RX_OK;
    }
    /* Retain the input route for diagnosis. Do not drive high, drain or retry. */
    return RX_LOW;
}
#endif
