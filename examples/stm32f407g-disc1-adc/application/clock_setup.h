/* Reused clock-v1 callback; unchanged register operations. */
#ifndef PRAXIS_ADC_CLOCK_SETUP_H
#define PRAXIS_ADC_CLOCK_SETUP_H
/* Compile-only owned-startup clock example. Not flashed or physically qualified.
 * Facts: actual Praxis ingestion and knowledge MCP, clock-v1 bundle.
 * RM0090 Rev22 pp80-82,98,141-144,218-221,225-231,247.
 * Startup/linker assets come from the separate matching build MCP.
 */
#include <stdint.h>
#include <stddef.h>
#include <stm32f407xx.h>
#include "clock_sequence.h"

extern uint32_t SystemCoreClock;
_Static_assert(offsetof(FLASH_TypeDef, ACR) == 0U, "reviewed ACR offset");
_Static_assert(offsetof(PWR_TypeDef, CSR) == 4U, "reviewed CSR offset");
_Static_assert(FLASH_ACR_LATENCY == 7U, "F407 latency is three bits");
_Static_assert(PWR_CR_VOS == (1UL << 14), "F407 single-bit voltage scale");
_Static_assert(PWR_CSR_VOSRDY == (1UL << 14), "reviewed voltage-scale status");
_Static_assert(RCC_APB1ENR_PWREN == (1UL << 28), "reviewed PWR gate");

#define CLOCK_BUDGET 1000000UL /* Iteration bound, not a measured time interval. */
#define BUS_MASK (RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2)
#define BUS_DIVIDERS ((5UL << RCC_CFGR_PPRE1_Pos) | (4UL << RCC_CFGR_PPRE2_Pos))
#define PLL_MASK (RCC_PLLCFGR_PLLM | RCC_PLLCFGR_PLLN | RCC_PLLCFGR_PLLP | \
                  RCC_PLLCFGR_PLLQ | RCC_PLLCFGR_PLLSRC)
#define PLL_RECIPE (8UL | (336UL << RCC_PLLCFGR_PLLN_Pos) | \
                    RCC_PLLCFGR_PLLSRC | (7UL << RCC_PLLCFGR_PLLQ_Pos))

/* Not the UART telemetry ABI; the existing UART observation tool cannot read this. */


static inline enum clock_action clock_apply(enum clock_step step, void *unused)
{
    (void)unused;
    switch (step) {
    case CLOCK_PRECONDITIONS:
        /* Caller owns reset/startup and has masked interrupts/quiesced all clients.
         * Reject other clock owners and unreviewed prefetch state, rather than
         * treating this example as a general live clock reconfiguration service.
         */
        return ((RCC->CR & (RCC_CR_PLLI2SON | RCC_CR_CSSON)) == 0U &&
                (FLASH->ACR & (FLASH_ACR_PRFTEN | FLASH_ACR_ICRST | FLASH_ACR_DCRST)) == 0U)
               ? CLOCK_DONE : CLOCK_REJECT;
    case CLOCK_HSI_ENABLE: RCC->CR |= RCC_CR_HSION; return CLOCK_DONE;
    case CLOCK_HSI_READY: return (RCC->CR & RCC_CR_HSIRDY) ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_HSI_SELECT: RCC->CFGR &= ~RCC_CFGR_SW; return CLOCK_DONE;
    case CLOCK_HSI_SELECTED:
        return (RCC->CFGR & RCC_CFGR_SWS) == 0U ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_SAFE_DIVIDERS:
        RCC->CFGR = (RCC->CFGR & ~BUS_MASK) | BUS_DIVIDERS;
        return (RCC->CFGR & BUS_MASK) == BUS_DIVIDERS ? CLOCK_DONE : CLOCK_REJECT;
    case CLOCK_PLL_DISABLE: RCC->CR &= ~RCC_CR_PLLON; return CLOCK_DONE;
    case CLOCK_PLL_DISABLED: return (RCC->CR & RCC_CR_PLLRDY) ? CLOCK_PENDING : CLOCK_DONE;
    case CLOCK_HSE_DISABLE: RCC->CR &= ~RCC_CR_HSEON; return CLOCK_DONE;
    case CLOCK_HSE_DISABLED: return (RCC->CR & RCC_CR_HSERDY) ? CLOCK_PENDING : CLOCK_DONE;
    case CLOCK_PWR_GATE:
        RCC->APB1ENR |= RCC_APB1ENR_PWREN;
        return (RCC->APB1ENR & RCC_APB1ENR_PWREN) ? CLOCK_DONE : CLOCK_REJECT;
    case CLOCK_PWR_SCALE:
        PWR->CR = (PWR->CR & ~(PWR_CR_CWUF | PWR_CR_CSBF)) | PWR_CR_VOS;
        return CLOCK_DONE;
    case CLOCK_PWR_READY: return (PWR->CSR & PWR_CSR_VOSRDY) ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_FLASH_LATENCY:
        FLASH->ACR = (FLASH->ACR & ~(FLASH_ACR_LATENCY | FLASH_ACR_ICRST | FLASH_ACR_DCRST)) |
                     FLASH_ACR_LATENCY_5WS;
        return CLOCK_DONE;
    case CLOCK_FLASH_ACK:
        return (FLASH->ACR & FLASH_ACR_LATENCY) == FLASH_ACR_LATENCY_5WS ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_HSE_CRYSTAL: RCC->CR &= ~RCC_CR_HSEBYP; return CLOCK_DONE;
    case CLOCK_HSE_ENABLE: RCC->CR |= RCC_CR_HSEON; return CLOCK_DONE;
    case CLOCK_HSE_READY: return (RCC->CR & RCC_CR_HSERDY) ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_PLL_CONFIGURE:
        RCC->PLLCFGR = (RCC->PLLCFGR & ~PLL_MASK) | PLL_RECIPE;
        return CLOCK_DONE;
    case CLOCK_PLL_ENABLE: RCC->CR |= RCC_CR_PLLON; return CLOCK_DONE;
    case CLOCK_PLL_READY: return (RCC->CR & RCC_CR_PLLRDY) ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_PLL_SELECT:
        RCC->CFGR = (RCC->CFGR & ~RCC_CFGR_SW) | RCC_CFGR_SW_PLL;
        return CLOCK_DONE;
    case CLOCK_PLL_SELECTED:
        return (RCC->CFGR & (RCC_CFGR_SWS | BUS_MASK)) == (RCC_CFGR_SWS_PLL | BUS_DIVIDERS)
               ? CLOCK_DONE : CLOCK_PENDING;
    case CLOCK_PUBLISH_FREQUENCY: SystemCoreClock = 168000000UL; return CLOCK_DONE;
    default: return CLOCK_REJECT;
    }
}


#endif
