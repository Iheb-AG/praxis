#include "protocol.h"

uint16_t frame_crc(const uint8_t *data, size_t length)
{
    uint16_t crc = 0xFFFFU;
    for (size_t i = 0; i < length; ++i) {
        crc ^= (uint16_t)((uint16_t)data[i] << 8);
        for (unsigned bit = 0; bit < 8U; ++bit)
            crc = (uint16_t)((crc & 0x8000U) ? ((uint32_t)crc << 1) ^ 0x1021U : (uint32_t)crc << 1);
    }
    return crc;
}

void frame_make(uint8_t frame[FRAME_SIZE], uint32_t sequence)
{
    frame[0] = 0xA5U; frame[1] = 0x5AU;
    frame[2] = 1U; frame[3] = 1U;
    for (unsigned i = 0; i < 4U; ++i) frame[4U+i] = (uint8_t)(sequence >> (8U*i));
    frame[8] = 8U;
    for (unsigned i = 0; i < 8U; ++i)
        frame[9U+i] = (uint8_t)((sequence >> (8U*(i % 4U))) ^ (0x31U + 17U*i));
    const uint16_t crc = frame_crc(frame+2U, 15U);
    frame[17] = (uint8_t)(crc >> 8); frame[18] = (uint8_t)crc;
}

bool frame_valid(const uint8_t frame[FRAME_SIZE], uint32_t sequence)
{
    uint8_t expected[FRAME_SIZE];
    frame_make(expected, sequence);
    /* Compare framing, payload, sequence and CRC, not CRC alone. */
    for (unsigned i = 0; i < FRAME_SIZE; ++i)
        if (expected[i] != frame[i]) return false;
    return true;
}
