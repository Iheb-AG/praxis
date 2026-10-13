Supported operating subset: **EXTI line 0 on PA0**, both-edge USER button notification.
The board signal is active high with an external pull-down; GPIO must select input with
no internal pull. Check the board's SB20 path separately. Route PA0 through
[[peripherals/syscfg]] before unmasking line 0.

| Register | Line-zero behavior | Source |
| --- | --- | --- |
| IMR | bit0=0 masks interrupt request; bit0=1 unmasks | rm_exti_mask:page:386 |
| EMR | bit0 controls events; leave zero for interrupt-only use | rm_exti_mask:page:386 |
| RTSR | bit0=1 enables rising-edge detection | rm_exti_edges:page:387 |
| FTSR | bit0=1 enables falling-edge detection | rm_exti_edges:page:387 |
| SWIER | software event/request action; unused | rm_exti_pending:page:388 |
| PR | bit0 is **write-one-to-clear**; write PR=1, never PR|=1 | rm_exti_pending:page:388 |

Keep line 0 masked while configuring both edge selectors and handler state. Clear the
peripheral pending bit first, then NVIC pending, then configure priority/enable the line.
Restore global interrupts only after all sources are ready. Preserve other lines and
reserved bits. The ISR writes PR=1 and records a timestamp/generation counter; debounce
and press/release policy run outside the ISR. A single edge is not a debounced press.
Require a stable input for nominal 50 ms and a release before another press.

EXTI0_IRQn=6, vector slot 22, handler EXTI0_IRQHandler: `header:EXTI0_IRQn` and the
pinned startup vector. Header MR/IM aliases are explicitly selected as individual MR
bits in this profile; they do not become overlapping independent fields.
See [[peripherals/nvic]], [[peripherals/gpio]], [[schemas/board]] and [[sources]].
