#!/bin/sh

mkdir -p ~/.streamlit

cat > ~/.streamlit/config.toml <<EOF
[server]
headless = true
port = ${PORT:-8501}
address = "0.0.0.0"
EOF