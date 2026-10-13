#include <assert.h>
#include <stdbool.h>
#include <avr/io.h>
volatile uint8_t fixture_avr[256];
extern bool praxis_uart_init(void);
extern bool praxis_uart_init_irq(void);
extern bool praxis_uart_write(uint8_t value, uint16_t budget);
extern void fixture_avr_rx_handler(void);
extern volatile uint8_t praxis_rx_byte;
extern volatile uint8_t praxis_rx_status;

int main(void) {
    PRR = 0xFF;
    DDRD = 0xF0;
    PORTD = 0xFF;
    SREG = 0x80;
    assert(praxis_uart_init());
    assert(PRR == 0xFD && DDRD == 0xF2 && PORTD == 0xFE);
    assert(UBRR0H == 0 && UBRR0L == 103);
    assert(UCSR0A == 0 && UCSR0B == 0x18 && UCSR0C == 6);
    assert(SREG == 0x80); /* Restore prior global state only after initialization. */
    assert(!praxis_uart_write(0x55, 2));
    UCSR0A = 0x20;
    assert(praxis_uart_write(0x55, 2) && UDR0 == 0x55);
    assert(praxis_uart_init_irq());
    assert(UCSR0B == 0x98 && SREG == 0x80);
    UCSR0A = 0x90;
    UDR0 = 0x42;
    fixture_avr_rx_handler();
    assert(praxis_rx_byte == 0x42 && praxis_rx_status == 0x90);
    CLKPR = 1;
    DDRD = 0xF0;
    assert(!praxis_uart_init());
    assert(DDRD == 0xF0 && SREG == 0x80);
    return 0;
}

