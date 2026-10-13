/* Host-only instrumented register model; not an AVR header replacement. */
#ifndef PRAXIS_AVR_MODEL_H
#define PRAXIS_AVR_MODEL_H
#include <stdint.h>
extern volatile uint8_t fixture_avr[256];
#define CLKPR fixture_avr[0x61]
#define PRR fixture_avr[0x64]
#define DDRD fixture_avr[0x2A]
#define PORTD fixture_avr[0x2B]
#define UCSR0A fixture_avr[0xC0]
#define UCSR0B fixture_avr[0xC1]
#define UCSR0C fixture_avr[0xC2]
#define UBRR0L fixture_avr[0xC4]
#define UBRR0H fixture_avr[0xC5]
#define UDR0 fixture_avr[0xC6]
#define SREG fixture_avr[0x5F]
#define PRAXIS_ADDR_UCSR0A 0xC0
#define PRAXIS_ADDR_DDRD 0x2A
#define PRAXIS_IO_DDRD 0x0A
#define _SFR_MEM_ADDR(reg) PRAXIS_ADDR_##reg
#define _SFR_IO_ADDR(reg) PRAXIS_IO_##reg
#define PRUSART0 1
#define DDD0 0
#define DDD1 1
#define PORTD0 0
#define UCSZ00 1
#define UCSZ01 2
#define RXEN0 4
#define TXEN0 3
#define RXCIE0 7
#define RXC0 7
#define UDRE0 5
#define USART_RX_vect_num 18
#define USART_RX_vect fixture_avr_rx_handler
#endif

