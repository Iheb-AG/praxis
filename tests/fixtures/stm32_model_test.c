#include <assert.h>
#include <stdbool.h>
#include <string.h>
#include <stm32f401xe.h>
RCC_TypeDef fixture_rcc;
GPIO_TypeDef fixture_gpio;
USART_TypeDef fixture_usart;
uint32_t fixture_primask;
unsigned fixture_irq_enabled;
unsigned fixture_priority;
extern bool praxis_uart_init(void);
extern bool praxis_uart_init_irq(void);
extern bool praxis_uart_write(uint8_t value, uint32_t budget);
extern void USART2_IRQHandler(void);
extern volatile uint8_t praxis_rx_byte;
extern volatile uint32_t praxis_rx_status;

int main(void) {
    fixture_rcc.CR = 2; /* Model is ready; no oscillator behavior is simulated. */
    fixture_gpio.MODER = 0xA8000000UL;
    fixture_gpio.AFR[0] = 0xF000000FUL;
    assert(praxis_uart_init());
    assert(fixture_usart.BRR == 139);
    assert(fixture_usart.CR1 == 0x200CUL);
    assert(fixture_usart.CR2 == 0 && fixture_usart.CR3 == 0);
    assert((fixture_rcc.APB1ENR & (1UL << 17)) != 0);
    assert((fixture_gpio.MODER & 0xF0) == 0xA0);
    assert((fixture_gpio.MODER & ~0xF0UL) == 0xA8000000UL);
    assert(fixture_gpio.AFR[0] == 0xF000770FUL);
    assert(fixture_primask == 0 && fixture_irq_enabled == 0);
    assert(!praxis_uart_write(0x55, 2));
    fixture_usart.SR = 0x80;
    assert(praxis_uart_write(0x55, 2) && fixture_usart.DR == 0x55);
    assert(praxis_uart_init_irq());
    assert(fixture_irq_enabled && fixture_priority == 5 && fixture_primask == 0);
    fixture_usart.SR = 0x28;
    fixture_usart.DR = 0x42;
    USART2_IRQHandler();
    assert(praxis_rx_byte == 0x42 && praxis_rx_status == 0x28);
    fixture_rcc.CR = 0;
    fixture_gpio.MODER = 0x12345678;
    assert(!praxis_uart_init());
    assert(fixture_gpio.MODER == 0x12345678); /* Clock timeout blocks later stages. */
    return 0;
}

