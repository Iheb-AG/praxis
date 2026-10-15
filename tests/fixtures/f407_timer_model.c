/* Independent timer effect model: preload transfer, rc_w0 flags, read-to-clear
 * capture and forbidden accesses. Same controller executes here and on target.
 * It is not an emulator or evidence of electrical/timing behavior.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "timer_controller.h"
struct model {
    uint32_t r[T_REGISTERS], active_arr, active_ccr;
    unsigned reads,writes,barriers,violation,gate_seen,ug,events,ccr_writes,ccr_reads;
    int fault, armed;
};
static void update(struct model *m)
{
    m->active_arr=m->r[T_ARR]; m->active_ccr=m->r[T_CCR1];
    m->r[T_CNT]=0U; m->r[T_SR]|=TIM_SR_UIF;
}
static void capture(struct model *m)
{
    if (m->r[T_SR]&TIM_SR_CC1IF) m->r[T_SR]|=TIM_SR_CC1OF;
    m->r[T_CCR1]=m->r[T_CNT]; m->r[T_SR]|=TIM_SR_CC1IF; ++m->events;
}
static uint32_t read_reg(void *context, enum timer_register reg)
{
    struct model *m=context; ++m->reads;
    if (reg>=T_CR1 && (!(m->r[T_GATE]&RCC_APB1ENR_TIM2EN) || !m->gate_seen)) ++m->violation;
    if (reg==T_EGR) ++m->violation;
    if (reg==T_GATE && (m->r[T_GATE]&RCC_APB1ENR_TIM2EN)) m->gate_seen=1U;
    if (m->armed && reg==T_SR && m->fault!=12 && (m->r[T_CR1]&TIM_CR1_CEN)) update(m);
    uint32_t result=m->r[reg];
    if (reg==T_CCR1 && (m->r[T_CCMR1]&TIM_CCMR1_CC1S)) {
        ++m->ccr_reads; m->r[T_SR]&=~TIM_SR_CC1IF;
        if (m->armed && m->fault==16) capture(m); /* New event after data read. */
        if (m->armed && m->fault==17) m->r[T_SR]|=TIM_SR_CC1OF;
    }
    return result;
}
static void write_reg(void *context, enum timer_register reg, uint32_t value)
{
    struct model *m=context; ++m->writes;
    if (reg>=T_CR1 && (!(m->r[T_GATE]&RCC_APB1ENR_TIM2EN) || !m->gate_seen)) ++m->violation;
    if (reg==T_GATE && m->fault==8) return;
    if (reg==T_RESET && m->fault==9 && value&RCC_APB1RSTR_TIM2RST) return;
    if (reg==T_RESET && m->fault==10 && !(value&RCC_APB1RSTR_TIM2RST)) return;
    if (reg==T_RESET && value&RCC_APB1RSTR_TIM2RST) {
        memset(m->r+T_CR1,0,(T_REGISTERS-T_CR1)*sizeof(uint32_t));
        m->r[T_ARR]=UINT32_MAX; m->active_arr=UINT32_MAX;
    }
    if (reg==T_CCMR1 && (m->r[T_CCER]&TIM_CCER_CC1E)) ++m->violation;
    if (reg==T_PSC && value>65535U) ++m->violation;
    if (reg==T_CCR1) {
        ++m->ccr_writes;
        if (m->r[T_CCMR1]&TIM_CCMR1_CC1S) ++m->violation;
        if (m->armed && m->fault==13) return;
        if (m->fault==23) return;
    }
    if (reg==T_CCER && value) {
        if (!m->ug || !m->barriers || m->r[T_DIER] || m->r[T_SR] ||
                m->r[T_CCMR1]!=TIMER_CAPTURE_CCMR || value!=TIM_CCER_CC1E) ++m->violation;
        if (m->fault==11) return;
    }
    if (reg==T_CR1 && value&TIM_CR1_CEN) {
        if (!m->ug || !m->barriers || m->r[T_SR] || m->r[T_CCER] || m->r[T_DIER] ||
                m->r[T_CCMR1]!=TIMER_PWM_CCMR || m->active_arr!=m->r[T_ARR] ||
                m->active_ccr!=m->r[T_CCR1]) ++m->violation;
        if (m->fault==11) return;
    }
    if (m->armed && m->fault==20 && reg==T_CR1 && !value) return;
    if (reg==T_EGR) {
        if (value==TIM_EGR_UG) { ++m->ug; update(m); }
        else if (value==TIM_EGR_CC1G) {
            if (m->r[T_CR1] || m->r[T_CCMR1]!=TIMER_CAPTURE_CCMR ||
                    m->r[T_CCER]!=TIM_CCER_CC1E || m->r[T_SMCR]) ++m->violation;
            if (m->fault!=14) capture(m);
            if (m->fault==15) capture(m); /* Overcapture before consumption. */
            if (m->fault==18) m->r[T_CCR1]^=1U;
        } else ++m->violation;
        return;
    }
    if (reg==T_SR) { if (m->fault!=24) m->r[reg]&=value; return; }
    if (reg==T_SMCR && m->fault==25) value=TIM_SMCR_ECE;
    if (reg==T_CCMR1 && m->fault==26) value^=TIM_CCMR1_CC1S;
    m->r[reg]=value;
}
static void barrier(void *context) { ++((struct model *)context)->barriers; }
int main(int argc, char **argv)
{
    struct model m={0};
    int mode=argc>1?atoi(argv[1]):0; m.fault=argc>2?atoi(argv[2]):0;
    uint32_t high=argc>3?(uint32_t)strtoul(argv[3],NULL,0):250U;
    if (mode==2 && argc==6) {
        struct timer_plan plan={0};
        bool valid=timer_plan((uint32_t)strtoul(argv[2],NULL,0),(uint32_t)strtoul(argv[3],NULL,0),
            (uint32_t)strtoul(argv[4],NULL,0),(uint32_t)strtoul(argv[5],NULL,0),&plan);
        printf("{\"valid\":%u,\"prescaler\":%u,\"period\":%u,\"high\":%u}\n",valid,plan.prescaler,plan.period,plan.high);
        return 0;
    }
    m.r[T_CLOCK]=16000000U; m.r[T_RCC_CR]=RCC_CR_HSION|RCC_CR_HSIRDY; m.r[T_PRIMASK]=1U;
    m.r[T_GATE]=1UL<<17; /* Unrelated UART gate must survive every RCC write. */
    m.r[T_RESET]=1UL<<21;
    switch (m.fault) {
    case 1:m.r[T_PRIMASK]=0U;break;
    case 2:m.r[T_IPSR]=16U;break;
    case 3:m.r[T_CLOCK]=84000000U;break;
    case 4:m.r[T_CFGR]=RCC_CFGR_PPRE1_DIV4;break;
    case 5:m.r[T_RCC_CR]&=~RCC_CR_HSIRDY;break;
    case 6:m.r[T_GATE]|=RCC_APB1ENR_TIM2EN;break;
    case 7:m.r[T_APB2]=RCC_APB2ENR_TIM1EN;break;
    default:break;
    }
    struct timer_io io={.read=read_reg,.write=write_reg,.barrier=barrier,.context=&m};
    struct timer_plan plan;
    if (!timer_plan(16000000U,1000000U,1000U,high,&plan)) return 2;
    enum timer_status start=timer_start(&io,mode?TIMER_SOFTWARE_CAPTURE:TIMER_PWM_REFERENCE,&plan,true);
    enum timer_status operation=start,stop=start,retry=TIMER_OK;
    uint32_t value=0xDEADBEEFU, active_before=0U, active_after=0U, ones=0U, ones_before=0U;
    if (start==TIMER_OK) {
        m.armed=1;
        if (m.fault==19) m.r[T_GATE]&=~RCC_APB1ENR_TIM2EN;
        if (m.fault==21) m.r[T_CCMR1]^=TIM_CCMR1_CC1S;
        if (mode) {
            if (m.fault==22) m.r[T_SR]|=TIM_SR_CC1IF;
            operation=timer_capture(&io,0x12345678U,8U,&value);
        } else {
            active_before=m.active_ccr;
            for (uint32_t cnt=0U;cnt<=m.active_arr;++cnt) ones_before+=cnt<m.active_ccr;
            operation=timer_pwm_set(&io,750U);
            if (operation==TIMER_OK) operation=timer_wait_update(&io,8U);
            active_after=m.active_ccr;
            for (uint32_t cnt=0U;cnt<=m.active_arr;++cnt) ones+=cnt<m.active_ccr;
        }
        stop=operation==TIMER_OK?timer_stop(&io):operation;
    }
    unsigned writes=m.writes;
    if (io.failed) retry=timer_start(&io,mode?TIMER_SOFTWARE_CAPTURE:TIMER_PWM_REFERENCE,&plan,true);
    printf("{\"start\":%u,\"operation\":%u,\"stop\":%u,\"retry\":%u,\"retry_writes\":%u,"
        "\"value\":%u,\"quiet\":%u,\"failed\":%u,\"reads\":%u,\"writes\":%u,\"violation\":%u,"
        "\"active_before\":%u,\"active_after\":%u,\"ones\":%u,\"ones_before\":%u,\"events\":%u,\"ccr_reads\":%u,"
        "\"ccr_writes\":%u,\"gate\":%u,\"reset\":%u,\"ccer\":%u,\"dier\":%u,\"cr1\":%u}\n",
        start,operation,stop,retry,m.writes-writes,value,io.quiet,io.failed,m.reads,m.writes,m.violation,
        active_before,active_after,ones,ones_before,m.events,m.ccr_reads,m.ccr_writes,m.r[T_GATE],m.r[T_RESET],
        m.r[T_CCER],m.r[T_DIER],m.r[T_CR1]);
    return 0;
}
