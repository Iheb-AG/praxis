/* Stopped counter and software capture through EGR.CC1G; no external input. */
#include "timer_mmio.h"
volatile enum timer_status praxis_timer_status;
volatile uint32_t praxis_timer_captures[2], praxis_timer_completed;
static struct timer_io timer={.read=timer_mmio_read,.write=timer_mmio_write,.barrier=timer_mmio_barrier};
int main(void)
{
    __disable_irq();
    SystemCoreClockUpdate();
    struct timer_plan plan;
    uint32_t value;
    if (!timer_plan(16000000U,1000000U,1000U,0U,&plan)) for (;;) __NOP();
    praxis_timer_status=timer_start(&timer,TIMER_SOFTWARE_CAPTURE,&plan,true);
    if (praxis_timer_status==TIMER_OK) {
        praxis_timer_status=timer_capture(&timer,0x12345678U,64U,&value);
        if (praxis_timer_status==TIMER_OK) praxis_timer_captures[0]=value;
    }
    if (praxis_timer_status==TIMER_OK) {
        praxis_timer_status=timer_capture(&timer,0xFFFFFFFEU,64U,&value);
        if (praxis_timer_status==TIMER_OK) praxis_timer_captures[1]=value;
    }
    if (praxis_timer_status==TIMER_OK) praxis_timer_status=timer_stop(&timer);
    praxis_timer_completed=praxis_timer_status==TIMER_OK && timer.quiet;
    for (;;) __NOP();
}
