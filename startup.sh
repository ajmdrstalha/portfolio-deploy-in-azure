#!/usr/bin/env bash
set -euo pipefail

# Azure App Service typically routes traffic to the port your app listens on.
# We'll default to 8000, but allow override via env vars.
PORT="${PORT:-${WEBSITES_PORT:-8000}}"

# Ensure dependencies exist in the active Python environment.
# On App Service, Oryx may create a venv (often named "antenv"); this installs into that env.
python -c "import streamlit" >/dev/null 2>&1 || python -m pip install -r requirements.txt

exec python -m streamlit run app.py \
  --server.address 0.0.0.0 \
  --server.port "$PORT" \
  --server.headless true
