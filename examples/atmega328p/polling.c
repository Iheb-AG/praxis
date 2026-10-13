#include <stdbool.h>
#include <stdint.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include "praxis_sequence.h"

#ifndef F_CPU
#error F_CPU must describe the reviewed fixture clock
#endif
_Static_assert(F_CPU == 16000000UL, "Fixture clock mismatch");
_Static_assert(_SFR_MEM_ADDR(UCSR0A) == 0xC0, "USART data-space address");
_Static_assert(_SFR_IO_ADDR(DDRD) == 0x0A, "GPIO I/O address");
_Static_assert(_SFR_MEM_ADDR(DDRD) == 0x2A, "GPIO data-space address");
_Static_assert(sizeof(UDR0) == 1, "USART access width");
_Static_assert(USART_RX_vect_num == 18, "Receive vector number");

enum { PRAXIS_UBRR = 103 };
_Static_assert(PRAXIS_UBRR == (F_CPU + 16UL * 9600UL / 2) / (16UL * 9600UL) - 1,
               "Rounded normal-mode divider");

static bool clocks(void) {
    if ((CLKPR & 0x0F) != 0) {
        return false; /* Do not invent a timed clock/fuse reconfiguration. */
    }
    PRR &= (uint8_t)~(1U << PRUSART0);
    return true;
}

static bool pins(void) {
    DDRD = (DDRD & (uint8_t)~(1U << DDD0)) | (1U << DDD1);
    PORTD &= (uint8_t)~(1U << PORTD0);
    return true;
}

static bool control(void) {
    UCSR0B = 0;
    UCSR0A = 0;
    UBRR0H = (uint8_t)(PRAXIS_UBRR >> 8);
    UBRR0L = (uint8_t)PRAXIS_UBRR;
    UCSR0C = (1U << UCSZ01) | (1U << UCSZ00);
    UCSR0B = (1U << RXEN0) | (1U << TXEN0);
    return true;
}

bool praxis_uart_init_with_irq(praxis_stage irq) {
    uint8_t previous = SREG;
    cli();
    bool result = praxis_bring_up(clocks, pins, control, irq);
    SREG = previous;
    return result;
}

bool praxis_uart_init(void) {
    return praxis_uart_init_with_irq(0);
}

bool praxis_uart_write(uint8_t value, uint16_t budget) {
    while (budget-- > 0) {
        if (UCSR0A & (1U << UDRE0)) {
            UDR0 = value;
            return true;
        }
    }
    return false;
}

