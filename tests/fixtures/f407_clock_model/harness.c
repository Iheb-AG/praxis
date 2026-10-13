#include <assert.h>
#include <setjmp.h>
#include <stdlib.h>
#include <stm32f407xx.h>

RCC_TypeDef model_rcc;
GPIO_TypeDef model_gpioa, model_gpiod;
uint32_t SystemCoreClock = 168000000U;
static uint32_t update_calls, systick_calls, systick_ticks, systick_error;
static bool irq_enabled = true;
static jmp_buf fail_stop;

void SystemCoreClockUpdate(void)
{
    const uint32_t shift[16] = {0,0,0,0,0,0,0,0,1,2,3,4,6,7,8,9};
    update_calls++;
    SystemCoreClock = 16000000U >> shift[(model_rcc.CFGR >> 4) & 15U];
}
uint32_t SysTick_Config(uint32_t ticks)
{
    systick_calls++;
    systick_ticks = ticks;
    return systick_error;
}
void model_nop(void) { longjmp(fail_stop, 1); }
void model_irq(bool enabled) { irq_enabled = enabled; }

#define main firmware_main
#include APP_SOURCE
#undef main

int main(int argc, char **argv)
{
    assert(argc == 2);
    int scenario = atoi(argv[1]);
    model_rcc.CR = RCC_CR_HSIRDY;
    model_rcc.CFGR = (8U << 4); /* HSI selected but AHB /2: non-reset state. */
    if (scenario == 0) {
        system_clock_hsi_init();
        assert((model_rcc.CFGR & RCC_CFGR_HPRE) == 0U);
        assert(SystemCoreClock == 16000000U);
        assert(update_calls == 1U);
#ifndef ORIGINAL_APP
        assert(systick_init_1ms());
        assert(systick_calls == 1U && systick_ticks == 16000U);
    } else if (scenario >= 1 && scenario <= 3) {
        if (scenario == 1) model_rcc.CR = 0; /* HSI readiness never arrives. */
        if (scenario == 2) model_rcc.CFGR |= (2U << 2); /* Switch never completes. */
        if (scenario == 3) model_rcc.CR |= RCC_CR_PLLRDY; /* PLL never reports stopped. */
        if (setjmp(fail_stop) == 0) {
            firmware_main();
            assert(0 && "Clock failure must stop initialization");
        }
        assert(!irq_enabled);
        assert(systick_calls == 0U && update_calls == 0U);
        assert(model_rcc.AHB1ENR == 0U && model_gpiod.MODER == 0U);
    } else if (scenario == 4) {
        SystemCoreClock = 16000001U;
        assert(!systick_init_1ms() && systick_calls == 0U);
    } else if (scenario == 5) {
        SystemCoreClock = 16000000U;
        systick_error = 1U;
        assert(!systick_init_1ms() && systick_calls == 1U);
    } else if (scenario == 6) {
        model_gpiod.MODER = 0xA0000001U;
        model_gpioa.MODER = 0xA8000003U;
        gpio_led_button_init();
        assert(model_gpiod.BSRR == ((1U << 28) | (1U << 29)));
        assert(model_gpiod.MODER == 0xA5000001U);
        assert(model_gpioa.MODER == 0xA8000000U);
#endif
    } else {
        assert(0 && "Unknown test scenario");
    }
    return 0;
}
