# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install the project into /app
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Copy the project definition
# (we only need pyproject.toml and uv.lock to install dependencies)
COPY pyproject.toml uv.lock ./

# Install the project's dependencies using the lockfile and settings
RUN uv sync --frozen --no-install-project --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Copy the project source code
COPY . .

# Install the project itself (if needed, or just ensures venv is consistent)
RUN uv sync --frozen --no-dev

# Expose the port used by NiceGUI
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]
