"""Explicit extraction configuration, separate from firmware/hardware qualification."""

from praxis.compatibility import qualified_target
from praxis.errors import PraxisError


def cmsis_cpu(target):
    if target.knowledge_adapter is not None:
        return target.knowledge_adapter.cpu
    return qualified_target(target)["cpu"]


def check_header_identity(target, definitions):
    required = (target.knowledge_adapter.header_identity if target.knowledge_adapter is not None
                else qualified_target(target)["header_identity"])
    missing = sorted(set(required) - definitions.keys())
    if missing:
        raise PraxisError("TARGET_MISMATCH", f"Header identity does not match selected target; missing {missing}")


def require_firmware_target(target):
    if target.knowledge_adapter is not None or qualified_target(target) is None:
        raise PraxisError("UNSUPPORTED_FIRMWARE_TARGET",
                          "This target has knowledge extraction only. Add independently reviewed "
                          "compiler, headers, startup/linker and hardware profiles before verification or flashing.")
