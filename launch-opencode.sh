#!/usr/bin/env bash
# Launch a fresh local OpenCode instance with the checked-in Praxis selection.
set -euo pipefail

praxis_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
praxis_config="$praxis_root/temp/opencode.json"

if ! command -v opencode >/dev/null 2>&1; then
    echo "OpenCode is not on PATH. Run this launcher from the terminal where opencode works." >&2
    exit 127
fi

# Inline config takes precedence over normal global and project configuration.
# Keep the custom path explicit too, for clients that load configuration by path.
export OPENCODE_CONFIG="$praxis_config"
export OPENCODE_CONFIG_CONTENT="$(cat -- "$praxis_config")"
cd -- "$praxis_root/temp"
exec opencode
