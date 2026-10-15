/* Requires a verified passive PA1/P1-11 -> PA2/P1-14 jumper, no other
 * attachments or USART2/ADC owners on those pins. Compile/model tested only.
 */
#include <stddef.h>
#include "routed_timer.h"
_Static_assert(offsetof(TIM_TypeDef,CCR2)==0x38U,"PWM CCR2 offset");
_Static_assert(offsetof(TIM_TypeDef,CCR3)==0x3CU,"capture CCR3 offset");
_Static_assert(offsetof(GPIO_TypeDef,AFR)==0x20U,"AFRL offset");
volatile enum route_status praxis_route_status;
volatile uint32_t praxis_route_frames,praxis_route_last_delta,praxis_route_completed;
static uint32_t read_route(void *unused,enum route_register reg)
{
    (void)unused;
    switch(reg) {
    case R_CLOCK:return SystemCoreClock;
    case R_RCC_CR:return RCC->CR;
    case R_CFGR:return RCC->CFGR;
    case R_AHB1:return RCC->AHB1ENR;
    case R_APB1:return RCC->APB1ENR;
    case R_RESET:return RCC->APB1RSTR;
    case R_APB2:return RCC->APB2ENR;
    case R_PRIMASK:return __get_PRIMASK();
    case R_IPSR:return __get_IPSR();
    case R_MODER:return GPIOA->MODER;
    case R_OTYPER:return GPIOA->OTYPER;
    case R_SPEED:return GPIOA->OSPEEDR;
    case R_PULL:return GPIOA->PUPDR;
    case R_AFRL:return GPIOA->AFR[0];
    case R_LOCK:return GPIOA->LCKR;
    case R_CR1:return TIM2->CR1;
    case R_CR2:return TIM2->CR2;
    case R_SMCR:return TIM2->SMCR;
    case R_DIER:return TIM2->DIER;
    case R_SR:return TIM2->SR;
    case R_CCMR1:return TIM2->CCMR1;
    case R_CCER:return TIM2->CCER;
    case R_CNT:return TIM2->CNT;
    case R_PSC:return TIM2->PSC;
    case R_ARR:return TIM2->ARR;
    case R_CCR2:return TIM2->CCR2;
    case C_CR1:return TIM5->CR1;
    case C_CR2:return TIM5->CR2;
    case C_SMCR:return TIM5->SMCR;
    case C_DIER:return TIM5->DIER;
    case C_SR:return TIM5->SR;
    case C_CCMR2:return TIM5->CCMR2;
    case C_CCER:return TIM5->CCER;
    case C_CNT:return TIM5->CNT;
    case C_PSC:return TIM5->PSC;
    case C_ARR:return TIM5->ARR;
    case C_CCR3:return TIM5->CCR3;
    default:return UINT32_MAX; /* No EGR or BSRR reads. */
    }
}
static void write_route(void *unused,enum route_register reg,uint32_t value)
{
    (void)unused;
    switch(reg) {
    case R_AHB1:RCC->AHB1ENR=value;break;
    case R_APB1:RCC->APB1ENR=value;break;
    case R_RESET:RCC->APB1RSTR=value;break;
    case R_MODER:GPIOA->MODER=value;break;
    case R_OTYPER:GPIOA->OTYPER=value;break;
    case R_SPEED:GPIOA->OSPEEDR=value;break;
    case R_PULL:GPIOA->PUPDR=value;break;
    case R_AFRL:GPIOA->AFR[0]=value;break;
    case R_BSRR:GPIOA->BSRR=value;break;
    case R_CR1:TIM2->CR1=value;break;
    case R_CR2:TIM2->CR2=value;break;
    case R_SMCR:TIM2->SMCR=value;break;
    case R_DIER:TIM2->DIER=value;break;
    case R_SR:TIM2->SR=value;break;
    case R_EGR:TIM2->EGR=value;break;
    case R_CCMR1:TIM2->CCMR1=value;break;
    case R_CCER:TIM2->CCER=value;break;
    case R_CNT:TIM2->CNT=value;break;
    case R_PSC:TIM2->PSC=value;break;
    case R_ARR:TIM2->ARR=value;break;
    case R_CCR2:TIM2->CCR2=value;break;
    case C_CR1:TIM5->CR1=value;break;
    case C_CR2:TIM5->CR2=value;break;
    case C_SMCR:TIM5->SMCR=value;break;
    case C_DIER:TIM5->DIER=value;break;
    case C_SR:TIM5->SR=value;break;
    case C_EGR:TIM5->EGR=value;break;
    case C_CCMR2:TIM5->CCMR2=value;break;
    case C_CCER:TIM5->CCER=value;break;
    case C_CNT:TIM5->CNT=value;break;
    case C_PSC:TIM5->PSC=value;break;
    case C_ARR:TIM5->ARR=value;break;
    default:break; /* Capture CCR3 is never writable. */
    }
}
static void barrier(void *unused) { (void)unused;__DSB(); }
static struct route_io route={.read=read_route,.write=write_route,.barrier=barrier};
int main(void)
{
    __disable_irq();SystemCoreClockUpdate();
    struct timer_plan plan;
    if (!timer_plan(16000000U,1000000U,1000U,250U,&plan)) for (;;) __NOP();
    praxis_route_status=route_start(&route,&plan,true,true);
    uint32_t previous=0U,current=0U;
    /* Discard the output-enable edge and prime a natural PWM-period edge. */
    if (praxis_route_status==ROUTE_OK) praxis_route_status=route_capture(&route,100000U,&previous);
    if (praxis_route_status==ROUTE_OK) praxis_route_status=route_capture(&route,100000U,&previous);
    for (unsigned i=0U;i<8U && praxis_route_status==ROUTE_OK;++i) {
        praxis_route_status=route_capture(&route,100000U,&current);
        if (praxis_route_status==ROUTE_OK) {
            praxis_route_last_delta=current-previous;
            /* Authored loopback tolerance in local timer ticks, not a calibrated Hz claim. */
            if (!route_period(previous,current,1000U,2U)) praxis_route_status=route_fail(&route,ROUTE_STATE);
            else { ++praxis_route_frames;previous=current; }
        }
    }
    if (praxis_route_status==ROUTE_OK) praxis_route_status=route_stop(&route);
    praxis_route_completed=praxis_route_status==ROUTE_OK && route.quiet && praxis_route_frames==8U;
    for (;;) __NOP();
}
