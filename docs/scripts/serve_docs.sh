#!/bin/bash
set -e

. venv/bin/activate
rm -rf ./_build
mkdir -p ./_build/pydocmd/examples
python docs/autogen.py
mkdocs serve
