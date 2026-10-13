#include "led_button.h"

static volatile uint32_t g_tick_ms = 0U;

void SysTick_Handler(void)
{
    g_tick_ms++;
}

uint32_t millis(void)
{
    return g_tick_ms;
}

void system_clock_hsi_init(void)
{
    RCC_TypeDef *rcc = RCC;

    rcc->CR |= RCC_CR_HSION;
    uint32_t timeout = 100000U;
    while ((rcc->CR & RCC_CR_HSIRDY) == 0U) {
        if (--timeout == 0U) {
            return;
        }
    }

    rcc->CFGR &= ~RCC_CFGR_SW;
    timeout = 100000U;
    while ((rcc->CFGR & RCC_CFGR_SWS) != 0U) {
        if (--timeout == 0U) {
            return;
        }
    }

    rcc->CR &= ~RCC_CR_PLLON;
    timeout = 100000U;
    while ((rcc->CR & RCC_CR_PLLRDY) != 0U) {
        if (--timeout == 0U) {
            return;
        }
    }

    SystemCoreClock = 16000000U;
}

void systick_init_1ms(void)
{
    if (SystemCoreClock % 1000U != 0U) {
        return;
    }
    uint32_t reload = SystemCoreClock / 1000U;
    SysTick_Config(reload);
}

void gpio_led_button_init(void)
{
    RCC_TypeDef *rcc = RCC;
    GPIO_TypeDef *gpioa = GPIOA;
    GPIO_TypeDef *gpiod = GPIOD;

    rcc->AHB1ENR |= RCC_AHB1ENR_GPIOAEN;
    rcc->AHB1ENR |= RCC_AHB1ENR_GPIODEN;
    (void)rcc->AHB1ENR;

    gpiod->BSRR = (1U << (12 + 16)) | (1U << (13 + 16));

    gpiod->MODER &= ~(GPIO_MODER_MODER12 | GPIO_MODER_MODER13);
    gpiod->MODER |= (1U << GPIO_MODER_MODER12_Pos) | (1U << GPIO_MODER_MODER13_Pos);

    gpiod->OTYPER &= ~(GPIO_OTYPER_OT12 | GPIO_OTYPER_OT13);

    gpiod->OSPEEDR &= ~(GPIO_OSPEEDR_OSPEED12 | GPIO_OSPEEDR_OSPEED13);
    gpiod->OSPEEDR |= (1U << GPIO_OSPEEDR_OSPEED12_Pos) | (1U << GPIO_OSPEEDR_OSPEED13_Pos);

    gpiod->PUPDR &= ~(GPIO_PUPDR_PUPD12 | GPIO_PUPDR_PUPD13);

    gpioa->MODER &= ~GPIO_MODER_MODER0;
    gpioa->PUPDR &= ~GPIO_PUPDR_PUPD0;
}

void led_a_set(uint32_t state)
{
    GPIO_TypeDef *gpiod = GPIOD;
    if (state) {
        gpiod->BSRR = (1U << 12);
    } else {
        gpiod->BSRR = (1U << (12 + 16));
    }
}

void led_a_toggle(void)
{
    GPIO_TypeDef *gpiod = GPIOD;
    uint32_t odr = gpiod->ODR;
    if (odr & (1U << 12)) {
        gpiod->BSRR = (1U << (12 + 16));
    } else {
        gpiod->BSRR = (1U << 12);
    }
}

void led_b_set(uint32_t state)
{
    GPIO_TypeDef *gpiod = GPIOD;
    if (state) {
        gpiod->BSRR = (1U << 13);
    } else {
        gpiod->BSRR = (1U << (13 + 16));
    }
}

uint32_t button_read(void)
{
    GPIO_TypeDef *gpioa = GPIOA;
    return (gpioa->IDR & (1U << 0)) != 0U;
}

int main(void)
{
    system_clock_hsi_init();
    systick_init_1ms();
    gpio_led_button_init();

    uint32_t last_toggle = 0U;
    uint32_t button_state = 0U;
    uint32_t button_stable = 0U;
    uint32_t button_debounce_start = 0U;

    while (1) {
        uint32_t now = millis();

        if ((now - last_toggle) >= 500U) {
            led_a_toggle();
            last_toggle = now;
        }

        uint32_t btn_raw = button_read();

        if (btn_raw == button_state) {
            if ((now - button_debounce_start) >= 50U) {
                button_stable = button_state;
            }
        } else {
            button_state = btn_raw;
            button_debounce_start = now;
        }

        if (button_stable) {
            led_b_set(1U);
        } else {
            led_b_set(0U);
        }
    }
}