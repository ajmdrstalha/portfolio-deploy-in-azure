#!/usr/bin/env bash
set -euo pipefail

PORT="${PORT:-${WEBSITES_PORT:-8000}}"

echo "Starting Streamlit"
echo "- Working dir: $(pwd)"
echo "- Port: ${PORT}"
python --version

# In Azure App Service, dependencies are usually installed during build.
# If they aren't (misconfiguration), fall back to installing at startup.
python -c "import streamlit" >/dev/null 2>&1 || python -m pip install --no-cache-dir -r requirements.txt

exec python -m streamlit run app.py \
	--server.address 0.0.0.0 \
	--server.port "${PORT}" \
	--server.headless true \
	--server.enableCORS false \
	--server.enableXsrfProtection false