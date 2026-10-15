/* One-shot application procedure, shared by target and independent effect model. */
#ifndef PRAXIS_TIMER_ROUTE_SCENARIO_H
#define PRAXIS_TIMER_ROUTE_SCENARIO_H
#include "routed_timer.h"
#include "telemetry.h"
static inline void route_saved_capture(volatile PraxisTimerRouteTelemetry *result,uint32_t value)
{
    switch(result->captures) {
    case 0:result->capture0=value;break;
    case 1:result->capture1=value;break;
    case 2:result->capture2=value;break;
    case 3:result->capture3=value;break;
    case 4:result->capture4=value;break;
    case 5:result->capture5=value;break;
    case 6:result->capture6=value;break;
    case 7:result->capture7=value;break;
    case 8:result->capture8=value;break;
    default:return;
    }
    ++result->captures;
}
static inline void route_end_snapshot(struct route_io *io, volatile PraxisTimerRouteTelemetry *result)
{
    /* Never read an inaccessible timer/GPIO domain to fabricate a quiet report. */
    uint32_t gates=io->read(io->context,R_APB1),resets=io->read(io->context,R_RESET);
    if (io->owned && (gates&RCC_APB1ENR_TIM2EN) && !(resets&RCC_APB1RSTR_TIM2RST)) {
        result->end_pwm_cr1=io->read(io->context,R_CR1);
        result->end_pwm_ccer=io->read(io->context,R_CCER);
        result->end_pwm_dier=io->read(io->context,R_DIER);
        result->end_valid_mask|=1U;
    }
    if (io->owned && (gates&RCC_APB1ENR_TIM5EN) && !(resets&RCC_APB1RSTR_TIM5RST)) {
        result->end_capture_cr1=io->read(io->context,C_CR1);
        result->end_capture_ccer=io->read(io->context,C_CCER);
        result->end_capture_dier=io->read(io->context,C_DIER);
        result->end_valid_mask|=2U;
    }
    if (io->pins_owned && (io->read(io->context,R_AHB1)&RCC_AHB1ENR_GPIOAEN)) {
        result->end_pin_modes=io->read(io->context,R_MODER)&ROUTE_MODE_MASK;
        result->end_valid_mask|=4U;
    }
    result->flags=(io->timer_quiet?1U:0U)|(io->pins_quiet?2U:0U)|
        (io->failed?4U:0U)|(io->read(io->context,R_PRIMASK)==1U?8U:0U);
}
static inline void route_run(struct route_io *io, PraxisTimerRouteTelemetry *result,
                             bool startup_owned, bool wiring_owned)
{
    /* Explicit volatile scalar stores: pinned freestanding assets supply no memset. */
    volatile PraxisTimerRouteTelemetry *clear=result;
    clear->generation=0U;
#define ROUTE_CLEAR(name) clear->name=0U;
    ROUTE_TELEMETRY_FIELDS(ROUTE_CLEAR)
#undef ROUTE_CLEAR
    result->magic=ROUTE_TELEMETRY_MAGIC;result->abi=ROUTE_TELEMETRY_ABI;
    result->size_bytes=sizeof(*result);result->expected_frames=8U;
    result->clock_hz=io->read(io->context,R_CLOCK);
    result->period_ticks=1000U;result->tolerance_ticks=2U;
    result->prescaler=15U;result->period_counts=1000U;result->high_counts=250U;
    struct timer_plan plan;
    enum route_status status=ROUTE_INVALID;
    if (timer_plan(16000000U,1000000U,1000U,250U,&plan))
        status=route_start(io,&plan,startup_owned,wiring_owned);
    uint32_t previous=0U,current=0U;
    if (status==ROUTE_OK) status=route_capture(io,100000U,&previous); /* Discard enable edge. */
    if (status==ROUTE_OK) {
        status=route_capture(io,100000U,&previous);
        if (status==ROUTE_OK) route_saved_capture(result,previous);
    }
    for (unsigned i=0U;i<8U && status==ROUTE_OK;++i) {
        status=route_capture(io,100000U,&current);
        if (status==ROUTE_OK) {
            route_saved_capture(result,current); /* Preserve rejected interval evidence too. */
            if (!route_period(previous,current,1000U,2U)) status=route_fail(io,ROUTE_STATE);
            else { ++result->frames;previous=current; }
        }
    }
    if (status==ROUTE_OK) status=route_stop(io);
    route_end_snapshot(io,result);
    result->status=status;
    result->phase=status==ROUTE_OK && result->frames==8U && io->quiet?1U:2U;
}
#endif
