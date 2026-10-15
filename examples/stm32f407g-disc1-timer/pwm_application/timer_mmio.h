#ifndef PRAXIS_F407_TIMER_MMIO_H
#define PRAXIS_F407_TIMER_MMIO_H
#include <stddef.h>
#include "timer_controller.h"
_Static_assert(offsetof(TIM_TypeDef, CCMR1)==0x18U, "CCMR1 offset");
_Static_assert(offsetof(TIM_TypeDef, CCER)==0x20U, "CCER offset");
_Static_assert(offsetof(TIM_TypeDef, CCR1)==0x34U, "CCR1 offset");
_Static_assert(sizeof(((TIM_TypeDef *)0)->CCR1)==4U, "CCR1 word storage");

static uint32_t timer_mmio_read(void *unused, enum timer_register reg)
{
    (void)unused;
    switch (reg) {
    case T_CLOCK: return SystemCoreClock;
    case T_RCC_CR: return RCC->CR;
    case T_CFGR: return RCC->CFGR;
    case T_GATE: return RCC->APB1ENR;
    case T_RESET: return RCC->APB1RSTR;
    case T_APB2: return RCC->APB2ENR;
    case T_PRIMASK: return __get_PRIMASK();
    case T_IPSR: return __get_IPSR();
    case T_CR1: return TIM2->CR1;
    case T_CR2: return TIM2->CR2;
    case T_SMCR: return TIM2->SMCR;
    case T_DIER: return TIM2->DIER;
    case T_SR: return TIM2->SR;
    case T_CCMR1: return TIM2->CCMR1;
    case T_CCER: return TIM2->CCER;
    case T_CNT: return TIM2->CNT;
    case T_PSC: return TIM2->PSC;
    case T_ARR: return TIM2->ARR;
    case T_CCR1: return TIM2->CCR1;
    default: return UINT32_MAX; /* EGR is action-only, never read. */
    }
}
static void timer_mmio_write(void *unused, enum timer_register reg, uint32_t value)
{
    (void)unused;
    switch (reg) {
    case T_GATE: RCC->APB1ENR=value; break;
    case T_RESET: RCC->APB1RSTR=value; break;
    case T_CR1: TIM2->CR1=value; break;
    case T_CR2: TIM2->CR2=value; break;
    case T_SMCR: TIM2->SMCR=value; break;
    case T_DIER: TIM2->DIER=value; break;
    case T_SR: TIM2->SR=value; break;
    case T_EGR: TIM2->EGR=value; break;
    case T_CCMR1: TIM2->CCMR1=value; break;
    case T_CCER: TIM2->CCER=value; break;
    case T_CNT: TIM2->CNT=value; break;
    case T_PSC: TIM2->PSC=value; break;
    case T_ARR: TIM2->ARR=value; break;
    case T_CCR1: TIM2->CCR1=value; break;
    default: break;
    }
}
static void timer_mmio_barrier(void *unused) { (void)unused; __DSB(); }
#endif
