/* Independent timer/GPIO effects plus NVIC pending/active delivery; no adapter. */
#define main old_polling_model_main
#include "f407_timer_route_model.c"
#undef main
#include "irq_controller.h"
struct interrupt_model {
    struct model hw;
    uint32_t n[N_IDLE+1];
    struct irq_route *state;
    unsigned irq_reads,irq_writes,deliveries;
    int fault,started,wrap,immediate;
};
static volatile PraxisTimerRouteTelemetry published;
static unsigned publication_fences,publication_violations;
static void publication_fence(void)
{
    if (!(published.generation&1U)) ++publication_violations;
    ++publication_fences;
}
static uint32_t hw_read(void *ctx,enum route_register reg)
{
    struct interrupt_model *m=ctx;
    if (reg==C_CCR3 && m->n[N_IPSR]!=16U+(uint32_t)TIM5_IRQn) ++m->hw.violations;
    return read_reg(&m->hw,reg);
}
static void hw_write(void *ctx,enum route_register reg,uint32_t value)
{
    struct interrupt_model *m=ctx;
    if (reg==C_DIER && value && m->fault==42) return;
    if (reg==C_DIER && !value && m->started && m->fault==47) return;
    write_reg(&m->hw,reg,value);
    if (reg==R_CR1 && (m->hw.r[R_CR1]&TIM_CR1_CEN)) {
        m->started=1;
        if (m->wrap) m->hw.r[C_CNT]=0xFFFFF800U;
    }
}
static void hw_fence(void *ctx) { (void)ctx; }
static void dispatch(struct interrupt_model *m)
{
    if (!m->started) return;
    if (!(m->hw.r[C_SR]&TIM_SR_CC3IF) && m->fault!=1) {
        m->hw.r[C_CNT]+=m->fault==24?1100U:1000U;capture(&m->hw);
    }
    if (m->fault==21) capture(&m->hw);
    if ((m->hw.r[C_SR]&TIM_SR_CC3IF) && (m->hw.r[C_DIER]&TIM_DIER_CC3IE)) m->n[N_PENDING]=1U;
    if (!m->hw.r[R_PRIMASK] && m->n[N_LINE] && m->n[N_PENDING] && m->fault!=48) {
        m->n[N_PENDING]=0U;m->n[N_ACTIVE]=1U;m->n[N_IPSR]=16U+(uint32_t)TIM5_IRQn;
        if (m->fault==44) m->n[N_IPSR]=16U;
        if (m->fault==49) m->hw.r[C_SR]=0U;
        if (m->fault==25) m->hw.r[R_APB1]&=~RCC_APB1ENR_TIM5EN;
        if (m->fault==26) m->hw.r[R_AHB1]&=~RCC_AHB1ENR_GPIOAEN;
        if (m->fault==27) m->hw.r[R_APB1]&=~RCC_APB1ENR_TIM2EN;
        if (m->fault==30) m->hw.r[R_AFRL]^=1UL<<4U;
        ++m->deliveries;irq_handler(m->state);
        m->n[N_IPSR]=0U;
        if (m->fault!=50) m->n[N_ACTIVE]=0U;
    }
}
static uint32_t irq_read(void *ctx,enum irq_register reg)
{
    struct interrupt_model *m=ctx;++m->irq_reads;
    if (reg==N_IDLE) {dispatch(m);return 0U;}
    return m->n[reg];
}
static void irq_write(void *ctx,enum irq_register reg,uint32_t value)
{
    struct interrupt_model *m=ctx;++m->irq_writes;
    if (reg!=N_PRIORITY && value!=1U) ++m->hw.violations;
    switch(reg) {
    case N_PRIORITY:if (m->fault!=40) m->n[N_PRIORITY]=value;break;
    case N_CLEAR:if (!(m->fault==45 && m->started)) m->n[N_PENDING]=0U;else m->n[N_PENDING]=1U;break;
    case N_ENABLE:
        if (m->hw.r[C_DIER] || m->hw.r[R_CCER] || m->hw.r[R_CR1]&TIM_CR1_CEN ||
                m->n[N_PRIORITY]!=32U || m->n[N_PENDING] || m->n[N_VECTOR_OK]!=1U ||
                m->hw.r[C_CCER]!=TIM_CCER_CC3E || m->hw.r[C_CR1]!=TIM_CR1_CEN)
            ++m->hw.violations;
        if (m->fault!=41) m->n[N_LINE]=1U;
        break;
    case N_DISABLE:if (m->fault!=46) m->n[N_LINE]=0U;break;
    case N_MASK:m->hw.r[R_PRIMASK]=1U;m->hw.armed=1;break;
    case N_UNMASK:
        if (m->fault!=43) m->hw.r[R_PRIMASK]=0U;
        if (m->immediate) dispatch(m);
        break;
    default:++m->hw.violations;break;
    }
}
int main(int argc,char **argv)
{
    struct interrupt_model m={0};m.fault=argc>1?atoi(argv[1]):0;
    m.wrap=argc>2 && atoi(argv[2]);m.immediate=argc>3 && atoi(argv[3]);
    m.hw.fault=m.fault<=31?m.fault:0;m.n[N_VECTOR_OK]=1U;
    m.n[N_SYSTEM_QUIET]=m.n[N_OTHER_QUIET]=1U;
    m.hw.r[R_CLOCK]=16000000U;m.hw.r[R_RCC_CR]=RCC_CR_HSION|RCC_CR_HSIRDY;m.hw.r[R_PRIMASK]=1U;
    m.hw.r[R_AHB1]=RCC_AHB1ENR_GPIODEN;m.hw.r[R_APB1]=RCC_APB1ENR_USART2EN;
    m.hw.r[R_RESET]=1UL<<21U;m.hw.r[R_MODER]=0xA8000000U;m.hw.r[R_PULL]=0x64000000U;
    m.hw.r[R_SPEED]=0x0C000000U;m.hw.r[R_OTYPER]=1UL<<8U;m.hw.r[R_AFRL]=0x90000000U;
    switch(m.fault) {
    case 2:m.hw.r[R_PRIMASK]=0U;break;
    case 3:m.hw.r[R_CFGR]=RCC_CFGR_PPRE1_DIV4;break;
    case 4:m.hw.r[R_APB1]|=RCC_APB1ENR_TIM2EN;break;
    case 5:m.hw.r[R_APB1]|=RCC_APB1ENR_TIM5EN;break;
    case 6:m.hw.r[R_MODER]|=2UL<<4U;break;
    case 7:m.hw.r[R_LOCK]=ROUTE_PINS|GPIO_LCKR_LCKK;break;
    case 32:m.n[N_BASEPRI]=16U;break;
    case 33:m.n[N_FAULTMASK]=1U;break;
    case 34:m.n[N_CONTROL]=1U;break;
    case 35:m.n[N_GROUP]=4U;break;
    case 36:m.n[N_VECTOR_OK]=0U;break;
    case 37:m.n[N_LINE]=1U;break;
    case 38:m.n[N_PENDING]=1U;break;
    case 39:m.n[N_ACTIVE]=1U;break;
    case 51:m.n[N_CONTROL]=2U;break;
    case 52:case 53:m.n[N_SYSTEM_QUIET]=0U;break;
    case 54:m.n[N_OTHER_QUIET]=0U;break;
    default:break;
    }
    struct route_io route={.read=hw_read,.write=hw_write,.barrier=hw_fence,.context=&m};
    struct irq_io irq={.read=irq_read,.write=irq_write,.fence=hw_fence,.context=&m};
    PraxisTimerRouteTelemetry result;
    struct irq_route state={.route=&route,.irq=&irq,.result=&result};m.state=&state;
    irq_run(&state,m.fault!=31);
    if (argc>4 && atoi(argv[4])) {published.generation=0xFFFFFFFEU;result.publications=0xFFFFFFFFU;}
    for (unsigned i=0;i<2U;++i) {
        ++result.publications;route_telemetry_publish(&published,&result,publication_fence);
    }
    printf("{\"violations\":%u,\"reads\":%u,\"writes\":%u,\"irq_reads\":%u,\"irq_writes\":%u,\"deliveries\":%u,\"fences\":%u,\"words\":[%u",
        m.hw.violations+publication_violations,m.hw.reads,m.hw.writes,m.irq_reads,m.irq_writes,m.deliveries,publication_fences,published.generation);
#define PRINT(name) printf(",%u",published.name);
    ROUTE_TELEMETRY_FIELDS(PRINT)
#undef PRINT
    puts("]}");return 0;
}
