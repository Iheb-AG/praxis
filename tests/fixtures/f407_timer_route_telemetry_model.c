/* Reuse the independent timer/GPIO effects, running the actual application procedure.
 * No physical board, subprocess or network operation is performed by this fixture. */
#define main historical_model_main
#include "f407_timer_route_model.c"
#undef main
#include "route_scenario.h"
static int injected,wrap_counter;
static unsigned fences,publication_violations;
static volatile PraxisTimerRouteTelemetry published;
static void publication_fence(void)
{
    if (!(published.generation&1U)) ++publication_violations;
    ++fences;
}
static uint32_t scenario_read(void *context,enum route_register reg)
{
    struct model *m=context;
    if (m->armed && reg==R_PRIMASK && !injected) {
        injected=1;
        if (m->fault==25) m->r[R_APB1]&=~RCC_APB1ENR_TIM5EN;
        if (m->fault==26) m->r[R_AHB1]&=~RCC_AHB1ENR_GPIOAEN;
        if (m->fault==27) m->r[R_APB1]&=~RCC_APB1ENR_TIM2EN;
        if (m->fault==30) m->r[R_AFRL]^=1UL<<4U;
    }
    return read_reg(context,reg);
}
static void scenario_write(void *context,enum route_register reg,uint32_t value)
{
    struct model *m=context;
    write_reg(context,reg,value);
    if (reg==R_CR1 && (m->r[R_CR1]&TIM_CR1_CEN)) {
        m->armed=1;
        if (wrap_counter) m->r[C_CNT]=0xFFFFF800U;
    }
}
int main(int argc,char **argv)
{
    struct model m={0};m.fault=argc>1?atoi(argv[1]):0;wrap_counter=argc>2;
    m.r[R_CLOCK]=16000000U;m.r[R_RCC_CR]=RCC_CR_HSION|RCC_CR_HSIRDY;m.r[R_PRIMASK]=1U;
    m.r[R_AHB1]=RCC_AHB1ENR_GPIODEN;m.r[R_APB1]=RCC_APB1ENR_USART2EN;
    m.r[R_RESET]=1UL<<21U;m.r[R_MODER]=0xA8000000U;
    m.r[R_PULL]=0x64000000U;m.r[R_SPEED]=0x0C000000U;
    m.r[R_OTYPER]=1UL<<8U;m.r[R_AFRL]=0x90000000U;
    if (m.fault==2) m.r[R_PRIMASK]=0U;
    if (m.fault==3) m.r[R_CFGR]=RCC_CFGR_PPRE1_DIV4;
    if (m.fault==4) m.r[R_APB1]|=RCC_APB1ENR_TIM2EN;
    if (m.fault==5) m.r[R_APB1]|=RCC_APB1ENR_TIM5EN;
    if (m.fault==6) m.r[R_MODER]|=2UL<<4U;
    if (m.fault==7) m.r[R_LOCK]=ROUTE_PINS|GPIO_LCKR_LCKK;
    struct route_io io={.read=scenario_read,.write=scenario_write,.barrier=barrier,.context=&m};
    PraxisTimerRouteTelemetry result;
    route_run(&io,&result,true,m.fault!=31);
    for (unsigned i=0;i<2;++i) {
        ++result.publications;route_telemetry_publish(&published,&result,publication_fence);
    }
    printf("{\"violations\":%u,\"reads\":%u,\"writes\":%u,\"fences\":%u,\"words\":[%u",
        m.violations+publication_violations,m.reads,m.writes,fences,published.generation);
#define PRINT(name) printf(",%u",published.name);
    ROUTE_TELEMETRY_FIELDS(PRINT)
#undef PRINT
    puts("]}");return 0;
}
