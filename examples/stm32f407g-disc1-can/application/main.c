/* Compile/model-qualified one-shot internal self-test. Not physically qualified.
 * Source-backed CAN facts: actual ingestion MCP, RM0090 Rev22 pp1073-1111.
 * No CAN GPIO alternate functions or external transceiver are configured.
 */
#include "clock_setup.h"
#include "can_controller.h"
#include <stddef.h>

_Static_assert(offsetof(CAN_TypeDef, sTxMailBox[0].TIR) == 0x180U, "TX0 offset");
_Static_assert(offsetof(CAN_TypeDef, sFIFOMailBox[0].RIR) == 0x1B0U, "FIFO0 offset");
_Static_assert(offsetof(CAN_TypeDef, FMR) == 0x200U, "CAN1 filter offset");
_Static_assert(offsetof(CAN_TypeDef, sFilterRegister[0].FR1) == 0x240U, "bank0 offset");
_Static_assert(CAN1_RX0_IRQn == 20 && __NVIC_PRIO_BITS == 4, "IRQ identity");
_Static_assert(RCC_APB1ENR_CAN1EN == (1UL << 25), "CAN1 gate");
_Static_assert(RCC_APB1RSTR_CAN1RST == (1UL << 25), "CAN1 reset");
_Static_assert(42000000U / (6U * (1U + 11U + 2U)) == 500000U, "nominal bitrate");
_Static_assert(CAN_TI0R_STID == (0x7FFUL << 21), "standard identifier placement");

static uint32_t mmio_read(void *unused, enum can_reg reg)
{
    (void)unused;
    switch (reg) {
    case C_MCR: return CAN1->MCR;
    case C_MSR: return CAN1->MSR;
    case C_TSR: return CAN1->TSR;
    case C_RF0: return CAN1->RF0R;
    case C_RF1: return CAN1->RF1R;
    case C_IER: return CAN1->IER;
    case C_ESR: return CAN1->ESR;
    case C_BTR: return CAN1->BTR;
    case C_FMR: return CAN1->FMR;
    case C_FM1: return CAN1->FM1R;
    case C_FS1: return CAN1->FS1R;
    case C_FFA1: return CAN1->FFA1R;
    case C_FA1: return CAN1->FA1R;
    case C_FR1: return CAN1->sFilterRegister[0].FR1;
    case C_FR2: return CAN1->sFilterRegister[0].FR2;
    case C_TIR: return CAN1->sTxMailBox[0].TIR;
    case C_TDTR: return CAN1->sTxMailBox[0].TDTR;
    case C_TDLR: return CAN1->sTxMailBox[0].TDLR;
    case C_TDHR: return CAN1->sTxMailBox[0].TDHR;
    case C_RIR: return CAN1->sFIFOMailBox[0].RIR;
    case C_RDTR: return CAN1->sFIFOMailBox[0].RDTR;
    case C_RDLR: return CAN1->sFIFOMailBox[0].RDLR;
    case C_RDHR: return CAN1->sFIFOMailBox[0].RDHR;
    case C_IRQ_ENABLE: return NVIC->ISER[0];
    case C_IRQ_PRIORITY: return NVIC->IP[20];
    case C_IRQ_ACTIVE: return NVIC->IABR[0];
    default: return UINT32_MAX;
    }
}
static void mmio_write(void *unused, enum can_reg reg, uint32_t value)
{
    (void)unused;
    switch (reg) {
    case C_MCR: CAN1->MCR = value; break;
    case C_TSR: CAN1->TSR = value; break;
    case C_RF0: CAN1->RF0R = value; break;
    case C_IER: CAN1->IER = value; break;
    case C_BTR: CAN1->BTR = value; break;
    case C_FMR: CAN1->FMR = value; break;
    case C_FM1: CAN1->FM1R = value; break;
    case C_FS1: CAN1->FS1R = value; break;
    case C_FFA1: CAN1->FFA1R = value; break;
    case C_FA1: CAN1->FA1R = value; break;
    case C_FR1: CAN1->sFilterRegister[0].FR1 = value; break;
    case C_FR2: CAN1->sFilterRegister[0].FR2 = value; break;
    case C_TIR: CAN1->sTxMailBox[0].TIR = value; break;
    case C_TDTR: CAN1->sTxMailBox[0].TDTR = value; break;
    case C_TDLR: CAN1->sTxMailBox[0].TDLR = value; break;
    case C_TDHR: CAN1->sTxMailBox[0].TDHR = value; break;
    case C_IRQ_ENABLE: NVIC->ISER[0] = value; break;
    case C_IRQ_DISABLE: NVIC->ICER[0] = value; __DSB(); __ISB(); break;
    case C_IRQ_CLEAR: NVIC->ICPR[0] = value; break;
    case C_IRQ_PRIORITY: NVIC->IP[20] = (uint8_t)value; break;
    default: break; /* No RX, ESR, MSR or active-state writes. */
    }
}
static void fence(void *unused) { (void)unused; __DMB(); }
static struct can_io controller = {
    .read = mmio_read, .write = mmio_write, .fence = fence, .reset_required = true
};
/* Debug-visible observations, not the existing UART telemetry ABI. */
volatile uint32_t praxis_can_status = C_STATE, praxis_can_irq_count, praxis_can_received;
volatile uint32_t praxis_can_esr, praxis_can_tsr, praxis_can_rf0;

void CAN1_RX0_IRQHandler(void) { can_fifo0_isr(&controller); }

int main(void)
{
    __disable_irq();
    struct clock_result clock = clock_sequence(clock_apply, NULL, CLOCK_BUDGET);
    enum can_status status = C_STATE;
    if (clock.completed && !(RCC->APB1ENR & (RCC_APB1ENR_CAN1EN | RCC_APB1ENR_CAN2EN))) {
        RCC->APB1ENR |= RCC_APB1ENR_CAN1EN;
        if (RCC->APB1ENR & RCC_APB1ENR_CAN1EN) {
            RCC->APB1RSTR |= RCC_APB1RSTR_CAN1RST;
            RCC->APB1RSTR &= ~RCC_APB1RSTR_CAN1RST;
            status = can_configure(&controller, 42000000U, true, true, 1000000U);
            if (status == C_OK) status = can_arm_fifo0(&controller, true);
            const uint8_t payload[8] = {0x50U, 0x52U, 0x41U, 0x58U, 0x49U, 0x53U, 0x00U, 0xFFU};
            if (status == C_OK) status = can_send_eight(&controller, payload);
            if (status == C_OK) {
                __DMB();
                __enable_irq();
                status = can_finish(&controller, 1000000U);
            }
        }
    }
    __disable_irq();
    praxis_can_status = status;
    praxis_can_irq_count = controller.irq_count;
    praxis_can_received = controller.received;
    praxis_can_esr = controller.last_esr;
    praxis_can_tsr = controller.last_tsr;
    praxis_can_rf0 = controller.last_rf0;
    /* This image has not been flashed. A physical run needs exact-image approval. */
    for (;;) __NOP();
}
