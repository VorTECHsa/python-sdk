#!/bin/bash

# WARNING: SEMI-AUTOMATED SCRIPT.
echo "This script is not to be run as a whole"
echo "You must instead follow the instructions and run invididual lines in your shell"
exit 1

# Autogenerate the docs
rm -rf mkdocs.yml.backup
mkdir -p ./_build/pydocmd/examples
python docs/autogen.py

# Haven't found a way to do this in a non-convoluted way yet. We need to append google_analytics to our mkdocs file,
# pydocmd doesn't copy google_analytics from the pydocmd file into the mkdocs.yml file, and it also deletes the file
# when pydocmd stops 'serving'.
# To get around this, follow the below:


# Serve the docs locally in a terminal
pydocmd serve

# while the docs are being served, take a backup of the mkdocs.yml file.
cp mkdocs.yml mkdocs.yml.backup

# Now cancel the pydocmd serve process (ctrl+c) to prevent the local docs serving from interfering with the github deploy.

# append to the backed up file
echo "google_analytics: ['UA-153895438-1', 'vortechsa.github.io']" >> mkdocs.yml.backup

# deploy to github pages using our backup file
pydocmd gh-deploy -f ./mkdocs.yml.backup
