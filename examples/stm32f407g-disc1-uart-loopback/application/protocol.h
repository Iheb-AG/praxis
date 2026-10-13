#ifndef PRAXIS_LOOPBACK_PROTOCOL_H
#define PRAXIS_LOOPBACK_PROTOCOL_H
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#define FRAME_SIZE 19U
uint16_t frame_crc(const uint8_t *data, size_t length);
void frame_make(uint8_t frame[FRAME_SIZE], uint32_t sequence);
bool frame_valid(const uint8_t frame[FRAME_SIZE], uint32_t sequence);
#endif
