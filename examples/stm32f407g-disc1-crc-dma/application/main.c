/* Compile-only feature smoke example, not flashed or hardware-qualified.
 * Facts retrieved through Praxis knowledge MCP, bundle bd8b793388df...:
 * crc: rm_features_113..115; dma/dma_stream: rm_features_306,324..336;
 * rcc: rm_features_243..244. No guessed board pins or PLL initialization.
 * Startup/linker/system files are supplied by the matching build MCP.
 */
#include <stdint.h>
#include <stm32f407xx.h>
#include "word_crc.h"

_Static_assert(sizeof(uint32_t) == 4U, "32-bit register access required");
_Static_assert(RCC_AHB1ENR_CRCEN == (1UL << 12), "reviewed CRC gate");
_Static_assert(RCC_AHB1ENR_DMA2EN == (1UL << 22), "reviewed DMA2 gate");
_Static_assert(DMA_SxCR_DIR_1 == (2UL << 6), "memory-to-memory direction");
_Static_assert(DMA_SxFCR_DMDIS == 4UL, "FIFO required");

#define WORDS 16U
#define POLL_BUDGET 1000000UL /* Iteration bound, not a timing guarantee. */
#define STREAM0_CLEAR (DMA_LIFCR_CFEIF0 | DMA_LIFCR_CDMEIF0 | \
                      DMA_LIFCR_CTEIF0 | DMA_LIFCR_CHTIF0 | DMA_LIFCR_CTCIF0)
#define STREAM0_ERRORS (DMA_LISR_FEIF0 | DMA_LISR_DMEIF0 | DMA_LISR_TEIF0)

/* The pinned linker places these in main SRAM, not CCM. DMA reachability must
 * be independently reviewed before a hardware qualification of this example.
 */
static uint32_t source_words[WORDS];
static uint32_t destination_words[WORDS];

typedef struct {
    uint32_t done;
    uint32_t failed_stage;
    uint32_t hardware_crc;
    uint32_t software_crc;
    uint32_t dma_status;
    uint32_t copied_words;
    uint32_t disable_acknowledged;
    uint32_t crc_matches;
} feature_result;

/* This is not the UART telemetry ABI. The UART tool cannot read it. */
volatile feature_result praxis_feature_smoke;

static int disable_stream(void)
{
    DMA2_Stream0->CR &= ~DMA_SxCR_EN;
    for (uint32_t budget = POLL_BUDGET; budget != 0U; --budget) {
        if ((DMA2_Stream0->CR & DMA_SxCR_EN) == 0U) {
            praxis_feature_smoke.disable_acknowledged = 1U;
            return 1;
        }
    }
    return 0;
}

static int copy_words(void)
{
    if (!disable_stream()) {
        praxis_feature_smoke.failed_stage = 1U;
        return 0;
    }
    DMA2->LIFCR = STREAM0_CLEAR; /* W1C, never read-modify-write. */
    DMA2_Stream0->PAR = (uint32_t)(uintptr_t)source_words;
    DMA2_Stream0->M0AR = (uint32_t)(uintptr_t)destination_words;
    DMA2_Stream0->NDTR = WORDS;
    DMA2_Stream0->CR = DMA_SxCR_DIR_1 | DMA_SxCR_PINC | DMA_SxCR_MINC |
                      DMA_SxCR_PSIZE_1 | DMA_SxCR_MSIZE_1;
    /* FIFO quarter threshold, single word bursts, no circular/direct/DBM. */
    DMA2_Stream0->FCR = DMA_SxFCR_DMDIS;
    __DMB();
    DMA2_Stream0->CR |= DMA_SxCR_EN; /* Enable last. */
    int complete = 0;
    for (uint32_t budget = POLL_BUDGET; budget != 0U; --budget) {
        uint32_t status = DMA2->LISR;
        praxis_feature_smoke.dma_status = status;
        if ((status & STREAM0_ERRORS) != 0U) {
            praxis_feature_smoke.failed_stage = 2U;
            break;
        }
        if ((status & DMA_LISR_TCIF0) != 0U) {
            complete = 1;
            break;
        }
    }
    if (!complete && praxis_feature_smoke.failed_stage == 0U) {
        praxis_feature_smoke.failed_stage = 3U;
    }
    if (!disable_stream()) {
        praxis_feature_smoke.failed_stage = 4U;
        return 0;
    }
    DMA2->LIFCR = STREAM0_CLEAR;
    __DMB();
    return complete;
}

int main(void)
{
    /* Keep the build assets' documented reset-HSI startup; no PLL assumption. */
    RCC->AHB1ENR |= RCC_AHB1ENR_CRCEN | RCC_AHB1ENR_DMA2EN;
    (void)RCC->AHB1ENR;
    for (uint32_t i = 0U; i < WORDS; ++i) {
        source_words[i] = 0x12345678UL ^ (i * 0x1020304UL);
        destination_words[i] = 0U;
    }
    uint32_t reference = 0xFFFFFFFFUL;
    CRC->CR = CRC_CR_RESET;
    for (uint32_t i = 0U; i < WORDS; ++i) {
        CRC->DR = source_words[i];
        reference = praxis_crc_word(reference, source_words[i]);
    }
    praxis_feature_smoke.hardware_crc = CRC->DR;
    praxis_feature_smoke.software_crc = reference;
    praxis_feature_smoke.crc_matches = CRC->DR == reference;
    if (!praxis_feature_smoke.crc_matches) {
        praxis_feature_smoke.failed_stage = 5U;
    } else if (copy_words()) {
        for (uint32_t i = 0U; i < WORDS; ++i) {
            if (destination_words[i] != source_words[i]) {
                praxis_feature_smoke.failed_stage = 6U;
                break;
            }
            ++praxis_feature_smoke.copied_words;
        }
    }
    praxis_feature_smoke.done = 1U;
    for (;;) {
        __NOP();
    }
}
