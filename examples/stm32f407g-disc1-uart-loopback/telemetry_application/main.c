/* Hardware facts: actual Praxis knowledge MCP responses, bundle revision
 * 1e7e9f44e7e8a4a9c2f1730ae725a2fed50cd80271b75adf63cdaa495899900b.
 * Reviewed subset: RCC/GPIO/USART2/TIM2/SYSCFG/EXTI0/NVIC.
 * MB997-E-01 reference; physical PCB revision is not confirmed.
 */
#include <stm32f407xx.h>
#include <stddef.h>
#include "controller.h"
#include "queue.h"
#include "telemetry.h"

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
volatile PraxisTelemetry praxis_telemetry;
static volatile uint32_t timer_irq_total, uart_irq_total, exti_irq_total;
static volatile uint32_t rx_total, tx_total, uart_error_total, overflow_total;

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
        ++timer_irq_total;
    }
}

void EXTI0_IRQHandler(void)
{
    if (EXTI->PR & 1U) {
        EXTI->PR = 1U; /* W1C; do not read-modify-write PR. */
        ++button_generation;
        ++exti_irq_total;
    }
}

void USART2_IRQHandler(void)
{
    ++uart_irq_total;
    const uint32_t sr = USART2->SR;
    const uint32_t errors = sr & (USART_SR_ORE | USART_SR_FE | USART_SR_NE);
    if ((sr & USART_SR_RXNE) || errors) {
        const uint8_t byte = (uint8_t)USART2->DR; /* SR then DR clears sampled errors. */
        ++rx_total;
        if (errors) { ++uart_errors; ++uart_error_total; io_failure = true; }
        else {
            if (!queue_push(&rx, byte)) { ++queue_overflows; ++overflow_total; io_failure = true; }
        }
    }
    if ((sr & USART_SR_TXE) && (USART2->CR1 & USART_CR1_TXEIE)) {
        uint8_t byte;
        if (queue_pop(&tx, &byte)) { USART2->DR = byte; ++tx_total; }
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
    if (available < FRAME_SIZE) { ++queue_overflows; ++overflow_total; io_failure = true; }
    else {
        for (unsigned i = 0; i < FRAME_SIZE; ++i) {
            (void)queue_push(&tx, frame[i]);
        }
        __DMB(); USART2->CR1 |= USART_CR1_TXEIE;
    }
    unlock(saved);
}

static void publish(const Controller *c, bool green, uint32_t run_number,
                    uint32_t started, uint32_t validated, uint32_t last_good,
                    uint32_t presses, uint32_t iterations)
{
    /* A short critical section snapshots ISR-owned software counters. It never
       waits for a debugger/reader. Main is the sole record writer. */
    const uint32_t saved = lock();
    ++praxis_telemetry.generation; __DMB();
    praxis_telemetry.magic = 0x50525831U;
    praxis_telemetry.abi = 1U;
    praxis_telemetry.size_bytes = sizeof(PraxisTelemetry);
    praxis_telemetry.uptime_ms = milliseconds;
    praxis_telemetry.timer_irqs = timer_irq_total;
    praxis_telemetry.uart_irqs = uart_irq_total;
    praxis_telemetry.exti_irqs = exti_irq_total;
    praxis_telemetry.run_number = run_number;
    praxis_telemetry.state = (uint32_t)c->state;
    praxis_telemetry.frames_started = started;
    praxis_telemetry.frames_validated = validated;
    praxis_telemetry.run_validated = c->validated;
    praxis_telemetry.rx_bytes = rx_total;
    praxis_telemetry.tx_bytes = tx_total;
    praxis_telemetry.uart_errors = uart_error_total;
    praxis_telemetry.queue_overflows = overflow_total;
    praxis_telemetry.failure_reason = (uint32_t)c->failure_reason;
    praxis_telemetry.flags = (c->blue ? 1U : 0U) | (c->orange ? 2U : 0U) |
        (c->in_flight ? 4U : 0U) | (green ? 8U : 0U);
    praxis_telemetry.last_good_ms = last_good;
    praxis_telemetry.next_sequence = c->sequence;
    praxis_telemetry.button_presses = presses;
    praxis_telemetry.main_iterations = iterations;
    __DMB(); ++praxis_telemetry.generation;
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
    uint32_t run_number = 0U, started = 0U, validated = 0U, last_good = 0U;
    uint32_t presses = 0U, iterations = 0U, published_at = milliseconds;
    publish(&c, green, run_number, started, validated, last_good, presses, iterations);
    for (;;) {
        uint8_t data[QUEUE_SIZE]; unsigned count = 0U;
        const uint32_t saved = lock();
        const uint32_t now = milliseconds, generation = button_generation;
        const bool raw = (GPIOA->IDR & 1U) != 0U, fault = io_failure;
        const FailureReason io_reason = queue_overflows ? FAIL_QUEUE : FAIL_UART;
        while (count < QUEUE_SIZE && queue_pop(&rx, &data[count])) ++count;
        unlock(saved);
        ++iterations;
        if (fault && (c.state == RUNNING || c.state == PAUSING)) controller_fail(&c, io_reason);
        const uint32_t before = c.validated;
        for (unsigned i = 0; i < count; ++i) controller_receive(&c, data[i], now);
        if (c.validated != before) { ++validated; last_good = now; }
        if (button_step(&b, raw, now, generation)) {
            ++presses;
            if (controller_press(&c, now)) { ++run_number; clear_io(); }
        }
        uint8_t outgoing[FRAME_SIZE];
        if (controller_tick(&c, now, outgoing)) { ++started; send_frame(outgoing); }
        if (c.state == FAILED) {
            const uint32_t stop = lock(); USART2->CR1 &= ~USART_CR1_TXEIE;
            tx.head = tx.tail; unlock(stop);
        }
        if ((uint32_t)(now - last_green) >= 500U) { last_green = now; green = !green; }
        const uint32_t on = (green ? LED_GREEN : 0U) | (c.orange ? LED_ORANGE : 0U) |
            (c.blue ? LED_BLUE : 0U) | (c.state == FAILED ? LED_RED : 0U);
        GPIOD->BSRR = on | ((LED_ALL & ~on) << 16);
        /* Publish every 250 nominal ms so bounded SWD reads usually find a quiet
           interval. A reader may still return TELEMETRY_BUSY; it never halts. */
        if ((uint32_t)(now - published_at) >= 250U) {
            published_at = now;
            publish(&c, green, run_number, started, validated, last_good, presses, iterations);
        }
        /* TIM2 wakes main at least each ms; a pre-WFI arrival can delay <=1 tick. */
        __WFI();
    }
}
