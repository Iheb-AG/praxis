#ifndef LED_BUTTON_H
#define LED_BUTTON_H

#include <stdint.h>
#include <stm32f407xx.h>

void system_clock_hsi_init(void);
void systick_init_1ms(void);
void gpio_led_button_init(void);
void led_a_toggle(void);
void led_a_set(uint32_t state);
void led_b_set(uint32_t state);
uint32_t button_read(void);
uint32_t millis(void);

#endif