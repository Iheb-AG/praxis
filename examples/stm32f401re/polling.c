#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stm32f401xe.h>
#include "praxis_sequence.h"

_Static_assert(offsetof(USART_TypeDef, BRR) == 0x08, "USART BRR layout");
_Static_assert(offsetof(USART_TypeDef, CR1) == 0x0C, "USART CR1 layout");
_Static_assert(sizeof(((USART_TypeDef *)0)->DR) == 4, "USART access width");
_Static_assert(offsetof(GPIO_TypeDef, AFR[0]) == 0x20, "GPIO AFRL layout");
_Static_assert(offsetof(RCC_TypeDef, APB1ENR) == 0x40, "RCC bus gate layout");
_Static_assert(RCC_APB1ENR_USART2EN == (1UL << 17), "USART2 bus gate bit");
_Static_assert(USART2_IRQn == 38, "USART2 vector number");

enum { PRAXIS_BRR = 139, PRAXIS_AF = 7, PRAXIS_BUDGET = 100000 };
_Static_assert(PRAXIS_BRR == (16000000UL + 115200UL / 2) / 115200UL, "Rounded BRR");

static bool wait_mask(volatile uint32_t *address, uint32_t mask, uint32_t expected) {
    for (uint32_t remaining = PRAXIS_BUDGET; remaining > 0; --remaining) {
        if ((*address & mask) == expected) {
            return true;
        }
    }
    return false;
}

static bool clocks(void) {
    /* Startup must have quiesced other users of the system clock. */
    RCC->CR |= RCC_CR_HSION;
    if (!wait_mask(&RCC->CR, RCC_CR_HSIRDY, RCC_CR_HSIRDY)) {
        return false;
    }
    RCC->CFGR &= ~RCC_CFGR_SW;
    if (!wait_mask(&RCC->CFGR, RCC_CFGR_SWS, 0)) {
        return false;
    }
    RCC->CFGR &= ~(RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2);
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;
    (void)RCC->AHB1ENR;
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN;
    (void)RCC->APB1ENR;
    RCC->APB1RSTR |= RCC_APB1RSTR_USART2RST;
    RCC->APB1RSTR &= ~RCC_APB1RSTR_USART2RST;
    return true;
}

static bool pins(void) {
    GPIOA->MODER = (GPIOA->MODER & ~((3UL << 4) | (3UL << 6))) | (2UL << 4) | (2UL << 6);
    GPIOA->OTYPER &= ~((1UL << 2) | (1UL << 3));
    GPIOA->OSPEEDR = (GPIOA->OSPEEDR & ~((3UL << 4) | (3UL << 6))) | (1UL << 4) | (1UL << 6);
    GPIOA->PUPDR &= ~((3UL << 4) | (3UL << 6));
    GPIOA->AFR[0] = (GPIOA->AFR[0] & ~((15UL << 8) | (15UL << 12))) |
                    (PRAXIS_AF << 8) | (PRAXIS_AF << 12);
    return true;
}

static bool control(void) {
    USART2->CR1 = 0;
    USART2->BRR = PRAXIS_BRR;
    USART2->CR2 = 0;
    USART2->CR3 = 0;
    USART2->CR1 = USART_CR1_UE | USART_CR1_TE | USART_CR1_RE;
    return true;
}

bool praxis_uart_init_with_irq(praxis_stage irq) {
    uint32_t previous = __get_PRIMASK();
    __disable_irq();
    NVIC_DisableIRQ(USART2_IRQn);
    bool result = praxis_bring_up(clocks, pins, control, irq);
    __set_PRIMASK(previous);
    return result;
}

bool praxis_uart_init(void) {
    return praxis_uart_init_with_irq(0);
}

bool praxis_uart_write(uint8_t value, uint32_t budget) {
    while (budget-- > 0) {
        if (USART2->SR & USART_SR_TXE) {
            USART2->DR = value;
            return true;
        }
    }
    return false;
}

