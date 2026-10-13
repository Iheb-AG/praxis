#include <stdbool.h>
#include <stdint.h>
#include <stm32f401xe.h>
#include "praxis_sequence.h"

extern bool praxis_uart_init_with_irq(praxis_stage irq);
volatile uint32_t praxis_rx_status;
volatile uint8_t praxis_rx_byte;

static bool receive_irq(void) {
    volatile uint32_t status = USART2->SR;
    volatile uint32_t drained = USART2->DR;
    (void)status;
    (void)drained;
    NVIC_SetPriority(USART2_IRQn, 5);
    NVIC_ClearPendingIRQ(USART2_IRQn);
    USART2->CR1 |= USART_CR1_RXNEIE;
    NVIC_EnableIRQ(USART2_IRQn);
    return true;
}

bool praxis_uart_init_irq(void) {
    return praxis_uart_init_with_irq(receive_irq);
}

void USART2_IRQHandler(void) {
    uint32_t status = USART2->SR;
    if (status & (USART_SR_RXNE | USART_SR_ORE | USART_SR_FE | USART_SR_NE | USART_SR_PE)) {
        uint8_t value = (uint8_t)USART2->DR;
        praxis_rx_status = status;
        if (status & USART_SR_RXNE) {
            praxis_rx_byte = value;
        }
    }
}

