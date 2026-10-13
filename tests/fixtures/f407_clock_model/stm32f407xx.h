/* Limited host register model for the reviewed LED/button fixture, not silicon simulation.
 * Register fields/masks: pinned ST stm32f407xx.h in assets/stm32f407vg/include.
 */
#ifndef PRAXIS_CLOCK_MODEL_H
#define PRAXIS_CLOCK_MODEL_H
#include <stdint.h>
#include <stdbool.h>
typedef struct { volatile uint32_t CR, CFGR, AHB1ENR; } RCC_TypeDef;
typedef struct { volatile uint32_t MODER, OTYPER, OSPEEDR, PUPDR, IDR, ODR, BSRR; } GPIO_TypeDef;
extern RCC_TypeDef model_rcc;
extern GPIO_TypeDef model_gpioa, model_gpiod;
extern uint32_t SystemCoreClock;
#define RCC (&model_rcc)
#define GPIOA (&model_gpioa)
#define GPIOD (&model_gpiod)
#define RCC_CR_HSION (1U << 0)
#define RCC_CR_HSIRDY (1U << 1)
#define RCC_CR_PLLON (1U << 24)
#define RCC_CR_PLLRDY (1U << 25)
#define RCC_CFGR_SW 3U
#define RCC_CFGR_HPRE (15U << 4)
#define RCC_CFGR_SWS (3U << 2)
#define RCC_AHB1ENR_GPIOAEN (1U << 0)
#define RCC_AHB1ENR_GPIODEN (1U << 3)
#define GPIO_MODER_MODER0 3U
#define GPIO_MODER_MODER12 (3U << 24)
#define GPIO_MODER_MODER13 (3U << 26)
#define GPIO_MODER_MODER12_Pos 24U
#define GPIO_MODER_MODER13_Pos 26U
#define GPIO_OTYPER_OT12 (1U << 12)
#define GPIO_OTYPER_OT13 (1U << 13)
#define GPIO_OSPEEDR_OSPEED12 (3U << 24)
#define GPIO_OSPEEDR_OSPEED13 (3U << 26)
#define GPIO_OSPEEDR_OSPEED12_Pos 24U
#define GPIO_OSPEEDR_OSPEED13_Pos 26U
#define GPIO_PUPDR_PUPD0 3U
#define GPIO_PUPDR_PUPD12 (3U << 24)
#define GPIO_PUPDR_PUPD13 (3U << 26)
void SystemCoreClockUpdate(void);
uint32_t SysTick_Config(uint32_t ticks);
void model_nop(void);
void model_irq(bool enabled);
#define __disable_irq() model_irq(false)
#define __enable_irq() model_irq(true)
#define __NOP() model_nop()
#endif
