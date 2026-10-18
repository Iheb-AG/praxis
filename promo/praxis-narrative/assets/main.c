/* Hardware facts: actual Praxis knowledge MCP responses, bundle revision
 * 1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b.
 * Reviewed subset: RCC/GPIO/USART2/TIM2/SYSCFG/EXTI0/NVIC.
 * MB997-E-01 reference; physical PCB revision is not confirmed.
 */
#include <stm32f407xx.h>
#include <stddef.h>
#include "controller.h"
#include "queue.h"

_Static_assert(offsetof(TIM_TypeDef, PSC) == 0x28U, "TIM PSC offset");
_Static_assert(offsetof(TIM_TypeDef, ARR) == 0x2CU, "TIM ARR offset");
_Static_assert(offsetof(USART_TypeDef, BRR) == 8U, "USART BRR offset");
_Static_assert(offsetof(SYSCFG_TypeDef, EXTICR) == 8U, "EXTICR layout");
_Static_assert(offsetof(EXTI_TypeDef, PR) == 0x14U, "EXTI PR offset");
_Static_assert(TIM2_IRQn == 28 && USART2_IRQn == 38 && EXTI0_IRQn == 6, "IRQ identities");
_Static_assert(__NVIC_PRIO_BITS == 4, "NVIC priorities");

#define LED_GREEN (1U << 12)
#define LED_ORANGE (1U << 13)
#define LED_RED (1U << 14)
#define LED_BLUE (1U << 15)
#define LED_ALL (LED_GREEN | LED_ORANGE | LED_RED | LED_BLUE)

static Queue rx, tx;
static volatile uint32_t milliseconds, button_generation;
static volatile uint32_t uart_errors, queue_overflows;
static volatile bool io_failure;

/* Main accesses queue indices/data only with interrupts masked. ISR executes
   with main suspended. DMB precedes publication/interrupt unmasking; volatile
   alone is not relied on for synchronization. These sections never wait. */
static uint32_t lock(void) { uint32_t saved = __get_PRIMASK(); __disable_irq(); __DMB(); return saved; }
static void unlock(uint32_t saved) { __DMB(); __set_PRIMASK(saved); }

void TIM2_IRQHandler(void)
{
    if (TIM2->SR & TIM_SR_UIF) {
        TIM2->SR = 0U; /* rc_w0; this timer owns update events only. */
        ++milliseconds;
    }
}

void EXTI0_IRQHandler(void)
{
    if (EXTI->PR & 1U) {
        EXTI->PR = 1U; /* W1C; do not read-modify-write PR. */
        ++button_generation;
    }
}

void USART2_IRQHandler(void)
{
    const uint32_t sr = USART2->SR;
    const uint32_t errors = sr & (USART_SR_ORE | USART_SR_FE | USART_SR_NE);
    if ((sr & USART_SR_RXNE) || errors) {
        const uint8_t byte = (uint8_t)USART2->DR; /* SR then DR clears sampled errors. */
        if (errors) { ++uart_errors; io_failure = true; }
        else {
            if (!queue_push(&rx, byte)) { ++queue_overflows; io_failure = true; }
        }
    }
    if ((sr & USART_SR_TXE) && (USART2->CR1 & USART_CR1_TXEIE)) {
        uint8_t byte;
        if (queue_pop(&tx, &byte)) USART2->DR = byte;
        if (tx.tail == tx.head) USART2->CR1 &= ~USART_CR1_TXEIE;
    }
}

static bool clock_init(void)
{
    uint32_t budget = 1000000U;
    RCC->CR |= RCC_CR_HSION;
    while (!(RCC->CR & RCC_CR_HSIRDY)) if (--budget == 0U) return false;
    RCC->CFGR = (RCC->CFGR & ~RCC_CFGR_SW) | RCC_CFGR_SW_HSI;
    budget = 1000000U;
    while ((RCC->CFGR & RCC_CFGR_SWS) != RCC_CFGR_SWS_HSI)
        if (--budget == 0U) return false;
    RCC->CFGR &= ~(RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2);
    SystemCoreClockUpdate();
    return SystemCoreClock == 16000000U &&
        !(RCC->CFGR & (RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2));
}

static void hardware_init(void)
{
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN | RCC_AHB1ENR_GPIODEN;
    (void)RCC->AHB1ENR;
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN | RCC_APB1ENR_TIM2EN;
    (void)RCC->APB1ENR;
    RCC->APB2ENR |= RCC_APB2ENR_SYSCFGEN;
    (void)RCC->APB2ENR;

    GPIOD->BSRR = LED_ALL << 16;
    GPIOD->OTYPER &= ~LED_ALL;
    GPIOD->OSPEEDR &= ~0xFF000000U;
    GPIOD->PUPDR &= ~0xFF000000U;
    GPIOD->MODER = (GPIOD->MODER & ~0xFF000000U) | 0x55000000U;
    GPIOA->MODER = (GPIOA->MODER & ~((3U << 4) | (3U << 6) | 3U)) | (2U << 4) | (2U << 6);
    GPIOA->OTYPER &= ~((1U << 2) | (1U << 3));
    GPIOA->OSPEEDR = (GPIOA->OSPEEDR & ~((3U << 4) | (3U << 6))) | (1U << 4) | (1U << 6);
    GPIOA->PUPDR &= ~((3U << 4) | (3U << 6) | 3U);
    GPIOA->AFR[0] = (GPIOA->AFR[0] & ~((15U << 8) | (15U << 12))) | (7U << 8) | (7U << 12);

    NVIC_DisableIRQ(TIM2_IRQn); NVIC_DisableIRQ(USART2_IRQn); NVIC_DisableIRQ(EXTI0_IRQn);
    RCC->APB1RSTR |= RCC_APB1RSTR_TIM2RST | RCC_APB1RSTR_USART2RST;
    RCC->APB1RSTR &= ~(RCC_APB1RSTR_TIM2RST | RCC_APB1RSTR_USART2RST);
    TIM2->CR1 = 0U; TIM2->DIER = 0U;
    TIM2->PSC = 15U; TIM2->ARR = 999U; TIM2->CNT = 0U;
    TIM2->EGR = TIM_EGR_UG;
    TIM2->SR = 0U; /* Clear update from UG before enabling interrupt. */

    USART2->CR1 = 0U; USART2->CR2 = 0U; USART2->CR3 = 0U;
    USART2->BRR = 139U; /* round(16 MHz / 115200), OVER8=0. */
    (void)USART2->SR; (void)USART2->DR;

    EXTI->IMR &= ~1U; EXTI->EMR &= ~1U;
    SYSCFG->EXTICR[0] &= ~15U; /* Manual EXTICR1 / catalog EXTICR0: route PA0. */
    EXTI->RTSR |= 1U; EXTI->FTSR |= 1U;
    EXTI->PR = 1U;
    NVIC_ClearPendingIRQ(TIM2_IRQn); NVIC_ClearPendingIRQ(USART2_IRQn); NVIC_ClearPendingIRQ(EXTI0_IRQn);
    NVIC_SetPriority(TIM2_IRQn, 4U); NVIC_SetPriority(USART2_IRQn, 5U); NVIC_SetPriority(EXTI0_IRQn, 6U);

    /* All static handler state is initialized by startup before these enables. */
    TIM2->DIER = TIM_DIER_UIE;
    USART2->CR1 = USART_CR1_UE | USART_CR1_TE | USART_CR1_RE | USART_CR1_RXNEIE;
    EXTI->IMR |= 1U;
    NVIC_EnableIRQ(TIM2_IRQn); NVIC_EnableIRQ(USART2_IRQn); NVIC_EnableIRQ(EXTI0_IRQn);
    TIM2->CR1 = TIM_CR1_CEN;
}

static void clear_io(void)
{
    const uint32_t saved = lock();
    USART2->CR1 &= ~USART_CR1_TXEIE;
    rx.head = rx.tail = tx.head = tx.tail = 0U;
    uart_errors = queue_overflows = 0U; io_failure = false;
    (void)USART2->SR; (void)USART2->DR;
    unlock(saved);
}

static void send_frame(const uint8_t frame[FRAME_SIZE])
{
    const uint32_t saved = lock();
    const unsigned available = queue_available(&tx);
    if (available < FRAME_SIZE) { ++queue_overflows; io_failure = true; }
    else {
        for (unsigned i = 0; i < FRAME_SIZE; ++i) {
            (void)queue_push(&tx, frame[i]);
        }
        __DMB(); USART2->CR1 |= USART_CR1_TXEIE;
    }
    unlock(saved);
}

int main(void)
{
    __disable_irq(); SysTick->CTRL = 0U;
    if (!clock_init()) for (;;) { __NOP(); } /* Stop; no unreliable time base. */
    Controller c; Button b;
    controller_init(&c);
    hardware_init();
    button_init(&b, (GPIOA->IDR & 1U) != 0U, milliseconds, button_generation);
    __enable_irq();
    bool green = false;
    uint32_t last_green = milliseconds;
    for (;;) {
        uint8_t data[QUEUE_SIZE]; unsigned count = 0U;
        const uint32_t saved = lock();
        const uint32_t now = milliseconds, generation = button_generation;
        const bool raw = (GPIOA->IDR & 1U) != 0U, fault = io_failure;
        while (count < QUEUE_SIZE && queue_pop(&rx, &data[count])) ++count;
        unlock(saved);
        if (fault && (c.state == RUNNING || c.state == PAUSING)) controller_fail(&c);
        for (unsigned i = 0; i < count; ++i) controller_receive(&c, data[i], now);
        if (button_step(&b, raw, now, generation) && controller_press(&c, now)) clear_io();
        uint8_t outgoing[FRAME_SIZE];
        if (controller_tick(&c, now, outgoing)) send_frame(outgoing);
        if (c.state == FAILED) {
            const uint32_t stop = lock(); USART2->CR1 &= ~USART_CR1_TXEIE;
            tx.head = tx.tail; unlock(stop);
        }
        if ((uint32_t)(now - last_green) >= 500U) { last_green = now; green = !green; }
        const uint32_t on = (green ? LED_GREEN : 0U) | (c.orange ? LED_ORANGE : 0U) |
            (c.blue ? LED_BLUE : 0U) | (c.state == FAILED ? LED_RED : 0U);
        GPIOD->BSRR = on | ((LED_ALL & ~on) << 16);
        /* TIM2 wakes main at least each ms; a pre-WFI arrival can delay <=1 tick. */
        __WFI();
    }
}
