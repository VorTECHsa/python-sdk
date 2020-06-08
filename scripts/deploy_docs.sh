#!/bin/bash

mkdir -p ./_build/pydocmd/examples
python docs/autogen.py
pydocmd serve & sleep 5
cp mkdocs.yml mkdocs.yml.backup
echo "google_analytics: ['UA-153895438-1', 'vortechsa.github.io']" >> mkdocs.yml.backup
pydocmd gh-deploy -f /Users/kit/Development/git_repositories/python-sdk/mkdocs.yml.backup
