/* Fictional portability fixture, MIT. This is not a real vendor header. */
#ifndef PRAXIS_DEMO_M3_H
#define PRAXIS_DEMO_M3_H
#define PRAXIS_DEMO_PART 3
#if !defined(__ARM_ARCH_7M__)
#error "The synthetic target requires Cortex-M3 preprocessing"
#endif
#include "vendor_blocks.h"
#define CLOCK0_BASE 0x40000000UL
#define CLOCK0 ((CLOCK_Type *) CLOCK0_BASE)
#define PINMUX0_BASE 0x40001000UL
#define PINMUX0 ((PINMUX_Type *) PINMUX0_BASE)
#define UART0_BASE 0x40002000UL
#define UART0 ((UART_Type *) UART0_BASE)
#define IRQCTRL0_BASE 0x40003000UL
#define IRQCTRL0 ((IRQCTRL_Type *) IRQCTRL0_BASE)
#define CLK_CTRL_ENABLE_SHIFT 0U
#define CLK_CTRL_ENABLE_MASK (1UL << CLK_CTRL_ENABLE_SHIFT)
#define CLK_CTRL_RESET_VALUE 0U
#define PIN_ROUTE_SELECT_SHIFT 4U
#define PIN_ROUTE_SELECT_MASK (0xFUL << PIN_ROUTE_SELECT_SHIFT)
#define UART_CTRL_ENABLE_SHIFT 2U
#define UART_CTRL_ENABLE_MASK (1UL << UART_CTRL_ENABLE_SHIFT)
#define UART_CTRL_RESET_VALUE 0U
#define IRQ_ENABLE_LINE_SHIFT 0U
#define IRQ_ENABLE_LINE_MASK 0xFFFFFFFFUL
#endif
