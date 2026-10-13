/* Compile-only controller example; no pin/target-device inference or bus scan.
 * Provenance and limits: matching I2C bundle, reviewed/i2c-v1/i2c.md.
 */
#include "clock_setup.h"
#include "i2c_controller.h"

_Static_assert(offsetof(I2C_TypeDef, CR1) == 0x00U, "CR1 offset");
_Static_assert(offsetof(I2C_TypeDef, DR) == 0x10U, "DR offset");
_Static_assert(offsetof(I2C_TypeDef, SR1) == 0x14U, "SR1 offset");
_Static_assert(offsetof(I2C_TypeDef, SR2) == 0x18U, "SR2 offset");
_Static_assert(offsetof(I2C_TypeDef, TRISE) == 0x20U, "TRISE offset");
_Static_assert(sizeof(I2C_TypeDef) == 0x24U, "F407 has nine I2C registers, no FLTR");
_Static_assert(I2C_SR1_BTF == 4U && I2C_SR1_AF == 0x400U, "reviewed status masks");
_Static_assert(RCC_APB1ENR_I2C1EN == (1UL << 21), "reviewed clock gate");
_Static_assert(RCC_APB1RSTR_I2C1RST == (1UL << 21), "reviewed reset");

static volatile uint32_t *reg(enum i2c_register name)
{
    switch (name) {
    case I_CR1: return &I2C1->CR1;
    case I_CR2: return &I2C1->CR2;
    case I_OAR1: return &I2C1->OAR1;
    case I_OAR2: return &I2C1->OAR2;
    case I_DR: return &I2C1->DR;
    case I_SR1: return &I2C1->SR1;
    case I_SR2: return &I2C1->SR2;
    case I_CCR: return &I2C1->CCR;
    case I_TRISE: return &I2C1->TRISE;
    }
    return &I2C1->CR1; /* All enum inputs originate in the fixed controller. */
}
static uint32_t mmio_read(void *unused, enum i2c_register name)
{ (void)unused; return *reg(name); }
static void mmio_write(void *unused, enum i2c_register name, uint32_t value)
{ (void)unused; *reg(name) = value; }
static struct i2c_io controller = {mmio_read, mmio_write, NULL, false, true, 0U};
volatile uint32_t controller_configured;

/* Integration entry, intentionally not called by this configuration-only main.
 * Caller must supply independently reviewed wiring/device parameters. The boolean
 * cannot qualify a bus; it only makes the caller's prerequisite explicit.
 */
struct i2c_result application_transmit(uint8_t address, const uint8_t *data,
                                      size_t length, bool wiring_reviewed)
{
    return i2c_transmit(&controller, address, data, length, 100000U, wiring_reviewed);
}

int main(void)
{
    __asm volatile ("cpsid i" ::: "memory");
    struct clock_result clock = clock_sequence(clock_apply, NULL, CLOCK_BUDGET);
    if (clock.completed) {
        RCC->APB1ENR |= RCC_APB1ENR_I2C1EN;
        if (RCC->APB1ENR & RCC_APB1ENR_I2C1EN) {
            RCC->APB1RSTR |= RCC_APB1RSTR_I2C1RST;
            RCC->APB1RSTR &= ~RCC_APB1RSTR_I2C1RST;
            controller_configured = i2c_configure(&controller, 42000000U, true);
        }
    }
    /* No GPIO configuration, PE enable, address, START or transaction occurs. */
    for (;;) __asm volatile ("nop");
}
