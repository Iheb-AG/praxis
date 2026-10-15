/* Internal OC1REF configuration only: no GPIO changes and CC1E stays disabled. */
#include "timer_mmio.h"
volatile enum timer_status praxis_timer_status;
volatile uint32_t praxis_timer_completed;
static struct timer_io timer={.read=timer_mmio_read,.write=timer_mmio_write,.barrier=timer_mmio_barrier};
int main(void)
{
    __disable_irq();
    SystemCoreClockUpdate();
    struct timer_plan plan;
    if (!timer_plan(16000000U,1000000U,1000U,250U,&plan)) for (;;) __NOP();
    praxis_timer_status=timer_start(&timer,TIMER_PWM_REFERENCE,&plan,true);
    if (praxis_timer_status==TIMER_OK) praxis_timer_status=timer_wait_update(&timer,100000U);
    if (praxis_timer_status==TIMER_OK) praxis_timer_status=timer_pwm_set(&timer,750U);
    if (praxis_timer_status==TIMER_OK) praxis_timer_status=timer_wait_update(&timer,100000U);
    if (praxis_timer_status==TIMER_OK) praxis_timer_status=timer_stop(&timer);
    praxis_timer_completed=praxis_timer_status==TIMER_OK && timer.quiet;
    for (;;) __NOP();
}
