/* Host register model only. Real target tests compile the pinned vendor header. */
#ifndef PRAXIS_STM32_MODEL_H
#define PRAXIS_STM32_MODEL_H
#include <stdint.h>
#include <assert.h>
typedef struct {
    volatile uint32_t CR, PLLCFGR, CFGR, CIR, AHB1RSTR, AHB2RSTR, RESERVED0[2];
    volatile uint32_t APB1RSTR, APB2RSTR, RESERVED1[2], AHB1ENR, AHB2ENR, RESERVED2[2], APB1ENR;
} RCC_TypeDef;
typedef struct {
    volatile uint32_t MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR, LCKR, AFR[2];
} GPIO_TypeDef;
typedef struct { volatile uint32_t SR, DR, BRR, CR1, CR2, CR3, GTPR; } USART_TypeDef;
extern RCC_TypeDef fixture_rcc;
extern GPIO_TypeDef fixture_gpio;
extern USART_TypeDef fixture_usart;
extern uint32_t fixture_primask;
extern unsigned fixture_irq_enabled;
extern unsigned fixture_priority;
#define RCC (&fixture_rcc)
#define GPIOA (&fixture_gpio)
#define USART2 (&fixture_usart)
#define RCC_CR_HSION (1UL << 0)
#define RCC_CR_HSIRDY (1UL << 1)
#define RCC_CFGR_SW 0x3UL
#define RCC_CFGR_SWS 0xCUL
#define RCC_CFGR_HPRE 0xF0UL
#define RCC_CFGR_PPRE1 0x1C00UL
#define RCC_CFGR_PPRE2 0xE000UL
#define RCC_AHB1ENR_GPIOAEN 1UL
#define RCC_APB1ENR_USART2EN (1UL << 17)
#define RCC_APB1RSTR_USART2RST (1UL << 17)
#define USART_CR1_UE (1UL << 13)
#define USART_CR1_TE (1UL << 3)
#define USART_CR1_RE (1UL << 2)
#define USART_CR1_RXNEIE (1UL << 5)
#define USART_SR_RXNE (1UL << 5)
#define USART_SR_TXE (1UL << 7)
#define USART_SR_ORE (1UL << 3)
#define USART_SR_NE (1UL << 2)
#define USART_SR_FE (1UL << 1)
#define USART_SR_PE (1UL << 0)
enum { USART2_IRQn = 38 };
static inline uint32_t __get_PRIMASK(void) { return fixture_primask; }
static inline void __disable_irq(void) { fixture_primask = 1; }
static inline void __set_PRIMASK(uint32_t value) { fixture_primask = value; }
static inline void NVIC_DisableIRQ(int irq) { assert(irq == 38); fixture_irq_enabled = 0; }
static inline void NVIC_SetPriority(int irq, unsigned priority) { assert(irq == 38); fixture_priority = priority; }
static inline void NVIC_ClearPendingIRQ(int irq) { assert(irq == 38); }
static inline void NVIC_EnableIRQ(int irq) {
    assert(irq == 38);
    assert(fixture_primask == 1);
    assert((USART2->CR1 & USART_CR1_RXNEIE) != 0);
    assert(USART2->BRR == 139);
    assert(((GPIOA->AFR[0] >> 8) & 0xFF) == 0x77);
    fixture_irq_enabled = 1;
}
#endif

