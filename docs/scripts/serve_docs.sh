#!/bin/bash
set -e

. venv/bin/activate
rm -rf ./_build
mkdir -p ./_build/pydocmd/examples
mkdir -p ./_build/pydocmd/css
cp -r docs/css/* ./_build/pydocmd/css/
python docs/autogen.py
pydocmd serve
