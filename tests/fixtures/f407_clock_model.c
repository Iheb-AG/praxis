/* Instrument the SAME register-writing callback as the target example.
 * This is a RAM register model, not an STM32 simulator or timing measurement.
 */
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <stm32f407xx.h>
static RCC_TypeDef model_rcc;
static PWR_TypeDef model_pwr;
static FLASH_TypeDef model_flash;
#undef RCC
#undef PWR
#undef FLASH
#define RCC (&model_rcc)
#define PWR (&model_pwr)
#define FLASH (&model_flash)
#define PRAXIS_CLOCK_MODEL 1
#include "main.c"
uint32_t SystemCoreClock = 16000000UL;

struct model { int fault, order_ok; uint32_t seen, calls; };
#define SEEN(ctx, step) (((ctx)->seen & (1UL << (step))) != 0U)
static enum clock_action instrument(enum clock_step step, void *context)
{
    struct model *ctx = context;
    ++ctx->calls;
    int allowed = 1;
    switch (step) {
    case CLOCK_PLL_DISABLE: allowed = SEEN(ctx, CLOCK_HSI_SELECTED); break;
    case CLOCK_PWR_SCALE: allowed = SEEN(ctx, CLOCK_PWR_GATE); break;
    case CLOCK_HSE_CRYSTAL: allowed = SEEN(ctx, CLOCK_HSE_DISABLED); break;
    case CLOCK_PLL_CONFIGURE:
        allowed = SEEN(ctx, CLOCK_PLL_DISABLED) && SEEN(ctx, CLOCK_HSE_READY) &&
                  SEEN(ctx, CLOCK_PWR_READY) && SEEN(ctx, CLOCK_FLASH_ACK) &&
                  (RCC->CR & (RCC_CR_PLLON | RCC_CR_PLLI2SON)) == 0U;
        break;
    case CLOCK_PLL_SELECT:
        allowed = SEEN(ctx, CLOCK_PLL_READY) && SEEN(ctx, CLOCK_FLASH_ACK) &&
                  SEEN(ctx, CLOCK_PWR_READY) && (RCC->CFGR & BUS_MASK) == BUS_DIVIDERS;
        break;
    case CLOCK_PUBLISH_FREQUENCY: allowed = SEEN(ctx, CLOCK_PLL_SELECTED); break;
    default: break;
    }
    if (!allowed) { ctx->order_ok = 0; return CLOCK_REJECT; }
    int fail = ctx->fault == (int)step;
    switch (step) {
    case CLOCK_HSI_READY:
        RCC->CR = fail ? RCC->CR & ~RCC_CR_HSIRDY : RCC->CR | RCC_CR_HSIRDY; break;
    case CLOCK_HSI_SELECTED:
        RCC->CFGR = (RCC->CFGR & ~RCC_CFGR_SWS) | (fail ? RCC_CFGR_SWS_PLL : 0U); break;
    case CLOCK_PLL_DISABLED:
        RCC->CR = fail ? RCC->CR | RCC_CR_PLLRDY : RCC->CR & ~RCC_CR_PLLRDY; break;
    case CLOCK_HSE_DISABLED:
        RCC->CR = fail ? RCC->CR | RCC_CR_HSERDY : RCC->CR & ~RCC_CR_HSERDY; break;
    case CLOCK_PWR_READY:
        PWR->CSR = fail ? PWR->CSR & ~PWR_CSR_VOSRDY : PWR->CSR | PWR_CSR_VOSRDY; break;
    case CLOCK_FLASH_ACK:
        if (fail) FLASH->ACR &= ~FLASH_ACR_LATENCY;
        break;
    case CLOCK_HSE_READY:
        RCC->CR = fail ? RCC->CR & ~RCC_CR_HSERDY : RCC->CR | RCC_CR_HSERDY; break;
    case CLOCK_PLL_READY:
        RCC->CR = fail ? RCC->CR & ~RCC_CR_PLLRDY : RCC->CR | RCC_CR_PLLRDY; break;
    case CLOCK_PLL_SELECTED:
        RCC->CFGR = (RCC->CFGR & ~RCC_CFGR_SWS) | (fail ? 0U : RCC_CFGR_SWS_PLL); break;
    default:
        if (fail) return CLOCK_REJECT;
        break;
    }
    enum clock_action action = clock_apply(step, 0);
    if (action == CLOCK_DONE) ctx->seen |= 1UL << step;
    return action;
}

int main(int argc, char **argv)
{
    int fault = argc > 1 ? atoi(argv[1]) : -1;
    uint32_t budget = argc > 2 ? (uint32_t)atoi(argv[2]) : 3U;
    struct model context = {fault, 1, 0U, 0U};
    RCC->CR = RCC_CR_HSION | (0x5AUL << RCC_CR_HSICAL_Pos);
    RCC->APB1ENR = RCC_APB1ENR_TIM2EN; /* Preserve an unrelated interface gate. */
    FLASH->ACR = FLASH_ACR_ICEN | FLASH_ACR_DCEN;
    PWR->CR = PWR_CR_DBP | PWR_CR_CWUF | PWR_CR_CSBF;
    struct clock_result result;
    if (fault == -2) {
        result = (struct clock_result){0U, CLOCK_PLL_SELECT, 1U};
        (void)instrument(CLOCK_PLL_SELECT, &context);
    } else {
        result = clock_sequence(instrument, &context, budget);
    }
    uint32_t m = RCC->PLLCFGR & RCC_PLLCFGR_PLLM;
    uint32_t n = (RCC->PLLCFGR & RCC_PLLCFGR_PLLN) >> RCC_PLLCFGR_PLLN_Pos;
    uint32_t p = (((RCC->PLLCFGR & RCC_PLLCFGR_PLLP) >> RCC_PLLCFGR_PLLP_Pos) + 1U) * 2U;
    uint32_t q = (RCC->PLLCFGR & RCC_PLLCFGR_PLLQ) >> RCC_PLLCFGR_PLLQ_Pos;
    uint32_t vco = m ? (8000000UL / m) * n : 0U;
    printf("{\"completed\":%u,\"failed_step\":%u,\"attempts\":%u,\"calls\":%u,"
           "\"order_ok\":%d,\"system_core_clock\":%u,\"sysclk\":%u,\"pll48\":%u,"
           "\"latency\":%u,\"scale1\":%u,\"commands_clear\":%u,\"preserved\":%u}\n",
           result.completed, result.failed_step, result.attempts, context.calls, context.order_ok,
           SystemCoreClock, vco / p, q ? vco / q : 0U, (uint32_t)(FLASH->ACR & FLASH_ACR_LATENCY),
           !!(PWR->CR & PWR_CR_VOS), !(PWR->CR & (PWR_CR_CWUF | PWR_CR_CSBF)),
           (RCC->APB1ENR & RCC_APB1ENR_TIM2EN) &&
           (RCC->CR & RCC_CR_HSICAL) == (0x5AUL << RCC_CR_HSICAL_Pos) &&
           (PWR->CR & PWR_CR_DBP) &&
           (FLASH->ACR & (FLASH_ACR_ICEN | FLASH_ACR_DCEN)) == (FLASH_ACR_ICEN | FLASH_ACR_DCEN));
    return 0;
}
