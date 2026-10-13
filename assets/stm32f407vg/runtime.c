/* Project Praxis, MIT. Minimal constructor support for the pinned ST startup.
 * This profile has no hosted C runtime, heap, syscalls or exit implementation.
 * Source: ST startup's __libc_init_array call and GNU init-array ABI contract.
 */
typedef void (*initializer)(void);
extern initializer __preinit_array_start[], __preinit_array_end[];
extern initializer __init_array_start[], __init_array_end[];

void __libc_init_array(void)
{
    for (initializer *entry = __preinit_array_start; entry != __preinit_array_end; ++entry) {
        (*entry)();
    }
    for (initializer *entry = __init_array_start; entry != __init_array_end; ++entry) {
        (*entry)();
    }
}
