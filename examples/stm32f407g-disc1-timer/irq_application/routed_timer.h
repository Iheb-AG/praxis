/* Reviewed MB997-E-01 PA1/TIM2_CH2 -> external jumper -> PA2/TIM5_CH3.
 * RM0090 Rev22 GPIO/timer semantics; DS8626 Rev12 AF1/AF2/package rows.
 * This is target-specific firmware example code, not compiler policy.
 */
#ifndef PRAXIS_ROUTED_TIMER_H
#define PRAXIS_ROUTED_TIMER_H
#include "timer_controller.h" /* Reuse the existing checked integer plan. */
enum route_register {
    R_CLOCK,R_RCC_CR,R_CFGR,R_AHB1,R_APB1,R_RESET,R_APB2,R_PRIMASK,R_IPSR,
    R_MODER,R_OTYPER,R_SPEED,R_PULL,R_AFRL,R_BSRR,R_LOCK,
    R_CR1,R_CR2,R_SMCR,R_DIER,R_SR,R_EGR,R_CCMR1,R_CCER,R_CNT,R_PSC,R_ARR,R_CCR2,
    C_CR1,C_CR2,C_SMCR,C_DIER,C_SR,C_EGR,C_CCMR2,C_CCER,C_CNT,C_PSC,C_ARR,C_CCR3,
    R_REGISTERS
};
enum route_status {
    ROUTE_OK,ROUTE_INVALID,ROUTE_CONTEXT,ROUTE_CLOCK,ROUTE_BUSY,
    ROUTE_STATE,ROUTE_TIMEOUT,ROUTE_OVERCAPTURE,ROUTE_RESET_REQUIRED
};
struct route_io {
    uint32_t (*read)(void *,enum route_register);
    void (*write)(void *,enum route_register,uint32_t);
    void (*barrier)(void *);
    void *context;
    bool owned,pins_owned,configured,failed,timer_quiet,pins_quiet,quiet;
};
#define ROUTE_PINS ((1UL<<1U)|(1UL<<2U))
#define ROUTE_MODE_MASK ((3UL<<2U)|(3UL<<4U))
#define ROUTE_AF_MODE ((2UL<<2U)|(2UL<<4U))
#define ROUTE_AF_MASK ((15UL<<4U)|(15UL<<8U))
#define ROUTE_AF ((1UL<<4U)|(2UL<<8U))
#define ROUTE_PULL (2UL<<4U)
#define ROUTE_PWM ((6UL<<TIM_CCMR1_OC2M_Pos)|TIM_CCMR1_OC2PE)
#define ROUTE_CAPTURE (1UL<<TIM_CCMR2_CC3S_Pos)
#define ROUTE_CHANNELS TIM_CCER_CC2E
#define ROUTE_TIMER_GATES (RCC_APB1ENR_TIM2EN|RCC_APB1ENR_TIM5EN)
#define ROUTE_TIMER_RESETS (RCC_APB1RSTR_TIM2RST|RCC_APB1RSTR_TIM5RST)

static inline bool route_interface(struct route_io *io)
{ return io && io->read && io->write && io->barrier; }
static inline bool route_context(struct route_io *io)
{ return io->read(io->context,R_PRIMASK)==1U && io->read(io->context,R_IPSR)==0U; }
static inline bool route_clock(struct route_io *io)
{
    return io->read(io->context,R_CLOCK)==16000000U &&
        (io->read(io->context,R_RCC_CR)&(RCC_CR_HSION|RCC_CR_HSIRDY))==(RCC_CR_HSION|RCC_CR_HSIRDY) &&
        !(io->read(io->context,R_CFGR)&TIMER_CLOCK_BITS);
}
static inline void route_quiesce(struct route_io *io)
{
    io->timer_quiet=false;io->pins_quiet=false;
    if (io->owned) {
        uint32_t gates=io->read(io->context,R_APB1),resets=io->read(io->context,R_RESET);
        bool pwm=false,capture=false;
        if ((gates&RCC_APB1ENR_TIM2EN) && !(resets&RCC_APB1RSTR_TIM2RST)) {
            io->write(io->context,R_CCER,0U);io->write(io->context,R_DIER,0U);io->write(io->context,R_CR1,0U);
            io->barrier(io->context);
            pwm=io->read(io->context,R_CCER)==0U && io->read(io->context,R_DIER)==0U && io->read(io->context,R_CR1)==0U;
        }
        if ((gates&RCC_APB1ENR_TIM5EN) && !(resets&RCC_APB1RSTR_TIM5RST)) {
            io->write(io->context,C_CCER,0U);io->write(io->context,C_DIER,0U);io->write(io->context,C_CR1,0U);
            io->barrier(io->context);
            capture=io->read(io->context,C_CCER)==0U && io->read(io->context,C_DIER)==0U && io->read(io->context,C_CR1)==0U;
        }
        io->timer_quiet=pwm && capture;
    }
    if (io->pins_owned && (io->read(io->context,R_AHB1)&RCC_AHB1ENR_GPIOAEN)) {
        uint32_t mode=io->read(io->context,R_MODER);
        io->write(io->context,R_MODER,mode&~ROUTE_MODE_MASK);
        io->barrier(io->context);
        io->pins_quiet=(io->read(io->context,R_MODER)&ROUTE_MODE_MASK)==0U;
    }
    io->quiet=io->timer_quiet && io->pins_quiet;
}
static inline enum route_status route_fail(struct route_io *io,enum route_status result)
{
    io->failed=true;io->configured=false;route_quiesce(io);
    return result;
}
static inline enum route_status route_prepare(struct route_io *io,const struct timer_plan *plan,
                                           bool startup_owned,bool wiring_owned)
{
    /* wiring_owned means ONLY the reviewed passive PA1-to-PA2 jumper is fitted;
     * other attachments and USART2/ADC/Ethernet/other GPIO owners are excluded.
     * It is an integration precondition, not an electrical auto-detection.
     */
    if (!route_interface(io) || !startup_owned || !wiring_owned || !plan ||
            plan->clock!=16000000U || plan->prescaler>65535U ||
            plan->period<2U || !plan->high || plan->high>=plan->period) return ROUTE_INVALID;
    if (io->failed) return ROUTE_RESET_REQUIRED;
    if (io->owned || io->pins_owned || io->configured) return ROUTE_BUSY;
    if (!route_context(io)) return ROUTE_CONTEXT;
    if (!route_clock(io)) return ROUTE_CLOCK;
    uint32_t apb=io->read(io->context,R_APB1),reset=io->read(io->context,R_RESET);
    if ((apb&ROUTE_TIMER_GATES)||(reset&ROUTE_TIMER_RESETS)) return ROUTE_BUSY;
    uint32_t ahb=io->read(io->context,R_AHB1);
    io->write(io->context,R_AHB1,ahb|RCC_AHB1ENR_GPIOAEN);
    io->barrier(io->context);
    if (io->read(io->context,R_AHB1)!=(ahb|RCC_AHB1ENR_GPIOAEN)) return route_fail(io,ROUTE_STATE);
    uint32_t mode=io->read(io->context,R_MODER);
    if ((mode&ROUTE_MODE_MASK) || (io->read(io->context,R_LOCK)&ROUTE_PINS)) return ROUTE_BUSY;
    io->pins_owned=true;
    io->write(io->context,R_APB1,apb|ROUTE_TIMER_GATES);
    io->barrier(io->context);
    if (io->read(io->context,R_APB1)!=(apb|ROUTE_TIMER_GATES)) return route_fail(io,ROUTE_STATE);
    io->owned=true;
    io->write(io->context,R_RESET,reset|ROUTE_TIMER_RESETS);
    io->barrier(io->context);
    if (io->read(io->context,R_RESET)!=(reset|ROUTE_TIMER_RESETS)) return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_RESET,reset);
    io->barrier(io->context);
    if (io->read(io->context,R_RESET)!=reset) return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_CCER,0U);io->write(io->context,R_DIER,0U);io->write(io->context,R_CR1,0U);
    io->barrier(io->context);
    if (io->read(io->context,R_CCER)||io->read(io->context,R_DIER)||io->read(io->context,R_CR1))
        return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_CR2,0U);io->write(io->context,R_SMCR,0U);
    io->write(io->context,C_CCER,0U);io->write(io->context,C_DIER,0U);io->write(io->context,C_CR1,0U);
    io->write(io->context,C_CR2,0U);io->write(io->context,C_SMCR,0U);
    io->write(io->context,R_CCMR1,ROUTE_PWM);io->write(io->context,C_CCMR2,ROUTE_CAPTURE);
    io->barrier(io->context);
    if (io->read(io->context,R_CCMR1)!=ROUTE_PWM || io->read(io->context,C_CCMR2)!=ROUTE_CAPTURE)
        return route_fail(io,ROUTE_STATE); /* Check output direction before CCR2 write. */
    io->write(io->context,R_PSC,plan->prescaler);
    io->write(io->context,R_ARR,plan->period-1U);io->write(io->context,R_CCR2,plan->high);
    io->write(io->context,R_CNT,0U);io->write(io->context,R_CR1,TIM_CR1_ARPE);
    io->write(io->context,R_EGR,TIM_EGR_UG);io->write(io->context,R_SR,0U);
    io->write(io->context,C_PSC,plan->prescaler);io->write(io->context,C_ARR,UINT32_MAX);io->write(io->context,C_CNT,0U);
    io->write(io->context,C_EGR,TIM_EGR_UG);io->write(io->context,C_SR,0U);
    io->barrier(io->context);
    if (io->read(io->context,R_PSC)!=plan->prescaler || io->read(io->context,R_ARR)!=plan->period-1U ||
            io->read(io->context,R_CCR2)!=plan->high || io->read(io->context,R_CR2) ||
            io->read(io->context,R_SMCR) || io->read(io->context,R_SR) ||
            io->read(io->context,R_CR1)!=TIM_CR1_ARPE || io->read(io->context,C_CR1) ||
            io->read(io->context,C_CR2) || io->read(io->context,C_SMCR) || io->read(io->context,C_DIER) ||
            io->read(io->context,C_CCER) || io->read(io->context,C_SR) ||
            io->read(io->context,C_PSC)!=plan->prescaler || io->read(io->context,C_ARR)!=UINT32_MAX) return route_fail(io,ROUTE_STATE);
    /* Never reset GPIOA: preserve SWD, USER and unrelated pin settings. */
    io->write(io->context,R_BSRR,1UL<<(1U+16U));
    uint32_t type=io->read(io->context,R_OTYPER),speed=io->read(io->context,R_SPEED);
    uint32_t pull=io->read(io->context,R_PULL),af=io->read(io->context,R_AFRL);
    io->write(io->context,R_OTYPER,type&~ROUTE_PINS);
    io->write(io->context,R_SPEED,speed&~ROUTE_MODE_MASK);
    io->write(io->context,R_PULL,(pull&~ROUTE_MODE_MASK)|ROUTE_PULL);
    io->write(io->context,R_AFRL,(af&~ROUTE_AF_MASK)|ROUTE_AF);
    io->barrier(io->context);
    if (io->read(io->context,R_OTYPER)!=(type&~ROUTE_PINS) ||
            io->read(io->context,R_SPEED)!=(speed&~ROUTE_MODE_MASK) ||
            io->read(io->context,R_PULL)!=((pull&~ROUTE_MODE_MASK)|ROUTE_PULL) ||
            io->read(io->context,R_AFRL)!=((af&~ROUTE_AF_MASK)|ROUTE_AF)) return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_MODER,(mode&~ROUTE_MODE_MASK)|ROUTE_AF_MODE);
    io->barrier(io->context);
    if (io->read(io->context,R_MODER)!=((mode&~ROUTE_MODE_MASK)|ROUTE_AF_MODE))
        return route_fail(io,ROUTE_STATE);
    io->configured=true;return ROUTE_OK;
}
static inline enum route_status route_start(struct route_io *io,const struct timer_plan *plan,
                                           bool startup_owned,bool wiring_owned)
{
    enum route_status prepared=route_prepare(io,plan,startup_owned,wiring_owned);
    if (prepared!=ROUTE_OK) return prepared;
    io->write(io->context,C_CCER,TIM_CCER_CC3E); /* Start the independent capture timebase first. */
    io->barrier(io->context);
    if (io->read(io->context,C_CCER)!=TIM_CCER_CC3E) return route_fail(io,ROUTE_STATE);
    io->write(io->context,C_CR1,TIM_CR1_CEN);
    io->barrier(io->context);
    if (io->read(io->context,C_CCER)!=TIM_CCER_CC3E || io->read(io->context,C_CR1)!=TIM_CR1_CEN) return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_CCER,ROUTE_CHANNELS);
    io->barrier(io->context);
    if (io->read(io->context,R_CCER)!=ROUTE_CHANNELS) return route_fail(io,ROUTE_STATE);
    io->write(io->context,R_CR1,TIM_CR1_ARPE|TIM_CR1_CEN);
    io->barrier(io->context);
    if (io->read(io->context,R_CCER)!=ROUTE_CHANNELS ||
            io->read(io->context,R_CR1)!=(TIM_CR1_ARPE|TIM_CR1_CEN)) return route_fail(io,ROUTE_STATE);
    io->configured=true;return ROUTE_OK;
}
static inline enum route_status route_capture(struct route_io *io,uint32_t budget,uint32_t *out)
{
    if (!route_interface(io)||!out||!budget||budget>TIMER_POLL_LIMIT) return ROUTE_INVALID;
    if (io->failed) return ROUTE_RESET_REQUIRED;
    if (!io->configured) return ROUTE_INVALID;
    if (!route_context(io)) return ROUTE_CONTEXT;
    if (!route_clock(io) || !(io->read(io->context,R_AHB1)&RCC_AHB1ENR_GPIOAEN) ||
            (io->read(io->context,R_APB1)&ROUTE_TIMER_GATES)!=ROUTE_TIMER_GATES) return route_fail(io,ROUTE_CLOCK);
    if (io->read(io->context,R_CCER)!=ROUTE_CHANNELS || io->read(io->context,R_CCMR1)!=ROUTE_PWM ||
            io->read(io->context,C_CCMR2)!=ROUTE_CAPTURE || io->read(io->context,R_DIER) ||
            io->read(io->context,C_DIER) || io->read(io->context,C_CR1)!=TIM_CR1_CEN ||
            io->read(io->context,C_CCER)!=TIM_CCER_CC3E ||
            io->read(io->context,R_CR1)!=(TIM_CR1_ARPE|TIM_CR1_CEN) ||
            (io->read(io->context,R_MODER)&ROUTE_MODE_MASK)!=ROUTE_AF_MODE ||
            (io->read(io->context,R_AFRL)&ROUTE_AF_MASK)!=ROUTE_AF) return route_fail(io,ROUTE_STATE);
    for (uint32_t i=0U;i<budget;++i) {
        uint32_t before=io->read(io->context,C_SR);
        if (before&(TIM_SR_CC3IF|TIM_SR_CC3OF)) {
            uint32_t value=io->read(io->context,C_CCR3); /* Input read clears CC3IF. */
            uint32_t after=io->read(io->context,C_SR);
            if (((before|after)&TIM_SR_CC3OF)||(after&TIM_SR_CC3IF)) return route_fail(io,ROUTE_OVERCAPTURE);
            if (!(before&TIM_SR_CC3IF)) return route_fail(io,ROUTE_STATE);
            *out=value;return ROUTE_OK;
        }
    }
    return route_fail(io,ROUTE_TIMEOUT);
}
static inline bool route_period(uint32_t before,uint32_t after,uint32_t period,uint32_t margin)
{
    /* TIM5 free-runs over the complete 32-bit range, independently of PWM ARR.
     * This tests counter ticks, not calibrated real-world frequency.
     */
    if (period<2U || margin>=period) return false;
    uint32_t elapsed=after-before;
    return (uint64_t)elapsed+margin>=period && (uint64_t)elapsed<=(uint64_t)period+margin;
}
static inline enum route_status route_stop(struct route_io *io)
{
    if (!route_interface(io)) return ROUTE_INVALID;
    if (io->failed) return ROUTE_RESET_REQUIRED;
    if (!io->configured || !route_context(io)) return ROUTE_CONTEXT;
    io->configured=false;route_quiesce(io);
    return io->quiet?ROUTE_OK:route_fail(io,ROUTE_STATE);
}
#endif
