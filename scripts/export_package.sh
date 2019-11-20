#!/usr/bin/env bash
set -e

# Generate changelog
sudo gem install github_changelog_generator
github_changelog_generator -u V0RT3X4 -p python-sdk

# Tag the current commit
TAG=$(python setup.py --version)

git add CHANGELOG.md
git add setup.py

git commit -m "New tag $TAG"
git push

git tag -a $TAG -m "New tag $TAG"
git push --tags

# Push new version to pypi
. venv/bin/activate
rm -rf dist
pip install wheel
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/*
