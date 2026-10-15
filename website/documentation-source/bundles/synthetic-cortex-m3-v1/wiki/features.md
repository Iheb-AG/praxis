# Target feature support

Recognized register blocks, declared instances and explicitly reviewed modes; not an exhaustive inventory of every instruction, boot mode or operating combination.

**Complete MCU feature support is not established.**

| Entity | Declared instances | Reviewed modes and scope | Ready mode workflows | Declaration status | Provenance |
| --- | --- | --- | --- | --- | --- |
| clock | CLOCK0 | none | none | declarations_only | vendor_blocks:CLOCK_Type |
| interrupts | IRQCTRL0 | none | none | declarations_only | vendor_blocks:IRQCTRL_Type |
| pins | PINMUX0 | none | none | declarations_only | vendor_blocks:PINMUX_Type |
| uart | UART0 | none | none | declarations_only | vendor_blocks:UART_Type |

See [[index]], [[coverage]] and [[sources]].

## Machine-readable report

```json
{"all_features_supported":false,"counts":{"blocks_without_mode_contracts":4,"declared_instances":4,"register_blocks":4,"reviewed_mode_contracts":0},"features":{"clock":{"build_qualification":"separate artifact evidence required","declaration_status":"declarations_only","declared_instances":["CLOCK0"],"hardware_qualification":"separate workflow evidence required","issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"missing":["No explicit reviewed operating-mode contract"],"mode_scoped_workflows":[],"physical_package_availability":"not established by register declarations","published":true,"reviewed_modes":{},"source":"vendor_blocks:CLOCK_Type"},"interrupts":{"build_qualification":"separate artifact evidence required","declaration_status":"declarations_only","declared_instances":["IRQCTRL0"],"hardware_qualification":"separate workflow evidence required","issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"missing":["No explicit reviewed operating-mode contract"],"mode_scoped_workflows":[],"physical_package_availability":"not established by register declarations","published":true,"reviewed_modes":{},"source":"vendor_blocks:IRQCTRL_Type"},"pins":{"build_qualification":"separate artifact evidence required","declaration_status":"declarations_only","declared_instances":["PINMUX0"],"hardware_qualification":"separate workflow evidence required","issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"missing":["No explicit reviewed operating-mode contract"],"mode_scoped_workflows":[],"physical_package_availability":"not established by register declarations","published":true,"reviewed_modes":{},"source":"vendor_blocks:PINMUX_Type"},"uart":{"build_qualification":"separate artifact evidence required","declaration_status":"declarations_only","declared_instances":["UART0"],"hardware_qualification":"separate workflow evidence required","issues":["Enclosing masks represent contained aliases; absent masks remain unasserted."],"missing":["No explicit reviewed operating-mode contract"],"mode_scoped_workflows":[],"physical_package_availability":"not established by register declarations","published":true,"reviewed_modes":{},"source":"vendor_blocks:UART_Type"}},"format":"praxis-features-v1","limits":["Register instances do not establish package pins or board connectivity.","A reviewed mode is not a compiler check or a hardware qualification.","Capability absence in this inventory does not establish silicon absence."],"scope":"Recognized register blocks, declared instances and explicitly reviewed modes; not an exhaustive inventory of every instruction, boot mode or operating combination.","target":"synthetic_cortex_m3"}
```
