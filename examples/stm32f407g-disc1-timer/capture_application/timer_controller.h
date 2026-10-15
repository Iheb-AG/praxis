/* F407 TIM2 owned-startup internal PWM reference / software capture.
 * Source: RM0090 Rev22 pp604,607-608,624-639; reviewed/timer-modes-v1.
 * Hardware-specific example code, not a vendor branch in the compiler.
 */
#ifndef PRAXIS_F407_TIMER_CONTROLLER_H
#define PRAXIS_F407_TIMER_CONTROLLER_H
#include <stdbool.h>
#include <stdint.h>
#include <stm32f407xx.h>

enum timer_register {
    T_CLOCK, T_RCC_CR, T_CFGR, T_GATE, T_RESET, T_APB2, T_PRIMASK, T_IPSR,
    T_CR1, T_CR2, T_SMCR, T_DIER, T_SR, T_EGR, T_CCMR1, T_CCER,
    T_CNT, T_PSC, T_ARR, T_CCR1, T_REGISTERS
};
enum timer_status {
    TIMER_OK, TIMER_INVALID, TIMER_CONTEXT, TIMER_CLOCK, TIMER_BUSY,
    TIMER_STATE, TIMER_TIMEOUT, TIMER_STALE, TIMER_OVERCAPTURE, TIMER_RESET_REQUIRED
};
enum timer_mode { TIMER_NONE, TIMER_PWM_REFERENCE, TIMER_SOFTWARE_CAPTURE };
struct timer_plan { uint32_t clock, prescaler, period, high; };
struct timer_io {
    uint32_t (*read)(void *, enum timer_register);
    void (*write)(void *, enum timer_register, uint32_t);
    void (*barrier)(void *);
    void *context;
    bool owned, clocked, configured, failed, quiet;
    enum timer_mode mode;
    uint32_t period, last_status;
};
#define TIMER_CLOCK_BITS (RCC_CFGR_SW | RCC_CFGR_SWS | RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2)
#define TIMER_PWM_CCMR ((6UL << TIM_CCMR1_OC1M_Pos) | TIM_CCMR1_OC1PE)
#define TIMER_CAPTURE_CCMR (3UL << TIM_CCMR1_CC1S_Pos)
#define TIMER_POLL_LIMIT 1000000UL

static inline bool timer_plan(uint32_t clock, uint32_t tick, uint32_t period,
                              uint32_t high, struct timer_plan *out)
{
    if (!out || !clock || !tick || clock % tick || clock / tick > 65536U ||
            period < 2U || high > period) return false;
    *out = (struct timer_plan){clock, clock / tick - 1U, period, high};
    return true;
}
static inline bool timer_interface(struct timer_io *io)
{
    return io && io->read && io->write && io->barrier;
}
static inline bool timer_context(struct timer_io *io)
{
    return io->read(io->context,T_PRIMASK)==1U && io->read(io->context,T_IPSR)==0U;
}
static inline bool timer_clock(struct timer_io *io)
{
    return io->read(io->context,T_CLOCK)==16000000U &&
        (io->read(io->context,T_RCC_CR)&(RCC_CR_HSION|RCC_CR_HSIRDY))==(RCC_CR_HSION|RCC_CR_HSIRDY) &&
        !(io->read(io->context,T_CFGR)&TIMER_CLOCK_BITS) &&
        !(io->read(io->context,T_APB2)&RCC_APB2ENR_TIM1EN);
}
static inline bool timer_quiesce(struct timer_io *io)
{
    io->write(io->context,T_DIER,0U);
    io->write(io->context,T_CCER,0U);
    io->write(io->context,T_CR1,0U);
    io->barrier(io->context);
    return io->read(io->context,T_DIER)==0U && io->read(io->context,T_CCER)==0U &&
        io->read(io->context,T_CR1)==0U;
}
static inline enum timer_status timer_fail(struct timer_io *io, enum timer_status reason)
{
    io->failed=true;
    io->configured=false;
    io->quiet=io->clocked && timer_quiesce(io);
    return reason; /* A failure is latched; do not turn cleanup into success or retry. */
}
static inline enum timer_status timer_live(struct timer_io *io, enum timer_mode mode)
{
    if (!timer_interface(io)) return TIMER_INVALID;
    if (io->failed) return TIMER_RESET_REQUIRED;
    if (!io->configured || io->mode!=mode) return TIMER_INVALID;
    if (!timer_context(io)) return TIMER_CONTEXT;
    if (!(io->read(io->context,T_GATE)&RCC_APB1ENR_TIM2EN)) {
        io->clocked=false; /* No timer access is permitted after gate loss. */
        return timer_fail(io,TIMER_CLOCK);
    }
    if (!timer_clock(io)) return timer_fail(io,TIMER_CLOCK);
    return TIMER_OK;
}
static inline enum timer_status timer_start(struct timer_io *io, enum timer_mode mode,
                                           const struct timer_plan *plan, bool startup_owned)
{
    /* Caller owns TIM2 and its downstream TRGO consumers. TIM1 stays gated to
     * keep TIM2 ITR0/TRC free of incoming events. No GPIO configuration occurs.
     */
    if (!timer_interface(io) || !startup_owned || !plan || plan->clock!=16000000U ||
            plan->prescaler>65535U || plan->period<2U || plan->high>plan->period ||
            (mode!=TIMER_PWM_REFERENCE && mode!=TIMER_SOFTWARE_CAPTURE)) return TIMER_INVALID;
    if (io->failed) return TIMER_RESET_REQUIRED;
    if (io->owned || io->configured) return TIMER_BUSY;
    if (!timer_context(io)) return TIMER_CONTEXT;
    if (!timer_clock(io)) return TIMER_CLOCK;
    uint32_t gate=io->read(io->context,T_GATE), reset=io->read(io->context,T_RESET);
    if ((gate&RCC_APB1ENR_TIM2EN) || (reset&RCC_APB1RSTR_TIM2RST)) return TIMER_BUSY;
    io->owned=true;
    io->write(io->context,T_GATE,gate|RCC_APB1ENR_TIM2EN);
    io->barrier(io->context);
    if (io->read(io->context,T_GATE)!=(gate|RCC_APB1ENR_TIM2EN)) return timer_fail(io,TIMER_STATE);
    io->clocked=true;
    io->write(io->context,T_RESET,reset|RCC_APB1RSTR_TIM2RST);
    io->barrier(io->context);
    if (io->read(io->context,T_RESET)!=(reset|RCC_APB1RSTR_TIM2RST)) return timer_fail(io,TIMER_STATE);
    io->write(io->context,T_RESET,reset);
    io->barrier(io->context);
    if (io->read(io->context,T_RESET)!=reset) {
        io->clocked=false; /* Held reset cannot provide a meaningful quiet readback. */
        return timer_fail(io,TIMER_STATE);
    }
    if (!timer_quiesce(io)) return timer_fail(io,TIMER_STATE);
    io->write(io->context,T_CR2,0U);
    io->write(io->context,T_SMCR,0U); /* SMS=0, ECE=0, TS=ITR0 (TIM1_TRGO). */
    io->write(io->context,T_CCMR1,mode==TIMER_PWM_REFERENCE?TIMER_PWM_CCMR:TIMER_CAPTURE_CCMR);
    io->barrier(io->context);
    if (io->read(io->context,T_CCMR1)!=(mode==TIMER_PWM_REFERENCE?TIMER_PWM_CCMR:TIMER_CAPTURE_CCMR))
        return timer_fail(io,TIMER_STATE); /* Check direction before any CCR1 write. */
    io->write(io->context,T_PSC,plan->prescaler);
    io->write(io->context,T_ARR,mode==TIMER_PWM_REFERENCE?plan->period-1U:UINT32_MAX);
    io->write(io->context,T_CNT,0U);
    if (mode==TIMER_PWM_REFERENCE) {
        io->write(io->context,T_CR1,TIM_CR1_ARPE);
        io->write(io->context,T_CCR1,plan->high);
    }
    io->write(io->context,T_EGR,TIM_EGR_UG); /* Action register: never RMW. */
    io->write(io->context,T_SR,0U); /* rc_w0; exclusive timer, all events discarded. */
    io->barrier(io->context);
    if (io->read(io->context,T_CR2)!=0U || io->read(io->context,T_SMCR)!=0U ||
            io->read(io->context,T_DIER)!=0U || io->read(io->context,T_CCER)!=0U ||
            io->read(io->context,T_CCMR1)!=(mode==TIMER_PWM_REFERENCE?TIMER_PWM_CCMR:TIMER_CAPTURE_CCMR) ||
            io->read(io->context,T_PSC)!=plan->prescaler ||
            io->read(io->context,T_ARR)!=(mode==TIMER_PWM_REFERENCE?plan->period-1U:UINT32_MAX) ||
            io->read(io->context,T_CR1)!=(mode==TIMER_PWM_REFERENCE?TIM_CR1_ARPE:0U) ||
            io->read(io->context,T_SR)!=0U) return timer_fail(io,TIMER_STATE);
    if (mode==TIMER_PWM_REFERENCE && io->read(io->context,T_CCR1)!=plan->high)
        return timer_fail(io,TIMER_STATE);
    /* PWM reference only: CC1E remains zero. Capture: counter remains stopped,
     * input maps to TRC/ITR0; events will be issued explicitly through CC1G.
     */
    io->write(io->context,mode==TIMER_PWM_REFERENCE?T_CR1:T_CCER,
        mode==TIMER_PWM_REFERENCE?(TIM_CR1_ARPE|TIM_CR1_CEN):TIM_CCER_CC1E);
    io->barrier(io->context);
    if (io->read(io->context,T_CR1)!=(mode==TIMER_PWM_REFERENCE?(TIM_CR1_ARPE|TIM_CR1_CEN):0U) ||
            io->read(io->context,T_CCER)!=(mode==TIMER_PWM_REFERENCE?0U:TIM_CCER_CC1E))
        return timer_fail(io,TIMER_STATE);
    io->mode=mode; io->period=plan->period; io->configured=true; io->quiet=false;
    return TIMER_OK;
}
static inline enum timer_status timer_pwm_set(struct timer_io *io, uint32_t high)
{
    if (!timer_interface(io) || high>io->period) return TIMER_INVALID;
    enum timer_status result=timer_live(io,TIMER_PWM_REFERENCE);
    if (result!=TIMER_OK) return result;
    if (io->read(io->context,T_CR1)!=(TIM_CR1_ARPE|TIM_CR1_CEN) ||
            io->read(io->context,T_CCMR1)!=TIMER_PWM_CCMR || io->read(io->context,T_CCER)!=0U ||
            io->read(io->context,T_DIER)!=0U) return timer_fail(io,TIMER_STATE);
    io->write(io->context,T_CCR1,high);
    io->barrier(io->context);
    if (io->read(io->context,T_CCR1)!=high) return timer_fail(io,TIMER_STATE);
    return TIMER_OK; /* Readback is the preload, not proof of active duty. */
}
static inline enum timer_status timer_wait_update(struct timer_io *io, uint32_t budget)
{
    if (!budget || budget>TIMER_POLL_LIMIT) return TIMER_INVALID;
    enum timer_status result=timer_live(io,TIMER_PWM_REFERENCE);
    if (result!=TIMER_OK) return result;
    io->write(io->context,T_SR,0U); /* Discard stale UIF; wait for a new event. */
    io->barrier(io->context);
    for (uint32_t i=0U;i<budget;++i) {
        if (io->read(io->context,T_SR)&TIM_SR_UIF) return TIMER_OK;
    }
    return timer_fail(io,TIMER_TIMEOUT);
}
static inline enum timer_status timer_capture(struct timer_io *io, uint32_t counter,
                                              uint32_t budget, uint32_t *out)
{
    if (!out || !budget || budget>TIMER_POLL_LIMIT) return TIMER_INVALID;
    enum timer_status result=timer_live(io,TIMER_SOFTWARE_CAPTURE);
    if (result!=TIMER_OK) return result;
    if (io->read(io->context,T_CR1)!=0U || io->read(io->context,T_SMCR)!=0U ||
            io->read(io->context,T_CCMR1)!=TIMER_CAPTURE_CCMR ||
            io->read(io->context,T_CCER)!=TIM_CCER_CC1E || io->read(io->context,T_DIER)!=0U)
        return timer_fail(io,TIMER_STATE);
    io->last_status=io->read(io->context,T_SR);
    if (io->last_status&(TIM_SR_CC1IF|TIM_SR_CC1OF)) return timer_fail(io,TIMER_STALE);
    io->write(io->context,T_CNT,counter);
    io->barrier(io->context);
    if (io->read(io->context,T_CNT)!=counter) return timer_fail(io,TIMER_STATE);
    io->write(io->context,T_EGR,TIM_EGR_CC1G);
    io->barrier(io->context);
    for (uint32_t i=0U;i<budget;++i) {
        uint32_t status=io->read(io->context,T_SR);
        if (status&(TIM_SR_CC1IF|TIM_SR_CC1OF)) {
            uint32_t captured=io->read(io->context,T_CCR1); /* Clears CC1IF in input mode. */
            io->last_status=status|io->read(io->context,T_SR); /* Data before final overcapture check. */
            if ((io->last_status&TIM_SR_CC1OF) || (io->read(io->context,T_SR)&TIM_SR_CC1IF))
                return timer_fail(io,TIMER_OVERCAPTURE);
            if (!(status&TIM_SR_CC1IF) || captured!=counter) return timer_fail(io,TIMER_STATE);
            *out=captured; /* Publish only a checked, non-overcaptured sample. */
            return TIMER_OK;
        }
    }
    return timer_fail(io,TIMER_TIMEOUT);
}
static inline enum timer_status timer_stop(struct timer_io *io)
{
    if (!timer_interface(io)) return TIMER_INVALID;
    if (io->failed) return TIMER_RESET_REQUIRED;
    if (!io->configured || !timer_context(io)) return TIMER_CONTEXT;
    if (!(io->read(io->context,T_GATE)&RCC_APB1ENR_TIM2EN)) {
        io->clocked=false; return timer_fail(io,TIMER_CLOCK);
    }
    io->configured=false;
    io->quiet=timer_quiesce(io);
    return io->quiet?TIMER_OK:timer_fail(io,TIMER_STATE);
}
#endif
