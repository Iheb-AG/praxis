/* F407 owned-startup SysTick/SCB subset, PM0214 Rev10 pp39-41,184-185,
 * 225-227,233-234,246-251; RM0090 HSI/CFGR evidence. No hardware qualification.
 * Used unchanged by ARM firmware and the synthetic MMIO effect model.
 */
#ifndef PRAXIS_F407_CORE_CONTROLLER_H
#define PRAXIS_F407_CORE_CONTROLLER_H
#include <stdbool.h>
#include <stdint.h>
#include <stm32f407xx.h>
_Static_assert(__NVIC_PRIO_BITS == 4U, "This reviewed controller targets the F407 priority implementation");

enum core_register {
    CORE_CLOCK, CORE_RCC_CR, CORE_RCC_CFGR, CORE_PRIMASK, CORE_IPSR,
    CORE_CTRL, CORE_LOAD, CORE_VAL, CORE_ICSR, CORE_VTOR, CORE_PRIORITY,
    CORE_VECTOR_SP, CORE_VECTOR_HANDLER, CORE_EXPECT_HANDLER, CORE_REGISTERS
};
enum core_status {
    CORE_OK, CORE_INVALID, CORE_CONTEXT, CORE_CLOCK_ERROR, CORE_BUSY,
    CORE_VECTOR_ERROR, CORE_STATE_ERROR, CORE_TIMEOUT, CORE_NOT_CONFIGURED,
    CORE_RESET_REQUIRED
};
struct core_io {
    uint32_t (*read)(void *, enum core_register);
    void (*write)(void *, enum core_register, uint32_t);
    /* Implement DSB followed by ISB; the host model checks the ordering event. */
    void (*barrier)(void *);
    void *context;
    bool configured, irq, owned, failed, quiet;
    enum core_status failure;
};
#define CORE_FLASH_TABLE 0x08000000UL
#define CORE_STACK_TOP 0x20020000UL
#define CORE_CONTROL_BITS (SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_TICKINT_Msk | SysTick_CTRL_ENABLE_Msk)
#define CORE_HSI_CLOCK_BITS (RCC_CFGR_SW | RCC_CFGR_SWS | RCC_CFGR_HPRE | RCC_CFGR_PPRE1 | RCC_CFGR_PPRE2)

static inline bool core_context(struct core_io *io)
{
    /* Call only in privileged Thread mode with exclusive ownership. PRIMASK=1
     * blocks configurable exceptions, not NMI/HardFault or another bus master.
     */
    return io->read(io->context, CORE_PRIMASK) == 1U &&
           io->read(io->context, CORE_IPSR) == 0U;
}

static inline bool core_period(uint32_t clock_hz, uint32_t tick_hz, uint32_t *reload)
{
    if (!reload || !clock_hz || !tick_hz || clock_hz % tick_hz) return false;
    uint32_t cycles = clock_hz / tick_hz;
    /* LOAD=0 cannot generate a 1->0 transition. Keep all reserved bits zero. */
    if (cycles < 2U || cycles - 1U > SysTick_LOAD_RELOAD_Msk) return false;
    *reload = cycles - 1U;
    return true;
}

static inline enum core_status core_failed(struct core_io *io, enum core_status status)
{
    io->failure = status;
    io->failed = true;
    io->configured = false;
    io->quiet = false;
    if (io->owned) {
        io->write(io->context, CORE_CTRL, 0U);
        io->barrier(io->context);
        io->quiet = (io->read(io->context, CORE_CTRL) & CORE_CONTROL_BITS) == 0U;
        if (io->irq) {
            /* Exact W1 action. RMW could pend NMI/PendSV or write SET+CLR. */
            io->write(io->context, CORE_ICSR, SCB_ICSR_PENDSTCLR_Msk);
            io->barrier(io->context);
            io->quiet = io->quiet &&
                (io->read(io->context, CORE_ICSR) & SCB_ICSR_PENDSTSET_Msk) == 0U;
        }
    }
    return status; /* Never retry automatically, even if shutdown readback succeeds. */
}

static inline enum core_status core_flash_vector(struct core_io *io, uint32_t address,
                                                 bool startup_owned)
{
    if (!io || !io->read || !io->write || !io->barrier || !startup_owned ||
            address != CORE_FLASH_TABLE || (address & 511U)) return CORE_INVALID;
    if (io->failed) return CORE_RESET_REQUIRED;
    if (io->configured || io->owned) return CORE_BUSY;
    if (!core_context(io)) return CORE_CONTEXT;
    if (io->read(io->context, CORE_CTRL) &
            (SysTick_CTRL_ENABLE_Msk | SysTick_CTRL_TICKINT_Msk)) return CORE_BUSY;
    uint32_t handler = io->read(io->context, CORE_VECTOR_HANDLER);
    if (io->read(io->context, CORE_VECTOR_SP) != CORE_STACK_TOP || !(handler & 1U) ||
            (handler & ~1UL) < CORE_FLASH_TABLE ||
            (handler & ~1UL) >= CORE_FLASH_TABLE + 0x100000UL ||
            handler != io->read(io->context, CORE_EXPECT_HANDLER)) return CORE_VECTOR_ERROR;
    /* Device operating mask is stricter than the shared CMSIS TBLOFF envelope.
     * Fixed approved table only; no arbitrary relocation, handoff or MSP change.
     */
    io->write(io->context, CORE_VTOR, address);
    io->barrier(io->context);
    if (io->read(io->context, CORE_VTOR) != address)
        return core_failed(io, CORE_VECTOR_ERROR);
    return CORE_OK;
}

static inline enum core_status core_start(struct core_io *io, uint32_t tick_hz,
                                         uint32_t priority, bool irq, bool startup_owned)
{
    uint32_t reload;
    if (!io || !io->read || !io->write || !io->barrier || !startup_owned ||
            priority > 15U || !core_period(16000000U, tick_hz, &reload)) return CORE_INVALID;
    if (io->failed) return CORE_RESET_REQUIRED;
    if (io->configured || io->owned) return CORE_BUSY;
    if (!core_context(io)) return CORE_CONTEXT;
    if (io->read(io->context, CORE_CLOCK) != 16000000U ||
            (io->read(io->context, CORE_RCC_CR) & (RCC_CR_HSION | RCC_CR_HSIRDY)) !=
                (RCC_CR_HSION | RCC_CR_HSIRDY) ||
            (io->read(io->context, CORE_RCC_CFGR) & CORE_HSI_CLOCK_BITS)) return CORE_CLOCK_ERROR;
    /* Polling never installs an IRQ handler or clears SCB pending state. Refuse
     * a pre-existing pending exception before touching the timer; TICKINT=0 or
     * writing VAL is not evidence that the pending exception is gone.
     */
    if (!irq && (io->read(io->context, CORE_ICSR) & SCB_ICSR_PENDSTSET_Msk)) return CORE_BUSY;
    /* Reading CTRL clears COUNTFLAG, even on the busy path. The caller must
     * establish ownership BEFORE this inspection; it is not a passive probe.
     */
    if (io->read(io->context, CORE_CTRL) &
            (SysTick_CTRL_ENABLE_Msk | SysTick_CTRL_TICKINT_Msk)) return CORE_BUSY;
    if (irq) {
        enum core_status status = core_flash_vector(io, CORE_FLASH_TABLE, true);
        if (status != CORE_OK) return status;
        io->write(io->context, CORE_PRIORITY, priority << (8U - __NVIC_PRIO_BITS));
        if (io->read(io->context, CORE_PRIORITY) != priority << (8U - __NVIC_PRIO_BITS))
            return core_failed(io, CORE_STATE_ERROR);
    }
    io->irq = irq;
    io->owned = true;
    io->write(io->context, CORE_CTRL, 0U);
    io->write(io->context, CORE_LOAD, reload);
    if (io->read(io->context, CORE_LOAD) != reload) return core_failed(io, CORE_STATE_ERROR);
    io->write(io->context, CORE_VAL, 0U); /* Clears current AND COUNTFLAG, not pending exception. */
    if (io->read(io->context, CORE_VAL) != 0U) return core_failed(io, CORE_STATE_ERROR);
    if (irq) {
        io->write(io->context, CORE_ICSR, SCB_ICSR_PENDSTCLR_Msk);
        io->barrier(io->context);
        if (io->read(io->context, CORE_ICSR) & SCB_ICSR_PENDSTSET_Msk)
            return core_failed(io, CORE_STATE_ERROR);
    }
    uint32_t control = SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_ENABLE_Msk |
                       (irq ? SysTick_CTRL_TICKINT_Msk : 0U);
    /* Handler/software state must already be ready; source enable is last.
     * The caller retains PRIMASK=1 and decides when to restore global masking.
     */
    io->write(io->context, CORE_CTRL, control);
    io->barrier(io->context);
    if ((io->read(io->context, CORE_CTRL) & CORE_CONTROL_BITS) != control)
        return core_failed(io, CORE_STATE_ERROR);
    io->configured = true;
    io->quiet = false;
    return CORE_OK;
}

static inline enum core_status core_poll_event(struct core_io *io, uint32_t budget)
{
    if (!io || !io->read || !io->write || !io->barrier || !budget) return CORE_INVALID;
    if (io->failed) return CORE_RESET_REQUIRED;
    if (!io->configured || !io->owned || io->irq) return CORE_NOT_CONFIGURED;
    if (!core_context(io)) return CORE_CONTEXT;
    uint32_t expected = SysTick_CTRL_CLKSOURCE_Msk | SysTick_CTRL_ENABLE_Msk;
    uint32_t control = io->read(io->context, CORE_CTRL); /* Drain stale COUNTFLAG. */
    if ((control & CORE_CONTROL_BITS) != expected) return core_failed(io, CORE_STATE_ERROR);
    for (uint32_t n = 0; n < budget; ++n) {
        control = io->read(io->context, CORE_CTRL);
        if ((control & CORE_CONTROL_BITS) != expected) return core_failed(io, CORE_STATE_ERROR);
        if (control & SysTick_CTRL_COUNTFLAG_Msk) return CORE_OK;
    }
    return core_failed(io, CORE_TIMEOUT);
}

static inline bool core_stop(struct core_io *io)
{
    if (!io || !io->read || !io->write || !io->barrier || !io->owned ||
            !io->configured || io->failed || !core_context(io)) return false;
    io->write(io->context, CORE_CTRL, 0U);
    io->barrier(io->context);
    if (io->read(io->context, CORE_CTRL) & CORE_CONTROL_BITS) {
        (void)core_failed(io, CORE_STATE_ERROR); return false;
    }
    if (io->irq) {
        io->write(io->context, CORE_ICSR, SCB_ICSR_PENDSTCLR_Msk);
        io->barrier(io->context);
        if (io->read(io->context, CORE_ICSR) & SCB_ICSR_PENDSTSET_Msk) {
            (void)core_failed(io, CORE_STATE_ERROR); return false;
        }
    }
    io->configured = false;
    io->owned = false;
    io->quiet = true;
    return true;
}
#endif
