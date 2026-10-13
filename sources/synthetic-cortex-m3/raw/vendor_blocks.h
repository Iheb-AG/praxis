/* Fictional vendor declarations with _Type suffix, MIT. */
#ifndef PRAXIS_DEMO_BLOCKS_H
#define PRAXIS_DEMO_BLOCKS_H
typedef struct { volatile unsigned int CTRL; } CLOCK_Type;
typedef struct { volatile unsigned int ROUTE[2]; } PINMUX_Type;
typedef struct {
    volatile unsigned int CTRL;
    unsigned int RESERVED[3];
    volatile unsigned char DATA[4];
} UART_Type;
typedef struct { volatile unsigned int ENABLE; } IRQCTRL_Type;
#endif
