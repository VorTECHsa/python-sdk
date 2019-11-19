#!/usr/bin/env bash
set -e

. venv/bin/activate

gitchangelog

TAG=$(python setup.py --version)

git tag -a $TAG -m "New tag $TAG"
git push --tags

rm -rf dist
pip install wheel
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/*
