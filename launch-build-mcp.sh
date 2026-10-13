#!/usr/bin/env bash
# OpenCode starts this child process; stdout is exclusively the MCP transport.
set -euo pipefail
praxis_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$praxis_root/.praxis-output/podman-env.sh" ]]; then
    source "$praxis_root/.praxis-output/podman-env.sh"
fi
praxis_options=()
if [[ -f "$praxis_root/.praxis-output/hardware-profile.json" ]]; then
    praxis_options+=(--hardware-profile "$praxis_root/.praxis-output/hardware-profile.json")
fi
# Explicit operator opt-in only; never enable programming merely because a grant file exists.
if [[ -n "${PRAXIS_HARDWARE_AUTHORIZATION:-}" ]]; then
    praxis_options+=(--hardware-authorization "$PRAXIS_HARDWARE_AUTHORIZATION")
fi
exec "$praxis_root/.venv/bin/praxis" build-serve \
    --bundle "$praxis_root/bundles/stm32f407g-disc1-e01-m1" \
    --assets "$praxis_root/assets/stm32f407vg" \
    --workspace "$praxis_root/temp" \
    --artifacts "$praxis_root/.praxis-output/firmware-artifacts" \
    --lock "$praxis_root/toolchain-f407.lock.json" "${praxis_options[@]}"
