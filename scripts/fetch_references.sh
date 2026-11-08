#!/usr/bin/env sh
set -eu
cd "$(dirname "$0")/.."
exec python scripts/fetch_references.py "$@"
