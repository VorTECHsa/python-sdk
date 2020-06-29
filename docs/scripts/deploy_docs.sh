#!/bin/bash

rm -rf mkdocs.yml.backup
mkdir -p ./_build/pydocmd/examples
python docs/autogen.py

# Haven't found a way to do this in a non-convoluted way yet. We need to append google_analytics to our mkdocs file,
# pydocmd doesn't copy google_analytics from the pydocmd file into the mkdocs.yml file, and it also deletes the file
# when pydocmd stops 'serving'.
# To get around this we:

# Kill the old process on port 8000 if it exists
process_on_our_port=$(sudo lsof -t -i:8000)
if [[ $process_on_our_port ]]; then
  sudo kill $process_on_our_port
fi

#   1. serve the docs locally
pydocmd serve & sleep 5

#   2. backup the generated mkdocs.yml file
cp mkdocs.yml mkdocs.yml.backup

#   3. append to the backed up file
echo "google_analytics: ['UA-153895438-1', 'vortechsa.github.io']" >> mkdocs.yml.backup

#   4. deploy to github pages using our backup file
pydocmd gh-deploy -f ./mkdocs.yml.backup
