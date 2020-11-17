#!/bin/bash

rm -rf mkdocs.yml.backup
mkdir -p ./_build/pydocmd/examples
python docs/autogen.py

# Haven't found a way to do this in a non-convoluted way yet. We need to append google_analytics to our mkdocs file,
# pydocmd doesn't copy google_analytics from the pydocmd file into the mkdocs.yml file, and it also deletes the file
# when pydocmd stops 'serving'.
# To get around this we:

