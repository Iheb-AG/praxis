#ifndef PRAXIS_AVR_INTERRUPTS_MODEL_H
#define PRAXIS_AVR_INTERRUPTS_MODEL_H
#include <avr/io.h>
#define cli() (SREG &= (uint8_t)~0x80U)
#define ISR(vector) void vector(void)
#endif

