/* Pure software publication model: no target peripheral access. */
#include <stdio.h>
#include "telemetry.h"
static volatile PraxisCanTelemetry source, output;
static unsigned fences, failures;
static void barrier(void)
{
    if (!(output.generation & 1U)) ++failures;
    if (fences & 1U) {
#define VERIFY(name) if (source.name != output.name) ++failures;
        PRAXIS_CAN_FIELDS(VERIFY)
#undef VERIFY
    }
    ++fences;
}
int main(void)
{
    source.generation = 999U; /* Must never overwrite publisher generation. */
    source.magic = PRAXIS_CAN_MAGIC;
    source.abi = PRAXIS_CAN_ABI;
    source.size_bytes = sizeof(PraxisCanTelemetry);
    source.publications = 1U;
    can_telemetry_publish(&output, &source, barrier);
    if (output.generation != 2U) ++failures;
    output.generation = 0xFFFFFFFEU;
    source.publications = 2U;
    can_telemetry_publish(&output, &source, barrier);
    if (output.generation != 0U || fences != 4U) ++failures;
    printf("{\"failures\":%u,\"fences\":%u,\"words\":[%u", failures, fences, output.generation);
#define PRINT(name) printf(",%u", output.name);
    PRAXIS_CAN_FIELDS(PRINT)
#undef PRINT
    puts("]}");
    return failures ? 1 : 0;
}
