/* Target-specific example. TIM5 IRQ50/slot66 from pinned device header;
 * PM0214 Rev10 NVIC210-215, special registers22-26, vector227, group228-229;
 * RM0090 Rev22 DIER629 and SR630-631. No compiler policy is encoded here. */
#ifndef PRAXIS_TIMER_IRQ_CONTROLLER_H
#define PRAXIS_TIMER_IRQ_CONTROLLER_H
#include "route_scenario.h"
enum irq_register {N_LINE,N_PENDING,N_ACTIVE,N_PRIORITY,N_BASEPRI,N_FAULTMASK,
    N_CONTROL,N_GROUP,N_VECTOR_OK,N_IPSR,N_SYSTEM_QUIET,N_OTHER_QUIET,
    N_ENABLE,N_DISABLE,N_CLEAR,N_MASK,N_UNMASK,N_IDLE};
struct irq_io {
    uint32_t (*read)(void *,enum irq_register);
    void (*write)(void *,enum irq_register,uint32_t);
    void (*fence)(void *);
    void *context;
};
struct irq_route {
    struct route_io *route;
    struct irq_io *irq;
    volatile PraxisTimerRouteTelemetry *result;
    volatile uint32_t done;
    volatile enum route_status status;
    bool irq_owned,armed;
};
static inline bool irq_disable(struct irq_route *state)
{
    struct route_io *r=state->route;struct irq_io *n=state->irq;
    bool source=false;
    if (r->owned && (r->read(r->context,R_APB1)&RCC_APB1ENR_TIM5EN) &&
            !(r->read(r->context,R_RESET)&RCC_APB1RSTR_TIM5RST)) {
        r->write(r->context,C_DIER,0U);r->barrier(r->context);
        source=r->read(r->context,C_DIER)==0U;
    }
    n->write(n->context,N_DISABLE,1U);n->fence(n->context);
    n->write(n->context,N_CLEAR,1U);n->fence(n->context);
    return source && !n->read(n->context,N_LINE) && !n->read(n->context,N_PENDING);
}
static inline void irq_latch(struct irq_route *state,enum route_status status,uint32_t reason)
{
    state->status=status;state->result->irq_error=reason;
    if (state->irq_owned && !irq_disable(state)) state->result->irq_error=10U;
    state->done=1U;
}
static inline bool irq_live(struct irq_route *state)
{
    struct route_io *r=state->route;
    if (!route_clock(r) || !(r->read(r->context,R_AHB1)&RCC_AHB1ENR_GPIOAEN) ||
            (r->read(r->context,R_APB1)&ROUTE_TIMER_GATES)!=ROUTE_TIMER_GATES ||
            (r->read(r->context,R_RESET)&ROUTE_TIMER_RESETS)) return false;
    return r->read(r->context,R_CCMR1)==ROUTE_PWM && r->read(r->context,C_CCMR2)==ROUTE_CAPTURE &&
        r->read(r->context,R_CCER)==ROUTE_CHANNELS && r->read(r->context,C_CCER)==TIM_CCER_CC3E &&
        r->read(r->context,R_CR1)==(TIM_CR1_ARPE|TIM_CR1_CEN) &&
        r->read(r->context,C_CR1)==TIM_CR1_CEN && !r->read(r->context,R_DIER) &&
        r->read(r->context,C_DIER)==TIM_DIER_CC3IE &&
        (r->read(r->context,R_MODER)&ROUTE_MODE_MASK)==ROUTE_AF_MODE &&
        (r->read(r->context,R_AFRL)&ROUTE_AF_MASK)==ROUTE_AF;
}
static inline void irq_handler(struct irq_route *state)
{
    struct irq_io *n=state->irq;struct route_io *r=state->route;
    volatile PraxisTimerRouteTelemetry *out=state->result;
    ++out->irq_count;
    if (!state->armed || state->done || n->read(n->context,N_IPSR)!=(16U+(uint32_t)TIM5_IRQn) ||
            r->read(r->context,R_PRIMASK) || n->read(n->context,N_BASEPRI) ||
            n->read(n->context,N_FAULTMASK)) { irq_latch(state,ROUTE_CONTEXT,1U);return; }
    if (!irq_live(state)) { irq_latch(state,ROUTE_STATE,2U);return; }
    uint32_t before=r->read(r->context,C_SR);
    if (!(before&TIM_SR_CC3IF) || (before&TIM_SR_CC3OF)) {
        irq_latch(state,(before&TIM_SR_CC3OF)?ROUTE_OVERCAPTURE:ROUTE_STATE,3U);return;
    }
    uint32_t value=r->read(r->context,C_CCR3);++out->data_reads;
    uint32_t after=r->read(r->context,C_SR);
    if (after&(TIM_SR_CC3IF|TIM_SR_CC3OF)) { irq_latch(state,ROUTE_OVERCAPTURE,4U);return; }
    if (!out->discarded_edges) { out->discarded_edges=1U;return; }
    uint32_t previous=0U;
    switch(out->captures) {
    case 0:break;
    case 1:previous=out->capture0;break;
    case 2:previous=out->capture1;break;
    case 3:previous=out->capture2;break;
    case 4:previous=out->capture3;break;
    case 5:previous=out->capture4;break;
    case 6:previous=out->capture5;break;
    case 7:previous=out->capture6;break;
    case 8:previous=out->capture7;break;
    default:irq_latch(state,ROUTE_STATE,5U);return;
    }
    bool primed=out->captures!=0U;
    route_saved_capture(out,value);
    if (primed) {
        if (!route_period(previous,value,1000U,2U)) {irq_latch(state,ROUTE_STATE,6U);return;}
        ++out->frames;
    }
    if (out->frames==8U) {
        if (!irq_disable(state)) {irq_latch(state,ROUTE_STATE,10U);return;}
        state->done=1U;
    }
}
static inline enum route_status irq_start(struct irq_route *state,bool wiring_owned)
{
    struct irq_io *n=state->irq;struct route_io *r=state->route;
    if (!route_interface(r) || !n || !n->read || !n->write || !n->fence || !state->result)
        return ROUTE_INVALID;
    if (state->irq_owned || state->armed || state->done) return ROUTE_BUSY;
    if (!route_context(r) || (n->read(n->context,N_CONTROL)&3U) ||
            n->read(n->context,N_BASEPRI) || n->read(n->context,N_FAULTMASK)) return ROUTE_CONTEXT;
    if (n->read(n->context,N_GROUP) || n->read(n->context,N_VECTOR_OK)!=1U) return ROUTE_STATE;
    if (!n->read(n->context,N_SYSTEM_QUIET) || !n->read(n->context,N_OTHER_QUIET)) return ROUTE_BUSY;
    state->result->vector_verified=1U;
    if (n->read(n->context,N_LINE) || n->read(n->context,N_PENDING) || n->read(n->context,N_ACTIVE))
        return ROUTE_BUSY;
    struct timer_plan plan;
    if (!timer_plan(16000000U,1000000U,1000U,250U,&plan)) return ROUTE_INVALID;
    enum route_status status=route_prepare(r,&plan,true,wiring_owned);
    if (status!=ROUTE_OK) return status;
    state->irq_owned=true;
    n->write(n->context,N_PRIORITY,2U<<(8U-__NVIC_PRIO_BITS));n->fence(n->context);
    state->result->irq_priority=n->read(n->context,N_PRIORITY);
    if (state->result->irq_priority!=(2U<<(8U-__NVIC_PRIO_BITS))) return ROUTE_STATE;
    n->write(n->context,N_CLEAR,1U);n->fence(n->context);
    if (n->read(n->context,N_PENDING)) return ROUTE_STATE;
    r->write(r->context,C_CCER,TIM_CCER_CC3E);r->barrier(r->context);
    if (r->read(r->context,C_CCER)!=TIM_CCER_CC3E) return ROUTE_STATE;
    r->write(r->context,C_CR1,TIM_CR1_CEN);r->barrier(r->context);
    if (r->read(r->context,C_CR1)!=TIM_CR1_CEN) return ROUTE_STATE;
    n->write(n->context,N_ENABLE,1U);n->fence(n->context);
    if (n->read(n->context,N_LINE)!=1U) return ROUTE_STATE;
    r->write(r->context,C_DIER,TIM_DIER_CC3IE);r->barrier(r->context);
    if (r->read(r->context,C_DIER)!=TIM_DIER_CC3IE) return ROUTE_STATE;
    r->write(r->context,R_CCER,ROUTE_CHANNELS);r->barrier(r->context);
    if (r->read(r->context,R_CCER)!=ROUTE_CHANNELS) return ROUTE_STATE;
    r->write(r->context,R_CR1,TIM_CR1_ARPE|TIM_CR1_CEN);r->barrier(r->context);
    if (r->read(r->context,R_CR1)!=(TIM_CR1_ARPE|TIM_CR1_CEN)) return ROUTE_STATE;
    state->armed=true;state->status=ROUTE_OK;n->fence(n->context);
    n->write(n->context,N_UNMASK,1U);
    if (r->read(r->context,R_PRIMASK)) { state->result->irq_error=9U;return ROUTE_CONTEXT; }
    return ROUTE_OK;
}
static inline void irq_run(struct irq_route *state,bool wiring_owned)
{
    struct route_io *r=state->route;struct irq_io *n=state->irq;
    volatile PraxisTimerRouteTelemetry *out=state->result;
    out->generation=0U;
#define IRQ_CLEAR(name) out->name=0U;
    ROUTE_TELEMETRY_FIELDS(IRQ_CLEAR)
#undef IRQ_CLEAR
    out->magic=ROUTE_TELEMETRY_MAGIC;out->abi=ROUTE_TELEMETRY_ABI;out->size_bytes=sizeof(*out);
    out->expected_frames=8U;out->clock_hz=r->read(r->context,R_CLOCK);
    out->period_ticks=1000U;out->tolerance_ticks=2U;out->prescaler=15U;out->period_counts=1000U;out->high_counts=250U;
    enum route_status status=irq_start(state,wiring_owned);
    if (status==ROUTE_OK) {
        for (uint32_t i=0U;i<TIMER_POLL_LIMIT && !state->done;++i) (void)n->read(n->context,N_IDLE);
        n->write(n->context,N_MASK,1U);n->fence(n->context);
        if (!state->done) {
            if ((r->read(r->context,R_APB1)&RCC_APB1ENR_TIM5EN) &&
                    !(r->read(r->context,R_RESET)&RCC_APB1RSTR_TIM5RST))
                out->timeout_pending_capture=(r->read(r->context,C_SR)&(TIM_SR_CC3IF|TIM_SR_CC3OF))!=0U;
            irq_latch(state,ROUTE_TIMEOUT,7U);status=ROUTE_TIMEOUT;
        }
        else status=state->status;
    }
    if (state->irq_owned) {
        n->write(n->context,N_MASK,1U);n->fence(n->context);
        if (!irq_disable(state)) {status=ROUTE_STATE;out->irq_error=10U;}
        out->end_irq_enabled=n->read(n->context,N_LINE);
        out->end_irq_pending=n->read(n->context,N_PENDING);
        out->end_irq_active=n->read(n->context,N_ACTIVE);
        out->irq_snapshot_valid=1U;
        if (out->end_irq_enabled || out->end_irq_pending || out->end_irq_active) {
            status=ROUTE_STATE;out->irq_error=11U;
        }
    }
    if (status==ROUTE_OK && (out->irq_count!=10U || out->data_reads!=10U ||
            out->discarded_edges!=1U || out->frames!=8U || out->captures!=9U)) {
        status=ROUTE_STATE;out->irq_error=8U;
    }
    if (r->owned || r->pins_owned) {
        if (status!=ROUTE_OK) (void)route_fail(r,status);
        else status=route_stop(r);
    }
    route_end_snapshot(r,out);
    out->status=status;out->phase=status==ROUTE_OK && r->quiet?1U:2U;
}
#endif
