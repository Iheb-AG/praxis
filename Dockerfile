# Multi-architecture upstream indexes, resolved 2026-10-13. Refresh deliberately.
ARG PYTHON_IMAGE=python:3.12-slim-bookworm@sha256:34386ef0cb081344d7ec1c103ba398e6e9f64e9ab3a1509accc92a4e24a07258
ARG UV_IMAGE=ghcr.io/astral-sh/uv:0.12.24@sha256:3af4716e991d6956a41e573eab705d0ee08500cd829ed30293eb8472f372c65a
FROM ${UV_IMAGE} AS uv
FROM ${PYTHON_IMAGE} AS builder
COPY --from=uv /uv /usr/local/bin/uv
ENV UV_PYTHON_DOWNLOADS=never UV_NO_CACHE=1
WORKDIR /app
COPY pyproject.toml uv.lock README.md LICENSE ./
COPY praxis ./praxis
# Install a normal wheel, not an editable source-tree link. No ingestion/test extras.
RUN uv sync --locked --no-dev --no-editable --python /usr/local/bin/python

FROM ${PYTHON_IMAGE} AS runtime
LABEL org.opencontainers.image.title="Project Praxis knowledge MCP" \
      org.opencontainers.image.description="Experimental read-only vectorless hardware knowledge server; mount one published bundle" \
      org.opencontainers.image.version="0.1.0" \
      org.opencontainers.image.licenses="MIT"
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/tmp \
    PATH="/app/.venv/bin:${PATH}"
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
COPY LICENSE /usr/share/doc/project-praxis/LICENSE
USER 10001:10001
ENTRYPOINT ["/app/.venv/bin/praxis"]
# /bundle must be explicitly mounted by the client; no board is silently selected.
CMD ["serve", "--bundle", "/bundle"]
