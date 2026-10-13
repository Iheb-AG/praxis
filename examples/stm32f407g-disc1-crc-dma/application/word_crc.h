#ifndef PRAXIS_WORD_CRC_H
#define PRAXIS_WORD_CRC_H

#include <stdint.h>

/* MSB-first, no reflected bytes/final XOR; RM0090 word-feed convention.
 * This portable calculation is not evidence of the target CRC peripheral.
 */
static inline uint32_t praxis_crc_word(uint32_t crc, uint32_t word)
{
    crc ^= word;
    for (unsigned bit = 0U; bit < 32U; ++bit) {
        uint32_t feedback = crc >> 31;
        crc <<= 1;
        if (feedback != 0U) {
            crc ^= 0x04C11DB7UL;
        }
    }
    return crc;
}

#endif
