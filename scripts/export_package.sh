#!/usr/bin/env bash
set -e

# Tag the current commit
TAG=$(python setup.py --version)

# Add the new version to src control and push directly to master
git add ./vortexasdk/version.py
git commit -m "chore: New tag $TAG"
git push

# Tag this version
git tag -a $TAG -m "chore: New tag $TAG"
git push --tags


# Generate changelog
gem install github_changelog_generator
github_changelog_generator -u vortechsa -p python-sdk -t $GITHUB_CHANGELOG_TOKEN
git add CHANGELOG.md
git commit -m "docs: Update changelog with tag $TAG"
git push


# Generate distribution package and export to pypi
. venv/bin/activate
rm -rf dist
pip install wheel
python3 setup.py sdist bdist_wheel
pip install twine
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/*

# Read the following script for instructions on how to deploy docs.
#./docs/scripts/deploy_docs.sh
