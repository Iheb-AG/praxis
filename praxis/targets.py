"""Explicit extraction configuration, separate from firmware/hardware qualification."""

from praxis.errors import PraxisError


def cmsis_cpu(target):
    return target.knowledge_adapter.cpu if target.knowledge_adapter is not None else "cortex-m4"


def check_header_identity(target, definitions):
    guards = {"STM32F401RE": "__STM32F401xE_H", "STM32F407VGT6": "__STM32F407xx_H"}
    required = (target.knowledge_adapter.header_identity if target.knowledge_adapter is not None
                else [guards[target.mcu]] if target.family == "stm32" else [])
    missing = sorted(set(required) - definitions.keys())
    if missing:
        raise PraxisError("TARGET_MISMATCH", f"Header identity does not match selected target; missing {missing}")


def require_firmware_target(target):
    if target.knowledge_adapter is not None or target.family not in ("stm32", "avr"):
        raise PraxisError("UNSUPPORTED_FIRMWARE_TARGET",
                          "This target has knowledge extraction only. Add independently reviewed "
                          "compiler, headers, startup/linker and hardware profiles before verification or flashing.")
