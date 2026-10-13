#include <stdbool.h>
#include <stdint.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include "praxis_sequence.h"

extern bool praxis_uart_init_with_irq(praxis_stage irq);
volatile uint8_t praxis_rx_status;
volatile uint8_t praxis_rx_byte;

static bool receive_irq(void) {
    if (UCSR0A & (1U << RXC0)) {
        volatile uint8_t status = UCSR0A;
        volatile uint8_t drained = UDR0;
        (void)status;
        (void)drained;
    }
    UCSR0B |= (1U << RXCIE0);
    return true;
}

bool praxis_uart_init_irq(void) {
    return praxis_uart_init_with_irq(receive_irq);
}

ISR(USART_RX_vect) {
    uint8_t status = UCSR0A;
    uint8_t value = UDR0;
    praxis_rx_status = status;
    praxis_rx_byte = value;
}

