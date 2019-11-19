#!/usr/bin/env bash
set -e

. venv/bin/activate

sudo gem install github_changelog_generator
github_changelog_generator -u V0RT3X4 -p python-sdk

TAG=$(python setup.py --version)

git tag -a $TAG -m "New tag $TAG"
git push --tags

rm -rf dist
pip install wheel
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/*
