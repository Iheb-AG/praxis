/* Independent dual-timer/GPIO effects; no simulated hardware qualification. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "routed_timer.h"
struct model {
    uint32_t r[R_REGISTERS],pwm_arr,pwm_ccr;
    unsigned reads,writes,violations,gpio_seen,gate_seen,pwm_ug,capture_ug,output_enables,events,ccr_writes;
    int fault,armed,post;
};
static void capture(struct model *m)
{
    if (m->r[C_SR]&TIM_SR_CC3IF) m->r[C_SR]|=TIM_SR_CC3OF;
    m->r[C_CCR3]=m->r[C_CNT];m->r[C_SR]|=TIM_SR_CC3IF;++m->events;
}
static void check_access(struct model *m,enum route_register reg)
{
    if (reg>=R_MODER && reg<=R_LOCK &&
            (!(m->r[R_AHB1]&RCC_AHB1ENR_GPIOAEN)||!m->gpio_seen)) ++m->violations;
    if (reg>=R_CR1 && reg<=R_CCR2 &&
            (!(m->r[R_APB1]&RCC_APB1ENR_TIM2EN)||!m->gate_seen)) ++m->violations;
    if (reg>=C_CR1 && reg<=C_CCR3 &&
            (!(m->r[R_APB1]&RCC_APB1ENR_TIM5EN)||!m->gate_seen)) ++m->violations;
}
static uint32_t read_reg(void *context,enum route_register reg)
{
    struct model *m=context;++m->reads;check_access(m,reg);
    if (reg==R_AHB1 && (m->r[R_AHB1]&RCC_AHB1ENR_GPIOAEN)) m->gpio_seen=1U;
    if (reg==R_APB1 && (m->r[R_APB1]&ROUTE_TIMER_GATES)==ROUTE_TIMER_GATES) m->gate_seen=1U;
    if (reg==R_BSRR || reg==R_EGR || reg==C_EGR) ++m->violations;
    if (reg==C_SR && m->armed) {
        if (m->post) m->post=0;
        else if (m->fault!=1 && !(m->r[C_SR]&TIM_SR_CC3IF) &&
                (m->r[R_CR1]&TIM_CR1_CEN) && (m->r[C_CR1]&TIM_CR1_CEN)) {
            m->r[C_CNT]+=m->fault==24?1100U:1000U;
            capture(m);
            if (m->fault==21) capture(m);
        }
    }
    uint32_t result=m->r[reg];
    if (reg==C_CCR3) {
        m->r[C_SR]&=~TIM_SR_CC3IF;m->post=1;
        if (m->fault==22) capture(m);
        if (m->fault==23) m->r[C_SR]|=TIM_SR_CC3OF;
    }
    return result;
}
static void write_reg(void *context,enum route_register reg,uint32_t value)
{
    struct model *m=context;++m->writes;check_access(m,reg);
    if (reg==C_CCR3) ++m->violations;
    if (reg==R_AHB1 && m->fault==11) return;
    if (reg==R_APB1 && m->fault==12) return;
    if (reg==R_RESET && m->fault==13 && value&ROUTE_TIMER_RESETS) return;
    if (reg==R_RESET && m->fault==14 && !(value&ROUTE_TIMER_RESETS)) return;
    if (reg==R_RESET && value&ROUTE_TIMER_RESETS) {
        memset(m->r+R_CR1,0,(R_REGISTERS-R_CR1)*sizeof(uint32_t));
        m->r[R_ARR]=m->r[C_ARR]=UINT32_MAX;
    }
    if (reg==R_CCMR1 && m->fault==9) value=TIM_CCMR1_CC2S;
    if (reg==C_CCMR2 && m->fault==10) value=0U;
    if (reg==R_CCR2) {
        ++m->ccr_writes;
        if (m->r[R_CCMR1]&TIM_CCMR1_CC2S) ++m->violations;
        if (m->fault==19) return;
    }
    if (reg==R_AFRL && m->fault==8) return;
    if (reg==R_MODER && (value&ROUTE_MODE_MASK)==ROUTE_AF_MODE && (m->r[R_CCER]&TIM_CCER_CC2E))
        ++m->violations;
    if (reg==R_MODER && m->armed && m->fault==28 && !(value&ROUTE_MODE_MASK)) return;
    if (reg==R_CCER && m->armed && m->fault==29 && !value) return;
    if (reg==R_EGR) {
        if (value!=TIM_EGR_UG) ++m->violations;
        ++m->pwm_ug;m->pwm_arr=m->r[R_ARR];m->pwm_ccr=m->r[R_CCR2];m->r[R_CNT]=0U;
        m->r[R_SR]|=TIM_SR_UIF;return;
    }
    if (reg==C_EGR) {
        if (value!=TIM_EGR_UG) ++m->violations;
        ++m->capture_ug;m->r[C_CNT]=0U;m->r[C_SR]|=TIM_SR_UIF;return;
    }
    if (reg==R_SR || reg==C_SR) {
        if (m->fault!=20) m->r[reg]&=value;
        return;
    }
    if (reg==C_CCER && value) {
        if (!m->capture_ug || m->r[C_CCMR2]!=ROUTE_CAPTURE || m->r[C_DIER] ||
                m->r[C_SR] || m->r[C_ARR]!=UINT32_MAX) ++m->violations;
        if (m->fault==15) return;
    }
    if (reg==C_CR1 && value&TIM_CR1_CEN && m->fault==18) return;
    if (reg==R_CR1 && value&TIM_CR1_CEN && m->fault==17) return;
    if (reg==R_CCER && value) {
        if (!m->pwm_ug || m->pwm_arr!=999U || m->pwm_ccr!=250U || m->r[R_DIER] ||
                m->r[C_CCER]!=TIM_CCER_CC3E || m->r[C_CR1]!=TIM_CR1_CEN ||
                (m->r[R_MODER]&ROUTE_MODE_MASK)!=ROUTE_AF_MODE ||
                (m->r[R_AFRL]&ROUTE_AF_MASK)!=ROUTE_AF) ++m->violations;
        if (m->fault==16) return;
        ++m->output_enables;
        if (m->fault!=1) capture(m); /* Initial enable edge, discarded by the application. */
    }
    m->r[reg]=value;
}
static void barrier(void *context) { (void)context; }
int main(int argc,char **argv)
{
    struct model m={0};m.fault=argc>1?atoi(argv[1]):0;
    m.r[R_CLOCK]=16000000U;m.r[R_RCC_CR]=RCC_CR_HSION|RCC_CR_HSIRDY;m.r[R_PRIMASK]=1U;
    m.r[R_AHB1]=RCC_AHB1ENR_GPIODEN;m.r[R_APB1]=RCC_APB1ENR_USART2EN;
    m.r[R_RESET]=1UL<<21U;
    m.r[R_MODER]=0xA8000000U;m.r[R_PULL]=0x64000000U;m.r[R_SPEED]=0x0C000000U;
    m.r[R_OTYPER]=1UL<<8U;m.r[R_AFRL]=0x90000000U;
    switch(m.fault) {
    case 2:m.r[R_PRIMASK]=0U;break;
    case 3:m.r[R_CFGR]=RCC_CFGR_PPRE1_DIV4;break;
    case 4:m.r[R_APB1]|=RCC_APB1ENR_TIM2EN;break;
    case 5:m.r[R_APB1]|=RCC_APB1ENR_TIM5EN;break;
    case 6:m.r[R_MODER]|=2UL<<4U;break;
    case 7:m.r[R_LOCK]=ROUTE_PINS|GPIO_LCKR_LCKK;break;
    default:break;
    }
    struct route_io io={.read=read_reg,.write=write_reg,.barrier=barrier,.context=&m};
    struct timer_plan plan;timer_plan(16000000U,1000000U,1000U,250U,&plan);
    enum route_status start=route_start(&io,&plan,true,m.fault!=31);
    enum route_status operation=start,stop=start,retry=ROUTE_OK;
    unsigned frames=0U;uint32_t previous=0U,value=0xDEADBEEFU,last_delta=0U;
    if (start==ROUTE_OK) {
        m.armed=1;
        if (m.fault==25) m.r[R_APB1]&=~RCC_APB1ENR_TIM5EN;
        if (m.fault==26) m.r[R_AHB1]&=~RCC_AHB1ENR_GPIOAEN;
        if (m.fault==27) m.r[R_APB1]&=~RCC_APB1ENR_TIM2EN;
        if (m.fault==30) m.r[R_AFRL]^=1UL<<4U;
        operation=route_capture(&io,8U,&previous);
        if (operation==ROUTE_OK) operation=route_capture(&io,8U,&previous);
        if (argc>2 && operation==ROUTE_OK) { m.r[C_CNT]=0xFFFFFF00U;previous=m.r[C_CNT]; }
        for(unsigned i=0U;i<8U && operation==ROUTE_OK;++i) {
            operation=route_capture(&io,8U,&value);
            if (operation==ROUTE_OK) {
                last_delta=value-previous;
                if (!route_period(previous,value,1000U,2U)) operation=route_fail(&io,ROUTE_STATE);
                else { ++frames;previous=value; }
            }
        }
        stop=operation==ROUTE_OK?route_stop(&io):operation;
    }
    unsigned writes=m.writes;
    if (io.failed) retry=route_start(&io,&plan,true,true);
    printf("{\"start\":%u,\"operation\":%u,\"stop\":%u,\"failed\":%u,\"quiet\":%u,"
        "\"pins_quiet\":%u,\"timer_quiet\":%u,\"retry\":%u,\"retry_writes\":%u,\"violations\":%u,"
        "\"frames\":%u,\"delta\":%u,\"value\":%u,\"reads\":%u,\"writes\":%u,\"enables\":%u,"
        "\"ccr_writes\":%u,\"moder\":%u,\"afrl\":%u,\"pull\":%u,\"gate\":%u,\"ahb\":%u}\n",
        start,operation,stop,io.failed,io.quiet,io.pins_quiet,io.timer_quiet,retry,m.writes-writes,m.violations,
        frames,last_delta,value,m.reads,m.writes,m.output_enables,m.ccr_writes,
        m.r[R_MODER],m.r[R_AFRL],m.r[R_PULL],m.r[R_APB1],m.r[R_AHB1]);
    return 0;
}
